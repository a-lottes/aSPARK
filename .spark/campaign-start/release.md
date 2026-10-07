# Release: campaign-start

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `handed-off` |
| **Version** | v0.14.0 (tag `v0.14.0` exists, on the release commit; see §3) |
| **Date** | 2026-10-07 |
| **Ticket** | none |
| **Commit** | `1ce9dc6` (release commit); merged as `2ba7629` (merge commit `2ba7629a4d26068b0b1efa91efbfd98342515cef`) |
| **PR** | https://github.com/a-lottes/aSPARK/pull/72 (merged 2026-10-07T19:22:36Z) |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** Adds the optional `/campaign <name> [kind]` command, which writes a draft campaign file and stops. Pushed, PR #72 opened and merged into `main` (2ba7629); tag `v0.14.0` pushed on the release commit.
- **Open:** `1 outstanding` — the tag `v0.14.0` points at the release commit `1ce9dc6`, not the merge commit `2ba7629` (precedent v0.13.1 tags the merge commit); recorded, not re-tagged. Pushing this record (branch `docs/v0.14.0-released`) and its PR await the user's go.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

<!-- Run 2026-10-07 on branch feat/campaign-start, fresh, not copied. -->

- [x] `review.md` status is `passed` (round 2; REVIEW GATE all 7 boxes checked; open: F8 Minor routed to a later `/charter`, F12 Nit accepted)
- [x] `qa.md` status is `passed` (round 2; QA GATE all 7 boxes checked). Per `.spark/constitution.md` §8, QA ran by the project's standing declared method (hands-on QA against the installed plugin), a standing project fact, not a per-feature override. Exception pre-declared in plan D8: AC-4.3, closed below
- [x] Full test suite green: none exists (no runtime); the project's bar is `claude plugin validate .` = "Validation passed with warnings" (one warning, pre-existing: `CLAUDE.md` at the plugin root); `git ls-files '*.py'` empty
- [x] Build succeeds from a clean checkout: nothing to build (Markdown + JSON); validate above is run on this tree
- [x] No uncommitted changes: `git status --short` showed only the unrelated untracked `.spark/.guard/` (left alone)
- [x] Branch current: `git rev-list --left-right --count origin/main...HEAD` = `0 23` after `git fetch`; merge-base `460d6fc`; `git merge-tree --write-tree origin/main HEAD` clean
- [x] `skills/campaign/SKILL.md`: no TODO/TBD/FIXME (the word "placeholder" there is the skill's own vocabulary); 75 lines vs cap 70, yield recorded in plan Deviations
- [x] Constitution §2/§9 say eleven (Amendments row 2026-10-05, AC-4.4); `ls skills` = 11 folders
- [x] AC-4.3 verified after the bump (observed, below)

**AC-4.3 evidence** (after editing `.claude-plugin/plugin.json`, the only file that versions; `marketplace.json` has no version field; no README or docs mention a version):
- `grep '"version"' .claude-plugin/plugin.json` -> `"version": "0.14.0",`
- `git show origin/main:.claude-plugin/plugin.json | grep '"version"'` -> `"version": "0.13.1",`
- `git diff -U0 .claude-plugin` -> exactly one line changed, `0.13.1` -> `0.14.0`; `python3 -c` JSON parse prints `0.14.0`; `claude plugin validate .` still passes with the same one warning
- Result: pass, a minor bump with nothing renamed or removed

## 2. Changelog

### Added
- A new optional command, `/campaign <name> [kind]`, starts a campaign for you. You no longer name the plugin folder or build the file by hand: it reads the available kinds and the template itself, asks only what the chosen kind leaves open, and writes one draft at `.spark/campaigns/<name>/campaign.md`.
- It stops at the draft. The draft is marked `draft`, the approval and the veto record stay blank, nothing is committed, and the closing message lists what is still unfilled and which session to run next. Approving and running a campaign remain your steps.
- It is instructed to refuse, writing nothing, when the goal is not measurable, when you give several goals, when no kind fits, when the name is invalid or already taken, or when a kind is missing a required key.

### Changed
- The README and the campaigns guide now present `/campaign` as the way to start one; hand-starting still works, and running a campaign is still done by hand.
- The docs now count eleven commands in total; the loop itself still has ten ceremonies.

### Fixed
- Nothing fixed; this release only adds. Limits to know: these checks are prompt material, so they make the behavior likely, never certain. In testing, a kind with a missing key was caught in 24 of 24 sessions but only after a fix (1 of 5 before it). A goal that is not measurable was refused 5 of 5, several goals 5 of 5, a taken name 5 of 5. Known small gaps, accepted: some drafts keep the placeholder title (5 of 16), the note about other running campaigns was missed once in 7, and the closing sentence is sometimes worded differently (4 of 5 verbatim). No campaign has run on a real project yet, and its real-world effectiveness is unmeasured.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | Bumped 0.13.1 -> 0.14.0 in `.claude-plugin/plugin.json` (release commit `1ce9dc6`). Minor: one new optional command, nothing renamed or removed (spec AC-4.3, plan D8, semver). Annotated tag `v0.14.0` (tag object `4c5fca0`) is pushed (`git ls-remote`) and points at `1ce9dc6`, **not** the merge commit `2ba7629`. v0.13.1 tags its merge commit (`9536fa1`); this deviates and is recorded, no re-tag. |
| PR / merge | Repo `a-lottes/aSPARK`. Branch `feat/campaign-start` pushed; PR https://github.com/a-lottes/aSPARK/pull/72 opened and merged 2026-10-07T19:22:36Z as a regular merge commit `2ba7629` (`gh pr view 72`: state MERGED). Approver `a-lottes` (self-review via PR). |
| Deploy | N/A — handed-off, no deploy |
| Post-release smoke check | Run 2026-10-07 on `origin/main` @ `2ba7629` (detached scratch worktree, not in `~/aSPARK`): `plugin.json` version `0.14.0`; `claude plugin validate .` = "Validation passed with warnings" (same one pre-existing `CLAUDE.md` warning); `skills/campaign/SKILL.md` present; `.py` files on `origin/main` = 0. Real `claude -p "/campaign smoke-x"` with `--plugin-dir` in a fresh scratch git repo: first run stopped for lack of read access to the plugin dir and wrote nothing; rerun with `--add-dir` read the kind, found the name free, proposed the one kind `migration-campaign`, asked what it leaves open (no goal given, so none invented) and wrote nothing (`git status` clean, no files). Command responds. |

**Rollback path:** before merge, nothing is published: `git reset --hard 6b7af60` on the branch drops the release commit, or close the PR and delete the remote branch (`git push origin --delete feat/campaign-start`). After merge, `git revert -m 1 2ba7629` through a PR restores `0.13.1` and removes the command (additive release, no data migration); users already on `0.14.0` update to the reverting version. Campaign drafts users already wrote are plain files and stay valid for hand-running.

## 4. Learnings (Keep!)

- **What went well:** Round 2 QA re-derived every row from fresh sessions and caught a real Major (B1, key check) that round 1 missed; the rates in the README are now measured n of m, honestly labelled best effort. Deferring the version bump to `/go-live` (D8) kept AC-4.3 an honest not-verified-live until it could be observed.
- **What we'd do differently:** Put the skill's own line cap yield (75 vs 70) into the plan up front. Add a `/campaign` NFR-7 re-run when a fix pass touches nearby text. Cut the feature branch at the first write rather than late.
- **Patterns worth reusing:** (proposals for CLAUDE.md, not applied) (1) "A release-time acceptance criterion is verified by the Release Manager with observed output after the act, and QA records it not-verified-live rather than passing it." (2) "Put the load-bearing check first in the agent's reply (the kind check before the goal is used): the same check moved to open the reply went from 1 of 5 to 24 of 24." (3) "Report prompt-material rates as n of m by round in one place, not two unlabelled figures (QA B7)."

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time
- [x] Changelog written in user-facing language
- [x] Release actions executed and verified (or `aborted` with reason) — in declared `pr` mode: PR open on the target branch, validate passing, the declared approver requested, rollback path written; Deploy N/A. PR #72 merged (read-only `gh pr view`), validate passes on `origin/main`, post-release smoke check done (§3). Tag sits on `1ce9dc6`, a recorded deviation
- [x] Learnings recorded
- [x] Line budget respected: Ist 83 / Soll ~100 (excluding HTML comments), self-reported; the changelog's honest limits bullet is the longest line
- [x] Status set to `handed-off` — outstanding: this record's own push and PR (awaiting the user's go); the tag/merge happened outside aSPARK's control (user), owned by `a-lottes` (declared approver). Not a direct-mode deploy.
