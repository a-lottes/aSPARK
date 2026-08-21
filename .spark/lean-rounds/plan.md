# Plan: lean-rounds

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/lean-rounds/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-08-20 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Two decoupled prompt-material edits — overwrite-in-place body mechanics for `review-report.md`/`qa-report.md` (US-1/2/3), and a self-reported Ist/Soll budget gate item across all five templates + a matching Hard Rule in all five owning agents (US-4). Walking skeleton is one report template proven against the live `aspark-graph` parser before the rest is touched.
- **Open:** `none` — all 8 tasks done, see §3 Task Breakdown
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** No runtime, no build, no test suite (constitution §3/§4): "implementation" is editing Markdown prompt material. The one non-human reader is `aspark-graph`'s parser (`_parse_review`/`_parse_qa`/`_normalise_result`/`queries.open_findings`), which raises `TemplateDriftError` on protected-structure drift and does an **exact** `== "open"` match. The spec's own correctness bonus (§1) is that today's append pattern hides round-2 findings *outside* the parsed section; overwrite-in-place keeps every row inside `## 3. Findings`/`## 3. Exploratory Findings` forever. Two changes ship together but are independent by concern: overwrite-mechanics (US-1/2/3, two report templates + their two owning agents + `/increment`) and the budget gate item (US-4, all five templates + all five agents).
- **Decision:** Treat the two concerns as two ordered task groups sharing four files. **Group A (mechanics):** rework `review-report.md` into the new shape *first* as the walking skeleton and validate it statically against the real parser — if the new shape drifts or breaks the `open` match, everything downstream is moot, so integration risk dies in T1. Mirror the proven pattern to `qa-report.md`, then ripple the described behavior into `reviewer.md` (re-review), `qa-tester.md` (new re-test mode), and `skills/increment/SKILL.md` (fix-mode writes bare `fixed`). **Group B (budget):** add the identical Ist/Soll checklist item to all five gates and the identical one-sentence Hard Rule to all five agents — uniform on purpose, because 3-of-5 leaves F17's failure mode reachable (spec C15). No new file, command, agent, lens or tool: purely additive edits, minor version bump.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Edit all 11 files in one coordinated task | Not verifiable in one sitting and defers the only real integration risk (parser drift) to the end; the walking-skeleton rule demands the parser check first, on one template |
  | A "resolved-findings appendix"/round-log section to keep history in-file | Explicitly out of scope (§6); relocates rows out of the first `##`-matching section, the exact defect that got the appendix cut in `lean-artifacts` — git already holds history |
  | Add a `Round`/budget linter or `plugin validate` hook to enforce the number | Constitution §3 forbids a new toolchain and §4 has no suite to hook; AC-4.2/A5 fix the bar as self-report, same honesty as every existing gate box |
  | Widen budget gate to only the three templates that had a stated budget | Reopens F17 (spec C15): the first reader who checks `qa-report.md`/`release-notes.md` learns the rule is advisory; only 5-of-5 closes the uneven-enforcement gap |
- **Consequences:** Easier — re-ruled reports carry one Scope/Verdict/gate ever, and every gate reads the same budget line; the parser sees round-2 findings it currently misses. Harder — `Status`/`Result`/`Verdict` cell vocabulary is now load-bearing (`open` exactly, `fixed` vs `fixed r<n>`), so the templates must state it and the agents must obey it; two ceremonies (`/increment` and the owner) write the same table, disambiguated only by the round suffix (spec C10).

## 2. Affected Components

Blast radius scoped **by hand** (per-file below). The `impact` query was run on the union of all 11 task `files:` paths and came back empty — `found: true`, `files: []`, `affected_stories: []`, `affected_acs: []`, with all 11 paths in `unknown_files`. Read per the tool doc's own caveat: the analysed repo declares no file links because this is a **Markdown-only repo with no source-file nodes** ("A Markdown-only or config-only project has no file nodes at all") — a **structural** empty, confirmed not a risk signal, **not** an all-clear. The list below was therefore scoped by hand, not by the tool.

