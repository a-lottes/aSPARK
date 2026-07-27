# Plan: graph-gates

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/graph-gates/spec.md` (status `approved`, 2026-07-25) |
| **Status** | `approved` |
| **Date** | 2026-07-25 |

> **Revision 2 — 2026-07-25, after `/peer-review` returned `changes-requested`.**
> Finding **F3** (`.spark/graph-gates/review.md`) invalidated the test strategy at
> its root: Claude Code executes skills and agents from the **installed plugin
> cache**, not from this working tree, so no ceremony run in this session exercises
> the changed material. §4 is rewritten around the three evidence methods that are
> actually available — static verification, parser-in-the-loop verification against
> the consumer's real code, and a manual walkthrough of the written instructions —
> and every criterion that now ships **not proven** is named as such. T11–T15 are
> reconsidered one by one; what this session cannot do is restated as a
> post-release checklist owned by the user. The architecture decision in §1 is
> **unchanged**: nothing in F1–F9 challenged the design, only its verification and
> two pieces of shipped text. Status returns to `draft` for the user's
> re-approval.

> **Scope source.** The spec is binding, including its §6 list of documented "no"s.
> `.spark/graph-gates/PATCH-PLAN.md` was input only; where it and the spec differ,
> the spec wins. Three of its statements are stale and are **not** planned back in:
> `gate_health` is cut entirely (spec §6, C1/C7), its test step 5 is replaced by a
> diff-only check (AC-5.3/NFR-1), and its optional T5 (the DoD path note) is a Must
> here and is ordered **before** the wiring that consumes it (C12).
>
> This plan is itself the first artifact written under the pre-change rules; its
> DoD cells already carry the path note that T2 introduces — the plan dogfoods its
> own change, and all fifteen of its cells were parsed clean by the consumer's real
> parser during review.

> **Five planning questions, resolved by the user on 2026-07-25 before build.**
> **P-Q1 — the reading of AC-1.1's zero-occurrence bar:** the checkable surface is
> the produced **artifact** plus the ceremony's **user-visible output**; detection
> tool-calls and file reads are excluded, on the grounds that a spec mandating a
> CLI probe (AC-2.3) cannot forbid the probe from existing. Refined further by
> deviation **D3** (volunteered mentions). **P-Q2 —** `/sprint-plan` relays the
> Plan-phase query; the EM stays read-only, no `Bash` grant. **P-Q3 —** the fourth
> availability state (graph data present, no runner reachable) exists as its own
> single sentence, distinct from AC-2.3's unbuilt-graph hint, and the two can never
> both fire in one run. **P-Q4 —** the evidence record is
> `.spark/graph-gates/evidence.md`. **P-Q5 —** `/increment` drives all tasks
> including the verification ones, with the user's explicit go before each command
> that writes anything in `~/aSPARK-graph`.
>
> **Two further decisions taken on 2026-07-25, after F3.** The user **rejected**
> installing this working tree as the active plugin, and **rejected** overwriting
> the plugin cache. Neither is planned. They also rejected shipping on static
> evidence alone — hence the walkthrough method in §4.

## 1. Architecture Decision

<!-- Mini-ADR. The EM decides — but shows the alternatives that were rejected and why. -->

- **Context:** Core is Markdown prompt material with no runtime, no tests and no
  dependencies (constitution §3), installed into arbitrary projects. It must be
  able to *offer* an external, install-from-source capability
  (`aspark-graph` v0.5.0) in three ceremonies without acquiring a dependency on
  it and without any project that lacks it noticing (US-1, NFR-5, constitution
  §6). The repo already has exactly one mechanism for optional, situational
  knowledge — `lenses/`: a file whose path a skill passes to its agent, which
  reads its own phase slice (`lenses/README.md`). A lens is activated by the
  constitution's *project profile*; a tool is activated by *installation state*,
  which no profile can know. Two hard facts constrain the shape:
  1. **The runner is not reliably reachable.** Verified 2026-07-25: the CLI lives
     at `~/aSPARK-graph/.venv/bin/aspark-graph` and is **not** on `PATH`, so
     `command -v aspark-graph` fails in precisely the environment where the tool
     exists. The MCP surface (FastMCP server `aspark-graph`, tools `staleness`,
     `impact`, `story_trace`, `gate_health`, `build_graph` —
     `~/aSPARK-graph/src/aspark_graph/server.py`) does not have this problem: a
     registered server is visible in the session's tool list with no probe at all.
     Its tools are exposed **namespaced** as `mcp__<server>__<tool>`, so detection
     must match on names *ending in* `staleness` / `impact` (F2).
  2. **The consuming side is ready and idle.** `_files_note`
     (`~/aSPARK-graph/src/aspark_graph/artifacts.py:351`) already parses an inline
     path note out of a DoD cell with `re.compile(r"files:\s*([^|]+)")`, splitting
     the capture on `[,\s]+`, and `impact` returns `affected_stories: []` /
     `affected_acs: []` today because Core emits none (A7).
- **Decision:** Ship `tools/` as a **sibling of `lenses/` with the same
  pass-by-path mechanics and a different activation trigger** — two files
  (`tools/README.md`, `tools/aspark-graph.md`), no new skill, no new agent, no new
  frontmatter parser. Three sub-decisions carry the weight:
  1. **Availability is resolved by the skill, in its existing gate-check step, as
     the last sub-step *after* the existing hard gates pass.** Precedence
     (AC-2.2): **MCP first** — if the session exposes tools whose names end in
     `staleness` and `impact` (namespaced form `mcp__aspark-graph__staleness`),
     that surface is used and **no command is run**; **CLI second** — otherwise one
     single, read-only, combined probe (`command -v aspark-graph`, plus a `-f`
     test for `.aspark-graph/graph.json` per deviation D2). Exactly one probe per
     ceremony run, never repeated, never in a run that already stopped on a hard
     gate (which keeps AC-3.5 clean: `/demo-day` never probes when the browser or
     app is missing). The probe must be written so that it **exits zero and
     self-describes** in the absent case (F4).
  2. **Four resolved states, mutually exclusive, and the missing runner gets its
     own hint instead of a filesystem hunt.** `graph.json` + a surface → offer
     (pass the tool path). Surface + no `graph.json` → the AC-2.3 sentence, once
     per run, naming `aspark-graph build .` without running it. `graph.json` +
     **no** surface (the venv-local case) → one sentence, once per run, that graph
     data exists but no runner is reachable, naming the two supported ways to
     expose it (register the MCP server, or put the runner on `PATH`). Nothing at
     all → silence and the pre-change loop, bit for bit. The states are keyed on
     the same two facts (`surface?`, `graph.json?`), so **at most one hint sentence
     can fire in a run**, and never more than once (P-Q3). **A ceremony that
     resolves only "available / not available" collapses this design and makes
     AC-2.3 unreachable — that is finding F1, and it is a defect, not an accepted
     simplification.** Core **never** guesses a binary path: hardcoding
     `~/aSPARK-graph/.venv/bin/…` would encode a sibling repo's install layout
     (constitution §3 off-limits), break on every other layout, and execute a
     binary found by guesswork (NFR-7). Via MCP, an unbuilt graph surfaces as
     `{"found": false, "error": …}` from `_open()` rather than exit 1 — classified
     as the unbuilt state, not as AC-3.3's empty result.
  3. **The Plan-phase query is relayed by the skill, not executed by the EM**
     (P-Q2). `agents/engineering-manager.md` declares
     `tools: Read, Grep, Glob, Write` — no `Bash`. Rather than widen a planning
     agent to shell access for one optional tool, `/sprint-plan` extends its
     existing step 3 (*Relay questions*): the EM cuts its tasks with path notes
     first, then returns a tool-query request naming the union of those paths; the
     skill runs the read-only `query` and re-invokes with the JSON. This makes
     US-5 the enabler of AC-2.4 inside a single Plan run and keeps every command
     invocation in the ceremony, where the user's permission prompt lands. The
     Reviewer (`tools: … Bash`) and the QA Tester (no `tools:` key → inherits all)
     call read-only queries themselves.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Implement it as a lens (`lenses/aspark-graph.md`) | Re-validated against `lenses/README.md`: a lens is a *concern checklist* whose activation is `applies-to` (type) or `triggers` (characteristic), read from the constitution — the single source of truth for lens activation. A tool activates from installation state, which the constitution cannot know and must not claim. Bending the lens contract would make "no constitution → no lens" untrue for one file and blur both concepts (spec A1, US-6/AC-6.2) |
  | Write the guidance into each SKILL.md | Duplicates ~120 lines of product-specific text across three ceremonies and guarantees drift; it is the finding the feature exists to fix (spec §1 pain 1). What *is* duplicated is one probe bullet per ceremony — the shape US-6 asks for ("one new file plus one line per ceremony"), with the canonical wording held in `tools/README.md` and grep-comparable |
  | Leave the copy-paste block in the consumer's `docs/aspark-integration.md` | Status quo. Pushes integration into every target project (violates AC-1.5's zero-config bar), and the copy ages silently when the query surface moves. It also cannot be narrowed per C1: that block instructs `gate_health` in both of its sections |
  | Make the graph a hard dependency, or vendor/auto-install it | Breaks Core for essentially every user and is a constitution §3/§6 non-negotiable. Not a live option; recorded because the brief listed it |
  | Detect the CLI by probing conventional venv locations (`.venv/bin`, `~/aSPARK-graph/.venv/bin`, `pipx`) | Would make detection succeed in the author's environment, at the price of a hardcoded sibling-repo layout, silent breakage everywhere else, and executing a binary found by guesswork. Rejected in favour of the missing-runner hint, which is a one-time fix in the operator's hands and self-documenting (confirmed by the user, P-Q3) |
  | Pre-fetch every query in the skill and hand results to the agents | Plan phase has no diff and no file list until the EM has cut its tasks, so the input does not exist at hand-over time; Review would need the skill to own the query call forms, pulling product detail back into three skills (the rejection above, one level up). Only the Plan-phase call is relayed, because only it needs the agent's own output as input |
  | Add `Bash` to `agents/engineering-manager.md` | A permanent capability widening of a planning agent, for all users, to serve one optional tool with a population of ≈1. The relay costs one round trip, and only in the available case. Rejected by the user in P-Q2 |
  | Append a `Files` column to the plan table instead of an inline note | Legal (the consumer matches headings by substring) but cut in spec §6: every column added is a structure someone can depend on, and `_files_note` already parses the inline form |
  | *(Verification, not architecture — added in revision 2)* Install this working tree as the active plugin, or overwrite the `0.3.1` plugin cache, so ceremony runs exercise the change | Both **rejected by the user** on 2026-07-25. A dev-install changes the machine's plugin state for the sake of one feature's evidence, and overwriting a published cache makes the running loop untraceable to any released version. Consequence: no ceremony-level proof in this session — carried openly as risk P10 and as the unproven column in §4 |
- **Consequences:**
  - *Easier:* the next optional tool is one file in `tools/` plus one probe bullet
    per ceremony (AC-6.4); the deferred queries (`gate_health`,
    `story_trace`'s QA leg) reopen as one phase slice in one file when the
    consumer fixes its filename defect; `impact` gains a story-level answer for
    every plan written after T2, graph or no graph.
  - *Harder:* Core now names queries it does not own (R4) and hardcodes one
    external product name — and now one external *filename* — in the wired skills;
    the guidance carries three caveats it must not lose inside NFR-11's 150-line
    budget; the single beneficiary must expose a runner once (MCP or `PATH`)
    before the positive path works.
  - *Hardest, and only visible after the fact:* **the change cannot be exercised
    by running the loop in the session that writes it**, because the loop runs
    from the installed plugin (§2, F3). Every future change to `skills/` or
    `agents/` inherits this. It is why §4 is what it is.
  - *Accepted limitation, stated plainly:* `EXTENSION_LANGUAGE`
    (`~/aSPARK-graph/src/aspark_graph/extractors/base.py:45`) is exactly
    `.py .ts .tsx .js .jsx .mjs .cjs .java .go .rs`. Every file in this repo is
    `.md` or `.json` (plus a binary handbook under `docs/`), so **no `File` node is
    created for any file in this repo at all**. Together with the `has_node` guard
    at `artifacts.py:189`, this plan's own path notes build **zero** `implements`
    edges here — not few, zero — and the Plan-phase `impact` slice is inert in this
    repo and in any Markdown-only project. That is AC-3.3's empty-result case, not
    a defect. It also means `~/aSPARK-graph` is **the only possible venue** for
    corroborating US-5 (T15).

## 2. Affected Components

<!-- Files, modules, services, external dependencies. New dependencies need a justification. -->

**Where the ceremonies in this session actually execute from (F3, measured).**
Claude Code resolves skills and agents from the **installed plugin cache**:
`~/.claude/plugins/cache/aspark/aspark/0.3.1/`. That copy has no `tools/`
directory and its `skills/peer-review/SKILL.md` contains **0** occurrences of
`aspark-graph`, while the working-tree copy contains 3. Edits made here are
therefore **inert for every ceremony run in this session**, including the `/spark`
orchestrating it. This changes no design decision and no shipped file; it changes
only what evidence is obtainable, and §4 is built on that fact rather than around
it.

**New files (2 shipped + 1 evidence artifact)**

| Path | What it is |
|---|---|
| `tools/aspark-graph.md` | The one tool file: frontmatter (`name`, `phases`, `activation`, `detect`), an `## Availability` block (precedence, the one probe, the four mutually exclusive states, the two hint sentences, what may never be invoked), one slice per phase, a `## Reading a result` block, and a `## Not wired (deliberate)` block with its reopen condition. Built at 131 lines (≤ 150, NFR-11) |
| `tools/README.md` | Authoring guide: what a tool file is, installation-state activation, the tool↔lens boundary with an example on each side, the canonical probe/hand-over wording to copy into a ceremony, how to add the next one |
| `.spark/graph-gates/evidence.md` | The record required by NFR-10 — baseline, then one dated entry per verification step, each naming its **method** (static, parser-in-the-loop, walkthrough) and what it does *not* prove |

