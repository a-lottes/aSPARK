# Spec: accessibility-lens

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-09-14 |
| **Ticket** | none |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this spec updates it in the same edit that resolves a clarification or
     changes status: overwrite in place, never append. The block holds one current
     state, never a per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** `approved` by the user, 2026-09-15 — reworked against the verbatim GitHub issue #6 text (round 2; round 1 worked from an unverified paraphrase and got the activation model wrong — see C1/C6). Clarify pass done (C1–C7). Design Review N/A (§8, `situational-lenses` precedent), accepted at approval.
- **Summary:** Add `lenses/accessibility.md` as a **characteristic-triggered** lens (`triggers: [must-be-accessible]`, structured like `security.md`), giving every SPARK phase from Specify through QA a falsifiable, non-duplicative accessibility check — closing the gap where today only the Designer's one-time baseline critique (`agents/designer.md` §3) exists, and nothing verifies the implemented code or the running UI against a traceable `NFR-n`.
- **Open:** `none` — no blocking open questions. The positive-firing half of the success signal and the "characteristic declared with no UI surface" edge case (C7) are named risks, not open questions.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for the round-2 correction and why.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** The Designer's baseline Critique Lens (`agents/designer.md` §3) checks contrast, keyboard
  reachability, labels/alt text and touch targets — but only **once**, at Design-review time, before any
  code exists, and only as freeform prose in the spec's Design Review section, not a traceable `NFR-n`.
  Nothing downstream re-confirms it: `/peer-review` traces no accessibility concern in the diff (a custom
  modal that traps focus, a form whose semantics were dropped for a raw `<div>`, ARIA bolted on where
  native HTML would have worked, ship undetected), and `/demo-day` has nothing concrete to verify against.
  Today accessibility is only partly covered inside `ux.md`, gated on project *type* (`web-app`/`website`)
  — but per issue #6, "is this WCAG-checkable" is a concern a growing number of projects carry
  **independently of type**, especially with the European Accessibility Act now in force (June 2025):
  a `library` that ships a generated docs site, an `api` service with an admin console, a `cli` tool with
  a companion web dashboard, all can carry the same obligation a `website` does.
- **Goal:** `lenses/accessibility.md`, triggered by a **characteristic** (`must-be-accessible`), not a
  type — mirroring `security.md`'s own structure (the issue's named precedent) — gives every phase from
  Specify through QA a falsifiable check, so a concern raised upstream is genuinely verified downstream,
  without re-covering what the Designer's baseline or `ux`/`seo` already own.
- **Half-size version considered:** drop Act-phase ownership (semantic markup/ARIA) and leave it as a
  Review-only finding, since Review already exists on every diff. Rejected: by the time Review runs, the
  wrong markup is already written; catching it at Review costs a fix-and-re-review cycle every lens the
  Reviewer already runs (`api`, `library`) accepts for other concerns, but issue #6 explicitly asks for the
  Act-phase row, and it costs **zero new wiring** (C6) — there's no half-size saving worth taking here.
