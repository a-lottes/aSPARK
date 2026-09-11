# Review Report: metrics-script-removal

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment` (`main..HEAD`, 9 commits), `.spark/metrics-script-removal/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-09-11 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** The removal and the published method are sound and every figure reproduces independently — but the branch is based two commits behind `origin/main`, which already publishes a third machine report and 77-feature figures over the same files, so merging as-is republishes contradicted numbers and re-breaks this feature's own privacy claim.
- **Open:** `9 open` — Blockers: `F1`, `F2`; Majors: `F3`, `F4` (Minors/Nits: see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed: `36a3f17..e8afe51` (9 commits) and `git diff main...HEAD` — 11 paths: `.spark/constitution.md`, three new `.spark/metrics-script-removal/*`, `README.md`, `ROADMAP.md`, `docs/metrics.md`, `docs/reports/README.md`, both `docs/reports/*.json`, and `D scripts/spark-metrics.py`. Read `spec.md`, `plan.md`, `evidence.md` and `.spark/constitution.md` in full; applied the `library` lens including §3 *Packaging & footprint* per the user's spec-gate ruling. Re-ran every AC grep, both privacy greps, `claude plugin validate .` (passes, same single pre-existing `autoUpdate` warning), the three commands printed in `docs/metrics.md` (extracted from the file, not retyped), and an **independently written** derivation of all 23 published figures.

Not reviewed: the deleted script's internals (only the identity of its recovery blob); `docs/reports/m-382a803dcc0de961.json`'s own provenance, which arrived on `origin/main` via PR #40 outside this diff — reviewed only where this branch's claims depend on it (F1, F2). AC-1.3/AC-1.5 were not performed here either: both write outside the repository (§6), so I reviewed the prepared command sequences instead (F4).

Graph tool: `aspark-graph query staleness --repo .` returns `files_checked: 0`. Per the tool file's own contract that is **"no answer", not "nothing at risk"**, so scope was established by reading and grep per its fallback. Stated once; not repeated per finding.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Negative case real and first: `f5d546d` precedes `db4ab15` in `git log main..HEAD`; I re-ran the AC-1.4 grep over the six contract paths — 0 hits |
| T2/T3 | ✅ | 23 figures, all `reproduced`; I re-derived them from the JSON independently and agree exactly (§4) |
| T4 | ✅ | Diff is exactly one line per report (`…428827c8d.json:663`, `…543f46c.json:272`); both still parse |
| T5 | ✅ | AC-5.2 holds — my own pre/post comparison of the stripped field against every published figure shows no dependency |
| T6 | ⚠️ | D6 (`jq`→`python3`) accepted — see §4/NFR-4. Two published figure groups got no printed command (F6) |
| T7 | ✅ | Workflow block gone, closed-snapshot statement stands in its place, "what is in a report" paragraph kept and true on the branch |
| T8 | ✅ | `scripts/` removed as a directory; recovery commit `a2c0541` verified reachable and byte-identical (§4/AC-2.3) |
| T9 | ⚠️ | Four edits + Amendments row exactly as planned. D7's fifth §3 hunk exceeds both T9's DoD and §3's own "nothing else in this section changes" — **ruled acceptable**, no finding raised: the removed qualifier's sole referent was the deleted paragraph, the rule binds identically before and after, and leaving it would have left the constitution citing text it no longer contains |
| T10 | ⚠️ | Headline no longer numeric, dated block carries the table. New `####` heading has no closing boundary (F5) |
| T11 | ✅ | AC-6.1 holds: `grep -n 'handbook honesty exception' ROADMAP.md` → no hit anywhere; the removal is listed under `## Next` |
| T12 | ⚠️ | Sweep and NFR-1 check correct; the AC-1.3 package is missing the step that makes it non-tautological (F4), and the branch-staleness check this project's `CLAUDE.md` prescribes was not performed (F1) |

Deviations D1, D2, D6 were put to the user and ruled before/during Act; I re-derived each from the sources rather than accepting the narration (§4). D3, D4, D5 hold as recorded. D7 ruled above. The plan's §6 "Observation" (absolute path in the approved `spec.md:45`) stands: the spec is immutable, NFR-6 scopes to `docs/`, no action.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Blocker | `docs/metrics.md:41-49,70-75,90-96`; `README.md:262-264`; `docs/reports/README.md:9-11` | Branch base is stale. `git merge-base HEAD origin/main` = `a2c0541`, but `origin/main` = `8e7b078` (PR #40, `git ls-remote` confirms), which adds `docs/reports/m-382a803dcc0de961.json` and publishes **77 features / 11 projects / 84 tags** over these same files. `git merge-tree --write-tree origin/main HEAD` → content conflicts in all three. Post-merge I ran the three **printed** commands over the three-report directory: they print `projects 11 / features 77 / 77 76 75 64 71`, `tags 84 / added 240291 / deleted 18872 / 8 of 11`, `sessions_total 138` — none matching the output printed beneath them. AC-2.1, AC-2.2, NFR-4 and NFR-5 are falsified the moment this lands, and the repo would publish 54/10 with three reports on disk. **Fix:** rebase onto `origin/main` (project `CLAUDE.md`'s staleness habit), re-derive over all three reports, republish the figures and the "two machines / two reports" framing in `README.md`, `docs/metrics.md` and `docs/reports/README.md`, then re-verify every printed output. | open |
| F2 | Blocker | `docs/reports/m-382a803dcc0de961.json:370` (on `origin/main`), against `docs/reports/README.md:18` | That report carries `"root": "/home/silenttz/.claude/projects"` — an absolute home path with a **username**, in a public repo. After the merge, this feature's certified claim *"No project name, no feature name, no hostname, no path"* is false again and AC-5.3's own grep returns a hit; constitution §6 ("nothing private in the working tree at release — the test is presence, not tracking") is violated. Note AC-5.1/NFR-6's `grep -rn '/Users/' docs/` **cannot** catch it: the leak is `/home/…`. Not the builder's error — but US-5 is scoped to `docs/reports/*.json` as a set, so it is this feature's to close. **Fix:** strip the field from the third report exactly as T4 did (one line), and widen the check to AC-5.3's broader pattern rather than the `/Users/`-only grep. | open |
| F3 | Major | `.spark/metrics-script-removal/spec.md:136` (NFR-3) vs the diff | NFR-3's one measurable clause — "the tracked footprint drops by 32,654 B" — is false as written. Summing `git ls-tree -r` blob sizes: `main` 5,737,241 B → `HEAD` 5,802,856 B, a **net +65,615 B**; the 32,654 B script leaves, the three new `.spark/` artifacts add ~98 KB, and `.spark/` ships to every consumer (§3 "the published surface is the whole working tree", §5). The qualitative claims do hold: zero files with the executable bit, zero `.py`, and nothing in the plugin requires an interpreter. **Fix:** record the honest pair (−32,654 B of executable, +65,615 B net of Markdown) as a documented deviation in `evidence.md` and in `release.md`; do not let `/go-live` restate "footprint drops" unqualified. The spec is immutable — this is a deviation, not a spec edit. | open |
| F4 | Major | `.spark/metrics-script-removal/evidence.md:694-710` (Entry 9, AC-1.3) | The prepared sequence omits the plugin **re-install** that `plan.md` §4 itself names ("`claude plugin marketplace update aspark`, then re-install `aspark@aspark`"). As written it updates the *marketplace* and then asserts `gitCommitSha` moved — but nothing re-installs the plugin, so the record (verified today: `gitCommitSha 9c47bc95…`, `lastUpdated 2026-08-31`, installPath `…/aspark/aspark/0.8.0`) has no reason to change and QA's step 3 — the step the entry calls "the whole point" — fails for a missing-command reason on a Must AC. **Fix:** insert the re-install between steps 2 and 3, using R1's uninstall-then-install remedy since no version bump means the `0.8.0` cache directory is reused; keep the stop rule and the user's-go requirement. | open |
| F5 | Minor | `README.md:258` vs `:295-302`, `:304`, `:311` | The new `#### Snapshot — 2026-09-09` heading has no closing boundary, so by Markdown nesting the Area/State maturity table, "The one real gap" and the #8–#11 proof-state paragraph all sit *inside* a block introduced as "Dated **evidence**, taken 2026-09-09 and not updated since", while `README.md:241` asserts "This section always reflects the current state" (constitution §4 makes that assertion the bar). AC-7.2/AC-7.3 hold either way. **Fix:** open a sibling `####` heading (e.g. `#### Proof state`) after `:293` so the dated block ends where the dated content does. | open |
| F6 | Minor | `docs/metrics.md:220`, `:223` | Two published figure groups have no printed command: the per-agent breakdown (`reviewer 108 · …`) and `116 ceremonies` with its breakdown. Neither `transcripts.agent_runs` nor `transcripts.ceremonies` is named anywhere in the file — the only fields printed are `sessions_aspark`, `sessions_total`, `agent_runs_total`, `gates`, `days` — so a reader must invent the extraction step, which is what AC-2.2 forbids for the method and what AC-2.4 ("the rule that reproduces it printed in `docs/metrics.md`") only barely survives via the generic "transcript counters are summed" row. Both reproduce exactly in my own derivation. **Fix:** sum those two dict-valued fields in the third printed command and print the output, or name both fields in the rules table. | open |
| F7 | Minor | commit `db4ab15` subject | Subject is `feat!:` — Conventional Commits' breaking marker — while its own body says "Not a breaking change" and NFR-2 requires "a minor/patch bump, never major". The branch is unpushed (`git ls-remote origin refs/heads/feat/metrics-script-removal` is empty), so the one commit `/go-live` reads for its version decision is still cheap to correct. **Fix:** reword to `feat:` before pushing, or record the contradiction explicitly in `release.md` so the bump is not taken from the marker. | open |
| F8 | Minor | `.spark/metrics-script-removal/evidence.md:586-588` | Entry 7 states the literal AC-1.2 command "returns **three** hits" and names them. Re-run today it returns **six** — the same three plus `evidence.md:583,599,601`, written by the entry that records the count. The criterion's intent is unaffected: all six are inside `.spark/metrics-script-removal/`, and both alternative checks return 0 in my own re-run. Artifact wording, capped at Minor. **Fix:** state "every hit is inside this feature's own artifacts" instead of a count the file changes as it is written. | open |
| F9 | Nit | `.spark/metrics-script-removal/evidence.md:457` | Cites the constitution's `spark-metrics` hit at `:295`; it is at `:296` today, shifted by the amendment row the same task added. **Fix:** cite `:296`, or cite the row by its date so it cannot drift. | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `db4ab15` | ✅ met — `git ls-files '*.py'` empty, `ls scripts` → no such file; no `100755` blob remains (`git ls-tree -r HEAD`) |
| AC-1.2 | `README.md`, `docs/metrics.md` | ⚠️ partial — literal command returns 6 hits (F8), all inside this feature's own artifacts; intent re-verified two ways by me, both 0. Criterion wording is the defect, not the work |
| AC-1.3 / AC-1.5 | `evidence.md:689-745` | ⚠️ deferred by design — outside-repo writes reserved to the user (§6); correctly `/demo-day`'s. AC-1.3's package is incomplete (F4); AC-1.5's sequence is correct, though cloning the local repo proves a clone, not the pushed remote |
| AC-1.4 | `f5d546d`, before `db4ab15` | ✅ met — re-ran the grep myself: 0 hits across `skills agents templates lenses tools .claude-plugin` |
| AC-2.1 / AC-2.2 | `docs/metrics.md:24-96` | ✅ met **on the branch** — I extracted the three fenced blocks from the file and ran them unmodified: exit 0, output identical to what is printed beneath each. ❌ on merge (F1) |
| AC-2.3 | `README.md:291-293` | ✅ met — `a2c0541` is an ancestor of `origin/main` (`git ls-remote` agrees with the local ref), and its blob at `scripts/spark-metrics.py` is `7c258cf…`, the **same blob SHA** as at `3fa75fa`, the commit before the deletion — byte-identity proven by hash, not by `cmp`. `grep -n '\-\-merge' README.md` → 0 |
| AC-2.4 / AC-2.5 | `evidence.md:160-190` | ✅ met — re-derived from scratch (Must-AC verification, so the full re-derivation condition applies, not citation): 10 / 54 / 54·53·52·41·48 / 61 / +114,630 / −12,589 / 7 of 10 / 3 n/a / 42 of 114 / 429 / 377 / 51 days 2026-07-13→2026-09-08 / agent breakdown to the unit / 116 ceremonies with breakdown / naive 65 across 13. Tags per project `[0,1,2,3,5,8,9,9,12,12]` = 61 under max-per-project-then-sum; the `79` was a cross-machine naive sum. The merge prose also checks out: 3 shared projects, 11 duplicated features, aSPARK 8/8 identical, the other two one-sided subsets (9↔2, 2↔1). No refutation was needed |
| AC-3.1 / AC-3.2 / AC-3.3 / AC-3.4 | `docs/metrics.md`, `docs/reports/README.md`, `README.md` | ✅ met — all four greps re-run by me: 0 hits each; flag-table count 0; the closed-snapshot statement stands where the workflow was |
| AC-4.1 | `d1e5fd6`, `.spark/constitution.md` | ⚠️ refuted-with-finding (user-ruled, D1) — **correct disposition**, independently confirmed: the sole remaining hit is `:296`, the amendment row recording this very ruling, and the new row at `:299` is worded without the literal string so the count stays at 1. Satisfying the clause would mean editing an audit trail to clean a grep. First clause holds |
| AC-4.2 | `.spark/constitution.md:256-266` | ✅ met under D2 — live `git ls-files '*.py'` = 0; at `db4ab15` the pinned totals are 106 / 90 `.md`, which is exactly what §8 states |
| AC-4.3 / AC-4.4 | `d1e5fd6` | ✅ met — hunk by hunk: preamble unqualified, `cli` row parenthetical gone with lens load unchanged, §3 exception deleted, §8 restated, new Amendments row cites the user's 2026-09-11 authority. Fifth §3 hunk ruled in §2 |
| AC-5.1 / AC-5.2 / AC-5.3 | `3fa75fa` | ✅ met on the branch — both greps 0, figures unchanged. ❌ on merge (F2) |
| AC-7.1 / AC-7.2 / AC-7.3 / AC-7.4 | `README.md:244-293` | ✅ met — numeric headline gone; table sits 2-4 lines under a paragraph carrying both `2026-09-09` and `evidence`. I re-walked every sentence outside the dated block rather than trusting the regex sweep, and spot-checked all five dismissals (skills/agents/templates+"end-to-end run"; the fall-backs enumeration; "one … question"; `#11`/`#9`; `#4`) — each is a genuine false positive, no count of projects/features/runs/days survives. AC-7.4 is `/demo-day`'s. Block boundary: F5 |
| AC-6.1 (`Could`) | `ROADMAP.md:45-52` | ✅ met |
| NFR-1 | `git diff --name-status main` | ✅ met — no path under `skills/ agents/ lenses/ templates/ tools/ .claude-plugin/`; re-run by me, 11 paths, all expected |
| NFR-2 | `f5d546d` + `db4ab15` | ✅ met on substance — nothing in the consumed contract referenced the file, no slash command, template heading, column or ID pattern touched, so no deprecation is owed. Commit marker contradicts it (F7) |
| NFR-3 | lens §3 | ⚠️ partial — zero executables and zero interpreters required to *use* the plugin; footprint arithmetic is wrong as written (F3). The A9 hedge is repeated, not escalated: all five ignored artifacts are still present in the working tree, and no document in this diff claims consumer exposure |
| NFR-4 | `docs/metrics.md` | ✅ met on the branch — observed running by me, not by reading. D6 (`python3` for `jq`) is the right call: `jq` and `brew` are both absent here while `/usr/bin/python3` (3.9.6) is present, and the commands use stdlib only. ❌ on merge (F1) |
| NFR-5 | `evidence.md` Entry 2-3 | ⚠️ partial — every figure derived live and reproduced by me; nothing restated unchanged, nothing published with a caveat in place of a rule. Two breakdowns lack a printed command (F6), and F1 breaks the live derivability on `main` |
| NFR-6 | `3fa75fa` | ⚠️ partial — holds on the branch, fails on merge and the AC's grep is too narrow to notice (F2) |
| NFR-7 | `f5d546d`, `e8afe51` | ✅ met — negative case recorded before the deletion commit; `claude plugin validate .` re-run by me, passes with the one pre-existing `autoUpdate` warning on a file this diff does not touch; derivation stayed untracked (`git status --porcelain` is clean) |

