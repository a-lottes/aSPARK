# Plan: tracker-handoff

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/tracker-handoff/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-08-06 |

## 1. Architecture Decision

- **Context.** Prompt-material change to aSPARK Core (Markdown + JSON, no runtime, no
  tests — constitution §3). The Keep phase hard-codes `released` as the only terminal
  status, in a template (`release-notes.md:8`) and in two state-machine readers
  (`spark/SKILL.md:50–51`, `next-steps/SKILL.md:35–36,73`). We must add a second honest
  terminal status (`handed-off`) for PR-mode delivery, a once-declared delivery mode in
  the constitution, and a single home for a ticket reference — while a project that
  declares nothing behaves bit-for-bit as today (US-1, the dominant risk). The template
  contract to `aspark-graph` is verified safe for a new enum value (spec A3/C1): the
  consumer regex-extracts the `Status` cell with no enum validation and never compares
  against the literal `released`.
- **Decision.** Purely **additive, declaration-driven, single-gate** design. (1) Add
  `handed-off` to the existing `Status` enum — no row renamed or reordered (NFR-1).
  (2) The delivery mode is a **standing constitution fact** in a new `Delivery & Handoff`
  section, read by `go-live`/`release-manager`; every field defaults to today's behavior
  when absent, so an undeclared project never sees a prompt or a new string (AC-3.5,
  NFR-5). (3) **One** KEEP GATE, not two: handoff mode is expressed as inline
  mode-annotations on the existing five boxes plus mode-specific `Release Actions` values
  (deploy/smoke → N/A with the mode named, Version → *proposed*, no tag before merge),
  keeping the gate ≤10 boxes (NFR-8). (4) The `Ticket` row lives only in `spec.md`; the
  `release-manager` changelog rule (`:88`) is scoped so it stops stripping the reference.
  The seventh constitution section is named in `facilitator.md:59` so `/charter` actively
  grounds it (see below).
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Two parallel KEEP-GATE checklists (direct vs handoff) | Doubles the gate and invites picking the easier list (R2); risks NFR-8's ≤10-box ceiling and the "gate nobody finishes reading" failure. Inline annotations on one list keep the diff additive and the gate short. |
  | Mode chosen by the agent at release time (infer from remote/branch-protection) | Violates AC-3.2/AC-2.7 — the agent must never infer a mode. A standing constitution fact removes the guess and the R2 softening. |
  | New `Delivery & Handoff` as a subsection of an existing constitution section | AC-3.1/AC-3.4 treat it as a distinct section amended in isolation; nesting it muddies the "only that section added" diff and the facilitator's section-by-section drafting. |
  | Leave `facilitator.md:59` untouched (rely on template structure) | Its six-name enumeration reads as a closed list; an agent following it literally would leave the seventh section as placeholder text, breaking AC-3.3. One added name is cheap insurance. |
  | A fifth "approved/merged" enum value | Out of scope (§6) — nothing in the loop observes it; a status nobody writes is dead weight. |
- **Consequences.** *Easier:* a corporate team closes the loop honestly; the ticket has
  one home; the negative case is provably unchanged (grep for zero `handed-off`).
  *Harder:* two terminal statuses are now a contract any future board must special-case
  (R6, recorded); self-attestation may become the common path for AC-2.2's PR/CI facts
  (R9, watched at `/peer-review`); this feature's *positive-case* QA evidence is
  sequence-blocked on a separate `/charter` PR-first amendment (R8) — the build is not
  blocked, only the QA gate.

## 2. Affected Components

**Scoping method.** Scoped **by hand**. `aspark-graph`'s `impact` indexes only source
files (`.py/.ts/...`); this repo is Markdown-only, so an impact query returns empty *by
construction* (per `tools/aspark-graph.md`), not as an all-clear — it was therefore not
run. Line references below were verified against the live files.

- `templates/release-notes.md` — `Status` enum (`:8`), KEEP GATE (`:60–64`), Release
  Actions (`:35–44`), pre-flight (`:16–20`). *Protected rows `Status`/`Version` unchanged.*
- `templates/constitution.md` — new `Delivery & Handoff` section (before Amendments).
- `templates/spec.md` — new `Ticket` header row (protected US/AC forms untouched).
- `agents/release-manager.md` — read mode; steps 3/5 (proposed version, no tag, Q1/C10
  mechanism); changelog-rule scoping (`:88`).
