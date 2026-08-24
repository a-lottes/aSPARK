# Spec: lean-rounds

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-20 |
| **Ticket** | `none` (constitution §7) |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Round-2/3 report sections currently *append* a near-duplicate of the whole report instead of overwriting the original tables — this feature replaces that with overwrite-in-place for `review.md`/`qa.md`, and gives all **five** templates (`spec.md`, `plan.md`, `review-report.md`, `qa-report.md`, `release-notes.md`) a binding, self-reported line-budget gate item.
- **Open:** `none` — C15's Must-bump for US-4 confirmed by the user 2026-08-20
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed since the last round and why
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** `lean-artifacts` gave every report a fixed-address Handoff block, but
  the *body* still accretes: a re-review or re-test doesn't update the original
  tables, it appends a whole new "Round N" section that restates Scope, Plan
  Conformance, the Traceability table (every row, not just the changed ones) and
  the Verdict, plus a separate "Fixes applied" heading. Measured: `.spark/graph-gates/review.md`
  is 695 lines, 71% (lines 202–695) round-2/3 narrative; `qa.md` is 625 lines,
  ~53% round-2 accretion. `templates/review-report.md` states a ~150-line budget
  in a comment that enforces nothing; `spec.md`/`plan.md` do the same (~250/~300);
  `qa-report.md` and `release-notes.md` state no budget at all — and even where a
  budget is stated, nothing checks it, a gap this repo's own history already
  flagged as a credibility risk (`.spark/graph-gates/review.md` finding **F17**:
  uneven, unenforced budget coverage teaches the first reader who checks that the
  rule is advisory). **A concrete correctness bonus, not just a size problem:**
  verified against `~/aSPARK-graph/src/aspark_graph/artifacts.py:276–290`,
  `_parse_review`'s Findings table is the *first* table under the *first*
  `##`-level heading containing "findings" — i.e. only `## 3. Findings`. Round-2
  findings (`review.md`'s `F10`–`F17`) live under `### 7.4 Findings (round 2)`,
  physically *after* `## 6. Verdict`, outside that section entirely — the
  consumer's graph never sees them. The append pattern doesn't just cost tokens;
  it silently hides findings from the one real reader that isn't human.
- **Goal:** Round-2+ writes to `review.md`/`qa.md` update the *same* Findings,
  Traceability/AC-Verification and narrative sections in place — one current
  state per row, one Scope, one Verdict, one gate checklist, ever. History lives
  in git, not in the file. All **five** templates — `spec.md`, `plan.md`,
  `review-report.md`, `qa-report.md`, `release-notes.md` — get a stated line
  budget and a self-reported gate item comparing actual (Ist) to budget (Soll),
  closing the uneven-enforcement gap named above rather than narrowing it to
  three templates and reopening the same risk.
- **Success signal:** A dogfood transcript of this very feature's own
  `/story-time` → `/sprint-plan` → `/peer-review` → (if a finding needs fixing)
  `/increment` fix-mode → re-`/peer-review` shows `review.md` growing by
  round-suffixed cell edits only — no `## Round N` heading, no duplicate gate
  checklist, no restated table — across however many rounds it actually takes,
  and shows every one of this feature's own five touched artifacts carrying a
  correctly self-reported Ist/Soll line. No token-count claim is made (NFR-4,
  same honesty bar as `lean-artifacts` NFR-4).
- **Why now:** This is the feature `lean-artifacts` §6 named and deliberately cut
  as "the *actual* driver behind 695 lines … bigger win, separate feature;
  propose it at the next `/next-steps`." It is that proposal, run through the
  same interrogation, widened once during that interrogation (§7 C14–C17) when
  the budget half of the idea turned out to touch the whole template set, not
  half of it.

## 2. Target Users

- The **Reviewer** agent (`agents/reviewer.md`), re-review mode — owns
  `review.md`, writes every round.
- The **QA Tester** agent (`agents/qa-tester.md`), re-test mode — owns `qa.md`,
  writes every round. (Today this agent has *no* documented re-test/bounded-read
  step at all, unlike the Reviewer's — this feature adds one, generalizing the
  same precedent one level deeper for both owners.)
- **`/increment` in fix-mode** (`skills/increment/SKILL.md`) — not the owner of
  either report, but writes back into both when it applies a fix.
- The **Product Owner**, **Engineering Manager** and **Release Manager** agents
  — each now records its own artifact's Ist/Soll line at its own gate
  (SPEC GATE / PLAN GATE / KEEP GATE) as part of US-4's widened scope.
- Downstream readers unaffected in *how* they read (`lean-artifacts` already
  bounded that) but who benefit from a body that stays small when they do read
  it by exception: `release-manager`, `product-owner` (`/next-steps`), the human
  maintainer.
- **`aspark_graph.artifacts`** — the one non-human consumer; its exact parsing
  behavior (verified directly, not assumed) is what several rulings below are
  grounded in.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A5 | The budget check is a self-report by the writing agent, not a linter — constitution §3 rules out a new toolchain and §4 has no test suite to hook into (same constraint `lean-artifacts` NFR-4/A2 already accepted for its own claims). Nothing stops an agent checking the box while over budget. | **Accepted risk**, same shape as `lean-artifacts` A2 — the gate item is only as honest as the agent filling it in, exactly like every other REVIEW/QA/SPEC/PLAN/KEEP GATE checkbox already is |
| A6 | §2's consumer list was cross-checked against all five owning agents' files directly (`product-owner.md`, `engineering-manager.md`, `reviewer.md`, `qa-tester.md`, `release-manager.md`), not just the three the user originally named. | Verified 2026-08-20 (§7 C17) |
| A7 | C15's Must-bump for US-4 is a PO ruling made under delegated authority ("your call, but flag it") — it reverses the user's earlier confirmation of **Should** (C11) on the strength of new information (the widened, all-five-template footprint and the F17 precedent). | **Confirmed by the user 2026-08-20.** US-4 is Must — see §7 C15/C18 |

## 4. User Stories

### US-1 (Must): Findings tables are overwritten in place, not accreted

> As the Reviewer or QA Tester re-checking a previous round, I want the
> Findings / Exploratory Findings table to hold exactly one row per issue,
> updated where its state changed, so that the report never grows a second
> copy of the same table.

**Acceptance criteria:**

- [ ] AC-1.1: Given a finding an `/increment` fix-mode pass or a later round
  confirms fixed, when that confirmation happens, then the existing row's
  `Status` cell is overwritten in place to `fixed r<n>` (n = the confirming
  round) — no new row, no new heading, no restated table.
- [ ] AC-1.2: Given a finding a later round finds was never actually a problem,
  when that's discovered, then its `Status` cell becomes `not reproducible r<n>`
  and the Finding/Steps cell gets at most a one-line amendment explaining why —
  never a second row for the same issue, and the amendment replaces, not
  appends to, any part of the cell it directly contradicts.
- [ ] AC-1.3: Given a finding closed in one round and broken again in a later
  one, when that's discovered, then its `Status` cell reverts to exactly `open`
  — never a new word such as `reopened` — because `aspark_graph`'s
  `open_findings` query (`queries.py:302`) does an **exact**, case-insensitive
  match on the literal string `open`; any other value silently drops the
  finding from that answer.
- [ ] AC-1.4: Given a round discovers a genuinely new issue, when it's logged,
  then it gets the next unused `F<n>`/`B<n>` ID, appended as a new row at the
  bottom of the *same* table (`## 3. Findings` / `## 3. Exploratory Findings`)
  — never under a new heading — so it stays inside the section
  `aspark_graph`'s `_section`/`_first_table` actually reads.
- [ ] AC-1.5: Given `/increment` fix-mode applies a code fix
  (`skills/increment/SKILL.md` step 5), when it writes back, then it sets that
  finding's `Status` cell to exactly `fixed` (no round number — `/increment`
  never owns or guesses the round) in the same edit that overwrites the
  Handoff block; it creates no new section and no "Fixes applied" heading.
