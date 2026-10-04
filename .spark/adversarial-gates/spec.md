# Spec: adversarial-gates

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-09-30 |
| **Ticket** | none |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Gates are prompt-enforced, so an agent can reason past one and a reviewer can grade too kindly. Two PRs, two minor version bumps: Increment 1 (grounded rebuttal rows only from `agent-evaded-gate` evidence, plus honest docs) ships alone first; Increment 2 (an always-active anti-generosity standard for review and demo-day) follows with its own gate. Dual review is parked.
- **Open:** `0 open` — unresolved rows in §3 Assumptions & Open Questions
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed since the last round and why
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

<!-- Related context only (not an import): GitHub issue #13 "Anti-rationalization tables at every gate", widened by two patterns from affaan-m/ECC (santa-loop dual review, gan-evaluator anti-generosity). -->

- **Problem:** aSPARK's gates are prompt-enforced. An agent under context pressure can reason around one ("I'll just…") and, from its own view, that reasoning is a passed gate. Reviewer and QA agents can also drift generous: round up a verdict, call a partial check clean. This is not hypothetical here: aSPARK's own trails record reviewers downgrading or correcting overstatements after the fact (`.spark/accessibility-lens/review.md:44` "downgraded from clean pass"; `.spark/project-kickoff/evidence.md:599` a fix row that "overstated what was actually written", caught only at round 2; `.spark/graph-gates/review.md:354` "byte-identical" was the overstatement). The pain is felt by the maintainer and by any user who trusts a green gate.
- **Tension, stated plainly:** `ROADMAP.md` (Next) sequences #13 *after* field reports because tables written from imagination list excuses no agent makes. The top open gap is that aSPARK is unproven on someone else's real project. The evidence that exists is in-repo: one author, mostly one model family, mostly reviewer-caught over-claims. It is real but **not field evidence**. The user has ruled for a narrow slice now (US-1, US-4), US-2 as the follow-on, and no dual review this cycle.
- **Goal:** each hardening is (a) grounded in a cited observation or clearly marked as not, (b) silent where it does not apply, (c) never a self-approving gate, (d) labelled at its true maturity.
- **Success signal:** (1) every shipped rebuttal row cites an observed trail location; a row with no citation is a defect. (2) In a replay of a recorded in-repo evasion, a fresh agent with the row present is observed to hold the gate where the same agent without it did not, recorded as an n=1 anecdote, not proof. (3) After the first external field report, the maintainer can add or delete rows from real rationalizations. Signal (3) is beyond this cycle and is stated so it is not mistaken for delivered.
- **Why this sequence:** US-1 + US-4 is the smallest slice that delivers value and it is honest even if the corpus yields nothing (US-4 still documents the state). US-2 is cheap, independent of the corpus, and addresses the more frequently observed failure (verdict over-claims), so it follows immediately, but it changes behavior for every consumer's reviews and so ships as its own PR, own version bump and own gate (C8).
- **If we never build this:** gates stay as fallible as today; a real cost, not an emergency.

## 2. Target Users