- **Templates (5):** `templates/review-report.md`, `templates/qa-report.md` — full mechanics + `Round` field + budget item; `templates/spec.md`, `templates/plan.md` — budget item **only** (AC-3.5/4.5, no `Round`); `templates/release-notes.md` — budget item + new `~100` budget number.
- **Agents (5):** `agents/reviewer.md` (re-review mode + tightened budget rule), `agents/qa-tester.md` (**new** re-test mode + **new** budget rule), `agents/product-owner.md` / `agents/engineering-manager.md` (tighten existing budget rule to the checkbox), `agents/release-manager.md` (**new** budget rule).
- **Skill (1):** `skills/increment/SKILL.md` — fix-mode write-back sets `Status` to bare `fixed`, never bumps `Round`, no new heading.
- **Protected structures NOT touched (constitution §3):** `Findings` heading; `Severity`/`Location`/`Status` and `Spec ID`/`Result` columns; `^F\d+$`/`^B\d+$` IDs; header rows `Status`/`Version`. `Round` is a new, non-protected header row; cell *values* are free text. No new dependency, service or pattern.

## 3. Task Breakdown

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | **Walking skeleton.** Rework `review-report.md` body into overwrite-in-place shape: add `Round` header row (default `1`); rewrite Handoff `Binding ruling` to the fixed target "§6 Verdict and the gate checklist below"; instruct overwrite-in-place for §1 Scope/§2 Conformance/§4 Traceability/§6 Verdict with an `r<n>` suffix **only when a cell's value changed**; new `F<n>` appended to the *same* `## 3. Findings` table; state that a currently-open finding's `Status` must read exactly `open`; single REVIEW GATE, edited in place | US-1, US-2, US-3 | AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-2.1, AC-2.3, AC-2.4, AC-3.1, AC-3.2, AC-3.3, NFR-1, NFR-2 | – | `done` | Static walkthrough (documented) confirms the new-shape template parses under `_parse_review`/`_normalise_result`/`queries.open_findings` with no `TemplateDriftError`, same Feature/Finding node + `open` semantics as the old shape, and `Severity`/`Location`/`Status`/`^F\d+$` unchanged — files: templates/review-report.md |
| T2 | Mirror the proven T1 pattern to `qa-report.md`: `Round` row (default `1`); fixed `Binding ruling` target; overwrite §2 AC Verification `Result` (suffix `r<n>` only on change) and §3 Exploratory Findings (`B<n>` appended in place, `not reproducible r<n>` amendment replaces contradicted text); exact-`open` note; single QA GATE in place | US-1, US-2, US-3 | AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-2.1, AC-2.3, AC-2.4, AC-3.1, AC-3.2, AC-3.3, NFR-1, NFR-2 | T1 | `done` | Static walkthrough confirms new-shape `qa.md` parses under `_parse_qa`/`_normalise_result` with no `TemplateDriftError`, same QaCheck semantics, `Spec ID`/`Result` and `^B\d+$` unchanged — files: templates/qa-report.md |
| T3 | Add re-review mechanics to `reviewer.md`: at the start of a re-review bump `Round`; overwrite `Status` in place (`fixed r<n>`, `not reproducible r<n>`, revert to exactly `open` on regression, confirm an `/increment` `fixed`→`fixed r<n>`); append new `F<n>` to the same table; overwrite Verdict/Traceability, never a new numbered heading; state this governs what is *written*, not re-verify depth | US-1, US-2, US-3 | AC-1.1, AC-1.2, AC-1.3, AC-1.6, AC-2.1, AC-2.2, AC-2.3, AC-3.1 | T1 | `done` | `agents/reviewer.md` re-review section names each `Status` transition and the "suffix only on change / no new heading / bump Round yourself" rules verbatim against the spec's AC wording — files: agents/reviewer.md |
| T4 | Add a **new** re-test mode to `qa-tester.md` (none today): read `qa.md` Handoff bounded, bump `Round`, overwrite `Result`/`Status` in place (same vocabulary as T3), append new `B<n>` in the same table, no new numbered heading, re-verify depth left to the tester's judgment | US-1, US-2, US-3 | AC-1.1, AC-1.2, AC-1.3, AC-1.6, AC-2.1, AC-2.2, AC-2.3, AC-3.1 | T2 | `done` | `agents/qa-tester.md` carries a re-test step mirroring reviewer.md's, naming each `Status`/`Result` transition and the overwrite/no-new-heading/bump-Round rules — files: agents/qa-tester.md |
| T5 | Update `/increment` fix-mode: in the same edit that overwrites the Handoff block, set the fixed finding's `Status` to exactly `fixed` (no round number — never owns/guesses the round), never bump `Round`, create no new section or "Fixes applied" heading | US-1 | AC-1.5 | T1, T2 | `done` | `skills/increment/SKILL.md` step 5 states the bare-`fixed` write-back, the no-`Round`-bump rule and the no-new-heading rule explicitly — files: skills/increment/SKILL.md |
| T6 | Add the identical Ist/Soll budget gate item ("Line budget respected: Ist N / Soll ~X", excluding HTML comments) to all five gate checklists; add the missing budget numbers `qa-report.md ~130` and `release-notes.md ~100`; `spec.md`/`plan.md` get the item **only** (no `Round`, no mechanics) | US-4 | AC-4.1, AC-4.2, AC-4.3, AC-4.5, AC-3.5, NFR-3 | T1, T2 | `done` | Each of the five templates carries one budget checkbox with the Ist/Soll form and its stated Soll (~250/~300/~150/~130/~100); `spec.md`/`plan.md` gained nothing else — files: templates/spec.md, templates/plan.md, templates/review-report.md, templates/qa-report.md, templates/release-notes.md |
| T7 | Add/tighten the one-sentence "respect and report the line budget at the gate checkbox" Hard Rule in all five owning agents: tighten the existing prose in `product-owner.md`/`engineering-manager.md`/`reviewer.md` to point at the new checkbox; add the identical rule to `qa-tester.md` and `release-manager.md`, which carry none today | US-4 | AC-4.2, AC-4.4, NFR-3 | T6 | `done` | All five agents carry the identical budget Hard Rule pointing at the new gate checkbox; the two that had none now do — files: agents/product-owner.md, agents/engineering-manager.md, agents/reviewer.md, agents/qa-tester.md, agents/release-manager.md |
| T8 | **Dogfood + negative case.** Document a dry run reading the old-shape `.spark/graph-gates/review.md`/`qa.md` (no `Round` row, full accretion) confirming no ceremony behavior differs, no migration, no error; capture this feature's own `/peer-review` round showing round-suffixed cell edits only (no `## Round N`, no duplicate gate) and every touched gate carrying a correct Ist/Soll line. No token-count claim | US-1, US-2, US-3, US-4 | AC-1.7, AC-3.4, AC-2.5, NFR-4, NFR-5 | T1, T2, T3, T4, T5, T6, T7 | `done` | A written record shows (a) old-shape artifacts read unchanged (round-1 default, no error) and (b) a bounded-growth transcript of this feature's own re-review, both filed as the dogfood evidence |

