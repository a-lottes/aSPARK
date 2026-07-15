# Spec: situational-lenses

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `draft` |
| **Date** | 2026-07-15 |

> **Retrospective spec.** This feature is already implemented in the working
> tree. This document is the spec the work *should have had*: it interrogates the
> idea, judges scope, and its acceptance criteria are written to match reality so
> the build can be traced against them. Each story carries a **Build status**
> line noting where the implementation already satisfies the AC and where a gap
> remains. The Clarify pass is now resolved (C1–C5); two agreed ACs describe
> behavior the built code does **not** yet meet — see *Gaps: built code vs. this
> spec*. The gate stays open on design-review confirmation and user approval.

## 1. Problem & Goal

- **Problem:** aSPARK applies the *same* quality checklists to every project.
  A one-size-fits-all loop hurts in two opposite directions at once:
  - **Relevant concerns fall through.** A public website ships with no SEO
    scrutiny, an API with inconsistent error envelopes, an auth-handling app
    with only baseline security — because no phase is told to look, and the
    concern is never raised-then-verified under a traceable ID.
  - **Irrelevant concerns nag.** A CLI or a library gets pestered about SEO and
    mobile UX. Noise trains the user (and the agents) to skim, which erodes
    trust in *every* check.

  The person who hurts is the **aSPARK user building a specific kind of
  software** who gets generic feedback instead of feedback shaped to what they
  are actually building. A secondary user, the **lens author/maintainer**, hurts
  when adding a new concern means rewriting agents and skills.
- **Goal:** The loop adapts to the project. The kind of software (type +
  characteristics) is recorded once, activates a set of situational checklists
  ("lenses"), and those checklists are applied *by the existing agents in the
  phases they own* — so a relevant concern becomes a measurable NFR in Specify
  and is verified downstream under the same `NFR-n` ID, while an irrelevant
  concern is consciously switched off.
- **Success signal (observable):** the measure spans **both** a UI-lens verified
  in QA and a non-UI/Review-lens verified in Review, so the whole loop — not just
  the browser end — is demonstrably situational:
  - **UI-lens fires and is QA-verified.** On a `website` feature, `/story-time`
    produces **≥1 SEO NFR** that `/demo-day` verifies in the browser under the
    same `NFR-n`.
  - **Review-lens fires and is Review-verified.** On an `api` project,
    `/story-time` produces **≥1 `api`/`security` NFR** that `/peer-review` traces
    to the diff under the same `NFR-n` — a non-UI concern with no `/demo-day`
    surface still completes the chain.
  - **Suppression works.** On a `cli`/`library`/`api`-only feature, **zero**
    SEO/UX NFRs are raised.
  - **Add-a-file holds.** Adding a new concern touches only `lenses/` — **no**
    agent or skill file is edited (verifiable by diff).
- **Why now:** Situational relevance is the concrete expression of aSPARK's core
  promise — "does the product *actually* work". Without it, the loop's feedback
  is generic, which is exactly the value a solo user could already get from an
  unguided model. This is what makes the gated process worth its ceremony.

## 2. Target Users

- **The aSPARK user (primary):** a solo developer or small team running the loop
  on one project of a definite shape — a public marketing site, an app-like
  dashboard, an API service, a CLI, a library — who wants feedback tuned to that
  shape and quiet about everything else.
- **The lens author / plugin maintainer (secondary):** a contributor who wants
  to add a new concern (a new lens) without touching the agents or ceremonies.

