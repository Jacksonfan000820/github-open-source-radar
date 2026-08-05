# Codex Runbook

## Architecture

`config.json` defines one or more GitHub repository search queries. `src/radar.py` expands relative UTC date placeholders, requests the official GitHub Search API, validates and filters metadata, deduplicates by numeric repository ID, and compares against `data/latest.json`. Only after every query succeeds does it transactionally replace the current/history JSON and generated README section, rolling back the set if a replacement fails. If restoration itself fails, the recovery backup is retained and its path is reported.

The first successful scan establishes a baseline. Later scans calculate Star deltas against the previous successful snapshot, including across repository renames. The report is a transparent proxy for popularity and is not GitHub's official Trending rank.

## Output lifecycle

- `data/latest.json` is the comparison source for the next successful run.
- `data/history/YYYY-MM-DD.json` uses the UTC date; reruns on the same date replace that file.
- `README.md` is regenerated only between `<!-- RADAR:START -->` and `<!-- RADAR:END -->`.
- API, timeout, invalid-response, config, previous-snapshot, or README-marker failures exit nonzero before successful output replacement.

## Local operation

```bash
python -m unittest discover -s tests -v
python src/radar.py --config config.json --data-dir data --readme README.md
```

`GITHUB_TOKEN` is optional locally and raises GitHub API limits. Do not echo or save it. Proxy configuration is an operator/machine concern and must not be committed.

## GitHub automation

- `.github/workflows/ci.yml` runs unit tests on pushes to `main` and pull requests with `contents: read`.
- `.github/workflows/radar.yml` runs at `00:17 UTC` (`08:17 Asia/Shanghai`) and via manual dispatch.
- The radar job runs tests before scanning, stages only `README.md` and `data/`, skips an empty diff, and pushes as `github-actions[bot]` using `contents: write`.
- A commit made with `GITHUB_TOKEN` does not recursively trigger ordinary push workflows.

## Failure recovery

1. Inspect the failed Actions run and classify API/rate-limit, validation, test, permission, or push failure.
2. Confirm `data/latest.json` and the README still show the last successful snapshot.
3. For API rate limits, wait for reset; do not increase retries or introduce a PAT by default.
4. For write permission failures, inspect repository Actions workflow permissions and the job-level `contents: write` declaration.
5. Re-run manually after the root cause is corrected.

Public repositories can have scheduled workflows disabled after 60 days without repository activity. Generated radar commits normally provide activity; if the workflow stops, re-enable it from Actions after diagnosing the cause.

## Verification baseline

Replace this section after a material change.

- Local Python: 3.13.2.
- Unit tests: 17 passed on 2026-08-05.
- Live scan: 161 unique repositories across 2 categories; 39 unlicensed candidates excluded.
- Generated snapshot schema: version 1; JSON parsed successfully; README markers remained unique.
- Remote CI run `30969941477` and radar run `30969965389` succeeded on 2026-08-05; the radar produced bot commit `f81db03`.
