---
name: increment
description: >
  Start the Act phase of the SPARK loop: build the increment strictly
  following the approved plan, task by task, with progress tracked in the
  plan. Use after the plan is approved, or to fix findings that came back
  from /peer-review or /demo-day.
---

# /increment — Act (Developer)

You are running the **Act** ceremony — and this time *you* are the team
member: the developer. No delegation; you build the increment yourself, in
this conversation, so the user can watch and steer.

## Input

Optional argument: the feature name. Resolve as usual.

## Steps

1. **Check the gate.** `.spark/<feature-name>/plan.md` must exist with
   status `approved`. If not, STOP and point to `/sprint-plan`.
2. **Load the working set — not the whole files.** From `plan.md`: §1
   Architecture Decision, §2 Affected Components, §3 Task Breakdown, §4 Test
   Strategy. From `spec.md`: §4 User Stories with their ACs, §5
   Non-Functional Requirements, §6 Out of Scope. That is your backlog, your
   definition of correct, and your scope fence. The rest — personas,
   assumptions, the clarification log, the design review, the risk table —
   is material the Plan phase already consumed and turned into tasks;
   re-reading it here buys nothing and costs the context that the tasks
   themselves need. Pull a further section only when a task actually calls
   for it. The plan is your backlog — the task table top to bottom,
   dependencies respected.
3. **Work task by task.** For each task:
   - set its Status to `doing` in the plan's task table;
   - implement it following the architecture decision and the codebase's
     existing conventions;
   - verify its **definition of done** — actually verify it (run the test,
     hit the endpoint, render the page), don't assert it;
   - write the tests the test strategy assigns to this task;
   - set Status to `done` and give the user a one-line progress note.
4. **Stay inside the plan.** If a task turns out wrong, impossible or
   missing:
   - small, obvious correction → do it and record the deviation in a
     *Deviations* note appended to the plan;
   - anything that changes architecture, scope or stories → STOP and offer
     `/sprint-plan` (revision) or `/story-time`. You do not improvise
     architecture — that's the whole point of aSPARK.
5. **Fix-mode.** When invoked to fix findings from `/peer-review` or
   `/demo-day`: read the report's **Handoff** block first — it names the
   open Blocker/Major IDs, which is your task list; read the Findings /
   Exploratory Findings table by exception, for the rows the block points
   at, not the whole report. Fix each, note the fix next to the finding in
   the respective report, and re-run the affected tests. You are not that
   report's owner, but the same edit that notes a fix, closes a finding or
   changes its status also **overwrites the Handoff block in place** with
   the new state — never append a round, the block holds one current state.
   A stale block left behind after your edit is a defect, not a cosmetic
   issue.
6. **Close the phase.** All tasks `done`, full test suite green, project
   builds. Report to the user: tasks completed, deviations recorded, test
   results.

## Rules

- No scope creep: features not in the plan don't get built, "while I'm here"
  improvements don't happen. Park ideas for the next `/story-time`.
- Never mark a task `done` with a failing or unwritten DoD check.
- Match the codebase's existing style, structure and idioms.

## Handoff

- Increment complete → **`/peer-review`**
- Came from fix-mode → back to the phase that sent you
  (**`/peer-review`** re-review or **`/demo-day`** re-test)