**Edited files (9)**

| Path | Insertion point (verified) | Change |
|---|---|---|
| `skills/peer-review/SKILL.md` | end of step 1 *Check the gate*; step 2 invocation list after the lens-paths clause | probe sub-bullet resolving **all four** states; tool path handed over beside the lens paths |
| `skills/sprint-plan/SKILL.md` | end of step 1; step 2 hand-over; step 3 *Relay questions* | same probe bullet; tool path hand-over; relay extended to read-only tool-query requests |
| `skills/demo-day/SKILL.md` | end of step 1, **after** the browser/app gear check; step 2 hand-over | same probe bullet, placed so a stopped run never probes; tool path hand-over |
| `agents/reviewer.md` | inside `## How You Work` step 2 *Get the diff* | generic tool paragraph, no renumbering, no product name |
| `agents/qa-tester.md` | inside `## How You Test` step 2 *Read the spec* | generic tool paragraph; `Result` cells still rest on performed steps |
| `agents/engineering-manager.md` | step 4 *Cut the tasks* | the DoD path-note bullet **and** the generic tool paragraph (two-pass: notes first, then request the blast-radius query) |
| `templates/plan.md` | the HTML comment above the task table | guidance text only — header row, both example rows and every protected column byte-identical (verified against `HEAD` during review) |
| `README.md` | new `## Optional Tools` before *Project Status*; one bullet in the toolbox list; the Project Status entry | optional, install-from-source, no registry claim; proof state stated truthfully, including what ships unproven. **Also, from the fix pass (F14 + D6):** the unproven criteria itemised as a table rather than prose, and the clean-handoff paragraph after the `/spark` usage example |
| `docs/workflow.md` | after the resumability paragraph in *Where the state lives* | **Added by the fix pass (D6)** — documents the clean-handoff offer: it offers and never clears, and only once every status on disk is current. Recorded here after round 3 raised **F18**: this file was in neither list, which is the same *Affected Components* gap that produced F10 one round earlier |
| `.claude-plugin/plugin.json` | `"version"` | `0.3.1` → `0.4.0` |

