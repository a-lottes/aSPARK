# Release: adversarial-gates

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `preparing` |
| **Version** | v0.13.1 (proposed only; no tag before merge) |
| **Date** | 2026-10-04 |
| **Commit** | `<filled after the release commit and push>` |
| **PR** | `<filled after the PR is opened>` |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** Increment 1 of 2, docs and evidence only: a search of the repo's own trails for gate evasions found one, too few to justify rebuttal rows, so none shipped and no skill changed.
- **Open:** `1 outstanding` - the user's go for push and PR; then merge and the real tag `v0.13.1` by the maintainer (`a-lottes`, self-review via PR), outside aSPARK's control. Also the user's ruling on untracked `.spark/.guard/` (§1).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

Run fresh on branch `feat/adversarial-gates`, head `cfc7412`; `origin/main` = `fa33f2c` after `git fetch` = merge-base, so 0 behind, not stale.

- [x] `review.md` status `passed` (round 2; REVIEW GATE: all 7 boxes checked)
- [x] `qa.md` status `passed` (round 1; QA GATE: all 7 boxes checked). QA ran by the project's standing method (constitution §8, hands-on against the installed plugin), not a per-release override
- [x] Real bar (constitution §4, no test suite): `claude plugin validate .` -> "Validation passed with warnings" (one warning: `CLAUDE.md` at plugin root is not loaded as context; pre-existing)
- [x] `git ls-files '*.py'` empty
- [x] `git diff origin/main -- skills agents templates lenses` is 0 lines (nothing consumers run changed)
- [x] Version lives in one place: `.claude-plugin/plugin.json`; `marketplace.json` has no version field; no CHANGELOG file exists
- [ ] Working tree: clean except untracked `.spark/.guard/` (below). Open for the user's ruling

**`.spark/.guard/` presence check.** Not in this feature's diff. Contents: `ledger.jsonl` (117 KB) and `trail.jsonl` (19 KB), the aspark-guard write log (agent, feature, path, sha256, timestamps, session ids, from 2026-09-18 on). Its own `.gitignore` ignores only itself and `activity*`, so those two files are **not ignored**: `git add -A` or `git add .spark` would commit them, and with `source: "./"` they would then ship to every installer. The release commit adds named paths only, so it does not include them, and neither does the PR. No secrets matched (`sk-`, token, api_key, password: 0 hits). The decision to ignore, delete or commit them is the user's.

## 2. Changelog

Docs and evidence only. No skill, agent, template or lens changed; installed projects behave exactly as before.

### Added
- **Gate-evasion search.** A recorded search of this repo's own 51 review, QA and evidence files for cases where an agent got past a gate. It found one clear case; the bar for adding a defensive rule was two at the same gate, so none was added.
- A README section, roadmap entry and status row that say this plainly.

### Changed
- The roadmap item formerly titled "Anti-rationalization tables at every gate" is renamed "Stricter verdict rules for review and QA" and marked planned, not built.

### Fixed
- Nothing.

### Limits, stated plainly
- No rebuttal rows shipped and no verdict rule changed. Stricter verdict rules are planned only.
- The evidence is this repo's own trails, not field reports. The search used fixed terms and is not a census. Effectiveness is unmeasured.
- Gates remain prompt-enforced; code-level enforcement is the optional `aspark-guard` sibling's concern.

## 3. Release Actions

Mode `pr` (constitution §7). Ticket format `none`: no tracker call.

| Action | Result |
|---|---|
| Version bump & tag | Proposed 0.13.0 -> 0.13.1 in `plugin.json`, committed locally. Patch: the release is docs and evidence only with no behaviour change. Recorded plainly: the spec (NFR-4, C8) called for a minor bump per increment; the user chose patch at the go gate (a user decision, recorded). No tag: the real tag v0.13.1 is created after merge, outside aSPARK |
| PR / merge | Not opened. Pending the user's go (commands in the caller's report). Approver: self-review via PR (`a-lottes`), per §7. No CI exists (no workflows) |
| Deploy | N/A - handed-off, no deploy |
| Post-release smoke check | N/A - handed-off, no deploy |
| Rollback | Before merge: close the PR, delete the remote branch (only with the user's go). After merge: `git revert -m 1 <merge-sha>` via a new PR; installs on 0.13.0 are untouched, and nothing runs differently, so no migration. If the tag was created after merge: delete it only with the user's go |

## 4. Learnings (Keep!)

- **What went well:** The search rules were committed before the scan, so a one-entry result could be reported as refuted-with-finding instead of being rounded up. Two review rounds re-derived quotes from source and caught a wrong E2 premise.
- **What we'd do differently:** Count scope files at plan time (folder count was wrong once). Run the loop on a feature branch from the first write.
- **Patterns worth reusing:** Commit the search method before the results. A release commit adds named paths, never `-A`, while untracked logs sit in `.spark/`. Candidate for CLAUDE.md (offer only): the `.spark/.guard/` log files are not ignored and `source: "./"` ships `.spark/`; ignore them or add paths by name.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time, except the `.spark/.guard/` ruling open for the user
- [x] Changelog written in user-facing language
- [ ] Release actions executed and verified: not yet; prepared, awaiting go (push, PR, approver request). Rollback path written
- [x] Learnings recorded
- [x] Line budget respected: Ist 81 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `handed-off` after the PR is open; outstanding: PR, merge and real tag, owned by `a-lottes` outside aSPARK's control
