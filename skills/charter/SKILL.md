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

1. **Locate.** If `.spark/constitution.md` exists, this is an **amendment** —
   read it first and preserve everything the user isn't changing. If not, this
   is a **first draft** from the template at
   `${CLAUDE_PLUGIN_ROOT}/templates/constitution.md`.
2. **Learn the terrain.** Read the project's README, existing `.spark/` specs
   and enough code to infer the real stack, conventions and quality practices.
   Propose a draft grounded in what the project already is — do not invent
   principles the code contradicts.
3. **Interview, don't dictate.** Walk the five sections (product principles,
   technical constraints, quality bars, conventions, non-negotiables). For
   each, propose a concrete default from what you found and ask the user to
   confirm, sharpen, or cut. Use AskUserQuestion where the choices are
   enumerable. Keep it short — a constitution nobody reads is dead weight.
4. **Write it.** Save to `.spark/constitution.md` following the template. On an
   amendment, add a dated row to the *Amendments* log with the reason.
5. **Confirm.** Show the user the final constitution and remind them it now
   binds every phase — the PO scopes within it, the EM plans within it, the
   Reviewer enforces it.

## Rules

- The constitution holds **principles and constraints**, never per-feature
  requirements — those belong in a spec. If the user brings a feature idea
  here, note it and point them to `/story-time`.
- Keep every entry falsifiable and true. Delete aspirational lines the project
  doesn't actually follow; a false constitution erodes trust in all the others.
- This is the user's document. You draft and challenge, but the user decides
  what the team is bound by.

## Handoff

- Constitution set → **`/story-time`** (spec the first feature within it) or
  **`/spark`** (run the full loop).
