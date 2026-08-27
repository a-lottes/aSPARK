# Release: graph-gates-verification

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 1) |
| **Status** | `preparing` |
| **Version** | v0.7.1 (proposed — unbumped) |
| **Date** | 2026-08-27 |

**Handoff**
- **Status:** mirrors the header table above. **Prepared, awaiting go** — local
  branch/commit done; nothing outward-facing has run.
- **Summary:** Verify-only sweep closed #9/#11 live, confirmed #10's two MCP
  backends, refuted #8 with a routed Core doc finding; version stays 0.7.1
  (spec NFR-2 forbids bumping — the fence requires `plugin.json` byte-identical).
- **Open:** `2 outstanding` — (1) user's explicit go to push/open PR; (2) the
  push target: a fresh branch `feat/graph-gates-verification` was cut off
  `origin/main` (see §3) because `feat/handbook-maturity`'s PR #27 already
  merged — the caller resolved this, recorded here for the record.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body wins except `Status`/`Version`; log the
  mismatch at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Run fresh, on commit `284f6ef`, just now — not copied from `review.md`/`qa.md`.*

- [x] `review.md` status is `passed` — round 2, `F1`-`F11` `fixed r2`, `F12`/`F13` fixed
- [x] `qa.md` status is `passed` — round 1, both review residues independently confirmed
- [x] Full test suite green — N/A (constitution §4, no test suite for prompt material); this
      feature's own evidence-bar substitute (`.spark/graph-gates-verification/evidence.md`)
      already ran under review+QA, not re-executed here (fix-nothing rule)
- [x] Build succeeds from clean checkout — N/A, no build step (docs/evidence-only diff)
- [x] No uncommitted changes in the working tree — `git status --porcelain` empty on
      `feat/graph-gates-verification` @ `284f6ef`
- [x] **Fence re-verified independently:** `git diff --name-only origin/main HEAD` =
      `README.md` + 5 files under `.spark/graph-gates-verification/**`, nothing else;
      `skills/ agents/ tools/ lenses/ templates/ .claude-plugin/plugin.json` byte-identical
      to `origin/main`; counts unchanged (10 skills / 7 agents); `plugin.json` still `0.7.1`

## 2. Changelog

### Added
- A written, run-by-run evidence record proving live what could previously only be
  claimed on paper about the optional dependency-graph tooling.

### Changed
- The project status page now states, with evidence behind each line, which of the
  optional graph tooling's promises hold up in practice and which don't yet.
- Both alternative browser-automation backends for the demo-review flow (Playwright
  and Chrome DevTools) are now confirmed to actually drive a page, not just named in
  the setup instructions.

### Fixed
- The "stop and tell me what to set up" message for a missing browser tool now stays
  reliable even when the optional graph tooling is otherwise available — one no longer
  quietly overrides the other.
- The "you have the tool but no graph built yet" reminder was confirmed to appear
  exactly once per run, never repeated and never nagging.

*(The MCP-first precedence claim was tested and did not hold reliably across runs —
recorded as a refuted claim with a named, unfixed documentation gap; not listed as
"Fixed" because nothing was changed to fix it in this diff.)*

## 3. Release Actions

**Branch situation resolved before any commit:** the working tree was still on
`feat/handbook-maturity`, but that branch's PR #27 was already merged into
`origin/main` (merge commit `085db99`) by a prior, unrelated release. Continuing
there would have bundled this feature into an already-closed PR. Verified
`git diff feat/handbook-maturity origin/main -- README.md` was empty (bases
match) before cutting a fresh branch: `git switch -c feat/graph-gates-verification
origin/main`, which carried this feature's uncommitted changes (README.md's
modification + the untracked `.spark/graph-gates-verification/` directory) onto it
cleanly — `git diff origin/main` on the new branch shows exactly those 6 files and
nothing from `feat/handbook-maturity`. That branch itself was left untouched at
its own tip (`59d14bc`).

**Version:** proposed **v0.7.1, unbumped**. The spec's own NFR-2 requires
`.claude-plugin/plugin.json` byte-identical to the pre-sweep state as part of the
verify-only fence (no shipped skill/agent/tool capability changed — only an
evidence record and one README paragraph). Bumping would itself violate the gate
`/peer-review` already checked. In `pr` mode this version is proposed only; no tag
is cut here (skipped per constitution §7 `pr` mode) — the real tag, if any, happens
at/after merge, outside this role's control.

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only, not applied** — v0.7.1 unbumped (justified above); no tag cut (pr mode) |
| Release commit | **Done, local** — `284f6ef` on `feat/graph-gates-verification` (cut fresh off `origin/main`, see above): README.md + `.spark/graph-gates-verification/{spec,plan,evidence,review,qa}.md` |
| PR / merge | **Not started — awaiting go.** Pending commands: `git push -u origin feat/graph-gates-verification`, then `gh pr create --base main --head feat/graph-gates-verification --title "..." --body "..."` |
| Deploy | N/A — no deploy target; documentation/evidence-only feature |
| Post-release smoke check | N/A — handed-off mode, nothing deployed; smoke check happens at merge, outside this role |

## Rollback path

Everything so far is local and unpushed: `git reset --hard origin/main` on
`feat/graph-gates-verification` (or simply delete the branch,
`git branch -D feat/graph-gates-verification`) fully undoes it with zero
external trace — nothing has left the machine. If the caller's later go is given
and the branch is pushed, rollback becomes `git push origin --delete
feat/graph-gates-verification` (deletes the remote branch before any PR merges)
or, once a PR is open, closing it unmerged. There is no scenario in this run where
`main` itself needs unwinding, since merge only happens at/after the declared
approver's own action, outside this role's control.

## 4. Learnings (Keep!)

- **What went well:** The verify-only fence was genuinely load-bearing — every
  claim in this feature traces to a performed step (command, transcript, or
  probe), and two full independent re-derivations (review round 2, QA) each
  re-walked raw transcripts rather than trusting prior narration, catching real
  gaps (F1–F13) before this gate.
- **What we'd do differently:** The release-commit branch should have been cut
  fresh the moment the prior feature's PR merged, not discovered as a surprise
  at `/go-live` — a `/go-live` pre-check that diffs the working branch against
  its own merge-base could catch "you're building on a closed PR" earlier in
  the loop, not at the last gate.
- **Patterns worth reusing:** The refuted-with-finding outcome (#8) is a clean
  template for "verification surfaced a defect, don't fix it here" — worth a
  short line in this repo's `CLAUDE.md`/constitution as the standard shape for
  future verify-only sweeps, alongside the two-paragraph fix F2/F3 already
  named for `tools/aspark-graph.md` and the three ceremony `SKILL.md` files as
  a candidate for the next increment (not this diff — the fence is verify-only
  and forbids touching `tools/`/`skills/`).

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time
- [x] Changelog written in user-facing language
- [ ] Release actions executed and verified (or `aborted` with reason) — **not
      applicable yet: prepared, not published.** In declared `pr` mode this box
      requires PR open on `main`, CI green, the declared approver requested —
      none of that exists yet because the outward-facing step has not run.
      Rollback path is written (above). Re-check this box once the go is given
      and the PR is actually open.
- [x] Learnings recorded
- [x] Line budget respected: Ist ~100 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode —
      **holds at `preparing`.** Outstanding: the user's explicit go for
      `git push` + `gh pr create`; owner = the caller, relaying that go from
      the user. Once given, the terminal status becomes `handed-off` (never
      `released` — this repo's constitution §7 declares `pr` mode), and even
      then the real tag/merge happens at/after the declared approver's own
      action (self-review-via-PR, sole maintainer `a-lottes`), outside this
      role's control.
