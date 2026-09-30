# Release: campaign-core

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `preparing` |
| **Version** | v0.13.0 (proposed only, pr mode) |
| **Date** | 2026-09-30 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** Experimental, hand-started campaigns, Increment 1 of 3: format, extension rule, one kind (`migration-campaign`). Prepared, awaiting the user's go.
- **Open:** `3 outstanding` - the go to push/open the PR; rulings on local-token presence and ledger paths (see §3); Increments 2 and 3 are later features.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

Run fresh on HEAD `c9d7505` (0 behind / 11 ahead of `origin/main` `c5eb37d`).

- [x] `review.md` status `passed` (round 5; REVIEW GATE read)
- [x] `qa.md` status `passed` (round 3). Per the project's standing QA method (constitution §8, hands-on against the plugin), not a per-release override. User-accepted partials: AC-2.1, AC-5.4 (SR-9 half); B15 waived; B4/B9/B14/B16 accepted
- [x] Real bar (constitution §4): `claude plugin validate .` passes, one known warning (`autoUpdate`); no test suite exists
- [x] `git ls-files '*.py'` empty
- [x] Caps: `templates/campaign.md` 60/60, `campaigns/README.md` 87/90, `campaigns/migration-campaign.md` 64/90, standing rule 3/6
- [x] Diff vs `origin/main` over `skills agents ROADMAP.md .spark/constitution.md .claude-plugin`: empty before the bump; `templates/`: only `campaign.md` new
- [x] New relative links resolve (three `docs/status.md` links to other features' ledgers are pre-existing, not from this change)
- [x] Tracked files added: no secrets, no emails other than commit attribution
- [ ] Working tree: clean except untracked `.spark/.guard/`, `.spark/adversarial-gates/` (not in this release). **Ignored file `.claude/settings.local.json` holds a live API token** - §6 presence test, user to rule (§3)

## 2. Changelog

### Added
- **Campaigns (experimental, hand-started).** A second way of working next to the feature loop: one measurable goal you approve, a budget, stop rules, and a rollback path, run in iterations until the goal is reached or a rule halts it.
- **`migration-campaign`**, the first kind: move code in reversible slices, each checked by a fresh Parity Verifier.
- **A format and a contract for new kinds** (`templates/campaign.md`, `campaigns/README.md`, CONTRIBUTING section): a new kind is a new file, never an edit to an agent or skill.

### Changed
- README, project status and repo layout describe campaigns and their limits. Repos without `.spark/campaigns/` see no difference.

### Fixed
- Nothing.

### Limits, stated plainly
- The need is anticipated, not observed. Effectiveness is unmeasured. Tested on scratch fixtures, not a real project. One kind only. No external proof.
- Budgets and stop rules are followed by the agent, not enforced by Core (enforcement is `aspark-guard`'s concern).
- Start by naming `.spark/campaigns/<name>/campaign.md` and the plugin folder in your prompt. The ten ceremonies have no campaign logic; the standing rule for ordinary features is inert until routing ships.
- Measured: a kind with a missing key is reported malformed in 13 of 19 sessions. The SR-9 trip on a real diff is not verified live; SR-2/SR-6 only on planted history; SR-8 on an engineered state. Nothing detects an edit to an approved instance; overlapping slice paths are not flagged.
- Later features: Increment 2 (routing, standing rule), Increment 3 (project-local definitions, needs the user's constitution §3 amendment).

## 3. Release Actions

Mode `pr` (constitution §7). Ticket format `none`: no tracker call.

| Action | Result |
|---|---|
| Version bump & tag | Proposed only: 0.12.0 -> 0.13.0 (minor: new optional capability, nothing removed or renamed). `plugin.json` bumped locally; `marketplace.json` has no version field; tags `v0.12.0` = manifest, no disagreement. No tag before merge |
| PR / merge | Not opened. Pending on the user's go: `git push -u origin feat/campaign-core`; `gh pr create --repo a-lottes/aSPARK --base main --head feat/campaign-core --title "feat: campaign-core - experimental campaigns, increment 1 (v0.13.0)"` with the §2 changelog as body; then self-review request (approver `a-lottes`) and `claude plugin validate .` re-run. Merge and the real tag happen outside aSPARK's control |
| Deploy | N/A - handed-off, no deploy |
| Post-release smoke check | N/A - handed-off, no deploy |
| Rollback | Before merge: close the PR, delete the branch (`git push origin --delete feat/campaign-core` only with the user's go). After merge: `git revert -m 1 <merge-sha>` via a new PR; installs on 0.12.0 are untouched. If tagged: delete the tag only with the user's go. Nothing to migrate: additive Markdown |

Rulings the user owes before the go:
1. `.claude/settings.local.json` (ignored, never pushed) holds a live API token; a local-directory install copies ignored files (§3, §6). Move it out of the tree or rotate the token.
2. `evidence.md` (36 scratch paths under `/private/tmp/...`, `/Users/andreaslottes/` twice) and `qa.md` (once) quote the local username. Not a secret; 20+ shipped ledgers already do. Accept or scrub.
3. `.spark/campaign-core/` is 280 KB / about 2,760 lines (evidence 1,153, fixtures 685); other ledgers are comparable. Accept, or trim before merge.
Also untracked `.spark/.guard/` (logs, not ignored except `activity*`) and `.spark/adversarial-gates/` are excluded: the PR carries tracked commits only.

## 4. Learnings (Keep!)

- **What went well:** Dry runs found gaps every round, negative case first; the user's explicit rulings turned unfixable residue (13/19 detection) into honest documented partials.
- **What we'd do differently:** Stop at the 3-round rule sooner for a best-effort check; start the loop on a feature branch; pre-state which claims prompt material can only make likely, not certain.
- **Patterns worth reusing:** Prompt material makes a check likely, never certain: say so in the doc. Name the thing in the file the agent actually reads. Keep a re-derived disclosure at every gate. Candidates for CLAUDE.md: the first two.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time, except the token-presence item open for the user's ruling
- [x] Changelog written in user-facing language
- [ ] Release actions executed and verified: PR not yet open (awaiting go); rollback path written; Deploy and smoke check N/A
- [x] Learnings recorded
- [x] Line budget respected: Ist 86 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `handed-off` - pending: PR open, validate green, approver requested. Outstanding: the go (user); real merge and tag (`a-lottes`, outside aSPARK)