**Untouched by the graph wiring:** `skills/spark/SKILL.md` (its step 3 says to
read and follow each ceremony's own SKILL.md, so the orchestrator inherits the
wiring with no edit), `skills/increment`, `skills/go-live`, `skills/charter`,
`skills/story-time`, `skills/look-and-feel`, `skills/next-steps`, all other
templates, `.claude-plugin/marketplace.json` (no version field), `lenses/`.
NFR-2's counts (10 skills / 7 agents) hold because no skill or agent is *added*,
not because these files are unedited.

> **Superseded in part — see D6.** `skills/spark`, `skills/increment`,
> `skills/go-live`, `templates/spec.md`, `templates/review-report.md` and
> `agents/product-owner.md` **are** modified in the shipped tree, by the
> artifact-budget workstream the user folded into this increment on 2026-07-26.
> None of it is graph wiring; the sentence above stays true of the wiring and is
> no longer true of the tree.

**Dependencies:** none added, and none possible — no manifest, no runtime
(NFR-4). `aspark-graph` is discovered at run time, is not declared anywhere, and
its absence is the normal case.

**The binding reading of AC-1.1 (P-Q1, refined by D3).** "Zero occurrences" is
measured on exactly two surfaces: **(1)** the artifact the ceremony produced, and
**(2)** the ceremony's user-visible output. **Excluded:** the detection sub-step's
own tool calls and file reads (P-Q1), and mentions that quote or discuss **the
diff under review**, since the diff under review *is* this feature (D3). What must
be zero is **volunteered** mentions: no probe output, no hint sentence, no
availability remark, in a repo that has no graph.

**Blast radius, derived by hand (AC-2.4, applied to this plan).** No graph result
is cited: this repo has no reachable runner and — per D2 — no `graph.json`, so the
tool is in the silent state and scoping was done by grep and reading. Even with a
graph built here, `impact` would return nothing for these paths: none is in an
indexed language, so none has a `File` node (§1). This paragraph is the "recorded
that the result was empty" branch of AC-2.4, in the format the EM slice requires.

## 3. Task Breakdown

<!-- Ordered. Every task maps to the spec by ID (the story and the specific AC-n.m / NFR-n it serves)
     and has its own definition of done. The "Covers" column is the traceability spine: every Must AC
     and every applicable NFR must appear against at least one task.
     /increment works through this table top to bottom — nothing else — and keeps Status current. -->

**`/increment` owns every task, verification included** (P-Q5), and **stops for the
user's explicit go before any command that writes inside `~/aSPARK-graph`** (T13's
optional `touch`, T15's scratch edit and rebuilds). Each such task states how that
repo is left afterwards.

