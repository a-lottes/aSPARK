---
name: charter
description: >
  Establish or amend the project constitution — the standing principles and
  constraints that bind every SPARK phase. Use once at project start to give
  the team its ground rules, or any time a project-wide decision (stack choice,
  quality bar, non-negotiable) changes and should apply to all future features.
---

# /charter — The Project Constitution

You are setting the **standing context** for the whole SPARK loop. The
constitution lives at `.spark/constitution.md` and is read by every agent
before phase work — so decisions that hold across all features are made once
here, not re-argued in every `/story-time`.

## Input

Optional argument: a principle, constraint, or "set up our ground rules". No
argument → offer to create the constitution from scratch or amend the existing
one.

## Steps

1. **Delegate to the Facilitator.** Invoke the `facilitator` agent with the
   path `.spark/constitution.md`, the template from
   `${CLAUDE_PLUGIN_ROOT}/templates/constitution.md`, and the user's input
   verbatim. Say whether this is a first draft or an amendment if you already
   know; the agent will otherwise detect it from the file's presence.
2. **Relay, don't guess.** The agent grounds a draft in the codebase but cannot
   talk to the user. When it returns questions — the team's priorities, a
   deliberate quality bar, a contradiction only the user can resolve — put them
   to the user (AskUserQuestion where the choices are enumerable), then
   re-invoke the agent with the answers.
3. **Present the result.** Show the user the drafted constitution, separating
   what the agent **inferred from the project** from what still needs their
   decision, plus any contradiction it flagged. Keep it short — a constitution
   nobody reads is dead weight. Surface the **detected type(s), characteristics
   and proposed active lenses** (e.g. `seo`, `ux`, `security`) as their own
   decision, with the evidence the agent found — this is what makes later phases
   situational (an SEO lens only runs on a `website`, a `security` lens only when
   the project handles auth or PII), so confirm it consciously with the user
   rather than letting it ride. Also surface the **active-lens load** — if 4+
   lenses come out active, flag the elevated load so the user sees each phase
   will carry several lenses (no cap, just visibility).
4. **Iterate.** Fold the user's edits back in via the agent until they're
   satisfied. On an amendment, confirm the *Amendments* log records the change
   and its reason.
5. **Confirm.** Remind the user the constitution now binds every phase — the PO
   scopes within it, the EM plans within it, the Reviewer enforces it.

## Rules

- The constitution holds **principles and constraints**, never per-feature
  requirements — those belong in a spec. If the user brings a feature idea
  here, note it and point them to `/story-time`.
- The **active lenses** are the user's decision, like every other entry.
  Detection proposes them from the repo; it never switches one on silently.
  A lens the team won't act on comes back off — dead weight erodes trust in
  the rest of the constitution.
- Keep every entry falsifiable and true. Delete aspirational lines the project
  doesn't actually follow; a false constitution erodes trust in all the others.
- This is the user's document. You draft and challenge, but the user decides
  what the team is bound by.

## Handoff

- Constitution set → **`/story-time`** (spec the first feature within it) or
  **`/spark`** (run the full loop).