- **The aSPARK maintainer (solo, `a-lottes`)** who dogfoods every loop and is the only approver. Feels the pain when a gate passes on an over-claim.
- **A Claude Code user running the ten ceremonies on their own project** who reads a green gate as "checked". Feels it later, when the claim was wrong.
- Not targeted: users of other agent runtimes; anyone expecting code-level enforcement (that is optional sibling `aspark-guard`, out of Core).

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The user's phrasing was a solution set (tables, dual reviewer, anti-generosity prompt). Translated back to the need: stop gates being talked around and stop verdicts rounding up. Original phrasing kept in §1 context. | Assumption |
| A2 | In-repo trails (`.spark/*/{review,qa,evidence}.md`, ~50 files) contain enough observed evasions to ground a small corpus. Grep shows ≥3 clear instances, but most are verdict corrections, not "agent skipped a gate". With only `agent-evaded-gate` counting (C10), the chance that no gate reaches 2 is materially higher. Unverified until the corpus step runs. | Risk, accepted: if too few, AC-1.7 (refuted-with-finding), no table ships; Increment 1 is then docs plus corpus only |
| A3 | A corpus from the maintainer's own loops is representative of other users' agents. It probably is not. | Accepted (C4), only if labelled "in-repo, not field-validated" |
| A4 | Location of the US-2 standard file: `lenses/` is for situational lenses with activation rules; a new directory would itself be a pattern question under the constitution's "new concern = new file" rule. | Deferred to `/sprint-plan` (not decided here); see AC-2.5 |
| Q1 | Release cadence for the two increments. | Resolved (C8): two PRs, two minor bumps; Increment 1 ships alone first |
| Q2 | US-2 activation: always active or opt-in. | Resolved (C9): always active in every `/peer-review` and `/demo-day` run; stated in the README |
| Q3 | Which observation classes count toward a gate's ≥2 threshold. | Resolved (C10): only `agent-evaded-gate`; `verdict-rounded-up` is routed to US-2 |
| Q7 | Context-budget allowance for added lines. `docs/workflow.md` § *Context Budget* defines what each ceremony reads, with no numeric per-skill cap. | Resolved (C6): no hard cap exists; NFR-1 sets this feature's own cap; Plan re-checks |

## 4. User Stories

Sequence: **Increment 1 = US-1 + US-4**, one PR and one minor bump, independently shippable and valuable. **Increment 2 = US-2**, a second PR and second minor bump, starts after Increment 1 has shipped and gets its own gate. US-4's claims must be true at the moment each increment ships (see AC-4.1, AC-4.5, AC-4.6).

### US-1 (Must): Grounded rationalization rows at the gates that have evidence

> As the maintainer, I want short inline rebuttals only for rationalizations actually observed at a gate, so that agents are stopped where they really slip without tables of invented excuses training them to skim.

**Acceptance criteria:**

- [ ] AC-1.1: Given the committed trails under `.spark/*/{review,qa,evidence}.md`, when the corpus step runs, then a list is committed at `.spark/adversarial-gates/evidence.md` of observed gate-evasions or over-claims, each with a verbatim quote, `file:line`, the ceremony gate it occurred at, and a class of `agent-evaded-gate`, `verdict-rounded-up` or `other`. The count per class and per gate is stated.
- [ ] AC-1.2: Given that list, when a skill's gate has fewer than 2 `agent-evaded-gate` observations (the only class that counts; `verdict-rounded-up` and `other` never count toward the threshold, C10), then its `SKILL.md` gains no table and no mention. A `git diff` of that skill is empty.
- [ ] AC-1.3: Given a gate with ≥2 `agent-evaded-gate` observations, when its table is added, then it has at most 5 rows, each row is `excuse | rebuttal`, the rebuttal is written inline (not "see elsewhere"), each row carries a citation to the corpus entry it derives from, and the table is labelled "in-repo, not field-validated".
- [ ] AC-1.4: Given any row, when a reader looks for its source, then a row with no corpus citation is a review finding of at least Major severity.
- [ ] AC-1.5: Given negative-case-first, when every skill without a table is compared to its pre-change state, then the diff is empty (AC-1.2), and one recorded dry run of an uncovered ceremony behaves as before.
- [ ] AC-1.6: Given the positive case, when one recorded in-repo evasion is replayed against a fresh agent, once without and once with the row, then both outcomes are written down verbatim and labelled an n=1 anecdote, not proof the table works.
- [ ] AC-1.7: Given zero qualifying gates (A2 fails), when the corpus step finishes, then no table ships, the corpus is committed as evidence, and the outcome is recorded as refuted-with-finding (per `CLAUDE.md`); US-4 still ships and states this outcome.
- [ ] AC-1.8: Given corpus entries classed `verdict-rounded-up`, when the corpus is committed, then they are kept in `.spark/adversarial-gates/evidence.md` and flagged as input for US-2 (Increment 2); they produce no row in any `SKILL.md` in Increment 1.

