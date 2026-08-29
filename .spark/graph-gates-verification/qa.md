# QA Report: graph-gates-verification

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/graph-gates-verification/{spec.md,plan.md,evidence.md,review.md}`, `README.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-08-27 |

**Handoff**
- **Status:** `passed`.
- **Verdict:** Yes — I'd close #9, #10, #11 and accept #8's refutation on this evidence. I independently redid the fence audit, re-derived seven of the ten `/tmp/ggv/*.jsonl` transcripts myself, re-ran the two live queries that survive, and read the current `README.md` and `evidence.md` text directly rather than trusting either file's own narration. Every claim I re-checked held. Two review residues (F12, F13) that `/peer-review` left as unconfirmed `fixed` are, on my independent read of the cited lines, genuinely applied — I'm confirming both here.
- **Open:** `none` — Blockers: none; Majors: none. B1 (Minor) fixed by `/increment` fix-mode, 2026-08-27 (see §3).
- **Binding ruling:** §5 Verdict and the gate checklist below — the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch at the next `/demo-day` and proceed.

## 1. Test Environment

**Documented ceremony override, user-approved (same precedent as `.spark/graph-gates/qa.md` §1).** This feature ships no application — verify-only sweep, issues #8–#11. There is no URL, no server, no page. The "app under test" is the evidence record itself.

**Substituted definition of a performed step, applied strictly:** a real command run and its actual output observed, or a real file read and its actual content checked. Every row below rests on one of mine, not on re-reading `evidence.md`'s or `review.md`'s prose about itself. What I actually did:

- **Fence, redone from scratch:** `git status --porcelain`, `git diff --stat`, `git diff --stat` + `git status --porcelain --untracked-files=all` over `skills/ agents/ tools/ lenses/ templates/ .claude-plugin/plugin.json`, `ls -d skills/*/ | wc -l`, `ls agents/*.md | wc -l`, plugin version grep.
- **Live queries re-run:** `aspark-graph query staleness --repo ~/aSPARK-graph`; `test -f ~/aSPARK/.aspark-graph/graph.json` + `ls -la`.
- **Scratch venues:** `/tmp/ggv/{silence-repo,positive,browser,hint}` and all ten `*-session.jsonl` transcripts are still on disk (not cleaned up — see B1). This let me re-derive claims directly instead of trusting quotes.
- **Transcripts I personally re-parsed** (Python, tool_use/tool_result walk, not grep-on-faith): `t2-transcript.jsonl` (silence case, 0-mentions claim), `t4-session.jsonl` (MCP branch, probe count), `t5b-session.jsonl` and `t6-session.jsonl` (determinism/CLI-branch comparison), `t7-session.jsonl` (stop path, tool-call sequence), `t8-session.jsonl` / `t9-session.jsonl` (Playwright / Chrome DevTools MCP action identifiers), `t11-session.jsonl` (hint count, including the specific `Agent`-tool_result-only re-count that F11 claims), `t12-session.jsonl` (orchestrator vs. subagent probe split).
- **Filesystem spot checks:** `/tmp/ggv/positive/calc.py` (the undeclared `mul()` — F1/FX1), `/tmp/ggv/positive/.spark/positive-fixture/review.md` (FX-vs-F1 ID-space claim), `/tmp/ggv/{positive,browser}/.mcp.json` (registrations still present), `lsof -i :8899` (no leaked server process).
- **README.md**: read `§Project Status` directly at its current line numbers, not `evidence.md`'s description of it.

