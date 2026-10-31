# Review Report: visual-qa-review

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Uncommitted working-tree diff on `factory/issue-1` (9 files) + `.spark/visual-qa-review/{spec,plan,evidence}.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-10-30 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Round 2: F1-F4 fixed and re-read (gate item and QA text now keep `⚠` rows open; docs disclose 2/6 then 4/4; F3 clause dropped; evidence IDs relabelled). Mode: static read plus dry runs in evidence.md.
- **Open:** `none`
- **Binding ruling:** §6 Verdict and the gate checklist below
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Scope

`git diff` against `HEAD` 7920845 (= `main` = `origin/main`; the branch is not stale): README.md, ROADMAP.md, agents/designer.md, agents/qa-tester.md, docs/status.md, lenses/ux.md, skills/demo-day/SKILL.md, templates/qa-report.md, templates/spec.md. Also untracked spec/plan/evidence. Read against `standards/anti-generosity.md` (applied) and constitution §3 (protected structures). **Mode: static read only.** This is Markdown with no test suite, and `claude plugin validate` is not available here (it is also absent from evidence.md). I did not repeat the dry runs, so every behavioural AC below is at best `⚠ not-verified-live`.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ⚠️ | Done. Adds an "older spec: any required change is binding" rule that is not in the spec (F3) |
| T2 | ✅ | `lenses/ux.md:63-67` |
| T3 | ✅ | `agents/designer.md:55-58`, `:102-106` |
| T4 | ✅ | §6 sits after the protected tables; the spec.md §8 heading is unchanged (comment only) |
| T5 | ⚠️ | Labels say "prompt-enforced, unmeasured", but they leave out the failed observation (F2) |
| T6 | ⚠️ | Negative case ran first. The added `⚠` rule was not re-run (disclosed). AC IDs do not match the spec (F4) |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `templates/qa-report.md:113`, `agents/qa-tester.md:204` | The gate item says "one row per UI state and viewport, each with an observation". A table of `⚠ not-verified-live` or "cannot reach" rows satisfies it as written. Entry 2 of the dry run produced exactly that (4 of 6 rows not imaged), so US-1 can pass QA with no image looked at. This conflicts with anti-generosity rule 2 (a partial check is not a pass), and the gate is where the agent acts. **Fix:** add to the gate item "no row is `⚠ not-verified-live`; any such row keeps this box unchecked". Have the PO decide whether an unreachable state blocks the gate. | fixed r2 |
| F2 | Major | `docs/status.md:283`, `README.md:141`, `ROADMAP.md:47` | NFR-2 asks for honest maturity labels. The only live run of the changed QA Tester partly failed AC-1.1: 2 of 6 rows had a screenshot. The `⚠` rule added to fix that has never been run (`evidence.md` Entry 2). None of the three docs says so: status.md only says "one session each, not a rate". README says `/demo-day` "asks … look at each image", but the one observation shows that did not happen. **Fix:** add one clause to each doc, e.g. "one dry run: 2 of 6 rows imaged; the follow-up rule was not re-run". | fixed r2 |
| F3 | Minor | `agents/qa-tester.md:208` | "(or, in an older spec, any stated required change)" treats every unlabelled required change in an existing spec as binding, so each one becomes a Major. AC-2.1 covers only `binding` directions, and README/status.md do not disclose the retroactive effect. **Fix:** either drop the clause, or get the PO to approve it in the spec and disclose it in the README. | fixed r2 |
| F4 | Minor | `.spark/visual-qa-review/evidence.md:5,8,10,14-16` | Evidence cites AC-1 to AC-8, but the spec defines AC-1.1, 1.2, 2.1, 3.1, 4.1 and NFR-1/2. This breaks traceability: "AC-6" is the spec's AC-1.2 and "AC-8" is NFR-1. **Fix:** relabel the IDs to match the spec. | fixed r2 |
| F5 | Minor | `templates/qa-report.md:20-21,32` | The Handoff re-test overwrite list and the budget comment ignored the new §6, so a re-test could append to §6. Fixed by the reviewer: §6 added to both comments (comment-only, no protected structure changed). | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `agents/qa-tester.md:195-206`, `templates/qa-report.md:91-101,113` | ⚠ not-verified-live. The text is present. The only live run produced 2/6 imaged rows, and the remedy was not re-run (F1, F2) |
| AC-1.2 | `agents/qa-tester.md:204-206`, `templates/qa-report.md:93,113` | ⚠ not-verified-live. Static read: the requirement is conditioned on a browser surface and the gate allows N/A. The browser-less path of `skills/demo-day/SKILL.md` is untouched. Not run live |
| AC-2.1 | `agents/qa-tester.md:207-212`, `skills/demo-day/SKILL.md:108-109`, `templates/qa-report.md:112` | ⚠ not-verified-live. Text PASS. The dry run shows no contrast, because the old tester also rated D1 Major (evidence Entry 2 note) |
| AC-3.1 | `lenses/ux.md:63-67`, `agents/qa-tester.md:179-180,219-220` | ✅ text met (storage-throwing, reload, resize; a failed start is a Blocker). Blocker B1 was reproduced once |
| AC-4.1 | `agents/designer.md:55-58` | ✅ met. The finding format is unchanged |
| NFR-1 | diff of `templates/*` | ✅ met. Marker line 3 is unchanged. The `Spec ID`/`Result` columns and the spec.md story/AC line forms are untouched. No new agent or lens, no JSON |
| NFR-2 | README/ROADMAP/status.md | ❌ maturity omission (F2) |

## 5. What Was Checked

- [x] Correctness: each AC traced to text. Behaviour is only `⚠ not-verified-live`
- [x] Non-functional: NFR-1 holds. NFR-2 fails (F2)
- [x] Error handling: n/a (Markdown). The rules are checked for consistency with anti-generosity (F1)
- [x] Security: no secrets, no code
- [ ] Tests: none exist (Markdown). Plugin validate not run
- [x] Readability

## 6. Verdict

Round 2, anti-generosity standard applied, mode: static read of the fixes. `templates/qa-report.md` gate item and `agents/qa-tester.md` now keep any `⚠ not-verified-live` Visual Review row open (F1); README, ROADMAP and docs/status.md disclose the 2/6 then 4/4 observation and that it is one session each (F2); the retroactive-binding clause is removed (F3); evidence IDs match the spec (F4). Protected structures and the marker are unchanged. No open finding. `claude plugin validate .` could not run here (CLI not installed): `⚠ not-verified-live`, disclosed in evidence.md.