### US-4 (Must): Honest maturity in the docs

> As a user reading the README and ROADMAP, I want to see which hardening exists, what it is grounded in and that it is unproven in the field, so that I do not read a prompt-level defence as an enforced guarantee.

**Acceptance criteria:**

- [ ] AC-4.1: Given the README entry and the `ROADMAP.md` line for #13, when an increment ships, then each states exactly what has shipped so far (rows at N gates or none, anti-generosity standard or not), that grounding is in-repo trails and not field reports, and that effectiveness is unmeasured. Nothing unshipped is described as delivered.
- [ ] AC-4.2: Given the `ROADMAP.md` Next entry for #13, when Increment 1 ships, then it is updated in step (moved, split or reworded) and does not contradict the new state; the anti-generosity standard remains listed as planned, not delivered.
- [ ] AC-4.3: Given any statement about enforcement, when read, then it says the gates remain prompt-enforced and that code-level enforcement is the optional sibling's concern.
- [ ] AC-4.4: Given dual review is parked, when the docs mention it, then it appears only as not built, with the re-open condition from §6.
- [ ] AC-4.5: Given the Increment 1 PR, when the README, `ROADMAP.md` and any other doc touched are read at that PR's head, then they claim only: rebuttal rows at N gates (or none, per AC-1.7), evidence-grounded in-repo, unmeasured, gates still prompt-enforced. They do not describe the anti-generosity standard as shipped or active, and they do not claim any change to review or demo-day verdict behavior.
- [ ] AC-4.6: Given the Increment 2 PR, when the same docs are read at that PR's head, then the README states that the anti-generosity standard is always active in every `/peer-review` and `/demo-day` run, that this changes verdict behavior for already-installed projects (stricter verdicts, partial checks recorded as `not-verified-live`), and that it is unmeasured; the `ROADMAP.md` line for #13 is updated to match. Increment 1's claims remain true.

### US-2 (Should): Explicit anti-generosity standard for verdicts

> As the maintainer, I want the evaluating agents to name their own tendency to be generous and grade against objective PASS/FAIL criteria, so that a verdict cannot round up.

Ships as Increment 2 (its own PR, minor bump and gate). Always active (C9).

**Acceptance criteria:**

