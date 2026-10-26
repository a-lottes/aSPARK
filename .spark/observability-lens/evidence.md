# Evidence: observability-lens

| | |
|---|---|
| Feature | observability-lens (issue #89, tracks #15) |
| Date | 2026-10-26 |
| Nature | **Dry runs.** One agent reading the lens, skills and a constitution. Not public runs, not a real `api` project. |

## E1 — Phase dispatch and activation audit (AC-2)

The lens frontmatter claims `phases: [specify, review]`, `applies-to: [api]` (`lenses/observability.md:3-4`). No `design`, `act` or `qa` claimed, so those phases are not dispatched. The lens says so in its "No QA row and no Act row" note.

| Site | Phase | Result |
|---|---|---|
| `skills/story-time/SKILL.md:70-71` | specify | Passes **all** active lens paths to the PO; PO (`agents/product-owner.md:85`) reads each. Clean, no name list. |
| `skills/peer-review/SKILL.md:49-52` | review | Dispatches by each active lens's own `phases` containing `review`; explicitly no name list. Clean. |
| `skills/demo-day/SKILL.md:83` | qa | Same `phases` rule; lens does not claim `qa`, so not sent. Correct. |
| `skills/increment/SKILL.md` | act | Dispatches no lens files by design; lens does not claim `act`. |
| `lenses/README.md` "Two ways a lens activates" bullet | activation | **Gap found, fixed:** type bullet listed `api`←`api` only. Added `observability`←`api`. |
| `agents/facilitator.md:71-72` | activation | **Gap found, fixed:** closed type→lens list. Added `observability`←`api` (deployed services only). |
| `templates/constitution.md:27` | activation | **Gap found, fixed:** same closed list. Added `observability`←`api`. |
| `lenses/README.md` Available-lenses table | registry | Row added. |
| `README.md`, `docs/status.md`, `docs/workflow.md` prose copies | docs | Count "Nine"→"Ten", status row, non-UI lens list updated. |
| `docs/workflow.md:77`, `docs/family.md:16`, `agents/qa-tester.md:192` | docs / qa note | **Missed by T2, found and fixed at review** (review F2): closed type→lens list, "9 lenses" count, non-`qa` lens example list. |

Residual, disclosed: `.spark/constitution.md` still says 9 lenses and has no `observability` row. Amending it is `/charter`'s alone; this repo's `api` row is already Off, so behaviour is unaffected. Flag for the next `/charter`.

## E2 — Negative case: no service profile (AC-3)

Repo: this one. `.spark/constitution.md:37` declares `Project type(s): library`, no characteristics, and its lens table lists `api` as Off ("no route handlers, no OpenAPI spec, no service"). The lens declares `applies-to: [api]` only, so neither `/story-time` nor `/peer-review` receives it: both pass only *active* lenses, and `observability` is not in this constitution's active list. The lens text also names `library`, `cli`, static `website` and `web-app` as silent.

Check that nothing changes: the only active lens remains `library` (`.spark/constitution.md:58`). The diff of this feature touches no skill or agent dispatch rule except the activation vocabulary. **Verdict: does not fire, nothing changes.** Hold rate of the instruction followed by an agent: not measured; this is a read, not a session.

## E3 — Positive case: sample `api` project (AC-4)

Sample, not a real repo: a FastAPI service with route handlers and an OpenAPI file, constitution `Project type(s): api`, active lenses `api, observability`. A feature "add `POST /imports`" with a background job.

- **Specify:** `story-time` passes both lens paths; the PO's per-lens rule yields NFRs such as "every request log line carries a request ID returned in `X-Request-Id`" and "the import job reports success/failure counts" (lens §2, §4).
- **Review:** `peer-review` sees `observability.md` `phases` contain `review`, passes it. Reviewer applies §1-§5 to the diff. A handler that does `except Exception: return 500` without logging is a finding under §1; a job that dead-letters silently is a finding under §4.
- **Silent boundary:** a diff that logs a password is raised once under `security` (if active), not here.

**Labelled a dry run.** The lens firing here is inferred from the dispatch rules, not observed in a separate agent session. **Measured hold rate: none; 0 sessions run.** Prompt material makes the check likely, never certain, and no test enforces that the lens fired. The first public run on a real `api` is still outstanding (ROADMAP #15).

## E4 — Version (AC-6)

A new lens file is additive: nothing existing is removed or changed in behaviour for projects that don't declare `api`. Per the `library` lens's semver rule (`lenses/library.md:37-39`) that is **minor**: `0.14.3` → `0.15.0` (`.claude-plugin/plugin.json`). Note: `CONTRIBUTING.md:189` says contributors don't bump; AC-6 of the issue overrides for this change, and the maintainer can revert that one line.
