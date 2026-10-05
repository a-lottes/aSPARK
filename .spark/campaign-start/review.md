# Review Report: campaign-start

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment` (`origin/main...HEAD`, merge-base `460d6fc`), `.spark/campaign-start/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-10-05 |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report — including `/increment` in fix-mode, which is not this
     report's owner — updates it in the same edit that closes or re-rules a finding:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue.

     Re-review: bump `Round` yourself (only the owner bumps it, never `/increment`) at
     the start of the pass, then overwrite every section below in place — §1 Scope, §2
     Plan Conformance, §3 Findings, §4 Traceability, §6 Verdict and the gate checklist
     all hold exactly one current state, never a `## Round N` heading or a second gate.
     History lives in git, not in this file. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 1: changes requested (two Majors: an existing instance could be overwritten, F1; the draft was a rewrite not a copy, F2). All open Majors and Minors except F8 are fixed in place and re-measured (F1 5 of 5, F2 4 of 4 written drafts); awaiting re-review. F8 (stale constitution facts that predate this feature) is routed to a later `/charter`.
- **Open:** `1 open` — Blockers: none; Majors: none; F8 (Minor, constitution wording, a later `/charter`, non-blocking). F1-F5, F7, F9-F11 fixed, awaiting re-review
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

- **Reviewed:** all 18 commits `6dfe2c7..6f2a64d`, i.e. `skills/campaign/SKILL.md` (read whole, 67 lines), `README.md`, `campaigns/README.md`, `docs/{status,repo-layout,family}.md`, `.spark/constitution.md` (commit `5c3b705`), and spec, plan and evidence. Lens `library` applied (public surface, semver, contract clarity; packaging N/A).
- **Graph tool:** `staleness` gives `files_checked: 0` (nothing indexed). `impact --diff origin/main...HEAD` lists all 10 changed files as `unknown_files`. `story_trace US-1 --feature campaign-start` gives `not_found` (the graph predates this feature). No graph result scoped anything. **Scoped by hand.**
- **Re-derived, not cited** (condition (b) Must ACs; (a)/(d) for the NFR-3 rates, at the caller's request): every T9 row, from the jsonl session files and the scratch repos' `git status`/`shasum`/file contents. T3.1 (AC-1.8), T5.3 (AC-2.3), T2(c)/T11 (no `Skill` call), the NFR-4 table (`grep -n`), and the T12 count sweep (my own `git grep`).
- **Live, by me** (scratchpad `rv/`, outside the repo, `--plugin-dir` = this tree): four fresh happy paths `h1`–`h4`; `h1` turn 2 asks the session to record approval; a continuation (`--resume`, on a copy) of the T9 AC-3.1 miss session as `m5`.
- **Cited, not re-run:** T3.2–3.6, T4, T8b/c (Should ACs or NFR-7; no doubt raised).
- **Outside the diff, seen in passing:** `campaigns/migration-campaign.md:51` SR-5 ends mid-sentence ("until they have"). It predates this feature and the plan's fence keeps it out of scope, so route it to a follow-up. `.github/ISSUE_TEMPLATE/field_report.yml:35-44` lists loop phases only. That is correct, because `/campaign` is not a phase.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | The "T1(c) wording" fix (`8811e58`) holds: the ledger says invocation was *inferred*, not observed |
| T2 | ✅ | A8 resolved (absolute Glob in `t2-a`). The T2(b) wording deviation is recorded honestly in the ledger. Validate passes (re-run by me) |
| T3–T7 | ✅ / ⚠️ | Deviation 1 (one-pass build) is accurate: `0819e8e` holds steps 1–8. Deviation 2 is accurate: `bfe60e1` adds exactly the quote-each-key sentence (67 lines). D4's Never list omits "invent a tracker", but that rule sits at `:19` and `:34` (F9) |
| T8 | ✅ | The planted run reproduces from `t8a`. Its "observation for review" is evaluated as F4 |
| T9 | ⚠️ | All five rates re-count exactly. One AC-3.1 inference is wrong (F1). One read-only `git` call went unrecorded (F7) |
| T10 | ⚠️ | 11 added lines (cap 25). `status.md:117` is a new row the plan's §2 did not list (F9). AC-4.1 lacked the project-local-kinds clause (F6, fixed) |
| T11 | ✅ | Audits re-run by me, same results |
| T12 | ✅ | `5c3b705` touches only the constitution. Four lines say eleven. The Amendments row is present. Both corrected citations are true. The dispatch claim is true (8 skills name an agent; `increment`, `spark`, `campaign` name none) |

D3 (`disable-model-invocation`): built as planned. **Recommendation: keep.** It is a documented host key that `validate` accepts, and it costs one line. The `c6` control (n=1) shows only that the description sufficed once, not that the key is redundant. The case it guards (the model writing campaign files unasked) is the B14 failure mode. The cost (routing cannot invoke it) is already written down in plan §1 Consequences. D4 and D7 match what was built. Q1/Q2 are recorded correctly: A8 resolved (T2a), and the guard denied nothing (T2e).

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `skills/campaign/SKILL.md:27-28,53-57`; `campaigns/README.md:48`; `evidence.md` T9 AC-3.1 | **AC-3.1: a missed existence check overwrites the instance.** The T9 miss (`d1-ac31-5`, Status `complete`) checked with Glob `.spark/campaigns/*`, which returned "No files found" because Glob matches files, not a directory holding only a subdirectory. Continued one turn (`rv/m5`, same session, user answers the interview), the session re-ran the same Glob, then made one Write. The `complete` instance was **overwritten**: shasum `875a5b3d`→`48d8f6b4`, 11+/16−. "Nothing was overwritten / no instance was lost" (doc and ledger) holds only because the headless session stopped at its question. That is a false reassurance. **Fix:** step 2 checks the file `.spark/campaigns/<name>/campaign.md` itself (Read or `ls`), and says an empty directory glob proves nothing. Step 7 re-checks that path right before the Write and stops as in step 2. Re-measure AC-3.1 with each session continued to the Write. Reword the doc parenthetical to the measured fact | fixed |
| F2 | Major | `skills/campaign/SKILL.md:53-57` | **AC-1.3: the draft is a rewrite, not a copy.** Step 7 never says "verbatim". Review run `h1` dropped "The agent does not resume after `SR-5` until they have" from the frozen SR-5 row (the campaign-core F24 rule), demoted §8 headings `##`→`###`, swapped §8's stop-rule table for a pointer, and dropped the template's comment. Across the 17 `/campaign` drafts on disk, 7 dropped that comment (which holds "the agent may set Status only to `running`/`halted`"). 16 blanked the approval row's rule text ("only the user sets `approved`"). T6's byte-identity check was one run. **Fix:** step 7 says: copy template and kind body verbatim, keep the HTML comment and every line not filled, change only filled placeholders, the Status cell and the `SR-5…` row (kind rows verbatim). Keep the approval row's placeholder text. QA measures fidelity n of 5 | fixed |
| F3 | Minor | `skills/campaign/SKILL.md:59-61` | **AC-1.7: "a session that you run" addresses the agent.** The skill speaks to the agent as "you" throughout (`:13`), so this tells the agent it runs the planning session. In `h1` the agent wrote "(run by me)" and in turn 2 offered "Want me to kick off that session now?" (C8 says no). The same report left out the veto record. 1 of 17 drafts. The `:60` example also names a kind in a skill (`campaigns/README.md:41`). **Fix:** "…as a session the user runs; run or offer nothing", and drop the kind example | fixed |
| F4 | Minor | `skills/campaign/SKILL.md:58-61,65` | **T8 offer contradicts the Never list.** `t8a` says "I'll then record your statement and set `approved`. A commit is a separate step you can ask for". The text leaks from `templates/campaign.md:8` and `campaigns/README.md:54`, which allow transcription on instruction. My probe (`h1` turn 2, explicit approval request) was refused and the file was unchanged (n=1), so the rule held when tested. The offer is still a misleading promise. **Fix:** step 8 adds: approval and commits are not this command's, offer neither, and say that the user records approval later per the template | fixed |
| F5 | Minor | `skills/campaign/SKILL.md:48-57` | **AC-1.5: the user's §1 words were reworded without confirmation.** `h1` added "(every migration slice is parity-green)" to the Condition and "(dispatched in a context separate…)" to the Verifier. `h2` merged the kind's goal into Condition and Observable and only afterwards asked "Please confirm". Low impact (a draft, read before approval), but a Must AC failed in 2 of 3 written review drafts. **Fix:** "write the user's §1 answers verbatim; a change is a question first; the kind's goal shape stays in §8". QA measures it | fixed |
| F6 | Minor | `README.md:137` | **AC-4.1 clause missing:** neither README §Campaigns nor `campaigns/README.md` "Instantiating" said project-local kinds are unbuilt. Reviewer appended one sentence to the existing line ("Project-local kinds are not built either: only the plugin's own kinds are read."), adding 0 lines. Uncommitted | fixed |
| F7 | Minor | `skills/campaign/SKILL.md:66`; `evidence.md` T9 | The Never list's "use any git command" was broken read-only in `d1-ac16-4` (`git ls-files`; it also ran `python3 -m pyflakes --version`). The ledger does not record it. **Fix:** record it, and either narrow the ban to writing git operations or keep it absolute and let QA count it | fixed |
| F8 | Minor | `.spark/constitution.md:287,301` (user's `/charter`) | The amended lines still say "6 templates" (`templates/` holds 8: `campaign.md`, `releases-index.md` are added). Module structure omits `campaigns/`, though its new citation `docs/repo-layout.md:9` lists it. Both predate this feature, and the ledger records only the second. Artifact wording, non-blocking. **Fix:** a later `/charter` (and `docs/family.md:16`) | open |
| F9 | Nit | `plan.md:26,44`; `docs/status.md:117` | Stale plan facts and two undocumented drifts. The branch is described as `9536fa1`/`781a566` but is now `460d6fc`/`6dfe2c7`. D4's Never-list contents differ from what was built. The new status row is not in plan §2 or Deviations. **Fix:** one Deviations line | fixed |
| F10 | Nit | `campaigns/README.md:48` | 'without a false "usable" opening sentence': one of the three false openings (T9 s4) said "All seven keys are present". `status.md:117`'s "false opening sentence" is exact. **Fix:** drop "usable" | fixed |
| F11 | Minor | `docs/status.md:116` | New, unevidenced claim "(hand-running an instance still needs it)" (the plugin folder). It contradicts spec A4 and `campaigns/README.md:66-67` (activation names only the instance). **Fix:** delete it or cite a run | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `SKILL.md:31-34` | ✅ met (`t2-a`; `h1`–`h4` absolute paths, none asked) |
| AC-1.2 | `SKILL.md:35-41` | ✅ met (0 kind file names; `:60` example, F3) |
| AC-1.3 | `SKILL.md:18-19,53-57` | ⚠️ partial: one file and the right path hold; the copy is not faithful (F2) |
| AC-1.4 | `SKILL.md:36-40` | ✅ best-effort, recount 5/5 substance, 2/5 strict (s1, s3, s4 false openings) |
| AC-1.5 | `SKILL.md:48-52` | ⚠️ partial (F5) |
| AC-1.6 | `SKILL.md:55-57,65-66` | ✅ best-effort, recount d2 5/5 (s3 keeps placeholder, unfilled); `h1`,`h2`,`h4` hold |
| AC-1.7 | `SKILL.md:58-61` | ⚠️ partial (F3) |
| AC-1.8 | `SKILL.md:24-26` | ✅ met (`t3a`: no tool call, no `.spark/campaigns/`) |
| AC-2.1 / 2.2 | `SKILL.md:42-47` | ✅ best-effort, recount 5/5 each (no write, `/story-time` named in all 10) |
| AC-2.3 | `SKILL.md:45-46` | ✅ met (`t5c`) |
| AC-2.4 | `SKILL.md:58-59` | ✅ met (`h2`,`h4` list slice list, parity check, veto record) |
| AC-3.1 | `SKILL.md:27-28` | ❌ 4/5 named correctly; the miss overwrites when continued (F1) |
| AC-3.2–3.6 | `SKILL.md:24-34,35-41` | ✅ cited T3/T4; unexpanded-token branch `not-verified-live` (honestly labelled) |
| AC-4.1 | `README.md:136-137`, `campaigns/README.md:46-48` | ✅ after F6 fix |
| AC-4.2 / 4.4 / 4.5 | sweep, `5c3b705` | ✅ my grep: live totals say eleven; ROADMAP:35, status:107,181,285 classified correctly |
| AC-4.3 | `plugin.json` 0.13.1 | ✅ deferred to `/go-live` as planned |
| NFR-1 / 6 / 10 | — | ✅ 67 lines; 11 doc lines; 0-line diffs in every fenced path; `.py` none; validate passes |
| NFR-2 | frontmatter `:8` | ✅ `t2-c`,`t2-c2`,`t11-unrel`: no `Skill` call |
| NFR-3 | docs rate lines | ⚠️ figures exact and labelled development; F1 parenthetical, F10 |
| NFR-4 | `SKILL.md` | ✅ ledger T7 table matches `grep -n` row by row |
| NFR-5 | docs | ⚠️ F11 |
| NFR-7 / 8 / 9 / 11 | `:16-20,63-67` | ✅ (NFR-9: `t8a` + my approval probe; F4 caveat) |

## 5. What Was Checked

- [x] Correctness: logic does what the acceptance criteria demand. Two ACs fail live (F1, F2)
- [x] Non-functional: applicable NFRs and constitution quality bars hold, except F11 and NFR-3's F1 parenthetical
- [x] Error handling: refusals write nothing (re-counted), except the F1 continuation
- [x] Security: no secrets; target-repo reads only `.spark/campaigns/` and the user's named files
- [x] Tests: no suite (constitution §4); structural analogues and validate green; live analogues re-performed
- [x] Readability: 67 clear lines; one pronoun ambiguity (F3)

## 6. Verdict

Changes requested. The build is mostly sound and honestly documented. It has one skill file with every NFR-4 rule at its acting step, a 0-line footprint elsewhere, an accurate count sweep, and a constitution amendment whose claims I verified. Every T9 rate re-counts exactly from the session files. But re-performing the work live found two defects that the single-run or headless evidence hid. **F1:** the AC-3.1 miss the docs call harmless overwrites a `complete` instance as soon as the session continues to its Write. Its root cause (a directory Glob that cannot see a subdirectory) and its fix (check the file path, re-check before the Write) are both concrete. **F2:** the draft is a model rewrite, not the copy AC-1.3 specifies. One review run silently cut the SR-5 resume ban from the frozen stop rules, and 7 of 17 drafts lose the template comment that carries the agent's Status limits. Both are Majors that `/increment` fix-mode can close within the 70-line cap, and both need a fresh measurement afterwards. Minors F3–F5 are one-line wording fixes in the same step 6–8 region, worth folding into that pass. F8 is the user's `/charter`. Only the user can waive a Major.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here): F1, F2 open
- [ ] Every Must AC traces to implementing code; no constitution non-negotiable violated. Every Must AC traces to code and no non-negotiable is broken, but AC-1.3 is partial (F2)
- [x] All plan deviations documented and accepted (both recorded deviations verified accurate; F9 asks for one more line, Nit)
- [x] Test suite runs green (no suite per constitution §4; `claude plugin validate .` passes; structural checks green)
- [x] Line budget respected: Ist 114 / Soll ~150 (excluding HTML comments)
- [ ] Status set to `passed`