**Revision-2 note on IDs and order.** IDs are never renumbered (constitution §4),
so the fix-mode task appended after the review carries the next free ID, **T16**,
but sits in the table at its execution position — right after T5. Read the table
top to bottom, not by number.

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | **Capture the pre-change baseline.** Create the evidence record and freeze what "unchanged" means, before any edit | US-1 | AC-1.2, AC-1.4, NFR-10 | – | `done` | Evidence file holds the base commit SHA, the pre-change 0-hit grep, the three pre-change ceremonies' numbered step lists, the review/QA report headings, the protected plan header row, and the AC-1.1 reading quoted verbatim. Entry dated and labelled `pre-change baseline` — files: .spark/graph-gates/evidence.md |
| T2 | **The DoD path note.** Add the format to `templates/plan.md`'s guidance comment and to the EM's step 4, in one identical wording | US-5 | AC-5.1, AC-5.2, AC-5.3, AC-5.4, NFR-1, NFR-8 | – | `done` | Both places state the same rules in word-identical text: repo-relative POSIX paths, comma-separated; the note is the **last** thing in the cell; **no** punctuation attached to a path and no prose after the last one; omitted rather than guessed when the files are not knowable. The rationale claims **only what the parser does**: `_files_note` splits its greedy capture on `[,\s]+`, so punctuation abutting a path and prose running past the last path become tokens that the `has_node` guard drops with no error — and only the *first* keyword in a cell is anchored, so text after it is swallowed wholesale and what parses stops being predictable. **No claim that a second keyword breaks the note** (F5 — it does not; verified with the real parser). `git diff templates/plan.md` touches only the HTML comment; heading, header row and both example rows byte-identical — files: templates/plan.md, agents/engineering-manager.md |
| T3 | **Write `tools/aspark-graph.md`** — frontmatter, `## Availability` (MCP-then-CLI precedence, the single self-describing probe, the four mutually exclusive states with their two one-per-run hint sentences), one slice per phase, `## Reading a result`, `## Not wired (deliberate)` | US-2, US-3, US-4 | AC-2.2, AC-2.3, AC-3.2, AC-3.3, AC-3.6, AC-4.1, AC-4.2, AC-4.3, AC-4.4, AC-4.5, NFR-3, NFR-6, NFR-7, NFR-11 | – | `done` | Every wired query documented with call form, return shape and failure behaviour — `query staleness --repo .`, `query impact <file…> --repo .` (or `--diff <range>`), `query story_trace <US-n> --feature <f> --repo .` — each verified against the consumer's source rather than assumed. `stale: true` ⇒ say once, treat as **absent**, cite nothing, fall back, still reach the verdict. Empty or `found: false` ⇒ one line that scoping was done by hand, then the ordinary method. `story_trace`'s QA leg declared not-to-be-read; `impact`'s `affected_stories`/`affected_acs` carry the empty-by-construction caveat. `gate_health` appears **only** in the deferral block. No agent is instructed to run anything but `query`. `wc -l` ≤ 150. *Two DoD items remain open and are carried by T16: the per-query input trace (F7) and `story_trace`'s return shape and `ambiguous` failure (F8)* — files: tools/aspark-graph.md |
| T4 | **Walking skeleton: wire `/peer-review` end to end** — probe bullet in step 1, tool path hand-over in step 2, generic tool paragraph in the Reviewer's step 2 | US-2, US-3, US-6 | AC-2.1, AC-2.5, AC-3.1, AC-3.6, AC-6.3 | T3 | `done` | Availability is resolved inside the existing step 1 (no new numbered step; 5 before, 5 after) and `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` is handed over like a lens path. **The bullet resolves and acts on all four states**, not two: surface + `graph.json` → pass the tool file; surface, no `graph.json` → the one unbuilt sentence; `graph.json`, no surface → the one no-runner sentence; neither → say nothing at all. MCP tools are matched on names *ending in* `staleness`/`impact`. The probe exits zero and self-describes in the absent case (F4). Nothing blocks, warns or branches a gate outcome on availability. The Reviewer paragraph names no product and no query. *Open: F1 (two states shipped), F4 — both carried by T16* — files: skills/peer-review/SKILL.md, agents/reviewer.md |
| T5 | **Negative case first — by walkthrough and static check, not by a ceremony run.** Establish that the changed material cannot volunteer a word about the tool in a repo without one | US-1 | AC-1.1, AC-1.2, AC-1.3, AC-1.4, NFR-5, NFR-10 | T1, T4 | `done` | Recorded in the evidence file **before any available-case claim**, and labelled with its method. (a) *Static:* grep of the changed `skills/`, `agents/`, `templates/`, `lenses/` shows the product name in the wired skill only, in no agent and no template; the absent branch reads "say nothing at all"; the review-report template and both agents' step numbering are untouched; step count 5 → 5 against T1's baseline. (b) *Walkthrough:* read the modified `skills/peer-review/SKILL.md` and `agents/reviewer.md` and execute their steps by hand against this repo, recording per step what a conforming run would emit — and that the absent branch emits nothing. (c) *Honest limits:* states explicitly that the `/peer-review` run performed in this session executed the installed `0.3.1` cache (F3), that its silence is evidence about the **old** material only, and that ceremony-level proof of AC-1.1 is deferred to the post-release checklist in §4 — files: .spark/graph-gates/evidence.md |
| T16 | **Fix-mode: close the open review findings** (`.spark/graph-gates/review.md` F1, F4, F5, F7, F8) | US-2, US-4, US-5 | AC-2.3, AC-4.2, AC-4.4, AC-5.4, NFR-3, NFR-5 | T5 | `done` | Per finding, verified and recorded: **F1** — the wired skill resolves four states and both hint sentences are reachable, each at most once per run, mutually exclusive by construction. **F4** — the probe exits zero in the absent case and self-describes; the evidence notes whether a permission prompt naming the tool appeared. **F5** — the false second-keyword claim removed from both files, identically (AC-5.4 re-diffed word-for-word), the honest rationale in its place. **F7** — one sentence under `## Calls` tracing all three wired queries to `spec.md`, `plan.md`, source and mtimes, and connecting that to why the deferral below does not touch them. **F8** — `story_trace`'s top-level keys named, the two QA-leg keys named in the "do not read it" sentence, and the `ambiguous` failure documented. `wc -l tools/aspark-graph.md` still ≤ 150; `claude plugin validate` still passes — files: skills/peer-review/SKILL.md, tools/aspark-graph.md, templates/plan.md, agents/engineering-manager.md |
| T6 | **Wire `/sprint-plan` + the EM slice** — probe bullet, tool path hand-over, step 3 relay extended to read-only tool queries, and the two-pass Affected-Components instruction | US-2, US-4, US-6 | AC-2.1, AC-2.4, AC-4.5, AC-3.6, AC-6.3 | T2, T3, T16 | `done` | The probe bullet is byte-identical to the corrected one in T16 and resolves **all four** states. The skill's step 3 accepts a tool-query request from the agent, runs only a read-only `query`, and re-invokes with the JSON; the EM paragraph is product-agnostic and prescribes the order: cut the tasks with their path notes, then request the blast radius for the union of those paths, then fill *Affected Components* either citing the result or recording that it was empty — with the caveat that an empty story/AC list means the analysed plan has no notes, not that nothing is at risk. The EM's `tools:` frontmatter is **unchanged** (no `Bash`, per P-Q2) — files: skills/sprint-plan/SKILL.md, agents/engineering-manager.md |
| T7 | **Wire `/demo-day` + the QA slice** — probe bullet after the gear check, tool path hand-over, generic tool paragraph in the QA Tester's step 2 | US-2, US-3, US-6 | AC-2.1, AC-2.6, AC-3.4, AC-3.5, AC-3.6, AC-4.2, AC-6.3 | T3, T16 | `done` | The probe bullet is byte-identical to T16's corrected one and resolves **all four** states. The browser/app prerequisite stays hard and is evaluated **before** the probe, so a stopped run never probes; no checklist item passes or fails on tool state. The QA paragraph says the tool file may scope *which* ACs to exercise and *where* to look via the Story→AC→Task→Code legs, names the QA-leg keys it must not read, and states that no `Result` cell may rest on a tool answer — every one rests on a performed step — files: skills/demo-day/SKILL.md, agents/qa-tester.md |
| T8 | **Write `tools/README.md`** — the authoring guide and the canonical ceremony wording | US-6 | AC-6.1, AC-6.2, AC-6.4, NFR-3 | T3, T4, T6, T7, T16 | `done` | States what a tool file is, that it activates from **installation state** and not from the constitution's project profile, how a ceremony picks it up, and the numbered steps to add another. Answers "lens or tool?" with the stated boundary and one example on each side. Holds the four-state probe/hand-over bullet **verbatim** as the text a ceremony copies — taken from the corrected wording after T16 — so the three copies can be compared byte-for-byte, and states that a conforming second tool file needs no new agent, no new ceremony and no edit to an existing agent's role text — files: tools/README.md |
| T9 | **README entry** — a short *Optional Tools* section, the `tools/` bullet in the toolbox list, and a truthful Project Status entry | US-2, US-6 | NFR-3, NFR-9 | T8, T11 | `done` | Describes `aspark-graph` as **optional** and **install-from-source**, with no registry or PyPI claim, and says the loop is unchanged when it is absent. The Project Status entry states the proof state as §4 leaves it: which criteria are discharged by static, parser and walkthrough evidence, and — named individually — which ship **not proven** because the loop runs from the installed plugin (AC-1.1 at ceremony level, AC-2.1's live hand-over, AC-2.3's and the no-runner hint's firing, AC-2.4, AC-2.5, AC-2.6, AC-3.1, AC-3.2 behaviourally). Nothing intended is written as delivered — files: README.md |
| T10 | **Conformance sweep + version bump.** Run the grep / `wc` / diff / validate checks the NFRs name, record them, then set the version | US-1, US-4, US-5 | AC-1.3, AC-4.1, NFR-1, NFR-2, NFR-6, NFR-7, NFR-8, NFR-11 | T2, T3, T4, T6, T7, T8, T9, T16 | `done` | Recorded with command and output: `gate_health` only in the deferral block, 0 hits under `skills/` and `agents/`; no shipped material instructs `build`, `build_graph`, `serve`, `install` or any non-`query` invocation (NFR-7, unaffected by P-Q5 — §4); all three caveats present at the point of use; **the three probe bullets byte-identical to `tools/README.md`'s canonical four-state wording**; `wc -l tools/aspark-graph.md` ≤ 150; `git diff templates/` touches only comment text; no ID renumbered; skills = 10, agents = 7; every DoD cell of this plan re-checked for the note format under the corrected rules (note last, no punctuation on a path, no prose after it); `claude plugin validate` passes; version reads `0.4.0` — files: .claude-plugin/plugin.json, .spark/graph-gates/evidence.md |
| T11 | **Negative-case walkthrough across all three ceremonies** (replaces the former three-ceremony run, which this session cannot perform — F3) | US-1, US-5 | AC-1.1, AC-1.2, AC-1.3, AC-1.5, AC-5.1, AC-5.2, NFR-5, NFR-10 | T5, T10 | `done` | For each of `/sprint-plan`, `/peer-review`, `/demo-day`: read the modified `SKILL.md` and its agent file and execute the steps by hand against this repo, recording per step what a conforming run would and would not emit, and that the absent branch emits nothing about the tool. Recorded alongside: step counts and artifact sections identical to T1's baseline; `/demo-day`'s gear gate still stops before the probe is reached; `git status` shows no config, flag or `CLAUDE.md` block anywhere; every DoD cell of this plan carries a path note where the files are knowable and none where they are not. Each entry is labelled **walkthrough of the written instructions, not an execution of the shipped plugin**, and names the ACs it does *not* discharge — files: .spark/graph-gates/evidence.md |
| T12 | **Contract verification against the live consumer** (replaces the former positive-case ceremony run — F3) | US-2, US-3, US-4 | AC-2.2, AC-4.4, NFR-3, NFR-10 | T11, T16 | `done` | Read-only, in `~/aSPARK-graph`, which already holds a built graph: run each wired call exactly as `tools/aspark-graph.md` writes it — `query staleness --repo .`, `query impact <a real .py file> --repo .`, `query story_trace <US-n> --feature <f> --repo .` — plus one deliberate `found: false` case, and paste the real outputs into the evidence file beside the documented shapes. Every mismatch is a finding against T3, not a footnote. Confirms MCP-vs-CLI precedence is resolvable as written by recording which surfaces exist in the session. **No writing command is run:** no build, no touch, no artifact; if any step would write, stop and ask the user first. **End state:** that repo unchanged, shown by pasted `git status`. Labelled as parser/contract evidence, which does **not** discharge AC-2.5 or AC-3.1 — those need a real Review run — files: .spark/graph-gates/evidence.md |
| T13 | **Stale-path verification from the consumer's source, live check only on request** | US-3 | AC-3.2, AC-3.3, NFR-10 | T12 | `done` | Read `~/aSPARK-graph/src/aspark_graph/queries.py::staleness` and record what `stale: true` actually reports and when, confirming that the tool file's stale instruction rests on real behaviour. **Optional live corroboration only with the user's explicit go**, recorded: `touch` one source file there (mtime only, no content edit), re-query, observe `stale: true`, then rebuild on a second go so the repo is not left stale; `git status` pasted showing no content modification. Whether or not the live step is taken, the entry states that AC-3.2's *ceremony* behaviour — say it once, cite nothing further, still reach a verdict — is **not proven** in this session and belongs to the post-release checklist — files: .spark/graph-gates/evidence.md |
| T14 | **QA-slice walkthrough** (replaces the former agent dry run, which would have invoked the cached `0.3.1` agent — F3) | US-2, US-3 | AC-2.6, AC-3.4, AC-4.2, NFR-10 | T7, T12, T16 | `done` | Read the modified `agents/qa-tester.md` slice and `tools/aspark-graph.md`'s QA section and execute them by hand against one feature in `~/aSPARK-graph`, using the read-only `story_trace` output already obtained in T12: record which ACs a conforming test plan would scope, where it would look, that the QA-leg keys are recognised and not read as evidence, and that no `Result` cell could be produced from a tool answer. **Writes nothing anywhere outside this repo's evidence file**, and needs no go because it runs no writing command; if a step would write, stop and ask first. Labelled **walkthrough, not a ceremony**; AC-2.6 is recorded as **not proven** and stays that way through the QA gate and the README — files: .spark/graph-gates/evidence.md |
| T15 | **Path-note corroboration in `~/aSPARK-graph` — the only possible venue, and the strongest evidence available for US-5** | US-5, US-4 | AC-5.1, AC-4.5, NFR-10 | T11, T12 | `done` | Unaffected by F3: it exercises the **consumer's** parser and build, not Core's skills. **Stop and ask for the user's explicit go before editing that repo's plan, and again before each rebuild**, recording both. Append a note naming an indexed `.py` file to one DoD cell of an existing plan there, rebuild, and record before/after for the same call: `query impact <that .py file> --repo .` returns `affected_stories` and `affected_acs` **non-empty** with the note in place and empty without it (A7 reproduced), with the resulting `implements` edge at confidence `declared`. **End state:** the scratch edit reverted with `git checkout -- <that plan>` and the graph rebuilt, `git status` pasted showing a clean tree — or, if the user chooses to keep the note, that choice named in the evidence as a change deliberately left in their repo. The file touched there is deliberately **not** named as a path note in this cell: it is outside this repo, so no repo-relative path exists (AC-5.2) — files: .spark/graph-gates/evidence.md |

**Not applicable, so covered by no task:** NFR-4 (packaging/footprint — no bundle,
no dependency; recorded, not verified), NFR-12 (accessibility/performance — no UI,
no runtime), NFR-13 (security/privacy — `security` lens off per the
constitution's profile; the one live concern is NFR-7, covered by T3, T10 and
T16). Every other NFR and every Must AC appears above at least once; §4 states, per
criterion, whether the available evidence discharges it or whether it ships
unproven. AC-6.1–6.4 belong to the single `Should` story and are covered by T8,
with AC-6.3 additionally enforced in T4, T6 and T7.

## 4. Test Strategy

<!-- What gets unit tests, what gets integration tests, what is left to /demo-day in the browser. -->

**No unit tests, no integration tests, and none possible.** The change is Markdown
prompt material plus one JSON version field: no runtime to call, no function to
assert on, no harness, by constitution (§3, §4; spec A2, NFR-10). `/demo-day` in a
real browser is not applicable — the change renders nothing (spec §8).

**And, since revision 2, no ceremony-run evidence either.** The loop executes the
installed `0.3.1` plugin cache, not this working tree (§2, F3), and the user
rejected both ways of changing that (dev-install, cache overwrite). A ceremony run
in this session therefore proves things about the *old* material. Three methods
remain, and the strategy is built out of them:

1. **Static verification.** `grep`, `git diff` (byte-level against `HEAD`),
   `wc -l`, `claude plugin validate`, step-count and section comparison against
   T1's frozen baseline. This is what proves the *material* cannot leak: an
   instruction that is not in the file cannot be followed.
2. **Parser-in-the-loop verification.** Running the **consumer's real code** —
   `_files_note`, `load_graph`, `staleness`, `impact`, `story_trace` — against the
   exact strings this change emits, and reading its source where behaviour matters.
   This is a **first-class method, not a fallback**: it is executable, repeatable,
   and it already caught a factual error in shipped text that four readings missed
   (F5). Where a claim in `tools/aspark-graph.md` can be checked against the
   consumer, it is checked, and a mismatch is a finding.
3. **Manual walkthrough.** Reading the modified `SKILL.md` and agent file and
   executing their steps **by hand** against a real repo, recording at each step
   what a conforming run would and would not emit. Every walkthrough entry is
   labelled *walkthrough of the written instructions, not an execution of the
   shipped plugin*, and names the criteria it does not discharge. It is weaker
   than a run — an agent walking its own instructions is a generous judge (P11) —
   so it never stands alone: it is always paired with the static grep that would
   catch the same leak from the other side.

**What "the negative case runs first" means now.** Constitution §1 and AC-1.4
require the absent case to be established before any available-case claim. It can
no longer mean a ceremony run. It now means: **T5's static grep plus walkthrough of
the absent branch is written into the evidence file before any entry that uses the
graph** — before T12's live queries, before T14, before T15. The intent is
preserved exactly: nothing may be claimed about the tool being useful until it is
on record that a project without it is untouched. The ordering is enforced by the
`Depends on` column (T12, T13, T14, T15 all descend from T5 and T11).

**NFR-7 and P-Q5 are different questions — do not read them as contradictory.**
NFR-7 constrains **the shipped prompt material**: nothing in `tools/`, `skills/`
or `agents/` may instruct an agent to run `build`, `build_graph`, `serve`,
`install` or any non-`query` invocation; `aspark-graph build .` may be *named to
the user* and is never executed by an agent on its own. Grep-verified in T10; a
property of the product. P-Q5 is about who drives this feature's verification in
this session, with the user's per-step go as its control. Neither licenses the
other.

| Must story | What discharges it here | Method | What it does not discharge |
|---|---|---|---|
| US-1 — nothing changes | T5 and T11: the changed material names the tool in one wired skill and nowhere else; the absent branch says "say nothing at all"; step counts, artifact sections and gate checklists identical to T1's baseline; walkthroughs of all three ceremonies emit nothing in the absent branch | Static + walkthrough | A real absent-case ceremony run (AC-1.1 at ceremony level) — post-release |
| US-2 — the gate offers it unasked | T12 proves every documented call form, return shape and failure mode is real; T4/T6/T7 + T16 put the four-state hand-over in the text; T14 walks the QA scoping | Parser-in-the-loop + static + walkthrough | The hand-over actually firing (AC-2.1), the two hint sentences firing (AC-2.3, P-Q3), AC-2.4, AC-2.5, AC-2.6 — post-release |
| US-3 — a map, never a verdict | T13 confirms the stale contract from the consumer's source; T10 greps that every slice and agent paragraph carries the "replaces neither reading nor performing" sentence; `/demo-day`'s hard gear gate verified statically | Static + source verification | AC-3.1's `file:line` finding in a real graph-assisted review, and AC-3.2's behaviour in a real stale run — post-release |
| US-4 — only sound answers | T10's greps (`gate_health` only in the deferral block; no mutating invocation) and T16's F7 input trace; every external claim in the tool file checked against the consumer's source in T3 and T12 | Static + parser-in-the-loop | Nothing material — this story is fully dischargeable without a run, which is why it is the strongest-evidenced one here |
| US-5 — a plan says which files a task touches | T2's byte-level diff; this plan's own cells parsed clean by the real `_files_note`; T15's before/after in the one repo that indexes source, ending non-empty where it is empty today | Static + parser-in-the-loop | The post-change `/sprint-plan` emitting notes in a *live* run — post-release; the format itself is already proven end to end |

**Ships not proven — named, so nobody reads it as delivered** (constitution §1,
NFR-9; each goes into `README.md` via T9 and into the evidence record):

| Criterion | Why it cannot be proven here | Where it goes |
|---|---|---|
| AC-1.1 (ceremony level) | Needs an absent-case run of the *changed* skill | Post-release checklist, item 1 |
| AC-2.1 (live hand-over) | Needs the changed skill to execute and pass the path | Post-release, item 2 |
| AC-2.3 and the no-runner hint (P-Q3) | Both sentences fire only from a live probe; T16 makes them reachable in the text, nothing more | Post-release, item 3 |
| AC-2.4 | Needs `/sprint-plan` to relay a query in a live Plan run | Post-release, item 4 |
| AC-2.5, AC-3.1 | Need a real Review run with a graph present | Post-release, item 2 |
| AC-2.6 | Needs a `/demo-day` run with a graph *and* a browser surface — no such venue exists (P3), so this one stays unproven even post-release until such a project exists | **No checklist item — venue-blocked (P3).** It stays unproven until a project with both a built graph and a browser surface exists |
| AC-3.2 (behaviour) | Needs a live stale run; the contract half is discharged by T13 | Post-release, item 5 |
| F4's user-visible-prompt leg | Whether Claude Code shows the *user* a permission prompt containing the string `aspark-graph` when the probe runs cannot be attested from inside the session — the agent sees the command succeed, not what the user was shown | Post-release, **item 6** (added 2026-07-26; the fix pass first claimed this leg already lived here when it did not — caught by round 3) |

**Post-release verification checklist — owned by the user, after they update their
plugin install to a version containing this change.** Not tasks in this plan:
`/increment` cannot perform them. Each is one run plus one line in
`.spark/graph-gates/evidence.md`, and together they close the table above.

1. In any project **without** `aspark-graph`: run `/peer-review` and confirm the
   report and the ceremony's narrative volunteer nothing about the tool, and that
   the steps match the pre-change ones.
2. In `~/aSPARK-graph` with the graph built and a surface exposed: run
   `/peer-review` and confirm the tool file is handed over, the report names which
   results scoped the reading, and it still carries a `file:line` finding with the
   code behind it.
3. In a repo with the CLI reachable but no `graph.json`: confirm the unbuilt
   sentence appears exactly once. In a repo with `graph.json` but no runner:
   confirm the no-runner sentence appears exactly once, and never both.
4. Run `/sprint-plan` on any feature in a source-indexed repo with the graph
   present and confirm *Affected Components* cites the blast radius or records it
   empty.
5. Make the graph stale and re-run `/peer-review`: one statement, no further
   citations, a verdict all the same.

**Deliberately left to the human gate.** Whether an agent actually consulted the
tool file cannot be observed from outside (R1; spec §6). Both failure directions
stay cheap to catch in the artifact: a wiring that fired leaves a named result, a
wiring that leaked leaves a grep hit.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| **P10 (new, revision 2) — the loop runs from the installed plugin, not the working tree.** `~/.claude/plugins/cache/aspark/aspark/0.3.1/` has no `tools/` and 0 occurrences of the product name; the working tree has 3 (F3, measured twice) | Every "run the ceremony and observe it" task in the original plan proved something about the *old* material. Left unnoticed, this feature would have shipped with a negative case recorded as passed that was never performed — precisely the dishonesty constitution §1 forbids | §4 rebuilt on static, parser-in-the-loop and walkthrough evidence; T5, T11, T12, T13, T14 restated; the seven criteria that cannot be discharged are named in §4 and repeated in `README.md` (T9). Dev-install and cache overwrite were offered and **rejected by the user**, so the gap is closed by labelling, not by pretending. Every future change to `skills/` or `agents/` inherits this constraint — a candidate for the backlog, not for this cycle |
| **P11 (new) — a walkthrough is a generous judge.** The same agent that would execute the instructions is the one reading them | A walkthrough can "pass" material a real run would trip over | Never stands alone: each walkthrough is paired with the static grep that catches the same leak from the other side, must record per step the exact strings a conforming run would emit, and is labelled as a walkthrough in the evidence file. The post-release checklist is the real proof and is written down as owed |
| **P1 (resolved) — AC-1.1 read literally would forbid its own detection** | Would have made the AC unverifiable | Resolved by the user (P-Q1) and refined by D3: artifact plus user-visible output, excluding the detection sub-step's own calls and mentions of the diff under review; what must be zero is **volunteered** mentions. Quoted into the evidence file by T1 |
| **P2 — the Plan relay is skipped in implementation.** The EM has no `Bash`; if T6's relay is not built, the EM silently cannot query and AC-2.4 degrades to prose | AC-2.4 unmet while looking met | T6's DoD names both halves and T10 greps for them; the EM's `tools:` list must stay unchanged (P-Q2), so a shortcut shows in the diff. AC-2.4 is on the unproven list either way until a live Plan run happens |
| **P3 — AC-2.6 has no venue for a full ceremony** | The QA leg of US-2 cannot be proven, in this session or after release | T14 walks the slice by hand; AC-2.6 is on the unproven list flagged **venue-blocked**, stated in `README.md` (T9) and at the QA gate. The user has been told it cannot be proven |
| **P4 — three copies of the probe bullet drift** | Two ceremonies detect differently, breaking AC-2.2's "two runs resolve identically" | `tools/README.md` holds the canonical four-state wording (T8, taken from T16's corrected text) and T10 compares the three copies byte-for-byte. F1 is exactly this risk arriving early, in the first copy |
| **P5 (sharpened by F5) — the note format fails silently, but not for the reason first written.** `_FILES_NOTE_RE` (`artifacts.py:42`) captures greedily to the pipe and `_files_note` splits on `[,\s]+`, so punctuation attached to a path and prose after the last path become tokens the `has_node` guard (`:189`) drops with no error. A **second keyword does not break the note** — verified with the real parser | An emitted note that looks right and builds nothing; and, worse, a rationale that overstates its case, which costs the reader's trust in the rules that *are* load-bearing | T2's corrected text claims only what the parser does; T16 fixes both files identically (AC-5.4 re-diffed); T10 re-checks every cell of this plan under the corrected rules; T15 proves an edge is really built |
| **P6 — NFR-11's 150-line budget versus the caveats US-4 demands** | Either the cap breaks or a caveat is dropped | Built at 131 lines with F7/F8's fixes costing ~5 more; `wc -l` re-checked in T16 and T10. If the cap binds, the deferral block compresses — never a caveat |
| **P7 (resolved, and now defended) — the fourth availability state** | An unspecced sentence in someone's run — or, as F1 showed, no sentence at all | Confirmed by the user (P-Q3). F1 proved the real risk runs the other way: an implementation collapsed four states into two and silently removed a Must criterion. T4, T6, T7 and T16 now require all four states explicitly, and T8/T10 make the wording comparable across ceremonies |
| **P8 — the graph indexes nothing in this repo** | `impact` returns empty here forever; US-5 has no local corroboration | AC-4.5's caveat at the point of use (T3); recorded in §1 and §2 as AC-2.4's empty branch; corroboration relocated of necessity to T15 |
| **P9 — a verification run leaves someone else's repo changed** | The user's other repo modified without their say | Per-step go before every writing command (now only T13's optional `touch` and T15's scratch edit — T12 and T14 are read-only by construction), plus a stated end state in each of those cells |
| **R1 (inherited) — convention, not enforcement** | A skipped wiring and a correct silence are indistinguishable | Negative case first, now as walkthrough + static (T5 before everything available-case), plus the artifact-level asymmetry in §4 |
| **R2 (inherited) — the regression that breaks everyone** | The worst failure mode this repo has | The probe is a sub-bullet of an existing step, after the hard gate, with a self-describing zero-exit form (F4) and an explicit "say nothing at all" branch; verified statically now, by run post-release |
| **R3 (inherited) — quality erosion via false authority** | Reviews feel faster and get worse | The "replaces neither reading nor performing" sentence per slice and per agent paragraph, grepped in T10; AC-3.1 stays on the unproven list rather than being claimed |
| **R4 (inherited) — contract drift in the other repo** | Instructions point into the void, silently | Every documented call form, return shape, failure mode, confidence tier and extension list verified against the consumer's source (T3, review, T12); degradation is to silence, so drift costs capability, not correctness |
| **R6 / R9 (inherited) — a note that lies; empty answers on legacy plans** | A wrong declared link outranks a correct inference | AC-5.2's omit-rather-than-guess rule (T2) and AC-4.5's caveat (T3); no post-build correction this cycle (spec §6) |
| **R7 / R8 (inherited) — one-element abstraction, ≈1 beneficiary** | The mechanism may never pay for itself | US-5 (T2) ships before and independently of the graph wiring, and is the part with the strongest evidence |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft) — `.spark/graph-gates/spec.md`, `approved` 2026-07-25
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess) — nine, including the two verification routes the user rejected in revision 2
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded) — §3's new-concern-is-a-new-file, `${CLAUDE_PLUGIN_ROOT}/…` paths, the template contract byte-identical, no sibling-repo dependency, no guessed binary path, nothing executed unasked (§6); NFR-7 and P-Q5 distinguished in §4
- [x] Every task maps to a user story — no orphan tasks, no story without tasks — T16 included (US-2/US-4/US-5)
- [x] Every Must AC and every applicable NFR is covered by at least one task — and §4 states, per criterion, whether the evidence discharges it or whether it ships **not proven**
- [x] Every task has a checkable definition of done — each is a grep, a diff, a `wc -l`, a real parser output, a recorded walkthrough step or a named artifact fact; the cross-repo tasks additionally carry a stop-and-confirm step and a stated end state
- [x] Task order respects dependencies — T2 before T6; the skeleton is T1→T3→T4→T5; T16 before every remaining wiring task; all available-case evidence descends from T5 and T11
- [x] Test strategy covers every Must story — three methods named, ordering preserved, and the seven unproven criteria listed with a post-release checklist that closes them
- [x] Review findings folded in — F1, F4, F5, F7, F8 carried by T16; F2 and F6 already fixed by the Reviewer; F9 corrected in this table's `Status` column
- [x] Status set to `approved` by the user — revision 2 re-approved explicitly in conversation on 2026-07-25, after review of the downgraded test strategy (static + parser-in-the-loop + walkthrough, no ceremony-run evidence), the seven ACs named as shipping **not proven**, and the five-item post-release checklist the user owns

