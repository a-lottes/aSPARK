# Spec: graph-build-then-offer

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-11-16 |
| **Ticket** | #125 (a-lottes/aspark; this spec was seeded from it) |
| **Path** | `full` |
| **Gate comment** | none |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** The graph is never used in a fresh checkout or after `/increment`, because the ceremonies forbid a build and treat stale as absent. Goal: build once, rebuild once when stale, let the three agents call the graph, and change nothing where no graph surface exists.
- **Open:** `0 open` — A1 ruled (a) in autonomous mode (Factory-selected recommended option, not a personal confirmation): the plan amends constitution §3/§6; the PR reviewer sees it.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed since the last round and why
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** In experiment E2 the graph was available and recommended, and no session called it once. Three causes sit in aSPARK itself, verified against the repo at v0.19.0:
  1. `/sprint-plan`, `/peer-review` and `/demo-day` (step 1, "four states") pass `tools/aspark-graph.md` only when `.aspark-graph/graph.json` already exists, and `tools/aspark-graph.md:37` forbids building it. A fresh checkout never gets a graph (`tools/aspark-graph.md:33` only names the build command to the user).
  2. `tools/aspark-graph.md:79` says "Stale => absent". After `/increment` the graph is stale, so it counts as absent exactly at review and QA.
  3. The agent side is half done. v0.19.0 put the graph tools into the `tools:` lists of `engineering-manager` (`agents/engineering-manager.md:8`) and `reviewer` (`agents/reviewer.md:9`). But the engineering-manager body still says it has no shell and returns a "tool query request" (`agents/engineering-manager.md:98-105`), and `agents/qa-tester.md` says nothing about the graph (no `tools:` line, so it inherits all tools).
  Pain is felt by the maintainer and by users of an installed aSPARK who have `aspark-graph` on the machine: they installed it to scope work and the loop never uses it.
- **Goal:** With a graph surface present, the ceremonies make the graph usable (build once if missing, rebuild once if stale) and the plan, review and QA agents can call it. With no surface, nothing changes.
- **Success signal:** In a registered set of sessions on a repo with a surface but no `graph.json`, the ceremony builds once and the agent's report names a graph result that scoped its reading (floor in NFR-1). In a repo with no surface, ceremony output is unchanged from v0.17.0.
- **Why now:** Without this the graph tool is shipped, documented and measured as unused (E2: zero calls). v0.19.0 removed the tool-list blocker, so the remaining blockers are the three prompt texts above.

## 2. Target Users