Explicitly **not** a user of this feature: an end user of the *built product*.
This feature governs how aSPARK scrutinizes projects; it ships no runtime surface.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived partly as a solution ("activate concern-checklists (lenses) driven by a project profile in the constitution"). Translated to the underlying need: *the loop's scrutiny must match the kind of software, without adding roles*. Original phrasing recorded here per the no-solutions-in-spec rule. | Accepted framing |
| A2 | aSPARK's own repo had **no** `.spark/constitution.md` — the feature was unproven by dogfooding on aSPARK itself. It now carries this spec under `.spark/situational-lenses/`; the dogfooding gap is being closed via this very `/story-time` run, and running `/charter` on aSPARK is the recommended next proof. | Being closed — see Risk R6 |
| A3 | aSPARK is a set of markdown prompts executed by LLM agents. "Correct behavior" here means *the instructions reliably steer the agents*, not a deterministic guarantee. No automated test enforces that a lens was applied. | Assumption — see Risk R1 |
| Q1 | **Success signal not defined by the idea.** What is the falsifiable measure this feature is judged by? | **Resolved (C1)** — both a UI-lens (QA-verified) and a Review-lens (Review-verified) must fire; folded into §1 and AC-2.1a/AC-3.4. |
| Q2 | **Per-phase fallback detection** — intended, or should detection happen once? | **Resolved (C2)** — slim the fallback to a *nudge*; per-lens logic always reads the constitution. Current build over-does this (Gap G1). Folded into US-4. |
| Q3 | **Lens overload** — cap or not? | **Resolved (C3)** — no cap, but the profile must flag when 4+ lenses are active. Folded into AC-1.4 (Gap G2). |
| Q4 | **Baseline/lens seam** — who adjudicates? | **Resolved (C4)** — the agent that owns the phase adjudicates; every lens's "cite each finding once" prevents double-reporting. Folded into NFR-9. |
| Q5 | **Half-size** — all eight lenses, or three exemplars? | **Resolved (C5)** — user consciously keeps all eight; the five beyond the exemplars are the deliberate "add-a-file" proof that the mechanism scales. Folded into §6 and US-7. |

## 4. User Stories

### US-1 (Must): Record the project profile

> As an aSPARK user, I want the constitution to record my project's type(s) and
> characteristics, so that the loop knows which situational concerns apply.

**Acceptance criteria:**

