# QA Report: graph-mcp-verification

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/graph-mcp-verification/spec.md`, `evidence.md`, `review.md` (`passed` r3); constitution §8 |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-21 |

**Handoff**
- **Status:** `passed` — no new defect found; every AC and NFR carries a performed-step verdict.
- **Verdict:** Yes, demo this now. All 14 ACs and 10 NFRs (2 N/A) are `confirmed`; every claim I could cheaply and safely re-derive myself matched the ledger exactly; the claims gated behind new MCP registration/build/serve were left un-repeated per this pass's explicit fence and are covered instead by /peer-review's own from-primary-source re-derivation across 3 rounds, which I spot-checked and reproduced identically.
- **Open:** `none`
- **Binding ruling:** §5 Verdict and the gate checklist below — the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/demo-day` and proceed.

## 1. Test Environment

- **App URL:** N/A — constitution §8 declares `Browser-observable surface: no` with a performable substitute method (hands-on QA against the installed plugin); confirmed by reading §8 directly (`.spark/constitution.md:247-283`) before starting. Per `/demo-day`'s own gate logic this is a complete, performable declaration, so the browser/URL check does not apply — no Claude-in-Chrome/Playwright MCP/Chrome DevTools MCP backend was sought for this pass.
- **Browser / viewport(s):** N/A — no browser surface exists in this repo (verify-only Markdown evidence ledger, no runtime code, no UI).
- **Test data / accounts used:** the live `~/aSPARK` checkout at commit `2ec691c` (`HEAD` == `origin/main`); no new scratch fixtures created this round — see §2 for what was re-probed in place versus cited from `evidence.md`/`review.md`.

## 2. Acceptance Criteria Verification