---

## Deviations

Recorded by `/increment` per its rule 4. Small, obvious corrections only —
anything touching architecture, scope or stories stops and returns to
`/sprint-plan`.

| # | Task | Deviation | Why |
|---|---|---|---|
| D1 | T4 | The step-1 probe bullet states the probe **inline** instead of deferring to `${CLAUDE_PLUGIN_ROOT}/tools/README.md`, and step 2 passes the concrete path `tools/aspark-graph.md` rather than a generic `tools/<name>.md` | Caught by the walking skeleton before T5, which is what it is for. `tools/README.md` does not exist until T8, so the deferral was a dangling reference. It also contradicted mitigation P4, which requires the wording to live **in** each ceremony so the three copies can be grep-compared byte-for-byte against the canonical copy in `tools/README.md` (T8, T10). No architecture change: the probe, its precedence and its four states are unchanged |
| D2 | T3, T4 | The availability probe tests `test -f .aspark-graph/graph.json`, **not** `test -d .aspark-graph` as §1 sub-decision 2 and the brief's §4 both specify | Correctness fix, not a design change. `queries.load_graph` (`~/aSPARK-graph/src/aspark_graph/queries.py:25-31`) raises `GraphNotBuiltError` unless `.aspark-graph/graph.json` exists — the directory alone proves nothing. Found the hard way: this repo contains a `.aspark-graph/` holding only an orphaned `parse-cache.json` with `"entries": {}` and no graph, which passes a directory test and then fails every query. The four states, the MCP-first precedence and the two hint sentences are unchanged; only the predicate for "is it built" is corrected |
| D3 | T5, T11 | AC-1.1's measure is refined to **zero volunteered mentions**: the ceremony must not raise the tool on its own account — no probe output, no hint sentence, no availability remark — and its steps, artifact sections and gate outcomes must match T1's baseline. Mentions that quote or discuss **the diff under review** do not count | The only diff in this tree *is* graph-gates, so any honest review of it names the tool repeatedly as its subject. A literal zero was unsatisfiable for a reason unrelated to leakage. §2's binding reading (P-Q1) excluded the detection sub-step's own calls but did not anticipate the subject-diff case. Resolved by the user on 2026-07-25. What R2 needs proven is unchanged: in a repo with no graph, the ceremony volunteers nothing and behaves exactly as before |
| D4 | T15 | The path-note corroboration was done in a **purpose-built fixture** in scratch (one `.py`, one `spec.md`, one `plan.md`) instead of by appending a note to an existing plan in `~/aSPARK-graph` | Same proof, strictly safer: a controlled before/after with the note present and absent, and **nothing written in the user's repo** — so the stop-and-confirm step and the revert step were not needed at all rather than merely performed carefully. The fixture also isolates the measurement from that repo's unrelated churn |
| D5 | T13 | The planned `touch`-based live staleness check was **not performed**; it was replaced by reading `queries.py::staleness` plus a live observation that arose independently | The planned method could not have worked. `staleness` compares sha256 **content hashes**, so a `touch` (mtime only, explicitly chosen in the plan because it needs no revert) leaves the hash identical and `stale` stays `false`. Performing it would have produced a green result that proved nothing. The independent observation — a separate user session created a worktree that made the graph genuinely stale — supplied the live evidence for free |

