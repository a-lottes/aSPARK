# Project notes for Claude Code

Patterns worth keeping across SPARK loops, distinct from `.spark/constitution.md`
(which holds the project's standing principles) — these are working habits.

## Refuted-with-finding is a valid ceremony outcome

A verify-only sweep (or any test/verification-only feature) that finds a
documented claim does *not* hold live should record it as **refuted-with-finding**,
not silently pass it or fix it inline. Route the finding (verbatim quote,
`file:line`, cause) to wherever the actual fix belongs — often a later increment,
since a verify-only feature's own fence typically forbids touching the files the
fix would require. A failed acceptance criterion is itself a valid, honest
outcome; grinding to force a "confirmed" verdict defeats the point of verifying
at all. See `.spark/graph-gates-verification/evidence.md` (issue #8) for the
worked example.

## Check branch staleness before committing a new feature's work

Before `/increment` starts committing, or at the latest before `/go-live`'s
pre-flight, diff the current working branch against its own merge-base with
`main`. If the branch's prior PR already merged, cut a fresh branch off
`origin/main` for the new feature *before* work piles up on the stale one —
don't discover this at the last gate. `/go-live` for `graph-gates-verification`
had to resolve this as a surprise; catching it earlier (e.g. at `/spark`'s
resume, or `/increment`'s first commit) avoids the detour.

## Re-derive, don't cite, for evidence living outside this repo

When an AC's grounding fact lives in a sibling repo (another plugin's README,
its own evidence doc, its published test counts), each phase that verifies that
AC should re-fetch and re-check the fact itself, not trust the prior phase's
citation of it. A cited chain of citations is exactly how a stale or fabricated
claim survives three gates unnoticed — Specify may reasonably *relay* a fact it
has no tool to check, but Review and QA do have the tools, and re-deriving costs
one command. `companion-offer`'s `review.md` and `qa.md` each independently
re-fetched `aspark-guard`'s own README (via `gh api` and `curl` respectively)
rather than citing `evidence.md`, and both caught that its evidence needed to be
carried as *self-reported*, not restated as this project's own claim.

## Pin a repeated claim once, quote it everywhere it's needed

When a feature must state the same fact in more than one file (a maturity
label, a status line, a short description), write the canonical wording once in
the feature's `evidence.md` — long form and any declared short form — before
any prose lands, and have every later task quote that block rather than
re-derive or reword it from scratch. This is mechanically checkable for drift
(a `grep` across the touched files) and cheaper to fix than three independent
drafts converging by eye. `companion-offer`'s T1 did this for `aspark-guard`'s
qualified maturity statement across `README.md` (twice) and `ROADMAP.md`; only
one benign reordering slipped through, caught at `/peer-review`.
