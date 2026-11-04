# QA Report: visual-qa-review

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Scratch apps under /tmp/scr (not committed), `.spark/visual-qa-review/spec.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-30 |

**Handoff**
- **Status:** mirrors the header table above.
- **Verdict:** Every AC has a performed dry run. `claude plugin validate .` could not run; the gate closes on a waiver of that step, selected automatically by the Factory in autonomous mode (not a personal user confirmation). A person reviewing the PR must run it.
- **Open:** `none` — B1 (Minor, validate not run) accepted by the Factory-selected waiver
- **Binding ruling:** §5 Verdict and the gate below
- **On conflict:** the numbered body wins for everything except `Status`.

Anti-generosity standard applied. Mode: live browser runs of the changed QA Tester on scratch apps (Playwright), one session per case; this repo itself has no browser surface, so the dry runs in `evidence.md` are the test.

## 1. Test Environment
- **QA method:** the declared substitute method of `.spark/constitution.md` §8 (a real ceremony invocation, observed output). URL, browser and viewport fields are N/A for this repo; the dry runs used a scratch app on http://localhost:8765 at 1280x800 and 390x844 and a scratch CLI project.
- **Test data:** seeded deviation (D1), decision (C3), throwing storage

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Changed tester on the scratch app, twice | One row per state x viewport, with observation | Run 1: 2 of 6 imaged; run 2 (after fix): 4 of 4 imaged | ✅ pass (run 2); evidence Entry 2, 3 |
| AC-1.2 | Changed tester on a scratch CLI project (§8 no surface) | No Visual Review, no screenshot rows | Section deleted, gate item "N/A" | ✅ pass (one session) |
| AC-2.1 | Seeded D1 (binding) and D2 waived by C3 | D1 Major, not accepted; D2 cited | D1 Major open; D2 cited as C3 | ✅ pass, but the old tester also rated D1 Major, so no contrast shown |
| AC-3.1 | Throwing storage seeded | Blocker | Blocker in both runs; run 2 simulated in-page | ✅ pass (run 1 real sandboxed iframe) |
| AC-4.1 | Read `agents/designer.md` | Scale/space bullet; format unchanged | Present; format unchanged | ✅ pass (static read) |
| NFR-1 | `git diff` of templates; JSON parse | Marker, protected columns untouched; validate passes | Marker and columns untouched; JSON parses; `claude plugin validate .` not run (CLI absent) | ⚠ not-verified-live |
| NFR-2 | Read README, ROADMAP, docs/status.md | Label "prompt-enforced, unmeasured" | Present in all three, with the 2/6 then 4/4 disclosure | ✅ pass |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Minor | Run `claude plugin validate .` | Expected pass; the CLI is not installed in this environment | accepted |

## 4. Console & Network
Dry-run apps only: a SecurityError in the storage-throwing copy, as seeded. Nothing for the repo itself.

## 5. Verdict
NFR-1's validate step stays `⚠ not-verified-live`; its waiver was auto-selected by the Factory (autonomous mode), not given personally by the user, and the PR reviewer should run `claude plugin validate .` before merge. All other rows pass on one session each; no rate is claimed. The release, validate run and merge belong to the Factory and a person.

---

## ✅ QA GATE

- [x] Every Must-story acceptance criterion verified and passed
- [x] Every browser-observable NFR verified and passed (NFR-1 validate step waived, ⚠)
- [x] No open Blocker or Major bugs
- [x] Browser console free of errors on the tested flows
- [x] Tested on all agreed viewports
- [x] Line budget respected: Ist ~50 / Soll ~130
- [x] Status set to `passed`