| D6 | — (no task) | `skills/spark/SKILL.md` **was modified** — a new numbered step 5, "Offer the clean handoff at heavy gates", taking the orchestrator from 7 steps to 8 — although §2 of this plan lists that file under *Untouched on purpose*. Recorded here after `/peer-review` round 2 raised it as **F10** (Major); it was not recorded when made | Not graph work at all: it belongs to the artifact-budget / context workstream the user folded into this increment on 2026-07-26, and it arrived without a task or a deviation row, which is the actual defect. Kept on the user's decision, for a reason this very session demonstrated: a previous session left `review.md` claiming `passed` with its verdict section missing, and the new step's "make sure every status on disk is current" is the guard against exactly that. AC-1.2 is **narrowed** to the three wired ceremonies to match what it was written to protect — see spec C13. **NFR-2 is unaffected:** editing `/spark` adds no skill, so the counts stay 10 skills / 7 agents; §2's reason conflated "not edited" with "count unchanged". `/spark` still has no baseline in `evidence.md` T1, which is why nothing caught this — noted as a gap for the next feature that touches an unbaselined ceremony |

**Not a deviation — a defect.** The collapse of the four availability states into
two (F1) is **not** recorded here as an accepted deviation. The four states are a
user-confirmed decision (P-Q3) and one of them carries a Must criterion (AC-2.3);
the collapse is fixed by T16, not adopted.