- [ ] AC-1.1: Given a repo with detectable signals, when `/charter` runs, then the Facilitator proposes the detected type(s) (`website`/`web-app`/`api`/`cli`/`library`) and characteristics (`handles-auth`/`is-public`/`handles-payments`/`handles-pii`/`has-database`/`is-multilingual`), each with the file or config that evidences it.
- [ ] AC-1.2: Given proposed profile, when the user confirms, then a *Project Profile & Active Lenses* section is written to `.spark/constitution.md` listing the type(s), characteristics, and the derived active lenses with a "why active/off" and "enforced in" per lens.
- [ ] AC-1.3: Given the user rejects a proposed lens, when the constitution is written, then that lens is recorded as off — no lens is switched on that the user did not confirm.
- [ ] AC-1.4: Given **4 or more** lenses are active, when the profile section is written, then it surfaces the active-lens count and flags the elevated load (so agents in each phase see the stack is large and don't skim it). *(New — from C3.)*

*Build status: **Satisfied.*** `templates/constitution.md` §2 provides the
section; `agents/facilitator.md` and `skills/charter/SKILL.md` cover AC-1.1–1.3.
**Gap G2 closed:** the template now carries an *Active-lens load* line with an
elevated-load flag at 4+ lenses, and the Facilitator/charter populate and surface
it (AC-1.4). (Instruction-driven, per R1.)

### US-2 (Must): Lens concerns enter the spec as measurable NFRs

> As an aSPARK user, I want each active lens's concerns captured as measurable
> NFRs in the spec, so that the concern is verified downstream, not asserted once.

**Acceptance criteria:**

- [ ] AC-2.1: Given active lens `seo` on a website feature, when `/story-time` runs, then the spec contains ≥1 SEO NFR (e.g. an LCP budget; unique title/description per route) whose "How it's verified" column names the owning downstream phase(s).
- [ ] AC-2.1a: Given an active **Review-owned** lens on a non-UI project (e.g. `api` or `security` on an `api` service), when `/story-time` runs, then the spec contains ≥1 NFR for that lens whose "How it's verified" column names `/peer-review`. *(New — from C1; ensures the success signal's Review half has a spec anchor.)*
- [ ] AC-2.2: Given an active lens with nothing relevant to *this* feature, when the spec is written, then a one-line conscious N/A records that — not a silent omission.
- [ ] AC-2.3: Given the PO applies a lens, when the spec is written, then the lens's own checklist is **not** pasted verbatim into stories — only the falsifiable slice this feature must meet appears, as NFRs.

*Build status: **Satisfied (unenforced).*** `agents/product-owner.md` step 4 and
`skills/story-time/SKILL.md` steps 2–3 wire this, including the non-UI case.
Caveat: compliance is instruction-driven, not verified by any test (Risk R1);
AC-2.1/2.1a/2.2 are only demonstrable by running the loop on a real project.

### US-3 (Must): A concern raised in one phase is verified in the phase that owns it

> As an aSPARK user, I want each agent to apply only the lens rows for the phase
> it owns, so that a concern raised in Specify is actually checked in Review/QA
> under the same NFR ID — never asserted then dropped.

**Acceptance criteria:**

- [ ] AC-3.1: Given a lens file, when it is authored, then every check names exactly one owner phase, and no check is owned by a phase absent from the lens's `phases` frontmatter.
- [ ] AC-3.2: Given an SEO NFR raised in Specify, when `/peer-review` and `/demo-day` run, then each verifies its owned slice (metadata/render in review; rendered title/meta and Core Web Vitals in the browser) and reports under the same `NFR-n`.
- [ ] AC-3.3: Given a non-UI lens (`api`/`cli`/`library`/`data`), when the loop reaches `/demo-day`, then it contributes zero browser checks — its verification is carried by Specify, Review and the increment's own tests.
- [ ] AC-3.4: Given a Review-owned lens NFR raised in Specify on a non-UI project, when `/peer-review` runs, then the Reviewer traces that `NFR-n` to a concrete location in the diff (or files a finding at the lens severity) under the same ID — the chain completes without a QA surface. *(New — from C1.)*

*Build status: **Satisfied.*** Each lens has a per-phase "Who owns what" map and
`phases` frontmatter; `agents/reviewer.md` step 8, `agents/qa-tester.md` step 4
and `agents/designer.md` §4 apply only their phase's rows; non-UI lenses declare
`phases` without `qa` and are Review-verified.

### US-4 (Should): Detection nudges, the constitution decides

> As an aSPARK user on a project without a constitution, I want each phase to give
> a lightweight *nudge* ("this looks like a `<type>` — run `/charter`") rather than
> re-run full lens logic itself, so that there is one source of truth and phases
> can't drift from each other.

**Acceptance criteria:**

- [ ] AC-4.1: Given no `.spark/constitution.md`, when a phase skill runs, then its fallback does **only** a lightweight nudge — it names the likely type(s) and points to `/charter` to make it stick. It does **not** resolve or apply per-lens checklists on its own.
- [ ] AC-4.2: Given detection nudges a lens, when the user does not run `/charter`, then no lens is applied — nothing is switched on silently.
- [ ] AC-4.3: Given a `.spark/constitution.md` exists, when any phase runs, then the per-lens logic reads the **active lenses from the constitution only** — the fallback nudge path is not used, so there is a single source of truth and no cross-phase drift. *(New — from C2.)*

*Build status: **Satisfied — Gap G1 closed.*** The fallback in `skills/story-time`,
`look-and-feel` and `spark` is now nudge-only: with no constitution it names the
likely type in one line and points to `/charter`, and applies **no** lens off a
guess (AC-4.1). Per-lens logic reads the active lenses from the constitution only,
making it the single source of truth with no cross-phase drift (AC-4.3).
`/peer-review` and `/demo-day` already read lenses from the constitution, so they
match the bar. (Instruction-driven, per R1.)

### US-5 (Should): A new concern is add-a-file

> As a lens author, I want adding a new concern to be a single new file following
> a documented contract, with no agent or skill rewrite, so that the system stays
> extensible.

**Acceptance criteria:**

- [ ] AC-5.1: Given `lenses/README.md`, when a contributor reads it, then the lens contract is documented: frontmatter (`name`, and either `applies-to` or `triggers`, plus `phases`), a per-phase owner map, and falsifiable-checks-only.
- [ ] AC-5.2: Given a new `lenses/<name>.md` plus a profile entry, when a phase runs with that lens active, then it is picked up without editing any agent or skill file (skills pass active lens paths generically by name).
- [ ] AC-5.3: Given a new lens binds to a new type or characteristic, when it is added, then the README's *Available lenses* table and *Detection signals* are updated to list it.

*Build status: **Satisfied.*** `lenses/README.md` documents the contract and the
"Adding a lens" procedure; skills pass `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`
paths generically.

### US-6 (Should): Irrelevant concerns are suppressed

> As an aSPARK user building software a lens doesn't apply to, I want irrelevant
> concerns switched off, so that I'm not nagged about SEO on a CLI.

**Acceptance criteria:**

- [ ] AC-6.1: Given a `cli`-only profile, when `/story-time` and `/demo-day` run, then no SEO or UX NFRs are raised or tested.
- [ ] AC-6.2: Given a lens, when it is authored, then its `applies-to`/`triggers` frontmatter scopes it to exactly the types/characteristics it belongs to (e.g. `seo: applies-to [website]`).

*Build status: **Satisfied (by construction, unenforced).*** Frontmatter scoping
is present; suppression relies on agents honoring "apply only lenses you were
given" (Risk R1).

### US-7 (Could): Eight starter lenses out of the box

> As an aSPARK user, I want the common project types and characteristics covered
> by ready-made lenses, so that the mechanism is useful on day one.

**Acceptance criteria:**

- [ ] AC-7.1: Given the plugin, when the user inspects `lenses/`, then eight lens files exist — `seo`, `ux`, `api`, `cli`, `library`, `security`, `i18n`, `data` — each conforming to AC-5.1.
- [ ] AC-7.2: Given the README, when the user reads it, then the *Available lenses* table and detection signals list all eight and how each activates.

*Build status: **Satisfied.*** All eight files present and README tables
complete. Per C5 the full eight are a **conscious scope decision**: three
exemplars prove the mechanism, and the other five are the deliberate
"add-a-file" demonstration that it scales — not an oversight.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Contract conformance | Every lens file carries valid frontmatter (`name`, exactly one of `applies-to`/`triggers`, and `phases`), a per-phase owner map, and only falsifiable checks (each names a location/signal and a concrete fix — no "make it SEO-friendly"). | `/peer-review` of `lenses/*.md` |
| NFR-2 | Traceability | No lens check is owned by a phase not listed in its `phases` frontmatter; every concern raised in Specify as an `NFR-n` has a downstream owner phase. | `/peer-review` |
| NFR-3 | Consent / no silent activation | No skill or agent applies a lens without either a confirmed constitution entry or a surfaced nudge the user acts on via `/charter`. | `/peer-review` of skill/agent instructions + a no-constitution dry run |
| NFR-4 | Architectural constraint | The feature adds **zero** new agents and **zero** new skills; count remains 7 agents / 8 skills. Lenses are applied only by existing agents. | Diff review |
| NFR-5 | Relevance / scoping | A lens contributes zero checks on a profile that does not activate it (e.g. `seo` on a `cli`). | Dry run on a `cli` sample project |
| NFR-6 | Extensibility / maintainability | Adding a lens requires edits only within `lenses/` (new file + README table + detection-signal row); no agent or skill file changes. | Diff review of a sample lens addition |
| NFR-7 | Accessibility | N/A — this feature ships no UI of its own; it governs how *other* projects' accessibility is checked (via the `ux`/`seo` lenses), which is those projects' concern. | N/A |
| NFR-8 | Performance | N/A at runtime — lenses are prompt-time context, not executed code. The real cost is *agent attention* when many lenses stack; bounded by the AC-1.4 4+-lens visibility flag rather than a cap. | N/A |
| NFR-9 | Seam governance (single source of truth) | The agent that **owns a phase** adjudicates the boundary between its baseline checks and any active lens's "depth beyond baseline"; every lens file instructs "cite each finding once" so an overlap (e.g. `seo` alt-text vs accessibility, `security` vs Reviewer baseline) is reported exactly once, never doubled or dropped. | `/peer-review` of lens files + agent instructions |

## 6. Out of Scope

Consciously cut this cycle (documented so the "no" isn't forgotten):

- **Automated enforcement.** No test/CI proves an agent actually applied a lens
  or wrote the expected NFR. The feature is convention; the human gate is the
  only check. (Named as R1; would be the highest-value follow-up.)
- **A hard cap on simultaneously-active lenses.** Per C3, unbounded stacking is
  *allowed*; instead of a cap, the profile flags the load when 4+ lenses are
  active (AC-1.4). No throttling or auto-disabling.
- **Machine-readable profile.** The profile is prose in the constitution, not
  structured data; nothing parses it deterministically.
- **Continuous re-detection.** The profile is set once and amended via `/charter`;
  it does not track the repo drifting into a new type over time.
- **Project-local / custom lenses beyond the plugin.** A team cannot ship a lens
  that lives only in their repo; lenses live in the plugin's `lenses/`.
- **Marketing SEO** (keyword strategy, link building) — explicitly excluded by
  the `seo` lens itself; it keeps only the *technical* foundations of findability.
- **Per-lens severity scales.** Lenses reuse the shared `Blocker`/`Major`/`Minor`
  scale; no lens-specific grading.

**Consciously kept in scope (not cut), per C5:** all eight lenses (`seo`, `ux`,
`api`, `cli`, `library`, `security`, `i18n`, `data`). The three exemplars prove
the mechanism; the remaining five are the deliberate proof that "a new concern is
just a new file" holds at scale. This was the user's explicit decision, recorded
here so it reads as chosen breadth, not scope creep.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-07-15 | What is the falsifiable success signal? (Q1) | Strengthened: the signal must show **both** a UI-lens firing and being QA-verified (SEO NFR on a `website`, verified in `/demo-day`) **and** a Review-lens firing and being Review-verified (`api`/`security` NFR on an `api` project, traced to the diff in `/peer-review`) under the same `NFR-n`. Folded into §1, AC-2.1a, AC-3.4. |
| C2 | 2026-07-15 | Is per-phase fallback detection intended, or detect once? (Q2) | Slim the fallback to a **nudge** — each skill without a constitution only names the likely type and points to `/charter`; all per-lens logic reads the constitution, removing cross-phase drift. Current build over-does this (Gap G1). Folded into US-4 (AC-4.1/4.3). |
| C3 | 2026-07-15 | Cap lenses when many activate? (Q3) | **No cap**, but the profile must **flag** when 4+ lenses are active so the load is visible. New requirement AC-1.4; template gap G2. Folded into US-1, NFR-8, §6. |
| C4 | 2026-07-15 | Who adjudicates the baseline/lens seam? (Q4) | The **phase-owning agent** adjudicates the seam between its baseline and a lens's "depth beyond baseline"; every lens's "cite each finding once" prevents double-reporting. Folded into NFR-9. |
| C5 | 2026-07-15 | All eight lenses, or three exemplars? (Q5) | **Keep all eight** — a conscious scope decision: three exemplars prove the mechanism, the other five prove "add-a-file" scales. Folded into US-7 and §6. |

## 8. Design Review

<!-- This feature ships no UI of its own — it is markdown prompt/template/lens
     artifacts executed by LLM agents. A design review is therefore N/A. -->

- **Status: N/A — no UI surface.** The feature governs how *other* projects are
  scrutinized (including their UI, via the `ux`/`seo` lenses); it renders nothing
  itself. Verifiable by diff: the change touches only `lenses/`, `agents/`,
  `skills/`, `templates/`, `docs/` and `README.md` — no runtime UI code. The
  Designer's usability/accessibility heuristics have no artifact to apply to here.
  (Recorded by the orchestrator at the SPEC GATE; a formal `/look-and-feel` pass
  can confirm this N/A if desired, but would return the same.)

---

## Gaps: built code vs. this spec — **both closed**

The Clarify resolutions created two places where the *agreed* spec outran the
*built* implementation. The user chose to close them directly rather than defer
them to a later `/increment`; both are now fixed in the working tree:

- **G1 — Fallback was over-built (US-4, AC-4.1/4.3). ✅ Closed.**
  `skills/story-time`, `look-and-feel` and `spark` re-derived full
  type/characteristic logic and offered to *apply* lenses per phase without a
  constitution. Per C2 they are now **nudge-only** (name the likely type, point to
  `/charter`, apply nothing), and all per-lens logic reads the constitution as the
  single source of truth. `peer-review`/`demo-day` already met this bar. Docs
  (`lenses/README.md`, `docs/workflow.md`) aligned to the same rule.
- **G2 — No 4+-lens load flag (US-1, AC-1.4). ✅ Closed.**
  `templates/constitution.md` §2 now carries an *Active-lens load* line and an
  elevated-load flag that appears at 4+ active lenses; `agents/facilitator.md`
  records the count and raises the flag, `skills/charter` surfaces it to the user.
  No cap — visibility is the throttle, per C3.

All of US-1..US-7 is now satisfied by the build, with the standing **R1** caveat
that satisfaction is instruction-driven, not test-enforced. The ACs remain
unchecked by design: they are verified by *running* the loop on real projects
(the success signal in §1), not asserted at spec time.

## Named Risks

- **R1 — Convention, not enforcement.** The whole feature relies on LLM agents
  obeying instructions; no test proves a lens fired. A silently-skipped lens
  looks identical to a correctly-N/A'd one. Highest-impact standing risk.
- **R2 — Fallback drift → resolved and realized (C2 / G1 closed).** The fallback
  is nudge-only and the constitution is the single source of truth, so the drift
  surface is gone.
- **R3 — Lens overload → resolved and realized (C3 / G2 closed).** No cap, but the
  profile flags elevated load at 4+ lenses, so the stack is visible.
- **R4 — Baseline/lens seam → resolved by design (C4/NFR-9).** The phase-owning
  agent adjudicates; "cite each finding once" prevents doubling.
- **R5 — Thin marginal value.** An Opus agent already knows SEO and security. The
  lens's value is *consistency, traceability, phase-ownership and suppression* —
  not net-new knowledge. If that framing isn't kept, the ROI over an unguided
  prompt is small.
- **R6 — Dogfooding being closed.** aSPARK's repo now carries this spec; running
  `/charter` on aSPARK itself is the recommended next proof that the profile and
  lenses work on the very repo that ships them.

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C5 resolved and folded
- [x] Open questions are resolved or explicitly accepted as risk — Q1–Q5 resolved; R1/R5 accepted as standing risks
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions — none exists (A2)
- [x] Design review done for UI-facing features (or marked N/A with reason) — **N/A: feature ships no UI (see §8)**
- [ ] Status set to `approved` by the user — **awaiting the user's explicit decision**

> **Note for planning:** the two gaps this spec opened (G1 nudge-slimming, G2
> 4+-lens load flag) were closed directly in the working tree at the user's
> decision, so the build now matches every agreed AC. What remains is not spec
> work but **proof**: the success signal in §1 is only demonstrable by running the
> loop on real projects (a `website` and an `api`), and R1 stands — no test
> enforces that a lens fired. Recommended next proof: `/charter` on the aSPARK
> repo itself.
