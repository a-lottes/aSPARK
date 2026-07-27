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
2. **Delegate to the Reviewer.** Invoke the `reviewer` agent with the
   feature paths, the report template from
   `${CLAUDE_PLUGIN_ROOT}/templates/review-report.md`, how to determine
   the diff (commit range or changed files since the increment started), and
   the paths of any active lenses with review-phase checks (from the
   constitution's profile — `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` for any of
   `seo`, `api`, `cli`, `library`, `security`, `data`, `i18n` that are active).
   If a tool resolved as available in step 1, pass
   `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` the same way — one more path
   alongside the lens paths, nothing else.
   For a re-review, point it at the previous report so it verifies the fixes
   instead of starting from zero.
3. **Present the report.** Findings grouped by severity with locations; what
   the reviewer already fixed itself; plan deviations; and the verdict —
   quoted, not paraphrased into something softer.
4. **Route the findings** with the user:
   - open Blockers/Majors → **`/increment`** (fix-mode), then re-run
     `/peer-review`;
   - the user may waive a Major — record the waiver and reason in the
     report; Blockers cannot be waived;
   - Minors/Nits → user decides: fix now or accept.
5. **Close the gate.** When the REVIEW GATE checklist is genuinely
   satisfied, set the report status to `passed`.

## Rules

- Never soften the verdict when presenting it.
- The reviewer's own fixes must be visible to the user — list them, they are
  part of the diff now.
- Don't skip re-review after fixes: fixed code is new code.

## Handoff

- Review `passed` → **`/demo-day`** (QA in the real browser)
- Findings to fix → **`/increment`**