- [ ] AC-2.1: Given a review or QA run with the standard active, when the verdict is written, then the standard states the agent's known tendency toward generosity and bans an exact, short list of concession phrases (for example "solid foundation", "overall good effort") in verdict text.
- [ ] AC-2.2: Given each rubric item, when the agent grades it, then the item is binary PASS/FAIL with the observable that decides it. "Mostly" and "partially" are not verdicts. A partial check is recorded under the existing `not-verified-live` status, never as PASS.
- [ ] AC-2.3: Given a check done only statically or by reading, when the verdict is written, then the report states which evaluation mode was actually available and that the result is degraded (constitution §8 "performed step" rule).
- [ ] AC-2.4: Given an agent has found an issue, when it writes the verdict, then it does not withdraw or downgrade the finding without a recorded, cited reason. Effort and potential earn no credit.
- [ ] AC-2.5: Given the delivery shape (ruling C2), when the diff is checked, then the standard is one file of at most ~40 lines that the `/peer-review` and `/demo-day` skills pass to the agents, analogous to lens paths; no file under `agents/` changed and no `/charter` amendment was needed. Its location (existing `lenses/` or a new directory) is decided at `/sprint-plan`, which records the pattern question if a new directory is proposed.
- [ ] AC-2.6: Given the delivery shape, when dispatch is checked, then every phase that claims the standard (review, QA) is verified at plan time for both dispatch and how it is activated, not only the phase already wired generically.
- [ ] AC-2.7: Given `templates/review-report.md` and `templates/qa-report.md`, when the diff is checked, then protected headings, columns and ID patterns (constitution §3) are unrenamed and unremoved; any addition is an appended column or section.
- [ ] AC-2.8: Given any `/peer-review` or `/demo-day` run in a project with no activation setting for the standard, when the skill dispatches, then the standard is passed to the agent unconditionally (no constitution opt-in, no opt-out flag), and the run's report names that it applied. A run where it was not passed is a review finding.
- [ ] AC-2.9: Given the `verdict-rounded-up` entries from Increment 1's corpus (AC-1.8), when the standard is written, then each rule or banned phrase that derives from an observation cites its corpus entry; any element without a citation is labelled "not grounded in the corpus".

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Attention budget | Each table has ≤5 rows; total added lines per touched `SKILL.md` ≤ 12 (this feature's own cap; `docs/workflow.md` § Context Budget has no numeric cap); a skill with no qualifying evidence is byte-identical. The US-2 standard file is ≤ ~40 lines. Plan re-checks against the contract. | /peer-review by `git diff --stat` |
| NFR-2 | Suppression | Docs and plan name where each item activates and where it stays silent (uncovered gates; ceremonies other than review/QA for US-2). | /peer-review |
| NFR-3 | Library: public surface | No slash command renamed or removed; no `skills/*/SKILL.md` frontmatter `name` changed; `${CLAUDE_PLUGIN_ROOT}` paths only. | /peer-review |
| NFR-4 | Library: compatibility | Protected template structures (§3) unchanged; only appended content. Each increment is additive and gets its own **minor** bump in `plugin.json` (two PRs, two bumps, C8). Increment 1: already-installed consumer projects run every uncovered ceremony unchanged. Increment 2: the standard is always active (C9), so it is a deliberate verdict-behavior change for installed consumers, stated in the README (AC-4.6) and not hidden behind a patch-looking release. | /peer-review + recorded dry run |
| NFR-5 | Library: contract clarity | README documents what each shipped piece does, where it applies, and its degraded behavior (evaluation mode degraded), per increment as it ships. | /peer-review |
| NFR-6 | Constitution: stack | Zero new tracked executable code; `git ls-files '*.py'` still empty; no runtime dependency; `claude plugin validate` passes. | /peer-review |
| NFR-7 | Traceability | Existing US/AC/NFR/T/F IDs never renumbered; review and QA trails cite the new IDs. | /peer-review |
| NFR-8 | Observability | No claim that a rebuttal "fires" without a recorded replay; docs say fired-ness is not testable in Core. | /peer-review |
| NFR-9 | Security & privacy | N/A — `security` lens off; corpus quotes come from already-public `.spark/` and add no customer material. | /peer-review |
| NFR-10 | Accessibility / performance | N/A — no UI or runtime (constitution §4); agent attention is covered by NFR-1. | — |

Active lens `library` (constitution): public surface, compatibility and contract clarity are covered by NFR-3, NFR-4, NFR-5; its packaging section is N/A (no bundle, no dependencies).

## 6. Out of Scope

- **Dual/independent second review (former US-3): Won't this cycle.** Reasons: no observed case in the trails where a second reviewer would have caught what a single reviewer missed (all cited misses were caught by the same reviewer at a later round); it is the costliest idea (extra agent per gate, provider-independence question, disclosure-vs-silence tension with constitution §6). Re-open only on a new argument or observation, for example a recorded single-reviewer miss. Parked reference: ECC `santa-loop` pattern (affaan-m/ECC).
- Tables in all ten skills. Only gates with ≥2 cited `agent-evaded-gate` observations.
- Rows built from `verdict-rounded-up` or `other` evidence; that evidence goes to US-2 only.
- An opt-in or opt-out switch for the US-2 standard (always active, C9), and releasing both increments in one PR or one version bump (C8).
- Rows written from imagination, or copied from ECC or another project's list without an in-repo citation.
- Any code, script, hook or CLI to enforce round caps, table firing or independence. That is optional `aspark-guard`, not Core.
- A hard dependency on any external model, provider or CLI.
- A reviewer verdict that sets `approved`, closes a waiver, or authorizes a release.
- Editing `agents/reviewer.md` or `agents/qa-tester.md`, or amending the constitution (§3 "new concern = new file" is honored, C2).
- Renaming, removing or reordering any protected template heading or column.
- Any effectiveness claim ("reduces rationalization by X%"). No baseline exists; measuring needs field data.
- Applying the anti-generosity standard to Specify, Plan, Act or any ceremony other than review and QA.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-30 | Ordering: narrow slice, defer all, or all at once? | Narrow slice now: US-1 + US-4 first; US-2 follows as Increment 2; not deferred, not all-at-once. US-1 and US-4 stay Must, US-2 Should |
| C2 | 2026-09-30 | Role edits vs constitution §3 for anti-generosity wording? | Standard file, no role edits, no `/charter` amendment: one file (≤ ~40 lines) that skills pass to agents, like lenses. Location flagged for `/sprint-plan` (A4); becomes AC-2.5, AC-2.6 |
| C3 | 2026-09-30 | Dual review (US-3) in this cycle? | Won't. Moved to §6 with reasoning and re-open condition; the disclosure-vs-silence and one-provider questions became moot with it |
| C4 | 2026-09-30 | Is an in-repo corpus acceptable grounding? | Accepted, labelled "in-repo, not field-validated". Only gates with ≥2 observations get a table; too few is refuted-with-finding, no table (AC-1.3, AC-1.7) |
| C5 | 2026-09-30 | Constitution conflicts (§3 roles; §6 optional-degrades for dual review)? | Both dissolved: no role edits, and dual review is out of scope. No open conflict remains |
| C6 | 2026-09-30 | Context-budget allowance (Q7)? | No numeric cap exists in `docs/workflow.md` § Context Budget; NFR-1 sets this feature's own cap and Plan re-checks |
| C7 | 2026-09-30 | Clarify pass over the reordered draft (functional boundaries, data, permissions, error cases, NFRs, integrations, UX states, out of scope) | Permissions: the user remains sole approver (AC-2.4, §6). Data: corpus at `.spark/adversarial-gates/evidence.md`, public and quote-only. Integrations and UX states: none (no dependency, no UI). Errors: empty corpus is AC-1.7. Remaining ambiguities were Q1 to Q3, resolved in C8 to C10 |
| C8 | 2026-09-30 | Q1: release cadence of the two increments? | Two PRs, two minor version bumps. Increment 1 (US-1 + US-4) ships alone first; Increment 2 (US-2) follows with its own gate. Folded into §4 sequence, NFR-4, US-4 per-increment ACs (AC-4.5, AC-4.6), §6 |
| C9 | 2026-09-30 | Q2: US-2 activation? | Always active in every `/peer-review` and `/demo-day` run, no opt-in. It is a behavior change for installed consumers and must be stated in the README; minor bump. Folded into AC-2.8, AC-4.6, NFR-4, §6 |
| C10 | 2026-09-30 | Q3: which classes count toward a gate's ≥2 threshold? | Only `agent-evaded-gate`. `verdict-rounded-up` evidence is routed to US-2 only (AC-1.8, AC-2.9). Consequence accepted: US-1 may yield few or no tables (A2, AC-1.7) |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

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
- [x] Clarify pass done: no ambiguity left unresolved or unparked (Q1 to Q3 resolved as C8 to C10; A2 and A4 parked as accepted risk / deferred to Plan)
- [x] Open questions are resolved or explicitly accepted as risk
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions (C2, C5: no conflict remains)
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A: no UI
- [x] Line budget respected: Ist 168 / Soll ~250 (excluding HTML comments; 170 raw lines) — self-reported
- [x] Status set to `approved` by the user