- [ ] AC-1.6: Given the owning agent's next re-review/re-test pass confirms an
  `/increment`-applied fix, then it overwrites that cell from `fixed` to
  `fixed r<n>` — the round-numbered form always means "the owner confirmed
  this", the bare word always means "the fixer claims this, unconfirmed".
- [ ] AC-1.7: Given `.spark/graph-gates/review.md`/`qa.md`, already in the old
  round-accreted shape, when any ceremony reads them after this feature ships,
  then nothing about the ceremony's behavior differs from today — no
  migration, no rewrite, no error.

### US-2 (Must): One current state per traceability row; no per-round narrative sections

> As a reader of a re-ruled report, I want Scope, Plan Conformance, the
> Traceability/AC-Verification table and the Verdict to each show the current
> round's answer in one place, so that I never have to find "which section is
> actually binding."

**Acceptance criteria:**

- [ ] AC-2.1: Given `review-report.md` §4 Requirements Traceability or
  `qa-report.md` §2 AC Verification, when a later round re-evaluates a row,
  then that row's `Verdict`/`Result` cell is overwritten in place; a round
  suffix (`r<n>`) is appended to the cell **only** when the value changed since
  the previous round — an unchanged cell is left exactly as it was, untouched.
- [ ] AC-2.2: This feature governs what gets **written**, never how much the
  Reviewer/QA Tester chooses to **re-verify** — that stays their judgment,
  unconstrained, per their existing Hunt/exploratory instructions. A row not
  re-examined this round is simply not touched; this is not a narrowing of
  review or test depth.
