# Spec: tracker-handoff

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-06 |
| **Ticket** | — (no tracker declared for this repo) |

> **Source brief.** The user's brief of 2026-08-06 was handed over as binding scope,
> including the decision *"PR-open is done-done; the loop is not gated on an external
> approver"*. That decision is not reopened here. Two of its factual claims did **not**
> survive verification and changed the spec: the file list is **incomplete** (A5,
> resolved by C7) and this repo is **not currently** PR-first (A4, resolved by C8 — it is
> becoming so, by a separate `/charter` amendment, before this feature's own release).
> One claim was verified and *reduces* risk: the template contract is safe for a new
> enum value (A3). **2026-08-06, second pass:** the user resolved Q2, Q3, Q4 and Q5;
> Q1 remained open with a stated default. **2026-08-06, third pass:** the user has
> confirmed Q1's default as the settled decision (C10) — see §3 and §7.

## 1. Problem & Goal

- **Problem.** In an organization where merging belongs to a third party, aSPARK's
  Keep phase has no truthful ending.
  1. **The terminal status lies.** `templates/release-notes.md:8` offers
     `preparing | released | aborted`. With a PR open and unapproved, `released` is
     false, `aborted` is false, and `preparing` claims work is still in progress
     when the team has none left. Two gate boxes then cannot be honestly checked:
     *"Release actions executed and verified"* (`:62`) and *"Status set to
     `released`"* (`:64`). The Release Manager's step 6 *"Confirm it's alive"*
     (`agents/release-manager.md:60–63`) and `/go-live` step 5 are unreachable —
     nothing was deployed. A framework whose own gate forces a false statement
     contradicts its constitution (§1 *Honesty about maturity*, §6 *no agent passes
     its own gate*).
  2. **The consequence is worse than a wrong word.** `released` is hard-coded as the
     only terminal status in two ceremonies that read state machine-style:
     `skills/spark/SKILL.md:26,50–51` routes any non-`released` release back to
     `/go-live` forever, and `skills/next-steps/SKILL.md:35–36,73` classifies the
     feature as in-flight or stalled and proposes finishing it. Today's workaround —
     leave it `preparing` — therefore produces a loop that **never closes** and a
     backlog that keeps re-proposing finished work.
  3. **The ticket reference has no home.** Nothing under `.spark/` records the
     Jira/GitHub issue a feature serves; `grep -rn "Ticket" templates/` returns
     nothing. It lives in a branch name, a commit message, or a human's memory. And
     `agents/release-manager.md:88` forbids ticket IDs *unscoped*, so any reference
     added by hand is removed at the next release.
- **Goal.** A project can **declare once** how it delivers — direct or via a PR
  approved by someone else — and the loop then ends honestly in either mode, with
  the organization's ticket reference carried in exactly one place. Where nothing is
  declared, the loop is bit-for-bit today's loop.
- **Success signal (observable, negative case first).**
  1. **Unchanged.** In a project with no `Delivery & Handoff` declaration (i.e. every
     project that exists today), a full `/go-live` produces the same steps, the same
     report sections, the same gate boxes and terminal status `released`, and the
     report contains **zero** occurrences of `handed-off`.
  2. **Honest.** In a project declaring PR mode, `/go-live` ends with status
     `handed-off` and **every** presented gate box checked truthfully — no box
     requires a deploy that did not happen, and none is checked on a false claim.
  3. **Terminal.** With that report on disk, `/spark` without an argument reports the
     loop closed instead of routing to `/go-live`, and `/next-steps` classifies the
     feature as shipped-pending-approval, not as work to resume.
  4. **Survives a round trip.** A `/go-live` run after the change leaves the spec's
     `Ticket` value intact and the changelog free of it.
- **Why now.** Cheap and small, and it removes a defect that is currently
  *invisible* — a team hits it exactly once, at the last gate, after the work is
  done. It is also a precondition for the tracker integration in the backlog: there
  is nothing to integrate with while no artifact names a ticket. It is additionally
  the forcing function for this repo's own switch to PR-first delivery (C8): that
  amendment now has a concrete first beneficiary instead of being adopted in the
  abstract.

## 2. Target Users

- **The corporate aSPARK user (primary beneficiary).** A developer in a team where
  merge rights sit with a lead, an architect or a CODEOWNER, and where a Jira/GitHub
  ticket is mandatory. They cannot close the loop honestly today. US-1..US-4.
- **The existing solo/direct-deploy user (primary stakeholder, not a beneficiary).**
  Everyone running the loop today. They gain nothing and require exactly one thing:
  nothing changes. US-1 is theirs and is the dominant risk.
- **This repo itself (beneficiary, starting with this feature's own release).** Per
  C8 the constitution is being amended to PR-first *before* this feature's own
  `/go-live` — so `tracker-handoff` is the first feature to actually exercise
  `handed-off`, on its own release. Not a synthetic user; the same feature is
  proof of its own positive case (NFR-6).
- **The maintainer of the loop's state machine (secondary).** Whoever later reads or
  automates artifact statuses — `/spark`, `/next-steps`, a future board. A second
  terminal status is a contract change for them. US-2 (AC-2.4).

Explicitly **not** a user: the external approver. They are never prompted, notified,
polled or gated by aSPARK. Their tool is their own.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived partly as a solution ("new status `handed-off`, new constitution section, `**Ticket**` row"). Underlying need, restated: *the loop must be able to end truthfully when the last step belongs to someone outside the team, and the trail must carry the organization's reference for the work.* Original phrasing recorded per the no-solutions rule. | Accepted; the user's decision is binding and not reopened |
| A2 | aSPARK is Markdown prompt material executed by LLM agents. "Correct behavior" means the instructions steer agents reliably; no automated test can enforce any AC here (constitution §4). | Standing — Risk R4 |
| A3 | **Verified 2026-08-06.** The template contract is safe for a new enum value: `aspark-graph`'s `_status` (`~/aSPARK-graph/src/aspark_graph/artifacts.py:266`) extracts the `Status` cell with a regex and validates it against **no** enum; `queries.py` contains **no** comparison against the literal `released`. Additionally, `_parse_feature` (`:97`) probes `release-notes.md`, which a Core-managed project never writes (constitution §3 defect 1) — so the file is not even parsed there. A new value cannot raise `TemplateDriftError` and changes no query answer. | No coordinated release needed → NFR-1 |
| A4 | **The brief's context claim was wrong at spec time.** This repo did *not* work PR-first: `.spark/graph-gates/release.md:159` records "PR / merge — Not applicable — this repo releases directly on `main`", and constitution §5 mentioned no PR. **Resolved by C8:** the user has decided to switch this repo to PR-first via a *separate* `/charter` amendment, landed before this feature's own `/go-live` — not folded into this feature's build scope. | Resolved — C8; NFR-6 rewritten around it |
| A5 | **The brief's file list was incomplete.** Five files were named; `handed-off` is also read by `skills/spark/SKILL.md:26,50–51`, `skills/next-steps/SKILL.md:35–36,73`, and documented as the sole terminal status in `docs/workflow.md:85,95` and `README.md:30`. `agents/facilitator.md:59–60` enumerates the constitution's six sections by name, so a seventh section is left unfilled on a fresh `/charter`. | Resolved — C7. File list expanded to 9 files; AC-2.4 is now buildable |
| A6 | Placement test from `tools/README.md` ("could the constitution know this?"): release mode, approver, target branch, ticket-reference format and terminal status are **stable declared project facts** → constitution side. Whether `gh`, a Jira MCP or any CLI is installed is **installation state** → would be a `tools/` file, and is out of scope here (§6). | Accepted |
| A7 | The ticket-reference format is free text the project declares (`PROJ-123`, `#123`, a URL). Core validates nothing, resolves nothing, and never asserts a ticket exists. | Accepted |
| A8 | The Release Manager may keep doing what it does today under explicit user authorization — push a branch, open a PR (`agents/release-manager.md:81–83`). The brief's "kein `gh`-Aufruf" is read as *no new tracker/tooling integration*, not as removing an existing capability. | Accepted, feeds the confirmed default for Q1 |
| A9 | In `handed-off` mode, a tag is explicitly **not** created before merge (C9/Q2) — tagging the commit under review is unsafe because the commit can still change (rebase, review feedback). The `Version` row therefore carries a value marked **proposed**, and creating the real tag at/after merge is a boundary of this feature, not a gap it fills: it happens outside aSPARK's control, by whoever/whatever tags on merge (CI, the approver, a later manual step). | Accepted — folds into US-2/AC-2.2, release-manager step 3/5 |
| Q1 | Who establishes "PR open, CI green, reviewer requested" for the gate — the agent, by a read-only check it is already allowed to run, or the user, by attestation relayed to the agent? | **Resolved — C10, user-confirmed 2026-08-06.** The agent performs a read-only check when it already has the access `agents/release-manager.md:81–83` grants (e.g. it opened the PR itself, or can query CI status); where it has no such access, it falls back to **explicit, visibly-labelled self-attestation** relayed by the user, never a silent assumption. |
| Q2 | In PR mode, is the version bumped and tagged before handoff, or is the protected `Version` row filled with a *proposed* version and tagging left to the merge/CI? | **Resolved — C9.** Proposed version only; no tag before merge. Tagging at/after merge is outside this feature's control, named as a boundary. |
| Q3 | Positive-case evidence (A4): accept a synthetic dry run, amend this repo to PR-first, or ship with the positive case recorded as unproven? | **Resolved — C8.** This repo is switched to PR-first by a separate `/charter` amendment *before* this feature's own `/go-live`. This feature's own release, under `handed-off`, is the positive-case evidence — not a synthetic scratch-repo run, and not proven at spec-gate time. |
| Q4 | Accept extending the touched-file list from 5 to 8+ (A5)? | **Resolved — C7.** Accepted; 9 files now in scope (see §6-adjacent file list below and NFR-8). |
| Q5 | Is `handed-off` bound strictly to a declared PR mode, or may a direct-deploy project use it situationally? | **Resolved — C11.** Strictly bound. The single condition is: the constitution declares PR-mode delivery. A deploy-mode project with a blocked release window stays at `preparing`; there is no situational override. |

**Gate status on open questions:** Q1, Q2, Q3, Q4 and Q5 are all resolved and folded
below. No open question remains outstanding in this section. R9 (below) stays as a
named, accepted risk on Q1's chosen mechanism — not a blocker.

## 4. User Stories

### US-1 (Must): A project that hasn't declared anything notices nothing

> As an aSPARK user releasing directly, I want the Keep phase to behave exactly as it
> does today, so that someone else's approval workflow never becomes a change to my
> loop.

**Acceptance criteria:**

- [ ] AC-1.1: Given a project with no constitution, or a constitution without a `Delivery & Handoff` declaration, when `/go-live` runs to completion, then it performs the same numbered steps, produces the same report sections and the same gate boxes as the pre-change version, ends `released` or `aborted`, and the report and transcript contain **zero** occurrences of `handed-off` — checkable by comparing the two runs and grepping the artifact.
- [ ] AC-1.2: Given an undeclared project, when `/go-live` starts, then it does **not** ask which mode to use, does not warn, and does not mention that a mode could be declared; direct mode is the silent default.
- [ ] AC-1.3: Given a `release.md` or `spec.md` written before this change, when any ceremony reads it, then it is neither migrated, edited, nor flagged as outdated; `preparing`, `released` and `aborted` keep exactly their current meaning and routing.
- [ ] AC-1.4: Given no tracker is declared, when a spec is written, then the `Ticket` value is an explicit "none" marker and no gate, ceremony or agent blocks, warns or asks about it.
- [ ] AC-1.5: Given this feature's evidence record, when it is read, then the negative case (AC-1.1–1.4) is recorded as having run **first**, before any positive-case run, with its outcome written down — constitution §1.

### US-2 (Must): The loop can end at "handed over, not yet approved"

> As a developer whose PR is approved by someone else, I want a terminal status that
> is true, so that I neither claim a release that hasn't happened nor leave the loop
> permanently open.

**Acceptance criteria:**

- [ ] AC-2.1: Given `templates/release-notes.md` after the change, when its header table is diffed, then the rows `Status` and `Version` are unchanged in name, order and presence, and the only diff is the added value `handed-off` in the Status cell's enum (constitution §3, A3).
- [ ] AC-2.2: Given a release in handoff mode, when the KEEP GATE is presented, then **every** presented box is one the team can satisfy without a deploy — the PR exists on the declared target branch, CI on it is green, the declared approver is requested, the ticket is linked where one is declared, and the rollback path is written — the `Version` row carries a value explicitly marked **proposed**, no tag is created before merge, and the deploy and post-release-smoke boxes are marked N/A with the mode named as the reason, not silently dropped. *(A9/C9.)* Each box's PR-open/CI-green/reviewer-requested facts are established per the Q1/C10 mechanism: agent read-only check where access exists, else labelled self-attestation.
- [ ] AC-2.3: Given a report with status `handed-off`, when a reader opens it, then it names in one line what remains outstanding and **who owns it** (the declared approver or role, plus that the real tag/merge happens outside aSPARK's control), so it cannot be read as shipped.
- [ ] AC-2.4: Given a `release.md` with status `handed-off`, when `/spark` is invoked with no argument and when `/next-steps` gathers loop state, then both treat the feature as **closed for this team** — `/spark` does not route to `/go-live`, `/next-steps` does not classify it as in-flight or stalled — and each names it distinctly from `released` rather than as a synonym. *(Promoted from aspirational to buildable by C7's file-scope expansion — see §5 file list.)*
- [ ] AC-2.5: Given a handed-off feature, when time passes and the PR is merged, rejected or abandoned, then no aSPARK ceremony polls, reminds, re-checks or re-opens the loop by itself; the trail changes only if the user runs a ceremony (R1, decided).
- [ ] AC-2.6: Given the changed pre-flight and gate text, when a *direct-mode* release runs, then it sees no handoff box and no mode question — the two variants never both apply to one release.
- [ ] AC-2.7: Given a Release Manager about to write status `handed-off`, when it checks whether it may, then the **only** condition it evaluates is "does the constitution declare PR-mode delivery" — never the state of a deploy pipeline, a release window, or any other situational signal; a deploy-mode project whose release is blocked stays at `preparing`. *(C11/Q5 — new, guards against situational drift.)*

### US-3 (Must): Delivery is declared once, not decided at release time

> As a team lead, I want how we deliver to be a standing project fact, so that the
> Release Manager never has to guess the mode at the last gate and every feature is
> handed over the same way.

**Acceptance criteria:**

- [ ] AC-3.1: Given `templates/constitution.md` after the change, when the new `Delivery & Handoff` section is read, then it declares five things and nothing per-feature: release mode (direct or PR), who approves, the target branch, the ticket-reference format (or "none"), and the terminal status the loop ends in.
- [ ] AC-3.2: Given a project with a constitution, when `/go-live` runs, then the mode comes from that declaration — today neither `skills/go-live/SKILL.md` nor `agents/release-manager.md` mentions the constitution at all (verified: zero occurrences) — and the agent never infers a mode from the repo, the remote, or the conversation.
- [ ] AC-3.3: Given a first `/charter` on a fresh project after the change, when the Facilitator drafts the constitution, then the `Delivery & Handoff` section is proposed with grounded or explicitly-marked-as-guessed values, not left as template placeholder text.
- [ ] AC-3.4: Given an existing constitution, when `/charter` amends it for this section, then only that section and one dated Amendments row are added; no other section is rewritten.
- [ ] AC-3.5: Given the declaration is absent or partial, when `/go-live` runs, then the missing facts default to today's behavior (direct mode, no ticket, terminal `released`) without an error and without a prompt.

### US-4 (Should): A feature's ticket has exactly one home

> As a developer in a ticket-driven organization, I want the ticket recorded once in
> the trail, so that the PR and the audit trail link to it and nothing strips it back
> out.

**Acceptance criteria:**

- [ ] AC-4.1: Given `templates/spec.md` after the change, when its header table is read, then it carries a `Ticket` row whose value follows the constitution's declared format, or an explicit "none" marker; the protected `### US-<n> (<MoSCoW>): <title>` and `- [ ] AC-<n>.<m>:` forms are untouched.
- [ ] AC-4.2: Given the other five templates, when they are grepped for a ticket field, then none exists — the reference is not duplicated into `plan.md`, `review.md`, `qa.md` or `release.md`.
- [ ] AC-4.3: Given `agents/release-manager.md`'s rule that a changelog contains no ticket IDs, when it is read after the change, then it names the **section it binds** (the user-facing changelog) and states that the header table, the Release Actions record and the PR description are exempt — so the next run cites the ticket instead of deleting it.
- [ ] AC-4.4: Given a ticket is recorded, when traceability is checked, then `US-`/`AC-`/`NFR-`/`T`/`F` remain the only IDs any artifact cites; the ticket is a reference for humans and external systems, never a substitute anchor.

**Priority held at Should, not raised to Must** (see report to caller for the
reasoning): US-4 remains cleanly separable from US-1/US-2/US-3, and its absence
degrades US-2's ticket-linked box gracefully (AC-2.2's "where one is declared"
clause already handles "no ticket field exists" the same way it handles "no ticket
declared"). Unlike US-5 in `graph-gates`, cutting US-4 does not create a Must
story that can't be satisfied — it only shrinks AC-2.2 by one clause.

*If US-4 is cut, AC-2.2's "ticket is linked" clause is cut with it — the box cannot
reference a field that does not exist.*

## 5. Non-Functional Requirements

**Touched-file list (post-C7, 9 files, up from the brief's 5):**
`templates/constitution.md`, `templates/spec.md`, `templates/release-notes.md`,
`agents/release-manager.md`, `skills/go-live/SKILL.md`, `skills/spark/SKILL.md`,
`skills/next-steps/SKILL.md`, `docs/workflow.md`, `README.md`. `agents/facilitator.md`
is touched only if its six-section enumeration (`:59–60`) needs a seventh name added —
`/sprint-plan` decides whether that is a real edit or already generic enough.

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Compatibility / versioning *(library lens §2)* | Purely additive: no template heading, row, column or ID pattern in constitution §3's protected table is renamed or removed. Specifically `release-notes.md` keeps the header rows `Status` and `Version`, and `spec.md` keeps its story/AC line forms. Evidence that the added enum value is non-breaking is A3 (consumer regex, no enum validation, no `released` literal in `queries.py`). → **minor** bump, no coordinated release. | `/peer-review` + `git diff templates/` (structure-only, no consumer needed) |
| NFR-2 | Backward compatibility *(constitution §4)* | An already-instantiated `spec.md` or `release.md` in a consumer project is never edited, migrated or invalidated by this change, and no ceremony asks the user to update one. Existing `released` reports keep their routing in `/spark` and `/next-steps` unchanged. | Dry run of `/spark` (resume) and `/next-steps` against this repo's existing `.spark/graph-gates/` trail, before and after |
| NFR-3 | Public surface *(library lens §1)* | Zero new slash commands, agents, templates or directories: counts stay 10 skills / 7 agents / 6 templates / 8 lenses. The added surface is exactly one constitution section, one template row and one enum value — each of which becomes a promise consumers may depend on. | `/peer-review` of the diff + `claude plugin validate` |
| NFR-4 | Contract clarity *(library lens §4)* | Every new declaration states its value **when undeclared**, and each gate variant names the mode it belongs to. A reader of any `release.md` can tell from the report alone which mode produced it and which boxes were therefore N/A. | `/peer-review` of `templates/` + a produced report in each mode |
| NFR-5 | Reliability — degrade to the default *(constitution §6, adapted)* | With nothing declared, the strings `handed-off`, `Delivery & Handoff` and any handoff prompt appear zero times in `/go-live`'s output and report, and no gate outcome differs from the pre-change run. No gate blocks on the presence of a constitution, a declaration or a ticket. | Dogfood step 1 (negative case, **run first**, in this repo) + `/peer-review` |
| NFR-6 | Evidence bar *(constitution §4)* | No automated test is claimed. Evidence is a written record in this feature's `.spark/` trail of a dry run of **every ceremony this change touches** — `/charter`, `/go-live`, `/spark` resume, `/next-steps` — negative case first, each outcome stated. **The positive case is deliberately deferred, not proven at Specify time (C8/Q3):** it is this feature's *own* Keep phase, once the separate `/charter` amendment to PR-mode has landed. **This means the SPEC GATE below closes without positive-case evidence existing yet** — it arrives when this feature's own `release.md` reaches status `handed-off`, and the QA gate for this feature must not be passed until that evidence exists (a QA report that only exercises the negative case is incomplete for this feature specifically). | The written record, checked at the QA gate; **positive-case entry added at this feature's own `/go-live`** |
| NFR-7 | Docs in step *(constitution §4)* | `README.md:30` and `docs/workflow.md:85,95` describe the terminal status; both state both terminal statuses in the same change, and `README.md` §Project Status labels the positive case truthfully as proven or unproven — truthfully meaning "unproven" until this feature's own release closes (NFR-6). | `/peer-review` of `README.md` + `docs/workflow.md` against the evidence record |
| NFR-8 | Agent attention *(constitution §4)* | Surface grew from 5 to 9 files (C7). **New ceiling:** net added lines across all touched files ≤ 90 (up from the prior 60, roughly proportional to the file-count growth, not a blank check), and `templates/release-notes.md`'s KEEP GATE does not grow beyond 10 boxes in either mode — a gate nobody finishes reading is not a gate. Each of the four newly-added files (`skills/spark/SKILL.md`, `skills/next-steps/SKILL.md`, `docs/workflow.md`, `README.md`) gets at most 1–3 lines changed — this is a vocabulary fix (recognize a second terminal status), not a rewrite of any of those ceremonies' logic. | `git diff --stat` + `/peer-review` |
| NFR-9 | Traceability *(constitution §4)* | No existing ID is renumbered; the `Ticket` row introduces no new ID namespace and is cited by no downstream artifact as an anchor (AC-4.4). | `/peer-review` of the diff |
| NFR-10 | Security & privacy | N/A — `security` lens off in the profile. One live concern is noted, not designed for: a ticket ID or PR URL committed under `.spark/` is **public** in this repo (constitution §5), so this repo's own Ticket row stays "none". | Recorded, checked at `/peer-review` |
| NFR-11 | Accessibility / performance | N/A — no UI, no runtime, no rendered surface (constitution §4). | N/A |

*Lens coverage: `library` is the only active lens. §1 → NFR-3, §2 → NFR-1 + NFR-2,
§4 → NFR-4 + NFR-7; §3 (packaging/footprint) is the constitution's declared N/A —
no bundle, no dependency added by this feature.*

## 6. Out of Scope

Each line is a documented "no", not an oversight.

- **Any tracker integration.** No MCP client, no `gh`/Jira API call to read or write a
  ticket, no availability probe, no `tools/` file. Declaration only — this works
  identically with and without a ticket system. *Follow-up feature; per A6 that one
  activates on installation state and therefore belongs in `tools/`, not here.*
- **Reading open tickets in `/next-steps` or mirroring gate transitions into a
  tracker.** Named by the brief as the separate follow-up; not planned here.
- **Watching the PR's fate.** No polling, no reminder, no status refresh, no reopening
  the loop on rejection. Decided (R1) — one does not gate on what one does not control.
- **A fifth enum value** for "the third party approved / merged". Nothing in the loop
  would observe it, and a status nobody writes is dead weight.
- **PR templates, branch-naming rules, CODEOWNERS, CI config, review-assignment
  policy.** The project's business, declared at most as the target branch and approver.
- **Enforcing that a ticket exists.** No gate blocks on a missing ticket, ever.
- **Backfilling `Ticket` rows or handoff sections into existing artifacts.**
- **Machine-readable release evidence** (commit SHA, date, tag as parseable fields) —
  that is BACKLOG C4, blocked on the consuming repo's G1. This feature must not
  restructure the Release Actions table in a way that pre-empts it.
- **The mechanics of this repo's own switch to PR-first** (branch protection, who the
  approver is, required CI checks). That is `/charter`'s decision and a separate
  amendment (C8) — this spec only depends on that amendment landing first; it does not
  specify its content.
- **Tagging on merge.** Creating the real, non-proposed tag once the PR merges is
  explicitly outside this feature's control (A9) — it happens via whatever mechanism
  the target repo uses (CI, a manual step by the approver), and no aSPARK ceremony
  performs or verifies it.
- **A per-feature override of the declared mode.** The constitution declares; a spec
  does not re-declare. Reopen only if a real project needs two modes at once.
- **Situational use of `handed-off` outside declared PR mode** (C11) — e.g. a
  deploy-mode project with a blocked release window. That project stays at
  `preparing`; there is no per-release escape valve.
- **A live CI/PR API integration for AC-2.2's checks.** The Q1/C10 mechanism uses only
  access the Release Manager already has under existing authorization
  (`agents/release-manager.md:81–83`); it does not add a new read capability, a new
  tool, or a polling loop to acquire one.
- **Offering a git commit into the feature branch at each SPARK gate-close step**
  (working name **`gate-commits`**: propose, get an explicit yes, then commit —
  never auto-commit — consistent with this repo's existing git-safety culture).
  Considered during this spec's review and deliberately **deferred to its own
  `/story-time` pass**, not folded in, because: (a) it roughly **doubles** this
  feature's touch surface — all seven build-phase ceremony skills
  (`story-time`, `look-and-feel`, `sprint-plan`, `increment`, `peer-review`,
  `demo-day`, `go-live`) each have exactly one gate-close step where it would
  attach, only two of which (`go-live`, `sprint-plan`) are already in this
  feature's file list; and (b) it needs its **own** Clarify pass, orthogonal to
  tracker/handoff — granularity (gate-close only, or also `/increment`'s
  per-task loop?), the no-op case (nothing to commit → silent skip, never an
  error), the branch-missing case (create it, or require it to pre-exist per
  constitution §5's "one branch per feature"?), whether a decline is sticky for
  the rest of the ceremony run, a commit-message convention, and an explicit
  **no retroactive scope** (applies only going forward from when it ships; no
  ceremony comments on pre-existing uncommitted state). **Shared-file
  coordination note, not joint scope:** both features touch
  `agents/release-manager.md` and overlapping ceremony skills, so the two
  features' eventual PRs/diffs should be sequenced or diffed with that overlap
  in mind — this does not require the two to be planned or built together.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-06 | Does adding `handed-off` to the Status enum breach the cross-repo template contract? | **No — verified, not assumed.** `_status` (`artifacts.py:266`) is a regex over the `Status` cell with no enum validation; `queries.py` never compares against `released`; and `_parse_feature` probes `release-notes.md`, which Core-managed projects never write (§3 defect 1). The protected rows `Status` and `Version` stay. Folded into A3, AC-2.1, NFR-1. |
| C2 | 2026-08-06 | Is `handed-off` really terminal, given `released` is hard-coded as the only terminal status in two ceremonies? | Only if those ceremonies are changed too. Raised as AC-2.4, A5, then **resolved by C7**. |
| C3 | 2026-08-06 | Which side of `tools/README.md`'s line ("could the constitution know this?") does each new declaration fall on? | Release mode, approver, target branch, ticket format and terminal status are **stable declared facts** → constitution. Installation state of any CLI or MCP surface → `tools/`, and therefore out of scope. A6, §6. |
| C4 | 2026-08-06 | What does "rollback path" mean when nothing was deployed? | It is the documented way back **after** the third party acts: which commit reverts the change, who may perform it, and what the consumer-visible effect is. A PR-mode report that writes "n/a, nothing deployed" fails AC-2.2 — the box exists precisely because the merge happens without us. |
| C5 | 2026-08-06 | Should the ticket reference also appear in the PR description and Release Actions, given the changelog rule forbids ticket IDs? | **Yes, and the rule must say so.** `agents/release-manager.md:88` is unscoped today and would strip the reference on the next run. AC-4.3 scopes it to the user-facing changelog (§2) and exempts the header table, the Release Actions record and the PR description. |
| C6 | 2026-08-06 | Is `handed-off` an escape hatch that lets a team declare done while the PR rots? | **Yes, structurally — and it is accepted with a mitigation, not designed away.** AC-2.3 forces the report to name the outstanding step and its owner, and AC-2.4 forces `/spark` and `/next-steps` to name it distinctly from `released`. Nothing more is possible without gating on a third party, which the decision forbids. R1. |
| C7 | 2026-08-06 | (Q4, user decision) File scope: accept the expansion from 5 to 9 files so AC-2.4 becomes buildable? | **Accepted.** `skills/spark/SKILL.md`, `skills/next-steps/SKILL.md`, `docs/workflow.md` and the `README.md` row are added; `agents/facilitator.md` is touched only if needed. AC-2.4 moved from aspirational to a Must acceptance criterion with a concrete file target. NFR-8's ceiling raised from 60 to 90 net lines to reflect the larger, still-small surface. |
| C8 | 2026-08-06 | (Q3, user decision) How is the positive case evidenced, given this repo is not PR-first? | **This repo switches to PR-first via a separate `/charter` amendment, landed before this feature's own `/go-live`.** `tracker-handoff` becomes the first real PR-first release of this repo; its own `release.md` under `handed-off` status is the evidence — not a synthetic scratch-repo run. The `/charter` amendment's mechanics (branch protection, who approves) are explicitly out of scope for *this* spec (§6). Consequence made explicit in NFR-6: the SPEC GATE can close without this evidence existing; the QA gate for *this* feature may not close until it does. |
| C9 | 2026-08-06 | (Q2, user decision) Version and tag in handoff mode? | **Proposed version only, no tag before merge.** The `Version` row carries a value marked proposed; creating the real tag happens at/after merge, outside this feature's control — a stated boundary (A9), not a gap. Folded into AC-2.2, AC-2.3, and the release-manager step 3/5 rewrite (`/sprint-plan`'s job to word). |
| C10 | 2026-08-06 | (Q1, **user-confirmed** 2026-08-06) Who establishes PR-open/CI-green/reviewer-requested? | **Resolved — the PO's recorded default is the settled decision, confirmed explicitly by the user.** The agent performs a read-only check where it already has the access `agents/release-manager.md:81–83` grants; otherwise, explicit, visibly-labelled self-attestation relayed by the user is the fallback — never a silent assumption. Folded into AC-2.2. The residual risk that self-attestation becomes the common case rather than the exception is carried forward as **R9**, an accepted risk for `/peer-review` to watch, not an open question. |
| C11 | 2026-08-06 | (Q5, user decision) Is `handed-off` bound to declared PR mode, or may it be used situationally? | **Strictly bound to the declared PR mode — no situational override.** The Release Manager's only check is "does the constitution declare PR-mode delivery"; a deploy-mode project with a blocked release window stays at `preparing`. New AC-2.7 guards this explicitly; new Out-of-Scope line records the rejected alternative. |
| C12 | 2026-08-06 | (Coordinator-proposed) Should a git-commit offer at every SPARK gate transition be folded into this spec? | **Split — deferred to a companion feature, working name `gate-commits`.** PO recommendation, accepted by the user: it roughly doubles the touch surface (all seven build-phase ceremonies vs. this feature's 9 files) and needs its own Clarify pass unrelated to tracker/handoff. No US-5 added, no NFR-8 change, no file-list expansion. Recorded as an Out-of-Scope line with a shared-file coordination note (not joint scope). |

## 8. Design Review

<!-- Filled by /look-and-feel. -->

- **Status: N/A — no UI surface.** This feature changes Markdown prompt material and
  template text only (`templates/`, `agents/`, `skills/`, `docs/`, `README.md`); it
  renders nothing. The Designer's heuristics have no artifact to apply to.

---

## Named Risks

- **R1 — `handed-off` as an escape hatch.** The loop declares itself closed while the
  decisive step hasn't happened; a rejected or abandoned PR leaves a trail claiming
  done-done, and nothing corrects it (AC-2.5, by decision). Mitigation: AC-2.3 and the
  distinct naming in AC-2.4. Accepted, not solved.
- **R2 — Two gate variants soften the gate.** A checklist with modes invites picking
  the easier list. Mitigation: the mode is declared in the constitution *before*
  release time (US-3) and never chosen by the agent (AC-3.2, AC-2.6, AC-2.7).
- **R3 — Terminal-status blindness.** **Resolved by C7** — the file scope now includes
  `/spark` and `/next-steps`, so AC-2.4 is buildable rather than aspirational.
- **R4 — Convention, not enforcement.** Prompt material, no tests (A2); a rule that is
  followed and a rule that is skipped look identical afterwards. Standing.
- **R5 — No native venue for the positive case.** **Resolved by C8** — this feature's
  own release becomes the venue, once the separate `/charter` amendment lands. New
  residual risk: **R8**, below.
- **R6 — Future consumer semantics.** No consumer compares against `released` today
  (A3), but a later board or metric that special-cases it will show handed-off
  features as unfinished. Cost is a wrong dashboard, not a broken parse; recorded so
  the next cross-repo change knows.
- **R7 — The rule collision returns.** If AC-4.3's scoping is worded loosely, a future
  Release Manager run strips the ticket reference back out and the loss is silent.
- **R8 — This feature's own delivery is now sequence-dependent on a second feature.**
  Per C8, `tracker-handoff` cannot reach a *proven* NFR-6/positive-case QA gate until a
  separate `/charter` amendment (this repo → PR-first) has landed and this feature's
  own PR has gone through it. If that amendment stalls or is rejected, this feature's
  QA gate is blocked on work outside this spec's scope — a real dependency, not a
  hypothetical one. Mitigation: none inside this spec; flagged so `/sprint-plan`
  sequences the two pieces of work correctly and the QA gate note (NFR-6) makes the
  wait explicit rather than silent. **Carried forward as-is — still live.**
- **R9 — Q1's confirmed mechanism is untested against a real corporate PR workflow.**
  The self-attestation fallback (C10, now settled) could become the common case
  rather than the exception if agents rarely have the access the primary path
  assumes, which would make AC-2.2's boxes weaker in practice than they read on
  paper. This is now an **accepted** risk, not an open question — the decision is
  made — but it stays a named risk because the settlement decided the mechanism,
  not its real-world hit rate. Mitigation: `/peer-review` should check which path
  actually fired in the dogfood evidence, not just that a box was checked, and
  `/demo-day` should note if self-attestation fired more often than the read-only
  path across the trial runs.

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — 3 Must, 1 Should
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason) — NFR-1..11, `library` lens mapped
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C12 folded
- [x] Open questions are resolved or explicitly accepted as risk — **Q1–Q5 all resolved** (C7–C11); R8 and R9 remain as named, accepted risks carried into Plan/Review/QA, not blockers
- [x] Out-of-scope section is filled (something was consciously cut) — including the deferred `gate-commits` companion (C12)
- [x] Constitution respected, or conflicts recorded as open questions — §3 template contract → AC-2.1/NFR-1 (verified, C1); §1 negative-case-first → AC-1.5/NFR-5; §4 backward compatibility → NFR-2; §6 nothing unasked → AC-2.5. **No conflict found**; the one tension (a public repo's Ticket row) is NFR-10
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A, §8
- [x] Status set to `approved` by the user — confirmed 2026-08-06 in the coordinating conversation

> **Note for planning.** How the mode is read, where in the template the variant sits,
> and the exact wording of each rule are `/sprint-plan`'s business, not this spec's.
> **Sequencing note:** this feature's plan should account for R8 — the separate
> `/charter` PR-first amendment is a precondition for this feature's own QA gate
> (NFR-6), not for `/sprint-plan` or `/increment`, which can proceed immediately.
> A separate companion feature, `gate-commits` (C12), may be specced independently
> whenever the user chooses — it is not a dependency of this feature's plan or build.
