# Review Report: companion-offer

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Working-tree diff vs `main`, `.spark/companion-offer/plan.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-14 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `passed`.
- **Verdict:** The AC-1.3 honesty bar holds verbatim and the NFR-1 fence is intact; four Minors were fixed in review, two Nits are open and block nothing.
- **Open:** `1 open` — Blockers: `none`; Majors: `none`; Minors: `none` (`F1`–`F4` fixed r1); Nits: `F6` fixed same-day by user decision, `F5` deferred to `/go-live` (see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

**Reviewed:** the uncommitted working-tree diff against `main` (`d1337a3`) on branch `docs/companion-offer` — `README.md` (+22/-2), `ROADMAP.md` (+1), `tools/README.md` (+14/-6). Surrounding context read in full: `README.md` §Optional Tools + §Project Status, all of `tools/README.md`, `ROADMAP.md` §§Next/Blocked/Not planned, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`. Process artifacts (`spec.md`, `plan.md`, `evidence.md`) read for context and sanity-checked for internal consistency. Binding context: `.spark/constitution.md` in full and `lenses/library.md` §§1, 2, 4 read directly, not via the plan's paraphrase.

**Re-derived from source rather than cited** (predecessor marked them *relayed*, and they carry a Must AC's verification — conditions (b) and (c)): `gh repo view a-lottes/aSPARK-guard` → `PUBLIC`, `pushedAt 2026-09-11`; the guard's `.claude-plugin/plugin.json` → `name: aspark-guard`, `version 0.1.0`; the guard's README → all six milestones **Built**, "proven by 142 tests and replayed over 22 real gated artifacts without a false positive", "Installed from the marketplace and verified working on 2026-09-11 — see `docs/evidence.md` §4", and its own gap "none of this has run a full feature loop on a project that isn't this author's". All four match `evidence.md`. `~/.claude/plugins/installed_plugins.json` re-read: only `aspark@aspark`. `claude plugin validate .` re-run by me post-fix (condition (d) — see F3).

**Not reviewed:** T8 (`/plugin install aspark-guard@aspark` executed live) — designed deferral to `/demo-day` per plan §3 and constitution §6; its absence is not treated as a defect. `aspark-graph` tool file read as context; no `query` call made — an `impact` over three Markdown files returns `unknown_files` by construction (the graph indexes no `.md`), which is structural absence, not a risk signal, so it would have told me nothing. Scoping was done by hand: `git diff`, `grep` and section-level `diff` against `main`.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Canonical long form, short form and install string pinned in `evidence.md:34–53`; baseline recorded at `:60–63`. |
| T2 | ⚠️ | Content complete; two deviations. (a) 5 sentences, not the DoD's "at most four" — **recorded** in plan §Deviations and sound: AC-1.2's four named clauses land in sentences 1 and 3, and compressing AC-1.3's two-sentence statement is the exact flattening plan §5 risk 1 forbids. Nothing was lost — I re-verified all five NFR-4 clauses against the live text. (b) the long form is reordered by one clause vs the pinned wording → **F4**. |
| T3 | ✅ | `README.md:321` scoped to "`aspark-graph` only"; new row `:322` carries the short form byte-for-byte plus the `#optional-tools` pointer. Snapshot block and all other rows verified unmodified. |
| T4 | ⚠️ | Table, paragraph and AC-2.3/AC-2.4 all correct, but the new column header shipped as `Companion plugin`, not the DoD's `Companion plugin (`.claude-plugin/marketplace.json`)` — an **undocumented** deviation → **F2**, fixed. |
| T5 | ✅ | `ROADMAP.md:102` in the **Not planned** table. Scoped to *inside Core*, grounded in constitution §3, does not mention or decline [#13] — which remains untouched in §Next (`:47`). §§head→Not planned and §The wider picture verified byte-identical to `main` by section `diff`. |
| T6 | ⚠️ | The comparison work is real and its five **Hit** verdicts are correct — I re-derived each against the live text. But its wording-match claim was inaccurate → **F4**, fixed. |
| T7 | ⚠️ | Sweep results correct and independently reproduced. The recorded validate command is not reproducible as written → **F3**, fixed. |
| T8 | n/a | `todo` by design — `/demo-day`, gated on the user's explicit go (constitution §6). Not a defect; see §1. |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Minor | `README.md:236–237` | Read "It addresses the gap this project's own roadmap names — the gates **below** are prompt-enforced". Nothing below line 236 describes the gates; the gate table is at `README.md:24` and the prompt-enforcement explanation at `:69` — both *above*. **Why:** a false cross-reference in the repo's most-read file sends the evaluating reader the wrong way, and §4's "always reflects the current state" bar is the one this feature exists to restore. **Fix applied:** dropped the word `below`, matching `ROADMAP.md:47`'s own phrasing ("The gates are prompt-enforced"). | fixed r1 |
| F2 | Minor | `tools/README.md:19` | New column header shipped as `Companion plugin`; plan T4's DoD specifies `Companion plugin (`.claude-plugin/marketplace.json`)`, and the other two columns both name their home path (`Lens (`lenses/`)`, `Tool (`tools/`)`). **Why:** a silent plan deviation, and the omitted path is exactly the one a contributor needs — `marketplace.json` is the *only* place the guard is declared, which is the §1 defect this feature fixes. **Fix applied:** header restored to the planned text; all pre-existing cells verified byte-preserved after the edit. | fixed r1 |
| F3 | Minor | `.spark/companion-offer/evidence.md:96` | Recorded the command as `claude plugin validate`. Run literally, that exits `error: missing required argument 'path'`; only `claude plugin validate .` produces the pasted output. **Why:** constitution §8's substitute-QA method turns on a *real command whose output was observed* — an unreproducible command string degrades NFR-7's evidence to a claim. The output itself is genuine: I re-ran `claude plugin validate .` and it matched byte for byte, warning included. **Fix applied:** command corrected, with the failure mode noted inline. | fixed r1 |
| F4 | Minor | `.spark/companion-offer/evidence.md:67` | T6 claimed "`README.md` §Optional Tools carries T1's long form, also unmodified." It is modified: shipped `README.md:247` reads "the same gap `ROADMAP.md` names about this project itself"; the pinned form (`evidence.md:41–42`) reads "the same gap this project's own `ROADMAP.md` names about itself". **Why:** the wording is equivalently scoped and all three AC-1.3 qualifiers survive, so no verdict changes — but a verification artifact asserting "unmodified" about something modified is the failure mode plan §1 rule 1 exists to catch. **Fix applied:** amended to record both forms verbatim and the reason (avoiding an echo of "this project's own roadmap" two sentences earlier). README prose left as shipped — it is the better read and equally honest. | fixed r1 |
| F5 | Nit | `.spark/companion-offer/spec.md:87` (NFR-1) | NFR-1's stated check is `git diff --name-only main...HEAD`. On the current uncommitted tree that returns **empty**, so it passes vacuously; the substantive fence check was `git diff --name-only main -- .` (T7), which I reproduced. **Why:** the fence is currently proven only against the working tree. **Fix:** re-run `git diff --name-only main...HEAD` once `/go-live` commits, and paste the post-commit result into `evidence.md` §T7. | deferred to `/go-live` |
| F6 | Nit | `.spark/companion-offer/plan.md:106–114` | The recorded deviation is framed against AC-1.2's cap only. T2's own DoD (`plan.md:57`) carries a second, unconditional cap — "The body of the guard paragraph is at most four sentences" — which the entry also misses and which the note does not mention. **Why:** the reasoning is right, but a deviation note that names the weaker of the two rules it broke is harder to audit next round. **Fix applied:** the note now names both caps explicitly, with a line marking the correction. | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `README.md:233` | ✅ met — `grep -rl 'aspark-guard' --include='*.md' . --exclude-dir=.spark` re-run by me → `README.md`, `ROADMAP.md`, `tools/README.md` (baseline: none) |
| AC-1.2 | `README.md:233–240` | ✅ met — all four clauses in sentences 1 and 3; literal `/plugin install aspark-guard@aspark`. Command shape re-verified against the live repo and its `plugin.json` (§1). Five-sentence entry is the accepted T2 deviation |
| AC-1.3 | `README.md:241–248` | ✅ met — (a) "142 tests replayed over 22 real gated artifacts with no false positive, and an author-verified marketplace install dated 2026-09-11 (its own `docs/evidence.md` §4)"; (b) "self-reported by the guard's own author, has not been independently verified by aSPARK Core"; (c) "has never been exercised through a full third-party feature loop". Closes with "This entry makes no claim about gate enforcement that aSPARK Core has observed directly." Nothing softened, dropped, or restated in Core's voice. **Re-derived from the guard's own README** (condition (b)) — all figures match |
| AC-1.4 | `README.md:236–239` | ✅ met — names prompt-enforced gates and links [#13]; paraphrases, does not copy, `marketplace.json`'s description |
| AC-1.5 | `evidence.md:11–26` | ⚠️ partial *by design* — repo/manifest checks recorded with date and method and correctly marked researched-not-executed; the `#13` URL added by T2 is not yet recorded. Completion is T8's DoD. **Critically, the shipped prose claims no verification T8 has not yet produced** — the install line is an instruction, and the only dated install claim is explicitly attributed to the guard's author |
| AC-1.6 | — | ⚠️ deferred — T8 / `/demo-day`, gated on the user's go (constitution §6). Not claimed anywhere as done |
| AC-2.1 | `tools/README.md:19–24` | ✅ met — third column on all four existing axes, `aspark-guard` as Example |
| AC-2.2 | `tools/README.md:32–38` | ✅ met — installed by the user in the host, never passed by path, no tool file, no probe, "Adding a `tools/<name>.md` for one is a defect" |
| AC-2.3 | `tools/README.md:129–` | ✅ met — §Available tools verified byte-identical to `main` by section `diff`; exactly one row |
| AC-2.4 | `tools/aspark-graph.md`, `tools/README.md:54–93` | ✅ met — `git diff main -- tools/aspark-graph.md` empty; §"The canonical probe bullet" (incl. the `no`/`no` → **say nothing** row) byte-identical by section `diff`. §§How a ceremony picks one up, The tool file contract, Adding another tool also verified identical |
| AC-3.1 | `README.md:321–322` | ✅ met — row scoped to "`aspark-graph` only" plus a new companion row pointing to §Optional Tools |
| AC-3.2 | `ROADMAP.md:102` | ✅ met — placed in the **Not planned** table, one why-sentence, no restatement of #45 |
| AC-3.3 | `README.md:322`, `ROADMAP.md:102`, `README.md:241–248` | ✅ met — short form verified **character-identical** in both table cells (case of the leading letter aside); §Optional Tools carries the long form, equivalently scoped (F4). `tools/README.md:37–38` makes no maturity claim and defers by link — no fourth wording, no looser claim |
| NFR-1 | working tree | ✅ met — `git diff --name-only main -- .` → exactly the three files; `git diff --name-only main -- skills/ agents/ templates/ lenses/ .claude-plugin/ docs/` → empty; under `tools/`, only `README.md`. `git status --porcelain` shows no other modification and `.spark/companion-offer/` untracked. See F5 for the post-commit re-run |
| NFR-2 | — | ✅ met (`library` §1) — no new slash command, no new `${CLAUDE_PLUGIN_ROOT}` path, `templates/` untouched, so every §3 protected heading/column/ID pattern is unchanged. Zero addition to the consumed contract |
| NFR-3 | `.claude-plugin/plugin.json` | ✅ met (`library` §2) — still `0.8.1`, unmodified; the `0.8.2` patch decision is recorded at `evidence.md:110–` for `/go-live`. Purely additive prose: no removal, no rename, no deprecation — no semver effect beyond patch |
| NFR-4 | `README.md:233–248` vs `:225–232` | ✅ met (`library` §4) — I re-derived all five clauses against the live text rather than trusting T6's table; each is present and each has a counterpart in the `aspark-graph` entry. The "nothing in aSPARK installs, builds or runs it on your behalf" clause is identical in both |
| NFR-5 | working tree | ✅ met for the both-absent leg — no file any ceremony reads changed, so zero prompts are added. The both-present leg is T8's and is not claimed. Constitution §6 degrade-to-silence is untouched: the README's own "no error, no warning, no mention" sentence is unmodified, and the guard's write-denying behaviour is disclosed plainly at `:234–235` before the install line, so a reader installs it knowing what it does |
| NFR-6 | `README.md:241–248`, `evidence.md` | ✅ met — every maturity claim is grounded inline and attributed; no sentence presents the guard's self-report, or an intention, as Core's delivered proof. Constitution §3's "no install claim that isn't true at the time of writing" holds: the command's shape was checked against the source repo and manifest, and `evidence.md` says plainly it has not been executed |
| NFR-7 | — | ✅ met (early) — `claude plugin validate .` re-run by me after my fixes: `✔ Validation passed with warnings`. The single `autoUpdate` warning is pre-existing on `main` and out of scope (spec §6 item 6) |

## 5. What Was Checked

- [x] Correctness: every Must AC traced to live text and re-read there, not taken from `evidence.md`
- [x] Non-functional: NFR-1…NFR-7 above; constitution §§1, 3, 4, 5, 6 and `library` §§1, 2, 4 checked directly against the diff
- [x] Error handling: n/a — no code path; the degrade-to-silence contract is the analogue and is untouched (NFR-5)
- [x] Security: no secret, credential or personal material added; both added URLs are public GitHub repos; §6 "nothing installed unasked" holds — no auto-install, and T8 is gated on the user's go
- [x] Tests: none exist and none are possible (constitution §4). The substitute bar was exercised: `claude plugin validate .` re-run green, the AC-1.1 `grep` re-run, and every byte-identity claim re-derived by section `diff` against `main`
- [x] Readability: purely additive; all pre-existing table cells and protected sections verified byte-preserved

## 6. Verdict

This passes. The one thing most likely to go wrong here — AC-1.3's qualified maturity statement getting softened into something that reads as Core's own claim — did not go wrong: the shipped paragraph at `README.md:241–248` carries all three qualifiers intact, attributes the evidence to the guard's author by name, and closes by disclaiming any gate-enforcement claim Core has observed. I re-derived the underlying figures from the guard's own repository rather than citing `evidence.md`, because that fact is a Must AC's verification and the predecessor marked it relayed; every number matched. The NFR-1 fence holds under independent measurement, `tools/aspark-graph.md` and the canonical probe bullet are byte-identical to `main`, and none of spec §6's ten cuts appears anywhere in the diff. What I did find were four Minors, all fixed in review and none of them a product defect: one false positional cross-reference in the README ("the gates below"), one silently dropped qualifier in a table header, and two inaccuracies in the evidence trail — a validate command that does not run as written, and a T6 claim of "unmodified" about wording that was in fact reordered. That last pair is worth naming plainly: the verification work behind them was genuine and its conclusions were right, but a verification artifact that overstates its own precision is the one kind of error this project cannot afford, because every later gate reads it instead of the source. Two Nits stay open, both housekeeping — the NFR-1 command needs one re-run after the commit lands, and the recorded T2 deviation names the weaker of the two caps it broke. Neither blocks `/demo-day`. T8 remains correctly `todo` and, importantly, nothing in the shipped prose borrows credit from it.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings — none raised
- [x] No open Major findings — none raised; the four Minors are `fixed r1`, the two open items are Nits
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — AC-1.1…AC-1.4 met; AC-1.5 partial and AC-1.6 deferred **by design** to T8 at `/demo-day`, gated on the user's explicit go per §6, and neither is claimed as done anywhere in the diff
- [x] All plan deviations documented and accepted — T2's is recorded in plan §Deviations and reviewed as sound (F6 asks only that the note name both caps); T4's was undocumented (F2) and is now fixed by restoring plan conformance, so no undocumented deviation remains
- [x] Test suite runs green — no suite exists or is possible (constitution §4); the declared substitute bar ran green: `claude plugin validate .` re-executed post-fix, plus the AC-1.1 `grep` and the byte-identity `diff`s
- [x] Line budget respected: Ist 102 / Soll ~150 (excluding HTML comments)
- [x] Status set to `passed`