<!-- "QA-performed" = command I ran myself this round, output shown/matched below. "Cited, cross-checked" = relies on evidence.md's own performed step, independently re-derived from primary source by /peer-review (not merely re-read), plus my own citation-accuracy check where applicable. Neither MCP registration nor `aspark-graph build` was re-run this round — both are excluded by this pass's explicit no-new-install/build/register/serve fence. -->

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | QA-performed: re-parsed `~/.claude/projects/-Users-andreaslottes-aSPARK/4c947ca7-eff7-4a1d-a33e-1e9981852f5a.jsonl` myself (the session `evidence.md` Entry 2 cites); ran live `claude mcp list` | `cwd=~/aSPARK`, non-sidechain, exactly 1 Bash tool_use (the documented probe), 1 reply with 0 tool mentions; `claude mcp list` shows no graph/browser MCP | Matched exactly: `cwd=/Users/andreaslottes/aSPARK`, `isSidechain=False`, 1 tool_use = the documented probe, 1 text block = *"The optional-tool check is done. Moving on to step 2..."* (0 mentions of aspark-graph/graph/staleness/impact/build); prompt's disclosure clause re-read verbatim, matches F12's quote exactly; `claude mcp list` shows only the unrelated `claude.ai Docs` connector | ✅ pass |
| AC-1.2 | QA-performed: `command -v aspark-graph`, `test -f .aspark-graph/graph.json`, `readlink -f ~/.local/bin/aspark-graph`, `claude mcp list`, `git status --porcelain`, `lsof -ti:8934` — the same final-state probes Entry 12 recorded | All mutations (M1–M8) restored; state identical to Entry 1/12's baseline | `runner=yes, graph=yes`; symlink → `/Users/andreaslottes/aSPARK-graph/.venv/bin/aspark-graph` (byte-identical to Entry 1); `claude mcp list` clean; `git status --porcelain` shows only `.spark/.guard/` + `.spark/graph-mcp-verification/`; port 8934 free (no process) | ✅ pass |
| AC-1.3 | Cited: entry order read in `evidence.md` (Entry 2 precedes Entries 3–11) | Silence case precedes every positive-case entry | Confirmed by direct reading — no positive claim appears before Entry 2 | ✅ pass |
| AC-2.1 | QA-performed: `grep -n` for the exact cited spans in `tools/aspark-graph.md` (`:16-17`, `:27-28`) and `skills/sprint-plan/SKILL.md` (step 1 spans `:23-44`, step 2 begins `:45`, its pass-through at `:49`). Cited: literal count of "1" from Entry 4 (subagent self-report, not independently re-countable — transcript not retained, per F8, corroborated by `review.md`'s own scope note: "Not reviewed: Entries 4/7/8/10/11's own transcripts") | Citations exact; single-hint-site claim holds | All citations matched exactly, character for character. The "exactly 1" figure itself rests on Entry 4's documented method and was not re-run this round (would require a fresh `/sprint-plan` ceremony invocation outside this pass's cheap/read-only scope) — same disclosed limitation the ledger and review already carry, not a new gap | ✅ pass (reproducibility caveat carried forward, not new) |
| AC-2.2 | QA-performed: read `agents/engineering-manager.md` frontmatter | `engineering-manager` has no Bash access | `tools: Read, Grep, Glob, Write` — confirmed, no Bash | ✅ pass |
| AC-2.3 | QA-performed: compared `evidence.md`'s quoted counting-domain rule against `spec.md:129-132` verbatim | Rule quoted verbatim, domain stated | Exact match | ✅ pass |
| AC-3.1 | Cited, cross-checked: Entry 7; `review.md` round 1 independently re-derived the subagent/MCP-visibility constraint and re-read the fresh-session output | MCP branch taken, 0 CLI probes | Matches Entry 7 and Reviewer's independent check; not re-invoked this round (new MCP registration excluded by this pass's fence) | ✅ pass |
| AC-3.2 | Cited, cross-checked: Entry 8 | Deterministic across 2 fresh sessions | Matches; not re-invoked this round | ✅ pass |
| AC-3.3 | Cited, cross-checked: Entry 6 | CLI branch taken, no MCP registered | Matches; not re-invoked (would need a built scratch graph — a new `build`, excluded by fence) | ✅ pass |
| AC-3.4 | Cited: Entry 7 | Registration succeeded both times → `N/A (failure path not triggered)` | Matches declared vocabulary | ✅ pass |
| AC-4.1 | QA-performed: re-read all 3 citations at their exact `file:line`s myself | `skills/demo-day/SKILL.md:55-58`, `agents/qa-tester.md:8`, `README.md:65` say what's quoted | All three verbatim-exact — including a live meta-check: this very ceremony run followed `skills/demo-day/SKILL.md:55`'s own "unless §8 declared a performable substitute method" clause to skip the browser gate, which is the behavior AC-4.1 documents | ✅ pass |
| AC-4.2 (Playwright MCP) | Cited, cross-checked: Entry 10; `review.md` r2 independently re-derived the pinned version (`0.0.82`) | ≥1 nav, ≥1 assertion, `confirmed (performed)` | Matches; not re-invoked (new MCP registration + page serve excluded by fence) | ✅ pass |
| AC-4.2 (Chrome DevTools MCP) | Cited, cross-checked: Entry 11; version `1.9.0` independently re-derived by Reviewer | ≥1 nav, ≥1 assertion, `confirmed (performed)` | Matches; not re-invoked | ✅ pass |
| AC-4.3 | Cited: Entries 10–11 | Both backends succeeded → `N/A (failure path not triggered)` | Matches declared vocabulary | ✅ pass |
| AC-4.4 | Cited: Entry 11 | Independent verdicts, no cross-contamination | Separate sessions/registrations confirmed by entry text | ✅ pass |
| NFR-1 | QA-performed: `git status --porcelain`, `git diff --name-only origin/main...HEAD` | Only `.spark/graph-mcp-verification/**` + pre-existing `.spark/.guard/`; `README.md` untouched | Confirmed live, matches | ✅ pass |
| NFR-2 | QA-performed: same diff (empty) covers protected paths | `skills/ agents/ tools/ lenses/ templates/ plugin.json` byte-identical | Confirmed — empty diff against `origin/main` | ✅ pass |
| NFR-3 | QA-performed: re-read 6 citations total (AC-4.1's 3, `tools/aspark-graph.md`'s 2, `.spark/graph-gates/evidence.md:681-684`) | Every quote verbatim + exact `file:line` | All 6 exact | ✅ pass |
| NFR-4 | Cited, cross-checked: `review.md` F3's fix, independently re-verified by me via the same JSONL (AC-1.1 row above) | No `confirmed (performed)` rests on a labelled simulation | Confirmed — the one entry that did was re-run for real (F3), and I re-derived that from the session file myself, not from the label | ✅ pass |
| NFR-5 | Cited: `evidence.md`'s stated counting methods (AC-2.1, AC-3.1/3.3) | Every zero/exactly-once claim states its method | Present; AC-2.1's count itself carries the reproducibility caveat noted above | ✅ pass |
| NFR-6 | QA-performed: live probes above (no leftover MCP registration, port free, symlink/graph restored) + independent JSONL re-parse of the 5th `bypassPermissions` run (M8/F11) | Every mutation restored; the ratified bypass mode's scope matches what the user was shown | Confirmed live; the 5th run's JSONL holds exactly the one read-only probe M8 claims, cwd `~/aSPARK`, nothing else | ✅ pass |
| NFR-7 | Cited: Entry 2 (no gate consulted the probe's outcome) | This sweep changes no gate's behavior for the absent case | Self-evident from the re-parsed transcript (single reply, no gate logic invoked) | ✅ pass |
| NFR-8 | Cited: `spec.md:197` | N/A — no runtime/scale concern | Confirmed by reading spec | ✅ N/A |
| NFR-9 | Cited: `spec.md:198` | N/A — no UI | Confirmed by reading spec | ✅ N/A |
| NFR-10 | Cited: full read of `evidence.md`'s per-issue verdict tables | No verdict rounded up; F1 disclosed, not absorbed | Confirmed — every verdict uses the declared 5-value vocabulary, nothing overstated | ✅ pass |

## 3. Exploratory Findings

None. I looked specifically for: (a) any AC whose "confirmed" verdict looked doubtful on a fresh, independent read — none found; every citation I re-checked was exact and every live-state probe matched the ledger's claimed end state exactly; (b) whether the declared §8 method itself was being correctly applied to this very ceremony run — it was (AC-4.1's meta-check above); (c) whether any of the three still-open GitHub issues' claims looked shakier than their verdict states — no, #8's two-branch determinism, #11's silence-then-hint behavior, and #10's two backends all check out against independently re-derived primary sources (session JSONLs, exact `file:line`s, live command output) rather than resting on the ledger's word alone.

