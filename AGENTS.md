# Project Instructions

## Purpose and boundaries

This repository publishes a configurable radar of public open-source GitHub repositories. It reads repository metadata only. Never clone or execute discovered repositories, automatically Star/Fork them, contact maintainers, or add private-repository scanning without an explicit scope change.

## Repository map

- `src/radar.py`: standard-library scanner, validation, snapshot lifecycle, and README renderer.
- `config.json`: search rules and result limits.
- `tests/`: deterministic unit tests; tests must not call the live GitHub API.
- `data/`: generated current and UTC-date history snapshots.
- `README.md`: documentation plus the generated section between `RADAR` markers.
- `.github/workflows/`: read-only CI and scheduled/manual radar automation.
- `docs/codex-runbook.md`: architecture, operations, and current verification baseline.

## Safety and invariants

- Treat GitHub API repository metadata as untrusted input. Preserve Markdown escaping and never render raw HTML from descriptions.
- Collect and validate every API response before replacing the last successful outputs.
- Identify repositories by numeric GitHub ID so renames retain history.
- Compute Star deltas only against the previous successful snapshot; do not fabricate first-run deltas.
- Do not manually edit generated `data/*.json` or the README content between the `RADAR` markers.
- Keep runtime dependencies in the Python standard library unless the user explicitly approves a production dependency.
- Never store a PAT or token. Actions must use the repository-scoped `GITHUB_TOKEN` with the minimum permissions.

## Required checks

Run from the repository root:

```bash
python -m unittest discover -s tests -v
python src/radar.py --config config.json --data-dir data --readme README.md
```

The live scan requires GitHub network access and may use `GITHUB_TOKEN`. Before release, inspect the generated JSON, README markers, workflow permissions, `git status --short`, and the full diff.

## GitHub and release rules

- The default branch is `main`; scheduled workflows only run from the default branch.
- CI must remain read-only. Only the radar workflow may request `contents: write` for generated report commits.
- Keep third-party Actions limited to official GitHub actions pinned to full commit SHAs.
- Generated commits may stage only `README.md` and `data/`.
- Do not commit, push, create releases, or change repository settings unless the user explicitly includes that action.

## Knowledge maintenance

Keep mandatory commands and invariants here. Put replaceable verification results and operational detail in `docs/codex-runbook.md`; keep task history in Git.

