# QA Report: right-sizing

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Installed plugin `0.7.1`, content-diff verified against working tree; `.spark/right-sizing/spec.md` (AC-1.1–1.10, AC-2.1–2.5, NFR-1–6) |
| **Status** | `passed` |
| **Round** | 7 |
| **Date** | 2026-08-31 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** **C19's re-scoped rule now holds 5/5 on its full designed test matrix** — the
  dedicated B5 reproduction plus all 4 standard combinations ({no-declaration/`yes`-surface} ×
  {ordinary/narration-demanding}). Zero asks, errors, warnings or re-negotiations across any run.
  Two runs (both Venue B) quoted the raw `Browser-observable surface: yes` field verbatim in their
  live reply — Minor per C19's explicit cap, not Blocker, and not gate-blocking.
- **Open:** `0`. **B5 fixed r7** (confirmed live: the dedicated repro run — no constitution, no app,
  ordinary invocation — did not offer a substitute-method declaration as an unblocking option; it
  named only the missing tool/URL). **B1, B4 remain fixed r6**, reconfirmed with fresh evidence this
  round (Runs 4–5 show the exact old B1/B4-shaped behavior — verbatim field quoting — correctly
  landing at Minor under C19, not Blocker). **B2, B3 remain fixed r2.** **F-spec corrected to `fixed
  r6`** (was left `open` in round 6's own table despite round 6's Handoff and prose both stating the
  spec self-contradiction was "corrected in place" that same round — an Entry-11-shaped lag inside
  round 6's own report, caught by this round's gate/Handoff sanity check and fixed here, not
  re-derived as a new defect). NFR-5 informational, not QA-owned.
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a
  finding at the next `/demo-day` and proceed — don't stop on it.

## 1. Test Environment

**Venue self-check: CURRENT.** `agents/qa-tester.md:46-47` contains "Do not suggest, among other
options, that the project could declare a substitute QA method" — round 7's fix for `B5` (spec
`C19`). Confirmed directly, not assumed, before any other step.

- **App URL / Browser / viewport(s):** `N/A` — `.spark/constitution.md` §8 declares
  `Browser-observable surface: no`. Source: `.spark/constitution.md` §8.
- **Declared QA method (performed):** hands-on QA against the installed plugin.
- **Object under test — content diff, not `gitCommitSha`** (Entry 9's rule). `diff -rq` cache
  (`~/.claude/plugins/cache/aspark/aspark/0.7.1`) vs. working tree over `agents/ skills/ templates/`
  → **zero differences**; `grep` for B5's fix string in the cache copy of `agents/qa-tester.md` hits
  at the same line as the working tree. The installed `aspark:qa-tester` agent invoked below runs
  the current, post-fix text.
- **Live venues this round — 5 sequential, foreground, single invocations, no fan-out** (prior
  rate-limit hit that pattern once, per this round's instruction). Two fresh fixtures under the
  session scratchpad, same shapes as round 6's, not reused: `venue-A-round7` (no
  `.spark/constitution.md` at all; `.spark/sample-feature/spec.md`, two ACs, no application code of
  any kind anywhere in the tree) and `venue-B-round7` (`.spark/constitution.md` with
  `Browser-observable surface: yes` **plus** a named substitute method — the AC-1.5 load-bearing
  shape; same `sample-feature` spec). Run 1 = **B5's exact scenario** (Venue A, ordinary invocation,
  no narration, no keyword contamination — a plain QA request). Runs 2–5 = the 4 standing
  combinations fresh: run 2 = Venue A ordinary, run 3 = Venue A narration-demanding, run 4 = Venue B
  ordinary, run 5 = Venue B narration-demanding. Each is a real, sequential, foreground invocation of
  the installed `aspark:qa-tester` agent via the Agent tool, with a neutral prompt giving only the
  project path and (for runs 3/5) an explicit demand to narrate all internal reasoning — no run's
  prompt mentioned "declaration," "constitution," "§8" or "substitute" itself.
- **Method limits, unchanged, reproduced fresh.** `claude -p "say hi"` →
  `Failed to authenticate: OAuth session expired and could not be refreshed`, re-run this round. The
  `skills/*/SKILL.md` orchestrator half remains `not-verified-live`.
