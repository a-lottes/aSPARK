# Release: lens-dispatch-registry

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 1) |
| **Status** | `preparing` |
| **Version** | v0.10.0 (proposed, `pr` mode — no tag before merge) |
| **Date** | 2026-09-17 |

**Handoff**
- **Status:** `preparing` — this is an explicit prepare-only pass. A local release-prep commit (version bump `0.9.0`→`0.10.0` + this report) sits on `feat/lens-dispatch-registry`; nothing pushed, no PR opened. Outward-facing steps await the caller's explicit go.
- **Summary:** Six sites across five files now read the lens/characteristic vocabulary from `lenses/README.md`'s registry instead of a hardcoded list, so the accessibility lens — and any future lens — is reachable via `/charter` and dispatched at every phase its own frontmatter claims. Closes `accessibility-lens`'s routed NFR-6 finding (`refuted-with-finding`). Both gates `passed`; minor bump proposed.
- **Open:** `2 outstanding` — (1) push branch, open PR, request self-review — owner `a-lottes`, outside this ceremony, pending the go. (2) `origin/main` advanced by one unrelated merged PR (#48, `docs/aspark-family`, README.md only) since this branch's merge-base; confirmed conflict-free by dry-run `git merge-tree`, but re-check immediately before pushing in case anything else lands — owner: whoever executes the publish step.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on `feat/lens-dispatch-registry` at `de5de95` — not copied from `review.md`/`qa.md`.*

- [x] `review.md` status is `passed` — REVIEW GATE at `review.md:138-149` read fresh: no open Blocker/Major (F1, the only Major, `fixed r2`, re-verified against source, not the fix-mode ledger), all plan deviations documented (T10/F2), line budget 149/150, status `passed`.
- [x] `qa.md` status is `passed` — QA GATE at `qa.md:60-68` read fresh: all 10 Must ACs + all 3 QA-owned NFRs verified (13/13 ✅), no open Blocker/Major, status `passed`. **QA method:** constitution §8 carries a complete declaration (surface `no`, substitute method named — hands-on QA against the installed plugin) — QA ran by that declared method as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID it owns, same as always.
- [x] Full test suite green — N/A, none exists or is possible for prompt material (constitution §4). Substitute bar re-run fresh just now: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning, unrelated to this diff, present on every prior release).
- [x] Build succeeds from a clean checkout — N/A, no build step (constitution §3/§4); `claude plugin validate .` is the equivalent bar and passed, above.
- [x] No uncommitted changes in the working tree — `git status --porcelain` / `git diff --stat HEAD` both empty for tracked files. One pre-existing, out-of-scope untracked directory, `.spark/.guard/` (the optional `aspark-guard` companion plugin's own session ledger, named out of scope by this feature's own `spec.md` §6) — not staged, not part of this release.

