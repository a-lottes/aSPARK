# Evidence: graph-build-then-offer

Method: commands run in this checkout (2026-11-16). Live sessions were **not** run in this
environment (no MCP graph server for scratch repos, no browser-driven app); every
session-level behaviour below is `not-verified-live`.

| Case | Check | Result |
|---|---|---|
| No surface, no graph.json (negative case first) | `git diff -U0 v0.17.0 -- tools/aspark-graph.md` hunks in table rows | only the yes/no row changed; no/no and no/yes rows byte-identical to v0.17.0 (observed). Session behaviour: `not-verified-live` |
| Probe paragraph identical | md5 of the paragraph in sprint-plan, peer-review, tools/README.md | identical (observed); demo-day differs only by its two documented phrases |
| Growth cap (NFR-5) | `git diff --numstat` | each skill +8/-4 (net 4) (observed) |
| Agent bodies | `grep gate_health agents/*.md` | each of the three says "never" (observed); no `tools:` hunk (observed) |
| No build ban left | grep `Stale ⇒ absent`, "Never run" build | none left; `Never run serve or install` remains (observed) |
| Round cap not taken over | grep diff | none added (observed) |
| Build / stale / failure / no-runner sessions, git status after build | T6 sessions | `not-verified-live` |

## Performed commands (2026-11-16, scratch repos under /tmp)

| Case | Command | Observed |
|---|---|---|
| Build, valid trail | `aspark-graph build .` in a scratch repo holding only this feature's trail | rc=0, "Built graph"; `git status` shows only `?? .aspark-graph/` (NFR-3 holds) |
| Stale then rebuild | edit `a.py`, `query staleness`, `build .`, `query staleness` | `stale: true` then `stale: false` after one rebuild |
| Build failure | `aspark-graph build .` in a clone of this repo (older trails) | "template drift in .spark/adversarial-gates-standard/spec.md"; no `graph.json` written; `query staleness` says "No graph found". A real failure path: the ceremony must say it once and continue |
| Ceremony sessions | `claude -p --plugin-dir …` in a scratch repo | `not-verified-live`: the CLI answers "Not logged in"; no MCP graph server here. T6 sessions and the registered QA set (AC-1.1, 2.1, 3.1; 10 of 10 no-surface) were not run, so no rate exists |