No table row below — nothing to report.

## 4. Console & Network

N/A — no browser surface, no console, no network requests to observe (constitution §8). The nearest analogue, `claude mcp list`, was run live twice this round and stayed clean throughout (only the unrelated `claude.ai Docs` connector, no `aspark-graph`/Playwright/Chrome DevTools MCP entries left registered).

## 5. Verdict

Yes, I'd demo this right now. This is a verify-only evidence ledger, not runtime code, so "demo" means: does the written record actually hold up when a skeptical third party re-runs its cheapest, safest checks independently? It does. I re-parsed the one contested session transcript (the 5th `bypassPermissions` run, previously F11) myself rather than trusting the ledger's or the Reviewer's word, and it matches both exactly: one `cwd=~/aSPARK` process, one read-only Bash probe, one reply, nothing else. Every `file:line` citation I re-read (9 total, across `tools/aspark-graph.md`, `skills/sprint-plan/SKILL.md`, `skills/demo-day/SKILL.md`, `agents/qa-tester.md`, `README.md`, `agents/engineering-manager.md`, `.spark/graph-gates/evidence.md`) resolved to exactly the quoted text. Every live-state probe (symlink target, graph presence, `claude mcp list`, `git status`, open port) matches the ledger's claimed restored end state. The one honest residual gap — AC-2.1's literal hint-count resting on an unrepeatable subagent self-report — is not new: `evidence.md` (F8) and `review.md` both already disclose it, neither this round nor the prior one found grounds to doubt the number itself, and closing that gap would mean re-running a ceremony, which this pass's own fence reserves for explicit authorization. Three GitHub issues (#8, #10, #11) close on evidence that has now been checked from two independent angles (Reviewer, QA) without drift.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run `/demo-day`.*

- [x] Every Must-story acceptance criterion verified by the declared method and passed — 14/14 (US-1–US-4)
- [x] Every NFR QA owns verified and passed (or N/A with reason) — 8 pass, 2 N/A (NFR-8, NFR-9, both per spec)
- [x] No open Blocker or Major bugs (Minor bugs listed and accepted by the user) — none found
- [x] Browser console free of errors on the tested flows — N/A, no browser surface (§8)
- [x] Tested on all agreed viewports — N/A, no browser surface (§8)
- [x] Line budget respected: Ist 82 / Soll ~130 (excluding HTML comments; file is 83 lines total, 1 HTML comment line)
- [x] Status set to `passed`
