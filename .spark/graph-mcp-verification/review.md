# Review Report: graph-mcp-verification

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The working-tree change of `/increment`, `.spark/graph-mcp-verification/plan.md` |
| **Status** | `passed` |
| **Round** | 3 |
| **Date** | 2026-09-21 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`) — now `passed`. Round 3 was a bounded re-check of three text corrections plus a live sanity pass; it did not re-open rows it did not re-examine.
- **Round 3 result:** F11's correction re-verified from primary source, not from its label: M8 now names **five** runs, **discloses** the original false "never `~/aSPARK`" claim instead of erasing it, and records the user's **second** explicit ratification together with what they were shown. I re-enumerated every `bypassPermissions` session on this machine dated 2026-09-21 — still exactly five, no sixth created by the fix pass — and re-parsed the fifth's JSONL: `cwd=/Users/andreaslottes/aSPARK`, one `tool_use` (the read-only probe), one result, one reply. F12's disclosure sentence is present at Entry 2 and its quote is verbatim against the real prompt. F13's corrected citations are exact. One new Minor, **F14**, in F13's own fix (a line labelled "step 2" that sits inside step 1) — Reviewer-fixed in place.
- **Open:** `0` — Blockers: none; Majors: none (F1, F3 `fixed r2`; F2, F11 `waived` by the user, both rulings verified as accurately recorded); Minors: none (F4–F10, F12, F13 `fixed`, F14 `fixed r3`). Gate clear.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

**Round 3** is a narrow re-check of three corrections (F11, F12, F13) plus a final live pass — not a
fourth review. Each was re-derived from primary source under condition (a) (verifying a fix), never
from its "done" label: M8's current text read in full at `evidence.md:33`; every
`bypassPermissions` session on this machine dated 2026-09-21 re-enumerated by parsing
`~/.claude/projects/**/*.jsonl` (**exactly five**, unchanged — the fix pass spawned no sixth); the
fifth's JSONL re-parsed (31 records, `cwd=/Users/andreaslottes/aSPARK`, `isSidechain: false`,
`turnOrigin: sdk`, **one** `tool_use`, one `tool_result`, one assistant text); its full prompt
re-read to check F12's quote; F13's three ranges re-read from `tools/aspark-graph.md` and
`skills/sprint-plan/SKILL.md`. Live again, all matching round 2 exactly: `git status --porcelain`
(still only `.spark/.guard/` + `.spark/graph-mcp-verification/`), `git rev-parse HEAD origin/main`
(both `2ec691c`), `git diff`/`--cached`/`origin/main...HEAD` (empty), `claude mcp list` (only the
unrelated `claude.ai Docs` connector), `readlink -f ~/.local/bin/aspark-graph` →
`/Users/andreaslottes/aSPARK-graph/.venv/bin/aspark-graph`, `lsof -ti:8934` (free), the
`runner=yes, graph=yes` probe. **Nothing regressed since round 2.** *Round-2 scope, retained:* F3's
session file parsed record by record, F7's three versions re-derived from the venv's `dist-info` and
`npm view`, F1's guard ledger re-checked (`grep -c` → 76 + 8; `git ls-files .spark/.guard/` empty).

*Round-1 scope, retained.* Re-scoped from git, not from the feature's self-report:
`git diff --name-only origin/main...HEAD` is empty but vacuous — nothing is committed — so it
cannot by itself prove a fence (see F1). Reviewed: `evidence.md` in full against
`spec.md` and `plan.md` in full, plus the source files it cites (`skills/demo-day/SKILL.md`,
`agents/qa-tester.md`, `README.md`, `skills/sprint-plan/SKILL.md`,
`agents/engineering-manager.md`, `tools/aspark-graph.md`, `.spark/graph-gates/evidence.md`), and
all three AC-4.1 citations re-derived (condition (b), Must-AC verification). **Not reviewed:**
Entries 4/7/8/10/11's own transcripts (no standing record — corroborated this round: zero
`isSidechain` records exist in any of today's session files, so Entry 4's "not retrievable"
justification is true, not an excuse), and the historical state of the M1/M2 bracket window.

**Tool use (`aspark-graph`).** Ran `query staleness --repo .` → `files_checked: 0`, which the
tool file (`tools/aspark-graph.md:39`) defines as *nothing indexed*, not *fresh* — so the graph
answers nothing about this Markdown-only repo. `query impact .spark/graph-mcp-verification/evidence.md`
→ `{"found": true, "files": [], "unknown_files": [".spark/graph-mcp-verification/evidence.md"]}`,
reproducing `plan.md:47` exactly. The tool therefore told me only *where not to look* (no indexed
file links to this change); every location below was read by hand.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Entry 1 carries all four DoD items; F1 logged as a finding, not absorbed. Quote precision fixed (F4). |
| T2 | ✅ r2 | Re-run for real in fix-mode; I parsed the cited session JSONL myself — genuine non-sidechain process, one Bash probe, one reply, verbatim as quoted. F3 closed; disclosure gap F12. |
| T3 | ✅ | `runner=yes, graph=no` probed; C9's install grant correctly recorded **unused, not claimed**. |
| T4 | ✅ r3 | Truncation labelled a bounded deviation; "no second hint site" re-derived from source twice, holds. Citations correct after F13; the "step 2" mislabel inside that fix is F14, Reviewer-fixed. |
| T5 | ✅ | `files_checked: 2 > 0`, `stale: false` — R7's vacuous-graph guard honoured. |
| T6 | ✅ | Control ran before any registration, per the recorded order deviation; non-degenerate (`impact` returned a real answer). |
| T7 | ✅ r3 | Registration quoted; the subagent/MCP-loading constraint solved for real. M8 now states its true scope (five runs, one of them in `~/aSPARK`), discloses the false claim it replaced, and carries both user ratifications — F11 closed as the user's waiver. |
| T8 | ✅ | Two fresh sessions compared side by side; teardown quoted and independently re-verified today. |
| T9 | ✅ | Three citations, all re-derived from source and accurate after F6's off-by-one fix; NFR-3 "no contradiction" holds. |
| T10 | ✅ r2 | Navigation + assertion attributable to `mcp__playwright__*` identifiers; teardown verified. Version now recorded and re-derived (`0.0.82`), caveat honest — F7 closed. |
| T11 | ✅ | Independent session, own registration, own verdict; the `ToolSearch`-loaded-but-uncalled tools correctly excluded from the tally. |
| T12 | ✅ r2 | Fifth value defined at the Method header; zero `N/A this run` left in `evidence.md` (6 uses of the new value) — F10 closed. |
| T13 | ✅ r2 | Fence prose corrected and accurate; its commands re-run today and still reproduce — F1 closed. |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `.spark/graph-mcp-verification/evidence.md:353,377` | The audit annotates `?? .spark/.guard/` as "pre-existing, **unrelated to this feature**" and concludes "the only path this feature touched is `.spark/graph-mcp-verification/**`". Both are false as written: `grep -c graph-mcp-verification .spark/.guard/ledger.jsonl` → **48**, `trail.jsonl` → **7**, all written by this loop (the newest row is this feature's own `plan.md` write). The directory is pre-existing; the rows are not. It matters because NFR-1's literal measure (`git diff --name-only`) returns empty *for every path* here — nothing is committed — so the fence rests entirely on this prose, and the prose is wrong about a file this feature wrote. The NFR-1/NFR-2 verdicts still stand on the evidence I re-derived (no tracked file modified; `.guard/` writes are the plugin's own provenance hook, untracked and never committed) — but the sentence must say that instead of "unrelated". **Fix:** restate as "`.spark/.guard/` is the guard hook's untracked provenance ledger; this sweep appended 48+7 rows to it. It is outside the feature's authorship and is never committed, so NFR-1's fence is unaffected" — and note explicitly that `git diff --name-only` is vacuous in an all-untracked tree, so `git status --porcelain` is the load-bearing check. Left open: whether guard writes count as "touched" under NFR-1 is the EM's ruling, not a typo. | fixed r2 — `evidence.md:390` now names `.spark/.guard/` as the guard hook's shared untracked provenance ledger, pins no number, and names `git status --porcelain` as the load-bearing check. Re-derived, not taken on trust: `grep -c` → 76 + 8 (grown from 48 + 7, as expected), `git ls-files .spark/.guard/` → empty |
| F2 | Major | `.spark/graph-mcp-verification/evidence.md:199,222,266,282` | Four legs (Entries 7, 8, 10, 11) were run as `claude -p … --permission-mode bypassPermissions` subprocesses. That execution mode is authorized nowhere: spec Q1/Q2/C9–C11 grant *what* may be installed, registered and served; plan Q6 grants the runner-removal bracket; none of them grants running an agent with the permission system switched off, and no mutation-log row (M1–M7) records it. It matters because this sweep's entire thesis is "every mutation names its authorization", and a bypassed subprocess's blast radius is bounded only by its prompt — the ledger will be read as precedent by the next sweep. Nothing bad is visible in the outcome (venues confined to the scratchpad, all teardown re-verified today). **Fix:** add a mutation-log row naming the mode, its cwd bound and what it could reach, and get the user's explicit ratification — or re-run the four legs with the default permission mode. A Major cannot be waived by me. | **waived** (user ruling 2026-09-21, "yes, grant it"): ratified post-hoc rather than re-run, on the strength of the Reviewer's own independent re-verification (containment to scratch cwds, narrow read-only prompts, all four registrations torn down and confirmed clean same-day). Recorded as `evidence.md` mutation-log row M8, naming the mode, its cwd bound and what it could reach, per this row's own fix instruction. **r2:** waiver confirmed properly recorded — ruling quoted, M8 present with mode, authorization and an explicit "no state to restore" field. The waiver stands as the user's; its *accuracy* does not — see F11 |
| F3 | Major | `.spark/graph-mcp-verification/evidence.md:98,102,108` | AC-1.1 is given `confirmed (performed)`, but its emission half is a subagent's section literally headed **"SIMULATED USER-FACING CEREMONY OUTPUT"**, whose content is the narration *"(nothing — the instruction says say nothing at all)"* — a description of an absence, not an observed empty ceremony output. Entry 4 draws exactly this line in the other direction ("a real `/sprint-plan` ceremony run (**not a simulation**)"), and constitution §8 rules that reasoning about what a file *would* do is never a performed step. The same entry also concedes "nothing in this window ran a gate at all", so AC-1.1's "no gate outcome differs from today's" half is reasoned, not observed. The probe half *is* genuinely performed (real command, real `runner=no`/`graph=no` output, exit 0), so this is a verdict-precision defect, not a fabrication. **Fix (thorough option taken, per user's ruling):** re-ran the silence leg with the real-fresh-process technique the sweep itself invented at T7 (`claude -p`, inside a fresh Q6 bracket) rather than the cheaper verdict-split. A genuinely fresh, non-subagent `claude -p` process performed the ceremony step for real (no "simulate" framing) and its transcript was pulled directly from its own session JSONL, not self-reported — its one real reply contained zero mentions of the tool, matching the rule. | fixed r2 — verified from the session file itself, not the ledger's word: `~/.claude/projects/-Users-andreaslottes-aSPARK/4c947ca7-eff7-4a1d-a33e-1e9981852f5a.jsonl` exists (31 records) and carries `isSidechain: false`, `permissionMode: bypassPermissions`, `turnOrigin: sdk` — a genuinely independent process, not an `Agent` subagent. It holds exactly one `Bash` tool_use (the documented probe, verbatim), its result `runner=no`/`graph=no`, and exactly one assistant text block, byte-identical to `evidence.md:104`. Zero tool mentions. No "SIMULATED" framing anywhere in the prompt |
| F4 | Minor | `.spark/graph-mcp-verification/evidence.md:63` | F1's quote of the prior sweep was presented as a quotation but paraphrased it ("The symlink is **machine-global**: `~/aSPARK` **now resolves** …"); the source reads "The symlink is global, so `~/aSPARK` moved from `runner=no, graph=no` (silent) to …". It also cited a section name, not a `file:line`, which NFR-3 requires. Reviewer replaced it with the verbatim text and the citation `.spark/graph-gates/evidence.md:681-684`. | fixed r1 |
| F5 | Minor | `.spark/graph-mcp-verification/evidence.md:361` | Teardown line read "all **four** registrations of this sweep, M4/M6/M7 plus README/plugin untouched" — there are three MCP registrations and "README/plugin untouched" is not a registration. Reviewer corrected to "all three MCP registrations of this sweep, M4/M6/M7". | fixed r1 |
| F6 | Minor | `.spark/graph-mcp-verification/evidence.md:252` | AC-4.1's citation read `skills/demo-day/SKILL.md:55-57`, but the quoted sentence ends "…at the given URL" on **line 58**. A one-line-short range in the evidence that exists to close issue #10 on exact citations. Reviewer corrected to `55-58`; the other two citations (`agents/qa-tester.md:8`, `README.md:65`) re-derived from source and are exact. | fixed r1 |
| F7 | Minor | `.spark/graph-mcp-verification/evidence.md:264,280` (M6, M7) | Both browser backends were registered as `npx -y …@latest`, and no version of either server is recorded — nor of `aspark-graph` (note: its CLI has no `--version`; `pip show` in the runner's venv would give one). #10 therefore closes on "Playwright MCP and Chrome DevTools MCP work" without naming *which* build worked, and NFR-5's reproducibility bar ("re-running the quoted command") silently resolves to a different artifact tomorrow. **Fix:** record the resolved versions (e.g. `npm view @playwright/mcp version` at the time of the run) alongside M6/M7, or state plainly that the verdicts are version-unpinned. | fixed r2 — all three re-derived live, all three match: `find` → `aspark_graph-0.7.0.dist-info` in the runner's venv, `npm view @playwright/mcp version` → `0.0.82`, `npm view chrome-devtools-mcp version` → `1.9.0`. The after-the-fact caveat at M6 is stated honestly rather than glossed |
| F8 | Minor | `.spark/graph-mcp-verification/evidence.md:94,134` | "Quoted instruction and full transcript are this task's own record" points at material that exists nowhere a reader can reach — the transcripts are not in the ledger or the repo. Both of the sweep's headline counts (AC-1.1's `0`, AC-2.1's `1`) are therefore re-countable only by re-running the ceremony, not by the re-count `plan.md:75` promises ("Reproduction = re-count over the **quoted** transcript or artifact"). Same weakness at Entry 7's `0` CLI probes, which rests on the session's own self-report. **Fix:** either inline the (short) emitted blocks, or replace the dangling pointer with one sentence stating that the counting source is the runner's own capture and that re-running is the reproduction path. Entry 2's dangling pointer was superseded entirely by F3's re-run (its transcript is now inlined from a real session file); Entry 4 and Entry 7 got the one-sentence reproducibility-path note. | fixed r2 — Entry 2's count is now genuinely re-countable (I re-counted it from the JSONL). Entry 4's and Entry 7's notes are present and their justification checks out: zero `isSidechain` records exist in any of today's session files, so "no retrievable standing transcript" is a fact, not a convenience |
| F9 | Minor | `.spark/graph-mcp-verification/evidence.md:128` | The T4 run "stopped … after presenting the drafted plan, before gate approval (step 6)", while AC-2.1 and T4's DoD both say "start to finish". Disclosed honestly but not labelled a deviation, and the fact that makes it harmless is not cited — `tools/aspark-graph.md:26-28` ("Resolve **once**, as the last sub-step of the ceremony's existing gate check" / "**At most one hint sentence fires per run, at most once.**") plus `skills/sprint-plan/SKILL.md:29-43`, which put the only hint site in step 1. Without that citation a reader cannot tell whether the count is complete or a lower bound. **Fix:** add the citation and mark the truncation a bounded, accepted deviation. | fixed r2 (substance) — the deviation is now labelled bounded and accepted, and I re-derived the claim rather than accepting it: `skills/sprint-plan/SKILL.md:29-43` is the only resolution/hint site; the sole later mention (`:50`) is step 2 *passing* the tool file, conditional on step 1, not a second resolution. The count is complete, not a lower bound. The new citation's line range is itself wrong — F13 |
| F10 | Minor | `.spark/graph-mcp-verification/evidence.md:315,326` | AC-3.4 and AC-4.3 carry `N/A this run`, a value outside the four-verdict vocabulary the ledger declares at its own head and that T12's DoD requires ("exactly one verdict from the §1 vocabulary"). The verdict is the honest one — a conditional AC whose antecedent never fired is neither passed nor unproven — but the vocabulary should say so. **Fix:** add a fifth, explicitly defined value to the Method header (e.g. `N/A (failure path not triggered)`) so T12's own rule is true of its own table. | fixed r2 — the fifth value is defined at `evidence.md:18`, and `grep -n "N/A this run" evidence.md` returns nothing: all four occurrences (AC-3.4, AC-4.3, in both entry prose and the T12 tables) were replaced, 6 uses of the new value in total |
| F11 | **Major** | `.spark/graph-mcp-verification/evidence.md:33` (M8), `:96` (Entry 2) | M8 ratifies the bypassed execution mode for **"Entries 7, 8, 10, 11's fresh-session legs"** and grounds the user's waiver on containment: *"each invocation was cwd-bound to a disposable scratch trail (`v-mcp-trail` or `v-page`), **never `~/aSPARK`**"*. That is false as written, and the fix-mode pass itself made it false: F3's own re-run is a **fifth** `bypassPermissions` process, and its session record shows `cwd = /Users/andreaslottes/aSPARK` — the protected tree, inside the open M1/M2 bracket. I enumerated every `bypassPermissions` session on this machine dated 2026-09-21: exactly five, four in `v-mcp-trail`/`v-page` (M8's four, containment confirmed) and this one in `~/aSPARK`. Entry 2:96 claims it ran "under the user's post-hoc-ratified `bypassPermissions` mode — see M8", but M8's own text excludes it. It matters for the same reason F2 did: this ledger's thesis is that every mutation names its authorization, AC-1.2 is a Must AC, and the user ruled on a four-leg framing that did not include a permission-bypassed run in the repo the feature's fence protects. I will not silently widen a user's waiver to cover a run they were not shown. The exposure itself is benign and I can prove it — the transcript holds exactly one tool call, the read-only documented probe — which is stronger evidence than the four ratified legs have. **Fix:** amend M8 to name the fifth invocation (Entry 2's F3 re-run), its real cwd `~/aSPARK`, and its verified blast radius (one read-only `Bash` probe, checkable in the cited JSONL); delete or correct "never `~/aSPARK`"; then put the corrected row to the user, since only the user can extend the waiver. **Done:** M8 corrected to name all five runs, disclose the original false claim rather than silently rewrite over it, and record the user's second explicit ratification ("yes, grant it") after being shown the fifth run's real, single-tool-call blast radius. | **waived** (user ruling 2026-09-21, second "yes, grant it", after review of the corrected M8 and the fifth run's verified single-probe blast radius). **r3:** waiver confirmed properly recorded, re-derived not trusted — M8 names **five** runs and Entry 2's re-run among them; the sentence *"This row originally claimed 'never `~/aSPARK`' … false"* discloses the superseded claim rather than erasing it; the second ratification is recorded with what the user was shown. Independently: exactly five `bypassPermissions` sessions exist dated 2026-09-21 (no sixth from the fix pass), and the fifth's JSONL holds one `tool_use` — the read-only probe — one result and one reply, so M8's "nothing else; no writes, no other command" is literally true |
| F12 | Minor | `.spark/graph-mcp-verification/evidence.md:96,107` | The re-run's prompt (session JSONL record 2) does more than restate the skill rule: it ends *"say zero words about aspark-graph, the graph, staleness, impact, or building anything, if that's what the rule calls for."* The evidence describes the instruction only as "no 'simulate,' no narrated reasoning section", so a reader takes the silence as an unprompted consequence of the rule. It matters because the sweep's headline count for AC-1.1 is *zero mentions*, and the prompt names the exact strings not to say — the branch decision was still the model's, but the output's shape was partly supplied. Not a verdict-flipper: the probe, its `runner=no`/`graph=no` result and the reply are all genuinely real. **Fix:** one sentence at Entry 2 disclosing that the prompt constrained the reply's form conditionally on the rule, so the count is "a real run under a form-constrained prompt", not "an unprompted silence". | fixed r3 — the note is at `evidence.md:98`, and its quote is verbatim against the prompt I re-read in the JSONL (*"say zero words about aspark-graph, the graph, staleness, impact, or building anything, if that's what the rule calls for"*). Its characterization is accurate: the clause is conditional on the rule, and the branch choice remained the process's own |
| F13 | Minor | `.spark/graph-mcp-verification/evidence.md:139` | F9's new citation reads `tools/aspark-graph.md:26-28` for a two-part quote. Only the second part is there (`:27-28`, and `:26` is blank); the first part — *"Resolve **once**, as the last sub-step of the ceremony's existing gate check, and only after that gate has passed"* — is at **`tools/aspark-graph.md:16-17`**. This is the F6 defect class recurring inside an F9 fix, in a ledger whose NFR-3 requires verbatim quote plus exact `file:line` and which exists partly to close #10 on citation exactness. The claim it supports is true (re-derived above). **Fix:** cite `tools/aspark-graph.md:16-17` and `:27-28` as the two ranges the ellipsis joins. | fixed r3 — all three ranges re-read from source and exact: `:16-17` carries the "Resolve **once** … only after that gate has passed" sentence, `:27-28` the "At most one hint sentence fires per run, at most once" sentence, and `skills/sprint-plan/SKILL.md:29-44` is the step-1 block's true extent (step 2 starts at `:45`). A residual mislabel inside this same fix is F14 |
| F14 | Minor | `.spark/graph-mcp-verification/evidence.md:141` | F13's fix added the parenthetical "(step 2 at `:40` only *passes the tool file*…)". `:40` is **not** step 2 — it sits inside step 1's own block (`:29-44`) and reads "pass the tool file in step 2 only when both hold"; step 2 begins at `:45`, and its own pass-through sentence is at `:49-50`, which the corrected text no longer cites at all even though round 2's verification rested on it. It matters because this is the F6→F13 citation-exactness class recurring a third time, inside the fix meant to close it, in a ledger whose NFR-3 demands exact `file:line`. The claim it supports is unaffected — I re-derived it again: step 1 is the single resolution site, and both `:40` and `:49-50` merely *pass* the file conditional on that one resolution. **Fix:** name both later mentions with their real locations and stop calling `:40` step 2. | fixed r3 — Reviewer-fixed in place at `evidence.md:141`; both lines verified from source before editing |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `evidence.md:80-117` (Entry 2) | ✅ met r2 — re-run for real; I verified the transcript in its own session file (form-constrained prompt: F12) |
| AC-1.2 | `evidence.md:24-33` (M1–M8) | ✅ met r3 — M1–M7 carry authorization + restoration, re-verified live; M8 now states its real scope (five runs, one in `~/aSPARK`), discloses the claim it replaced, and carries the user's second ratification |
| AC-1.3 | Entry order 1→11; `evidence.md:106,385` | ✅ met |
| AC-2.1 | `evidence.md:135-149` (Entry 4) | ✅ met r2 — literal count `1`, domain stated; truncation now a bounded deviation I re-derived from source |
| AC-2.2 | `evidence.md:138` | ✅ met — `engineering-manager` tool list re-derived from `agents/engineering-manager.md:8` (`Read, Grep, Glob, Write`): no Bash, as claimed |
| AC-2.3 | `evidence.md:19,132` | ✅ met — rule quoted verbatim against `spec.md:129-132`, domain restated at the count |
| AC-3.1 | `evidence.md:183-216` (Entry 7) | ✅ met — MCP tools named as the surface, 0 CLI probes |
| AC-3.2 | `evidence.md:220-232` (Entry 8) | ✅ met — two independent fresh sessions, identical branch and facts |
| AC-3.3 | `evidence.md:165-181` (Entry 6) | ✅ met — control ran before any registration; non-degenerate answer |
| AC-3.4 | `evidence.md:231,328` | ✅ met r2 — verdict now drawn from the declared vocabulary |
| AC-4.1 | `evidence.md:248-258` (Entry 9) | ✅ met — all three citations re-derived from source; labelled documentation-level, not conflated |
| AC-4.2 | `evidence.md:273-307` (Entries 10, 11) | ✅ met r2 — nav + assertion per backend; versions now recorded and independently re-derived |
| AC-4.3 | `evidence.md:289,307,339` | ✅ met r2 — verdict now drawn from the declared vocabulary |
| AC-4.4 | `evidence.md:292` | ✅ met — separate sessions, separate registrations, separate verdicts |
| NFR-1 | `git status --porcelain`, re-run this round | ✅ met r2 — no tracked file modified, `README.md` untouched; the audit's wording is now correct too |
| NFR-2 | `git diff --cached --stat`, `git status` | ✅ met — `skills/ agents/ tools/ lenses/ templates/ plugin.json` byte-identical to `origin/main`; no version bump |
| NFR-3 | `evidence.md:65,265,141` | ✅ met r3 — every citation I re-read resolves to its quote exactly, including F13's corrected ranges; the one residual mislabel (F14) is fixed |
| NFR-4 | Entries 1–12 | ✅ met r2 — no `confirmed (performed)` now rests on a simulation; the one that did is backed by a real session record |
| NFR-5 | `evidence.md:20,147,220` | ✅ met r2 — Entry 2 is re-countable from its JSONL (I re-counted it); Entries 4/7 name a reproduction path whose premise I verified |
| NFR-6 | M1–M8, `evidence.md:33` | ✅ met r3 — the mode is logged, correctly scoped to all five runs, and ratified twice by the user; the containment claim now matches what the session files actually show |
| NFR-7 | `evidence.md:102`, `tools/aspark-graph.md:26-35` | ✅ met — nothing in this sweep changes any gate's behavior for an absent tool |
| NFR-10 | `evidence.md:296-344` | ✅ met — per-issue tables round nothing up; F1 (the sweep's own) is disclosed and routed, not absorbed |
| NFR-8, NFR-9 | `spec.md:197-198` | ✅ N/A, carried as such |

*Library lens:* §1 public surface — zero new commands, agents, skills or exported names; §2
compatibility — no protected `templates/` structure touched, no version bump needed (verify-only);
§3 packaging — the constitution's declared N/A; §4 contract clarity — NFR-3 satisfied. No
lens finding.

## 5. What Was Checked

- [x] Correctness: every Must AC traced to the entry that earns it; rounds 2 and 3 re-derived F1's, F3's, F7's, F9's, F11's, F12's and F13's underlying facts from primary source rather than citing the round before
- [x] Non-functional: NFR-1–NFR-7, NFR-10 judged; constitution §3, §4, §6 ("nothing unasked") weighed — §6 produced F2 in round 1 and F11 in round 2
- [x] Error handling: the failure paths (AC-3.4, AC-4.3) exist, were not silently skipped, and now carry a defined verdict value (F10 closed)
- [x] Security: no secrets, credentials or customer material; the disposable page holds a random marker only; the two third-party MCP servers were user-authorized (C10), version-pinned after the fact (F7) and torn down — teardown re-confirmed live again this round. The bypassed permission mode is now waived by the user for all five runs, the fifth (in `~/aSPARK`) explicitly and after being shown its verified one-probe blast radius
- [x] Tests: no automated suite is possible (constitution §4); the ledger is the suite — Entry 2's count is now genuinely re-countable from a stored transcript, the rest name an honest reproduction path
- [x] Readability: entries are ordered, each names its venue and registration state; a stranger can reconstruct the configuration

## 6. Verdict

This passes, and it passes on the one thing that was actually in doubt: M8 no longer flatters
itself. I checked its correction the hard way rather than reading its label — I re-enumerated
every permission-bypassed session on this machine dated today (still exactly five; the fix pass
created no sixth) and re-parsed the fifth, which is the contested one: `cwd=/Users/andreaslottes/aSPARK`,
31 records, one `tool_use` — the documented read-only probe — one result, one reply. M8 names all
five runs, keeps the false "never `~/aSPARK`" sentence visible as a superseded claim instead of
quietly overwriting it, and records the user's second explicit ratification alongside what they
were shown before giving it. That is the right shape: the waiver is the user's, the disclosure is
the ledger's, and neither pretends the other happened. F12's disclosure is present and its quote
is verbatim against the prompt I re-read; F13's three ranges are exact. The one thing that did not
hold up is small and of a familiar kind: F13's own fix calls line `:40` "step 2" when `:40` sits
inside step 1 and step 2 begins at `:45`, and it dropped the `:49-50` citation round 2's reasoning
had rested on (F14). The claim underneath is still true — I re-derived it a second time, step 1 is
the single resolution site — so I fixed the label in place rather than opening a fourth round for
it. Everything else re-checked live is unchanged since round 2: nothing committed, no tracked file
touched, no MCP server registered, symlink and graph restored, port free. Two Majors stand waived
by the user (F2, F11) with their rulings recorded accurately, no Blocker was ever open, and
#8, #10 and #11 close on evidence that says plainly where it is thin. `/demo-day` may start.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here) — F1, F3 confirmed `fixed r2`; **F2 and F11 both waived by the user 2026-09-21** (two separate "yes, grant it" rulings), both confirmed at `evidence.md:33` (M8) as accurately recorded: five runs named, the superseded false claim disclosed rather than erased, and the second ruling logged with what the user was shown
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — §6 "nothing executed unasked" holds: all five bypassed runs are logged, user-ratified, and the one in `~/aSPARK` has a blast radius of a single read-only probe, re-verified in its own transcript this round
- [x] All plan deviations documented and accepted — T4, T12, T13 accepted (F9, F10, F13 closed); T7's execution-mode deviation is documented with its true scope and ratified (F11)
- [x] Test suite runs green — N/A by constitution §4; the ledger is the suite and its commands reproduce today (teardown, restoration, symlink, port, fence and all version/citation checks re-run live this round)
- [x] Line budget respected: **Ist 168 / Soll ~150** — 18 over, +3 since round 2 (one new finding row, F14); every other round-3 change was an in-place overwrite, with no `## Round 3` section appended anywhere
- [x] Status set to `passed` — round 3: no Blocker ever open, no Major open (F2 and F11 waived by the user, both verified as accurately recorded), no Minor open (F14 Reviewer-fixed). `/demo-day` may start
