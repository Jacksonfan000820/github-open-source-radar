# Minimum MVP Contract

## Outcome

Provide a GitHub-hosted, serverless radar that discovers popular public open-source repositories, preserves successful snapshots, and shows Star growth on the repository home page.

## Must Have

- Python standard-library scanner using GitHub's repository Search API.
- Two configurable default signals: recently created repositories with meaningful Stars, and high-Star repositories pushed recently.
- Filter forks, archived/disabled repositories, and repositories without a clear license.
- Deduplicate by numeric repository ID and preserve rename continuity.
- Baseline first run; adjacent-successful-snapshot Star deltas afterward.
- Atomic successful outputs to `README.md`, `data/latest.json`, and one UTC date history file.
- Daily and manual GitHub Actions execution with repository-scoped `GITHUB_TOKEN`.
- Unit tests for calculation, validation, filtering, failure preservation, and output lifecycle.

## Deferred

- Topic/language dashboards, custom watchlists, Releases/Issue monitoring, weekly notifications, RSS, GitHub Pages, charts, AI summaries, and long-term snapshot compaction.

## Out of Scope

- Cloning or executing discovered code, automatically starring/forking/contacting projects, private repository data, paid APIs, and claims that the result is GitHub's official Trending rank.

## Business Rules

- “Popular” means the configured Search API signals plus Star delta, not official Trending.
- Only adjacent successful snapshots participate in delta calculation.
- A failed or invalid scan must not replace successful output.
- Same-day reruns replace that UTC date's history file.
- Times are stored in UTC and displayed in UTC and Asia/Shanghai.
- Scanned repositories receive no notifications or state changes.

## Acceptance Criteria

1. A manual run creates valid non-empty JSON and a readable generated README section without a PAT.
2. The workflow schedules 00:17 UTC daily and supports manual dispatch.
3. Results contain no fork, archived, disabled, or unlicensed repositories.
4. First-run deltas are null; a fixture-backed second run calculates exact deltas.
5. Duplicate category results and renamed repositories are reconciled by numeric ID.
6. Empty categories render a valid empty state.
7. API/timeout/shape/config/README marker failures exit nonzero without altering prior outputs.
8. Tests cover baseline, delta, deduplication, rename continuity, filtering, empty results, same-day replacement, and failure preservation.
9. Workflow permissions are limited to repository contents and no personal token is stored.

## Release Gate

- Unit tests pass locally and in Actions.
- A real API scan succeeds and generated artifacts are inspected.
- Workflow syntax, minimal permissions, pinned official actions, branch target, and push behavior are independently reviewed.
- The first manual Actions run completes and the generated commit is visible on `main`.

