# Review Report: adversarial-gates

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/adversarial-gates/plan.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-10-04 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Round 2: `passed`. All round-1 findings confirmed fixed from source; two new Minors (F9, F10) found and fixed by the reviewer; refuted-with-finding and E2 `other` stand.
- **Open:** `0 open` — Blockers: none; Majors: none; F1–F10 all `fixed` (see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

- **Reviewed (round 2):** the fix pass `git diff 8d9aff8..HEAD` (`ce3300a`: `evidence.md`, `plan.md`, `README.md`, `ROADMAP.md`, `docs/status.md`, plus this report), read against the full `git diff origin/main...HEAD`. Base `fa33f2c` = `origin/main` after `git fetch` = merge-base, so the branch is not stale. The untracked `.spark/.guard/` is outside the diff (plan R9 routes it to `/go-live`).
- **Re-derived from source, not cited (condition (a), verifying fixes):** `right-sizing/evidence.md:980-990` and `qa.md:103-105` for F1; the Blocker sweep over the 51 scope files at `fa33f2c` (literal 3, severity-cell 7) for F2; folder count (18) for F3; the Method section of `evidence.md` diffed against `7416328` (identical except one trailing blank line) for F3/F6; `waiv`/`silently` line count (140) and `lean-rounds/review.md:67` for F6; README/ROADMAP/`docs/status.md` re-read in full for AC-4.1–4.5 (condition (b)).
- **Tool (`tools/aspark-graph.md`, review slice):** `query staleness` → `stale: false`, `files_checked: 0` (nothing indexed, not "fresh"). `query impact --diff 8d9aff8..HEAD` → `files: []`, all 6 paths under `unknown_files`: Markdown is not indexed, as plan §2 predicts. Scope came from `git diff`; every location below was read by hand.
- **Lens `library` (review phase):** fix pass touches no skill, agent, template, frontmatter or packaging; no lens finding.
- **Not reviewed:** T10–T15 (`deferred`, Inc 2). The `/go-live` version bump is not this phase's.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Branch cut from `origin/main`. Spec + plan are the first commit (`fe2025a`). Base SHA, validate, `*.py` and `wc -l` are quoted at `evidence.md:7-34`. |
| T2 | ✅ r2 | The Method is its own commit `7416328` with 0 entries; its text is unchanged at head (only a trailing blank line differs). Folder-count error documented as a deviation (`plan.md:181`), Method not edited. |
| T3 | ✅ r2 | 10/10 quotes verbatim; 18 raw counts reproduce. Sweep count corrected (`evidence.md:80`, reproduces); reading shortcut documented (`plan.md:180`); sweep pattern in the plan corrected (F9). |
| T4 | ✅ | Refuted-with-finding upheld. E2 note now matches the source (F1 fixed). |
| T5 | ✅ | Transcript quoted (`evidence.md:143-166`). Skills diff empty. |
| T6, T7 | ✅ `N/A — AC-1.7` | Correct per D5. |
| T8 | ✅ | The three docs state the true state. Re-open condition corrected (F5, fixed). Nit F8. The "Stricter verdict rules" rename is a documented deviation (`plan.md:177`). |
| T9 | ✅ | All audits reproduce at head (diffs 0, no `*.py`, validate green). File list extended for `review.md` (F10). |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Minor | `.spark/adversarial-gates/evidence.md:106`, `:131` | **Problem:** the E2 note says "the same forbidden act … is recorded as recurring: B1 and B4 earlier, B5 here" and concludes `/demo-day` step 1 "would reach 3". The source says the opposite: `right-sizing/evidence.md:980` reads "The one leak was not a repeat of B1/B4's failure mode". B1 is mentioning the absent declaration (`:770-771`) and B4 is announcing a silent check (`:820-821`); both are narration, which the current rule rates "Fine, not a violation" or "capped at Minor" (`skills/demo-day/SKILL.md:36-39`). **Why it matters:** it gives the user a false path to qualification on the one call flagged for them. **Fix:** replace the premise with the source's distinction, and state that reclassifying E2 alone leaves step 1 at 1. | fixed r2 |
| F2 | Minor | `evidence.md:80` | **Problem:** "A `Blocker` sweep (`\| Blocker \|` rows, 11 lines)" does not reproduce. Over the 51 files at `fa33f2c`, `grep -F '\| Blocker \|'` gives **3** lines, `\| *Blocker` gives 6, and any Blocker-cell row gives 7. **Why it matters:** a count in a search that decides a Must AC must be recountable. **Fix:** record the exact pattern and its real count. | fixed r2 |
| F3 | Minor | `evidence.md:52` (Method, frozen per `:76`) | **Problem:** "51 files across **17** feature folders": the 51 files span **18** folders. **Why it matters:** the Method is frozen, so the error can only be corrected the way the Method itself prescribes. **Fix:** a one-line `plan.md` Deviations entry plus a correction note in §Corpus. Do not edit the Method. | fixed r2 |
| F4 | Minor | `evidence.md:196` | **Problem:** "observed at branch head … (6 files, 533 insertions, 5 deletions)" was measured at `50e45cd` (T8). Head reads 576/5. **Fixed by reviewer:** the line now names the commit and gives the head figure. | fixed r1 |
| F5 | Minor | `README.md:127`, `ROADMAP.md:57`, `docs/status.md:266` | **Problem:** dual review was "re-open only on a recorded single-reviewer miss", but spec §6 (`spec.md:117`) says "Re-open only on a new argument or observation, for example a recorded single-reviewer miss". AC-4.4 requires the §6 condition, and the docs had narrowed it. **Fixed by reviewer** in all three docs: "a new argument or observation, such as a recorded single-reviewer miss". | fixed r1 |
| F6 | Minor | `evidence.md:54` vs `:80`; `plan.md:178` | **Problem:** the Method requires that "Every hit is read in context (±5 lines)". The Corpus says the 142 `waiv`/`silently` hits were "read through their per-file counts and the lines that name an agent act". That is a deviation from the frozen Method, and the plan's T3 deviation note does not mention it. Treatment is also inconsistent: E5 (an act the user later waived) is an entry, while `lean-rounds/review.md:67` F10 (fix-mode amended an `approved` spec, later user-ratified) is absent. **Why it matters:** the Method exists so nobody can quietly loosen the search. **Reviewer check:** all 140 matching lines read; none is a `SKILL.md` gate-step evasion, so T4 is unaffected. **Fix:** add a Deviations line. | fixed r2 |
| F7 | Minor | `docs/status.md:265` | **Problem:** "The classification of one borderline entry (E2) is open and flagged for review" goes stale once the user takes this round's E2 ruling (§6). **Fix:** reword it to the ruling as accepted. | fixed r2 |
| F8 | Nit | `ROADMAP.md:44` | **Problem:** the Shipped row omits "whether a row would fire cannot be tested in Core", which T8's DoD lists for each doc. NFR-8 itself is met (`README.md:126`, `docs/status.md:266`). **Fix:** append the clause. | fixed r2 |
| F9 | Minor | `.spark/adversarial-gates/plan.md:178` | **Problem:** the T3 Deviations line still said the sweep was "`\| Blocker \|` rows" and "found E2 and E7"; the literal pattern gives 3 rows and misses E2's source row (`right-sizing/qa.md:103`, `\| B5 \| Blocker → confirmed fixed \|`). F2 corrected `evidence.md` only. **Why it matters:** the plan and evidence disagreed on a search that decides Must AC-1.7. **Fixed by reviewer:** the line now names the severity-cell form (7 rows) and says the literal form gives 3 and misses E2. | fixed r2 |
| F10 | Minor | `.spark/adversarial-gates/evidence.md:196` | **Problem:** the audit "observed at branch head" says `git diff --stat origin/main` "lists only" the 6 §2 paths; since `ce3300a` it also lists this `review.md` (7 files, 676 insertions). **Why it matters:** the audit is cited as current. **Fixed by reviewer:** one clause added naming `review.md` from `ce3300a` on. | fixed r2 |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `evidence.md:78-123` | ✅ met: quotes, `file:line`, gate, class and per-class/per-gate counts are present. Count caveats in F2, F3 |
| AC-1.2 | `git diff origin/main...HEAD -- skills` → 0 lines | ✅ met |
| AC-1.3, AC-1.4, AC-1.6 | — | N/A — AC-1.7 (no qualifying gate) |
| AC-1.5 | Empty skills diff; `evidence.md:143-192`; reviewer re-run (§5) | ✅ met. Routing and questions are identical in 3 runs. n=1 per side, likely-only |
| AC-1.7 | `evidence.md:125-133` | ✅ met: refuted-with-finding re-derived and upheld |
| AC-1.8 | `evidence.md:89-92`, `:123` | ✅ met |
| AC-4.1, AC-4.5 | `README.md:122-127`, `ROADMAP.md:44`, `docs/status.md:260-266` | ✅ met: "no rows shipped", in-repo, unmeasured, prompt-enforced. No shipped standard, no verdict change |
| AC-4.2 | `ROADMAP.md:50-57` | ✅ met: the shipped part moved to Shipped; the standard is "Planned, not built" |
| AC-4.3 | `README.md:124`, `ROADMAP.md:55-56`, `docs/status.md:266` | ✅ met: aspark-guard named |
| AC-4.4 | same three docs | ✅ met (after F5 fix) |
| NFR-1, NFR-3, NFR-6 | diffs of `skills agents templates lenses .spark/constitution.md .claude-plugin` → 0 lines; `git ls-files '*.py'` → 0; `claude plugin validate .` → "✔ Validation passed with warnings" (the known root-`CLAUDE.md` warning) | ✅ met |
| NFR-2, NFR-5, NFR-8 | `README.md:125-127`, `docs/status.md:266` | ✅ met (Nit F8) |
| NFR-4 | no template diff; bump deferred to `/go-live` | ✅ met for Inc 1 |
| NFR-7, NFR-9 | no ID renumbered; quotes only from `.spark/`, and the E7 quote names no project | ✅ met |

## 5. What Was Checked

- [x] Correctness: every corpus quote opened at its line (`grep -n -F` at `fa33f2c`, sources unchanged on the branch); each class checked against Method rules 1–3. E1 fits rule 1 (asserted `passed` against `/demo-day` step 6, `SKILL.md:104-105`). E3/E4 fit rule 2. E5–E10 cite no `SKILL.md` gate step. E8 (no agent act) and E10 (`campaign-core/evidence.md:494` says "The kind named the role but not the order", so no rule was skipped) are arguably not entries at all, but they count toward nothing. The dropped hit `right-sizing/evidence.md:321` is genuinely retracted at `:316-322`.
- [x] Non-functional: NFR-1–NFR-9 per §4. Constitution §1 honesty and the `CLAUDE.md` refuted-with-finding rule hold.
- [x] Error handling: the empty-corpus path is AC-1.7, taken and recorded.
- [x] Security: no secrets. The untracked `.spark/.guard/` is not in the diff, and plan R9 flags it for `/go-live`'s presence check.
- [x] Tests: no suite (constitution §4). `validate` is green after my edits. Reviewer re-run of AC-1.5: a scratch fixture identical to `fx2`, `claude -p "/aspark:next-steps" --plugin-dir ~/aSPARK --max-turns 10`, exit 0. It recommended `/charter` first, gave three options, wrote nothing (`git status` empty) and never mentioned rebuttals.
- [x] Readability: docs are plain and short (README section is 6 lines, within D6's cap of 8).

## 6. Verdict

Round 2 passes. I checked every round-1 fix from the source, not from the fix notes. The E2 note and the T4 bullet now quote `right-sizing/evidence.md:980` correctly, and no file in the diff still says "would reach 3" or treats B1/B4 as a recurrence. The Blocker sweep figures reproduce exactly: 3 literal rows, 7 severity-cell rows, and the 7-row form contains both E7 (`situational-lenses/review.md:55`) and E2's source row (`right-sizing/qa.md:103`). Both new Deviations entries are accurate: 18 folders, 142 hits on 140 lines, and the E5 vs `lean-rounds` F10 inconsistency recorded without being repaired. The frozen Method text is unchanged since `7416328`. The doc edits (F5, F7, F8) add no unshipped claim and leave nothing stale, so AC-4.1–4.5 still hold. I found two more Minor drifts and fixed both myself: the plan still described the sweep by its literal pattern (F9), and the head audit's file list did not include this report (F10). No Blocker or Major is open, and no waiver is needed. Refuted-with-finding and the user-accepted E2 ruling (`other`) stand.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here)
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated
- [x] All plan deviations documented and accepted — F6 and F3 at `plan.md:180-181`, sweep pattern corrected at `plan.md:178` (F9); the user routed them to fix-mode at round 1
- [x] Test suite runs green — no suite (constitution §4); `claude plugin validate .` passes after round-2 reviewer edits
- [x] Line budget respected: Ist 100 / Soll ~150 (excluding HTML comments) — self-reported, no linter checks this
- [x] Status set to `passed`
