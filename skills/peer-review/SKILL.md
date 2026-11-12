---
name: peer-review
description: >
  Start the Review phase of the SPARK loop: the Reviewer audits the diff
  produced by /increment — plan conformance, correctness, edge cases,
  security, test quality — and writes the review report. Use after
  /increment reports done, or to re-review after fixes.
---

# /peer-review — Review (Reviewer)

You are running the **code review** ceremony. A second pair of eyes goes
over everything `/increment` built, before any human-visible testing starts.

## Input

Optional argument: the feature name. Resolve as usual.

## Steps

1. **Check the gate.** The plan at `.spark/<feature-name>/plan.md` must show
   all tasks `done`. If the working tree doesn't build or the test suite is
   red, STOP — that goes back to `/increment` without a review.
   Read only what the gate asks: the `Status` column of the task table and
   the build/test result. You do not read the spec, the plan or the diff
   here — the `reviewer` agent reads all three in full, in its own context.
   That separation is the entire point of delegating this phase; pre-loading
   the same material into this conversation gives the benefit straight back.
   - **Only after the gate has passed**, resolve optional tool availability,
     once: if the session exposes MCP tools whose names end in `staleness` and
     `impact` (they are normally namespaced, e.g.
     `mcp__aspark-graph__staleness`), treat that as the available surface and
     run no command; otherwise probe once, read-only, with
     `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no;
     test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no`
     — it reports both facts and **always exits 0**, so the absent case never
     looks like a failed command.
     Resolve **both** facts — is there a surface, and does
     `.aspark-graph/graph.json` exist — and act on the four states in
     `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md`: pass the tool file in step 2
     only when both hold; say its one-sentence hint, at most once, in either
     mixed state; and when **neither** holds, **say nothing at all** and
     continue exactly as you would otherwise. Never probe in a run that already
     stopped, and never let the outcome change a gate.
2. **Delegate to the Reviewer.** Pick the model first: if
   `.spark/constitution.md` §11 names a model for `reviewer`, pass exactly
   that as the agent call's `model`; if it names none, or there is no
   constitution or no §11, pass no model, so the agent's own default
   (`sonnet`) applies. Then invoke the `reviewer` agent with the
   feature paths, the report template from
   `${CLAUDE_PLUGIN_ROOT}/templates/review-report.md`, how to determine
   the diff (commit range or changed files since the increment started), and
   the path of every active lens whose own frontmatter `phases` field includes
   `review` — read each active lens's file
   (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`) to decide; do not work from a
   list of lens names given here.
   If a tool resolved as available in step 1, pass
   `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` the same way — one more path
   alongside the lens paths, nothing else.
   Always also pass `${CLAUDE_PLUGIN_ROOT}/standards/anti-generosity.md`, by this
   literal path: no constitution read, no flag. Tell the agent to read it in full
   before any verdict and to name it in the report as applied.
   For a re-review, check the round cap in step 4 **before** you invoke the
   agent, then point it at the previous report so it verifies the fixes
   instead of starting from zero.
3. **Present the report.** Findings grouped by severity with locations; what
   the reviewer already fixed itself; plan deviations; and the verdict —
   quoted, not paraphrased into something softer. If the report does not name
   the anti-generosity standard as applied, tell the user.
4. **Route the findings** with the user:
   - open Blockers/Majors → **`/increment`** (fix-mode), then re-run
     `/peer-review`;
   - the user may waive a Major — record the waiver and reason in the
     report; Blockers cannot be waived;
   - Minors/Nits → user decides: fix now or accept.
   - **round cap:** at most **two** Reviewer rounds per feature by default,
     the first review plus one re-review. A different number applies only
     when `.spark/constitution.md` §11 `Reviewer rounds` names one. Read the
     current round from the trail, not from memory: the `Round` row in the
     header table of `review.md`. When `Round` already equals the cap and a
     Blocker or Major is still open, do **not** route to `/increment` and do
     **not** invoke the Reviewer again. Stop and lay the open findings before
     the user, who picks one: waive a Major (recorded with its reason, as
     above), grant exactly one more round (fix, then re-review), or go back
     to `/sprint-plan` because the plan is the problem. You never raise the
     cap yourself, a Blocker still cannot be waived, and the report never
     becomes `passed` over an open Blocker.
5. **Close the gate.** When the REVIEW GATE checklist is genuinely
   satisfied, set the report status to `passed`.
6. **Open findings.** After the gate decision, run
   `${CLAUDE_PLUGIN_ROOT}/standards/open-findings.md` (read it now; it is
   conductor-side): propose follow-up tickets for findings that stay open,
   file only on an explicit yes, and say nothing when none are open.

## Rules

- Never soften the verdict when presenting it.
- The reviewer's own fixes must be visible to the user — list them, they are
  part of the diff now.
- Don't skip re-review after fixes: fixed code is new code. The round cap
  does not permit an unreviewed fix. At the cap, either the user grants a
  round or nothing more is fixed in this phase.

## Handoff

- Review `passed` → **`/demo-day`** (QA in the real browser)
- Findings to fix → **`/increment`**
