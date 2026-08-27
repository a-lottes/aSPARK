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
