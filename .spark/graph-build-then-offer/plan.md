# Plan: graph-build-then-offer

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/graph-build-then-offer/spec.md` (must be `approved`) |
| **Status** | `approved` |
| **Date** | 2026-11-16 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Keep the existing step 1 probe and extend its four-state table in place: surface yes + graph.json no builds once; stale rebuilds once; one build budget per run shared by ceremony and agent; the three agents get body text to call the graph themselves. Constitution §3/§6 amended first. No new file, no new step.
- **Open:** `8 tasks not done` — see §3 Task Breakdown for which
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** Spec `approved` (checked). Plugin is Markdown only, no test suite (`constitution.md §4`, §9 stack: cited, not re-derived). Re-derived from source, because the feature touches exactly this area and §9 does not describe it: the probe paragraph exists in `skills/sprint-plan/SKILL.md:29-44`, `skills/peer-review/SKILL.md:29-44`, `skills/demo-day/SKILL.md:62-78` and `tools/README.md:100-117`; its four-state table and the ban are in `tools/aspark-graph.md:30-39`; "Stale ⇒ absent" is at `:79-81`. The ban contradicts the spec, and the constitution forbids auto-build (`constitution.md:136`, `:203-205`), so the constitution is amended first (spec A1, ruled (a)).
- **Decision:** Edit the existing rules in place; add nothing structural. (1) `tools/aspark-graph.md` owns the full rule: state table rows `yes/no` build once, `Reading a result` says rebuild once then query, a **build budget** (at most one build or rebuild per run across ceremony and agent; a build makes the graph fresh, so no `staleness` follows), failure said once and graph treated as absent, the closing-report line, and "only `build_graph`, `staleness`, `impact`, `story_trace` may be called; never `gate_health`". (2) The probe paragraph stays one paragraph, identical in the three skills (demo-day keeps its permitted variation) and in `tools/README.md`; it gains only the build step and the closing-report clause, each pointing at the tool file for detail, within the 10-line growth cap (NFR-5). (3) Each agent body states the allowed calls itself (the file the agent reads at the moment it acts, per `CLAUDE.md`). Builder: MCP `build_graph`, else `aspark-graph build .`, else the unchanged hint.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Keep naming the command, only reword the hint | That is today's behaviour; E2 showed zero calls. Spec A1 option (b) |
  | Let each agent build when it needs the graph | Two builders, no shared budget, build inside delegated contexts the ceremony cannot report on; breaks AC-1.4 and AC-2.3 |
  | New step in each skill ("Build graph") | "No new numbered step is ever added" (`tools/README.md:91-92`); a count change means wrong wiring |
  | Narrow the nine-tool `tools:` lists to four | Out of scope (A7, C7); body text carries the limit |
  | Put the full rule in the skills, not the tool file | Triplicates prose, breaks NFR-5 and "identical" |
- **Consequences:** Easier: a fresh checkout or post-`/increment` repo gets a usable graph without a manual step; one source of truth for the rule. Harder: the "yes/no" state now executes a command, so NFR-3 safety (only `.aspark-graph/` written) must be checked by `git status`; behaviour is prompt material, only likely (NFR-1).

## 2. Affected Components

Blast radius: **not run.** The graph is unbuilt in this checkout (`staleness` returned `found: false`), the repo is Markdown-only (no source files indexed, `tools/aspark-graph.md:93-95`), and the plan was scoped **by hand** from grep. An empty `impact` here would mean the plan declares no linkable code, not that nothing is at risk.

- `.spark/constitution.md` §3 (`:136`), §6 (`:203-205`), Amendments table.
- `tools/aspark-graph.md`, `tools/README.md` (probe copy `:100-117`).
- `skills/sprint-plan/SKILL.md`, `skills/peer-review/SKILL.md`, `skills/demo-day/SKILL.md`.
- `agents/engineering-manager.md`, `agents/reviewer.md`, `agents/qa-tester.md` (body only; no `tools:` change, A7).
- Docs that state "nothing builds": `docs/family.md:47`; maturity labels: `docs/status.md:110`, `:155`, `README.md:186`. `docs/status.md:155` records proof of the superseded v0.17 behaviour (hint once, stale absent); it is annotated, not rewritten.
- Checked, no change (A10): `/spark`, `/increment`, `/go-live`, `campaigns/README.md`. No `templates/` change, no new dependency.

**Dispatch and activation per claimed phase (AC-5.2).** `tools/aspark-graph.md:3-5` claims `phases: [plan, review, qa]`, `activation: installation-state`. Activation for all three is the step 1 probe, run after the ceremony's gate.

| Phase | Ceremony probe (activation) | Pass to agent (dispatch) | Agent reads it | Other site |
|---|---|---|---|---|
| plan | `skills/sprint-plan/SKILL.md:29-44` | `:52-53` | `agents/engineering-manager.md:98-112` | relay of tool query request `:60-64` (kept) |
| review | `skills/peer-review/SKILL.md:29-44` | `:57-59` | `agents/reviewer.md:128-139` | none |
| qa | `skills/demo-day/SKILL.md:62-78` | `:90-92` | `agents/qa-tester.md:159-168` | none |

The three step 1 probes are the only activation sites; no lens or `/charter` vocabulary names this tool (grep of `skills/` and `agents/` showed no other `aspark-graph` mention; `README.md:186`, `docs/family.md:18,43-49` only describe it).

## 3. Task Breakdown

<!-- Order: constitution first (everything else is blocked by it), then the rule, then its copies, then agents, then docs, then verification. Negative case runs first inside T6, per constitution §1. -->

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Amend constitution: §3 off-limits and §6 "nothing executed unasked" each allow **one** build or rebuild that writes only `.aspark-graph/`, only when a graph surface is present; install, serve and every other command stay forbidden. Add one Amendments row (2026-11-16, change, why: E2 zero calls, spec A1) | US-1, US-2 | AC-1.1, NFR-3 | – | `done` | `grep -n "auto-build" .spark/constitution.md` shows each remaining hit qualified by the one-build exception; the Amendments table has a new last row citing `.spark/graph-build-then-offer/spec.md` A1; no other section text changes (`git diff` limited to those lines) — files: .spark/constitution.md |
| T2 | Rewrite the rule in the tool file: table row `yes/no` = build once (MCP `build_graph`; no `build_graph` or CLI only = `aspark-graph build .`; neither runnable = old hint, AC-1.5), then treat as `yes/yes`; replace "Never run `build`…" paragraph with the one-build budget (ceremony and agent share it; fresh after build, no `staleness`); replace "Stale ⇒ absent" with rebuild once then query, absent only after failed or ineffective rebuild; failure said once; the one build/failure sentence goes in the closing report; slices say only `build_graph`, `staleness`, `impact`, `story_trace` may be called, never `gate_health`; QA slice rule on `qa_checks`/`latest_result` unchanged; four-state table, one-hint rule and "outcome never changes a gate" stay | US-1, US-2, US-4 | AC-1.1, AC-1.3, AC-1.4, AC-1.5, AC-2.1, AC-2.2, AC-2.3, AC-2.4, AC-4.4, NFR-3 | T1 | `done` | `grep -n "Stale ⇒ absent" tools/aspark-graph.md` returns nothing as an unconditional rule; `grep -n "Never run" tools/aspark-graph.md` finds no sentence forbidding `build`/`build_graph`; the no/no and no/yes rows are byte-identical to v0.17.0 (`git diff v0.17.0 -- tools/aspark-graph.md` shows no hunk in them); the reference diff `git diff v0.17.0 b3574cb -- tools/aspark-graph.md` was consulted and no review round cap taken — files: tools/aspark-graph.md |
| T3 | Extend the probe paragraph in all four copies with the build step (pointing at the tool file), the closing-report clause and "one build per run"; keep wording identical across `sprint-plan`, `peer-review`, `tools/README.md` and `demo-day` (permitted variation only); update `tools/README.md` surrounding text that says "verbatim" and any no-build statement; keep `/sprint-plan` step 3 relay, but delete "Never run a build" from it only as far as the budget now allows, keeping "nothing that writes" for the relayed query | US-1, US-2, US-4 | AC-1.1, AC-1.3, AC-1.4, AC-4.1, AC-4.2, AC-4.4, AC-5.1, NFR-2, NFR-5 | T2 | `done` | `diff` of the paragraph extracted from the three skills and `tools/README.md` is empty except demo-day's two documented phrases; each file grows ≤ 10 lines net (`git diff --numstat`); the four-state wording, "at most once" and "never let the outcome change a gate" are still present in each (`grep -c`); the no/no and no/yes sentences unchanged vs v0.17.0; `/sprint-plan` step 3 still names the tool query request relay — files: skills/sprint-plan/SKILL.md, skills/peer-review/SKILL.md, skills/demo-day/SKILL.md, tools/README.md |
| T4 | Agent bodies: engineering-manager calls `impact` itself on the union of `files:` paths after cutting tasks, the "tool query request" path applies only when the tools are not exposed; all three bodies state `build_graph`, `staleness`, `impact`, `story_trace` may be called when exposed (`build_graph` only if the run's budget is unspent), `gate_health` never; reviewer keeps its slice; qa-tester gets body text only (no `tools:` line) and keeps "no `Result` cell rests on a graph answer", `qa_checks`/`latest_result` unread; no tool file passed = no graph call | US-3 | AC-3.1, AC-3.2, AC-3.3, AC-3.4, AC-2.3 | T2 | `done` | `grep -n "gate_health" agents/engineering-manager.md agents/reviewer.md agents/qa-tester.md` hits each file with "never"; `git diff -- agents/qa-tester.md` touches no frontmatter line; `agents/engineering-manager.md` no longer says the ceremony makes the call as the default; the three `tools:` lines are unchanged (`git diff` shows no hunk on them) — files: agents/engineering-manager.md, agents/reviewer.md, agents/qa-tester.md |
| T5 | Docs agree: `docs/family.md:47` no longer says nothing builds it (states: one build writing only `.aspark-graph/`, when present); `README.md:186` and `docs/status.md:110` label the new behaviour as prompt material, unproven until measured; annotate `docs/status.md:155` as proof of the v0.17 behaviour now superseded; `tools/README.md` available-tools entry agrees | US-5 | AC-5.1, AC-5.3 | T2, T3 | `done` | `grep -rniE "never run .{0,20}build|nothing in aSPARK installs, builds|no auto-build" README.md docs tools skills agents` returns no statement that a build is forbidden (hits in `.spark/` history and `constitution.md` Amendments are expected and excluded); `docs/status.md` and `README.md` each say "unproven until measured" for the build/rebuild/call behaviour — files: docs/family.md, README.md, docs/status.md, tools/README.md |
| T6 | Development check, negative case first (constitution §1): with no surface and no `graph.json`, run each of `/sprint-plan`, `/peer-review`, `/demo-day` in a scratch repo, ≥ 3 sessions each as development matrix; then surface-yes/graph-no (build + `git status`), stale (rebuild once, second stale step no second build), build-failure (one sentence in closing report, no gate change), no-`build_graph` and no-runner cases. Write the grep checks of T1-T5 and every observed result, with the method and counts, into the evidence file. Development figures are disclosed only | US-1, US-2, US-3, US-4 | AC-1.2, AC-1.3, AC-1.4, AC-1.5, AC-2.2, AC-4.1, AC-4.2, AC-4.3, NFR-2, NFR-3 | T3, T4 | `todo` | `.spark/graph-build-then-offer/evidence.md` exists with the no-surface case first, one row per case above, each a performed session or a command with its observed output (reading and reasoning is marked `not-verified-live`); `git status` after a build shows changes only under `.aspark-graph/` — files: .spark/graph-build-then-offer/evidence.md |
| T7 | After `/demo-day` (QA, not an `/increment` task): copy the **registered QA set** results into the docs: per-behaviour counts, the pooled and development figures labelled as disclosed only, and the sentence that prompt material makes build, rebuild and agent calls likely, never certain. A miss is recorded as refuted-with-finding, not reworded | US-5 | AC-5.3, NFR-1 | QA verdict | `todo` | `docs/status.md` and `README.md` carry the measured X of 10 per behaviour (build when missing, rebuild when stale, EM calls `impact`) and the no-surface 10 of 10 per ceremony, each tied to `.spark/graph-build-then-offer/qa.md`; no figure from the development matrix is used as a pass — files: docs/status.md, README.md |
| T8 | Release bookkeeping flagged, not done here: version is a minor bump at `/go-live` (NFR-4); this task only confirms no slash command, template heading, column or ID changed | US-4 | NFR-4 | T3, T4 | `done` | `git diff --stat -- templates skills/*/SKILL.md` shows no `templates/` file and no frontmatter hunk; `git diff` shows no change to a command name, column or ID pattern — files: .spark/graph-build-then-offer/evidence.md |

## 4. Test Strategy

Constitution §4: there is no test suite and none is possible; no unit or integration tests. Verification is two kinds only: **grep/diff checks** (T1-T5, T8, structural, cheap, run by the developer and the Reviewer) and **performed sessions** (T6 development, `/demo-day` QA). Reading a file and reasoning is never a pass (`constitution.md §8`).

- **Negative case first** (constitution §1, NFR-2): no surface, no `graph.json`, per ceremony. QA floor is **10 of 10 per ceremony** showing no graph mention, no extra command, wording as at v0.17.0.
- **Registered QA set** (decided now; it alone decides pass or fail, NFR-1): ten sessions per behaviour, floor **8 of 10** each: (a) surface yes, no `graph.json`: builds once and the report names a graph result (AC-1.1); (b) stale: rebuilds once then queries, no stale citation (AC-2.1); (c) EM calls `impact` itself after cutting tasks (AC-3.1). The development matrix (T6) and any pooled figure are disclosed, never used to claim a pass. **Expected gap:** QA scores below development (`CLAUDE.md`: 9 of 10 development became 5 of 10 at QA); stated here, not promised away.
- **Prompt material makes these likely, never certain** (A9). The build, rebuild, call and closing-report line are instructions, not enforcement; the docs say so with the measured rate (T7). If one wording only moves the failure between poles, the fix is structural, not a fifth rewording.
- Left to `/demo-day`: AC-1.2 and NFR-3 (`git status` after a build), AC-1.4 (the line is in the closing report, where output is written), AC-3.1, AC-3.3, AC-2.3 (second stale step triggers no second build). Left to `/peer-review`: NFR-2 diff on the no/no and no/yes sentences, NFR-4, NFR-5 line counts, the identical-paragraph diff.
- Honesty note: AC-1.1, AC-2.1, AC-3.1, AC-1.4 can only be made likely by prompt material; they are the ACs QA may record as `partial` with the measured rate.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Ceremony builds but agent also builds (budget not honoured) | Two builds, NFR-3/AC-2.3 breached | Budget stated in the tool file and in each agent body (the file the agent reads); T6 session where an agent sees stale after a build |
| The build/failure sentence is not in the closing report (mid-run "say X" rarely spoken, `CLAUDE.md`) | AC-1.4 missed | Clause lives in the probe paragraph's closing-report wording and the tool file; measured in T6; structural fix if wording only moves it |
| Edit drifts the no/no and no/yes text | NFR-2 regression, silent break for users without the tool | `git diff v0.17.0` on those sentences is a T2/T3 DoD; Reviewer re-derives it fresh |
| Four probe copies diverge | Contradicting ceremonies | T3 extracts and diffs the paragraphs; demo-day variation named |
| Build writes outside `.aspark-graph/` (e.g. a tracked file) | NFR-3 safety | `git status` check in T6 and QA; constitution amendment limits scope |
| Taking the reference diff `b3574cb` brings a review round cap | Out-of-scope change | T2 DoD forbids it; Reviewer greps for round cap text |
| QA floor missed (8 of 10) | Success signal unmet | Recorded as refuted-with-finding, routed to a later increment; no endless rewording |
| Blast radius not run (graph unbuilt, Markdown-only repo) | Missed affected file | Scoped by hand with grep over `skills/ agents/ docs/ README.md tools/`; Reviewer re-greps for "never run build" |
| Assumption inherited: A7 leaves nine-tool lists incl. `gate_health` | Agent could call it | Body text says never; tool file repeats it; no `tools:` edit |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded) — conflict with §3/§6 recorded and carried by T1
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Line budget respected: Ist ~95 / Soll ~300 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [x] Status set to `approved` by the user
