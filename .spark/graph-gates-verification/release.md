# Release: graph-gates-verification

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 1) |
| **Status** | `handed-off` |
| **Version** | v0.7.1 (proposed — unbumped) |
| **Date** | 2026-08-27 |

**Handoff**
- **Status:** mirrors the header table above. **Handed off** — pushed, PR #29
  open on `main`; nothing further is this role's to do.
- **Summary:** Verify-only sweep closed #9/#11 live, confirmed #10's two MCP
  backends, refuted #8 with a routed Core doc finding; version stays 0.7.1
  (spec NFR-2 forbids bumping — the fence requires `plugin.json` byte-identical).
- **Open:** `1 outstanding` — the actual merge and any tag are the declared
  approver's own subsequent act (self-review via PR, sole maintainer
  `a-lottes`, constitution §7), outside this role's control. Nothing else
  is pending from this role.
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

**User's explicit go received** in this conversation to run the outward-facing
steps. Executed: `git push -u origin feat/graph-gates-verification` (new remote
branch, tracking set), then `gh pr create --base main --head
feat/graph-gates-verification --title "docs: verify-only sweep for graph tooling
gates (v0.7.1, unbumped)" --body ...` using §2's changelog, referencing #8, #9,
#10, #11 without closing keywords (closing issues is the user's own act, spec A5)
→ **PR #29**, https://github.com/a-lottes/aSPARK/pull/29.

**Post-push smoke check (pr mode — nothing deployed):** `gh pr view 29 --json
state,url,files,baseRefName,headRefName` → `state: OPEN`, `base: main`, `head:
feat/graph-gates-verification`, 7 files changed (README.md + the 6
`.spark/graph-gates-verification/**` files, this file included) — matches the
expected diff exactly. Fence re-confirmed on the pushed ref: `git diff --name-only
origin/main origin/feat/graph-gates-verification` returns the same 7 paths, no
capability file (`skills/ agents/ tools/ lenses/ templates/
.claude-plugin/plugin.json`) touched. `gh pr checks 29` → "no checks reported" (no
CI configured in this repo, consistent with constitution §4's no-test-suite
stance) — treated as vacuously satisfied, not silently skipped. Approver-requested:
this repo's declared approver model is self-review-via-PR, sole maintainer
`a-lottes` (constitution §7) — PR #29 being open on `main` *is* that request under
the declared model. Both the PR-open and approver-requested facts above were
established by a **read-only check I ran myself** (`gh pr view`), since I opened
the PR directly — not by relayed self-attestation.

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only, not applied** — v0.7.1 unbumped (justified above); no tag cut (pr mode) |
| Release commit | **Done, local** — `284f6ef` on `feat/graph-gates-verification` (cut fresh off `origin/main`, see above): README.md + `.spark/graph-gates-verification/{spec,plan,evidence,review,qa}.md` |
| PR / merge | **Done — PR #29 open on `main`.** https://github.com/a-lottes/aSPARK/pull/29. Merge itself is the declared approver's own subsequent act, outside this role's control |
| Deploy | N/A — no deploy target; documentation/evidence-only feature |
| Post-release smoke check | N/A for deploy (nothing deployed). PR-mode substitute performed and passed: PR confirmed genuinely OPEN with the exact expected 7-file diff; fence re-confirmed on the pushed branch |

## Rollback path

Now that the branch is pushed and the PR is open: `gh pr close 29` (closes the PR
unmerged, remote branch untouched) or, to remove the branch too, additionally
`git push origin --delete feat/graph-gates-verification`. Locally,
`git branch -D feat/graph-gates-verification` after either. Nothing has touched
`main` — no merge has happened — so `main` itself needs no unwinding. If a merge
does later happen (the declared approver's own act, outside this role), rollback
at that point is a standard revert PR of the merge commit; no tag exists to
unpublish since `pr` mode skips tagging before merge.

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
- [x] Release actions executed and verified (or `aborted` with reason) — PR #29
      open on `main`, confirmed via read-only `gh pr view` (state, files,
      base/head all match expected); no CI configured in this repo (vacuously
      satisfied, consistent with constitution §4); approver-requested is met
      under the declared self-review-via-PR model by the PR itself being open.
      Rollback path is written (above).
- [x] Learnings recorded
- [x] Line budget respected: Ist ~130 / Soll ~100 (excluding HTML comments) —
      over budget; the §3 smoke-check paragraph documenting how PR-open/CI/
      approver-requested were each established was kept in full rather than
      trimmed, since that provenance is exactly what a `pr`-mode gate is for.
      Recorded, not silently absorbed.
- [x] Status set to `released`, or `handed-off` in declared `pr` mode —
      **set to `handed-off`** (this repo's constitution §7 declares `pr`
      mode; never `released`). Outstanding: the real merge and any tag,
      owned by the declared approver (self-review via PR, sole maintainer
      `a-lottes`), entirely outside this role's control. This report
      describes a PR opened for review, not a shipped release.
