# Spec: lean-artifacts

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-15 |
| **Ticket** | `none` (constitution §7) |

## 1. Problem & Goal

- **Problem:** A downstream phase needs very little from a completed predecessor
  artifact — is it passed, what is still open, what was ruled. In `review.md` and
  `qa.md` that state has **no fixed address**: it is scattered across the header
  table, the findings table, the verdict prose and the gate checklist, and a
  mature report accretes round-2/round-3 sections that supersede earlier ones.
  With no reliable anchor, the only safe read is the whole file. Measured in this
  repo: `.spark/graph-gates/review.md` is **695 lines** against the template's
  stated ~150-line budget, `qa.md` **625 lines**; the five template artifacts in
  that feature total **2,470 lines / 320,678 bytes**, while all six shipped
  templates together are **21,400 bytes**. The report's authors already felt this
  and hand-rolled a navigation preamble (`review.md:9–20`, "How to read this
  report") — a private, one-off fix for a structural gap.
- **Goal:** Every artifact this feature touches answers "what do you need to know
  to act on me?" at a fixed, compact address at the top, so a downstream phase
  reads the body **by exception**, not by default. That hand-rolled preamble is
  the shape being generalised: ~10 lines, maintained by **overwriting** it to the
  current binding state, while §§1–6 below it stay "kept unedited as the record".
  Index above, record below.
- **Success signal:** In the next feature's loop, the transcript of each phase
  that consumes a predecessor artifact shows a **bounded first read** (a read call
  with offset/limit or a named section, not a whole-file read), and **no reader
  has to hand-roll a "how to read this report" preamble** — the template already
  provides one.
- **Why now:** Every phase pays this cost again, and it grows with the artifact.
  It is also the cheapest half of the idea: additive, reversible, no new surface.

**Explicitly not the goal:** making artifacts *smaller*. A handoff block **adds**
lines. Anyone expecting a byte reduction from this feature will be disappointed —
see §6.

## 2. Target Users

Named consumers of a predecessor artifact, all inside this repo:

- the `reviewer` agent in **re-review** mode (`agents/reviewer.md:84`) — reads the
  previous report to verify fixes;
- `/increment` in **fix-mode** (`skills/increment/SKILL.md:50`) — findings are its
  task list, and it **writes back** into the report;
- the `release-manager` at `/go-live` (`agents/release-manager.md:42`) — reads
  `review.md` *and* `qa.md` purely to check two gates;
- the `product-owner` in `/next-steps` (`agents/product-owner.md:127`) — reads open
  findings in the newest `review.md`/`qa.md` across every feature dir;
- the **human maintainer** re-opening a stalled feature weeks later.

## 3. Assumptions & Open Questions

<!-- No open questions remain; C1–C11 in §7 record how each was resolved. The rows below are
     accepted risks and tracked dependencies, parked deliberately — not gaps. -->

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived as a solution ("stabiler Handoff-Block oben; erledigte Findings unter einen Marker in einen Appendix"). Recorded verbatim per the no-solutions rule; the underlying need is §1's *fixed address*, not a specific layout. Whether the block is a new element or an extension of the existing header table is `/sprint-plan`'s call. | Recorded |
| A2 | **The mechanism is a prompt instruction, not enforcement.** Nothing stops an agent reading the whole file anyway. Precedent says the instruction alone already works (`skills/increment/SKILL.md:24`, `skills/peer-review/SKILL.md:22–28`), but the only evidence available is a dogfood transcript. This spec claims no guaranteed saving. | **Accepted risk** (NFR-4) |
| A3 | Byte figures confirmed by the caller: `.spark/graph-gates/` = 320,678 B, `.spark/tracker-handoff/` = 114,451 B, `templates/` = 21,400 B. `evidence.md` (709 lines) and `PATCH-PLAN.md` (153) are inside that byte total but are **not** template artifacts — out of scope (§6). | Verified |
| A4 | Consumer parser behaviour verified against `~/aSPARK-graph/src/aspark_graph/artifacts.py`: `_status` / `_release_version` `re.search` the **whole file** and take the **first** `\| **Status** \|` / `\| **Version** \|` row; `_section` takes the **first** `##` heading containing the keyword and ends at the next `#`/`##`; `_first_table` takes the **first** table in that section. Prepending is therefore *conditionally* safe — safe only while the block adds no `##` heading containing `user stories`, `task breakdown`, `findings` or `acceptance criteria verification`, and no competing `Status`/`Version` row. | Verified 2026-08-15 |
| A5 | **Soft dependency:** constitution §3's protected list for `review-report.md` is being amended to add the `severity` / `location` / `status` columns the parser hard-requires (`artifacts.py:203–205`). That amendment is a `/charter` action, **not this feature's scope**. Non-blocking: this feature renames nothing, so it holds either way — but a reviewer citing §3 should read the amended version. | Tracked outside |
| A6 | §2's consumer list was derived by grep over `agents/` and `skills/`; it is believed complete but was not proven exhaustive. AC-2.1 is only as good as that list. | Parked — `/sprint-plan` re-derives it exhaustively as a task |

## 4. User Stories

### US-1 (Must): A fixed address for review and QA state

> As a phase that must act on a completed review or QA report, I want its status,
> verdict and still-open items at a fixed, compact place at the top, so that I can
> route correctly without reading the report body.

**Acceptance criteria:**

- [ ] AC-1.1: Given `templates/review-report.md` and `templates/qa-report.md`, when instantiated into a project, then each carries a handoff block above the first numbered section holding at minimum: artifact status, a one-line verdict, and the IDs of items still open.
- [ ] AC-1.2: Given a fact that the handoff block carries and that also appears elsewhere in the artifact, when the two disagree, then the template states in the artifact itself which location is authoritative — and no fact is written in two places without that stated precedence.
- [ ] AC-1.3: Given any phase that writes to a report — including `/increment` in fix-mode, which is not the artifact's owner — when that write closes a finding, changes a status or re-rules a verdict, then the same edit updates the block **in place, replacing the previous values**: the block carries one current state, never a per-round log. The template names a stale block as a defect, not a cosmetic issue.
- [ ] AC-1.4: Given a trail whose `review`/`qa` artifacts carry the block, when `aspark_graph.artifacts` parses it, then it raises no `TemplateDriftError` and yields the same Feature / Finding / QaCheck nodes and statuses as the same trail without the block.
- [ ] AC-1.5: Given a review or QA artifact written before this change (no block), when any ceremony reads it, then behaviour is exactly as today — no error, no warning, no migration prompt.
- [ ] AC-1.6: Given a report that has been re-ruled across rounds, when a reader reads only the block, then the block names which section carries the **binding** verdict and gate — so a hand-rolled "how to read this report" preamble is unnecessary.
- [ ] AC-1.7: Given a report with **zero** open items, when the block is read, then it says so explicitly rather than showing an empty field; given more open items than fit the block's ≤ 12-line budget, then it carries the total count plus the IDs of Blockers and Majors only, and points to the section holding the rest.
- [ ] AC-1.8: Given a block whose values contradict the body, when a reader detects it, then the reader proceeds on the location AC-1.2 declares authoritative and does not stop; the contradiction is logged as a finding at the next `/peer-review`.

### US-2 (Must): Read the block first, the body by exception

> As an agent starting a phase, I want my own instructions to tell me what to read
> first and the named condition under which I read more, so that loading a
> predecessor artifact whole stops being the default.

**Acceptance criteria:**

- [ ] AC-2.1: Given each consumer named in §2, when its skill or agent file is read, then that file states which part of the predecessor artifact it reads first and the named condition under which it reads further.
- [ ] AC-2.2: Given those instructions, when they are read end to end, then at least one condition **requires** the full body (e.g. a re-review verifying fixes) — the rule is bounded reading, never "never read the body".
- [ ] AC-2.3: Given a documented dogfood run of two consecutive phases against a new-shape artifact, when the transcript is inspected, then the downstream phase's first read of the predecessor is a read call with offset/limit or a named section — not a whole-file read — and the reader states explicitly whether it then needed the body.
- [ ] AC-2.4: Given the **negative case run first** — the same two phases against an old-shape artifact with no block — when the transcript is inspected, then nothing in the ceremony's behaviour or output differs from today.

### US-3 (Should): The same address in the other three artifacts

> As a maintainer, I want `spec.md`, `plan.md` and `release.md` to use the same
> handoff convention, so that "look at the top" is one rule and not three
> exceptions.

**Acceptance criteria:**

- [ ] AC-3.1: Given `templates/spec.md`, `plan.md` and `release-notes.md`, when instantiated, then each carries a handoff block of the same shape as US-1's.
- [ ] AC-3.2: Given those three, when `aspark_graph.artifacts` parses them, then `spec_status`, `plan_status`, `release_status` and `version` resolve to the same values as before the change, and no `US-`/`AC-`/`T` node is added, lost or renamed.
- [ ] AC-3.3: Given each template's stated line budget, when the block is added, then no template exceeds its budget; the block costs ≤ 12 rendered lines per artifact, counted excluding HTML comments.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Compatibility & versioning (library lens §2) | Purely **additive**: no protected heading, column or ID pattern in constitution §3 is renamed, removed or reordered; A4's three parser conditions hold. A trail in the new shape and the same trail in the old shape produce identical node/edge sets. Therefore a **minor** version bump, not breaking — no coordinated release with `aspark-graph` required. | `/peer-review` + documented dry run |
| NFR-2 | Public surface (library lens §1) | Zero new slash commands, agents, lenses or template *files*. The whole added surface is the handoff block in the 5 existing templates plus the reading rules in the consumers named in §2 — enumerated line by line in the release notes. | `/peer-review` |
| NFR-3 | Contract clarity (library lens §4) | Each template states, in the template, (a) which phase reads the block, (b) that every writing phase overwrites it in the same edit so it stays an index and not a log, (c) which location wins on conflict. A reader needs no external doc to use it correctly. | `/peer-review` |
| NFR-4 | Agent attention (constitution §4) | Honest claim only: the feature promises a bounded *first read*, not a token saving. Evidence is a transcript showing bounded reads (AC-2.3); the release notes must **not** claim a measured token or byte reduction. | `/peer-review` + dogfood transcript |
| NFR-5 | Reliability / degrade-to-silence (constitution §6) | Old-shape artifacts, artifacts with an empty block, and artifacts with a stale or contradictory block all continue to work: the ceremony proceeds, at worst falling back to the body. No gate ever blocks on a block's presence, freshness or emptiness. | `/peer-review` + dry run |

Not applicable, each with its reason: **Performance / Accessibility** — no runtime
and no UI (constitution §4). **Security** — lens off; no runtime, no data, no
network surface. **Roles & permissions** — Markdown files in a git repo; there is
no authorization surface to specify. **Library lens §3 (packaging/footprint)** —
per constitution §2: no bundle, no dependencies. **UX flows & states** — no UI;
the human-reading analogue (empty state, over-capacity state, "where is the
binding ruling") is covered by AC-1.6 and AC-1.7.

## 6. Out of Scope

- **The resolved-findings appendix — cut, confirmed (C1).** `.spark/graph-gates/review.md`
  holds **28** `F<n>` rows in 695 lines (**30** across all `review.md` in the repo).
  Even moving *every* finding row below a marker touches ~4% of the file. The
  indicator that motivated it (116 `resolved|fixed|✅` hits) counts mostly
  traceability cells (`✅ met`) and round-2/3 prose, not finding rows. It also
  carries the sharper contract risk: `_parse_review` reads only the *first* table
  of the *first* `##` heading containing "findings", so relocated findings vanish
  from the consumer's graph — a silent semantic change, masked in Core-managed
  repos only by constitution §3's known defect 1. Wrong target, real risk.
- **Bounding round-N accretion in reports** — the *actual* driver behind 695 lines
  (`review.md` §7.1–§7.11, §8.0–§8.6 are supersession narrative). Bigger win,
  **separate feature**; propose it at the next `/next-steps`.
- **`templates/constitution.md` — deliberately excluded, not forgotten (C10).**
  It is the most-read artifact in the loop, which is exactly why it stays out: a
  constitution hands nothing off. It has no status and no verdict to relay to a
  successor phase, so there is no handoff state to hoist. And summarising its
  principles at the top would invite agents to read the summary instead of the
  principles — the opposite of what it exists for.
- **Migrating the three existing `.spark/` feature dirs (C3).** They stay exactly
  as they are; AC-1.5 is the safeguard.
- **Non-template artifacts** — `evidence.md`, `PATCH-PLAN.md`, `.spark/BACKLOG.md`.
  Project-local inventions, not part of the shipped contract.
- **Amending constitution §3** to protect `severity`/`location`/`status` (C2) —
  a `/charter` action, tracked separately (A5).
- **Any enforcement mechanism** — no linter, no validator, no hook. Constitution
  §3 forbids introducing a toolchain, §4 rules out a test suite.
- **Compressing, summarising or truncating artifact bodies**, and anything at the
  LLM transport layer (the Headroom idea): wrong layer, collides with verbatim fidelity.
- **Fixing the two `aspark-graph` consumer defects** (constitution §3) — not Core's.
- **A template version marker / handshake.** Tempting while touching all five
  templates; it is its own cross-repo negotiation, not a rider on this one.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-15 | Keep the resolved-findings appendix? | **Cut** (user). Stays in §6 with the measured numbers; the feature is the handoff block only |
| C2 | 2026-08-15 | Constitution §3 omits the `severity`/`location`/`status` columns `_parse_review` hard-requires — amend? | **Yes, but out of scope** (user). `/charter` amendment; recorded as soft dependency A5, no story |
| C3 | 2026-08-15 | Migrate the three existing `.spark/` feature dirs to the new shape? | **No** (user). Out of scope; AC-1.5 guarantees old-shape artifacts keep working unchanged |
| C4 | 2026-08-15 | Minor bump, or a protected-structure change needing coordination with `aspark-graph`? | **Minor, purely additive** (user), grounded in A4: nothing protected is renamed, removed or reordered. Recorded in NFR-1 so it is traceable without re-reading the parser |
| C5 | 2026-08-15 | What is the block's *maximum* content? US-1 originally set a floor but no ceiling — an uncapped block becomes a second body and defeats the feature | **PO ruling:** ≤ 12 rendered lines, same cap as US-3. Empty and over-capacity behaviour in AC-1.7 |
| C6 | 2026-08-15 | Who updates the block when a *non-owner* phase writes to the artifact? `/increment` fix-mode edits `review.md` (`skills/increment/SKILL.md:50`) | **PO ruling:** whoever writes updates it in the same edit — part of the write, not a separate step. AC-1.3, NFR-3. Means US-2 touches `/increment`'s write path, not only its read path |
| C7 | 2026-08-15 | What does a reader do when block and body contradict each other? | **PO ruling:** proceed on the declared authoritative location, never stop (NFR-5); log the contradiction as a finding at the next `/peer-review`. AC-1.8 |
| C8 | 2026-08-15 | On re-review, is the block overwritten or appended to? | **Overwritten** (user, C11). **Grounded, not assumed:** `review.md:9–20` — the hand-rolled preamble is itself maintained by overwriting, describing in one current version that §7 supersedes §§1–6 and §8 supersedes §7, while §§1–6 sit beside it "kept unedited as the record". It is ~10 lines, already under the cap. Index above, record below — the division of labour already exists; this feature standardises it. AC-1.3, AC-1.7 |
| C9 | 2026-08-15 | How is AC-1.4 verified if `~/aSPARK-graph` is unavailable at build time? Constitution §3 forbids a hard dependency on it | **PO ruling:** running it is *verification*, not a dependency. Fallback where absent: a static walkthrough of `artifacts.py` against A4's three conditions, written down — precedent `.spark/graph-gates/evidence.md` Entry 3 |
| C10 | 2026-08-15 | Does `templates/constitution.md`, the sixth template and the most-read artifact in the loop, get a block? | **No** (user, PO recommendation confirmed). Reasoning recorded in §6 so it reads as a decision, not an omission |
| C11 | 2026-08-15 | Does overwriting the block conflict with this repo's "kept unedited as the record" norm? | **No** (user). The norm governs the *body*; the block is an index. See C8's grounding — the existing hand-rolled precedent already works this way |

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
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C11 resolved; A2, A5, A6 parked explicitly
- [x] Open questions are resolved or explicitly accepted as risk — A2 accepted as risk, A5 tracked outside, A6 handed to `/sprint-plan`
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected; the §3 gap is recorded as A5 and tracked as a separate `/charter` amendment
- [x] Design review — **N/A**: this repo ships no UI of any kind (constitution §2 — `seo`, `ux` lenses off, no website, no web-app, no UI)
- [x] Status set to `approved` by the user — given explicitly by the user on 2026-08-15, after walking this checklist together