- `agents/facilitator.md` — seventh section name in the drafting enumeration (`:59`).
- `skills/go-live/SKILL.md` — read the declared mode; default to direct when absent.
- `skills/spark/SKILL.md` — phase-map row (`:50–51`): `handed-off` = loop closed.
- `skills/next-steps/SKILL.md` — classify `handed-off` as shipped-pending-approval (`:35–36,73`).
- `docs/workflow.md` — terminal-status prose (`:85,95`).
- `README.md` — terminal status (`:30`) + §Project Status positive-case label.

No new dependency, service, slash command, agent, template or directory (NFR-3).

## 3. Task Breakdown

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | **Walking skeleton — additive terminal status + read-side recognition.** Add `handed-off` to the `Status` enum (rows `Status`/`Version` unchanged in name/order); teach `/spark`'s phase map and `/next-steps`' classification to treat it as closed-for-this-team, named distinctly from `released`. | US-2 | AC-2.1, AC-2.4, NFR-1, NFR-3 | – | `done` | `git diff templates/release-notes.md` shows only the added enum value, `Status`/`Version` rows byte-unchanged; `/spark` phase-map lists a `handed-off` → "loop closed" row (does not route to `/go-live`); `/next-steps` classifies `handed-off` as shipped-pending-approval, not in-flight/stalled — files: templates/release-notes.md, skills/spark/SKILL.md, skills/next-steps/SKILL.md |
| T2 | **Constitution declaration + facilitator drafting.** Add the `Delivery & Handoff` section declaring exactly five facts (mode, approver, target branch, ticket-reference format, terminal status), each with its *when-undeclared* default; add its name to `facilitator.md:59`'s section enumeration. | US-3 | AC-3.1, AC-3.3, AC-3.4, AC-3.5, NFR-4 | – | `done` | The new section declares the five facts and nothing per-feature, each stating its default; `facilitator.md` enumerates the seventh section so `/charter` grounds it (or marks it guessed) rather than leaving placeholder text; existing sections and the Amendments-log behavior are untouched — files: templates/constitution.md, agents/facilitator.md |
| T3 | **Mode-aware control flow (default to direct).** `/go-live` + Release Manager read the constitution's declaration; missing/partial → direct/no-ticket/`released` with no prompt, no warning, no `handed-off` string. The **only** gate condition for `handed-off` is "constitution declares PR mode" (never a pipeline/window signal); the two variants are mutually exclusive per run. | US-1, US-3, US-2 | AC-1.1, AC-1.2, AC-3.2, AC-3.5, AC-2.6, AC-2.7 | T2 | `done` | With no declaration, the numbered steps/report sections/gate boxes match the pre-change run and output greps to zero `handed-off`/`Delivery & Handoff`; the mode is read from the constitution only (never inferred from repo/remote/conversation); the Release Manager's sole `handed-off` check is the declared-PR-mode fact — files: skills/go-live/SKILL.md, agents/release-manager.md |
| T4 | **Handoff-mode gate variant + report content.** Inline mode-annotations on the KEEP GATE and Release Actions: PR on target branch / CI green / approver requested / ticket linked / rollback written, Version marked **proposed** (no tag before merge, C9/A9), deploy + smoke → N/A with the mode named. Release Manager step 3/5 rewritten for proposed-version and the Q1/C10 fact-establishing mechanism (read-only check where access exists per `:81–83`, else visibly-labelled self-attestation). One-line outstanding-owner statement in the report (AC-2.3). | US-2 | AC-2.2, AC-2.3, NFR-8 | T1, T3 | `done` | In handoff mode every presented box is satisfiable without a deploy; KEEP GATE stays ≤10 boxes; the report names the proposed version, the outstanding step and its owner (real tag/merge outside aSPARK), and each PR/CI/approver fact cites which C10 path established it — files: templates/release-notes.md, agents/release-manager.md |
| T5 | **Ticket has one home + rule scoping.** Add the `Ticket` row to `spec.md` (value follows the declared format or explicit "none"); scope `release-manager.md:88` so the no-ticket-ID rule binds only the user-facing changelog and exempts the header table, Release Actions record and PR description; confirm no other template gains a ticket field. | US-4, US-1 | AC-1.4, AC-4.1, AC-4.2, AC-4.3, AC-4.4, NFR-9, NFR-10 | – | `done` | `spec.md` carries a `Ticket` row (protected US/AC forms untouched); `release-manager.md:88` names the section it binds and the three exemptions so the next run cites rather than strips the ticket; grep confirms `plan/review/qa/release`/`constitution` templates carry no ticket field; the ticket anchors nothing in the `US-/AC-/NFR-/T/F` chain — files: templates/spec.md, agents/release-manager.md |
| T6 | **Docs in step.** State *both* terminal statuses in `README.md:30` and `docs/workflow.md:85,95` in this same change; `README.md` §Project Status labels this feature's positive case truthfully as **unproven** until its own release closes (NFR-6/NFR-7). Each file 1–3 lines. | US-2 | NFR-7 | T1 | `done` | Both docs name `released` and `handed-off` as terminal; README §Project Status marks the positive case unproven; `git diff --stat` confirms each file changed 1–3 lines — files: README.md, docs/workflow.md |
| T7 | **Evidence record — negative case first.** Written dry-run record in this feature's `.spark/` trail of every touched ceremony (`/charter`, `/go-live`, `/spark` resume, `/next-steps`), negative case run **first** in this repo, each outcome stated; confirm existing `.spark/graph-gates/` artifacts are neither migrated nor flagged and that no ceremony polls a handed-off PR. Positive case deliberately deferred to this feature's own `/go-live` (C8/R8). | US-1, US-2 | AC-1.1, AC-1.3, AC-1.5, AC-2.5, NFR-2, NFR-5, NFR-6 | T1, T3, T4 | `done` | The record shows the negative case ran first with its outcome; a before/after `/spark`-resume and `/next-steps` dry run over `.spark/graph-gates/` shows `released` routing unchanged and existing artifacts untouched; no ceremony re-checks or re-opens a handed-off PR; the QA-gate note states positive-case evidence is pending this feature's own release |