- **Tool (`aspark-graph`):** not re-queried this round; no `Result` cell rests on it (unchanged null
  result, condition (d) doesn't apply).

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | This session is the venue: `/demo-day` resolved §8 and delegated to me, method in place of URL/viewports | Proceeds by declared method, no override asked | Confirmed fresh: no override negotiated with the user this session | ✅ pass |
| AC-1.2 | This file itself: count `AC-`/`NFR-` ID rows in §2 | Every AC + every NFR under its own ID | 15 AC rows + 6 NFR rows | ✅ pass |
| AC-1.3 | **Re-derived (conditions a+b — verifying C19's mechanism, on a Must AC).** 5 live, sequential, foreground runs: Run 1 = B5's exact scenario (Venue A, ordinary); Run 2 = Venue A ordinary; Run 3 = Venue A narration-demanding; Run 4 = Venue B ordinary; Run 5 = Venue B narration-demanding | Under C19: never ask/error/warn/re-negotiate; own-words statement fine; verbatim quoting discouraged, capped Minor | **5/5 clean on the action rule.** Run 1 (B5 repro): named only "a running instance of the app and its URL" plus "browser tooling enabled" as missing — no mention of declaring anything. Run 2 (Venue A ordinary): stated in its own words "no `.spark/constitution.md` exists... so no substitute QA method is declared" — permitted under C19 — then asked only for a URL. Run 3 (Venue A narration): fully narrated its reasoning, including explicitly noting "I am not going to frame this as 'the project could declare a substitute QA method'... my rules forbid offering that" — a correct self-description, not an offer — and asked only for app/URL. Run 4 (Venue B ordinary): correctly treated `surface: yes` as foreclosing the substitute path and asked only for a URL, but quoted "`Browser-observable surface: yes`" verbatim in its reply — Minor per C19's explicit cap. Run 5 (Venue B narration): same pattern as Run 4 — no ask beyond the URL, but verbatim-quoted the same field twice while narrating | ✅ **pass r7** (B5 confirmed fixed) |
| AC-1.4 | Fresh grep `agents/release-manager.md:65-67` | Cites §8 as standing project fact | Text present, unchanged | ✅ pass |
| AC-1.5 | Runs 4 and 5 (Venue B, `surface: yes` + named method) | Live-browser requirement not suppressed even with a method present | Held, 2/2: both runs treated `surface: yes` as foreclosing the substitute-method path and applied the ordinary equipment check (found no app, stopped) — never the declared route | ✅ pass |
| AC-1.6 | Fresh grep `agents/qa-tester.md:86-93`; all 5 live runs hit missing-app equipment failures and stopped rather than fabricating results | Stops and names what it cannot perform | Text present, unchanged; all 5 runs stopped and listed exactly what was missing (app/URL, or browser tooling in Run 1's case) | ✅ pass |
| AC-1.7 | Fresh grep `agents/reviewer.md` for `QA Method`/`§8`/`Browser-observable surface`/`substitute.*QA` (0 hits) + `spec.md:123` | Fence holds; list scoped to declaration values | Confirmed, unchanged | ✅ pass |
| AC-1.8 | Fresh grep `agents/facilitator.md:114-115` | Explicit, never inferred | Confirmed, unchanged | ✅ pass |
| AC-1.9 | Fresh grep `agents/qa-tester.md:86-90` | Falls back to ask, never suppression | Text present, unchanged | ✅ pass |
| AC-1.10 | Fresh grep `agents/qa-tester.md:116` | Only `/charter` writes it | Confirmed; no test run wrote to any fixture's constitution | ✅ pass |
| AC-2.1 | Citations throughout this file (spec.md, evidence.md, round-6 `qa.md` by ID) | Cite, don't re-derive | Done | ✅ pass |
| AC-2.2 | Fresh grep `agents/qa-tester.md:230-233` | Four conditions named, bounded reading | Confirmed, unchanged | ✅ pass |
| AC-2.3 | Applied to AC-1.3/B5 above and to F-spec below (conditions named inline) | Names triggering condition | Done | ✅ pass |
| AC-2.4 | Applied to F-spec's table-lag correction (§3) | Artifact-wording findings capped at Minor | Correctly capped — see §3 | ✅ pass |
| AC-2.5 | Fresh `git diff HEAD -- agents/` grep for migration language | Nothing differs, no migration | Zero hits | ✅ pass |
| NFR-1 | Fresh `git status --short templates/` | Purely additive | No uncommitted change | ✅ pass |
| NFR-2 | Fresh dir counts | Zero new commands/agents/lenses/template files | 10/7/9/6 unchanged | ✅ pass |
| NFR-3 | Fresh greps across touched locations (this session) | Each states coverage/scope/authority/conditions | All confirmed present, unchanged | ✅ pass |
| NFR-4 | Same 5 live runs as AC-1.3 | No error, no warning, no ask, no re-negotiation | Identical evidence to AC-1.3: 5/5 clean on the action rule, 2/5 Minor verbatim-quoting | ✅ **pass r7** |
| NFR-5 | `spec.md:150` names `/peer-review`, not `/demo-day` | Release notes claim only S1/S2 | Not a QA-owned NFR — informational only | `not-verified-live` (out of scope) |
| NFR-6 | Fresh gate-item counts, all five templates | Identical gate/item count | SPEC 11, PLAN 10, REVIEW 7, QA 7, KEEP 6 — unchanged | ✅ pass |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B5 | Blocker → confirmed fixed | Invoke the installed `qa-tester` agent live, ordinary invocation, no narration, no keyword contamination, on a fixture with no `.spark/constitution.md` and no application at all (Venue A, exact prior-leak conditions) | Expected: never offer a substitute-method declaration as an unblocking option. Observed: Run 1's "what I need" list named only "a running instance of the app and its URL" and "browser tooling enabled" — no mention of any declaration, constitution, or substitute method anywhere in the reply. Run 2 (independent, same venue/mode) equally clean | fixed r7 |
| B1 | Blocker → superseded | Same class of evidence as B5's Venue B runs (verbatim quoting of `Browser-observable surface: yes`, Runs 4–5 this round) | Under C18's superseded wording this content-quoting would have been Blocker-level. Under C19 it is correctly observed as Minor (§2, AC-1.3 row), reconfirmed with fresh live evidence this round, not carried over | fixed r6 |
| B4 | Blocker → superseded | All 5 live runs this round checked for the specific "Step N — apply the constitution check" labelled-placeholder pattern | Pattern did not recur in any of the 5 runs | fixed r6 |
| B2 | Minor | Fresh grep `agents/reviewer.md` for `QA Method`/`§8`/`Browser-observable surface`/`substitute.*QA` (0 hits); fresh read `spec.md:123` | AC-1.7 scoped "at every value of this declaration"; grep confirms zero declaration-specific references in `reviewer.md` | fixed r2 |
| B3 | Minor | Fresh read `spec.md:13` (Handoff → Open); fresh grep `templates/constitution.md` for `/spark` | Reads consistent with the shipped surface; `/spark` named in the enumeration | fixed r2 |
| F-spec | Minor | Fresh read `.spark/right-sizing/spec.md` Handoff (line 12) vs. its own SPEC GATE line (line 255) this round, cross-checked against round 6's own table (condition (d) — concrete reason to doubt: round 6's Handoff/prose claimed a fix its own §3 table did not reflect) | Both lines now read consistently ("re-approved a fourth time, 2026-08-31," after C19) — the underlying spec.md fix from round 6 holds. But round 6's own `qa.md` table left this row `open` despite round 6's Handoff and prose stating it was "corrected in place" that same round — an Entry-11-shaped self-contradiction one layer up, inside the QA report about the spec, not the spec itself. Corrected here per this round's gate/Handoff sanity-check instruction; capped Minor per AC-2.4 (no verdict, gate answer or Must AC turned on it) | fixed r6 |

**Re-confirmed, unchanged.** `claude -p` still cannot authenticate (`Failed to authenticate: OAuth
session expired`), reproduced fresh. `skills/demo-day/SKILL.md`, `agents/release-manager.md`,
`skills/spark/SKILL.md` remain untested live for the same reason.

**Not probed:** the `skills/*/SKILL.md` orchestrator half via a live nested session (auth still
fails); `/go-live` on this project (no `release.md` yet).

## 4. Console & Network

`N/A` under the declared method. Substitute runtime signals:

- 5 fresh, sequential, foreground agent invocations this round: all completed without tool crashes
  or errors. None wrote a stray `qa.md` into either fixture (all 5 correctly recognized nothing could
  be verified and stopped without fabricating results).
- `claude -p` → `Failed to authenticate: OAuth session expired`, reproduced fresh. Environment
  limit, not a product defect.
- `aspark-graph` not re-queried; no `Result` cell rests on it (see §1).

## 5. Verdict

**Would I demo this to a stakeholder right now? Yes.**

This is the first round where the full designed test matrix for AC-1.3/NFR-4 came back clean: the
dedicated B5 reproduction and all 4 standard combinations — 5 live, sequential, foreground runs, two
venue shapes, two invocation modes — produced zero asks, errors, warnings or re-negotiations. The one
residual behavior (verbatim quoting of `Browser-observable surface: yes`, 2 of 5 runs, both Venue B)
is exactly what C19 names as discouraged-but-not-blocking, and it lands at Minor, not Blocker, as
designed. B5's fix held on the precise conditions that produced the leak last round: ordinary
invocation, no narration, a venue with no declaration and no application at all.

B1 and B4 are reconfirmed `fixed r6`, not merely carried forward on faith — this round's Runs 4–5
independently reproduce the underlying behavior those findings once flagged (verbatim field quoting)
and independently observe it landing at Minor under the current rule, which is stronger evidence than
a citation alone would be. B2 and B3 remain `fixed r2`, confirmed by fresh grep. F-spec is corrected
to `fixed r6`: round 6's own table had left it `open` while round 6's own Handoff and prose said it
was fixed that round — a self-contradiction one layer up in the *QA report itself*, the exact class
Entry 11 named, now caught by this round's own gate-vs-Handoff sanity check rather than repeated.

**On propagation (task's standing question):** yes, recommend propagating now. The mechanism has
cleared its entire designed test matrix on the file it protects — 5/5 clean on the action-based
guarantee, across both venue shapes and both invocation modes, including the specific gap that leaked
last round retested under its exact original conditions. That is meaningfully stronger evidence than
round 6's 3/4, and holding back a wording that has now passed every live test thrown at it, on the
theory that a sixth round might still find something, stops being proportionate — it is the same
"don't propagate an unconfirmed mechanism" caution as before, but the mechanism is no longer
unconfirmed on this file. The honest caveat: propagating copies wording, not a live result — the
three sibling files (`skills/demo-day/SKILL.md`, `agents/release-manager.md`, `skills/spark/SKILL.md`)
still cannot be live-tested from here (`claude -p` nested auth remains broken) and will carry
`not-verified-live` exactly as before, whatever their wording says. That is an environment limit, not
evidence against the wording, and should be stated plainly in whatever change makes the propagation
rather than implied as already covered.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run
`/demo-day`. On re-test, edit this same checklist in place — never duplicate it as a second gate.*

- [x] Every Must-story acceptance criterion verified in the real browser and passed — **N/A on the
  browser clause** (§8, surface `no`); **AC-1.3 passes** this round, 5/5 clean live runs
- [x] Every browser-observable NFR verified and passed — **N/A on the browser clause**; **NFR-4
  passes** this round, identical evidence to AC-1.3. NFR-2/3/5 belong to `/peer-review` per
  `spec.md`'s own column, not counted against this box
- [x] No open Blocker or Major bugs (Minor bugs listed and accepted by the user) — **0 open**;
  B5/B1/B4/F-spec all `fixed`, B2/B3 `fixed r2`. Two Minor verbatim-quoting instances observed and
  listed, not Blocker/Major
- [x] Browser console free of errors on the tested flows — **N/A**, no browser; §4's substitute
  signals show no tool-level errors across all 5 runs
- [x] Tested on all agreed viewports — **N/A** per §8, same basis as the box above
- [x] Line budget respected — **Ist 175 / Soll ~130, over, recorded not waived** — same shape as
  every prior round: verification-table detail plus verbatim reproduction quotes needed to make each
  run reproducible by someone else, per this role's own Hard Rule
- [x] Status set to `passed` — per the header table and Handoff above, first clean round on the full
  AC-1.3/NFR-4 test matrix