## 5. What Was Checked

- [x] Correctness: every Must AC traced and re-performed from the sources, not read off `evidence.md`
- [x] Non-functional: NFR-1…NFR-7 and the `library` lens incl. §3 packaging/footprint; constitution §§1,3,4,5,6,8
- [x] Error handling: the three printed commands tolerate `n/a` projects (`proj.get('git') or {}`, `r.get(field) or 0`) — the `TypeError` Entry 4 records is genuinely fixed, and I re-ran them against a three-report directory without a crash
- [x] Security: no secrets; one username still reachable post-merge (F2); no executable ships
- [x] Tests: none exist and none are possible (§4) — substitute is `claude plugin validate` plus observed command output, both performed here
- [x] Readability: `docs/metrics.md` is shorter and states its rules instead of describing a program

## 6. Verdict

Changes requested. The work itself is the strongest increment I have reviewed in this repo: `scripts/` is gone as a directory, the consumed contract is untouched, the negative case genuinely precedes the deletion in `git log`, the privacy strip is two lines and nothing else, the constitution's four edits are exactly the four that were authorised, and I re-derived all 23 published figures from `docs/reports/*.json` with my own script — every one reproduces exactly, down to the per-agent breakdown and the 61 tags the spec expected to refute. The three commands printed in `docs/metrics.md` run verbatim, extracted from the file, and match their printed output line for line. What fails is not the code but its base: `origin/main` has moved two commits ahead of this branch's merge-base, already publishes a third machine report and 77-feature figures over the same three files this branch rewrites, and carries a username in that new report. So on merge every printed command prints numbers that contradict the output printed beneath it, and `docs/reports/README.md`'s "no hostname, no path" claim — which this feature certifies as *now true* — becomes false again. That is an honesty defect inside the fix for an honesty defect, the precise failure mode the spec's own §1 names, and it is why F1 and F2 are Blockers rather than merge-time chores. Nothing else is structural: rebase, re-derive over three reports, strip the third `transcripts.root`, correct the footprint arithmetic and add the missing re-install step, and this passes. I fixed nothing myself — this round's instruction limits my writes to this file, and none of the nine findings is both safe to fix here and mine to own.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [ ] No open Blocker findings — **F1, F2 open**
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here) — **F3, F4 open**; Blockers cannot be waived, so no waiver is sought for F1/F2
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated *on the branch as it stands* — AC-4.1's second clause is user-ruled `refuted-with-finding`, AC-1.2's literal command is a criterion defect, AC-1.3/AC-1.5 are `/demo-day`'s by §6. §6's privacy non-negotiable is violated only by the merged result (F2)
- [x] All plan deviations documented and accepted — D1, D2, D6 user-ruled; D3, D4, D5 as recorded; D7 ruled acceptable by me in §2
- [x] Test suite runs green — none exists and none is possible (§4); substitute performed: `claude plugin validate .` passes with the one pre-existing `autoUpdate` warning, and all three printed commands were observed running
- [x] Line budget respected: Ist 111 / Soll ~150 (excluding HTML comments)
- [ ] Status set to `passed` — set to `changes-requested`