- [ ] AC-2.3: Given `review-report.md` §1 Scope, §2 Plan Conformance and §6
  Verdict (or `qa-report.md`'s Test Environment / Console & Network / Verdict),
  when a later round changes the binding content, then the existing section is
  overwritten in place to state the current round's content — no `## Round 2`,
  `### 7.x`, or any similarly numbered new heading is created in the body.
- [ ] AC-2.4: Given the header table's new `Round` field (US-3) and the Handoff
  block, when a reader reads only those, then it needs no other section to know
  which round is current — because under this feature there is exactly one
  Scope, one Verdict and one gate checklist in the file, always.
- [ ] AC-2.5: Given a review/QA report in this new shape, when
  `aspark_graph.artifacts` parses it, then it raises no *new* `TemplateDriftError`
  and yields the same Feature/Finding/QaCheck node and status semantics as the
  same content in the old accreted shape — verified statically against
  `_parse_review`, `_parse_qa`, `_normalise_result` and `queries.py`'s
  `open_findings` (2026-08-19; see §7 C7/C9), same fallback method
  `lean-artifacts` C9 used when a live run of the sibling repo isn't the
  cheapest proof. The pre-existing `Spec ID`/`AC`-column defect in `_parse_qa`
  (§7 C19) is unchanged by this feature — it fires identically on the old and
  new shape, so "no new drift" is the exact claim, not "no drift at all".

### US-3 (Must): A single gate and a visible round counter

> As anyone opening a review/QA report mid-loop, I want one gate checklist and
> a one-line answer to "what round is this", so that "which section wins" is
> never a question I have to ask.

**Acceptance criteria:**

- [ ] AC-3.1: Given `templates/review-report.md`/`qa-report.md`, when
  instantiated, then the header table carries a new `Round` row (default `1`),
  bumped only by the report's owner (Reviewer / QA Tester) at the start of a
  re-review/re-test pass — never by `/increment`.
- [ ] AC-3.2: Given the REVIEW GATE / QA GATE checklist at the bottom, when a
  later round re-rules it, then the same checklist is edited in place (boxes
  and the status line updated) — never duplicated as a second
  `## ✅ REVIEW GATE (binding)`-style heading.
- [ ] AC-3.3: Given the Handoff block's `Binding ruling` line, when the
  template is read, then it names a fixed target — "§6 Verdict and the gate
  checklist below" — never "the latest round", because under this feature
  there is no other round to point to.
- [ ] AC-3.4: Given a report written before this change (no `Round` row), when
  any ceremony reads it, then it's treated as round 1 by default — no error,
  no migration prompt.
- [ ] AC-3.5: `spec.md` and `plan.md` get **no** `Round` field and none of
  US-1–3's overwrite-mechanics changes — see §7 C16: their existing
  Clarifications/Deviations tables already grow by appending indexed rows, not
  by duplicating a whole prior section, so this problem doesn't exist there.

### US-4 (Must): Line budgets become a self-reported, binding gate item — all five templates

> As the writer of any of the five spec/plan/report templates, I want its
> stated line budget checked at the gate exactly like every other DoD item, so
> that "some templates enforce it, some don't" stops being something a reader
> can find true.

**Acceptance criteria:**

- [ ] AC-4.1: Given all five templates — `spec.md` (~250), `plan.md` (~300),
  `review-report.md` (~150), `qa-report.md` (new: ~130), `release-notes.md`
  (new: ~100) — when its gate checklist (SPEC GATE / PLAN GATE / REVIEW GATE /
  QA GATE / KEEP GATE) is completed, then it carries the same new item
  recording actual rendered lines, excluding HTML comments (same counting
  method as `lean-artifacts` AC-3.3), against the stated budget — e.g. "Line
  budget respected: Ist 142 / Soll ~150".
- [ ] AC-4.2: Given an overage, when the writing agent reaches the gate, then
  it either leaves the item unchecked with the overage and a reason recorded,
  or the user explicitly waives it with a reason recorded inline — the same
  treatment as an unwaived Major finding elsewhere on the same gate. No linter,
  hook or new tool enforces the number (constitution §3/§4 rule that out); the
  bar is the same self-reported honesty every other gate box already carries.
- [ ] AC-4.3: Given `qa-report.md` and `release-notes.md` had no stated budget
  before this feature, then each gets one grounded in its own section count:
  `qa-report.md` has 5 numbered sections against `review-report.md`'s 6 at
  ~150 (~25 lines/section); scaled up slightly for its prose-heavier
  Steps/Expected/Observed columns → **~130**. `release-notes.md` has 4 lighter,
  checklist-and-short-bullet sections → **~100**.
- [ ] AC-4.4: Given the five owning agents, when each finishes its own gate,
  then it records the Ist/Soll line itself, per agent: `product-owner.md` and
  `engineering-manager.md` already carry a "respect the line budget" Hard
  Rule — tightened to point at the new checkbox instead of standing as
  unchecked prose; `reviewer.md` already has the equivalent; `qa-tester.md` and
  `release-manager.md` have **no** budget-related Hard Rule today and each gain
  the identical one-sentence rule the other three already carry.
- [ ] AC-4.5: `spec.md`'s SPEC GATE and `plan.md`'s PLAN GATE gain the Ist/Soll
  item exactly as the other three gates do (AC-4.1) — this is the *only*
  change either template gets from this feature; neither gets a `Round` field
  or any other change from US-1–3 (AC-3.5).

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Compatibility & versioning (library lens §2) | Purely additive: no protected heading, column or ID pattern (constitution §3) renamed or removed; the `Round` row is a new, non-protected header-table field; `Status`/`Result` cell *values* are free text already, unconstrained by the protected contract, and AC-1.3/AC-2.5 pin the one value (`open`) that is load-bearing for the consumer. Minor version bump, no coordinated release with `aspark-graph` needed. | `/peer-review` + the static walkthrough already performed in this spec (§7 C7/C9) |
| NFR-2 | Contract clarity (library lens §4) | Each of `review-report.md`/`qa-report.md` states, in the template itself, that `Status` must read exactly `open` (never a synonym) for a currently-open finding, so a future editor doesn't invent new vocabulary that silently breaks `aspark_graph`'s exact-match check. | `/peer-review` |
| NFR-3 | Public surface (library lens §1) | Zero new commands, agents, lenses or template files. Added surface, enumerated in the release notes: one `Round` header-table row in two templates; one new gate-checklist budget item in **all five** templates; one new budget number in two templates (`qa-report.md`, `release-notes.md`); one Hard-Rules sentence in each of the **five** owning agents, two of which (`qa-tester.md`, `release-manager.md`) gain a budget-awareness rule they carry none of today. | `/peer-review` |
| NFR-4 | Agent attention / honesty (constitution §4) | No measured token or byte saving is claimed — only a structural guarantee (no forced full-table restatement) and a dogfood transcript showing bounded growth across this feature's own review rounds, however many it takes, plus every one of the five touched gates carrying a correctly self-reported Ist/Soll line. Same bar as `lean-artifacts` NFR-4. | `/peer-review` + dogfood transcript |
| NFR-5 | Reliability / degrade-to-silence (constitution §6) | Old-shape artifacts (no `Round` row, full round-accretion) keep working exactly as today (AC-1.7, AC-3.4); no gate ever blocks on the `Round` field's presence. | `/peer-review` + dry run against `.spark/graph-gates/` |

Not applicable, each with its reason: **Performance / Accessibility** — no
runtime, no UI (constitution §4). **Security** — lens off; no runtime, no data.
**Roles & permissions** — Markdown in a git repo, no authz surface. **Library
lens §3 (packaging/footprint)** — no bundle, no dependencies (constitution §2).
**UX flows & states** — no UI; the analogue (what a reader sees at each round)
is covered by AC-2.3/AC-2.4.

## 6. Out of Scope

- **Reopening the resolved-findings appendix**, cut by `lean-artifacts` §6.
  Confirmed architecturally different from this feature and does not share its
  parsing risk: the appendix idea *relocated* rows out of the Findings table
  into a new section, which `_parse_review`'s "first table under the first
  matching `##` heading" rule would silently drop. Overwrite-in-place never
  relocates a row — it stays in `## 3. Findings` / `## 3. Exploratory Findings`
  forever, only its cells change — so it cannot trigger that defect.
- **Migrating `.spark/graph-gates/review.md`/`qa.md`** or any other existing
  round-accreted artifact to the new shape. AC-1.7/AC-3.4 are the safeguards
  that make this safe to skip.
- **Any linter, validator or hook enforcing the line budget.** Constitution §3
  forbids a new toolchain, §4 has no test suite; AC-4.2 is explicit that this
  is a self-report, same honesty bar as every existing gate box.
- **A `Round` field, or any US-1–3 overwrite-mechanics change, for `spec.md` or
  `plan.md`.** §7 C16: those two templates' existing per-round growth
  (Clarifications, Deviations, Review Findings Carried) is already
  append-indexed, not whole-section duplication — nothing to fix there beyond
  the budget checkbox (AC-3.5, AC-4.5).
- **Inventing additional Status/Result vocabulary** beyond `open`, `fixed r<n>`,
  `not reproducible r<n>` and the user's own waiver — a wider taxonomy is a
  separate, smaller idea if it turns out to be needed.
- **A template version marker/handshake** — same reasoning `lean-artifacts` §6
  gave: its own cross-repo negotiation, not a rider here.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-19 | Exact overwrite mechanics for the Findings/Exploratory Findings tables — is a fixed finding's row edited in place, or is there still some per-round record? | **Overwritten in place, zero per-round record in the file** (PO ruling). The `Status` cell is the only thing that changes; git log is the only history — matching the idea's own framing verbatim. AC-1.1–1.6 |
| C2 | 2026-08-19 | Is this a new mechanism, or the existing Handoff-block precedent (`lean-artifacts` C8/C11) applied one level deeper? | **The same precedent, generalized** (PO ruling). `lean-artifacts` already established "index above, record below" for the Handoff block; this feature applies "overwrite, not append" to the body tables it always deferred to (§3 Findings, §2/§4 verification) instead of inventing a new rule |
| C3 | 2026-08-19 | Does overwriting body tables conflict with this repo's general "kept unedited as the record" norm for artifact bodies? | **No, same ruling as `lean-artifacts` C11, applied one level deeper** (PO ruling). The norm governs prose that *is* the record (e.g. a Finding's original description); it does not extend to the `Status`/`Result`/`Verdict` cells, which — like the Handoff block — are live state, not history. AC-1.2's one-line amendment is the single, narrow exception where description text may change, and only to correct a now-disproven claim |
| C4 | 2026-08-19 | Is exceeding a line budget a hard gate block, or recorded-and-accepted? | **Self-reported gate item, same treatment as an unwaived Major finding** (PO ruling). Constitution §3/§4 rule out any new enforcement tooling; AC-4.1/4.2 |
| C5 | 2026-08-19 | What budgets should `qa-report.md` and `release-notes.md` (currently none) get? | **~130 and ~100 lines respectively**, grounded in each template's own section count scaled from `review-report.md`'s established ~25-lines/section rate (AC-4.3) — not invented numbers. Confirmed by the user 2026-08-20 (C12) |
| C6 | 2026-08-19 | Migrate the two already-bloated `.spark/graph-gates/` artifacts? | **No** (PO ruling, matching `lean-artifacts` AC-1.5's precedent). AC-1.7/AC-3.4 are the safeguards |
| C7 | 2026-08-19 | Does overwrite-in-place share the appendix idea's `_parse_review` "first table only" risk that got the appendix cut in `lean-artifacts`? | **No — verified, not assumed** (PO ruling). Read `~/aSPARK-graph/src/aspark_graph/artifacts.py:276–315` directly: `_section` takes the first `##`-heading block matching "findings"/"acceptance criteria verification" and `_first_table` takes its first table. The appendix idea moved rows *out* of that block (drop risk); overwrite-in-place never moves a row — new rows append to the *same* table, inside the *same* section, forever. Architecturally immune to the defect that killed the appendix idea |
| C8 | 2026-08-19 | What proves the feature worked, given no measurable token count is available? | **A dogfood transcript**, same evidentiary bar as `lean-artifacts` NFR-4 — bounded growth across this feature's own review rounds is the proof, not a token-count claim this project can't actually measure |
| C9 | 2026-08-19 | Does a reopened finding get a new status word like `reopened rN`? | **No — must revert to the exact word `open`** (PO ruling, grounded not assumed). Read `~/aSPARK-graph/src/aspark_graph/queries.py:298–306` directly: `gate_health`'s `open_findings` does `(node.get("status") or "").lower() == "open"` — **exact** equality, not a substring match. Any other word, including a plausible-looking one like `reopened r3`, silently drops the finding from that answer. AC-1.3, NFR-1/NFR-2. Confirmed by the user 2026-08-20 (C13) |
| C10 | 2026-08-19 | Who owns bumping the new `Round` field — the owner (Reviewer/QA Tester) or `/increment`, which also writes to the report? | **The owner only, at the start of its own re-review/re-test pass** (PO ruling). `/increment` writes a fix's `Status` as plain `fixed` (no round number) and never touches `Round` — avoids two ceremonies racing to bump the same counter, and keeps the round-suffixed form meaning "the owner confirmed this" unambiguously. AC-1.5/1.6, AC-3.1 |
| C11 | 2026-08-20 | A1: MoSCoW priority for the (then 3-template) budget-gate story? | User confirmed **Should**, matching the PO's original recommendation — later superseded by C15 once the footprint widened (A4) |
| C12 | 2026-08-20 | A2: are the proposed budgets (`qa-report.md` ~130, `release-notes.md` ~100) accepted? | **Accepted as proposed**, confirmed by the user |
| C13 | 2026-08-20 | A3: must a reopened finding's `Status` read exactly `open`? | **Confirmed** by the user — the exact-match ruling (grounded in `queries.py:302`) stands as specified in C9 |
| C14 | 2026-08-20 | A4: extend the binding-budget gate item to `spec.md`/`plan.md` now, or keep it deferred to a follow-up? | **Extended now, by the user.** US-4 widened from 3 to all 5 templates; §6's earlier "deferred, propose separately" bullet is removed as superseded |
| C15 | 2026-08-20 | Given C14's widened footprint, does US-4's priority change from Should back to Must? | **PO ruling: yes, bumped to Must.** Grounded in `.spark/graph-gates/review.md`'s own round-2 finding **F17** (verified directly, `review.md:297`): uneven, unenforced budget coverage was already named in this repo's own history as a credibility risk — "the first reader who checks the new rule against the repo's own newest artifacts learns it is advisory." At 3-of-5 templates that exact failure mode stayed reachable; only 5-of-5 actually closes it. **Flagged explicitly for the user's confirmation** at spec approval — this reverses C11's answer on new information, not silently (A7) |
| C16 | 2026-08-20 | Does extending to `spec.md`/`plan.md` bring the same "Round N" accretion problem US-1–3 fix for `review.md`/`qa.md`? | **No** (PO ruling, re-run Clarify pass). `spec.md`'s Clarifications table and `plan.md`'s Deviations/Review-Findings-Carried tables already grow by **appending indexed rows**, never by duplicating a whole prior section — exactly the pattern US-1/US-2 are introducing for `review.md`/`qa.md`. For `spec.md`/`plan.md` this feature is therefore **budget-gate-checkbox only** (AC-3.5, AC-4.5); no `Round` field and no overwrite-mechanics work applies to them |
| C17 | 2026-08-20 | Who fills in the new checkbox on `spec.md`/`plan.md`/`release-notes.md`'s gates, given `qa-tester.md` and `release-manager.md` carry no budget-awareness instruction today? | **PO ruling** (re-run Clarify pass, verified directly against all five agent files, `agents/{product-owner,engineering-manager,reviewer,qa-tester,release-manager}.md`): `product-owner.md`, `engineering-manager.md` and `reviewer.md` already carry a "respect the line budget" Hard Rule, each tightened to point at the new checkbox; `qa-tester.md` and `release-manager.md` have none today and each gain the identical one-sentence rule (AC-4.4) |
| C18 | 2026-08-20 | A7: final call on the PO's Should→Must bump for US-4? | **Must, confirmed by the user.** A7 closed; spec has no open items |
| C19 | 2026-08-20 | `/peer-review` (F5) found AC-2.5's "raises no `TemplateDriftError`" false as an absolute claim — `_parse_qa` raises on `qa-report.md`'s `Spec ID` column not matching its own hard-required `AC` column, for the unmodified template exactly as much as the new-shape one (evidence.md Entry 2, independently re-verified live by the Reviewer). Amend the wording, or leave as a known gap? Round 2 of `/peer-review` filed F10 (Major): the wording change was made unilaterally by the developer during fix-mode, on a spec whose `Status` is `approved` — an authority overstep, even though the content was independently re-verified correct twice. | **Amended, and the amendment explicitly ratified by the user 2026-08-20** (F10's resolution, `.spark/lean-rounds/review.md`). AC-2.5 claims "no *new* drift" and names the pre-existing defect explicitly, matching what was actually verified live in two independent Reviewer passes. The defect itself stays out of scope, same reasoning as `lean-artifacts` §6. The process gap F10 raised is accepted as a one-off, corrected here by the user's direct ruling rather than by reverting and re-running `/story-time` |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **Overall impression:**
- **Heuristics findings:** (visibility of status, consistency, error prevention, recognition over recall, …)
- **Accessibility notes:** (contrast, keyboard navigation, focus order, labels)
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C19 resolved; A5–A7 named and routed
- [x] Open questions are resolved or explicitly accepted as risk — A5 accepted as risk, A6 verified, A7 (C15's Must-bump) confirmed by the user (C18)
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected — no protected structure touched; verified directly against the live `aspark-graph` parser, not assumed
- [x] Design review — **N/A**: this repo ships no UI of any kind (constitution §2)
- [x] Status set to `approved` by the user — given explicitly 2026-08-20, after walking the SPEC GATE together
