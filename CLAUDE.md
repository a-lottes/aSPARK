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

## An add-a-file scope check must examine every phase the artifact claims

When planning a new lens (or any artifact whose frontmatter declares which
SPARK phases it owns), verify dispatch **and activation** for every one of
those phases at plan time — not just the phase that happens to already be
wired generically. `accessibility-lens`'s plan checked only `/increment`
(found clean, C6) and stopped; `/peer-review` then had to discover, across
two separate rounds, that `/look-and-feel`, `/demo-day`, `/peer-review`'s own
dispatch parenthetical, and even `/charter`'s activation vocabulary
(`agents/facilitator.md`, `templates/constitution.md`) all shared the same
closed-enumeration defect. Checking every claimed phase's dispatch *and* how
its trigger gets declared in the first place — at Plan, not Review — would
have caught 4 of 5 sites before the diff ever reached a reviewer. See
`.spark/accessibility-lens/evidence.md` (T7, extended at review round 1) for
the worked example.

## A disclosed limitation stays honest only if re-verified at every gate

A `refuted-with-finding` (or any other honestly-disclosed gap) recorded once
does not stay accurate on its own — re-derive it fresh at each subsequent
gate rather than citing the prior gate's word for it. `accessibility-lens`'s
NFR-6 disclosure (a 5-site dispatch/activation gap) was independently
re-verified from primary source four separate times across one loop — plan,
review round 1, review round 2, and QA — with zero drift in either the
`file:line`s or their consequence. That is what kept the disclosure from
going stale between Plan and release; a single write-up trusted forward
would not have caught a fix pass narrowing a citation range by one line
(review round 2's own F9) or a wording change elsewhere going unnoticed.

## Re-check branch staleness with `git merge-tree` right before pushing, not just once

An earlier "confirmed synced with `origin/main`" claim in the same session
can go stale by the time `/go-live` actually pushes — another branch can
merge in the interval, especially in a repo where multiple sessions or
agents share the same working directory. `git merge-tree <merge-base> HEAD
origin/main` is a cheap, non-destructive way to check for real conflicts
(not just "is main ahead") at `/go-live` pre-flight, and it's worth running
twice: once when the release is prepared, and again immediately before the
actual `git push`, rather than trusting the first check. `lens-dispatch-
registry`'s release caught `origin/main` moving one merged PR ahead (#48)
between an earlier in-session "main is synced" check and pre-flight — the
`merge-tree` re-run showed zero conflicts (non-overlapping file regions), so
the push proceeded with actual evidence instead of a stale assumption. See
`.spark/lens-dispatch-registry/release.md` §1 for the worked example.

## Pin a diff's file/line counts to a commit SHA the first time they're asserted

A count like "N files changed, +X/−Y" drifts the moment another commit lands
on the same branch — stating it as a bare present-tense fact invites the next
reader (or the next round) to trust a number that's already gone stale, and
a later "correction" can repeat the same mistake by restating the count in
present tense again instead of anchoring it. Write the count with the commit
SHA it was true at from the very first assertion, not only after a fix.
`lens-dispatch-registry`'s round-2 review fix-mode pass corrected an
undercounted file list (F2) but restated the new count in present tense too
— and still undercounted by one file, since the fix commit's own edit
wasn't included. The re-review caught it and pinned the final count to the
exact commit SHA. See `.spark/lens-dispatch-registry/review.md` (F2) for the
worked example.
