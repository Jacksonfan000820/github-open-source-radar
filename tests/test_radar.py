from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from src.radar import RadarError, run_radar


NOW = datetime(2026, 8, 5, 0, 17, tzinfo=timezone.utc)


def repo(
    repo_id: int,
    name: str,
    stars: int,
    *,
    license_id: str | None = "MIT",
    fork: bool = False,
    archived: bool = False,
    disabled: bool = False,
) -> dict:
    return {
        "id": repo_id,
        "full_name": name,
        "html_url": f"https://github.com/{name}",
        "description": f"Description for {name}",
        "language": "Python",
        "license": {"spdx_id": license_id} if license_id else None,
        "stargazers_count": stars,
        "forks_count": 12,
        "open_issues_count": 3,
        "created_at": "2026-07-20T00:00:00Z",
        "pushed_at": "2026-08-04T00:00:00Z",
        "fork": fork,
        "archived": archived,
        "disabled": disabled,
        "private": False,
    }


class FakeClient:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def search_repositories(self, query, *, sort, order, limit):
        self.calls.append((query, sort, order, limit))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


class RadarTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.config = self.root / "config.json"
        self.readme = self.root / "README.md"
        self.data = self.root / "data"
        self.config.write_text(
            json.dumps(
                {
                    "candidate_limit": 100,
                    "report_limit": 20,
                    "exclude_without_license": True,
                    "queries": [
                        {
                            "key": "new",
                            "title": "New",
                            "query": "created:>={date_30d} stars:>=100",
                            "sort": "stars",
                            "order": "desc",
                        },
                        {
                            "key": "active",
                            "title": "Active",
                            "query": "pushed:>={date_7d} stars:>=1000",
                            "sort": "stars",
                            "order": "desc",
                        },
                    ],
                }
            ),
            encoding="utf-8",
        )
        self.readme.write_text(
            "# Radar\n\n<!-- RADAR:START -->\nold\n<!-- RADAR:END -->\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def run_scan(self, responses, now=NOW):
        return run_radar(
            self.config,
            self.data,
            self.readme,
            client=FakeClient(responses),
            now=now,
        )

    def test_first_run_is_baseline_and_writes_outputs(self):
        snapshot = self.run_scan([[repo(1, "acme/one", 100)], []])
        self.assertTrue(snapshot["baseline"])
        self.assertIsNone(snapshot["repositories"][0]["star_delta"])
        self.assertTrue((self.data / "latest.json").exists())
        self.assertTrue((self.data / "history" / "2026-08-05.json").exists())
        self.assertIn("本次为基线扫描", self.readme.read_text(encoding="utf-8"))

    def test_second_run_computes_delta_and_tracks_rename_by_id(self):
        self.run_scan([[repo(1, "acme/old", 100)], []])
        snapshot = self.run_scan([[repo(1, "acme/new", 107)], []])
        current = snapshot["repositories"][0]
        self.assertFalse(snapshot["baseline"])
        self.assertEqual("acme/new", current["name_with_owner"])
        self.assertEqual(7, current["star_delta"])

    def test_duplicate_repository_has_one_entity_and_two_categories(self):
        item = repo(1, "acme/one", 100)
        snapshot = self.run_scan([[item], [dict(item)]])
        self.assertEqual(1, len(snapshot["repositories"]))
        self.assertEqual(["new", "active"], snapshot["repositories"][0]["categories"])
        self.assertEqual([1], snapshot["categories"][0]["repository_ids"])
        self.assertEqual([1], snapshot["categories"][1]["repository_ids"])

    def test_filters_unlicensed_fork_archived_and_disabled(self):
        items = [
            repo(1, "acme/no-license", 100, license_id=None),
            repo(2, "acme/fork", 100, fork=True),
            repo(3, "acme/archived", 100, archived=True),
            repo(4, "acme/disabled", 100, disabled=True),
            repo(5, "acme/good", 100),
        ]
        snapshot = self.run_scan([items, []])
        self.assertEqual(["acme/good"], [r["name_with_owner"] for r in snapshot["repositories"]])
        self.assertEqual(4, snapshot["excluded_count"])

    def test_empty_category_renders_empty_state(self):
        self.run_scan([[], []])
        text = self.readme.read_text(encoding="utf-8")
        self.assertEqual(2, text.count("当前没有符合条件的项目。"))

    def test_same_day_rerun_replaces_history_file(self):
        self.run_scan([[repo(1, "acme/one", 100)], []])
        history = self.data / "history" / "2026-08-05.json"
        self.run_scan([[repo(1, "acme/one", 105)], []])
        files = list((self.data / "history").glob("*.json"))
        self.assertEqual([history], files)
        payload = json.loads(history.read_text(encoding="utf-8"))
        self.assertEqual(105, payload["repositories"][0]["stars"])

    def test_api_failure_preserves_previous_outputs(self):
        self.run_scan([[repo(1, "acme/one", 100)], []])
        latest_before = (self.data / "latest.json").read_bytes()
        readme_before = self.readme.read_bytes()
        with self.assertRaises(RadarError):
            self.run_scan([[repo(1, "acme/one", 101)], RadarError("boom")])
        self.assertEqual(latest_before, (self.data / "latest.json").read_bytes())
        self.assertEqual(readme_before, self.readme.read_bytes())

    def test_invalid_readme_markers_fail_before_writes(self):
        self.readme.write_text("# no markers\n", encoding="utf-8")
        with self.assertRaises(RadarError):
            self.run_scan([[], []])
        self.assertFalse((self.data / "latest.json").exists())

    def test_invalid_config_fails_before_writes(self):
        self.config.write_text("{}", encoding="utf-8")
        with self.assertRaises(RadarError):
            self.run_scan([[], []])
        self.assertFalse((self.data / "latest.json").exists())

    def test_query_placeholders_expand_for_fixed_time(self):
        fake = FakeClient([[], []])
        run_radar(self.config, self.data, self.readme, client=fake, now=NOW)
        self.assertIn("created:>=2026-07-06", fake.calls[0][0])
        self.assertIn("pushed:>=2026-07-29", fake.calls[1][0])

    def test_untrusted_description_is_rendered_as_plain_markdown_text(self):
        item = repo(1, "acme/one", 100)
        item["description"] = "<script>alert(1)</script> | [click](https://evil.example)"
        self.run_scan([[item], []])
        text = self.readme.read_text(encoding="utf-8")
        self.assertNotIn("<script>", text)
        self.assertNotIn("[click](https://evil.example)", text)
        self.assertIn("&lt;script&gt;", text)


if __name__ == "__main__":
    unittest.main()