- **Maintainer / user of an installed aSPARK with `aspark-graph` available** (MCP server registered, or runner on `PATH`) who runs `/sprint-plan`, `/peer-review` or `/demo-day`. Often a fresh checkout, or just after `/increment`.
- **Not affected:** users with no graph surface (the large majority); they must see no change.
- Plugin context (stack, entry points): `constitution.md §9`. Re-derived from source: the probe paragraph and tool file, because the feature touches exactly that area (§9 does not describe it).

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | **Conflict with the constitution.** §3 Off-limits: "no auto-build, no auto-execute on the user's behalf"; §6: "Nothing is executed or installed on the user's behalf unasked — no auto-build". Build-then-offer is an auto-build. The issue does not amend the constitution. | **RULED (a)** at the spec gate, autonomous mode: option recommended and taken by the Factory. The plan carries a constitution amendment task. Options for the user: (a) amend §3/§6 via `/charter` to allow one build that writes only `.aspark-graph/`, when a surface is present; (b) reject US-1/US-2's build and keep "name the command". Recommendation: (a), because the issue's whole purpose is that naming the command did not work (E2). Amendment is limited to: one build/rebuild writing only `.aspark-graph/`, only with a surface present. |
| A2 | Original phrasing recorded: "State `surface yes, graph.json no` becomes build, then offer" and "Stale means rebuild once". Translated to the need: the graph must be usable without a manual step by the user. | Stories below. |
| A3 | "Surface" keeps today's meaning: MCP tools ending in `staleness` and `impact`, or `aspark-graph` on `PATH`. Detection is not widened. | Decided. |
| A4 | Who builds: the ceremony, in its existing step 1 probe, after the gate has passed. MCP: `build_graph`; if the session exposes `staleness`/`impact` but no `build_graph`, or CLI only: `aspark-graph build .`. If neither can run (no runner on `PATH` and no `build_graph`), the existing "yes/no" hint sentence applies unchanged. | Decided. |
| A5 | One build budget per ceremony run, shared by the ceremony and the agent it delegates to: at most one build or rebuild in total. An agent calls `build_graph` only if the budget is unspent. | Decided. |
| A6 | A graph built in this run is fresh by definition, so no `staleness` check follows it. | Decided. |
| A7 | The v0.19.0 `tools:` lists (nine graph tools each, including `gate_health`) are left as they are (scope fence). The agent bodies and the tool file state that only `build_graph`, `staleness`, `impact` and `story_trace` may be called, and `gate_health` never. `agents/qa-tester.md` gets body text only, no `tools:` line (adding one would restrict it). | Decided; narrowing the lists is out of scope. |
| A8 | The constitution's `Ticket` format is `none` (§7, to keep real ticket IDs off the public `.spark/`). The caller instructed `#125`. Issue numbers of this public repo are not private. | Followed the caller's instruction; flagged here. |
| A9 | Prompt material makes the build, rebuild and call behaviours likely, never certain (CLAUDE.md, "Prompt material makes a check likely"). | NFR-1 states the floor up front. |
| A10 | `/spark`, `/increment`, `/go-live` and `campaigns/README.md` were checked: none states graph probe or build behaviour (`campaigns/README.md:56-61` only says the graph skips campaign directories). No change needed there. | Verified by grep. |

## 4. User Stories

### US-1 (Must): Build, then offer

> As a user with `aspark-graph` available but no built graph, I want the ceremony to build it once, so that the plan, review and QA agents actually get the graph instead of a hint I never act on.

**Acceptance criteria:**

- [ ] AC-1.1: Given a surface (MCP or runner) and no `.aspark-graph/graph.json`, when `/sprint-plan`, `/peer-review` or `/demo-day` passes its gate, then it builds once (`build_graph` over MCP, otherwise `aspark-graph build .`), and on success passes `tools/aspark-graph.md` to the agent as in the existing "yes/yes" state.
- [ ] AC-1.2: Given that build, when it finishes, then `git status` shows no change outside `.aspark-graph/`.
- [ ] AC-1.3: Given the build fails (non-zero exit or `{"found": false, "error": …}`), when the ceremony continues, then the failure is said exactly once, the tool file is not passed, the ceremony reaches its normal verdict, and no gate changes.
- [ ] AC-1.4: Given a build or a failed build, when the ceremony ends, then the one sentence about it is in the closing report (where the output is written), not only mid-run.
- [ ] AC-1.5: Given a surface that offers neither `build_graph` nor a runner on `PATH`, when the ceremony resolves it, then the existing hint sentence is said once and the ceremony continues without the graph.

### US-2 (Must): Stale means rebuild once

> As a user who just ran `/increment`, I want a stale graph rebuilt once and then queried, so that review and QA do not lose the graph exactly when they need it.

**Acceptance criteria:**

- [ ] AC-2.1: Given a surface, a `graph.json` and `staleness` returning `stale: true`, when the ceremony or its agent resolves the graph, then it rebuilds once and then queries; the stale result is not cited as evidence.
- [ ] AC-2.2: Given the rebuild fails or `staleness` still reports stale after it, when the run continues, then this is said once, the graph is treated as absent for the rest of the run (no result cited, fall back to reading and grep) and the verdict is reached as usual.
- [ ] AC-2.3: Given a build or rebuild already happened in this run, when any later step sees stale, then no second build runs (one build budget, A5).
- [ ] AC-2.4: `tools/aspark-graph.md` no longer contains the rule "Stale ⇒ absent" as an unconditional rule; the "Reading a result" section states rebuild once, then query, and absent only after a failed or ineffective rebuild.

