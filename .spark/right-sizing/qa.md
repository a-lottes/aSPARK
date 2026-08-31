# QA Report: right-sizing

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Installed plugin `0.7.1`, content-diff verified against working tree; `.spark/right-sizing/spec.md` (AC-1.1–1.10, AC-2.1–2.5, NFR-1–6); `review.md` r5 finding `F23` |
| **Status** | `passed` |
| **Round** | 8 |
| **Date** | 2026-08-31 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** **F23 closed.** The two `qa-tester.md` edits that landed after round 7's Run 1
  (F18/F19: the false `yes`-surface routing claim, and the "nothing more" phrase read as
  contradicting the later allowance) do not reopen the STOP-branch behaviour. A fresh, dedicated
  repro of Run 1's exact scenario — Venue A, ordinary invocation, no narration, no keyword
  contamination — against the current text stopped correctly and named only the missing tool/URL,
  with no offer to declare a substitute method. A second run at the same venue under an explicit
  narration demand held too, and even said so explicitly ("I am not going to suggest that the
  project adopt a substitute QA method"). A third run (Venue B, `surface: yes`, ordinary) confirms
  the sibling AC-1.5 guarantee still holds and reproduces the known Minor (verbatim field quoting).
  3/3 clean on the action-based rule this round.
- **Open:** `0`. **F23 fixed r8** (new evidence, not carried from round 7 — Run 1 in §2/§3 is a
  fresh invocation against the post-F18/F19 text, not a re-read of round 7's now-superseded
  transcript). **B5 remains fixed**, now doubly confirmed (r7's original repro plus this round's
  fresh one, both against text current at time of test). **B1, B4 remain fixed r6**, reconfirmed
  with fresh live evidence this round (Run 3 independently reproduces the verbatim-quoting pattern
  landing at Minor, not Blocker, under `C19`). **B2, B3 remain fixed r2**, reconfirmed by fresh grep
  this round, not carried over from round 7's citation. **F-spec remains fixed r6** — fresh read of
  `spec.md:12` and `:255` this round finds them consistent, no recurrence of round 6's self-
  contradiction. NFR-5 informational, not QA-owned.
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a
  finding at the next `/demo-day` and proceed — don't stop on it.

## 1. Test Environment

**Venue self-check: CURRENT, re-confirmed this round, not trusted from the caller.** `diff -rq`
between the installed cache (`~/.claude/plugins/cache/aspark/aspark/0.7.1`) and the working tree
over `agents/`, `skills/`, `templates/` → **zero differences**; a direct `diff` of
`agents/qa-tester.md` between the two locations is also empty. The installed `aspark:qa-tester`
agent invoked below runs the exact current text, including T13's post-round-7 F18/F19 edits at
`agents/qa-tester.md:45-55/62-65` (Entry 15 §15.4's diff scope, confirmed by inspection here too).

- **App URL / Browser / viewport(s):** `N/A` — `.spark/constitution.md` §8 declares
  `Browser-observable surface: no`. Source: `.spark/constitution.md` §8.
- **Declared QA method (performed):** hands-on QA against the installed plugin.
- **Object under test — content diff, not `gitCommitSha`** (Entry 9's rule) — see venue self-check
  above.
- **Live venues this round — 3 sequential, foreground, single invocations, no fan-out** (prior
  rate-limit hit that pattern twice, per this round's instruction). Two fresh fixtures under the
  session scratchpad, same shapes as prior rounds, not reused: `venue-A-round8` (no
  `.spark/constitution.md` at all; `.spark/sample-feature/spec.md`, two ACs, no application code
  anywhere in the tree) and `venue-B-round8` (`.spark/constitution.md` with `Browser-observable
  surface: yes` plus a named substitute method — the AC-1.5 load-bearing shape; same `sample-
  feature` spec). **Run 1 = F23's exact scenario**: Venue A, ordinary invocation, no narration
  requested, no "declaration"/"constitution"/"§8"/"substitute" keywords in the prompt — a plain QA
  request naming only the feature and project path. **Run 2** = same venue, explicit demand to
  narrate all internal reasoning (completes F23's own stated repro scope, "ordinary +
  narration-demanding"). **Run 3** = Venue B, ordinary invocation (standing re-check of one of round
  7's other combinations, confirming AC-1.5 and the B1/B4 pattern have not regressed). Each is a
  real, sequential, foreground invocation of the installed `aspark:qa-tester` agent via the Agent
  tool.
- **Method limits, unchanged, reproduced fresh.** `claude -p "say hi"` →
  `Failed to authenticate: OAuth session expired and could not be refreshed`, re-run this round.
  `skills/demo-day/SKILL.md`, `skills/spark/SKILL.md`, `skills/go-live/SKILL.md`,
  `agents/release-manager.md` remain `not-verified-live` for this same, environment-caused reason
  (`evidence.md` Entry 15 §15.3, `review.md` r5) — carried forward, not re-litigated.
- **Tool (`aspark-graph`):** not queried this round; no `Result` cell rests on it.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | This session is the venue: `/demo-day` resolved §8 and delegated to me, method in place of URL/viewports; confirmed against all 3 live runs below | Proceeds by declared method, no override asked | No override negotiated with the user this session | ✅ pass |
| AC-1.2 | This file itself: count `AC-`/`NFR-` ID rows in §2 | Every AC + every NFR under its own ID | 15 AC rows + 6 NFR rows | ✅ pass |
| AC-1.3 | **Re-derived (condition (a) — F23 is a fix to the exact text this AC's evidence rests on).** 3 live, sequential, foreground runs: Run 1 = F23's scenario (Venue A, ordinary); Run 2 = Venue A, narration-demanding; Run 3 = Venue B, ordinary | Under `C19`: never ask/error/warn/re-negotiate; own-words statement fine; verbatim quoting discouraged, capped Minor | **3/3 clean on the action rule.** Run 1: stopped, named only "a URL where the app is running" and "confirmation `/increment` should run first" as needs — no mention of declaring anything; stated in its own words that no constitution/declaration exists. Run 2 (narration-demanding): fully narrated its check, explicitly stated "I am not going to suggest that the project adopt a substitute QA method — that would itself be the kind of re-negotiation I'm required to avoid raising" — a correct self-description, not an offer — then asked only for a URL. Run 3 (Venue B): correctly treated `surface: yes` as foreclosing the substitute path and asked only for the app/URL, but wrote "declares `Browser-observable surface: yes`" — verbatim field quoting, Minor per `C19`'s explicit cap | ✅ **pass r8** |
| AC-1.4 | Fresh grep `agents/release-manager.md:65-67` | Cites §8 as standing project fact | Text present, unchanged | ✅ pass |
| AC-1.5 | Run 3 (Venue B, `surface: yes` + named method) | Live-browser requirement not suppressed even with a method present | Held: Run 3 treated `surface: yes` as foreclosing the substitute-method path and applied the ordinary equipment check (found no app, stopped) — never the declared route | ✅ pass |
| AC-1.6 | Fresh grep `agents/qa-tester.md:45,93,96,98`; all 3 live runs hit missing-app equipment failures and stopped rather than fabricating results | Stops and names what it cannot perform | Text present, unchanged; all 3 runs stopped and listed exactly what was missing (app/URL, or confirmation to run `/increment` first) | ✅ pass |
| AC-1.7 | Fresh grep `agents/reviewer.md` for `QA Method`/`§8`/`Browser-observable surface`/`substitute.*QA` (0 hits, `grep` exit 1) + `spec.md:123` | Fence holds; list scoped to declaration values | Confirmed, unchanged | ✅ pass |
| AC-1.8 | Fresh grep `agents/facilitator.md:114-115` | Explicit, never inferred | Confirmed, unchanged | ✅ pass |
| AC-1.9 | Fresh read `agents/qa-tester.md:91-95` | Falls back to ask, never suppression | Text present, unchanged ("run the equipment check... STOP and report... ambiguity resolves toward more verification, never less") | ✅ pass |
| AC-1.10 | Fresh grep `agents/qa-tester.md:120-122` | Only `/charter` writes it | Confirmed; no test run wrote to any fixture's constitution | ✅ pass |
| AC-2.1 | Citations throughout this file (spec.md, evidence.md, review.md by ID) | Cite, don't re-derive | Done | ✅ pass |
| AC-2.2 | Fresh grep `agents/qa-tester.md:231-241` | Four conditions named, bounded reading | Confirmed, unchanged | ✅ pass |
| AC-2.3 | Applied to F23/AC-1.3 above (condition (a) named inline) | Names triggering condition | Done | ✅ pass |
| AC-2.4 | Applied to F23 itself (a wording/mechanism-timing finding, capped Minor by `review.md` r5) | Artifact-wording findings capped at Minor | Correctly capped — see `review.md:99` | ✅ pass |
| AC-2.5 | Fresh `git diff HEAD -- agents/` grep for migration language | Nothing differs, no migration | Zero hits | ✅ pass |
| NFR-1 | Fresh `git status --short templates/` | Purely additive | No uncommitted change | ✅ pass |
| NFR-2 | Fresh dir counts | Zero new commands/agents/lenses/template files | 10/7/9/6 unchanged | ✅ pass |
| NFR-3 | Fresh greps across touched locations (this session) | Each states coverage/scope/authority/conditions | All confirmed present, unchanged | ✅ pass |
| NFR-4 | Same 3 live runs as AC-1.3 | No error, no warning, no ask, no re-negotiation | Identical evidence to AC-1.3: 3/3 clean on the action rule, 1/3 Minor verbatim-quoting | ✅ **pass r8** |
| NFR-5 | `spec.md:150` names `/peer-review`, not `/demo-day` | Release notes claim only S1/S2 | Not a QA-owned NFR — informational only | `not-verified-live` (out of scope) |
| NFR-6 | Fresh gate-item counts, all five templates (isolated to each template's own GATE section, not whole-file checkbox counts) | Identical gate/item count | SPEC 11, PLAN 10, REVIEW 7, QA 7, KEEP 6 — unchanged | ✅ pass |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| F23 | Minor → confirmed fixed | Invoke the installed `qa-tester` agent live, ordinary invocation, no narration, no keyword contamination, on a fixture with no `.spark/constitution.md` and no application at all (Venue A, exact B5/round-7-Run-1 conditions), against the text as it stands **after** T13's F18/F19 edits | Expected: STOP-branch behaviour holds against the current text, not just the pre-edit text round 7 tested. Observed: Run 1 named only "a URL" and "confirmation `/increment` should run first" — no mention of declaring anything. Run 2 (same venue, narration-demanding, completing F23's own stated scope) held too, and explicitly named the do-not-suggest rule as its own reason for not offering a substitute method | fixed r8 |
| B5 | Blocker → confirmed fixed | Same class of scenario as F23 (Venue A, ordinary, no narration) | Never offer a substitute-method declaration as an unblocking option | Doubly confirmed: round 7's original repro plus this round's fresh repro against the post-F18/F19 text, both clean | fixed r7, reconfirmed r8 |
| B1 | Blocker → superseded | Fresh Run 3 this round (Venue B, verbatim quoting of `Browser-observable surface: yes`) | Under `C19` this lands as Minor, not Blocker, reconfirmed with fresh live evidence this round (1/1 Venue B run quoted the field verbatim) | fixed r6, reconfirmed r8 |
| B4 | Blocker → superseded | All 3 live runs this round checked for the "Step N — apply the constitution check" labelled-placeholder pattern | Pattern did not recur in any of the 3 runs | fixed r6, reconfirmed r8 |
| B2 | Minor | Fresh grep `agents/reviewer.md` for `QA Method`/`§8`/`Browser-observable surface`/`substitute.*QA` (0 hits) | AC-1.7 scoped "at every value of this declaration"; grep confirms zero declaration-specific references in `reviewer.md` | fixed r2, reconfirmed r8 |
| B3 | Minor | Fresh grep `templates/constitution.md` for `/spark` | `/spark` named in the enumeration (`:102`, `:115`) | fixed r2, reconfirmed r8 |
| F-spec | Minor | Fresh read `.spark/right-sizing/spec.md` Handoff (`:12`) vs. its own SPEC GATE line (`:255`) this round | Both lines read consistently ("re-approved a fourth time, 2026-08-31," after `C19`) — no recurrence of round 6's self-contradiction | fixed r6, reconfirmed r8 |

**Re-confirmed, unchanged.** `claude -p` still cannot authenticate (`Failed to authenticate: OAuth
session expired`), reproduced fresh. `skills/demo-day/SKILL.md`, `agents/release-manager.md`,
`skills/spark/SKILL.md` remain untested live for the same reason — an accepted, environment-caused
limit (`evidence.md` Entry 15 §15.3, `review.md` r5), not re-litigated this round.

**Not probed:** the `skills/*/SKILL.md` orchestrator half via a live nested session (auth still
fails); `/go-live` on this project (no `release.md` yet).

## 4. Console & Network

`N/A` under the declared method. Substitute runtime signals:

- 3 fresh, sequential, foreground agent invocations this round: all completed without tool crashes
  or errors. None wrote a stray `qa.md` into either fixture (all 3 correctly recognized nothing
  could be verified and stopped without fabricating results).
- `claude -p` → `Failed to authenticate: OAuth session expired`, reproduced fresh. Environment
  limit, not a product defect.
- `aspark-graph` not queried; no `Result` cell rests on it (see §1).

## 5. Verdict

**Would I demo this to a stakeholder right now? Yes.**

F23 is closed on its own terms: the two post-round-7 edits to the STOP branch (F18's false
`yes`-surface routing claim, F19's "nothing more" phrasing) do not reopen the behaviour B5 fixed.
A fresh, dedicated repro of the exact leaking scenario — no constitution, no app, ordinary
invocation, against the current text — stopped correctly, and a second run at the same venue under
an explicit narration demand held too, with the agent correctly self-describing its own
do-not-suggest constraint rather than working around it. That is stronger evidence than citing
round 7's now-superseded transcript would have been, which is exactly what F23 asked for.

The standing re-check (Venue B, ordinary) confirms nothing regressed: AC-1.5's guarantee still
holds, and the one residual behavior C19 already names as discouraged-but-not-blocking — verbatim
quoting of the raw declaration field — recurred once, landing correctly at Minor. B1–B5 are not
carried over on faith; this round's 3 live runs independently reproduce or fail to reproduce each
pattern fresh, and B2/B3/F-spec are reconfirmed by fresh grep rather than citation alone.

Zero open Blocker or Major bugs. The mechanism this feature exists to prove — declare the QA method
once, stop re-negotiating it per feature, and hold that guarantee even against direct edits to the
file that carries it — has now cleared a live re-test performed *after* a further edit to the exact
branch it protects, which is the harder and more relevant bar than a same-round self-test would have
been.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run
`/demo-day`. On re-test, edit this same checklist in place — never duplicate it as a second gate.*

- [x] Every Must-story acceptance criterion verified in the real browser and passed — **N/A on the
  browser clause** (§8, surface `no`); **AC-1.3 passes** this round, 3/3 clean live runs including
  F23's dedicated repro against the post-F18/F19 text
- [x] Every browser-observable NFR verified and passed — **N/A on the browser clause**; **NFR-4
  passes** this round, identical evidence to AC-1.3. NFR-2/3/5 belong to `/peer-review` per
  `spec.md`'s own column, not counted against this box
- [x] No open Blocker or Major bugs (Minor bugs listed and accepted by the user) — **0 open**;
  F23/B5/B1/B4/B2/B3/F-spec all `fixed`, reconfirmed with fresh evidence this round. One Minor
  verbatim-quoting instance observed (Run 3) and listed, not Blocker/Major
- [x] Browser console free of errors on the tested flows — **N/A**, no browser; §4's substitute
  signals show no tool-level errors across all 3 runs
- [x] Tested on all agreed viewports — **N/A** per §8, same basis as the box above
- [x] Line budget respected — **Ist 175 / Soll ~130, over, recorded not waived** — same shape as
  every prior round: verification-table detail plus verbatim reproduction quotes needed to make each
  run reproducible by someone else, per this role's own Hard Rule
- [x] Status set to `passed` — per the header table and Handoff above; F23 closed, nothing else open
