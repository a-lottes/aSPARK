# Spec: right-sizing

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-29 |
| **Ticket** | `none` (constitution §7) |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). **Approved by the user at the spec gate, 2026-08-29**, together with A7's confirmation; **amended and re-approved 2026-08-29** (AC-1.7, NFR-4, NFR-2 — see C17); **amended and re-approved 2026-08-31** (AC-1.3, NFR-4 narrowed to ordinary invocation — see C18); **amended and re-approved a fourth time, 2026-08-31** (AC-1.3, NFR-4 re-scoped from a content-suppression claim to an action-based no-ask/no-error/no-warning/no-re-negotiation guarantee, after `/demo-day` round 5 disproved C18's narrowing on its own narrowest terms — see C19). Next ceremony step: `/increment`, to make the re-scoped guarantee hold in `agents/qa-tester.md` and the other declaration-reading files, then `/demo-day` for a fresh test of AC-1.3/NFR-4 — covering both ordinary invocation and an explicit narration demand — before B1/B4 can move off `open`.
- **Open:** `1` — **AC-1.3 and NFR-4 are not met until `agents/qa-tester.md` (and any other declaration-reading file) actually holds the re-scoped guarantee — no error, no warning, no asking the user to choose/confirm/supply a method, no re-negotiation of whether the ceremony should be overridden — confirmed by a fresh `/demo-day` round covering both ordinary and narration-demanding invocation** (C19, superseding C18). F15/AC-1.7 closed (`22673c8`, `qa.md` §2). A7 confirmed at the gate (AC-1.10 stands: `/charter` only). NFR-4 carries the same open item until the same fresh run.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed and why.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** Ceremony cost does not move with the change. Measured directly in
  this repo (line counts, 2026-08-29): `handbook-maturity` **1,012** `.spark/`
  lines for a 14-line product change; `lean-artifacts` **1,029** for 137;
  `lean-rounds` **1,045** for 201. A constant floor of ~1,030 lines, whatever
  ships. But the *causes* are mostly not size:
  1. **Ceremonies fire where they cannot apply.** `/demo-day` needs a browser;
     this repo has no UI (constitution §2). It was cancelled outright in
     `lean-rounds` (no `qa.md` exists; `release.md:24` records "N/A / user
     override") and redefined by documented override in `handbook-maturity`
     (`qa.md:17`, "the override method") and again in `graph-gates-verification`.
     Three features, three re-negotiations of the same standing fact.
     Constitution §1 names this exact failure: *"a check that fires where it
     doesn't apply trains users and agents to skim, which erodes trust in every
     other check."*
  2. **The same fact is derived three times.** Reported for
     `graph-gates-verification`: seven load-bearing counts derived from raw
     transcripts by `/increment`, re-derived by `/peer-review` r1, again by r2
     (justified — verifying fixes), and a third time by `/demo-day`, which found
     one Minor. Nothing in the loop says "cite the predecessor instead".
  3. **Artifacts record the session, not the product** — permission-classifier
     blocks, auto-mode denials. Deferred, evidence intact (§6).
  4. **Third-order findings** — five of eleven `/peer-review` r1 findings on
     `graph-gates-verification` concerned citation accuracy *inside* the evidence
     document. Partly addressed by AC-2.4; the rest deferred (§6).
  5. **The budget ruler doesn't move.** `lean-rounds` US-4 shipped an Ist/Soll
     gate item and it is reported honestly (`lean-rounds/review.md:149` Ist 150 /
     Soll ~150; `release.md:77` Ist 87 / Soll ~100). The defect is not dishonesty
     — it is that a 14-line change is measured against an M feature's ruler.
     Deferred, evidence intact (§6).
  Who feels it: the sole maintainer running `/spark` on this repo. That is the
  only *measured* user (A2).
- **Goal:** Stop paying twice for things the project already knows. A QA method
  the profile settles once is declared once, not re-negotiated per feature; a
  fact a predecessor established and cited is cited, not re-derived from raw
  sources. **The floor that never moves:** every gate still runs, every gate item
  is still answered by its owner, every Must AC is still verified, the ID chain
  stays intact, and the user is still the only approver.
- **Success signal** — two countable behaviours in the next feature's loop:
  (S1) its `release.md` §1 QA row cites the constitution as a standing project
  fact, and the session transcript contains **zero** per-feature negotiation of
  the QA method; (S2) in its `review.md`/`qa.md`, the count of facts re-derived
  from raw sources **without** a named AC-2.2 condition is **zero**.
- **What this half does not reach — stated so the spec claims no more than it
  delivers.** No `.spark/` line-volume target is claimed. The two levers that
  would move volume (US-3 session noise, US-4 the size-scaled ruler) are deferred
  (§6), and `evidence.md` — **395 / 369 / 203** lines in the last three features,
  **20–38%** of each feature's ceremony total — is out of this feature's reach
  entirely, routed to `/charter` (§6, A4). What US-1 saves is a recurring
  negotiation; what US-2 saves is agent attention, not lines.
- **Why now:** The same override has recurred three times, and `lean-rounds`'
  own `release.md:67` already recorded the learning — *"offer the ceremony-override
  QA method as the default before an outright skip on non-UI features"* — which
  was never actioned. A learning recorded and not acted on is the loop failing
  its own Keep phase, which is a sharper argument than cost.

**Recorded as evidence, not as irony:** this spec was itself halved at its own
gate, from four stories to two (C8) — the same suppression it argues for,
applied to itself before it shipped.

## 2. Target Users

- **The sole maintainer of aSPARK Core** running `/spark` on this repo — every
  `.spark/` directory here is his, and the whole measurement is his cost.
- **The `qa-tester` agent + `/demo-day`** invoked on a project with no
  browser-observable surface: today it must stop ("never substitute code reading
  for testing", `skills/demo-day/SKILL.md:30`) or be overridden by hand.
- **The `reviewer` agent on round 2+ and the `qa-tester` on re-test** — both
  re-derive from raw sources what a predecessor artifact already cited.
- **Any future consumer with a `library` / `api` / `cli` profile.** Same need,
  **unproven**: aSPARK has never run a full loop on someone else's project
  (`ROADMAP.md`, "the one gap that matters most").

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived as a solution: *"die SPARK-Schleife soll ihr eigenes Zeremoniegewicht an die Größe der Änderung anpassen"* (the SPARK loop should adapt its own ceremony weight to the size of the change). Recorded verbatim per the no-solutions rule. PO recommendation was to decline the tier mechanism — four of five measured causes are size-independent. | **Resolved (C8):** reframe accepted by the user at half size. Tier framing stays declined |
| A2 | The measurement generalizes poorly: n=3 features, one repo, Markdown-only, where a 14-line product change is *legitimately* XS. On an app repo, ~1,000 ceremony lines against a 600-line feature is not obviously waste. | **Accepted risk**, bounded by NFR-5: no claim of a general saving may ship |
| A3 | **Anti-gaming**, for any future size work: a declared size may bind bookkeeping volume only. | **Resolved (C9):** confirmed by the user as a binding ruling; carried into §6's US-4 deferral so it is inherited, not re-litigated |
| A4 | `evidence.md` is 20–38% of each feature's ceremony total and has no template, no budget and no gate (`lean-artifacts` §6 put non-template artifacts out of scope). | **Resolved (C10):** capped via `/charter` in this repo's own constitution, not in Core. Explicitly **outside this feature's reach** — stated in §1 so no larger effect is implied |
| A5 | No existing constitution has a QA-method declaration, so the field must be optional with a stated default and old projects must behave unchanged. Precedent verified: constitution §7 (`tracker-handoff`) already carries "Default when absent" per field; `lean-artifacts` AC-1.5 and `lean-rounds` AC-3.4 are the artifact-side precedents. | **Resolved by design** — NFR-1, NFR-4, AC-1.3, AC-2.5 |
| A6 | Issue [#25](https://github.com/a-lottes/aSPARK/issues/25) proposes an optional size field. | **Resolved (C12):** its vocabulary (`XS \| S \| M \| L \| XL \| unknown`) is settled prior art for whenever US-4 is built; #25 stays open and separate, since US-4 left this feature |
| A7 | **PO ruling from the Clarify pass, not a user decision:** only `/charter` (Facilitator drafts, user confirms) may create or amend the QA-method declaration — no phase agent may write it mid-loop (AC-1.10). Rationale: an agent that could declare its own gate inapplicable is the anti-rationalization risk [#13](https://github.com/a-lottes/aSPARK/issues/13) names, arriving through the front door. | **Confirmed by the user at the spec gate, 2026-08-29** — AC-1.10 stands as written; the cost (leaving the loop to amend the declaration mid-feature) was named and accepted |

## 4. User Stories

<!-- IDs US-3, US-4 and AC-3.x / AC-4.x were used by the two stories deferred in §6. They are
     retired, not free: no new story or AC in this feature may reuse them (constitution §4,
     traceability — IDs are never renumbered or recycled). -->

### US-1 (Must): A project with no browser surface declares its QA method once

> As the maintainer of a project with no browser-observable surface, I want that
> project's QA method declared once in the constitution, so that I stop
> re-negotiating the same override on every feature.

**Acceptance criteria:**

- [ ] AC-1.1: Given a constitution declaring that this project has no browser-observable surface and naming the substitute verification method, when the loop reaches the QA phase, then `/demo-day` proceeds by the declared method without asking the user for a per-feature override.
- [ ] AC-1.2: Given that declaration, when QA runs, then `qa.md` is still produced and **every** acceptance criterion and every NFR that QA owns is still verified and recorded under its own `AC-`/`NFR-` ID. The declaration changes the *method*, never whether verification happens or how much of it does.
- [ ] AC-1.3: Given a project whose constitution carries no such declaration, or no constitution at all, when `/demo-day` runs, then it proceeds exactly as today: no error, no warning, no asking the user to choose, confirm or supply a substitute QA method, and no re-negotiation of whether this project's ceremony should be overridden — the exact recurring ask US-1 exists to retire (`evidence.md` Entry 2). **Not a violation:** the agent's own live reply stating, in its own words, that no declaration applies before it proceeds by default; `qa.md` §1 documenting the same fact, symmetric with how the declared path already documents its method (AC-1.4). **Discouraged, capped at Minor, never a Blocker alone (by the same proportionality as AC-2.4):** the live reply gratuitously quoting the declaration's raw field values verbatim rather than describing the outcome in its own words. **Re-scoped from a content-suppression claim ("no mention, ever", then "no mention, under ordinary invocation") to this action-based one; supersedes C18's ordinary-invocation carve-out, which this narrower claim no longer needs — see C19.** Unconditional: holds at every invocation, including one where the caller explicitly demands full narration of internal reasoning.
- [ ] AC-1.4: Given a declared method, when `/go-live` writes `release.md` §1, then the QA row cites the constitution as a standing project fact — not as a per-feature user override, and never as a silently skipped check.
- [ ] AC-1.5: Given a project that *does* have a browser surface, then nothing about `/demo-day` changes, and no declaration or profile value can suppress the live-browser requirement there.
- [ ] AC-1.6: Given a declaration naming a method the session cannot actually perform, when the phase starts, then it stops and says so — a declaration is a route, never a licence to skip.
- [ ] AC-1.7: Given the shipped diff, when it is read, then the declaration is **specific to the browser/QA case**: it provides no generic mechanism to declare any other ceremony inapplicable, and at no value of it is any ceremony skipped, softened, merged or given an off switch (C11 — the generic-mechanism fence, as adjudicated at the plan gate, 2026-08-29). `/story-time`, `/look-and-feel`, `/sprint-plan`, `/increment` and `/peer-review` behave exactly as today **at every value of this declaration** — that is what this AC governs. (`/peer-review`'s reviewer *is* in this diff, for US-2's citation rule; that is a separate story, driven by no declaration value, and a grep of `agents/reviewer.md` for declaration references returns zero.) **Exactly two ceremonies have exactly one stated difference each, and every shipped file that repeats this list carries both:** `/go-live` runs every check it runs today and only *words* the §1 QA row differently (AC-1.4), and `/spark` runs every step it runs today and only stops asking for a start command, URL and browser tooling, naming the declared method instead (C17). Apart from `/demo-day`, whose method is this feature's whole point (AC-1.1), and `/charter`, its sole writer (AC-1.10, NFR-4), no ceremony behaves differently at any value.
- [ ] AC-1.8: Given the profile in constitution §2 (no `website`, no `web-app`), when `/charter` runs, then the declaration is still an **explicit** entry the user confirms — never inferred silently from lens state, so a mis-typed profile can never suppress QA on its own.
- [ ] AC-1.9: Given a declaration that is present but incomplete (no method named, or an empty value), when the QA phase starts, then behaviour falls back to today's — ask the user — and never to suppression. Ambiguity resolves toward more verification, never less.
- [ ] AC-1.10: Given any ceremony other than `/charter`, when it runs, then it may neither create nor amend the declaration; a phase that believes the declaration is wrong stops and points to `/charter` (A7).

### US-2 (Must): A fact a predecessor established is cited, not re-derived

> As a phase that needs a fact an earlier artifact already derived and cited, I
> want to cite it instead of re-deriving it from raw sources, so that the loop
> stops paying three times for one answer.

**Acceptance criteria:**

- [ ] AC-2.1: Given a fact a predecessor artifact states with a `file:line` or transcript citation, when a later phase needs the same fact, then it cites artifact + ID and does not re-derive it — unless a condition in AC-2.2 holds.
- [ ] AC-2.2: Given the rule, when the instructions are read end to end, then they name the conditions that **require** re-derivation, at minimum: (a) the round is verifying a fix to that very fact, (b) the fact is a Must AC's verification, (c) the predecessor marked it assumed/unverified, (d) the reader has a concrete reason to doubt it. The rule is bounded reading, never "never verify".
- [ ] AC-2.3: Given a re-derivation performed under AC-2.2, when it is written up, then the artifact names which condition triggered it — so a reader can tell a required re-check from a redundant one.
- [ ] AC-2.4: Given a finding that concerns only wording, citation formatting or timestamps *inside* a `.spark/` artifact, and that changes no verdict, no gate answer and no Must AC, then its severity is at most `Minor` and it never blocks a gate.
- [ ] AC-2.5: Given an artifact written before this change, when any ceremony reads it, then nothing differs from today — no migration, no rewrite, no warning.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | Covers | How it's verified |
|---|---|---|---|---|
| NFR-1 | Compatibility & versioning (library lens §2) | Purely additive. No protected heading, column or ID pattern (constitution §3) is renamed, removed or reordered, and no new row is added to any *parsed* artifact — the only new field lives in `templates/constitution.md`, which constitution §3 does not list and `aspark-graph` never parses. `qa.md` is still produced (AC-1.2), so `_parse_qa` sees exactly what it sees today. **Minor** bump; no coordinated release with `aspark-graph`. | US-1 | `/peer-review` + static walkthrough of `artifacts.py` (method established by `lean-artifacts` C9 / `lean-rounds` C7) |
| NFR-2 | Public surface (library lens §1) | Zero new slash commands, agents, lenses or template *files*. The whole added surface, enumerated line by line in the release notes: one optional constitution declaration (QA method only), and the reading/writing rules in `/demo-day`, `/go-live`, `/charter`, `qa-tester.md`, `reviewer.md` and `/spark` (added by the plan-gate ruling of 2026-08-29, one conditional clause in step 2). A generic "declare any ceremony away" field, or any new template file, makes this a different feature (AC-1.7). | US-1, US-2 | `/peer-review` |
| NFR-3 | Contract clarity (library lens §4) | Each touched template and agent file states, where its writer meets it: what the declaration does **not** do (AC-1.2), that it is browser/QA-specific (AC-1.7), that only `/charter` may write it (AC-1.10), and which conditions force re-derivation (AC-2.2). A reader needs no external doc to use either rule correctly. | US-1, US-2 | `/peer-review` |
| NFR-4 | Degrade to silence (constitution §6) | Absent constitution, absent declaration, incomplete declaration, old-shape artifact: every ceremony that reads the declaration behaves exactly as today, including whatever ordinary ask that flow already made before this feature (AC-1.6, AC-1.9) — and, unconditionally, at every invocation including one where the caller demands full narration of internal reasoning: no error, no warning, no asking the user to choose, confirm or supply a substitute method, no re-negotiation of whether the ceremony should be overridden. **Not a violation:** stating, in the agent's own words — in its live reply or in `qa.md` §1, symmetric with the declared path's own documentation (AC-1.4) — that no declaration applies. **Discouraged, capped at Minor, never a Blocker alone:** a live reply gratuitously quoting the declaration's raw field values verbatim. **One exemption:** `/charter`, the ceremony that *writes* it, asks the QA-method question on every project, declared or not (AC-1.8) — leaving it undeclared is a valid answer and returns every reading ceremony to today's path unchanged. **Re-scoped (C19), superseding C18's ordinary-invocation carve-out** — the mechanism that carve-out guarded against (irrepressible content disclosure under an explicit reveal-everything demand) does not bear on this action-based claim, so it is not carried forward; see C19. | US-1, US-2 | documented dogfood/dry run in a repo without the field, plus a fresh `/demo-day` round testing both ordinary and narration-demanding invocation (C19) |
| NFR-5 | Honesty of claim (constitution §4) | The release notes claim **only** S1 and S2 from §1. They must not claim a line, token or dollar saving, must not imply this reaches `evidence.md`'s 20–38%, and must not claim the result generalizes to other projects (A2). | US-1, US-2 | `/peer-review` against §1's "does not reach" paragraph |
| NFR-6 | Gate integrity (constitution §6) | Before and after this change, at every profile and every declaration value: the number of gates and of gate items per gate is **identical**, each is answered by its own owner, and `approved` / waivers / the release go remain the user's. | US-1 | `/peer-review` diffing all six gate checklists + the dogfood run |

Not applicable, each with its reason: **Performance / Accessibility** — no runtime
and no UI (constitution §4). **Security** — lens off; no runtime, no data, no
network surface. **Roles & permissions** — Markdown in a git repo, no authz
surface; the *authority* question (who may write the declaration) is a functional
AC, not a permission model — AC-1.10. **Library lens §3 (packaging & footprint)**
— no bundle, no dependencies (constitution §2). **UX flows & states** — no UI; the
human analogue is what the user is asked and when, carried by AC-1.1 (not asked),
AC-1.6/AC-1.9 (asked anyway when the route fails) and AC-1.4 (told afterwards).

## 6. Out of Scope

**Deferred, not rejected** — the measured evidence for both stands, and either
could be its own later feature:

- **US-3, session noise in artifacts** (§1.3). Artifacts record permission-classifier
  blocks and auto-mode denials — worthless in six months and permanently public
  (constitution §5). Cut only to keep this feature at half size (C8).
- **US-4, the size-scaled budget ruler** (§1.5). Cut with the tier framing, but
  the sound half survives as prior art. Whoever builds it **inherits two settled
  rulings** and must not re-litigate them: (a) *the binding safety property* (C9)
  — a declared size may bind bookkeeping volume only, and can never add, remove,
  merge, reorder, shorten in count or soften any gate, gate item, phase, agent,
  artifact or approval; under-declaring buys a shorter artifact, never a skipped
  check; and (b) *the vocabulary* (C12) — issue #25's `XS | S | M | L | XL |
  unknown` verbatim, with `unknown` so a missing size reads as "not stated", never
  silently as "small".

**Cut outright:**

- **Size tiers that drive which ceremonies run, or how deeply a phase reviews or
  tests.** Declined and confirmed (C8): four of five measured causes are
  size-independent.
- **A generic "declare any ceremony inapplicable" mechanism.** More useful and
  more dangerous; the user chose the narrow version (C11). Generalising it later
  requires a **second, genuinely different case** to appear first — evidence
  before mechanism, same bar `ROADMAP.md` sets for the anti-rationalization
  tables.
- **Merging phases** (e.g. review+QA in one pass). It collapses the separation of
  duties `docs/workflow.md:160` calls "the point": the reviewer who waives their
  own finding reviews nothing.
- **Skipping any gate, dropping any gate item, or sampling acceptance criteria.**
  NFR-6 is the fence.
- **Capping `evidence.md`** — the largest single line item (20–38%). A repo-local
  convention (`CONTRIBUTING.md:60`), not Core surface, so capping it belongs in
  *this repo's* constitution: a named `/charter` follow-up, not this diff (C10).
- **Any linter, hook or validator** (constitution §3 forbids a toolchain, §4 has
  no test suite).
- **Migrating existing `.spark/` directories.** AC-1.3 and AC-2.5 are the
  safeguards.
- **Nested `claude -p` session cost during `/increment`.** Session mechanics, not
  shipped surface.
- **Reopening `lean-rounds`' overwrite-in-place mechanics or its budget numbers.**

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-29 | Is the measured waste actually caused by change size? | **No, mostly not** (PO finding, §1.1–1.5). Four of five causes are size-independent — the finding that reframed the feature |
| C2 | 2026-08-29 | Does lighter ceremony mean lower quality, or only less paperwork? | **Only less paperwork** (PO ruling), made falsifiable by AC-1.2 (method may change, coverage may not) and NFR-6 (gate count identical before and after) |
| C3 | 2026-08-29 | What must never scale down? | **PO ruling:** constitution §6 in full, "the user is the only approver", every gate and gate item, every Must AC's verification, and the `US-`/`AC-`/`NFR-`/`T`/`F` chain. Floor, not dial — NFR-6 |
| C4 | 2026-08-29 | Is the recurring `/demo-day` override a per-feature decision or a project fact? | **A project fact** (PO ruling). Constant across features; constitution §7 (`tracker-handoff`) is the working precedent for an optional per-project declaration defaulting to today's behaviour |
| C5 | 2026-08-29 | Is the line-budget gate "never biting", as the idea assumed? | **Refuted, in part** (PO finding). `lean-rounds/review.md:149` Ist 150 / Soll ~150 and `release.md:77` Ist 87 / Soll ~100 are at or under budget, honestly reported. The defect is a ruler that doesn't move — which is US-4's ground, now deferred |
| C6 | 2026-08-29 | Who declares the size, and what stops "everything is XS"? | Superseded by C9 once US-4 was deferred; the safety property survives as a binding ruling regardless |
| C7 | 2026-08-29 | Does this supersede, absorb or sit beside issue #25? | Superseded by C12: with US-4 deferred, #25 stays open and separate, its vocabulary settled |
| C8 | 2026-08-29 | Accept the PO's reframe, and at what size? | **Accepted at half size** (user). US-1 + US-2 only; US-3 and US-4 cut to §6 as **deferred, not rejected**, evidence intact; the tier framing stays declined. Consequence recorded in §1: a feature about right-sizing ceremony was itself halved at its own gate |
| C9 | 2026-08-29 | Is the anti-gaming property binding even though its AC left with US-4? | **Yes — binding ruling** (user). A declared size may bind bookkeeping volume only; it can never add, remove, merge, reorder, shorten in count or soften any gate, gate item, phase, agent, artifact or approval. Carried into §6's US-4 deferral so it is inherited, not re-litigated |
| C10 | 2026-08-29 | Govern `evidence.md` in Core, cap it via `/charter`, or leave it? | **Cap via `/charter`** (user) — a convention of *this* repo (`CONTRIBUTING.md:60`), not new public surface in Core. Recorded in §6 as a named follow-up; §1 states plainly that this feature therefore does not reach that 20–38% |
| C11 | 2026-08-29 | Is US-1's declaration generic ("declare any ceremony away") or specific to the browser/QA case? | **Specific** (user) — only the case that actually recurred three times. AC-1.7 makes the narrowness testable; §6 records that generalising later needs a second, genuinely different case first: evidence before mechanism |
| C12 | 2026-08-29 | Which size vocabulary, if US-4 is ever built? | **Issue #25's, verbatim** — `XS \| S \| M \| L \| XL \| unknown`, t-shirt sizes rather than story points, optional, with an explicit `unknown` so a missing size reads as "not stated" rather than silently as "small". Settled prior art recorded in §6; no divergence possible later |
| C13 | 2026-08-29 | **Clarify pass, 2nd run:** with US-3/US-4 gone, does the old `≤ 600 lines` success signal still hold? | **No — replaced** (PO ruling). Both volume levers left the feature and `evidence.md` is out of reach, so a line target would over-claim. Replaced by S1/S2, two countable behaviours, plus an explicit "what this half does not reach" paragraph and NFR-5 forbidding a volume claim in the release notes |
| C14 | 2026-08-29 | **Clarify pass (scope boundary):** is the declaration inferred from the profile's types, or stated explicitly? | **Explicit, user-confirmed** (PO ruling, AC-1.8). Inferring it from lens state would let a mis-typed profile suppress QA with nobody deciding it — the opposite of constitution §1's "the user confirms" pattern |
| C15 | 2026-08-29 | **Clarify pass (error/edge):** what happens when the declaration is present but incomplete or names an unperformable method? | **Fall back to today's behaviour — ask; never to suppression** (PO ruling, AC-1.6/AC-1.9). Ambiguity resolves toward more verification, never less; this is the one direction in which failing open would be a defect |
| C16 | 2026-08-29 | **Clarify pass (roles/authority):** may a phase agent write or amend the declaration mid-loop? | **No — `/charter` only** (PO ruling, AC-1.10, parked as A7 for the user's confirmation). An agent that can declare its own gate inapplicable is exactly the anti-rationalization risk [#13](https://github.com/a-lottes/aSPARK/issues/13) names, arriving through the front door |
| C17 | 2026-08-29 | **Post-approval amendment** (`/peer-review` r3 §6, findings F9 + F15): AC-1.7's ceremony list and NFR-4's "every ceremony" were written *before* the plan-gate ruling of 2026-08-29 pulled `/spark` into scope, so every file mirroring them inherits an incomplete set and each review round fixes one mirror by hand. Repair the spec, or keep patching mirrors? | **Repair the spec — AC-1.7 and NFR-4 only** (PO ruling, on the Reviewer's routing; no scope, story, ID or priority moves). AC-1.7 now states `/spark`'s one difference beside `/go-live`'s, keeps C11's generic-mechanism fence as the rule for every unlisted ceremony, and requires every shipped file repeating the list to carry both differences — so F15 falls out as one clause in `templates/constitution.md:110-114` and the class closes. NFR-4 exempts the *writing* ceremony: `/charter` asks one more question on every project (F9), recorded honestly in `evidence.md` §4.1 but never in the NFR. **Noticed, deliberately not changed here:** NFR-2's enumeration has the same gap (five reading/writing locations, `skills/spark/SKILL.md` absent) — widening it is the user's call at this gate, not the PO's **Fourth mirror closed at the same gate:** NFR-2 enumerated the added surface and omitted `skills/spark/SKILL.md` for the same reason. The PO flagged it rather than widening a post-approval surface on its own; the **user ruled it in on 2026-08-29**, so NFR-2 now names `/spark` too. Left unfixed it would have bitten at `/go-live`, whose release notes must enumerate the surface line by line — six locations against a spec naming five. **Follow-up from `/demo-day` r1 (B2), user-approved 2026-08-30:** AC-1.7's ceremony list is now explicitly scoped "at every value of this declaration", because a reader checking it against the shipped diff finds `agents/reviewer.md` in there (US-2's citation rule) and cannot tell from the sentence alone that the claim is about declaration values, not about the diff — the exact re-derivation US-2 exists to prevent. |
| C18 | 2026-08-31 | **Post-approval amendment** (`/demo-day` r1–r4, findings B1/B4, both Blocker): AC-1.3 and NFR-4 promised "no mention of the declaration," unqualified, under any framing. Four QA rounds and three progressively careful fix attempts — r1's reinforcement sentence, r3's silent-precondition restructuring, r4's explicit narration-immunity clause — each failed under live testing: r4's own 4 fresh, sequential, neutral-prompt-but-full-narration-requested live runs (2 venues × 2 runs) found **3 of 4 still disclosed the declaration**, one quoting actual field content verbatim (`Browser-observable surface: yes` and a substitute-method fragment), one reproducing B4's exact "Step N — apply the constitution check" placeholder. Is the unqualified guarantee still achievable, or must it be narrowed to stay honest? | **Narrowed (PO ruling; scope-preserving repair, same class as C17 — needs the same `/story-time` gate walk with the user before `/increment` proceeds; not yet re-approved).** Diagnosis confirmed: an unqualified "never mention, under any framing" rule embedded in an agent's own definition is not achievable against a caller's explicit, same-turn instruction to narrate all internal reasoning — a property of how instructions compete for priority, not a wording defect a fourth attempt is likely to fix, given three attempts in progressively careful forms already failed under progressively adversarial (not contrived) live testing. AC-1.3 and NFR-4 now scope the "no mention" guarantee to **ordinary invocation** — no explicit caller instruction to narrate, dump or expose internal reasoning, steps or checks — and state plainly that an explicit instruction to reveal all internal reasoning is **out of scope**: no natural-language rule can be made robust against a contradicting explicit instruction in the same turn, and this feature does not claim otherwise. **A narrower, content-vs-occurrence two-tier carve-out was considered and rejected:** every one of r4's four counted runs was itself narration-demanding, so no evidence isolates "mentions a check occurred" from "discloses actual field content" under narration — a two-tier rule would be unfounded, not evidence-based. **Deliberately not touched:** AC-1.5 (the `yes`-surface guarantee) makes a different claim — that the live-browser check is never *suppressed*, not that nothing is ever said — and it held 2/2 under the same round-4 adversarial testing (`qa.md` §2); narrowing it would be a separate call for the user, not implied by this one. No other AC or NFR is touched. **Obliges elsewhere, flagged not actioned here:** `review.md`'s traceability rows for AC-1.3 (`✅ met r2`) and NFR-4 (`✅ met`) were written against the pre-amendment wording and are now stale exactly as AC-1.7's row went stale after C17 — mark unconfirmed at the next `/peer-review`. `qa.md`'s open B1/B4 (Blocker) were both reproduced **only** under explicit full-narration prompts, which the narrowed AC now places out of scope — that does not close them by itself; `/demo-day` must re-test the **ordinary-invocation** case fresh (the last clean data for it is round 3's single plain-prompt run, superseded by round 4's further edit) before either finding is reclassified. |
| C19 | 2026-08-31 | **Post-approval amendment, second on this pair** (`/demo-day` r5, reopening B1/B4): C18's ordinary-invocation narrowing failed on its own narrowest test — two clean, non-narration-demanding runs, 0/2, one naming `.spark/constitution.md` and "substitute QA method" unprompted, one quoting `Browser-observable surface: yes` verbatim (`qa.md` r5 §2, B1). The user judged the defect structural rather than a wording gap: `agents/qa-tester.md`'s whole Mission pervasively instructs exhaustive self-narration of every check performed, and one narrow silencing clause fighting that pervasive characteristic was never likely to hold — five rounds across two attempts (four wordings, then one narrowing) now say it hasn't. Re-scope the requirement at its root, back to what US-1's own "so that I stop re-negotiating" clause actually asks for, rather than draft a sixth wording? | **Re-scoped (user's direction; PO drafted the wording and endorses the direction — see risk note below).** **Kept from C18:** the diagnosis itself — an unqualified in-agent "never mention" rule cannot survive a contradicting explicit instruction in the same turn; and AC-1.5 stays untouched, a different, already action-based claim ("never suppressed", not "never said") that held 2/2 under round-4 adversarial testing and needs no reframing here. **Replaced:** the guarantee is no longer content-suppression ("no mention, ever", then "no mention, under ordinary invocation") but action-based — no error, no warning, no asking the user to choose/confirm/supply a method, no re-negotiation of whether the ceremony should be overridden. Stating, in the agent's own words, that no declaration applies is now explicitly **not** a violation, in either the live reply or `qa.md` §1 (symmetric with the declared path's own documentation, AC-1.4). Read again under this narrower claim rather than fresh live evidence (condition (a), verifying against the amended requirement — `qa.md` r5 §2/§3's own quoted transcripts), round 5's two leaks are **not** violations of the reframed rule: neither Venue A nor Venue B asked the user for input, raised an error, or re-opened whether the override applies — both explained context in their own words and proceeded by default, which the reframed rule now explicitly permits. **On question 1 (does re-scoping make C18's ordinary-invocation carve-out redundant): dropped, not kept as belt-and-suspenders.** The carve-out guarded against irrepressible content disclosure under a reveal-everything demand — a mechanism specific to suppressing *what is said*. The reframed claim asks nothing to be suppressed; it asks whether the agent performs one discrete action (stop and solicit user input). Nothing in `qa-tester.md`'s pervasive narration ethos requires it to solicit user input, so the carve-out has no failure mode left to guard against here, and retaining it as an unused hedge would misstate what is actually load-bearing. This is a judgment, not proof: the next `/demo-day` round must test the reframed claim under an explicit narration demand as well as ordinary invocation, precisely because ambiguity resolves toward more verification, never less (constitution §1) — not because the PO assumes narration is now harmless. **On question 2 (agent's live reply vs. the produced artifact): drawn explicitly.** `qa.md` §1 documenting the absence is symmetric with the declared path's existing convention (AC-1.4) and is never a violation, at any severity, in either channel. The agent's own live reply gets the same "stating the fact is fine" allowance, but gratuitous verbatim reproduction of the declaration's raw field values in that reply — as opposed to describing the outcome in its own words — is a discouraged courtesy, capped at `Minor`, never `Blocker`-level and never gate-blocking alone, proportional to AC-2.4's own artifact-wording cap and applied here by analogy to conversational output rather than to `qa.md` itself. **On question 3 (is "no re-negotiation" testable): defined explicitly.** Counts as re-negotiation: asking the user to choose, confirm or supply a substitute method, or asking whether the declared browser-surface default should be overridden for this feature, when none is declared. Does not count: proceeding by today's default, including whatever ordinary QA-prerequisite ask that flow already made before this feature existed (AC-1.6's stop-and-say and AC-1.9's incomplete-declaration ask are a different, already-required case, untouched here); or a report, in either channel, that no declaration applies. **Stale as a result:** `qa.md` r5's AC-1.3/NFR-4 rows and its `❌ fail r5` verdict were written against C18's now-superseded wording and do not carry forward as-is against C19's; B1/B4 do not close automatically either — the transcript evidence they quote reads as favorable to the reframed claim (above) but was not gathered to test it, so a fresh `/demo-day` round is still owed before either finding is reclassified. `review.md`'s AC-1.3/NFR-4 rows, already flagged stale by C18, remain stale under C19 too, unconfirmed at the next `/peer-review` — not fixed here. **PO's own assessment, not softened because the user chose the direction:** the reframing is well-grounded — it traces back to US-1's actual "so that" clause rather than a claim the loop invented, and round 5's own transcripts already read as consistent with it. The remaining risk is narrower than before but not zero: an explicit narration demand could in principle still pressure an agent to phrase its explanation as a question back to the user ("should I check with you before proceeding?") without technically erroring — that would be re-negotiation under this AC's own definition above, and it has never been tested. If a sixth round finds that, the honest next move is not a seventh wording of this one clause but asking whether `qa-tester.md`'s structural narration ethos itself needs a change the AC layer cannot buy on its own — named here rather than deferred past noticing. |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **Overall impression:**
- **Heuristics findings:** (visibility of status, consistency, error prevention, recognition over recall, …)
- **Accessibility notes:** (contrast, keyboard navigation, focus order, labels)
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone") — baseline line counts verified directly in this repo; S1/S2 are countable, and §1 states what the feature does *not* reach
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — two Musts, the half-size version the user chose (C8)
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason) — each NFR names the surviving story it covers; library lens §§1, 2, 4 land as NFR-2, NFR-1, NFR-3; §3 marked N/A per constitution §2
- [x] Clarify pass done: no ambiguity left unresolved or unparked — second pass run on the revised two-story spec (C13–C16); C1–C12 resolved, C6/C7 explicitly superseded; C17 records the post-approval repair of AC-1.7, NFR-4 and NFR-2; C18 recorded, and C19 now supersedes, the ordinary-invocation narrowing of AC-1.3/NFR-4; C19 re-scopes both to an action-based no-ask/no-error/no-warning/no-re-negotiation guarantee, drafted after `/demo-day` r5 disproved C18 on its own narrowest terms
- [x] Open questions are resolved or explicitly accepted as risk — A1, A3, A4, A6 resolved by the user's rulings; A2 accepted as risk; A5 resolved by design; A7 confirmed by the user at the gate
- [x] Out-of-scope section is filled (something was consciously cut) — including two stories cut from this very spec, with their evidence and settled rulings preserved for whoever picks them up
- [x] Constitution (`.spark/constitution.md`) respected — §1 (suppression, negative case first, the user confirms), §3 (no toolchain), §4 (no test suite, agent attention, traceability), §5 (`.spark/` is public), §6 (no silent breaking change, degrade to silence, no agent passes its own gate) all bind a story or NFR above; no conflict found
- [x] Design review — **N/A**: this repo ships no UI of any kind (constitution §2)
- [x] Line budget respected: Ist 253 / Soll ~250 (excluding HTML comments — 4 comment lines, in §4 and §8) — 3 over, C19's row on top of C18's; recorded not waived
- [x] Status set to `approved` by the user — 2026-08-29, in the `/story-time` gate walk, together with A7's confirmation. **Re-approved 2026-08-29** after the AC-1.7/NFR-4/NFR-2 amendment (C17), routed here by `/peer-review` r3's verdict, which diagnosed three findings as one stale-spec root cause. **Re-approved again 2026-08-31** at a third `/story-time` gate walk, after narrowing AC-1.3/NFR-4 to ordinary invocation (C18) — evidence: four `/demo-day` rounds, three failed fix attempts, findings B1 and B4 (both Blocker). **Re-approved a fourth time, 2026-08-31**, after C19 re-scoped AC-1.3/NFR-4 from a content-suppression claim to an action-based one (no ask, no error, no warning, no re-negotiation), superseding C18 — evidence: `/demo-day` r5 disproved C18's own narrowest test, 0/2, under an ordinary QA request with zero narration demanded.
