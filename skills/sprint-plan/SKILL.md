---
name: sprint-plan
description: >
  Start the Plan phase of the SPARK loop: the Engineering Manager turns an
  approved spec into a technical plan — architecture decision with rejected
  alternatives, ordered task breakdown with definitions of done, test
  strategy and risks. Use after the spec is approved, or to revise a plan
  after review/QA findings.
---

# /sprint-plan — Plan (Engineering Manager)

You are running the **Plan** ceremony. The Engineering Manager locks the
"how" so that `/increment` never has to invent architecture on the fly.

## Input

Optional argument: the feature name. Resolve as usual (single feature in
`.spark/` → use it; several → ask).

## Steps

1. **Check the gate.** `.spark/<feature-name>/spec.md` must exist with
   status `approved`. If not, STOP and tell the user what's missing —
   `/story-time` or `/look-and-feel` come first. Never plan against a draft.
   The gate needs the spec's `Status` row, not the spec: the
   `engineering-manager` agent reads it whole in its own context, and a copy
   in this conversation would only crowd out the phases still to come.
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
2. **Delegate to the Engineering Manager.** Invoke the `engineering-manager`
   agent with the feature paths and the plan template from
   `${CLAUDE_PLUGIN_ROOT}/templates/plan.md`. Point it at
   `.spark/constitution.md` if it exists — the architecture must live within
   its technical constraints. If a tool resolved as available in step 1, pass
   `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` too — one more path alongside
   the template, nothing else. For a plan revision (rework after `/peer-review`
   or `/demo-day` findings), pass those findings along and say explicitly that
   this is a revision.
3. **Relay questions.** If the agent returns technical questions that change
   the architecture, put them to the user (AskUserQuestion for enumerable
   choices), then re-invoke with the answers.
   - The agent may also return a **tool query request** — it has no shell of
     its own. Run only the read-only `query` call it names, exactly as the tool
     file documents it, and re-invoke with the result. Never run a build, an
     install, or anything that writes. If the call fails or returns nothing,
     say so and let the agent proceed without it.
4. **Present the plan.** Show the user: the architecture decision **with the
   rejected alternatives**, the task table (count, order, walking-skeleton
   start), the test strategy, and the top risks. This is the moment for the
   user to veto the approach — say so.
5. **Iterate** on feedback via the agent until the user is satisfied.
6. **Close the gate.** Walk the PLAN GATE checklist with the user. On their
   explicit approval: set the plan status to `approved`.

## Rules

- Never set `approved` without the user's explicit approval.
- If planning surfaced a spec problem, don't patch the spec here — offer to
  run `/story-time` to rework it, then return.

## Handoff

- Plan approved → **`/increment`** (build it)