## Review Findings Carried

From `.spark/graph-gates/review.md` (2026-07-25, `changes-requested`).

| Finding | Severity | Status | Where it is handled |
|---|---|---|---|
| F1 — four states collapsed to two in the wired skill | Major | fixed (T16) | T16; DoD of T4, T6, T7 now require all four explicitly |
| F2 — MCP tools matched literally, not on the namespaced suffix | Major | fixed by the Reviewer | §1 sub-decision 1 restated; T8 takes its canonical wording from the corrected text |
| F3 — the loop executes the installed plugin, not the working tree | Major | open by design | Not fixable here (user rejected dev-install and cache overwrite): §4 rewritten, risk P10, seven criteria labelled unproven, post-release checklist |
| F4 — the probe exits non-zero in the normal absent case | Minor | fixed (T16) | T16; probe form stated in §1 sub-decision 1 |
| F5 — false claim that a second keyword breaks the note | Minor | fixed (T16) | T16 and T2's corrected DoD; risk P5 rewritten |
| F6 — frontmatter `detect:` carried the pre-D2 predicate | Minor | fixed by the Reviewer | D2 |
| F7 — per-query input trace missing (AC-4.4's audit trail) | Minor | fixed (T16) | T16 |
| F8 — `story_trace` return shape and `ambiguous` failure undocumented | Minor | fixed (T16, shape) | T16; strengthens AC-4.2 |
| F9 — T4's `Status` stale in this table | Minor | corrected | `Status` column kept current; all 16 tasks now read `done` |
