# Release: project-kickoff

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3), `qa.md` (`passed`, round 1) |
| **Status** | `handed-off` |
| **Version** | v0.11.0 (proposed, `pr` mode — not tagged; PR [#50](https://github.com/a-lottes/aSPARK/pull/50) open against `main`) |
| **Date** | 2026-09-19 |

**Handoff**
- **Status:** `handed-off` — the release-prep commit is on `feat/project-kickoff`
  (pushed, `origin/feat/project-kickoff` tracking), and
  [PR #50](https://github.com/a-lottes/aSPARK/pull/50) is **open** against
  `main` (confirmed via `gh pr view 50`: `state: OPEN`, `baseRefName: main`,
  `headRefName: feat/project-kickoff`, `mergeable: MERGEABLE`,
  `isDraft: false`). `claude plugin validate .` is green on the pushed
  commit. The real merge and tag still happen outside this ceremony's
  control, so status stays `handed-off`, not `released`.
- **Summary:** `/charter` becomes the first-stop ceremony for a project with no
  constitution — a kickoff interview on an empty repo, a discovery pass on an
  existing one — and writes one bounded, evidenced Project Context that the PO
  and EM now cite instead of re-deriving. Both gates `passed`; minor bump
  `0.10.0` → `0.11.0` proposed; PR mode, PR open, published on the user's
  explicit go relayed this session.
- **Open:** `1 outstanding` — the declared approver (`a-lottes`,
  self-review-via-PR, constitution §7) still has to review and merge
  [PR #50](https://github.com/a-lottes/aSPARK/pull/50); the real tag is cut
  at/after that merge, outside this ceremony's control.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except
  `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and
  proceed — don't stop on it.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on `feat/project-kickoff` — not copied from
`review.md`/`qa.md`.*

- [x] `review.md` status is `passed` — round 3; REVIEW GATE (`review.md:130-136`)
      fully checked: 0 open Blocker/Major (two Minor/one Nit residue, all closed
      round 4); every Must AC traces; line budget 136/150.
- [x] `qa.md` status is `passed` — round 1; QA ran by the method constitution §8
      declares as this project's standing practice (no browser surface;
      substitute: hands-on QA against the installed plugin), not a per-feature
      waiver. QA GATE (`qa.md:171-182`) fully checked: all 12 Must ACs + all 8
      NFRs pass, 0 open Blocker/Major (1 Minor design question, non-blocking).
- [x] Full test suite green — N/A, no automated suite exists or is possible for
      prompt material (constitution §4). Substitute bar re-run fresh: `claude
      plugin validate .` → `✔ Validation passed with warnings` (one
      pre-existing, unrelated `autoUpdate` warning), on the actual merged
      release-branch tree, not the stale one review/QA ran against.
- [x] Build succeeds from a clean checkout — N/A, no build step; the `validate`
      run above is the equivalent bar and passed.
- [x] No uncommitted changes in the working tree — held throughout; the tree
      carried exactly the release commit plus the pre-existing, unrelated
      `.spark/.guard/` (aspark-guard's own ledger, out of this feature's
      scope) at every check, including immediately before pushing.

**Branch staleness found and resolved (this repo's own `CLAUDE.md` house
rule, re-checked live, not taken on trust).** The feature's work was sitting
uncommitted directly on local `main` (`56fa216`), which had drifted **8
commits behind `origin/main`** (`f67ef54`) — a whole sibling feature,
`lens-dispatch-registry`, had merged via PR #49 in the interim, touching 4 of
the same files this feature also touches (`README.md`,
`agents/facilitator.md`, `skills/spark/SKILL.md`, `templates/constitution.md`)
plus `.claude-plugin/plugin.json` (bumped there to `0.10.0`, not yet tagged).
Verified with a real 3-way merge test before building anything: **zero
conflicts** across all four overlapping files. The actual release branch,
`feat/project-kickoff`, was then built fresh off current `origin/main`
(stash → new branch → stash pop, both clean) rather than off the stale
local `main`, so the version bump and file state below are correct against
what `main` actually is, not what it was when review/QA ran. Re-verified on
this rebuilt tree, not assumed: NFR-1's five surface counts (10 skills / 7
agents / 9 lenses / 6 templates / 5 `/charter` steps, 0 new
`${CLAUDE_PLUGIN_ROOT}` paths) unmoved; both `§8`-by-number citations
(`skills/spark/SKILL.md`, `skills/demo-day/SKILL.md`) still resolve to `QA
Method`; `templates/constitution.md`'s `§1`–`§9` headings still in order,
`§9` still appended after `§8`, before Amendments.

**Re-confirmed immediately before pushing, per the caller's instruction:**
`git fetch origin` → `origin/main` still `f67ef54` (unmoved since the prepare
pass); `git branch --show-current` → `feat/project-kickoff`; `git log
--oneline -3` → exactly one commit (`180f23c`) ahead of `origin/main`;
`git merge-base feat/project-kickoff origin/main` → `f67ef54`, confirming
the branch is still built on the current tip, not a stale one; `git status
--porcelain` → only the pre-existing, unrelated `.spark/.guard/`. Nothing
had changed since the prepare pass.

## 2. Changelog

### Added
- `/charter` is now the natural first step on a brand-new project: on an
  empty repo it asks a short set of hard questions up front (who it's for,
  what they do today without it, the smallest version that would help, how
  you'll know it's working, your stack preference, any hard constraints, and
  what to build first) and drafts a starting constitution and first slice
  from your answers — offered for your go before anything else runs.
- On a project that already has code, `/charter` now runs a short discovery
  pass — reading your README, any `CLAUDE.md`, and existing specs — and
  writes back a bounded project summary (who it's for, the stack, how to run
  it, conventions, known pain points) that you review and correct once.
- The Product Owner and Engineering Manager now start each new feature from
  that shared project summary instead of re-reading the whole codebase from
  scratch every time, falling back to a fresh read only where the feature
  actually touches that area or the recorded picture is missing or in doubt.

### Changed
- The README now opens with a short "Start here" pointer to `/charter`, for
  both an empty project and one that already has code.

### Fixed
- Starting `/spark` or `/next-steps` on a project with no constitution used
  to leave you stuck between the two — each behaved as if the other had
  already set things up. Both now recommend `/charter` first, while still
  letting you skip it and continue exactly as before.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Proposed, pushed, not tagged.** `0.10.0` → `0.11.0` in `.claude-plugin/plugin.json`, in release commit `180f23c` on `feat/project-kickoff` (pushed to `origin`). **No tag created** (`pr` mode); the real tag is cut at/after merge, outside this ceremony's control. |
| PR / merge | **Opened.** [PR #50](https://github.com/a-lottes/aSPARK/pull/50), `feat/project-kickoff` → `main`. Established by a **read-only check I performed myself** (`gh pr view 50 --json url,state,baseRefName,headRefName,mergeable,isDraft,statusCheckRollup`), not self-attestation: `state: OPEN`, `baseRefName: main`, `headRefName: feat/project-kickoff`, `mergeable: MERGEABLE`, `isDraft: false`. Approver per §7: self-review-via-PR (`a-lottes`) — pending their own review and merge; no separate "request review" step applies (GitHub does not allow requesting review from the PR's own author, and the declared approver *is* the author here). Push and PR-open were executed on the user's explicit go, relayed by the caller this session. |
| Deploy | N/A — `pr` mode, no deploy (a Claude Code plugin ships via marketplace install, not a server deploy). |
| Post-release smoke check | N/A for a live app — `pr` mode, nothing was deployed. **What this pass does allow, performed:** confirmed the PR is real (above) and that no check shows broken — `statusCheckRollup: []`, which is correct, not a gap: `ls .github/workflows/` confirms this repo has **no CI workflow at all** (constitution §7), so an empty rollup is the expected state, not a missing signal. |

**Rollback path.** The 10 non-constitution files (README, ROADMAP,
`docs/workflow.md`, both skill files, three agent files,
`templates/constitution.md`) are additive prompt-text edits — a plain `git
revert <merge-commit>` on `main` removes them cleanly, no other side
effects. `.spark/constitution.md` is not as clean: this feature's own dated
Amendments rows (the §9 migration, and the two correction rows closing F11 /
F15 / F20) are real audit-trail entries recording decisions actually made
this cycle, not just the §9 content itself. A blanket revert of that file
would erase those records along with §9. If rollback is ever needed: revert
the other 10 files normally; for `.spark/constitution.md`, decide by hand
whether to (a) drop §9 while keeping the Amendments rows as history, noting
the rollback, or (b) accept losing that record with a full revert — that
choice belongs to whoever executes the rollback, not pre-decided here.
Reverting after merge would also need a follow-up on `.claude-plugin/plugin.json`'s
version (currently proposed `0.11.0`) and, if a tag was cut by then, a
decision on whether to yank or leave it — neither exists yet at this state.

## 4. Learnings (Keep!)

- **What went well:** Both gates were independently re-derived, not trusted
  forward — review round 3 and QA round 1 each re-checked prior rounds'
  claims against the live file rather than the notes, so pre-flight had
  nothing left to distrust on content; the only real finding this pass
  surfaced was git-positional (branch staleness), not a content defect.
- **What we'd do differently:** This feature's whole loop ran uncommitted,
  directly on local `main`, instead of on its own feature branch from the
  start — exactly what let `main` drift 8 commits (a full merged sibling
  feature) behind `origin/main` unnoticed until this gate.
- **Patterns worth reusing:** this repo's own `CLAUDE.md` "check branch
  staleness" rule names `/increment`'s first commit and `/spark`'s resume as
  the check points — this release shows it belongs at `/go-live`'s
  pre-flight too, and this time the drift collided with 4 of the files the
  feature itself touched, not just the branch tip. Candidate: widen that
  rule's own wording to name the release gate explicitly, and to recommend
  committing to a feature branch immediately rather than working uncommitted
  on `main`. Also worth keeping: re-confirming branch/`origin` state
  immediately before the outward-facing push, not just at prepare time — it
  cost one `fetch` and caught nothing this time, but it is the check that
  would have caught it had `origin/main` moved again in the gap.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time — including the
      branch-staleness discovery, resolved by rebuilding the release branch
      off current `origin/main` and re-verifying every structural fact review/
      QA relied on, not by patching content; re-confirmed unchanged
      immediately before the push
- [x] Changelog written in user-facing language — no commit hashes, ticket
      IDs or `AC-`/`F-`/`T-` IDs in §2
- [x] Release actions executed and verified (or `aborted` with reason) — `pr`
      mode: PR [#50](https://github.com/a-lottes/aSPARK/pull/50) open on
      `main`, established by a read-only `gh pr view` check I performed
      myself (not self-attestation); no CI configured in this repo so no
      check can show broken, confirmed by `ls .github/workflows/`; approver
      (`a-lottes`, self-review-via-PR) is the PR's own author, so "requested"
      reduces to "the PR is open and theirs to act on" — no separate GitHub
      action applies; rollback path written; Deploy and Post-release smoke
      check correctly N/A
- [x] Learnings recorded
- [x] Line budget respected: Ist 168 / Soll ~100 — over, for a stated reason:
      this feature carries 5 stories / 24 ACs / 8 NFRs (over double a typical
      feature), this pass documented a real branch-staleness finding and its
      resolution in full, and this update pass added the real PR verification
      and re-confirmation evidence rather than compressing it away; not
      waived by the user, recorded here with its reason per the template's
      own allowance
- [x] Status set to `handed-off` — **stays `handed-off`, not `released`,
      even with the PR open** (constitution §7: the real merge and tag
      happen outside this ceremony). **What remains outstanding:** the
      declared approver (`a-lottes`, self-review-via-PR) still has to review
      and merge [PR #50](https://github.com/a-lottes/aSPARK/pull/50); the
      real tag is cut at/after that merge, both outside this ceremony's
      control
