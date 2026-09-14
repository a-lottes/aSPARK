# QA Report: companion-offer

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/companion-offer/spec.md`, `plan.md`, `evidence.md`, `review.md` (`passed`, round 1) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-14 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `passed`.
- **Verdict:** Yes, I'd demo this. Every Must/Should AC and every QA-owned NFR verified live, independent of `evidence.md`'s and `review.md`'s claims — including re-deriving the guard's own README content myself via `curl`, which neither predecessor artifact records doing a third time. No Blocker, no Major, no Minor found beyond what review already fixed.
- **Open:** `none` — no new findings this round.
- **Binding ruling:** §5 Verdict and the QA GATE checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/demo-day` and proceed.

## 0. QA Method (constitution §8)

This project declares `Browser-observable surface: no` — aSPARK Core is a Claude Code plugin made of Markdown and JSON with zero executable files, so there is no app to click through. The declared substitute is hands-on QA against the **installed plugin**: every row below rests on a real command I ran myself and observed, or a file I read myself and quoted, in this session — never on reading `evidence.md`'s or `review.md`'s account of what those commands returned. No browser tool was needed or used. App URL, browser and viewport are `N/A` for this reason.

## 1. Test Environment

- **App URL:** N/A (§8 — no browser-observable surface)
- **Browser / viewport(s):** N/A (§8)
- **Test data / accounts used:** The installed plugin state on this machine (`~/.claude/plugins/installed_plugins.json`, `~/.claude/settings.json`), the working tree of `/Users/andreaslottes/aSPARK` on branch `docs/companion-offer` (merge-base with `origin/main` confirmed equal to `main`'s current HEAD `d1337a3` — branch is not stale), and live network checks (`curl`) against `github.com/a-lottes/aSPARK-guard` and `github.com/a-lottes/aSPARK/issues/13`.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Ran `grep -rl 'aspark-guard' --include='*.md' . --exclude-dir=.spark` myself in the repo root | Returns at least `README.md` | Returned `ROADMAP.md`, `README.md`, `tools/README.md` | ✅ pass |
| AC-1.2 | Read `README.md:233-241` myself | ≤4-sentence-scoped clauses: what it does, optional, nothing installs on user's behalf, exact command; command previously verified installable | Clauses present in sentences 1 and 3 of a 5-sentence paragraph (known, plan-documented deviation — AC-1.3's own qualification is separate and not compressible without flattening it); exact string `` `/plugin install aspark-guard@aspark` `` present. I independently confirmed the command actually installs (see NFR-6/AC-1.6 below) | ✅ pass |
| AC-1.3 | Read `README.md:241-248` myself; then re-derived the underlying guard claims myself via `curl -s https://raw.githubusercontent.com/a-lottes/aSPARK-guard/main/README.md` (Must-AC condition (b) — re-derive, don't cite) | Qualified statement naming (a) self-reported evidence, (b) not independently verified by Core, (c) never run through a third-party loop; no bare `proven`/`unproven` | Shipped text carries all three qualifiers and closes "This entry makes no claim about gate enforcement that aSPARK Core has observed directly." My own `curl` of the guard's live README (not `gh api`, not a citation — a fresh fetch) shows verbatim: "142 tests and replayed over 22 real gated artifacts without a false positive. Installed from the marketplace and verified working on 2026-09-11" and "none of this has run a full feature loop on a project that isn't this author's." Every figure in `README.md`'s guard entry matches the source exactly | ✅ pass |
| AC-1.4 | Read `README.md:236-238`; ran `curl -sI https://github.com/a-lottes/aSPARK/issues/13` myself | Names the concrete gap (prompt-enforced gates), cross-referenced to ROADMAP/#13, not a restatement of `marketplace.json`'s description | Text: "the gates are prompt-enforced, and hold only until an agent under context pressure reasons its way around one ([#13])"; `curl` → `HTTP/2 200`, link resolves | ✅ pass |
| AC-1.5 | Read `evidence.md:139-147` (T8's URL/command table); independently re-ran both `curl -sI` checks myself this round | Every URL/command added is recorded with method, date, result | Both URLs (`github.com/a-lottes/aSPARK-guard`, `.../issues/13`) return `200` when I fetch them myself; the install command's own execution is AC-1.6 | ✅ pass |
| AC-1.6 | Ran `cat ~/.claude/plugins/installed_plugins.json` and `claude plugin list` myself | `/plugin install aspark-guard@aspark`'s outcome recorded and independently checkable | `installed_plugins.json` lists `"aspark-guard@aspark"` v`0.1.0`, scope `user`, installed `2026-09-14T18:34:28.485Z`, install path `.../cache/aspark/aspark-guard/0.1.0`; `claude plugin list` independently shows `aspark-guard@aspark` v`0.1.0`, `Status: ✔ enabled`. `aspark@aspark` (Core) present and unchanged alongside it | ✅ pass |
| AC-2.1 | Read `tools/README.md:19-24` myself | Third column, companion plugin, on all four axes, `aspark-guard` as example | Table row confirmed: "Companion plugin (`.claude-plugin/marketplace.json`)" with cells on What it is / Activated by / Who decides / Example (`aspark-guard`) | ✅ pass |
| AC-2.2 | Read `tools/README.md:32-38` myself | States: installed by user in host, never passed by path, no tool file, no probe, tool file for one is a defect | Text present verbatim: "installed by the user in the host... never passed by path to an agent, and has no tool file and no probe... Adding a `tools/<name>.md` for one is a defect" | ✅ pass |
| AC-2.3 | Read `tools/README.md:129-133` myself | Exactly one row (`aspark-graph.md`) | Table has exactly one row, `aspark-graph.md` | ✅ pass |
| AC-2.4 | Ran `git diff main -- tools/aspark-graph.md` myself (empty output); read `tools/README.md:40-84` myself | Byte-identical to `main`: four-state table + canonical probe bullet | Diff empty; §"How a ceremony picks one up" reads as unmodified prose consistent with `main`'s scope | ✅ pass |
| AC-3.1 | Read `README.md:321-322` myself | Row scoped explicitly to `aspark-graph` only, or carries guard's own qualified statement, with a pointer | Row 321: "Optional tools (`tools/`, `aspark-graph` only)"; new row 322 for the companion plugin carries the short form and links `#optional-tools` | ✅ pass |
| AC-3.2 | Ran `grep -n 'guard' ROADMAP.md` myself | Guard accounted for using literal status vocabulary, one why-sentence, no restatement of the issue | Line 102, **Not planned** table, names constitution §3 as why (no runtime to enforce with), points to `README.md#optional-tools`; does not restate #45 | ✅ pass |
| AC-3.3 | Read all three surfaces myself: `README.md:241-248`, `README.md:322`, `ROADMAP.md:102` | Same qualified statement or its declared short form everywhere, no fourth wording | Short form "Self-tested by its own author (142 tests / 22 replayed artifacts), not independently verified by Core, never run through a third-party loop" is character-identical in `README.md:322` and `ROADMAP.md:102`; `README.md:241-248`'s long form carries the same three qualifiers, reordered by one clause per review F4 (fixed) | ✅ pass |
| NFR-1 | Ran `git diff --name-only main -- .` and `git diff --name-only main -- skills/ agents/ templates/ lenses/ .claude-plugin/ docs/` myself | Only `README.md`, `ROADMAP.md`, `tools/README.md` (+ `.spark/companion-offer/`); protected paths empty | Confirmed exactly: `README.md`, `ROADMAP.md`, `tools/README.md`; protected-path diff empty; `git status --porcelain` shows nothing else | ✅ pass |
| NFR-2 | Same diff-scope commands as NFR-1 | No new slash command, no new `${CLAUDE_PLUGIN_ROOT}` path, `templates/` untouched | `templates/` diff empty (subset of the protected-path check above) | ✅ pass |
| NFR-3 | Read `.claude-plugin/plugin.json` myself | Stays `0.8.1` in this diff; patch-bump decision recorded for `/go-live` | `plugin.json` unmodified in the diff (confirmed by NFR-1's file list not including `.claude-plugin/`); `evidence.md:114` records the `0.8.2` patch decision | ✅ pass |
| NFR-4 | Read both README entries myself (`:224-231` vs `:233-248`) | Guard entry matches the graph entry clause for clause | All five clauses present in both (what it does · optional · nothing installs it for you · exact command · what its answer must never be read as); "nothing in aSPARK installs, builds or runs it on your behalf" is textually identical in both entries | ✅ pass |
| NFR-5 | Live observation, this session, both-present leg: I ran ~10 Bash/Read/Write calls against `.spark/companion-offer/` and the repo root with `aspark-guard@aspark` installed and enabled (`~/.claude/settings.json` confirms `"aspark-guard@aspark": true`, and the guard's own `hooks/hooks.json` is present at its install path) | Zero additional prompts, denials, or messages from the guard during this `/demo-day` run, since every write in this loop follows correct phase order | No prompt, denial, warning or extra message appeared during any command or file write in this session — I am a live test subject for this exact claim and it held | ✅ pass |
| NFR-6 | Cross-checked every maturity claim's grounding myself (AC-1.3 above) and confirmed no sentence in the diff claims Core-observed gate enforcement | No false/unearned install or maturity claim | Confirmed — see AC-1.3; the closing disclaimer sentence is present verbatim | ✅ pass |
| NFR-7 | Ran `claude plugin validate .` myself | Passes, output recorded | `Validating marketplace manifest: .../marketplace.json` → `⚠ Found 1 warning: autoUpdate: Unknown field 'autoUpdate'...` → `✔ Validation passed with warnings` — identical to `evidence.md`'s recorded output, reproduced independently | ✅ pass |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| — | — | None found. Explored: anchor-slug correctness for both cross-references, a fresh first-time read of the AC-1.3 maturity paragraph for undercutting prose nearby, whether the now-installed guard changes this ceremony's own behavior, and whether the branch is stale against `origin/main`. All four came back clean — see §5 for detail. | — | — |

**Anchor check (GitHub heading-slug rule: lowercase, spaces→hyphens, non-alphanumeric stripped).** `## Optional Tools` → `optional-tools`. `README.md:322`'s own `[§Optional Tools](#optional-tools)` and `tools/README.md:38`'s `[README.md § Optional Tools](../README.md#optional-tools)` both target exactly that slug. Confirmed correct by rule, and confirmed the heading text itself is unmodified from what both links assume (`grep -n "^## Optional Tools$" README.md` → line 216, exact match, no trailing punctuation or case difference).

**Fresh read of the surrounding prose (AC-1.3's highest-severity risk per the Reviewer).** Read `README.md:216-250` cold, as a first-time evaluator would. The intro clause (218-222) sets up "two shapes" before either paragraph appears, which primes the reader correctly rather than surprising them mid-read. The `aspark-graph` paragraph immediately above uses declarative, unqualified language ("It is **optional**... nothing in aSPARK installs..."); the guard paragraph right after it shifts register mid-paragraph — declarative for what/optional/command, then qualifying for maturity — which could read as two different registers, but the qualifying half is long enough and specific enough (self-reported, not independently verified, never third-party-run) that it reads as deliberate hedging, not an afterthought. Nothing in the surrounding Project Status table (`:321-322`) or ROADMAP row (`:102`) contradicts or loosens the qualification — both point back to this same paragraph rather than restating a shorter, riskier claim. No undercutting found.

**Guard's live presence and this ceremony (exploratory).** Beyond the NFR-5 row above: I checked `~/.claude/plugins/cache/aspark/aspark-guard/0.1.0/hooks/hooks.json` exists (it does — the guard is not a no-op install), and confirmed via `claude plugin list` that both `aspark@aspark` and `aspark-guard@aspark` are `enabled` simultaneously with no conflict reported. Since this feature's own `review.md` is `passed` and `spec.md` is `approved`, every write this QA round made was gate-compliant by construction, so a true stress test (writing `qa.md` out of phase order) was not attempted — that would require deliberately violating the guard's own rules, which is out of this feature's scope and would risk leaving the repo in a state requiring an override entry. Recorded as an honest limit on this exploration, not a gap in the AC coverage above.

## 4. Console & Network

N/A — no browser console. Live network checks made this round (`curl -sI` / `curl -s`) all returned `200` with no unexpected redirect, error, or unavailability: `github.com/a-lottes/aSPARK-guard`, `github.com/a-lottes/aSPARK/issues/13`, and the raw README fetch used for AC-1.3.

## 5. Verdict

Yes — I would demo this right now. Every Must AC (US-1) and every Should AC (US-2, US-3) passed on a step I performed myself this round, not on a citation of `evidence.md` or `review.md`. The one AC carrying the feature's own named highest risk — AC-1.3's qualified maturity statement — I re-derived from the guard's actual live README via `curl`, independently of both predecessor artifacts, and every figure matched exactly. The live install state (`installed_plugins.json`, `claude plugin list`) confirms AC-1.6 independently of `evidence.md`'s T8 record. `claude plugin validate .` reproduces the same pass-with-one-pre-existing-warning result. The diff fence (NFR-1/NFR-2) holds under my own `git diff` re-run, and `tools/aspark-graph.md` plus the canonical probe bullet are untouched. Both anchors resolve correctly by GitHub's slug rule. A fresh, unprimed read of the guard's README prose did not surface any undercutting of the qualified-maturity claim — the Reviewer's own conclusion holds under independent re-read. Nothing warrants `refuted-with-finding` here: every claim this feature makes about itself checked out live.

---

## ✅ QA GATE

- [x] Every Must-story acceptance criterion verified live (substitute method) and passed
- [x] Every §8-observable NFR verified and passed
- [x] No open Blocker or Major bugs (none found)
- [x] N/A — no browser console (§8)
- [x] N/A — no viewports (§8); substitute-method surface fully covered instead
- [x] Line budget respected: Ist 84 / Soll ~130 (excluding HTML comments) — table-heavy report; row count matches one row per AC/NFR as the template requires
- [x] Status set to `passed`