### US-3 (Must): The three agents may use the graph; the engineering manager queries impact itself

> As the engineering manager, reviewer and QA tester, I want to call the graph myself when the session exposes it, so that I do not wait on a caller round-trip or skip it.

**Acceptance criteria:**

- [ ] AC-3.1: Given the session exposes `impact` to the engineering manager, when it has cut tasks with `files:` notes, then it calls `impact` itself on the union of those paths, and the "tool query request" path in `agents/engineering-manager.md` applies only when its tools are not exposed. `/sprint-plan` step 3's relay of a tool query request is kept for that case.
- [ ] AC-3.2: `agents/engineering-manager.md`, `agents/reviewer.md` and `agents/qa-tester.md` each state, in their own body, that `build_graph`, `staleness`, `impact` and `story_trace` may be called when exposed, and that `gate_health` is never called.
- [ ] AC-3.3: Given the QA agent uses `story_trace`, when it fills `qa.md`, then no `Result` cell rests on a graph answer and the QA leg (`qa_checks`, `latest_result`) is not read (existing QA slice rule, unchanged).
- [ ] AC-3.4: Given no tool file was passed, when any of the three agents runs, then it works as it does today and calls no graph tool.

### US-4 (Must): Without a graph surface nothing changes

> As a user without `aspark-graph`, I want the ceremonies to read and behave exactly as at v0.17.0, so that an optional tool never costs me anything.

**Acceptance criteria:**

- [ ] AC-4.1: Given no surface and no `graph.json`, when any of the three ceremonies runs, then it says nothing about the graph, runs no command beyond the existing probe, and its output matches a v0.17.0 run in structure and wording.
- [ ] AC-4.2: Given no surface and an existing `graph.json`, when the ceremony runs, then the existing one-sentence "no runner reachable" hint fires at most once and the ceremony continues without the graph.
- [ ] AC-4.3: Given any state, when the graph outcome is anything at all (built, failed, stale, absent), then no gate (spec gate, plan gate, review verdict, QA verdict) changes because of it.
- [ ] AC-4.4: The four-state table, the "at most one hint sentence per run" rule and "never let the outcome change a gate" are still present in `tools/aspark-graph.md` and the three skills.

### US-5 (Should): The docs agree and every claimed phase is checked

> As a maintainer, I want one consistent statement of the new states in every file that carries it, so that no file contradicts another.

**Acceptance criteria:**

- [ ] AC-5.1: `tools/aspark-graph.md`, `skills/sprint-plan/SKILL.md`, `skills/peer-review/SKILL.md`, `skills/demo-day/SKILL.md` and `tools/README.md` (its copy of the probe paragraph, "change in all three or nowhere") describe the same states; `grep -ri "never run .*build"` and similar find no remaining statement that a build is forbidden across the repo (`README.md`, `docs/status.md`, `docs/family.md`, `tools/README.md` included).
- [ ] AC-5.2: For each phase the tool file claims, the plan records dispatch and activation by file and line: plan (`/sprint-plan` to `engineering-manager`), review (`/peer-review` to `reviewer`), qa (`/demo-day` to `qa-tester`); activation is `installation-state` via the step 1 probe of each. (CLAUDE.md, "An add-a-file scope check must examine every phase the artifact claims".)
- [ ] AC-5.3: The docs that describe the graph's maturity (`docs/status.md`, `README.md`) label the new behaviour as prompt material with its measured rate, or as unproven until measured (constitution §1, honesty about maturity).

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Reliability (prompt material) | **Build, rebuild and agent-call behaviour is only likely, never guaranteed.** The floor is carried by the **registered QA set**: ten registered `/demo-day`-style sessions per behaviour (build when missing = AC-1.1; rebuild when stale = AC-2.1; EM calls `impact` itself = AC-3.1), floor 8 of 10 each. Development-matrix and pooled figures are disclosed only, never used to claim a pass. Expect QA to score below the development rate (CLAUDE.md). The measured rates are written into `tools/aspark-graph.md` or `docs/status.md` at QA. A miss is recorded as refuted-with-finding, not reworded endlessly; if wording only moves the failure, the fix is structural (CLAUDE.md). | /demo-day (performed sessions) |
| NFR-2 | Backward compatibility | Without any graph surface, 10 of 10 registered sessions per ceremony show no graph mention and no extra command. The step 1 text for the no/no and no/yes states is kept word for word as at v0.17.0 where those states apply (`git diff v0.17.0` on those sentences is empty). Constitution §4 and §6. | /peer-review (diff), /demo-day (negative case first) |
| NFR-3 | Safety | The only write the feature allows is `.aspark-graph/`; at most one build per run; no `install`, `serve` or any other command is run. | /demo-day (`git status` after a build), /peer-review |
| NFR-4 | Contract (library lens) | No slash command, template heading, column or ID pattern changes; no `templates/` change; no version bump rule broken (a new optional capability is a minor bump at release). | /peer-review |
| NFR-5 | Doc size | Plugin Markdown only (no executable code, constitution §3); each edited ceremony file grows by no more than 10 lines net; the probe paragraph stays textually identical across the three skills and `tools/README.md`. | /peer-review |
| NFR-6 | Accessibility, performance, security, observability | N/A: no UI, no runtime, no network surface of our own (constitution §2, §4). The one live concern, executing an external command, is A1. | n/a |