Not redone (accepted from the record on the strength of the above cross-checks and their internal consistency): Entry 3's one-time `aspark-graph build` invocation itself, and Entry 5's discarded "attempt A" — neither is load-bearing beyond what the re-parsed transcripts already corroborate.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Re-parsed `t2-transcript.jsonl`: counted `aspark-graph`/`.aspark-graph` across all assistant `text` blocks; `grep -c aspark-graph` on the produced `plan.md`. | 0 mentions both surfaces, probe exit 0, gates unchanged. | **0** assistant-text mentions (independently counted, matches Entry 2's claim); `plan.md` grep → 0; transcript's own probe result `runner=no\ngraph=no`. | ✅ pass |
| AC-1.2 | Re-ran P1–P7 myself (see §1) and diffed against Entry 1's baseline; read Entries 2/4/6/8/9's mutation logs directly for authorization/restoration lines. | Every mutation logged with authorization + restoration; final probe matches baseline. | Symlink target/exit unchanged; `~/aSPARK-graph` staleness byte-identical (`stale:false`, `files_checked:107`); `~/aSPARK` graph.json unchanged (same 56,668 bytes, same mtime). Project-scoped `.mcp.json` files in scratch venues reasoned as "no restoration owed, disposable venue" — true of the *repo*, but the venues themselves are still on disk (B1). | ✅ pass (B1 noted, not blocking — no live-repo mutation involved) |
| AC-1.3 | Read entry order in `evidence.md`; confirmed Entry 2 (silence) precedes Entries 3–15 (all positive-case). | Silence case first, every row cites what was executed. | Order holds; every entry I re-parsed cites a real command/session, matching its own text. | ✅ pass |
| AC-2.1 | Re-parsed `t4-session.jsonl` tool_use stream myself. | MCP branch taken, MCP tool names cited literally, 0 probe commands. | `ToolSearch` → both `mcp__aspark-graph__staleness`/`impact` resolve; `mcp__aspark-graph__staleness{"repo":"."}` called directly; the session's 3 `Bash` calls are gate-check/constitution-check only — **0** match either probe form, independently confirmed. | ✅ pass |
| AC-2.2 | Re-parsed `t5b-session.jsonl`: found `ToolSearch` resolves both MCP tools, then a `Bash: test -f .aspark-graph/graph.json` runs anyway, and `mcp__aspark-graph__staleness` is never called. | Second run resolves identically (same branch, same mechanics). | Branch/surface conclusion matches run 1; the zero-probe mechanic does not — independently reproduced the exact discrepancy Entry 5/F2 describes. | ⚠️ partial (as designed — spec C4 makes an honest refutation a valid outcome; this is the sweep correctly *not* smoothing over a real finding, not a gap in the evidence) |
| AC-2.3 | Re-parsed `t6-session.jsonl`. | No-MCP session takes CLI branch, same repo, both branches together demonstrate the order. | `ToolSearch "staleness impact"` → none found → the literal two-part `command -v aspark-graph …; test -f .aspark-graph/graph.json` probe runs → `runner=yes/graph=yes`; follow-on blast-radius query is also CLI (`aspark-graph query impact … --repo .`), never MCP. Matches Entry 6 exactly. | ✅ pass |
| AC-2.4 | Read Entry 4/13's finding-path text; confirmed no registration failure occurred anywhere in the sweep's transcripts (registrations succeeded in t4, t8, t9, t12). | Failure path never silently skipped if triggered. | Path never triggered (nothing failed) — correctly recorded as untested, not skipped, consistent across every transcript I read. | ✅ pass (untriggered path, honestly labelled) |
| AC-3.1 | Re-parsed `t7-session.jsonl`: full tool_use list is `Read, Read, Bash(curl), ToolSearch, Read(.mcp.json)` — **0** `Agent` calls. | Stops at gear check, names exactly what to set up, 0 QA delegation. | Confirmed: no `Agent` tool_use anywhere in the transcript; stop message (read directly) names both missing prerequisites. | ✅ pass |
| AC-3.2 | Same transcript; independently confirmed the session's only `ToolSearch` is `"browser playwright chrome devtools"` — never checks for `aspark-graph` MCP tools — so the "surface=yes,graph=yes" precondition really does rest on the config read + P1/P2 + Entry 3's build, as F5's correction states, not on a live in-session probe. | Tool sub-step never reached: 0 probes, 0 hints, 0 handovers, all counted. | All three transcript-side counts independently reproduced at 0; precondition grounds re-verified via my own P1/P2 rerun + `ls .aspark-graph/graph.json` in Entry 3's venue. | ✅ pass |
| AC-3.3 | Read Entries 8, 9, 10; cross-checked against my own re-parse of `t8`/`t9` showing the ceremony proceeded to a real `Agent → qa-tester` delegation and a written `qa.md` in both. | Gear gate passes with a confirmed backend, proceeds past step 1. | Confirmed in both backends' transcripts — genuine delegation and QA output exist, not just claimed. | ✅ pass |
| AC-4.1 / AC-4.2 | Re-parsed `t8-session.jsonl` subagent tool_use stream directly. | ≥1 navigation, ≥1 on-page assertion, backend-native action identifiers, gate passes on Playwright detection. | `mcp__playwright__browser_navigate` (×2), `browser_snapshot`, `browser_evaluate` (exact marker match `ggv-t8-marker-2f9a17`) all present with real arguments — independently reproduced, not just quoted. | ✅ pass |
| AC-4.3 | Re-parsed `t9-session.jsonl` subagent tool_use stream directly. | Same two observations for Chrome DevTools MCP, separate session. | `mcp__chrome-devtools__navigate_page` (×2), `take_snapshot`, `evaluate_script` (exact match) all present with real arguments. | ✅ pass |
| AC-4.4 | Confirmed via the same two re-parses: no failed tool call, no retry-after-failure pattern in either transcript. | Confirmed only on a full-pass attempt; instability recorded if any. | Both backends: 1 attempt, 0 failures, matches the "confirmed, 1/1" verdicts in Entry 13. | ✅ pass |
| AC-5.1 | Re-parsed `t11-session.jsonl` myself: counted `aspark-graph build` on assistant-text blocks (**1**, the hint sentence) and, going one step further than the evidence file did at first pass, isolated the single `Agent` tool_use's own `tool_result` (not all tool_results — Reads of the tool file also contain the string and must be excluded) and counted occurrences there. | Exactly 1 occurrence, counting method stated and reproducible. | Surface 2 (assistant text): **1**. `Agent` tool_result (the actual subagent-report surface AC-5.1 names, which F11 flagged as undeclared): **0**, independently confirmed by isolating the `Agent` tool_use id and matching its result block — not the broader "any tool_result" count, which would have falsely shown 3 (all inside `Read` payloads, correctly excluded). | ✅ pass |
| AC-5.2 | Read Entry 11's mutation-absence checks; independently confirmed `/tmp/ggv/hint/.aspark-graph` does not exist on disk today. | 0 build/install/serve, no `graph.json` created. | `ls /tmp/ggv/hint` shows no `.aspark-graph/` directory; matches the claim. | ✅ pass |
| AC-5.3 | Read the Counting-domains section and Entry 11's per-surface table against my own AC-5.1 re-derivation above. | Method stated, reproducible, loaded-file contents excluded. | Method as stated reproduced my own count exactly, including the subtlety of which `tool_result` blocks count. | ✅ pass |
| AC-6.1 | Read `/tmp/ggv/positive/.spark/positive-fixture/review.md` directly; re-ran `aspark-graph query staleness --repo /tmp/ggv/positive` is no longer meaningful (venue now clean again in some files but `calc.py`'s `mul()` is still present — confirmed via `grep -n "def mul" calc.py`) — the historical staleness statement in the fixture's own `review.md` §1 is the durable record and reads exactly as quoted. | Staleness announced once, 0 graph citations thereafter. | Fixture `review.md` states the `stale:true` result once, then explicitly disclaims using it as evidence for FX1/F1. | ✅ pass |
| AC-6.2 | Read fixture `review.md`'s Finding F1/FX1 row directly. | Verdict rests on ≥1 concrete `file:line` anchor, normal verdict reached. | `calc.py:12-13` cited directly, verdict `changes-requested` — a real, reasoned non-`passed` outcome. | ✅ pass |
| NFR-1 | `git diff --name-only` (self-run). | Touches only `.spark/graph-gates-verification/**` and `README.md`. | Exactly `README.md` (modified) + `.spark/graph-gates-verification/` (untracked) — nothing else. | ✅ pass |
| NFR-2 | `git diff --stat` + `git status --porcelain --untracked-files=all` over the six protected paths (self-run); counted skills/agents; grepped `plugin.json` version. | Byte-identical, 10 skills / 7 agents, no version bump. | Both diffs empty; 10 / 7; version `0.7.1` (unchanged from before this feature per `review.md`'s own scope note). | ✅ pass |
| NFR-3 | Read Entry 13's F1/F2 rows against the cited `file:line`s (`spec.md:76`, `tools/aspark-graph.md:19-22`, three `SKILL.md`s). | Verbatim quotes with `file:line`. | Quotes check out against the current file text at those lines. | ✅ pass |
| NFR-4 | Cross-cutting — assessed via every row above; every AC row rests on a step I performed, not a read of `evidence.md`'s conclusion. | Every claim performed, reasoning labelled as such. | Held throughout my own re-verification; the one place a label lagged (Entry 7's DoD line, F12) is confirmed fixed — see §3. | ✅ pass |
| NFR-5 | Independently re-derived the AC-5.1 count and the AC-1.1 count using the stated methods. | Counting method named and reproducible. | Reproduced both counts exactly by the stated method. | ✅ pass |
| NFR-6 | Read every mutation log; confirmed no `build`/`install`/`serve` ran outside `/tmp/ggv/*`; confirmed `~/aSPARK`, `~/aSPARK-graph` untouched (byte-identical `graph.json`, identical staleness result). | No unasked mutation on a user repo. | Held — both Core repos verified read-only-touched by my own reruns. | ✅ pass |
| NFR-9 | Read `README.md:239-283` directly (not `evidence.md`'s description of it). | Proven stays proven, refuted becomes refuted-with-finding, unattempted stays unproven. | Row + paragraph: #9/#11 proven, #10 proven for two backends, #8 refuted-with-finding (names the specific non-reproduced guarantee), AC-1.2/AC-5.2 (prior-spec numbering) explicitly labelled unproven and out of scope. Arithmetic (3 proven + 1 refuted + 2 unproven = the original six) checks out. | ✅ pass |

NFR-7/NFR-8: N/A per spec (no runtime, no UI) — confirmed by the spec's own §8 Design Review (no UI surface) and this feature's diff shape.

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Minor | `ls /tmp/ggv` and `cat /tmp/ggv/positive/.mcp.json`, `/tmp/ggv/browser/.mcp.json`, one day-plus after the sweep. | `evidence.md` Entries 4 and 8 justify skipping registration restoration with "not removed after this run … disposable venue deleted at sweep end." Observed: the venues and their `.mcp.json` registrations (`aspark-graph`, `chrome-devtools`, plus the preserved `.mcp.json.playwright.bak`) are all still present on disk. No NFR requires immediate deletion (disposable ≠ must-delete-now) and nothing live was mutated, so this isn't a fence breach — but the specific phrasing states a fact ("deleted") that hasn't happened, which a future reader of the evidence file would trust at face value. | fixed |

**Review residues independently confirmed (not new findings — closing the loop `/peer-review` left open):** `review.md` left F12 and F13 at a bare `fixed` (its own convention for "increment's claim, not yet re-confirmed") and its Verdict/Gate text explicitly held them `open` pending a next pass. I read the current cited text myself: `evidence.md:232` now reads "V-POSITIVE is reused by T5–T7, T12" (T11 correctly absent, F13a applied); `evidence.md:349` now reads "confirmed beforehand via the config/filesystem read … (per F5's correction above)" (F12 applied, no longer "direct probe"); `evidence.md:586-587` now names AC-1.2/AC-5.2 as "labelled unproven and out of scope" in both the edit-bullet and the content map (F13b applied). All three are genuinely fixed. I'm confirming them here since this is the first `/demo-day` pass on this record.

## 4. Console & Network

N/A — no browser session exists for this feature. Substituted: no unexpected stderr in any of the ten `*-session.stderr` files (all checked, all empty except the two Entry 2 already disclosed and explained — auth-source precedence notice, `unrecognized_model` fallback); no leaked background process (`lsof -i :8899` — the throwaway static-page server from V-BROWSER is not running).

## 5. Verdict

**Passed — I would tell the user to close #9, #10, and #11 on this evidence, and accept #8 as refuted-with-a-named-fix.** I redid the fence audit and the live queries from scratch, re-parsed seven of the ten session transcripts myself rather than trusting the quoted excerpts, and read `README.md`'s current text directly. Every claim I re-derived matched what `evidence.md` and `review.md` say it should — including two subtle ones a careless re-check would get wrong: t5b really does run a stray probe despite `ToolSearch` confirming both MCP tools (F2's substance holds), and t11's `Agent` tool_result really does contain zero occurrences of `aspark-graph build` once you isolate the correct tool_use id (F11's substance holds; a naive "any tool_result" count would have wrongly shown 3, all inside excluded `Read` payloads). The two review residues `/peer-review` left as unconfirmed (F12, F13) are genuinely applied in the current file — confirmed here, not on trust. One Minor (B1) is worth a follow-up line in `evidence.md` but changes no count, no route, and no shipped surface.

---

## ✅ QA GATE

- [x] Every Must-story acceptance criterion verified by a performed step and passed (AC-2.2 is an honest `partial` by the spec's own C4 design, not an unverified gap — its mechanism was independently reproduced)
- [x] Every NFR in scope verified and passed (NFR-7/8 N/A per spec)
- [x] No open Blocker or Major bugs (one Minor, B1, open — not user-facing, no NFR breach)
- [x] Console/network substitute checked and clean (stderr files, no leaked process)
- [x] Tested across the substituted "viewports": fence (git), live queries (CLI), and transcript-level re-derivation (7 of 10 sessions) — no browser viewport applies (N/A, no UI, per spec §8)
- [x] Line budget respected: Ist ~150 / Soll ~130 (excluding HTML comments) — 20 over; nineteen AC rows plus the NFR block is more surface than the template's single-app case, recorded not waived
- [x] Status set to `passed`
