# Evidence: light-path

Prompt material only: every rule here makes a behaviour likely, not certain. **No rate was
observed, and the saving was not measured.** One session per case, `sonnet`, Claude Code CLI
2.1.322, 2026-11-12. Made directly on the maintainer's instruction, without a spec, plan,
review or QA artifact of its own; this file is its whole trail.

## Why

Measurement runs of the full loop on a real repo (outside this repository) cost 25 to 42
times the output tokens of a single plain session. On two of three tasks the plain session
reached the same hidden-test result. The one task where the loop did better turned on a
single decision in the spec, not on the plan, QA or a second review. So the spec stays on
every path; what a small change can skip is the rest.

## What changed

| Change | Where the agent reads it |
|---|---|
| `Path` row (`full` \| `light`, absent = `full`) | `templates/spec.md` header |
| Six sizing checks at the spec gate; offer only, the user chooses; silent when a check fails | `skills/story-time/SKILL.md` step 8 |
| Short plan written by the orchestrator, user approves; build; one review; no `/demo-day`; exits back to the full loop | `skills/spark/SKILL.md` *The Light Path*, phase map, closing table |
| Cap of one Reviewer round on `light`; an open Blocker or Major switches to `full` | `skills/peer-review/SKILL.md` step 4 |
| A missing `qa.md` passes only on `light`, reported as `QA: not run (light path)` | `skills/go-live/SKILL.md` step 1, `agents/release-manager.md` step 1 |
| `Light path: on \| off`, default `on` | `templates/constitution.md` §11 |

## Dry runs

Fixture: a scratch git repo with `src/greet.py`, one test, and `.spark/greeting/` (one
story, two ACs). No constitution. Command per case:
`claude --plugin-dir <this branch> -p "<prompt>" --model sonnet --permission-mode acceptEdits`.

| Case | State | Result |
|---|---|---|
| N (negative) | spec `approved`, no `Path` row, no plan | Went to `/sprint-plan` and invoked the Engineering Manager, as before. No mention of the light path. |
| P | same, `Path` `light` | Did not invoke the Engineering Manager. Wrote `plan.md` itself, `draft`, two tasks, one line per AC, and stopped for approval. Closing table had `qa.md: not run (light path)` and `Path: light`. |
| E | `light`, review round 1 `changes-requested`, one open Major | Set `Path` to `full`, said why ("review round 1 left Major F1 open"), and routed to `/increment` fix-mode. Closing line `Path: full (left the light path: …)`. |
| G | `light`, review `passed`, no `qa.md` | `/go-live` accepted the missing `qa.md` and named `QA: not run (light path)` for the report. The Release Manager then stopped because its Bash was denied in the sandbox, so no pre-flight ran. |
| T1 → T2 (sizing, ineligible) | idea for a one-function change; another trail's story was titled "Greet by name" | First version of check 5 grepped bare words; the match on "greet" in another feature's story title made the route `full`. Correct by the rule as then written, but a false positive. Check 5 now greps file **paths** only (`src/greet.py`). |
| T3 (sizing, eligible) | same idea, check 5 by path | Round 1: spec written with three assumptions, no light offer. Round 2, after the user confirmed them: all six checks listed as met, light and full explained, user asked. Round 3, "Light.": `Path` `light` written, spec stays `approved`. |

**Misses in these runs.**

- T3 round 1 said "I'm not offering the light path … if you confirm both … I can offer
  light", although the rule says to say nothing when a check fails.
- T3 round 3 named `/sprint-plan` as the next step. The skill now says to name `/spark`, which
  writes the short plan; this wording change was not re-run.
- G: the pre-flight that stands in for QA did not run (sandbox), so the release half is not
  shown.

## Not verified live

- A whole light loop from idea to release in one session, and its token count against the
  full loop and against a plain session. `⚠ not-verified-live`
- The exits "plan needs a design choice or more than five tasks" and "`/increment` must touch a
  file outside the plan". `⚠ not-verified-live`
- `Light path: off` in a constitution. `⚠ not-verified-live`
- The Factory: it does not read the `Path` row; a Factory line runs the full loop or none.

## Structural audits

- `claude plugin validate .` → passed with the two warnings that exist on `main`
  (`autoUpdate` in the marketplace manifest, `CLAUDE.md` at the plugin root).
- `git ls-files '*.py'` empty; no executable code added.
- No protected template heading, column or ID pattern renamed or removed. The `Path` header
  row is new and optional; the `aspark-template` marker is unchanged.
