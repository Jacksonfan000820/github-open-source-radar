#!/usr/bin/env python3
"""Discover popular open-source GitHub repositories and publish a snapshot."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable


API_URL = "https://api.github.com/search/repositories"
API_VERSION = "2022-11-28"
README_START = "<!-- RADAR:START -->"
README_END = "<!-- RADAR:END -->"
SHANGHAI = timezone(timedelta(hours=8), name="Asia/Shanghai")


class RadarError(RuntimeError):
    """A user-facing scan or validation failure."""


@dataclass(frozen=True)
class QueryRule:
    key: str
    title: str
    query: str
    sort: str
    order: str


@dataclass(frozen=True)
class RadarConfig:
    candidate_limit: int
    report_limit: int
    exclude_without_license: bool
    queries: tuple[QueryRule, ...]


class GitHubClient:
    """Small REST client with bounded retries for transient failures."""

    def __init__(
        self,
        token: str | None = None,
        *,
        timeout: float = 20.0,
        max_attempts: int = 3,
        opener: Callable[..., Any] = urllib.request.urlopen,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        self.token = token
        self.timeout = timeout
        self.max_attempts = max(1, max_attempts)
        self.opener = opener
        self.sleeper = sleeper

    def search_repositories(
        self, query: str, *, sort: str, order: str, limit: int
    ) -> list[dict[str, Any]]:
        params = urllib.parse.urlencode(
            {
                "q": query,
                "sort": sort,
                "order": order,
                "per_page": limit,
                "page": 1,
            }
        )
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "github-open-source-radar",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(f"{API_URL}?{params}", headers=headers)

        for attempt in range(1, self.max_attempts + 1):
            try:
                with self.opener(request, timeout=self.timeout) as response:
                    raw = response.read()
                payload = json.loads(raw.decode("utf-8"))
                return _validate_search_payload(payload)
            except urllib.error.HTTPError as exc:
                retryable = exc.code == 429 or 500 <= exc.code <= 599
                if retryable and attempt < self.max_attempts:
                    self.sleeper(_retry_delay(exc.headers, attempt))
                    continue
                raise RadarError(f"GitHub API HTTP {exc.code} for query: {query}") from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                raise RadarError(f"GitHub API network failure for query: {query}: {exc}") from exc
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise RadarError(f"GitHub API returned invalid JSON for query: {query}") from exc

        raise RadarError(f"GitHub API retry budget exhausted for query: {query}")


def _retry_delay(headers: Any, attempt: int) -> float:
    if headers is not None:
        retry_after = headers.get("Retry-After")
        if retry_after:
            try:
                return min(max(float(retry_after), 0.0), 30.0)
            except ValueError:
                pass
    return min(float(2 ** (attempt - 1)), 8.0)


def _validate_search_payload(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
        raise RadarError("GitHub API response is missing the items list")
    if payload.get("incomplete_results") is True:
        raise RadarError("GitHub API returned incomplete search results")
    if not all(isinstance(item, dict) for item in payload["items"]):
        raise RadarError("GitHub API returned a non-object repository item")
    return payload["items"]


def load_config(path: Path) -> RadarConfig:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RadarError(f"Cannot read valid config JSON: {path}") from exc
    if not isinstance(raw, dict):
        raise RadarError("Config root must be an object")

    candidate_limit = raw.get("candidate_limit")
    report_limit = raw.get("report_limit")
    exclude_without_license = raw.get("exclude_without_license")
    query_items = raw.get("queries")
    if not isinstance(candidate_limit, int) or not 1 <= candidate_limit <= 100:
        raise RadarError("candidate_limit must be an integer from 1 to 100")
    if not isinstance(report_limit, int) or not 1 <= report_limit <= candidate_limit:
        raise RadarError("report_limit must be between 1 and candidate_limit")
    if not isinstance(exclude_without_license, bool):
        raise RadarError("exclude_without_license must be a boolean")
    if not isinstance(query_items, list) or not query_items:
        raise RadarError("queries must be a non-empty list")

    rules: list[QueryRule] = []
    seen_keys: set[str] = set()
    for item in query_items:
        if not isinstance(item, dict):
            raise RadarError("Each query must be an object")
        values = {name: item.get(name) for name in ("key", "title", "query", "sort", "order")}
        if not all(isinstance(value, str) and value.strip() for value in values.values()):
            raise RadarError("Each query requires non-empty key, title, query, sort, and order")
        if values["key"] in seen_keys:
            raise RadarError(f"Duplicate query key: {values['key']}")
        if values["order"] not in {"asc", "desc"}:
            raise RadarError(f"Invalid query order: {values['order']}")
        seen_keys.add(values["key"])
        rules.append(QueryRule(**values))

    return RadarConfig(
        candidate_limit=candidate_limit,
        report_limit=report_limit,
        exclude_without_license=exclude_without_license,
        queries=tuple(rules),
    )


def expand_query(template: str, now: datetime) -> str:
    dates = {
        "date_30d": (now - timedelta(days=30)).date().isoformat(),
        "date_7d": (now - timedelta(days=7)).date().isoformat(),
    }
    try:
        return template.format(**dates)
    except (KeyError, ValueError) as exc:
        raise RadarError(f"Invalid query date placeholder in: {template}") from exc


def load_previous(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RadarError(f"Previous snapshot is not valid JSON: {path}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("repositories"), list):
        raise RadarError("Previous snapshot has an invalid repositories collection")
    for repo in payload["repositories"]:
        if not isinstance(repo, dict) or not isinstance(repo.get("id"), int):
            raise RadarError("Previous snapshot contains an invalid repository")
        if not isinstance(repo.get("stars"), int):
            raise RadarError("Previous snapshot contains an invalid star count")
    return payload


def validate_readme(text: str) -> None:
    if text.count(README_START) != 1 or text.count(README_END) != 1:
        raise RadarError("README must contain exactly one RADAR start and end marker")
    if text.index(README_START) >= text.index(README_END):
        raise RadarError("README RADAR markers are in the wrong order")


def _license_id(item: dict[str, Any]) -> str | None:
    license_info = item.get("license")
    if not isinstance(license_info, dict):
        return None
    value = license_info.get("spdx_id") or license_info.get("key")
    if not isinstance(value, str) or value.strip().upper() in {"", "NOASSERTION"}:
        return None
    return value.strip()


def _validate_repository_item(item: dict[str, Any]) -> None:
    required = {
        "id": int,
        "full_name": str,
        "html_url": str,
        "stargazers_count": int,
        "forks_count": int,
        "open_issues_count": int,
        "created_at": str,
        "pushed_at": str,
    }
    for key, expected_type in required.items():
        value = item.get(key)
        if type(value) is not expected_type:
            raise RadarError(f"Repository item has invalid {key}")
    for key in ("fork", "archived", "disabled", "private"):
        if type(item.get(key)) is not bool:
            raise RadarError(f"Repository item has invalid {key}")
    if item["id"] <= 0:
        raise RadarError("Repository item has invalid id")
    for key in ("stargazers_count", "forks_count", "open_issues_count"):
        if item[key] < 0:
            raise RadarError(f"Repository item has invalid {key}")
    if not re.fullmatch(r"[A-Za-z0-9-]{1,39}/[A-Za-z0-9._-]{1,100}", item["full_name"]):
        raise RadarError("Repository item has invalid full_name")
    parsed_url = urllib.parse.urlsplit(item["html_url"])
    if (
        parsed_url.scheme != "https"
        or parsed_url.netloc.casefold() != "github.com"
        or parsed_url.path != f"/{item['full_name']}"
        or parsed_url.query
        or parsed_url.fragment
    ):
        raise RadarError("Repository item has invalid html_url")


def _excluded(item: dict[str, Any], require_license: bool) -> tuple[bool, str | None]:
    _validate_repository_item(item)
    if item.get("fork") is True:
        return True, "fork"
    if item.get("archived") is True:
        return True, "archived"
    if item.get("disabled") is True:
        return True, "disabled"
    if item.get("private") is True:
        return True, "private"
    if require_license and _license_id(item) is None:
        return True, "license"
    return False, None


def _normalize_repository(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "name_with_owner": item["full_name"],
        "url": f"https://github.com/{item['full_name']}",
        "description": item.get("description") if isinstance(item.get("description"), str) else "",
        "language": item.get("language") if isinstance(item.get("language"), str) else "",
        "license": _license_id(item) or "",
        "stars": item["stargazers_count"],
        "forks": item["forks_count"],
        "open_issues": item["open_issues_count"],
        "created_at": item["created_at"],
        "pushed_at": item["pushed_at"],
        "star_delta": None,
        "categories": [],
    }


def build_snapshot(
    config: RadarConfig,
    client: Any,
    previous: dict[str, Any] | None,
    now: datetime,
) -> dict[str, Any]:
    repositories: dict[int, dict[str, Any]] = {}
    categories: list[dict[str, Any]] = []
    excluded_ids: set[int] = set()
    excluded_by_reason: dict[str, int] = {}

    for rule in config.queries:
        expanded = expand_query(rule.query, now)
        items = client.search_repositories(
            expanded,
            sort=rule.sort,
            order=rule.order,
            limit=config.candidate_limit,
        )
        category_ids: list[int] = []
        for item in items:
            is_excluded, reason = _excluded(item, config.exclude_without_license)
            repo_id = item["id"]
            if is_excluded:
                if repo_id not in excluded_ids:
                    excluded_ids.add(repo_id)
                    excluded_by_reason[reason or "other"] = excluded_by_reason.get(reason or "other", 0) + 1
                repositories.pop(repo_id, None)
                continue
            if repo_id in excluded_ids:
                continue
            categories_for_repo = repositories.get(repo_id, {}).get("categories", [])
            normalized = _normalize_repository(item)
            normalized["categories"] = list(categories_for_repo)
            repositories[repo_id] = normalized
            if rule.key not in normalized["categories"]:
                normalized["categories"].append(rule.key)
            if repo_id not in category_ids:
                category_ids.append(repo_id)
        categories.append(
            {
                "key": rule.key,
                "title": rule.title,
                "query": expanded,
                "sort": rule.sort,
                "order": rule.order,
                "repository_ids": category_ids,
            }
        )

    for category in categories:
        category["repository_ids"] = sorted(
            (repo_id for repo_id in category["repository_ids"] if repo_id in repositories),
            key=lambda repo_id: (
                -repositories[repo_id]["stars"],
                repositories[repo_id]["name_with_owner"].casefold(),
            ),
        )

    previous_by_id = {
        repo["id"]: repo for repo in (previous or {}).get("repositories", [])
    }
    for repo in repositories.values():
        old = previous_by_id.get(repo["id"])
        if old is not None:
            repo["star_delta"] = repo["stars"] - old["stars"]

    repository_list = sorted(
        repositories.values(),
        key=lambda repo: (-repo["stars"], repo["name_with_owner"].casefold()),
    )
    generated_utc = now.astimezone(timezone.utc).replace(microsecond=0)
    generated_shanghai = generated_utc.astimezone(SHANGHAI)
    return {
        "schema_version": 1,
        "generated_at": generated_utc.isoformat().replace("+00:00", "Z"),
        "generated_at_beijing": generated_shanghai.isoformat(),
        "baseline": previous is None,
        "source": "GitHub REST Search repositories API",
        "report_limit": config.report_limit,
        "candidate_limit": config.candidate_limit,
        "excluded_count": len(excluded_ids),
        "excluded_by_reason": dict(sorted(excluded_by_reason.items())),
        "categories": categories,
        "repositories": repository_list,
    }


def _markdown(value: Any, limit: int | None = None) -> str:
    text = str(value or "").replace("\r", " ").replace("\n", " ").strip()
    if limit and len(text) > limit:
        text = text[: max(0, limit - 1)].rstrip() + "…"
    text = html.escape(text, quote=False).replace("\\", "\\\\")
    for character in ("|", "`", "*", "_", "[", "]"):
        text = text.replace(character, "\\" + character)
    return text or "-"


def render_report(snapshot: dict[str, Any]) -> str:
    by_id = {repo["id"]: repo for repo in snapshot["repositories"]}
    baseline_note = (
        "本次为基线扫描，Star 增量将在下一次成功扫描后显示。"
        if snapshot["baseline"]
        else "Star 增量按相邻两次成功快照计算。"
    )
    lines = [
        "## 最新雷达",
        "",
        f"- UTC：`{snapshot['generated_at']}`",
        f"- 北京时间：`{snapshot['generated_at_beijing']}`",
        f"- 数据源：{snapshot['source']}",
        f"- 排除候选：{snapshot['excluded_count']} 个",
        f"- 说明：{baseline_note}",
        "",
    ]
    for category in snapshot["categories"]:
        lines.extend(
            [
                f"### {category['title']}",
                "",
                f"查询规则：`{category['query']}`",
                "",
            ]
        )
        repo_ids = category["repository_ids"][: snapshot["report_limit"]]
        if not repo_ids:
            lines.extend(["当前没有符合条件的项目。", ""])
            continue
        lines.extend(
            [
                "| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |",
                "|---|---:|---:|---|---|---|---|",
            ]
        )
        for repo_id in repo_ids:
            repo = by_id[repo_id]
            delta = "基线" if repo["star_delta"] is None else f"{repo['star_delta']:+d}"
            pushed = _markdown(repo["pushed_at"][:10])
            lines.append(
                "| "
                f"[{_markdown(repo['name_with_owner'])}]({repo['url']}) | "
                f"{repo['stars']:,} | {delta} | {_markdown(repo['language'])} | "
                f"{_markdown(repo['license'])} | {pushed} | {_markdown(repo['description'], 120)} |"
            )
        lines.append("")
    lines.extend(
        [
            "---",
            "",
            "“热门”由仓库搜索条件与 Star 增量共同定义，不代表 GitHub 官方 Trending 排名。",
        ]
    )
    return "\n".join(lines).rstrip()


def replace_report(readme: str, report: str) -> str:
    validate_readme(readme)
    start = readme.index(README_START) + len(README_START)
    end = readme.index(README_END)
    return readme[:start] + "\n\n" + report.rstrip() + "\n\n" + readme[end:]


def _stage_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="\n", dir=path.parent, delete=False
    ) as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
        return Path(handle.name)


def _backup_file(path: Path) -> Path | None:
    if not path.exists():
        return None
    with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
        with path.open("rb") as source:
            shutil.copyfileobj(source, handle)
        handle.flush()
        os.fsync(handle.fileno())
        return Path(handle.name)


def _atomic_write_many(outputs: list[tuple[Path, str]]) -> None:
    """Replace a related output set and roll it back if any replace fails."""
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path | None] = {}
    replaced: list[Path] = []
    preserved_backups: set[Path] = set()
    try:
        for path, text in outputs:
            staged[path] = _stage_text(path, text)
        for path, _ in outputs:
            backups[path] = _backup_file(path)
        for path, _ in outputs:
            os.replace(staged[path], path)
            staged.pop(path)
            replaced.append(path)
    except OSError as exc:
        rollback_errors: list[str] = []
        for path in reversed(replaced):
            backup = backups.get(path)
            try:
                if backup is None:
                    path.unlink(missing_ok=True)
                else:
                    os.replace(backup, path)
                    backups[path] = None
            except OSError as rollback_exc:
                if backup is not None:
                    preserved_backups.add(backup)
                    rollback_errors.append(
                        f"{path}: {rollback_exc}; backup preserved at {backup}"
                    )
                else:
                    rollback_errors.append(f"{path}: {rollback_exc}")
        detail = ""
        if rollback_errors:
            detail = "; rollback failed for " + ", ".join(rollback_errors)
        raise RadarError(f"Cannot publish radar outputs: {exc}{detail}") from exc
    finally:
        cleanup_paths = [
            *staged.values(),
            *(path for path in backups.values() if path and path not in preserved_backups),
        ]
        for temp_path in cleanup_paths:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass


def run_radar(
    config_path: Path,
    data_dir: Path,
    readme_path: Path,
    *,
    client: Any | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    config = load_config(config_path)
    try:
        readme = readme_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RadarError(f"Cannot read README: {readme_path}") from exc
    validate_readme(readme)
    previous = load_previous(data_dir / "latest.json")
    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        raise RadarError("now must be timezone-aware")
    api_client = client or GitHubClient(os.environ.get("GITHUB_TOKEN"))

    # Finish every fallible fetch and render step before touching successful output.
    snapshot = build_snapshot(config, api_client, previous, current_time)
    report = render_report(snapshot)
    new_readme = replace_report(readme, report)
    serialized = json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    history_path = data_dir / "history" / f"{current_time.astimezone(timezone.utc).date().isoformat()}.json"

    _atomic_write_many(
        [
            (history_path, serialized),
            (data_dir / "latest.json", serialized),
            (readme_path, new_readme),
        ]
    )
    return snapshot


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--readme", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        snapshot = run_radar(args.config, args.data_dir, args.readme)
    except (RadarError, OSError) as exc:
        print(f"radar: {exc}", file=sys.stderr)
        return 1
    print(
        f"Generated {len(snapshot['repositories'])} repositories across "
        f"{len(snapshot['categories'])} categories at {snapshot['generated_at']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