- **Success signal:** two halves —
  - **Suppression (provable now, by this repo's own dogfood):** on a profile that does **not** declare
    `must-be-accessible` — any type, including aSPARK Core's own `library` profile — the lens contributes
    **zero** checks, findings or NFRs.
  - **Positive firing (not provable here — named, not guessed):** on a real project that declares
    `must-be-accessible`, `/story-time` produces ≥1 accessibility `NFR-n` that `/peer-review` traces to a
    `file:line` in the diff **and** `/demo-day` verifies live (keyboard-only walkthrough, measured
    contrast) under the same `NFR-n`. aSPARK Core has no browser-observable surface (constitution §8) and
    declares no UI-bearing characteristic, so this half is recorded `not-verified-live`, pending a field
    report — the same predicament `situational-lenses` named for its own `website`/`api` legs
    (`ROADMAP.md`, "The one gap that matters most"; `.spark/situational-lenses/evidence.md` T9).
- **Why now:** Issue #6, `good first issue`, cites the European Accessibility Act directly as the reason
  this is now a type-independent concern, not a niche one. The lens *mechanism* is proven
  (`situational-lenses`, `handed-off`) and "add-a-file" is its own demonstrated success signal — this is
  the cheapest possible next lens, grouped in `ROADMAP.md` with performance (#7) and observability (#15).

## 2. Target Users

- **The aSPARK user on any project that declares `must-be-accessible`, of any type (primary):** wants
  Specify-through-QA accessibility scrutiny tied to a traceable NFR, not a one-time Design pass nothing
  re-confirms — whether that project is a `website`, a `web-app`, or a `library`/`api`/`cli` with an
  embedded UI surface.
- **The lens author/maintainer (secondary):** wants the add-a-file contract (`lenses/README.md`) exercised
  correctly, including the first lens check ever owned by the **Act** phase (C6).
- **Not a user:** an end user of the *built* downstream product. **Not aSPARK Core's own maintainer in the
  positive-firing sense** — Core has no UI and declares no accessibility obligation; nobody here ever
  experiences the lens actually firing, only downstream consumers do.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | Round 1 of this spec worked from an unverified `/next-steps` paraphrase of issue #6 and got the activation model wrong (type-triggered `[web-app, website]` instead of the issue's own characteristic-triggered `[must-be-accessible]`). Round 2 (this version) works from the verbatim issue text. | Corrected — see C1, C6. |
| A2 | No WCAG conformance level was specified in the issue. Assumed **AA**, matching the spec template's own existing `NFR-3` example — the de facto default and the level EAA/ADA exposure is typically measured against. | Assumption — not blocking; AAA is out of scope (§6). |
| A3 | This repo is Markdown/prompt material; "correct behavior" means the instructions reliably steer the agents, same standing assumption as `situational-lenses` A3/R1 — no test enforces that this lens fired. | Inherited, standing risk (see Named Risks). |

## 4. User Stories

### US-1 (Must): The lens exists, is triggered by a characteristic, and stays silent when undeclared

> As a lens author, I want `lenses/accessibility.md` to activate on a `must-be-accessible` characteristic
> — not a project type — and contribute nothing when that characteristic isn't declared, so the lens fires
> on the actual obligation (WCAG-checkable, independent of shape) rather than a proxy for it.

**Acceptance criteria:**

- [ ] AC-1.1: Given `lenses/accessibility.md`, when read, then its frontmatter declares `name: accessibility`, `triggers: [must-be-accessible]` (characteristic-triggered, structured like `security.md` — not `applies-to`, unlike `ux`/`seo`), and `phases: [specify, design, act, review, qa]` — the first lens to declare `act`, per US-2's AC-2.3/C6.
- [ ] AC-1.2: Given a project profile that does **not** declare `must-be-accessible` — of any type, including this repo's own `library` profile — when `/story-time`, `/look-and-feel`, `/peer-review` or `/demo-day` run, then the accessibility lens contributes zero NFRs, findings or checks.
- [ ] AC-1.3: Given `lenses/README.md`, when read, then (a) the *Available lenses* table lists `accessibility.md`, triggered by characteristic `must-be-accessible`, in the same format as `security`/`i18n`/`data`'s rows, and (b) the *Characteristics* detection-signals table gains a new `must-be-accessible` row (signal: an existing accessibility statement/VPAT/WCAG target in the repo, or the product being public-facing within a jurisdiction with a legal accessibility mandate — EAA, ADA Title II/III, Section 508, EN 301 549 — or a direct user confirmation at `/charter` absent a file-based signal, the same judgment-call latitude `is-public` already has) → activates `accessibility`.
- [ ] AC-1.4: Given the diff that adds this lens, when reviewed, then it touches only `lenses/accessibility.md`, `lenses/README.md`, and (per US-3) the two pointer lines in `lenses/seo.md`/`lenses/ux.md` — no agent or skill file is edited, including `skills/increment/SKILL.md`, despite this lens being the first to claim an Act-phase-owned check (reasoning: C6).

### US-2 (Must): Every phase from Specify through QA owns a falsifiable check, none duplicating another

> As an aSPARK user, I want the accessibility lens to give Specify, Design, Act, Review and QA each a
> falsifiable check — grounding what the Designer's baseline already flags into a traceable NFR, adding
> the implementation- and diff-level depth nothing today provides, and verifying live — so a concern
> raised upstream is genuinely checked downstream, never just asserted once.

**Acceptance criteria:**

- [ ] AC-2.1: Given the accessibility lens is active on a feature (owner: Specify — Product Owner), when `/story-time` runs, then the spec's accessibility NFR names the actual flow(s) to keyboard/screen-reader-test and the actual contrast target — not the template's generic "WCAG 2.1 AA" example verbatim — or, if the feature adds no new UI, records a one-line conscious N/A (the lens flags; it never invents scope).
- [ ] AC-2.2: Given the accessibility lens is active (owner: Design — Designer), when `/look-and-feel` runs, then it checks contrast, focus order/keyboard reachability and touch target size **by citing the Designer's existing baseline §3 once** (same signals, not a duplicate finding) — grounding them as the spec's `NFR-n`, not just Design Review prose — and separately checks `prefers-reduced-motion` support, citing `ux`'s existing motion check once when `ux` is also active, or owning it outright when it isn't (e.g. a `library` project with a docs site that has no `web-app`/`website` type declared).
- [ ] AC-2.3: Given the accessibility lens's grounded NFR from AC-2.1 (owner: Act — Developer), when `/increment` runs, then the implementation uses semantic HTML and labelled form controls, and adds ARIA (including live-region announcements for async state changes) **only where semantics fall short** — verified through the plan's existing task→AC/NFR traceability (`plan.md`'s `Covers (AC / NFR)` column), the same generic mechanism every other NFR category already uses; no new lens-resolution step is added to `/increment` itself (C6).
- [ ] AC-2.4: Given the accessibility lens is active (owner: Review — Reviewer), when `/peer-review` runs on a diff introducing or changing UI, then it traces **keyboard traps** and **focus management on route and modal changes** in the diff against the NFR, filing a `file:line` finding for any violation — a narrower remit than AC-2.3's semantic/ARIA implementation, which Review does not re-check (Named Risks R3 names the resulting gap honestly).
- [ ] AC-2.5: Given the accessibility lens is active (owner: QA — QA Tester), when `/demo-day` runs, then the QA Tester walks through **every acceptance criterion of the feature keyboard-only** (no mouse) and reports pass/fail per AC, reports a **measured** (not eyeballed) contrast ratio for ≥1 borderline text/background pair, and confirms whether AC-2.3's live-region announcements actually fire — all under the same `NFR-n`.

### US-3 (Should): Existing lenses name this lens instead of a generic phrase

> As a lens author, I want `seo.md`'s and `ux.md`'s existing "this doubles as the accessibility check"
> notes to name `accessibility.md` by path, so the seam between all three lenses (plus the Designer's
> baseline) is unambiguous rather than resting on a phrase that predates this file.

**Acceptance criteria:**

- [ ] AC-3.1: Given `lenses/seo.md` and `lenses/ux.md`, when read after this feature ships, then each place currently reading "this doubles as the accessibility check" / "keyboard-accessibility check" names `lenses/accessibility.md` by path, with the citing phase unchanged.
- [ ] AC-3.2: Given this edit, when the diff is reviewed, then no check in `seo.md`/`ux.md` is added, removed or reworded beyond the pointer text — a cross-reference precision fix, not a scope change to either lens.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Contract conformance | `lenses/accessibility.md` carries valid frontmatter (`name`, `triggers`, `phases`), a per-phase owner map, and only falsifiable checks — same bar as the other seven lenses (`lenses/README.md`). | `/peer-review` of the new file |
| NFR-2 | Traceability | Every check names exactly one owner phase present in its `phases` frontmatter (including the new `act` token); every concern raised in Specify as an `NFR-n` has a downstream owner. | `/peer-review` |
| NFR-3 | Consent / no silent activation | No skill or agent applies this lens without a confirmed `.spark/constitution.md` entry declaring `must-be-accessible`— same rule as every other lens. | `/peer-review` + a dry run on a no-constitution scratch project |
| NFR-4 | Suppression / relevance (constitution §1) | Zero checks, findings or NFRs contributed on any profile that does not declare `must-be-accessible`, regardless of type — verifiable live on aSPARK Core itself (`library`, characteristic absent). | Dry run on this repo |
| NFR-5 | `library` lens (Core's own active lens) | Adding `lenses/accessibility.md` is strictly additive to the consumed contract (constitution §2: the `${CLAUDE_PLUGIN_ROOT}/…` paths skills resolve) — no slash command, template heading, column or ID pattern is renamed or removed; ships as a minor version bump (constitution §5), deferred to `/go-live`. | `/peer-review` diff review |
| NFR-6 | Extensibility / maintainability, incl. the new Act-phase case | Adding this lens edits only `lenses/accessibility.md`, `lenses/README.md`, and the two pointer lines in `seo.md`/`ux.md` (US-3) — no agent or skill file changes, **including `skills/increment/SKILL.md`**, because `/increment` already reads `spec.md` §4/§5 unconditionally (its own SKILL.md step 2) and needs no lens-specific resolution step (C6). | Diff review (`git diff --name-only`) |
| NFR-Provability | Honesty about maturity (constitution §1) | This feature's positive-firing claim (US-2's success signal) **cannot** be proven by this repo's own dogfood — aSPARK Core has no browser-observable surface (§8) and declares no `must-be-accessible` characteristic. Provable here: the negative case (NFR-4), artifact-contract conformance (NFR-1/NFR-2), and the add-a-file diff shape (NFR-6). Not provable here: the positive case — recorded `not-verified-live`, pending a field report, same shape as `situational-lenses`'s own unresolved legs. | `/peer-review` (dogfood record) + `/demo-day` substitute method (§8) |
| NFR-Accessibility (this feature's own build) | Accessibility | N/A — this feature ships no UI of its own (a lens file); it governs how *other* projects' UI is checked. See US-1–US-3 and `lenses/accessibility.md` for the substantive checklist this feature delivers. | N/A |
| NFR-Performance | Performance | N/A — lenses are prompt-time context, not executed code (same as `situational-lenses` NFR-8). | N/A |

## 6. Out of Scope

- **CLI/terminal accessibility** (screen-reader-friendly stdout, colorblind-safe indicators beyond
  `NO_COLOR`). This lens's checks (ARIA, DOM focus order, rendered-pixel contrast) are web/UI-specific
  techniques that don't map onto a terminal, independent of whether `must-be-accessible` could technically
  be declared on a `cli`-typed project. Already partly covered by the existing `cli` lens (§2,
  `NO_COLOR`/TTY suppression); a dedicated terminal-accessibility depth is a separate concern for a future
  add-a-file, not this one.
- **`ux`'s flow efficiency, state coverage, forms, responsive/touch.** This lens adds only the
  assistive-tech-observable dimension of `ux`'s existing checks (AC-2.5's live-region confirmation) — never
  a parallel NFR for the same state.
- **`seo`'s semantic structure** (heading hierarchy, landmark regions, link text, alt text). Already owned
  by `seo`'s Review row and the Designer's baseline; not restated here.
- **Full WCAG A/AA/AAA, success-criterion-by-success-criterion coverage.** Too broad for one lens's
  falsifiable checklist; cut to the five-phase depth gap this spec names. AAA is out of scope (A2).
- **Automated tooling** (axe-core, Lighthouse CI, etc.). Constitution §3: Markdown + JSON only, no new
  tracked executable code; verification stays human/agent-performed, same as every other lens.
- **A new `/increment` capability or agent.** Act-phase ownership (AC-2.3) is satisfied entirely by
  `/increment`'s existing generic NFR/AC consumption (C6) — no new "Developer agent" file, no skill edit.
- **`.claude-plugin/plugin.json` version bump.** Named as a consequence (NFR-5) but executed at `/go-live`,
  not drafted here.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-14 | Round 1 assumed a type-triggered lens (`applies-to: [web-app, website]`, reusing `ux`'s signals) absent the verbatim issue text. Was that right? | **No — corrected.** The verbatim issue text explicitly specifies `triggers: [must-be-accessible]`, a **characteristic**, structured like `security.md`. Reworked throughout (§1, US-1, NFR-4). |
| C2 | 2026-09-14 | What's the boundary against `ux`/`seo`/the Designer's baseline, now that Design is back in scope? | No duplication: the Design-row (AC-2.2) cites the baseline's contrast/focus/target-size once and only adds the *traceable-NFR* framing on top of it (real value is traceability, not new content, per `situational-lenses`' own R5 finding); `ux`'s motion check is cited once when `ux` is active, owned outright otherwise. Act (AC-2.3) and Review (AC-2.4) are genuinely new — nothing today checks implemented ARIA/semantics or diff-level keyboard traps/focus management. |
| C3 | 2026-09-14 | Which phases own checks? | Specify, Design, Act, Review, QA — all five, per the issue's own explicit split (§4 US-2). |
| C4 | 2026-09-14 | Can the positive case be dogfooded on this repo? | No — aSPARK Core declares no `must-be-accessible` characteristic and has no browser-observable surface (§8). Only the negative case and artifact-contract conformance are provable here (NFR-Provability). |
| C5 | 2026-09-14 | Is the full WCAG surface in scope? | No — a five-phase-owned slice sized to the issue's own suggested split (§6), not an exhaustive audit tool. |
| C6 | 2026-09-14 | Does an Act-phase-owned check (a first for any lens) require editing `skills/increment/SKILL.md`, breaking the add-a-file promise? | **No.** `skills/increment/SKILL.md` step 2 already reads `spec.md` §4 (ACs) and §5 (NFRs) unconditionally for every feature and builds to satisfy them — the same generic mechanism every other NFR category (security, performance, …) already relies on. Once Specify grounds the accessibility NFR (AC-2.1), `/increment` inherits it without any lens-specific resolution step. `act` is a legitimate new `phases` token (the SPARK phase name itself, same grain at which `qa`/`design` were introduced when first needed) — not a new capability. |
| C7 | 2026-09-14 | Can `must-be-accessible` be declared on a project with no actual UI surface (e.g. a pure `cli`/`api` with nothing rendered)? | Structurally possible but not meaningful — the lens's checks need a rendered UI to check against. Named as an edge case for the Facilitator's judgment at `/charter` (same latitude `is-public` already has), not blocked here; a declaration with nothing to check simply produces no findings, which is indistinguishable from AC-1.2's negative case and is an accepted, non-blocking risk (Named Risks R4). |

## 8. Design Review

<!-- This feature ships no UI of its own — it is a Markdown lens/template artifact
     executed by LLM agents, same shape as `situational-lenses` (whose spec §8
     records the identical N/A for the identical reason). A design review is
     therefore N/A, following that precedent directly rather than spinning up
     a separate /look-and-feel pass for a feature with nothing to critique. -->

- **Status: N/A — no UI surface.** The feature governs how *other* projects'
  UI is scrutinized (via the accessibility lens's Design/Act/Review/QA checks);
  it renders nothing itself. Verifiable by diff: the change touches only
  `lenses/accessibility.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md`
  (US-3's pointer edit) — no runtime UI code, no template, no agent, no skill
  file (NFR-6).

## Named Risks

- **R1 — Convention, not enforcement (inherited from `situational-lenses` A3/R1).** No test proves any
  agent actually applied this lens; a silently-skipped check looks identical to a correctly-N/A'd one.
- **R2 — The positive case has no venue on this repo.** Same predicament `situational-lenses` never fully
  closed (NFR-Provability); treated honestly (`not-verified-live`) rather than stretched via a fixture.
- **R3 — Act's semantic/ARIA correctness is only self-checked by the developer who wrote it.** Review's
  remit is deliberately narrower (keyboard traps, focus management only — AC-2.4), matching the issue's
  own split; an ARIA mistake ships if the developer got it wrong and QA's keyboard-only walkthrough doesn't
  happen to surface it. Accepted, not mitigated further — narrowing Review's remit here was the issue's
  explicit choice, not an oversight.
- **R4 — `must-be-accessible` declared with no real UI surface (C7).** Produces zero findings,
  indistinguishable from correct suppression; a Facilitator judgment call at `/charter`, not a defect in
  the lens itself.

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C7 resolved and folded
- [x] Open questions are resolved or explicitly accepted as risk — A1–A3 accepted; R1–R4 named
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions — no conflict; §1 (suppression), §2 (profile/lenses), §3 (add-a-file, no new tracked code), §4 (dogfood + traceability), §5 (minor bump), §7 (Ticket stays `none`), §8 (browser surface honestly named) all threaded through
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A, §8, `situational-lenses` precedent (no UI surface of its own)
- [x] Line budget respected: Ist 183 / Soll ~250 (excluding HTML comments) — under budget
- [x] Status set to `approved` by the user
