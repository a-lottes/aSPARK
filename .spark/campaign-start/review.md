# Review Report: campaign-start

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment` (`origin/main...HEAD`, merge-base `460d6fc`), `.spark/campaign-start/plan.md` |
| **Status** | `passed` |
| **Round** | 2 |
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
- **Verdict:** round 2: passed. F1 and F2 (Majors) and every Minor the user ruled on are confirmed fixed from source and by live re-runs. Open: F8 (Minor, constitution wording, routed to a later `/charter` by the user, non-blocking) and F12 (Nit, step 7 does not name the title line).
- **Open:** `1 open` — Blockers: none; Majors: none; F8 (Minor, later `/charter`, non-blocking). F12 (Nit) accepted by the user, QA measures it. F1-F7, F9-F11 and F13 fixed r2
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

- **Reviewed:** the fix pass `6f2a64d..79f6e1e` (`skills/campaign/SKILL.md` read whole, now 73 lines; `README.md`, `campaigns/README.md`, `docs/status.md`; the plan Deviations; the evidence section "Fix round after `/peer-review` round 1"), against the whole `origin/main...HEAD` diff for fences and docs counts. Lens `library` applied (public surface unchanged: one command, same name and argument hint).
- **Graph tool:** `staleness` gives `files_checked: 0`. `impact --diff 6f2a64d..HEAD` lists all 7 changed files as `unknown_files`. As in round 1, no graph result scoped anything. **Scoped by hand.**
- **Re-derived, not cited** (condition (a): this round verifies fixes to these facts; (b) for the Must ACs): the `e1-f1-1..5` and `e1-f2-1..5` counts, from the jsonl files and each scratch repo's `git status`, `shasum` and a line-by-line fidelity script. The NFR-4 placement table and the docs line counts were re-done with `grep -n` and `git diff --numstat`.
- **Live, by me** (scratchpad `rv2/`, outside the repo, `--plugin-dir` = this tree, the evidence's own `run.sh`): `x1` `approved`, 2 turns (`--resume` with the goal answers); `x2` `halted`, 2 turns; `x3` `running`, goal given up front; `x4` the race case: turn 1 found no instance and asked the interview, then I committed a `complete` instance, then turn 2 (`--resume`) gave the answers. `h1` and `h2` are fresh happy paths.
- **Housekeeping:** the repo holds no file from my runs. `claude -p` writes its own session logs under `~/.claude/projects/` for each scratch cwd, as every earlier run did. I copied nothing there.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1–T8, T10–T12 | ✅ | As round 1. F9 is now recorded in plan Deviations: the branch facts are true (merge-base `460d6fc`, spec `6dfe2c7`, plan `5510da7`), the Never list matches what was built, and the status row is listed |
| T9 | ✅ | The AC-3.1 correction stands in the fix-round section. The T9 paragraph at `evidence.md:642` had no pointer to it, so I added one (F13) |
| Fix round | ✅ | Documented as a Deviation: 67→73 lines, NFR-1 yield recorded (plan Deviations, evidence "Size") |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `skills/campaign/SKILL.md:27-32,56-57` | AC-3.1 overwrite after a missed existence check. **r2:** step 2 now checks the file path and says a glob proves nothing. Step 7 re-checks it before the Write. Ledger 5/5 recounted. My 4 runs were all unchanged (shasums `8a5cb238`, `0ceda773`, `26efd543`, `875a5b3d` identical before and after), including both `--resume` continuations. **`x4` exercised the step 7 re-check itself:** "my first check found nothing there… I haven't merged with it or overwritten it". The doc parentheticals are honest | fixed r2 |
| F2 | Major | `skills/campaign/SKILL.md:56-62` | AC-1.3 rewrite, not a copy. **r2:** step 7 says verbatim. The 4 `e1-f2` drafts plus my `h1`/`h2`, 6 of 6: HTML comment kept, approval row text kept, `## 8. Kind-specific`, 0 kind-body lines missing. The only differing lines are the title, Status, Kind, §1 Condition, §3 Tokens and, in `h2`, §5 Rollback (user answers). `e1-f2-2` asked first and wrote nothing (4/5 sessions wrote, matching the ledger) | fixed r2 |
| F3 | Minor | `SKILL.md:63-66` | "a session the user runs; run or offer nothing" holds. The kind example is gone (`grep -i migration` gives 0 hits). `h2`: "In a planning session you run… I have not run or dispatched either role" | fixed r2 |
| F4 | Minor | `SKILL.md:66-67` | "offer neither" holds. No approval or commit offer in `h1`, `h2` or the 4 `e1-f2` reports | fixed r2 |
| F5 | Minor | `SKILL.md:51-53` | §1 is written as the user gave it in all 6 drafts (the Condition line equals the stated goal). The kind's shape stays in §8 | fixed r2 |
| F6 | Minor | `README.md:137` | Reviewer's sentence, now committed in `79f6e1e` | fixed r2 |
| F7 | Minor | `SKILL.md:72`; `evidence.md` fix round | Narrowed to "commit or run a git command that changes the repo". That still covers AC-1.6 ("no git commit"), NFR-4 ("no commit") and NFR-9. README:136, `campaigns/README.md:46` and `status.md:117` say "never to … commit", which stays true. `d1-ac16-4` is now recorded | fixed r2 |
| F8 | Minor | `.spark/constitution.md:287,301` (user's `/charter`) | Re-verified: "6 templates" (8 exist) and no `campaigns/` in Module structure. Both predate this feature. The user routed this to a later `/charter`. Artifact wording, non-blocking | open |
| F9 | Nit | `plan.md` Deviations | One Deviations line, facts verified (see §2) | fixed r2 |
| F10 | Nit | `campaigns/README.md:48` | "usable" dropped | fixed r2 |
| F11 | Minor | `docs/status.md:116` | Unevidenced parenthetical removed | fixed r2 |
| F12 | Nit | `skills/campaign/SKILL.md:58-59` | **New (introduced by the F2 fix).** "Change only the Kind row, the Status cell, the answers… and the `SR-5…` row" omits the title line `# Campaign: <campaign-name>`. `e1-f2-4` followed the text literally: it kept the placeholder title and listed it as unfilled. The other 5 drafts filled it. The impact is cosmetic (the path carries the name). **Fix:** add "the title" to the change list | accepted by the user (2026-10-05): /demo-day measures the title as part of fidelity |
| F13 | Minor | `evidence.md:491,642` | **New.** The T9 paragraph still said "so no instance was lost" with no pointer to the fix-round correction. The T7 NFR-4 table carries the 67-line numbers and the old "use any git command" quote with no staleness note. Artifact wording. **Reviewer fixed it:** a one-sentence pointer at each place, wording otherwise untouched | fixed r2 |

## 4. Requirements Traceability

Rows not suffixed `r2` keep their round-1 verdict. Their line numbers refer to the 67-line text; the current map is the NFR-4 row.

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `SKILL.md:31-34` | ✅ met (`t2-a`; `h1`–`h4` absolute paths, none asked) |
| AC-1.2 | `SKILL.md:35-41` | ✅ met (0 kind file names; `:60` example, F3) |
| AC-1.3 | `SKILL.md:18-19,56-62` | ✅ met r2 (6/6 faithful drafts; F12 Nit) |
| AC-1.4 | `SKILL.md:36-40` | ✅ best-effort, recount 5/5 substance, 2/5 strict (s1, s3, s4 false openings) |
| AC-1.5 | `SKILL.md:50-55` | ✅ met r2 (6/6 §1 as given) |
| AC-1.6 | `SKILL.md:55-57,65-66` | ✅ best-effort, recount d2 5/5 (s3 keeps placeholder, unfilled); `h1`,`h2`,`h4` hold |
| AC-1.7 | `SKILL.md:63-67` | ✅ met r2 (`h1`,`h2`: list, statement, user-run next step, nothing offered) |
| AC-1.8 | `SKILL.md:24-26` | ✅ met (`t3a`: no tool call, no `.spark/campaigns/`) |
| AC-2.1 / 2.2 | `SKILL.md:42-47` | ✅ best-effort, recount 5/5 each (no write, `/story-time` named in all 10) |
| AC-2.3 | `SKILL.md:45-46` | ✅ met (`t5c`) |
| AC-2.4 | `SKILL.md:58-59` | ✅ met (`h2`,`h4` list slice list, parity check, veto record) |
| AC-3.1 | `SKILL.md:27-32,56-57` | ✅ best-effort r2: 5/5 ledger, 4/4 mine (2 continued to the answers, 1 race caught at step 7) |
| AC-3.2–3.6 | `SKILL.md:24-34,35-41` | ✅ cited T3/T4; unexpanded-token branch `not-verified-live` (honestly labelled) |
| AC-4.1 | `README.md:136-137`, `campaigns/README.md:46-48` | ✅ after F6 fix |
| AC-4.2 / 4.4 / 4.5 | sweep, `5c3b705` | ✅ my grep: live totals say eleven; ROADMAP:35, status:107,181,285 classified correctly |
| AC-4.3 | `plugin.json` 0.13.1 | ✅ deferred to `/go-live` as planned |
| NFR-1 / 6 / 10 | — | ✅ r2: 73 lines, the yield recorded in plan Deviations and evidence; docs 11 added lines (`--numstat`); fenced paths 0-line diff; `.py` none; validate passes; 0.13.1 |
| NFR-2 | frontmatter `:8` | ✅ `t2-c`,`t2-c2`,`t11-unrel`: no `Skill` call |
| NFR-3 | docs rate lines | ✅ r2 (honest "4 of 5 at first … 5 of 5 with the goal up front") |
| NFR-4 | `SKILL.md` | ✅ r2, `grep -n` on 73 lines, no rule dropped: never approve or run `71-72`, `65-67`; no overwrite `30`, `56-57`; one goal and Observable `44-46`; seven keys `38-41`; `campaign.md` and reserved dir `62`, `25-26`; one file `19`, `62`, `72`; unresolved path `35-36`; no commit `66`, `72`. "iterate nothing" became "run or offer nothing" plus the Never "run or resume a campaign", so AC-1.7 is still covered. The ledger T7 table is a dated snapshot, now labelled (F13) |
| NFR-5 | docs | ✅ r2 (F11 removed) |
| NFR-7 / 8 / 9 / 11 | `:16-20,69-73` | ✅ r2 (NFR-9: `t8a`, my approval probe, and F4's step 8 rule) |

## 5. What Was Checked

- [x] Correctness: the Must ACs hold live. AC-3.1 and AC-1.3 were re-measured by me
- [x] Non-functional: the applicable NFRs and constitution quality bars hold. NFR-1 yields by its own clause
- [x] Error handling: every refusal wrote nothing, including the two continued sessions and the race case
- [x] Security: no secrets. Target-repo reads are only `.spark/campaigns/` and the user's named files (one `e1-f2-4` Read of a non-existent `~/.spark/...` path, a wrong-cwd probe, no effect)
- [x] Tests: no suite (constitution §4). Validate is green and the live analogues were re-performed
- [x] Readability: 73 clear lines, one ambiguity (F12)

## 6. Verdict

Passed. Both round-1 Majors are fixed, and that is shown by behaviour, not only by the fix notes. Six of six drafts (four from the ledger, two of mine) are now faithful copies of the template and the kind. Every existing-instance case I ran left the file byte-identical, `approved`, `halted`, `running` and `complete` alike. That includes two sessions continued with the interview answers and a race case where the instance appeared between turns. The new step 7 re-check caught that one at the Write. Every Minor the user ruled on is fixed and checked against the source. The docs stay at 11 added lines, label every check best-effort and give the corrected AC-3.1 history honestly. The file grew to 73 lines under NFR-1's recorded yield, and the NFR-4 table re-run shows no rule dropped. Two items stay open and neither blocks: F8, the user's later `/charter`, and F12, a Nit the F2 wording introduced, which `/increment` can close with two words. I fixed F13 myself: a missing correction pointer in the ledger. The rates are still development figures from n=4–6 sessions on one fixture family; `/demo-day`'s re-measurement is what ships.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here): F1, F2 fixed r2
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated (AC-1.3, AC-1.5, AC-1.7, AC-3.1 re-verified r2)
- [x] All plan deviations documented and accepted (fix-round and F9 lines added to plan Deviations, verified)
- [x] Test suite runs green (no suite per constitution §4; `claude plugin validate .` passes, CLAUDE.md warning only; structural checks green)
- [x] Line budget respected: Ist 110 / Soll ~150 (excluding HTML comments)
- [x] Status set to `passed`
