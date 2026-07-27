---
name: aspark-graph
activation: installation-state
phases: [plan, review, qa]
detect: mcp-tools staleness,impact | cli aspark-graph + .aspark-graph/graph.json
---

# aspark-graph — deterministic code and artifact graph

An optional external tool. It indexes `.spark/` artifacts and source code and answers
scoping questions a phase would otherwise grep for by hand. It is **never** required:
in most projects it is absent, and every gate must behave exactly as it does without it.

## Availability

Resolve **once**, as the last sub-step of the ceremony's existing gate check,
and only after that gate has passed. Never resolve in a run that already stopped.

1. **MCP first.** If the session exposes tools whose names *end in* `staleness`
   and `impact` (e.g. `mcp__aspark-graph__staleness`), use them. **Run no command.**
2. **CLI second.** Otherwise probe once, read-only, in a form that always exits
   0: `command -v aspark-graph`, plus `test -f .aspark-graph/graph.json`.

Test for **`graph.json`, not the directory** — a `.aspark-graph/` left by an interrupted
build holds only a parse cache, passes a directory test, and then fails every query.

Those two facts give four mutually exclusive states. **At most one hint sentence
fires per run, at most once.**

| Surface | `graph.json` | Do this |
|---|---|---|
| yes | yes | **Offer.** Use the phase slice below. |
| yes | no | Say **once**: the graph is not built for this repo; `aspark-graph build .` would build it. Then continue without it. |
| no | yes | Say **once**: graph data exists but no runner is reachable — register the MCP server, or put the runner on `PATH`. Then continue without it. |
| no | no | **Say nothing.** Work exactly as you would with no tool. Do not mention it. |

Never run `build`, `build_graph`, `serve` or `install`. `aspark-graph build .` may be *named
to the user* — running it is their decision, never yours. Only read-only `query` calls are
permitted.

## Calls

`--repo .` is accepted by every query; MCP takes the same names and parameters.

| Call | Returns |
|---|---|
| `aspark-graph query staleness --repo .` | `{"stale", "files_checked", "changed", "missing", "advice"}` — hash-compared, so `files_checked: 0` means nothing indexed, not "fresh" |
| `aspark-graph query impact <file…> --repo .` | `{"found", "files": [{"path","in_graph","code_entities","affected_stories","affected_acs"}], "affected_stories", "affected_acs", "unknown_files"}` — a file with neither also carries `"note": "no affected stories or acceptance criteria"` |
| `aspark-graph query impact --diff <range> --repo .` | same, files derived from a git range, plus top-level `"range"`; a range resolving to no files also carries `"note": "no files in range"` |
| `aspark-graph query story_trace <US-n> --feature <f> --repo .` | `{"story": …, "acceptance_criteria": [{"ac", "text", "qa_checks": [...], "latest_result"}], "tasks": [{… "code": [{"id","type","confidence"}]}]}` |

Failure modes: unbuilt graph → CLI writes to stderr and **exits 1**; over MCP the same
condition returns `{"found": false, "error": …}` — both mean *not built*, not *nothing
found*. Bad arguments (files **and** `--diff`, or neither) → `{"found": false, "reason":
"bad_args"}` with a `message`. Unknown story id → `{"found": false, "reason": "not_found"}`.

**Read `unknown_files`.** It lists the paths the graph has no node for. If `files`
is empty and `unknown_files` holds everything you asked about, the answer is *"I
do not index these"* — not *"nothing depends on them"*. That is the single most
useful field for telling a real empty result from a structural one.

**Why these three and not the others.** Each reads only inputs that are named
identically no matter which artifact-filename convention a project uses:

| Query | Reads | Therefore |
|---|---|---|
| `staleness` | content hashes of indexed files | convention-independent |
| `impact` | source files + `implements` edges from `plan.md` | `plan.md` is named the same everywhere |
| `story_trace` | `spec.md` + `plan.md` + source | same — **except** its QA leg, which reads the QA artifact and is therefore not sound (see below) |

