---
name: next-steps
description: >
  Have the Product Owner survey the project's current state — shipped
  features, in-flight work, open findings, standing goals — and propose one
  concrete next feature ready to hand to /story-time or /spark. Use when the
  user has no idea in hand and asks "what should we build next", when a loop
  just closed and the next cycle needs a starting point, or when the backlog
  feels stale and needs a grounded suggestion instead of a guess.
---

# /next-steps — Propose the Next Feature (Product Owner)

You are running an **advisory** ceremony, not a gated one. The Product Owner
looks at where the project actually stands and proposes what to build next —
the user picks, tweaks, or discards it. Nothing here gets written to
`.spark/` and nothing needs approval; the output is a recommendation to carry
into `/story-time` or `/spark`.

## Input

None required. Optionally the user may point at a theme or constraint (e.g.
"something small", "focus on the API") — pass it through to the agent as a
steer, not a fixed answer.

## Steps

1. **Gather the loop state yourself — don't delegate this.** The
   `product-owner` agent cannot run `git` or walk `.spark/`. Collect a brief
   before invoking it:
   - `git log --oneline -20` (and further back if the project is young) for
     what actually shipped and when.
   - Every `.spark/<feature-name>/` directory: read `spec.md`, `plan.md`,
     `review.md`, `qa.md` where present and note each feature's status field
     (`draft`/`approved`, task completion, `passed`/`failed`, `released`).
     Classify each feature as **shipped** (released), **in-flight** (mid-loop,
     no open blocking findings), or **stalled** (open review/QA findings, or
     untouched for a while).
   - Any *unresolved* findings sitting in the newest `review.md` or `qa.md` —
     these are open points, not just status flags.
   - `.spark/constitution.md` if it exists — its Product Principles and
     Project Profile sections are the standing goals a proposal should serve.
   - If nothing exists yet in `.spark/` and git history is empty or trivial,
     say so plainly — there is no "state" to read yet, and the honest move is
     to ask the user for the first idea rather than fabricate one.
2. **Delegate to the Product Owner.** Invoke the `product-owner` agent in its
   *propose* mode (see its `## Proposing the Next Feature` section): give it
   the brief from step 1 verbatim (shipped list, in-flight/stalled features
   with their open points, constitution excerpt or "none"), plus any user
   steer. Point it at `.spark/constitution.md` if present.
3. **Relay, don't guess.** If the agent asks clarifying questions before it
   can propose anything sensible (e.g. the constitution is missing and the
   product's purpose is unclear), put them to the user, then re-invoke with
   the answers.
4. **Present the result as a conversation, not a report dump.** Show the
   recommended feature with its one-paragraph rationale (what gap it closes,
   why now, rough size, what it displaces), plus up to two alternatives the
   agent considered and rejected. Lead with the recommendation, not the list.
5. **Let the user decide.** They may: accept the recommendation as-is, ask
   for a different angle (re-invoke the agent with the steer), pick an
   alternative, or reject all of them and bring their own idea instead.
6. **Hand off on confirmation.** Once the user has settled on an idea
   (whichever source), ask whether to continue straight into `/story-time
   <idea>` or the full `/spark <idea>` loop, and invoke it if they say yes.
   Do not invoke either automatically — this skill only produces the idea.

## Rules

- Never write or modify files under `.spark/` — this ceremony produces a
  recommendation in conversation, not an artifact.
- Never treat the agent's proposal as chosen. It is a suggestion until the
  user says which one (or their own idea) to run with.
- If every existing feature is `released` and nothing is stalled, say that
  explicitly before proposing something new — a clean state is worth naming,
  not skipped past.
- If a stalled feature (open review/QA findings, or a plan sitting unbuilt)
  exists, the agent must weigh *finishing it* against *starting something
  new* as one of the candidates — half-shipped work is a real cost.

## Handoff

- User picks a proposal or brings their own idea → **`/story-time <idea>`**
  or **`/spark <idea>`**, on their explicit go.
- No idea survives, or the user wants to think first → stop here; nothing to
  persist.