**Branch staleness (project `CLAUDE.md` house rule, re-checked live, not taken on trust).** `git fetch origin` then `git rev-parse main origin/main` → both `56fa216`, but `git merge-base HEAD origin/main` → `5962f55`, an ancestor of `56fa216`. `origin/main` moved (PR #48, `docs/aspark-family`, README.md-only) **after** this branch was cut — the caller's "no staleness to resolve" was accurate earlier this session but is superseded. `git merge-tree 5962f55 HEAD origin/main` → **zero conflicts**: PR #48 touches `README.md:92-252`, this feature touches `README.md:318-346`, non-overlapping. No rebase required for a clean PR merge; the note above stands as a re-check-before-push item, not a blocker.

**Diff re-derived fresh, not cited.** `git diff main...HEAD --numstat -- ':!.spark'` → **10 files, +90/−59**. `review.md`/`qa.md` cite `+88/−59` for the same 10 files — a minor recount variance (2 insertions) that changes no verdict: same file set, same NFR-6 conclusion (every dispatch set a strict superset, no protected structure touched, additive).

**Version confirmed pre-bump.** `.claude-plugin/plugin.json` read directly at `de5de95`: `"version": "0.9.0"`, untouched by this feature's diff.

**Version bump justification (one line).** Minor: `0.9.0` → `0.10.0` — additive fix to lens dispatch/activation (constitution §5's "new optional capability" test and NFR-6's superset test both point the same way: no protected template heading/column/ID pattern, slash command, or consumed-contract path renamed or removed; every phase's dispatch set strictly widens).

## 2. Changelog

### Added
- Nothing net-new to turn on — no new lens, no new command.

### Changed
- Setting up a project (`/charter`) now offers every accessibility-style option it actually knows about, sourced from the same list the rest of the loop uses, instead of a fixed short list that could quietly leave a real option out.
- Design review, code review and testing now always pick up every check a project has turned on — adding a new check in the future takes effect everywhere at once, with no separate update needed to make it actually run.

### Fixed
- The accessibility check (added in the previous release) could be turned on for a project yet still silently not run during design review and testing. It now runs every time, exactly as project setup promised.

## 3. Release Actions

*Prepared, not executed — prepare-only pass per explicit instruction. Outward-facing steps require the user's explicit go, not yet relayed.*

| Action | Result |
|---|---|
| Version bump & tag | **Applied:** `0.9.0` → `0.10.0` in `.claude-plugin/plugin.json` (see justification above). No tag — `pr` mode creates the tag at/after merge, outside this ceremony's control. |
| PR / merge | **Not opened.** Prepared locally only; commands below are pending the user's go. |
| Deploy | N/A — no deploy surface; consumers pull via `/plugin install` / marketplace update, not a push from here. |
| Post-release smoke check | N/A — `pr` mode, nothing pushed or merged yet. Local analogue (`claude plugin validate .`) already re-ran fresh above and passed. |

**Exact release-prep commit (about to be created):**
```
chore: prepare lens-dispatch-registry release, propose v0.10.0 (pr mode, awaiting go)

Bumps .claude-plugin/plugin.json 0.9.0 -> 0.10.0 (minor: additive fix to
lens dispatch/activation per NFR-6 -- every phase's dispatch set is a
strict superset of what it replaced, no protected template
heading/column/ID pattern or slash command touched). review.md (passed,
round 2) and qa.md (passed, round 1) both fresh-verified green at
pre-flight; claude plugin validate . re-run clean (one pre-existing,
unrelated warning). Branch is one merged PR behind origin/main (#48,
docs/aspark-family, README.md-only) but a dry-run git merge-tree shows
zero conflicts against the current diff. No tag, no push, no PR yet --
pr mode, prepared and awaiting the user's explicit go. See
.spark/lens-dispatch-registry/release.md.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
Files: `.claude-plugin/plugin.json`, `.spark/lens-dispatch-registry/release.md`.

**Exact publish commands, pending the user's go (none executed):**
```
git push -u origin feat/lens-dispatch-registry

gh pr create --title "fix: make lens dispatch and /charter activation registry-driven" \
  --base main --head feat/lens-dispatch-registry --body "$(cat <<'EOF'
## Summary
- Six sites across five files (agents/facilitator.md,
  templates/constitution.md, skills/look-and-feel, skills/demo-day,
  skills/peer-review -- plus skills/spark and templates/spec.md folded
  in) now read the lens/characteristic vocabulary from
  lenses/README.md's registry instead of a hardcoded list, closing
  accessibility-lens's routed NFR-6 finding (refuted-with-finding).
- Any lens registered in lenses/README.md -- present or future -- is
  now discoverable through /charter and dispatched at every phase its
  own frontmatter claims, with zero further edit to the three phase
  skills, agents/facilitator.md, or templates/constitution.md.
- Proposes a minor bump, 0.9.0 -> 0.10.0 (additive fix, NFR-6).

## Test plan
- [x] review.md passed, round 2 (F1 Major fixed and independently
      re-verified against source; F8/F9 Nits closed)
- [x] qa.md passed, round 1, 10/10 AC + 3/3 QA-owned NFR verified
      hands-on against the installed plugin
- [x] claude plugin validate . passes locally (re-run at /go-live
      pre-flight; one pre-existing, out-of-scope warning)
- [x] Dry-run git merge-tree against current origin/main: zero conflicts
- [ ] Self-review and merge by the declared approver (a-lottes)
EOF
)"
```

**Rollback path.** Purely additive (NFR-6): no protected template structure, slash command or consumed-contract path is renamed or removed. Before merge: don't merge / close the PR — `origin/main` stays unaffected. After merge: `git revert -m 1 <merge-commit-sha>` on `main` restores all 10 files and reverts `.claude-plugin/plugin.json` to `0.9.0` in one commit; no tag exists yet to delete (`pr` mode cuts the tag at/after merge). Safe because every dispatch set this fix produces is a strict superset of what it replaced — reverting returns every consumer to exactly its prior (narrower) behavior, never a broken one.

## 4. Learnings (Keep!)

- **What went well:** NFR-6's superset/additive framing let Review and QA both independently re-derive compatibility with no code to run; round 2's self-correction (F2) shows the loop catching its own drift within one fix pass rather than needing a third round.
- **What we'd do differently:** round 2's fix for F2 restated a file/line count in the present tense and still undercounted by one file (`agents/qa-tester.md`) — pin a diff's file/line counts to a commit SHA the first time the number is asserted, not only after a correction. This ceremony repeats that discipline at pre-flight (10 files, +90/−59, pinned to `de5de95` above).
- **Patterns worth reusing (candidates for `CLAUDE.md`):** `git merge-tree <merge-base> HEAD origin/main` as a cheap, non-destructive staleness/conflict check at `/go-live` pre-flight, run every time regardless of an earlier "confirmed synced" claim in the same session — it caught a real drift here (PR #48 landed mid-session) that trusting the earlier claim would have missed.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time (§1, all five, plus the branch-staleness and diff re-derivation notes, re-run on `de5de95`)
- [x] Changelog written in user-facing language (§2 — no commit hashes, ticket IDs or internal jargon)
- [ ] Release actions executed and verified — **not applicable yet by design.** This is a prepare-only pass: the local release-prep commit is made, rollback path is written (§3), but no push/PR has happened and none should until the user's explicit go is relayed. Deploy and post-release smoke check are correctly N/A.
- [x] Learnings recorded (§4)
- [x] Line budget respected: Ist 96 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `released`/`handed-off` — **not yet; `preparing` is correct for this pass.** Outstanding: push + open PR + request self-review from `a-lottes` (outward-facing, needs the user's go); the real tag/merge happen after that, outside this ceremony's control.
