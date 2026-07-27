# Spec: graph-gates

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-07-25 |

> **Source brief.** `.spark/graph-gates/PATCH-PLAN.md` was handed over as binding
> scope. This spec keeps its §2 non-goals and its §3 decision, and **cuts two of
> the four queries** it wired (`gate_health` entirely, `story_trace`'s QA leg) —
> because they are unsound for a Core-managed project and a wrong number is worse
> than a missing one. See C1 and §6. Everything the brief's §5 says about *how* to
> build it is deliberately absent here; that is `/sprint-plan`'s business.
>
> **All six open questions were resolved by the user on 2026-07-25** (C7–C12).
> One resolution was empirical and changed the spec materially: the positive case
> is **proven possible**, and `files:` notes were shown to be a precondition for
> `impact` answering the question anyone would actually ask it — which promoted
> US-5 from `Should` to `Must` (C12). Status remains `draft`: approval is the
> user's separate, explicit step.

## 1. Problem & Goal

- **Problem.** Three distinct pains, of very different sizes:
  1. **Integration debt is pushed onto every project.** The gate-level guidance
     for `aspark-graph` exists, finished and specific — in the *other* repo
     (`aSPARK-graph/docs/aspark-integration.md`), as a copy-paste block each
     project must shovel into its own `CLAUDE.md`. `grep -riE "aspark-graph"`
     over `skills/`, `agents/`, `templates/`, `lenses/`, `README.md` returns
     zero hits. Whoever runs both products pays the wiring cost once per
     project, and the copy silently ages when the query surface moves.
  2. **The plan's task→code link is missing, and its absence is load-bearing.**
     A `plan.md` today names tasks and stories but never the files a task
     touches, so any reader — human or tool — reconstructs the link from prose.
     The human cost is borne by whoever reads a plan they did not write (an
     `/increment` run, a reviewer, the user three weeks later). The **measured**
     cost is larger: `aspark-graph query impact src/aspark_graph/artifacts.py`
     on a real, fully built graph returns that file's `code_entities`
     populated but `affected_acs: []` and `affected_stories: []` — because with
     no `files:` notes anywhere there are no `implements` edges to traverse
     (A7, verified 2026-07-25). Without this, `impact` cannot answer *"which
     stories and ACs does touching this file put at risk?"* — the only question
     worth asking it — and degrades to a file-level symbol list.
  3. **A conditional pain the fix must not cause.** Every existing aSPARK user
     is on a project *without* the graph. For them this feature has no upside at
     all; their entire interest is that their loop does not change. That is the
     dominant risk, not a side note.
- **Honest sizing.** If this is never built, the graph still works via the
  copy-paste block, and today's beneficiary population for pains 1 and 3 is
  approximately **one person** (the author, the only known holder of an
  install-from-source `aspark-graph`). Pain 2 — the `files:` note — is the only
  part with a beneficiary who does not need the graph at all, **and** it is what
  makes the graph wiring worth having for the one who does. This is therefore a
  **small, cheap change with one large downside risk and one unconditionally
  valuable part**. It earns its cycle on three grounds: it stops a copy-paste
  integration pattern before it spreads, it makes every *future* optional tool
  cost one file instead of four duplicated text blocks, and it closes the
  determinism gap that currently empties the blast-radius query.
- **Goal.** Where an optional external tool is present, the ceremonies offer it
  by themselves, with nothing to configure in the target project. Where it is
  absent — the normal case — the loop is bit-for-bit the loop of today. And a
  plan states the files a task touches, so its task→code link is declared
  instead of absent, graph or no graph.
- **Success signal (observable, negative case first):**
  1. **Silence.** In this repo (no built graph), a full `/peer-review` on this
     feature's own diff produces a report containing **zero** occurrences of
     `aspark-graph` / `.aspark-graph`, with the same steps, the same report
     sections and the same gate outcome set as a pre-change run.
  2. **Offer.** In `~/aSPARK-graph` — verified 2026-07-25 to build cleanly
     (`912 code entities, 276 artifact entities, 68 inferred links`) and to
     index source — `/peer-review` names ≥1 `impact` or `story_trace` result as
     the reason it looked where it looked, **and** still reports ≥1 finding or
     verification anchored at a concrete `file:line` with code content behind
     it. The venue is confirmed available; this signal is expected to be
     **proven**, not deferred (C11).
  3. **Stale.** With a deliberately stale graph, the run says so, stops citing
     graph results, falls back to reading, and **still reaches a verdict**.
  4. **Declared, and non-empty.** The first `/sprint-plan` after the change
     emits `files: <path>` notes in every DoD cell whose files are knowable,
     while `templates/plan.md`'s protected columns are unchanged in name, count
     and order. Corroboration in a source-indexed repo: `impact` on a file named
     by such a note returns **non-empty** `affected_stories` / `affected_acs`,
     where the same call returns empty today (A7).
  5. **Zero-config.** None of 2–4 required adding or editing a single file in
     the target project.
- **Why now.** The wiring is collection, not construction: the queries shipped
  in `aspark-graph` v0.5.0. The window matters because the copy-paste pattern is
  the thing being replaced — every project that adopts it first makes this
  change a migration instead of an addition. The consuming side is already
  waiting: `_files_note` is implemented there and receives nothing, because Core
  emits nothing (A7). And the `tools/` mechanism is a precondition for wiring
  anything else later, including the queries this spec defers.

## 2. Target Users

- **The existing aSPARK user (primary stakeholder, not a beneficiary).** A solo
  developer or small team running the loop on a project with no `aspark-graph`
  and no intention of installing one. They receive **no** capability from this
  feature. Their requirement is negative and absolute: nothing changes. US-1 is
  theirs.
- **The dual-tool operator (primary beneficiary, population ≈ 1 today).** Someone
  running aSPARK Core *and* an install-from-source `aspark-graph` on the same
  repo, who today maintains a hand-copied integration block per project. US-2,
  US-3, US-4 are theirs.
- **The plan reader (beneficiary independent of the graph).** Anyone who reads a
  `plan.md` they did not write — the `/increment` run, the Reviewer, the user
  later — and wants to know which files a task is expected to touch. US-5.
- **The plugin maintainer / tool author (secondary).** Whoever adds the *next*
  optional external capability and should not have to touch four skills and three
  agents to do it. US-6.

Explicitly **not** a user: an end user of any product built with aSPARK. This
feature ships no runtime surface of any kind.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived as a solution: "a new `tools/` directory analogous to `lenses/`, detection via installation state, never blocking". Underlying need, restated: *the ceremonies must be able to use an optional external capability without any project configuring it, and without any project that lacks it noticing.* Original phrasing recorded here per the no-solutions-in-spec rule. | Accepted framing. The directory name `tools/` is confirmed by the user as a deliberate public-surface commitment (C12/Q6); its internal shape remains `/sprint-plan`'s to design |
| A2 | aSPARK is Markdown prompt material executed by LLM agents. "Correct behavior" means *the instructions reliably steer the agents*, not a deterministic guarantee. No automated test can enforce any AC here (constitution §4). | Standing assumption — Risk R1 |
| A3 | The query contract of `aspark-graph` v0.5.0 (call forms, JSON on stdout, exit 1 when unbuilt, `inferred`<`extracted`<`declared`) is stable and normatively recorded outside this repo. Core will hard-code a name from another repo; if that contract moves, Core calls into the void. | Accepted — Risk R4 |
| A4 | **Verified 2026-07-25** against `~/aSPARK-graph/src/aspark_graph/artifacts.py:76–80`: the consumer probes `review-report.md`, `qa-report.md`, `release-notes.md`, while Core instantiates `review.md`, `qa.md`, `release.md`. Each probe is a bare `if x.exists():` with no alias. In **any** Core-managed project, three of five artifact types are silently invisible, so `gate_health.open_findings` is always `0` and `story_trace` has no QA leg — indistinguishable from clean answers. **Corroborating evidence:** that repo's own `.spark/aspark-graph/qa-report.md` carries the header `\| AC \| Steps performed \| Expected \| Observed \| Result \|` — Core's *old* column name. Its trails were authored against an earlier template, which is exactly why its build survives the `Spec ID` column defect, and exactly why it is an unrepresentative venue for any artifact-name-dependent query. | Resolved by scope cut — C1, §6 |
| A5 | The queries this spec wires read only `spec.md`, `plan.md`, source files and file mtimes — all identically named in a Core-managed trail and a template-named trail. A4 therefore does not affect them, so a positive-case dogfood in a template-named repo **is** representative for the wired surface. **Confirmed empirically 2026-07-25** in `~/aSPARK-graph`: `build .` succeeds (`912 code entities, 276 artifact entities, 68 inferred links`; a benign cache-version mismatch — cache written by 0.4.1, current 0.5.0 — triggered a full rescan and no abort), `query staleness --repo .` returns `files_checked: 98, changed: [], missing: []`, and `query impact src/aspark_graph/artifacts.py --repo .` returns populated `code_entities`. | Accepted and verified — the basis for AC-2.x being verifiable today |
| A6 | Core-side accountability for US-5 ends at *emitting* a correct `files:` note. The confidence label a consumer derives from it (`declared` vs `inferred`) and the edges it builds are the consumer's behavior — corroboration recorded with the dogfood evidence, not acceptance criteria. | Accepted |
| A7 | **Verified 2026-07-25.** `impact` on a real source file in a fully built graph returns populated `code_entities` but `affected_acs: []` and `affected_stories: []`: no `files:` notes exist anywhere, so there are no `implements` edges to traverse. The consuming side is ready and idle — `_files_note` is already implemented (`src/aspark_graph/artifacts.py::_files_note`) and receives nothing because Core emits nothing. **Consequence:** `files:` notes are a *precondition* for `impact` answering a story-level question, not a determinism nicety. | Folded into §1, US-5 (promoted to Must), AC-4.5 — C12 |
| Q1 | Does the user accept the scope cut in C1 (no `gate_health`, no QA leg), given it contradicts the binding brief's §5/T2? | **Resolved (C7)** — accepted exactly as specced, on the shared-JSON-object argument. |
| Q2 | `staleness` reports `stale: true`: treat the graph as **absent** for the rest of the run, or use its answers with reduced trust? | **Resolved (C8)** — treat as absent, state it once, fall back to reading, reach the verdict normally. AC-3.2 stands. |
| Q3 | State 3 ("CLI installed, graph not built"): how often may the one-line hint appear? | **Resolved (C9)** — at most once per ceremony run, never repeated within a run. AC-2.3 stands. |
| Q4 | Scope of the `files:` instruction, and must `/increment` correct a note reality diverged from? | **Resolved (C10)** — knowable → stated, not knowable → omitted, never guessed. No post-build correction this cycle; it stays in §6. AC-5.1/5.2 stand. |
| Q5 | Is the positive case (success signal 2) a release blocker, or may it ship recorded as unproven? | **Resolved (C11)** — moot: the positive case is **proven possible**. `~/aSPARK-graph` builds cleanly and indexes source (A5). It is expected to be run and passed, not deferred. |
| Q6 | `tools/` becomes a `${CLAUDE_PLUGIN_ROOT}` path and therefore part of the consumed contract (constitution §2) — renaming it later is breaking. Is `tools/` the name to commit to? | **Resolved (C12)** — `tools/`, as briefed, committed to publicly. |

**No open questions remain.** Every row above is either an accepted assumption
with a named risk or a resolved decision.

## 4. User Stories

### US-1 (Must): A project without the graph notices nothing

> As an aSPARK user on a project where `aspark-graph` is not installed, I want
> every ceremony to behave exactly as it does today, so that someone else's
> optional accelerant never becomes a change to my loop.

**Acceptance criteria:**

- [ ] AC-1.1: Given a repo with no `aspark-graph` on `PATH` and no `.aspark-graph/` directory, when `/sprint-plan`, `/peer-review` or `/demo-day` runs to completion, then the produced artifact and the ceremony's own output contain **zero** occurrences of the strings `aspark-graph` and `.aspark-graph` — checkable by grep of the artifact and the transcript.
- [ ] AC-1.2: Given the same repo, when one of the three **wired** ceremonies (`/sprint-plan`, `/peer-review`, `/demo-day`) runs, then it performs the same numbered steps, produces the same artifact sections and presents the same gate checklist as a run of the pre-change version on the same input — checkable by comparing the two runs' artifacts. **Narrowed by C13** (2026-07-26): the criterion binds *the graph wiring*, not unrelated concurrent work on other ceremonies.
- [ ] AC-1.3: Given any degraded state — tool absent, tool present but graph unbuilt, a query that errors, times out, or returns `{"found": false}` — when a gate evaluates its checklist, then no checklist item passes or fails because of the tool's availability, freshness or answer; the pass/fail set is identical to a run with no tool at all.
- [ ] AC-1.4: Given the dogfood evidence for this feature, when it is read, then the negative case (AC-1.1–1.3) is recorded as having run **first**, before any positive-case run, with its outcome written down — per constitution §1.
- [ ] AC-1.5: Given a target project, when any of the above is exercised, then no file in the target project was created or edited to enable or disable the tool — no `CLAUDE.md` block, no config, no flag.

### US-2 (Must): Where the graph exists, the gate offers it unasked

> As an operator running Core and `aspark-graph` on the same repo, I want the
> ceremonies to detect and use the graph on their own, so that I stop maintaining
> a hand-copied integration block in every project.

**Acceptance criteria:**

- [ ] AC-2.1: Given the graph is available for the current repo, when `/sprint-plan`, `/peer-review` or `/demo-day` starts, then it establishes availability during its existing gate-check step and hands the tool guidance to its agent **by path**, the same way it already hands over lens paths — with no new ceremony and no new agent.
- [ ] AC-2.2: Given both an MCP surface and a CLI are present, when availability is resolved, then a single documented precedence order decides which is used (MCP first, CLI second), so two runs in the same environment resolve identically.
- [ ] AC-2.3: Given the CLI is present but the repo has no built graph, when a ceremony starts, then it states this **once per ceremony run**, in one sentence, naming the command the user *could* run; it does not run it, does not ask, does not repeat within the run, and completes without the graph. *(C9.)*
- [ ] AC-2.4: Given the graph is available in the Plan phase, when the EM fills *Affected Components*, then the section either cites the `impact` result for the files the plan touches or records that the result was empty — a reader can tell whether the blast radius was derived or guessed.
- [ ] AC-2.5: Given the graph is available in the Review phase, when the report is written, then it names which query results it used to scope the diff and which locations it read as a consequence.
- [ ] AC-2.6: Given the graph is available in the QA phase, when the test plan is built, then it uses `story_trace`'s Story→AC→Task→Code legs to decide which ACs to exercise and where to look, and the QA report states that it did so.

*Dependency on US-5 (A7): AC-2.4's story-level value is created by US-5, not by
this story. Until `files:` notes exist in the plan being analyzed, `impact`
returns `affected_stories: []` / `affected_acs: []` by construction — which is
why US-5 is a Must in the same release and why AC-4.5 exists.*

### US-3 (Must): A graph answer is a map, never a verdict

> As an aSPARK user, I want the graph to speed up *scoping* without shortcutting
> the reading and the clicking the gates exist for, so that reviews and QA get
> faster, not shallower.

**Acceptance criteria:**

- [ ] AC-3.1: Given a Review run with the graph available, when the report is written, then it contains at least one finding or verification whose evidence is a concrete `file:line` plus the code content at that location — not a graph result restated.
- [ ] AC-3.2: Given `staleness` reports `stale: true`, when the ceremony continues, then it states in the artifact that the graph is stale, treats the graph as **absent** from that point on (citing no graph result as evidence), falls back to reading and grep, and still reaches its normal verdict. *(C8.)*
- [ ] AC-3.3: Given a query returns an empty result or `{"found": false}`, when the phase continues, then it records in one line that scoping was done by hand, proceeds by the pre-change method, and does **not** read the empty answer as "there is nothing there".
- [ ] AC-3.4: Given a QA run with the graph available, when the AC verification table is filled, then no `Result` cell rests on a graph answer — every one rests on a performed step.
- [ ] AC-3.5: Given a `/demo-day` run where browser tooling or the app is unavailable, when the gate is checked, then the ceremony stops exactly as it does today — graph availability neither softens nor substitutes that hard prerequisite.
- [ ] AC-3.6: Given the tool guidance and every agent section this feature adds, when they are read, then each states explicitly that a graph answer replaces neither reading the code (Review, Plan) nor performing the steps (QA).

### US-4 (Must): Only answers that are sound for a Core-managed project are offered

> As an aSPARK user, I want the gates to stay silent about numbers that would be
> wrong in my kind of project, so that I am never reassured by a zero that only
> means "no file was opened".

**Acceptance criteria:**

- [ ] AC-4.1: Given the shipped tool guidance, the wired ceremonies and the wired agent sections, when they are grepped for `gate_health`, then it appears in **no** instruction to call it — only, if at all, inside a documented deferral.
- [ ] AC-4.2: Given the guidance describes `story_trace`, when an agent reads it, then it is told that the QA leg is not populated for a project using Core's instantiated artifact filenames, that its emptiness must not be read as "no QA evidence exists", and that only the Story→AC→Task→Code legs are offered for scoping.
- [ ] AC-4.3: Given the tool guidance, when a maintainer reads it, then it lists which queries are deliberately **not** wired and the condition under which they may be (the consuming repo resolving its artifact-filename defect) — so the deferral is reopenable rather than forgotten.
- [ ] AC-4.4: Given any query the guidance instructs an agent to call, when its soundness is traced, then it depends only on artifacts whose filenames are identical in a Core-managed trail and a template-named trail (`spec.md`, `plan.md`), on source files, or on file mtimes.
- [ ] AC-4.5: Given the guidance describes `impact`, when an agent reads it, then it is told that `affected_stories` and `affected_acs` are **empty by construction** for any plan that carries no `files:` notes — including plans written before this change — that an empty list must not be read as "no story is at risk", and that the fallback in that case is the pre-change method. *(New — from A7/C12; the same failure mode as `gate_health`'s `open_findings: 0`, and the reason it is guarded rather than assumed away.)*

### US-5 (Must): A plan says which files a task touches

> As a reader of a plan I did not write — human or tool — I want each definition
> of done to name the files the task is expected to touch, so that the task→code
> link is declared rather than absent, and a question about a file can be
> answered at story level.

**Acceptance criteria:**

- [ ] AC-5.1: Given a plan produced by `/sprint-plan` after this change, when its tasks are inspected, then every DoD cell whose touched files are knowable at plan time ends with a `files: <path>[, <path>…]` note using repo-relative paths. *(C10.)*
- [ ] AC-5.2: Given a task whose files are genuinely not knowable at plan time, when its DoD is written, then the note is **omitted** rather than guessed — a wrong `files:` note outranks a correct inference downstream and is therefore a defect, not an approximation. *(C10.)*
- [ ] AC-5.3: Given `templates/plan.md` before and after the change, when the task table is diffed, then the columns `#`, `Task`, `Story`, `Status`, `Definition of Done` are identical in name, count and order; the heading words `Task Breakdown` and the `^T\d+$` task-ID form are unchanged; the only diff is guidance text.
- [ ] AC-5.4: Given the plan template's guidance and the EM's instructions after the change, when they are compared, then they state the same `files:` format — no second, divergent description of it exists in the repo.

*Priority: promoted `Should` → **Must** on 2026-07-25 (C12). The original
`Should` rested on "declared beats inferred", a quality improvement. A7 replaced
that with a harder argument: with no `files:` notes there are **no**
`implements` edges, so `impact` — one of only two fully sound queries this spec
wires — returns `affected_stories: []` and `affected_acs: []` and cannot answer
the only question worth asking it. Shipping US-2's Plan slice without US-5 would
therefore offer an agent an empty list that reads as "nothing at risk" — the
exact failure mode US-4 exists to prevent, and the exact reason `gate_health`
was cut. Internal consistency, not extra value, is what makes this a Must: a
partial delivery that drops US-5 must also narrow AC-2.4 to `impact`'s
file/symbol legs.*

*Note on accountability (A6): Core's obligation ends at emitting a correct note.
That a consumer then builds an `implements` edge at confidence `declared` is
corroboration recorded with the dogfood evidence (success signal 4), not an AC.
The consuming side is verified ready — `_files_note` is implemented and idle.*

### US-6 (Should): The next optional tool is add-a-file

> As a plugin maintainer, I want adding the next optional external capability to
> be one new file plus one line per ceremony, with a documented boundary against
> lenses, so that the mechanism does not decay into four copies of the same
> drifting text.

**Acceptance criteria:**

- [ ] AC-6.1: Given the tools authoring guide, when a contributor reads it, then it states what a tool file is, that it activates from **installation state** (not from the constitution's project profile), how a ceremony picks it up, and the steps to add another one.
- [ ] AC-6.2: Given the same guide, when a contributor asks "is my new concern a lens or a tool?", then it answers with a stated boundary — profile-activated concern checklist vs. installation-activated capability — and at least one example on each side.
- [ ] AC-6.3: Given the agent sections this feature adds, when they are read, then they are written **generically**: they instruct the agent to read whatever tool file the caller passed and name no specific external product; all product-specific detail lives in the tool file only.
- [ ] AC-6.4: Given a hypothetical second tool file conforming to the guide, when a ceremony runs with that tool installed, then it can be picked up by adding the file and referencing its path — with no new agent, no new ceremony and no edit to an existing agent's role text.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Compatibility / versioning *(library lens §2)* | No protected structure in `templates/` is renamed or removed: `plan.md` keeps the heading words `Task Breakdown`, the columns `#`, `Task`, `Story`, `Status`, `Definition of Done` in unchanged name, count and order, and task IDs matching `^T\d+$`. The change is purely additive → **minor** version bump to `0.4.0` in `.claude-plugin/plugin.json`, no major, no coordinated release needed. | `/peer-review` + `git diff templates/` (structure-only diff, no consumer required) |
| NFR-2 | Public surface *(library lens §1)* | Zero new slash commands, zero new agents, zero new ceremonies. Counts stay at 10 skills / 7 agents. The only added public surface is the `tools/` directory and its files — a name the user has consciously committed to publicly (C12) — referenced exclusively as `${CLAUDE_PLUGIN_ROOT}/tools/…`, never relatively. | `/peer-review` of the diff + `claude plugin validate` |
| NFR-3 | Contract clarity *(library lens §4)* | Every query Core instructs an agent to call is documented with its call form, its return shape, and its behavior on failure or empty result. The external tool is documented as optional and install-from-source, with **no** registry/PyPI claim anywhere. | `/peer-review` of `tools/` + `README.md` |
| NFR-4 | Packaging & footprint *(library lens §3)* | N/A — no bundle, no runtime, no dependencies, no engines to declare. This feature adds **no** dependency: the external tool is discovered at run time and its absence is the normal case (NFR-5). | N/A (recorded, not verified) |
| NFR-5 | Reliability — degrade to silence *(constitution §6)* | With the tool absent, the strings `aspark-graph` and `.aspark-graph` appear zero times in any ceremony's output or artifact, and no gate's step order, artifact sections or checklist outcomes differ from the pre-change version. No gate blocks on availability, freshness or emptiness. | Dogfood step 1 (negative case, **run first**, in this repo) + `/peer-review` of the diff |
| NFR-6 | Soundness of offered answers | Core places no query result in an agent's context whose answer is unsound or empty-by-construction for a Core-managed project without a caveat attached at the point of use: `gate_health` appears in no call instruction; `story_trace`'s QA leg is declared not-to-be-read; `impact`'s `affected_stories`/`affected_acs` carry the empty-by-construction caveat for plans without `files:` notes (AC-4.5); every wired query reads only `spec.md`, `plan.md`, source, or mtimes (AC-4.4). | `/peer-review`: grep of `tools/`, `skills/`, `agents/` for `gate_health`, for QA-leg instructions, and for the `affected_*` caveat |
| NFR-7 | Safety — nothing runs unasked *(constitution §6)* | Core instructs no write, build, install or mutating command. The only permitted invocations are read-only `query` calls and non-mutating detection probes; `aspark-graph build` may be **named to the user** but never executed by an agent. | `/peer-review`: grep of `tools/`, `skills/`, `agents/` for `build`, `install`, and any non-`query` invocation |
| NFR-8 | Traceability *(constitution §4)* | The `US-`/`AC-`/`NFR-`/`T`/`F` chain stays intact: the `files:` note is additive inside an existing cell and breaks no downstream ID citation; no ID is renumbered (AC-4.5 and this spec's later ACs append). | `/peer-review` of the diff |
| NFR-9 | Docs in step *(constitution §4, §1)* | `README.md` gains its optional-tools entry in the same change, describing the tool as optional and install-from-source, and §Project Status states the proof state **truthfully**. The expected state is *proven*: the positive case's venue (`~/aSPARK-graph`, verified to build and index source — A5) is named in the evidence record, and the negative case is recorded as run first. Anything not actually run is labelled as not run. | `/peer-review` of `README.md` against the dogfood evidence record |
| NFR-10 | Evidence bar *(constitution §4)* | No automated test is claimed or assumed. Evidence is a written record, in this feature's `.spark/` trail, of a dogfood or dry run of **every phase this change touches** (Plan, Review, QA), negative case first, each step's outcome stated. Success signals 1–4 in §1 are all expected to be exercised; brief §6 step 5 is dropped as unverifiable-by-us (C5). | The written record itself, checked at the QA gate |
| NFR-11 | Agent attention | The tool guidance declares its phases and is sliced per phase, so an agent reads only its own slice; the guidance file stays under 150 lines. | `/peer-review` + `wc -l` |
| NFR-12 | Accessibility / performance | N/A — no UI, no runtime, no rendered surface. The only cost is agent attention, bounded by NFR-11. | N/A (constitution §4) |
| NFR-13 | Security & privacy | N/A per the constitution's profile (`security` lens off). The one live concern — instructing an agent to invoke an external command — is carried by NFR-7, not by a lens. | N/A |

*Lens coverage: `library` is the only active lens. Its §1, §2 and §4 land as
NFR-2, NFR-1 and NFR-3; its §3 is the constitution's declared N/A, recorded as
NFR-4. All other lenses are off in the profile and contribute nothing here.*

## 6. Out of Scope

Consciously cut. Each line is a documented "no", not an oversight.

- **`gate_health`, entirely.** Its `open_findings` is always `0` for a
  Core-managed project because the findings file is never opened (A4), and the
  two sound fields arrive in the same JSON object as the unsound one — an agent
  cannot be relied on to ignore one key of an object it was handed. That
  argument is the one the user accepted (C7). **Reopen when** the consuming repo
  resolves its artifact-filename defect; the cost then is one phase slice in the
  tool file plus no skill change, which is precisely what the `tools/`
  mechanism buys.
- **`story_trace`'s QA leg.** Same root cause. The Story→AC→Task→Code legs are
  sound and are wired; the QA leg is declared not-to-be-read rather than shown
  with a footnote. Reopen on the same condition.
- **Any workaround inside Core for the consumer's filename defect** — no alias,
  no rename, no dual-write. Core renames nothing to accommodate a consumer
  (constitution §3); the fix is filed in the consuming repo.
- **`/go-live`, `/increment`, `/charter`, `/story-time`, `/look-and-feel`.** Not
  wired. `/go-live` additionally waits on a `Release` node that does not exist in
  the consumer yet.
- **`aspark-policy`.** It has no invocable surface to call.
- **The template version handshake** (`<!-- aspark-template: … -->`) — a separate,
  coordinated feature (BACKLOG C3). Shipping it alone produces a marker nobody
  reads.
- **A new column in `plan.md`.** The `files:` note lives inside the existing DoD
  cell. Appending a column is legal but unnecessary, and every column added is a
  structure someone else can come to depend on.
- **`/increment` keeping `files:` notes accurate.** If the build touches files the
  plan did not predict, nothing corrects the note this cycle — confirmed by the
  user (C10). Carried as Risk R6.
- **Backfilling `files:` notes into existing plans.** Plans written before this
  change keep none, so `impact`'s story legs stay empty for them; that is what
  AC-4.5 guards.
- **Any automated check that the wiring fired.** Impossible for prompt material
  (A2); the human gate and the written dogfood record are the only checks.
- **Auto-install, auto-build, or vendoring the external tool.** Non-negotiable
  (constitution §6).
- **A project-local `tools/` directory.** Tool files live in the plugin only; a
  team cannot ship one that exists solely in their repo.
- **Making anything about this configurable.** No opt-in flag, no opt-out flag,
  no setting. Installation state is the only switch.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-07-25 | The brief wires all four queries. Two return answers that are unsound for a Core-managed project (A4). Wire them with a caveat, or defer them? | **Split by kind of wrongness.** `story_trace` without its QA leg is *incomplete but not misleading* — its sound legs are exactly what Plan and Review need for scoping — so it ships with the QA leg declared not-to-be-read. `gate_health` is *actively misleading*: `open_findings: 0` is a false negative on the one thing a gate exists to catch, and it is bundled in the same object as two sound fields, so selective ignoring is unenforceable. It is cut entirely. Deferring is cheap *because* this feature builds the `tools/` mechanism. Folded into US-4, NFR-6, §6. **Accepted by the user — see C7.** |
| C2 | 2026-07-25 | What does `stale: true` mean for the rest of the run — ignore the graph, or trust it less? | **Treat as absent**, state it once, fall back to reading, complete normally. "Reduced trust" is not a behavior an agent can apply consistently. Folded into AC-3.2. **Confirmed by the user — see C8.** |
| C3 | 2026-07-25 | "Say it once" for the installed-but-unbuilt state — once per what? | **Once per ceremony run**, never repeated inside a run. Folded into AC-2.3. **Confirmed by the user — see C9.** |
| C4 | 2026-07-25 | How far does the `files:` obligation reach, and what if reality diverges? | **Knowable → stated; not knowable → omitted, never guessed** (AC-5.1/5.2), because a declared link outranks an inferred one downstream. Post-build correction out of scope. **Confirmed by the user — see C10.** |
| C5 | 2026-07-25 | The brief's test step 2 (positive case in a template-named repo) and step 5 (`build` without `TemplateDriftError`) are both compromised. How are the ACs verifiable anyway? | **By only wiring queries whose inputs are name-identical across both worlds** (AC-4.4): `spec.md`, `plan.md`, source, mtimes. The scope cut therefore rescues the test plan (A5). The template-safety AC was rewritten as a **diff** check (AC-5.3, NFR-1), which needs no consumer. Step 5 of the brief is dropped as unverifiable-by-us. **Reinforced by C11:** the venue's `qa-report.md` header is Core's *old* `AC` column, which is why its build survives — positive confirmation that it is unrepresentative for artifact-name-dependent queries, and irrelevant for the ones actually wired. |
| C6 | 2026-07-25 | Should the `files:` notes be their own feature? | **No — one feature, its own story.** Different beneficiary, different risk profile, so US-5 and its own risk row; but it edits `agents/engineering-manager.md`, which the wiring also edits, so splitting means two passes over one file for no gain. |
| C7 | 2026-07-25 | **Q1** — accept the C1 scope cut, against the binding brief's §5/T2? | **Accepted, exactly as specced**: `impact` + `staleness` + `story_trace` minus its QA leg; `gate_health` cut entirely and reopenable on the consumer fix. Accepted specifically on the shared-JSON-object argument (two sound fields and one misleading field in one payload cannot be selectively ignored). No spec change needed beyond marking Q1 resolved; §6's reopen condition stands. |
| C8 | 2026-07-25 | **Q2** — `stale: true` semantics? | **Treat the graph as absent**, state it once, fall back to reading, reach the verdict normally. AC-3.2 amended to say "treats the graph as absent" explicitly rather than implying it. |
| C9 | 2026-07-25 | **Q3** — hint frequency for the installed-but-unbuilt state? | **At most once per ceremony run**, never repeated within a run. AC-2.3 amended to state the scope of "once" explicitly. |
| C10 | 2026-07-25 | **Q4** — scope of the `files:` obligation and post-build drift? | **Knowable → stated, not knowable → omitted, never guessed.** No `/increment` post-build correction this cycle; it stays in §6 and remains Risk R6. AC-5.1/5.2 stand as written. |
| C11 | 2026-07-25 | **Q5** — is the positive case a release blocker, or may it ship unproven? | **Moot — the positive case is proven possible, so it is expected to be run and passed.** Verified in `~/aSPARK-graph` on 2026-07-25: `aspark-graph build .` **succeeds** (`912 code entities, 276 artifact entities, 68 inferred links`; a benign cache-version mismatch — cache 0.4.1 vs. current 0.5.0 — caused a full rescan, not an abort); `query staleness --repo .` → `files_checked: 98, changed: [], missing: []`; `query impact src/aspark_graph/artifacts.py --repo .` → populated `code_entities`. R5's central fear (an abort on the unrelated consumer defect) is **unfounded**. Folded into A5, §1 success signal 2, NFR-9, and R5 (rewritten and downgraded). The hedging language is removed throughout. |
| C12 | 2026-07-25 | **Q6** — commit to `tools/` publicly? And: does the new `impact` evidence change US-5's priority? | **`tools/` confirmed**, as briefed (folded into A1, NFR-2). **US-5 promoted `Should` → `Must`** on the evidence in A7: `impact` on a real source file returns populated `code_entities` but `affected_acs: []` / `affected_stories: []`, because no `files:` notes exist to build `implements` edges from, while the consumer's `_files_note` is already implemented and idle. Decisive reasoning: shipping US-2's Plan slice without US-5 would hand an agent an empty list that reads as "no story at risk" — the same failure mode that got `gate_health` cut (C1/C7), so consistency with US-4 forces it. New **AC-4.5** guards the residual case (plans written before this change). Folded into §1 pain 2, §1 success signal 4, US-2's dependency note, US-5's priority note. |
| C13 | 2026-07-26 | **F10** (Major, round 2) — `skills/spark/SKILL.md` gained a numbered step ("Offer the clean handoff at heavy gates", 7 → 8 steps), which AC-1.2 forbids as written. Fix, waive, revert, or narrow the criterion? | **Narrowed, and the change kept and documented.** AC-1.2 was written to guarantee that *this feature's graph wiring* leaves a ceremony behaving exactly as before; `/spark`'s new step is a separate, deliberate concern (the artifact-budget / context workstream the user folded into this increment on 2026-07-26) and has nothing to do with the tool. Reading AC-1.2 as a freeze on every file in the plugin would make any concurrent work on any ceremony a spec breach, which is not what US-1 protects. AC-1.2 therefore binds the three wired ceremonies, where the pre-change baseline exists (`evidence.md` T1) and where leakage is actually possible. **What is *not* narrowed:** AC-1.1, AC-1.3 and AC-1.5 still bind every ceremony — the new step says nothing about the tool, conditions no gate on it, and writes nothing in a target project. Recorded as deviation **D6** in `plan.md`, and the behaviour is documented in the README. Authorised by the user during round-2 finding routing; the spec keeps status `approved` because the amendment narrows scope and adds no requirement. |

## 8. Design Review

<!-- Filled by /look-and-feel. -->

- **Status: N/A — no UI surface.** This feature ships Markdown prompt material
  and one template comment. It renders nothing: verifiable by diff — the change
  touches `tools/`, `skills/`, `agents/`, `templates/`, `README.md` and
  `.claude-plugin/plugin.json` only, none of which produce a rendered surface.
  The Designer's usability and accessibility heuristics have no artifact to
  apply to. A formal `/look-and-feel` pass would return the same conclusion.

---

## Named Risks

- **R1 — Convention, not enforcement.** Every AC here relies on LLM agents
  following instructions; no test proves the wiring fired or stayed silent. A
  correctly-silent gate and a gate that silently skipped its wiring look
  identical. Standing, highest-impact risk. Mitigation: the negative case is
  mandatory and runs first (AC-1.4).
- **R2 — The regression that breaks everyone.** If any gate blocks, warns or
  mentions the tool when it is absent, this feature breaks the loop for
  essentially every existing user — the repo's worst failure mode (constitution
  §4). Mitigation: NFR-5 + AC-1.1–1.3, negative case first.
- **R3 — Quality erosion via false authority.** An agent that treats a graph
  answer as a verdict reviews less code, and the review gets *worse* while
  feeling faster. Mitigation: AC-3.1, AC-3.6, and the success signal's demand
  for `file:line` evidence in the same report that cites the graph.
- **R4 — Contract drift in the other repo.** Core will name queries it does not
  own. If the query surface moves, the instructions point into the void — and
  because nothing blocks, the failure is silent by design. Mitigation: the
  contract is normatively recorded outside this repo and known to the consumer's
  backlog; degradation is to silence, so drift costs capability, not
  correctness.
- **R5 — Venue constraint on the positive case (low, was: may not be provable).**
  **Downgraded 2026-07-25 (C11).** The original fear — that
  `aspark-graph build .` might abort on the unrelated `qa-report.md` column
  defect and leave the positive case unprovable — is **unfounded**: the build
  succeeds and the queries return real data (A5). The genuine residual
  limitation is narrower: *this* repo is Markdown-only, so `impact` and
  `story_trace`'s Code leg have nothing to index here. The positive case must
  therefore be run in a **source-indexed** repo, and `~/aSPARK-graph` is
  verified to be one. Mitigation: name that venue in the evidence record
  (NFR-9). No release-blocking uncertainty remains.
- **R6 — A `files:` note that lies.** A declared link beats an inferred one
  downstream, so an inaccurate note is a *downgrade* from having none.
  Mitigation: AC-5.2 (omit rather than guess). Post-build correction is
  consciously out of scope (C10), so the risk is accepted for this cycle and is
  the first candidate for a follow-up.
- **R7 — `tools/` stays a one-element abstraction.** Accepted deliberately: the
  cost is one directory and one guide, and the rejected alternative (the same
  text duplicated across three skills and three agents) is more expensive from
  the second tool onward. The name is now a public commitment (C12), so renaming
  it later is a breaking change.
- **R8 — Marginal value for the population (reduced).** Beneficiary count for
  the graph wiring is ≈1 today (§1), so US-2–US-4 largely pay for one user's
  convenience. **What changed:** US-5 is no longer the only unconditionally
  valuable part *and* an optional one — it is a Must (C12), it improves every
  plan whether or not a graph exists, and it is what makes `impact` answer a
  story-level question at all. The weakest-value slice is therefore now the
  detection and pass-through work alone, not the feature as a whole.
- **R9 — Empty-by-construction answers on legacy plans.** Every plan written
  before this change carries no `files:` notes, so `impact`'s
  `affected_stories`/`affected_acs` stay empty for them indefinitely (no
  backfill, §6). An agent reading that as "no story at risk" is the same defect
  that got `gate_health` cut. Mitigation: AC-4.5 makes the caveat explicit at
  the point of use, and NFR-6 makes it grep-verifiable.

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — 5 Must, 1 Should; US-5's promotion is justified in its priority note (C12)
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason) — NFR-1..13, `library` lens fully mapped
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C12 resolved and folded
- [x] Open questions are resolved or explicitly accepted as risk — **Q1–Q6 all resolved by the user on 2026-07-25 (C7–C12)**; A2/A3/A6 remain accepted assumptions with named risks R1/R4/R6
- [x] Out-of-scope section is filled (something was consciously cut) — including half the briefed query surface
- [x] Constitution (`.spark/constitution.md`) respected — §6's degrade-to-silence is US-1/NFR-5, §3's template contract is AC-5.3/NFR-1, §4's evidence bar is NFR-10; **no conflict found**
- [x] Design review done for UI-facing features (or marked N/A with reason) — **N/A, see §8**
- [x] Status set to `approved` by the user — given explicitly in conversation on 2026-07-25, after review of the MoSCoW split (5 Must / 1 Should) and the US-5 promotion argument (C12); **and the C13 narrowing of AC-1.2 authorised 2026-07-26**, during round-2 finding routing. Noted here because this box is where a reader checks the approval, and the 2026-07-25 approval predates the AC-1.2 text now in §4

> **Note for planning.** Everything about *how* — the `tools/` directory's
> internal shape, the frontmatter fields, how a skill probes for MCP tools, how a
> failing MCP call is classified relative to detection states 3 and 4 — is
> deliberately absent here and belongs to `/sprint-plan`. The brief's §5 task
> breakdown is input to that ceremony, not to this spec; note that its step 5 is
> dropped as unverifiable (C5), its T2 query list is narrowed by C1/C7, and **T5
> is no longer optional** — it serves a Must story and its ordering should
> reflect that US-2's Plan-phase value depends on it (C12).
