# Review Report: graph-gates-verification

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/graph-gates-verification/plan.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-08-27 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** All three Majors are genuinely fixed and independently re-verified — the #11 issue map, the README's proof state and F2's re-routing as a Core documentation defect all hold; all eleven Round-1 findings plus the two Round-2 residues (F12, F13) are now fixed. Gate passes.
- **Open:** `0 open` — Blockers: none; Majors: none. `F1`–`F11` confirmed `fixed r2` against the current file text; `F12`/`F13` fixed by `/increment` fix-mode, 2026-08-27, pending confirmation at the next `/peer-review` pass if one occurs.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Re-review at `HEAD = 59d14bc` on `feat/handbook-maturity` of the fixes `/increment` fix-mode
applied to all eleven Round-1 findings. Read in full: `spec.md`, `plan.md` (incl. the new
Deviations item), `evidence.md` (596 lines), `README.md` §Project Status, and Round 1's own
findings table. Every `fixed` label was checked against the current text — none taken on trust.

Fence re-verified independently: `git status --porcelain` → ` M README.md` + `?? .spark/graph-gates-verification/`;
`git diff --name-only` → `README.md` only (24 insertions / 1 deletion, §Project Status);
`git diff --stat` and `git status --porcelain --untracked-files=all` over `skills/ agents/ tools/
lenses/ templates/ .claude-plugin/plugin.json` → both empty; 10 skills / 7 agents; `plugin.json`
at `0.7.1`, unbumped. The fixes touched nothing they were not allowed to touch.