Active lens `library` (public surface, compatibility, contract clarity): covered by NFR-2 and NFR-4. All other lenses are off.

## 6. Out of Scope

- **The review round cap of the experiment branch (`b3574cb`)**: not taken over.
- Changes in the `aspark-graph` repo, including its artifact-filename mismatch (`review-report.md` vs `review.md`); `gate_health` and `story_trace`'s QA leg stay unwired (`tools/aspark-graph.md` "Not wired").
- Building or probing in `/spark`, `/increment`, `/go-live`, `/story-time`, `/look-and-feel`, `/campaign` (no graph text there today, A10).
- Narrowing the v0.19.0 `tools:` lists or adding a `tools:` line to `qa-tester` (A7).
- Installing `aspark-graph`, starting its server, registering its MCP server, or an offer to do so beyond today's companion offer.
- Widening what counts as a surface, or a background or scheduled rebuild.
- A new tool file or lens (the constitution's "new concern is a new file" does not apply: this edits an existing tool's rules).
- Anything the Factory adds at agent start (independent of this change).

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-11-16 | Does auto-build conflict with the constitution? | Yes (§3, §6). Ruled (a) in A1: amend. |
| C2 | 2026-11-16 | Who runs the build: ceremony or agent? | Ceremony in step 1; agents may build only if the single budget is unspent (A4, A5). |
| C3 | 2026-11-16 | What if only `staleness`/`impact` are exposed, no `build_graph`? | Fall back to the runner on `PATH`; else the existing hint (AC-1.5). |
| C4 | 2026-11-16 | Check staleness right after a fresh build? | No, fresh by definition (A6, AC-2.3). |
| C5 | 2026-11-16 | Where must the build or failure sentence appear? | In the closing report (AC-1.4), per the CLAUDE.md lesson on mid-run "say X" rules. |
| C6 | 2026-11-16 | Which floor decides prompt-material pass/fail? | The registered QA set, 8 of 10 per behaviour; other figures disclosed only (NFR-1). |
| C7 | 2026-11-16 | Should the nine-tool lists shrink to four? | No, out of scope (A7). |

## 8. Design Review

N/A: not UI-facing (Markdown-only plugin, no UI of any kind).

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked
- [x] Open questions are resolved or explicitly accepted as risk (A1 ruled (a))
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions (A1, ruled; amendment planned)
- [x] Design review done for UI-facing features (or marked N/A with reason)
- [x] Line budget respected: Ist ~165 / Soll ~250 (excluding HTML comments) — self-reported, no linter checks this
- [x] Status set to `approved` by the user (Factory autonomous mode)