## 4. Test Strategy

No automated tests — prompt material has no suite (constitution §4, A2). Evidence is a
written dogfood/dry run, **negative case first** (NFR-6), per Must story:

- **US-1 (unchanged default).** Grep-and-compare: run `/go-live`, `/spark` resume and
  `/next-steps` against this repo (which declares no mode) before and after the change;
  assert identical steps/sections/gate boxes, unchanged `released` routing, and **zero**
  `handed-off` / `Delivery & Handoff` occurrences (T7, AC-1.1/1.2/1.5, NFR-5).
- **US-2 (honest terminal).** Structure-only `git diff templates/release-notes.md`
  proves the enum is additive (T1/AC-2.1). The handoff *report* is exercised by this
  feature's own release — the deferred positive case (C8) — checked at this feature's QA
  gate, not now (NFR-6, R8).
- **US-3 (declared once).** Dry run of `/charter` on a scratch constitution confirms the
  Facilitator proposes the section grounded (AC-3.3), and a partial declaration defaults
  cleanly (AC-3.5) with no prompt (T2/T3).
- **US-4 (Should).** `git diff` + grep verify the `Ticket` row exists only in `spec.md`
  and the scoped `:88` rule preserves it across a simulated changelog write (T5).
- **Left to this feature's own Keep phase / `/peer-review`:** the live PR-mode run (R8)
  and which C10 path actually fired for AC-2.2's boxes (R9).

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| R8 — positive-case QA blocked on a separate `/charter` PR-first amendment | This feature's QA gate cannot close on positive evidence until that amendment lands and this feature's own PR runs through it | Out of plan/build scope (T1–T7 proceed now); NFR-6 QA-gate note makes the wait explicit; `/sprint-plan` sequences the two so the amendment lands before this feature's `/go-live` |
| R9 — self-attestation becomes the common path for AC-2.2 facts | The handoff boxes read stronger than they are | T4 requires the report to cite *which* C10 path established each fact; `/peer-review` checks the fired path in the dogfood evidence, not just that a box is ticked |
| R2 — two gate variants soften the gate | Team picks the easier list | Single gate with inline annotations (not two lists); mode declared before release, never agent-chosen (T3/AC-3.2/2.6/2.7) |
| R7 — loose `:88` scoping strips the ticket silently | Reference lost with no error | T5 names the bound section *and* the three exemptions explicitly; verified by a simulated changelog write |
| R1/R6 — `handed-off` as escape hatch / future consumer semantics | Trail claims done while PR rots; a later board mis-reads it | AC-2.3 outstanding-owner line + AC-2.4 distinct naming (T1/T4); R6 recorded for the next cross-repo change, no consumer compares `released` today (A3) |
| NFR-8 overrun (≤90 net lines, ≤10 gate boxes) | Increment too large to review in one pass | Additive-only edits; `git diff --stat` checked at T6; gate expressed as annotations, kept ≤10 boxes at T4 |

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
- [x] Status set to `approved` by the user