## 4. Test Strategy

No automated tests exist or are possible for prompt material (constitution §4). "Verification" = the two evidence methods `lean-artifacts` already used, negative case first (§1 constitution principle):

- **Static parser walkthrough (per-Must, T1/T2).** Read the new-shape template against `~/aSPARK-graph/src/aspark_graph/artifacts.py` (`_parse_review` 276–290, `_parse_qa`, `_normalise_result`) and `queries.py:302` (`open_findings` exact `== "open"`). Passing = no `TemplateDriftError`, protected columns/IDs intact, and every load-bearing cell value (`open`, and suffixed `Result`/`Verdict` cells) still normalizes as before. This is the walking skeleton's kill-criterion — it runs on T1's one template before any other file is touched. Covers US-1/2/3, AC-2.5, NFR-1/NFR-2.
- **Dogfood transcript (T8).** This feature's own Specify→Plan→Review→(fix)→re-Review loop is the live proof of bounded growth (US-1/2/3, NFR-4) and of five correctly self-reported Ist/Soll lines (US-4). No token/byte saving is claimed (NFR-4, same bar as `lean-artifacts`).
- **Backward-compat dry run (T8, negative case, runs first).** Read the two existing round-accreted `.spark/graph-gates/` artifacts after the change and confirm nothing differs — this is the constitution's "in a repo where the capability is absent, nothing may change" applied to old-shape files (AC-1.7, AC-3.4, NFR-5).
- **`claude plugin validate`** must pass (constitution §4 baseline) after every edited file.
- Deliberately **not** covered by automation: everything — there is no suite. That is the constraint, not a gap; the two methods above are the whole evidentiary bar.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| A round-suffixed `Result`/`Verdict` cell (`❌ fail r3`, `✅ met r2`) fails `_normalise_result`, silently changing QaCheck/verdict semantics | The parser (the one non-human reader) drifts — the exact class of bug the spec exists to avoid | T1/T2 static walkthrough re-confirms `_normalise_result` tolerates the suffix against the live parser before ship; it is the walking-skeleton kill-criterion, not an afterthought. Spec AC-2.5 claims this was verified (C7/C9) — T1 re-proves it, doesn't assume it |
| Agent forgets the exact `open` reversion and writes `reopened r<n>` | `open_findings` (exact match) silently drops the finding — the F17-class credibility failure | Template states the exact-`open` rule inline (T1/T2, NFR-2); reviewer/qa-tester Hard-Rule it (T3/T4); out-of-scope §6 bans inventing new vocabulary |
| Self-reported budget box checked while over budget (A5) | Gate honesty erodes, same as any unchecked gate box | Accepted risk per spec A5/AC-4.2 — identical to every existing gate; no new enforcement is in scope (constitution §3/§4) |
| `/increment` and the owner race to bump `Round` or both suffix a cell | Ambiguous round state in the file | Design fix (spec C10, enforced in T5): `/increment` writes bare `fixed` and never touches `Round`; only the owner bumps it and only the owner writes `r<n>` |
| Increment (11 files, 8 tasks) too large to review in one `/peer-review` pass | Reviewer can't hold it | Group B (T6/T7) is mechanical and uniform; Group A splits cleanly by file. If review strains, split at the A/B seam — but the change is additive-only and the two groups share just four files |