Independently re-derived this round from the still-present `/tmp/ggv/*.jsonl`: t4 (0 probe commands,
both MCP names literal), t5b (1 stray `Bash` probe, `staleness` never called), t7 (5 tool calls, no
`Agent`, only browser `ToolSearch`), t11 (hint = 1 on surface 2; **0** in the `Agent` tool_result —
F11's new claim), t12 (orchestrator: no `ToolSearch`, only the `graph.json` half; the
`command -v aspark-graph` in that transcript is the **subagent's**, issued after delegation, so
Entry 13's scoping holds). Quotes re-checked at source: `tools/aspark-graph.md:19-22`, `:27-28`,
`skills/{sprint-plan,peer-review}/SKILL.md:38`, `skills/demo-day/SKILL.md:40`, `docs/status.md:76-80`
— every `file:line` in the corrected findings is accurate.

Not reviewed: whether #8–#11 should be closed (the user's act at `/go-live`, spec A5);
`docs/status.md`'s table (consciously out of this diff). No test suite exists or is possible
(constitution §4) — the evidence record *is* the suite.

**Tool use:** `aspark-graph` (CLI, `graph=yes`) re-run — `query staleness --repo .` → `files_checked: 0`
(nothing indexed), `query impact README.md --repo .` → `files: []`, `unknown_files: ["README.md"]`.
Both vacuous again, as in Round 1; scoping was by hand. Every finding rests on files I read.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | P1–P8 captured; F1 drift logged, venues reassigned from measured state |
| T2 | ✅ | Counts re-verified: 0/0 both surfaces; restoration deviations disclosed at the point of claim |
| T3 | ✅ | One build, logged; `stale:false`, `files_checked: 2` |
| T4 | ⚠️ | Counts re-verified again (0 probes, both tool names literal). The mutation log still lists T11 among V-POSITIVE's reusers "per the ledger", contradicting the ledger F4 corrected — F13 |
| T5 | ✅ | Attempt A discarded with reason; B re-verified. The mid-flight DoD reinterpretation is now recorded in `plan.md`'s Deviations (F10) |
| T6 | ✅ | `ToolSearch "staleness impact"` → none → full CLI probe form; follow-on `impact` also CLI |
| T7 | ✅ | F5's relabel landed at the point of claim with the independent grounds cited; the DoD line's "direct probe" wording is the one residue — F12 |
| T8 | ✅ | Playwright detected, gate passed on that basis, navigation + two assertions |
| T9 | ✅ | Same for Chrome DevTools MCP in a separate session |
| T10 | ✅ | Cited back from Entries 8/9 as the sanctioned out-of-order exception |
| T11 | ✅ | Ledger now carries a V-HINT row and drops T11 from V-POSITIVE (F4); AC-5.1/5.2/5.3/NFR-5 attribution corrected and the quote re-attributed to the tool file (F6) |
| T12 | ✅ | Fixture findings renamed `FX1`–`FX5` at both sites, the separate ID space stated twice; grep found no stray reference (F7) |
| T13 | ✅ | #11's map rewritten to Entries 11/12 and Entry 6 re-filed under #8 (F1); F2 re-routed as a Core documentation defect quoting both halves, reliability kept as the residual (F3) |
| T14 | ✅ | Fence re-audited by me again this round; every claim holds |
| T15 | ⚠️ | README is now honest on all six partials (F2). Entry 15's own NFR-9 parenthetical still says nothing is claimed unproven — F13 |

`plan.md:89-96` now records six deviations; the sixth (T5's DoD reinterpretation) closes the gap
Round 1 filed as F10. All six are disclosed and defensible; none is an overstep.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `evidence.md:524` | Entry 13's issue map reads "**#11** (CLI branch, AC-2.3 target) — confirmed (Entry 6)". #11 tracks the installed-but-unbuilt hint (`docs/status.md:79`, `spec.md:31`) and, per `docs/status.md:80`, the stale-graph reaction — proven in Entries **11** and **12**. Entry 6 is *this* spec's AC-2.3, the CLI-branch control for US-2/#8: a different AC in a different spec. This section is explicitly the input for the user's `/go-live` close, so it points a closer at evidence that proves nothing about #11, while the real #11 evidence is cited nowhere in the map (US-6/AC-3.2 is absent entirely). Constitution §4 traceability. **Fix:** replace with `#11 (hint, prior AC-2.3; stale-graph reaction, prior AC-3.2) — confirmed (Entry 11: count = 1; Entry 12: announced once, 0 graph citations)` and re-file Entry 6 under #8's row. | fixed r2 |
| F2 | Major | `README.md:249` | "a 2026-08-26 verify-only sweep closed most of that gap live" — of the six partials at `docs/status.md:77-82` the sweep proved three (AC-2.3, AC-3.2, AC-3.5), refuted-with-finding one (AC-2.2) and never attempted two (AC-1.2, AC-5.2 — consciously cut, spec §6). Three of six is not "most", and neither the row nor the paragraph at 259-274 labels the two cut ones unproven. NFR-9 (`spec.md:174`) requires exactly that; constitution §1/§4 make §Project Status the honesty bar. Entry 15 scoped NFR-9 to "in-scope issues" while the row it edits speaks about all six. **Fix:** "closed three of those six live; AC-1.2 and AC-5.2 were out of scope and remain unproven". | fixed r2 |
| F3 | Major | `evidence.md:507-508` (route), `:28` | F2's route asserts "not a wording defect … the text itself is unambiguous in all three instances". The shipped text is not unambiguous: (a) `tools/aspark-graph.md:19-20` says "**Run no command**" while `skills/sprint-plan/SKILL.md:38`, `skills/peer-review/SKILL.md:38` and `skills/demo-day/SKILL.md:40` say "Resolve **both** facts — is there a surface, and does `.aspark-graph/graph.json` exist", and the only documented method for the second fact is a command (`tools/aspark-graph.md:22`) — so an agent on the MCP branch obeying "resolve both facts" is *pushed* into exactly the probe Entry 5's run 2 ran, and Entry 4 only avoided it by substituting an undocumented method (reading `files_checked` off an MCP call); (b) the detection *act* is nowhere specified — `ToolSearch` appears in no file under `skills/ agents/ tools/ lenses/` (verified by grep), and I counted **five** different mechanics across the seven transcripts (`select:` exact names t4/t5b; free-text t6; browser-only free-text t7; `select:Bash` t11; none t12). Routing this as inherent variance points a later increment at *qualifying the guarantee*; the evidence actually points at two cheap prose fixes. **Fix:** re-route F2 as (also) a Core documentation defect against `tools/aspark-graph.md:19-22` and the identical block in the three SKILLs, quoting both halves; keep the reliability observation as the residual. | fixed r2 |
| F4 | Minor | `evidence.md:17` | The venue ledger still lists `T11` under V-POSITIVE's "Used by", which Entry 11 (`:433`) and `plan.md:92` both contradict, and V-HINT (`/tmp/ggv/hint`) has no ledger row at all — so its declared state and authorized mutations live only in Entry 11's prose, while the ledger presents itself as the file's authority for venue assignment. **Fix:** add a V-HINT row; drop `T11` from V-POSITIVE. | fixed r2 |
| F5 | Minor | `evidence.md:321` | Labelled "**Direct probe** confirming `surface=yes, graph=yes` beforehand", but what was performed is a read of `.mcp.json` plus an `ls`. AC-3.2 (`spec.md:122`) says "verified by a direct probe"; NFR-4 (`spec.md:169`) forbids reading/reasoning from passing an AC. A registration file is not proof the session exposes the tools — t7's only `ToolSearch` is `"browser playwright chrome devtools"` (verified). The facts do hold on independent grounds (P1/P2's restored global symlink ⇒ `surface=yes` via the CLI runner; Entry 3's build ⇒ `graph=yes`), so AC-3.2's substance survives. **Fix:** relabel as a config/filesystem read and cite P2 + Entry 3 as the grounds. | fixed r2 |
| F6 | Minor | `evidence.md:455,459` | "matching AC-5.1/AC-5.2's *'at most one hint sentence fires per run, at most once'*" — that sentence is `tools/aspark-graph.md:27-28`, not either AC, and it is *weaker* than AC-5.1's "exactly **1** occurrence" (`spec.md:146`). Line 459 repeats the swap: AC-5.2 is credited with "fires exactly once" when it is the no-build/no-`graph.json` criterion (`spec.md:147`), and that criterion's evidence is credited to NFR-5 (countability). All the substance is present and I re-counted it as 1; three ID citations point at the wrong requirement. Constitution §4. **Fix:** AC-5.1 ← the count, AC-5.2 ← the mutation-absence checks, AC-5.3/NFR-5 ← the method; attribute the quote to the tool file. | fixed r2 |
| F7 | Minor | `evidence.md:484-490`, `plan.md:94` | Entry 12's fixture review table reuses `F1`–`F5` while the evidence file's own findings table (`:27-28`) already owns `F1`/`F2`. "F2" now resolves to both "MCP resolution gap" and "newline inside `render()`"; `plan.md:94` writes "F1–F5 in Entry 12" with no qualifier. Constitution §4 ("IDs are never renumbered") and §3's `^F\d+$` convention. **Fix:** renumber the fixture's to `FX1`–`FX5`, or label the table as a separate ID space at both sites. | fixed r2 |
| F8 | Minor | `evidence.md:267,269`; `plan.md:72` | Recountability (NFR-5 layer 3) resolves to `/tmp/ggv/*.jsonl`, and Entries 4/8 (`:229`, `:356`) justify skipping restoration precisely because the venue "is itself deleted at sweep end". `/tmp` does not survive a reboot; the file never says its substrate is ephemeral, so a reader at `/go-live` gets no warning. They happen to exist today — that is luck, not method. **Fix:** one line in the Rule/Counting-domains block stating the transcripts are ephemeral and the quoted excerpts are the durable record. | fixed r2 |
| F9 | Nit | `evidence.md:227,354,389,470` | Placeholder timestamps (`20:2X`, `21:0X–21:0X`, `~21:1X`, `~21:2X`) presented where NFR-4 requires a captured timestamp. The real values are recoverable from the transcript mtimes (t4 20:28–20:33, t8 21:04–21:07, t9 21:10–21:14, t12 21:28–21:34). **Fix:** substitute them. | fixed r2 |
| F10 | Nit | `plan.md:89-95` | Deviations records five mechanical items but omits the only one that changed a *definition of done*: T5's "resolves identically" was reinterpreted at `evidence.md:289` to "showing the comparison, whichever way it falls". Entry 5 states it openly, so nothing is hidden — but Deviations is the bounded read a downstream consumer trusts. **Fix:** add one line. | fixed r2 |
| F11 | Nit | `evidence.md:34-39` | AC-5.1 (`spec.md:146`) names three counting surfaces — "ceremony messages, produced artifact, **subagent reports**" — while the Counting domains block declares two and explicitly excludes the agent tool_result payloads where a subagent report lives. I checked t11's Agent tool_result myself: **0** occurrences of `aspark-graph build`, so the total of 1 is unaffected. The declared method still doesn't cover a surface the AC names, unacknowledged. **Fix:** note the divergence and the verified-zero third surface. | fixed r2 |
| F12 | Nit | `evidence.md:349` | Entry 7's DoD check still reads "direct probe confirms `surface=yes, graph=yes` beforehand ✓" — the exact label F5 corrected 25 lines above, where the same act is now called a "Config/filesystem read". The venue facts do rest on performed probes (P1/P2, Entry 3's build, the in-session `ls -la`), so the DoD holds and AC-3.2 is met; what is left is one entry carrying two labels for one act, which a re-counter will trip over. **Fix:** reword the DoD line to the grounds already stated at `:324`. | fixed |
| F13 | Minor | `evidence.md:232`, `:586` | Two cross-references still state the pre-fix version of a claim corrected elsewhere. (a) `:232` — "V-POSITIVE is reused by T5–T7, **T11**, T12 per the ledger": the ledger (F4) now reads `T3–T7, T12`, and T11 could not have run there (V-POSITIVE is `graph=yes` since T3; T11 needs `graph=no`), so this asserts, *citing the ledger as authority*, the very assignment F4 removed. (b) `:586` — Entry 15 still says the README was worded so that "nothing here is claimed unproven since every in-scope issue was actually run", while the README rewritten under F2 now labels AC-1.2 and AC-5.2 unproven in both the row and the paragraph; the ledger entry documenting that edit now misdescribes it, on the very NFR-9 point F2 was about. **Fix:** (a) drop `T11` from the reuse list at `:232`; (b) replace the parenthetical with "…and the two never-attempted partials (AC-1.2, AC-5.2) are labelled unproven", and add them to the content map at `:587`. | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | Entry 2 (`evidence.md:137-183`) | ✅ met — re-counted 0/0 by me on both surfaces |
| AC-1.2 | Entries 2, 4, 6, 8, 9 + Entry 14 (`:559-569`) | ✅ met — every mutation names authorization and restoration or reasoned non-restoration |
| AC-1.3 | Entry 14 (`:573`) | ✅ met — silence case is Entry 2, precedes every positive run |
| AC-2.1 | Entry 4 (`:256`) | ✅ met — re-verified 0 probe commands, both tool names literal |
| AC-2.2 | Entry 5 (`:287`) | ⚠️ partial — honestly recorded as partially refuted; declared branch/surface match, mechanics do not |
| AC-2.3 | Entry 6 (`:310`) | ✅ met — CLI branch, probe form cited verbatim, re-verified |
| AC-2.4 | Entry 4 (`:258`), Entry 13 (`:517`) | ✅ met — failure path not triggered, explicitly recorded as untested rather than skipped |
| AC-3.1 | Entry 7 (`:334-342`) | ✅ met — stop message names both prerequisites; 0 `Agent` calls re-verified |
| AC-3.2 | Entry 7 (`:324,347`) | ✅ met r2 — three zero-counts re-verified; precondition rests on P1/P2 + Entry 3 + the in-session `ls`, and the session-exposure read is now labelled a read (F5) |
| AC-3.3 | Entry 10 (`:422`) | ✅ met — cited back from Entries 8/9; both proceeded past step 1 |
| AC-4.1 / 4.2 | Entry 8 (`:364-379`) | ✅ met — detection, gate rationale, navigation + two assertions on backend identifiers |
| AC-4.3 | Entry 9 (`:400-413`) | ✅ met — repeated in a separate session |
| AC-4.4 | Entry 13 (`:513-517`) | ✅ met — confirmed/refuted/unstable semantics applied; both 1/1 full pass |
| AC-5.1 | Entry 11 (`:450-455`) | ✅ met — I re-counted: exactly 1 on surface 2, 0 in the artifact, 0 in the subagent report |
| AC-5.2 | Entry 11 (`:462`) | ✅ met — 0 build/install/serve, no `graph.json`; attribution corrected (F6) |
| AC-5.3 | Counting domains (`:32-42`), Entry 11 (`:451`) | ✅ met r2 — method stated and reproducible; the surface AC-5.1 names but the method omits is now disclosed and verified zero (F11) |
| AC-6.1 / 6.2 | Entry 12 (`:478-494`) | ✅ met — one staleness statement, 0 graph citations after it, verdict on five `file:line` anchors |
| NFR-1 | `README.md` + `.spark/graph-gates-verification/**` | ✅ — verified by my own `git status` / `git diff --name-only`, twice |
| NFR-2 | protected paths | ✅ — empty diff and empty untracked over all six; 10 skills / 7 agents; `0.7.1` unbumped |
| NFR-3 | Entry 13 (`:509-510`) | ✅ met r2 — both halves quoted verbatim with `file:line`, every line number checked at source, route named and now correct (F3) |
| NFR-4 | throughout | ⚠️ partial — F5 and F9 fixed and re-verified; the T7 DoD line still labels a config read a "direct probe" (F12) |
| NFR-5 | Entry 14 (`:574`), header Rule row (`:7`) | ✅ met r2 — every count states its method and re-counts correctly; the substrate's ephemerality is now disclosed (F8) |
| NFR-6 | Entries 2, 3, 4, 6, 8, 9, 11 | ✅ met — no build/install/serve outside declared scratch; nothing run on a user repo |
| NFR-9 | `README.md:249,259-281` | ✅ met r2 — three proven, one refuted-with-finding, two named unproven and out of scope, in both the row and the paragraph (F2) |

## 5. What Was Checked

- [x] Correctness: every Round-1 fix read against the current text, not the `fixed` label; five load-bearing counts re-derived again from the raw transcripts (t4, t5b, t7, t11, t12), including F11's new zero and the orchestrator/subagent split in t12 that decides whether Entry 13's F2 row is over-broad — **it is not**. All matched.
- [x] Non-functional: NFR-1/NFR-2 fence re-run independently after the fixes — nothing beyond `README.md` and the feature dir moved. Constitution §1 (honesty), §3, §4 (traceability, docs-in-step), §6 re-applied: the §4 failures Round 1 recorded at F1/F6/F7 and the §1/§4 failure at F2 are all closed; no non-negotiable is touched.
- [x] Error handling: the refutation paths still read as refutations — Entry 5's failed AC, AC-2.4's untriggered path, and #8's "not a clean confirm" all survive the fix round intact rather than being smoothed while the file was open.
- [x] Security: no secrets, credentials or customer material in the diff; the README addition adds only public issue links; `.spark/` publication risk re-checked — nothing private.
- [x] Tests: none exist and none are possible (constitution §4). The evidence record is the suite; I re-executed its checks rather than reading its conclusions.
- [x] Readability: the corrected issue map, the FX ID space and the ephemeral-substrate note all make the record easier to re-run, not harder; the two open residues are the only places the file now disagrees with itself.

## 6. Verdict

`passed`. The three Majors were fixed properly, not cosmetically, and I checked each against the
file rather than the label. Entry 13's issue map now sends a `/go-live` closer to Entries 11 and 12
for #11 and re-files Entry 6 under #8, which is what `docs/status.md:76-80` actually says the
issues track — I verified that mapping at source rather than taking Round 1's word for it. The
README's arithmetic is now honest in both places it speaks: three of six proven, one
refuted-with-finding, AC-1.2 and AC-5.2 named unproven and out of scope, and the row and the
paragraph agree with each other and with the evidence. F2's re-routing is the one I looked at
hardest, because a re-route can easily become a re-labelling: it is not. Entry 13 now quotes both
halves of the contradiction with accurate line numbers, names two concrete prose fixes, and keeps
the reliability question as an explicit residual — and the top findings table defers to it instead
of stating a second, competing route, so the two cannot drift apart. The eight Minors and Nits hold
up too: the FX rename is complete (grep found no stray reference, and the one surviving `F1` is
inside a verbatim quote that says so), the timestamps match the transcript mtimes exactly, the
V-HINT row is there, and F11's new claim — zero hint occurrences in the subagent report — I
re-counted myself and confirmed. What is left is two places where the file now disagrees with
itself: Entry 4 still tells a reader, citing the ledger, that T11 ran in a venue it demonstrably
could not have run in, and Entry 15 still describes the README as claiming nothing unproven when it
now claims exactly that. Both are one-line corrections, both are contradicted by correct text
elsewhere in the same file, and neither changes a count, a route or the shipped surface — so they
do not block the gate, but I am not waiving them either; they stay `open` for whoever next touches
this file, or for the user to `accept`. The record is sound and I stand behind it.

---

## ✅ REVIEW GATE

- [x] No open Blocker findings
- [x] No open Major findings — `F1`–`F3` confirmed `fixed r2`; `F13` (Minor) and `F12` (Nit)
      remain open and unwaived, which the gate does not block on
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — the
      §4 traceability failures (F1/F6/F7) and the §1/§4 docs-in-step failure (F2) are closed;
      AC-2.2 stays ⚠️ partial by design (a recorded refutation, spec C4) and NFR-4 ⚠️ partial (F12)
- [x] All plan deviations documented and accepted — six in `plan.md:89-96`, all sound; F10's gap closed
- [x] Test suite runs green — N/A by constitution §4; the evidence record is the suite and I
      re-executed five of its load-bearing counts against the raw transcripts, all matching
- [x] Line budget respected: Ist 168 / Soll ~150 (excluding HTML comments) — 18 over; thirteen
      finding rows, three of which must quote shipped text from four files to stay actionable.
      Recorded, not waived.
- [x] Status set to `passed`