The two deferred queries fail exactly this test: they read the review and QA
artifacts, whose filenames differ between conventions. That is the boundary — if
you reopen a deferral, re-check it against this table first.

## Reading a result

- **A result is a map, not a verdict.** It tells you where to look. It never
  replaces reading the code, and never replaces performing a step.
- **Stale ⇒ absent.** If `staleness` returns `stale: true`, say so **once**, then
  treat the graph as absent for the rest of the run: cite no result as evidence,
  fall back to reading and grep, and still reach your normal verdict.
- **Empty ≠ nothing there.** An empty list or `{"found": false}` means the graph
  has no answer, not that nothing exists. Record in one line that you scoped by
  hand, then proceed by the ordinary method.
- **Confidence tiers**, weakest to strongest: `inferred` (self-derived) <
  `extracted` (from tree-sitter) < `declared` (from an aSPARK artifact).
- **`affected_stories` and `affected_acs` are empty by construction** for any
  plan whose tasks carry no `files:` note — including every plan written before
  such notes existed. Empty here means *the plan declared no links*, **not**
  *nothing is at risk*. Never report it as reassurance — nor either `note` field, which
  restates that emptiness in prose ("no affected stories or acceptance criteria", "no
  files in range") and so reads exactly like an all-clear. Neither is one.
- **Only source files are indexed** — `.py .ts .tsx .js .jsx .mjs .cjs .java .go
  .rs`. A Markdown-only or config-only project has no file nodes at all, so
  `impact` is legitimately empty there. That is this case, not a defect.

## Plan slice

Use `impact` to ground *Affected Components* instead of guessing the blast radius.

Order matters: cut the tasks **with** their `files:` notes first, then ask for the blast
radius of the union of those paths. The notes make a story-level answer possible at all.

Then either cite what came back, or record that the result was empty and that you scoped
by hand — a reader must be able to tell which. If the story and AC lists are empty, say
so as *the analysed plan declares no file links*, never as *nothing is at risk*.

A blast radius is a starting point for reading the affected code, not a substitute
for it. Architecture is still decided by understanding the system.

## Review slice

1. `staleness` first. If stale, apply the stale rule above and stop using the graph.
2. `impact` on the changed files (or `--diff <range>`) to see what the diff reaches.
3. `story_trace <US-n>` for the stories the plan says the diff serves.

Name in the report which results scoped your reading and which locations you read as a
consequence. Then **read those locations.** A report whose findings restate graph output
without a concrete `file:line` and the code behind it has not reviewed anything.

## QA slice

`story_trace` can scope the test plan: which ACs belong to a story, which tasks
claim to implement them, and which code they reach — so you know where to look
first and what to probe hardest.

`tasks[].code` is **empty in every Markdown-only project** — aSPARK Core always included
— and where populated it carries `confidence: "inferred"`, from git history rather than
a `files:` note. Empty means *nothing was linked*, not *this task reaches no code*.

Its **QA leg is not populated** for a project using aSPARK's instantiated artifact
names, so it will look as though no QA evidence exists. The keys are
`acceptance_criteria[].qa_checks` (a list) and `acceptance_criteria[].latest_result`
— an empty list and a `null`. **Do not read either**, and never report their
emptiness as a finding: they are empty because the file was never opened, not
because the AC was never verified.

No `Result` cell may ever rest on a graph answer. Every verdict rests on a step you performed.

## Not wired (deliberate)

- **`gate_health`** — **do not call it.** Its `open_findings` is always `0` here
  (findings file never opened), a false zero on the one thing a gate exists to
  catch; its two sound fields share the same object, so they cannot be separated.
- **`story_trace`'s QA leg** — same root cause.

**Reopen both** when the tool resolves its artifact-filename mismatch (it probes
`review-report.md` / `qa-report.md` / `release-notes.md`; aSPARK writes
`review.md` / `qa.md` / `release.md`).