## Deviations

<!-- Small, obvious corrections made during fix-mode, recorded per the /increment SKILL's rule
     rather than looped back through /sprint-plan — none change architecture, scope or stories. -->

- **2026-08-20, `/peer-review` round 1 fix-mode (F1):** `skills/demo-day/SKILL.md` step 2 gained
  one sentence pointing the QA Tester at the previous `qa.md` on a re-test, mirroring
  `/peer-review`'s existing equivalent for the Reviewer. This is a 12th file, outside T4's declared
  `files:` note (`agents/qa-tester.md` only) — without it, T4's re-test mode as built is never
  actually triggered by the one ceremony that would invoke it, so the omission was a real gap in
  the original blast-radius scoping (§2), not a scope change now.
- **2026-08-20, `/peer-review` round 1 fix-mode (F5):** `.spark/lean-rounds/spec.md` AC-2.5 amended
  from an absolute "raises no `TemplateDriftError`" to "raises no *new* `TemplateDriftError`",
  naming the pre-existing `_parse_qa`/`Spec ID` defect explicitly (logged as spec §7 C19). Wording
  correction only, grounded in evidence already gathered (evidence.md Entry 2) and independently
  re-verified live by the Reviewer — no architecture, scope or story changed.

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded)
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Status set to `approved` by the user — given explicitly 2026-08-20, after the PLAN GATE walk
