# Spec: lens-dispatch-registry

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-09-17 |
| **Ticket** | none |

**Handoff**
- **Status:** `approved` — user approved 2026-09-17, both flagged judgment calls (C1 general-mechanism framing, C3/US-3 Must-level disclosure fix) confirmed as drafted, no changes requested.
- **Summary:** Six sites across five files hardcode the lens/characteristic vocabulary as closed lists instead of reading `lenses/README.md`'s registry, so a correctly-authored, correctly-registered lens (accessibility today, any future lens tomorrow) can be unreachable at `/charter` and undispatched at up to three phases without a human noticing.
- **Open:** `none` — two named assumptions in §3, both accepted, neither blocking.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for the framing decisions made in this draft.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Problem & Goal

- **Problem:** A lens can be fully authored and correctly registered in `lenses/README.md`, yet still silently fail to reach the agent that owns one or more of its phases, because six sites across five files encode the lens/characteristic vocabulary as closed, hand-maintained lists rather than reading it from the registry. `accessibility-lens` shipped with this gap disclosed as `refuted-with-finding` against its own NFR-6, at exactly these sites: `agents/facilitator.md:51-52` (the six-characteristic activation vocabulary `/charter` proposes) and `:67-69` (its characteristic→lens mapping, stopping at three lenses); `templates/constitution.md:27-28,35` (the same closed six shipped to every new project); `skills/look-and-feel/SKILL.md:34-35` (a closed 3-lens Design-dispatch list); `skills/demo-day/SKILL.md:84` (a closed 4-file QA-dispatch list); and `skills/peer-review/SKILL.md:50-51` (a generic head clause undercut by a closed 7-name parenthetical). Who hurts: any maintainer of an aSPARK-managed project who declares a characteristic-triggered lens — `must-be-accessible` today, whatever the roadmap's next characteristic-triggered lens picks tomorrow — discovers, only via a Reviewer/QA finding or not at all, that `/charter`'s own vocabulary never offered the characteristic and that two of five promised phases never fire. Workaround today: a diligent Facilitator who reads `lenses/README.md`'s tables directly, bypassing its own written instruction, still finds the lens (`evidence.md` F1's "not a Blocker" reasoning) — that is luck, not a workaround, since nothing tells the Facilitator to do it.
- **Goal:** any lens registered in `lenses/README.md` — present or future — is discoverable through the ordinary `/charter` path and dispatched at every phase its own frontmatter claims, with zero further edit to `agents/facilitator.md`, `templates/constitution.md`, or the three phase skills when a new lens is added.
- **Success signal:** re-reading each of the six sites' resolved instruction text finds a rule stated against the registry (or a lens's own frontmatter), not an enumerated name list — falsifiable: none of the six sites contains a hardcoded characteristic-name or lens-filename list after the fix. `README.md:302` and `lenses/README.md`'s "Adding a lens" §4 no longer assert the gap is open.
- **Why now:** this is a diagnosed, already-routed defect, not a new idea — `situational-lenses` Entry 3 predicted it verbatim before `accessibility-lens` confirmed it live at five files, and every future lens (the roadmap's next characteristic-triggered concern) repeats it until the mechanism, not the symptom, is fixed. The fix shape was already scoped by two review rounds and QA on the feature that found it (`.spark/accessibility-lens/evidence.md` T7+F1, `review.md` F1/F2/F3, `qa.md` NFR-6).

## 2. Target Users

- The **Facilitator agent**, running `/charter` on any project that should declare a characteristic-triggered lens — currently offers a vocabulary that stops at six names and a mapping that stops at three lenses.
- The **Designer, QA Tester and Reviewer agents**, who are supposed to receive every active lens's file at the phase it claims to own, and currently don't for lenses outside each skill's hardcoded list.
- **Future lens authors** (the roadmap's next characteristic-triggered lens) who rely on `lenses/README.md`'s "a new concern is a new file, nothing else" promise being literally true.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The exact lookup mechanism (each lens's `phases`/`triggers` frontmatter read directly at run time vs. re-deriving the same fact from `lenses/README.md`'s tables) is a Plan-phase design choice, not a Specify one. | Deliberately left open here — US-1/US-2's ACs fix the observable outcome (no hardcoded name list) and leave the mechanism to `/sprint-plan`. Not blocking. |
| A2 | Verifying the positive-firing case — an actual project with a characteristic-triggered lens active, actually reaching a previously-blind phase — has no live venue in this repo: aSPARK Core's own profile carries zero active characteristics (constitution §2). | Accepted, recorded `not-verified-live` by design, mirroring `accessibility-lens`'s own precedent (`qa.md` NFR-Provability). Not blocking — the negative case (this repo stays silent) is fully verifiable here and is the Must-level proof. |

## 4. User Stories

### US-1 (Must): Generic activation vocabulary at `/charter`

> As the Facilitator running `/charter`, I want the characteristic vocabulary I propose and the constitution template every project inherits to be sourced from `lenses/README.md`'s registry, so that a registered characteristic-triggered lens (present or future) is reachable through the ordinary `/charter` path without an edit to my own instructions.

**Acceptance criteria:**

- [ ] AC-1.1: Given `agents/facilitator.md`'s characteristic-activation vocabulary (today at `:51-52`), when read, it names a rule sourced from `lenses/README.md`'s Characteristics detection-signals table — currently 6 rows, `must-be-accessible` among them — rather than an enumerated list capped at six.
- [ ] AC-1.2: Given `agents/facilitator.md`'s characteristic→lens mapping (today at `:67-69`, stopping at `security`/`i18n`/`data`), when read, it names all characteristic-triggered lenses the registry currently lists (`security`, `i18n`, `data`, `accessibility`), not a subset.
- [ ] AC-1.3: Given `templates/constitution.md`'s Characteristics comment/example (today `:27-28,35`), when a new project is instantiated, the guidance points to `lenses/README.md`'s registry as the current, authoritative list rather than embedding a copy of the six characteristics that can go stale independently.
- [ ] AC-1.4: Given a future lens is added purely by following `lenses/README.md`'s existing "Adding a lens" steps 1–3 (new file, phase owners, registry-table rows), then no further edit to `agents/facilitator.md` or `templates/constitution.md` is required for `/charter` to be able to propose or accept its triggering characteristic — verified by re-reading both files' resolved text against the registry, since this repo ships no executable code to run.

### US-2 (Must): Generic phase dispatch in `/look-and-feel`, `/demo-day`, `/peer-review`

> As the Designer, QA Tester or Reviewer, I want the lens files passed to me to be computed from the constitution's active-lens list and each lens's own phase declaration, not a hardcoded name list in the skill that invokes me, so that every active lens claiming my phase actually reaches me without a skill edit when a new lens is added.

**Acceptance criteria:**

- [ ] AC-2.1: Given `skills/look-and-feel/SKILL.md` step 3 (today a closed list: `ux`, `seo`, `i18n`), when read, its instruction names every active lens whose declared phases include the design phase, not an enumerated subset.
- [ ] AC-2.2: Given `skills/demo-day/SKILL.md` step 2 (today a closed list: `ux.md`, `seo.md`, `security.md`, `i18n.md`), when read, its instruction names every active lens whose declared phases include the QA phase, not an enumerated subset.
- [ ] AC-2.3: Given `skills/peer-review/SKILL.md` step 2 (today a generic head clause undercut by a closed 7-name parenthetical), when read, its instruction names every active lens whose declared phases include the review phase — the parenthetical's membership list is removed or made non-restrictive, not merely re-counted.
- [ ] AC-2.4: Given `accessibility` (or any other lens currently shipped) is correctly declared active on a project (post US-1), when `/look-and-feel`, `/demo-day` and `/peer-review` are each run on that project, then the corresponding lens path is among what each skill passes to its agent — verified by re-reading each skill's resolved instruction text against the lens's own `phases` frontmatter, per this repo's established read-based verification method (constitution §8).

### US-3 (Must): Retire the stale disclosure

> As anyone reading `lenses/README.md`'s "Adding a lens" section or `README.md`'s live proof-state table, I want the known-exceptions caveat and the five/six-site gap to be updated once the mechanism is actually fixed, so I don't hand-edit files that no longer need editing or trust an "automatic" claim that used to be false.

**Acceptance criteria:**

- [ ] AC-3.1: Given US-1 and US-2 ship, when `lenses/README.md` §"Adding a lens" step 4 is read, its "known exceptions" paragraph (naming `/look-and-feel`, `/demo-day` and the `/charter` activation path as needing hand-edits) is rewritten to state they are now generic, or removed if nothing remains to caveat; the link to `.spark/accessibility-lens/evidence.md` is kept or repointed to this feature's own ledger, not silently dropped.
- [ ] AC-3.2: Given US-1 and US-2 ship, when `README.md:302`'s live proof-state row is read, it states the gap is closed (or names precisely which sub-case, if any, remains open) rather than continuing to assert five open sites that no longer are.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Performance | N/A — no runtime; every touched file is prompt-time instruction text (constitution §4) | — |
| NFR-2 | Security & privacy | N/A — no user input, no secrets, no network surface touched by this change | — |
| NFR-3 | Accessibility | N/A — this feature ships no UI of its own; it fixes the *mechanism* that dispatches the `accessibility` lens, not the lens's own UI-facing content (out of scope, §6) | — |
| NFR-4 | Reliability / scale | For every lens in `lenses/README.md`'s Available Lenses table whose frontmatter `phases` includes `design`, `qa` or `review`, the corresponding skill's resolved instruction names it — cross-checked against all lens files currently shipped (9 today), zero omissions | /peer-review |
| NFR-5 | Observability / ops | The disclosed gap stays honest after the fix: `README.md:302` and `lenses/README.md` §4 reflect the post-fix state (US-3), and this repo's own negative case — `library`-only profile, zero characteristics active — is re-run after the fix and still contributes zero accessibility (or any other off-lens) dispatch, mirroring `accessibility-lens`'s own T2/T9 method | /peer-review + evidence.md dry run |
| NFR-6 | Library (active lens — compatibility) | The fix is additive only to the consumed contract (constitution §3): no slash command, protected template heading/column/ID pattern renamed or removed; an already-instantiated consumer's own `.spark/constitution.md` is unaffected until that project's own next `/charter` run — the change lives in the plugin's skills/agents/templates, never in a consumer's instantiated artifact | /peer-review (library lens §2, compatibility/versioning) |

## 6. Out of Scope

- **`lenses/accessibility.md`'s own content or checklist.** Already authored, reviewed and shipped; this feature touches only how any lens gets discovered, activated and dispatched.
- **Correcting `.spark/constitution.md:16`'s stale lens count** in aSPARK's own constitution. Already routed to `/charter` (`accessibility-lens` evidence T9, Q3) — not duplicated here.
- **Generalizing the *type*-triggered vocabulary** (`website`/`web-app`/`api`/`cli`/`library`) in `agents/facilitator.md`'s inline type list or `templates/constitution.md`'s type comment. Not evidenced as defective — types are a small, rarely-growing enumeration by design (5, stable since inception), unlike characteristics, which have already grown once via this exact defect. Revisit only if a future type addition proves this wrong.
- **Any executable registry-lookup tool or script.** Constitution §3 forbids new tracked executable code; the fix must be expressed as instruction text an agent follows when reading files, never a program.
- **The `.spark/.guard/` untracked-ledger open question** (`review.md` Open Question 1). Unrelated to lens dispatch.
- **Authoring the roadmap's next characteristic-triggered lens.** This feature only removes the mechanism defect that would otherwise block it on arrival; it adds no new lens content.
- **GitHub branch protection, CI, or any release-process change.** Unrelated to this fix.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-17 | Frame this as an accessibility-specific patch, or as a general registry-mechanism fix that also future-proofs the roadmap's next characteristic-triggered lens? | General mechanism fix (US-1/US-2). Grounded in `evidence.md`'s own routed-fix language ("would make this and every future lens dispatch correctly without another skill edit") and `CLAUDE.md`'s add-a-file scope-check lesson, both already arguing for the generic form — not an assumption invented here. |
| C2 | 2026-09-17 | Should the *type*-triggered vocabulary (website/web-app/api/cli/library) be generalized in the same diff, since it shares the same closed-list shape? | No — moved to §6 Out of Scope. Not evidenced as broken by any cited finding; types are a materially smaller, more stable enumeration than characteristics. |
| C3 | 2026-09-17 | Should the stale disclosure (`README.md:302`, `lenses/README.md` §4) be corrected in this same diff? | Yes — Must (US-3). Constitution §4's docs-in-step bar and §1's honesty-about-maturity principle both require it; leaving a "still open" claim live after the gap closes is itself a defect. |
| C4 | 2026-09-17 | How is "dispatched" verified, given aSPARK ships no executable code and this repo's own profile carries zero active characteristics? | Read-based dry run against each site's resolved instruction text, per constitution §8's established QA method (a performed step is a real file read with its text quoted). The positive-firing case is recorded `not-verified-live` (§3 A2), not asserted. |
| C5 | 2026-09-17 | Is this a breaking change requiring a major version bump? | No — additive/minor. No protected template structure (constitution §3's contract table: `spec.md`, `plan.md`, `review-report.md`, `qa-report.md`, `release-notes.md`) is touched; `templates/constitution.md` is not in that protected set. NFR-6 states the compatibility bar for `/peer-review` to check against the diff. |

## 8. Design Review

<!-- N/A for this feature — no UI-facing surface; see SPEC GATE for the reasoned N/A. -->

- **Overall impression:**
- **Heuristics findings:**
- **Accessibility notes:**
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked
- [x] Open questions are resolved or explicitly accepted as risk (§3, both accepted)
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A, this repo ships no UI (constitution §4) and this feature is plumbing, not a rendered surface
- [x] Line budget respected: Ist 127 / Soll ~250 (excluding HTML comments)
- [x] Status set to `approved` by the user
