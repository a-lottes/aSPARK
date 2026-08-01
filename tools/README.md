# Tools — optional external capabilities

A **tool** is an external program a ceremony may use *if the person running it
happens to have it installed*. The tool file in this directory is the guidance an
agent reads to use it well: what to call, what the answer means, and what the
answer must never be taken to prove.

Tools are **knowledge about a capability**, not roles and not ceremonies. They add
no agent, no slash command and no gate. And they are never required: in most
projects every tool here is absent, and the loop must run exactly as it would if
this directory did not exist.

## Tool or lens?

Both are optional Markdown a skill passes to an agent by path. They differ in
**what turns them on**, and that difference is the whole reason they are separate
directories.

| | Lens (`lenses/`) | Tool (`tools/`) |
|---|---|---|
| What it is | A concern checklist | A capability's usage guide |
| Activated by | The **project profile** in `.spark/constitution.md` | **Installation state** — is the program actually here? |
| Who decides | The user, by recording it in the constitution | Nobody decides; the ceremony probes and finds out |
| Example | `security` — because this project handles auth | `aspark-graph` — because this machine has it built |

The test: *could the constitution know this?* A project's type and characteristics
are stable facts a user can declare once. Whether a program is installed is not —
it varies per machine and per checkout, and the constitution must never claim it.
Bending a lens to activate on installation state would make the constitution's
own rule ("no constitution → no lens") untrue for that one file.

## How a ceremony picks one up

The same pass-by-path mechanic lenses use:

1. **The skill resolves availability** in its existing gate-check step, as the
   last sub-step, *after* the hard gates have passed. Never in a run that already
   stopped.
2. **If available, the skill passes the file path** to its agent, alongside the
   lens paths — one more path, nothing else.
3. **The agent reads its own phase slice** and works accordingly.

No new numbered step is ever added to a ceremony. If the step count changes, the
wiring is wrong.

## The canonical probe bullet

Copy this verbatim into a ceremony's step 1. It is duplicated in three skills on
purpose — one line per ceremony was the design goal — so it must stay
comparable. Change it here and in all three, or nowhere.

```markdown
- **Only after the gate has passed**, resolve optional tool availability,
  once: if the session exposes MCP tools whose names end in `staleness` and
  `impact` (they are normally namespaced, e.g.
  `mcp__aspark-graph__staleness`), treat that as the available surface and
  run no command; otherwise probe once, read-only, with
  `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no;
  test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no`
  — it reports both facts and **always exits 0**, so the absent case never
  looks like a failed command.
  Resolve **both** facts — is there a surface, and does
  `.aspark-graph/graph.json` exist — and act on the four states in
  `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md`: pass the tool file in step 2
  only when both hold; say its one-sentence hint, at most once, in either
  mixed state; and when **neither** holds, **say nothing at all** and
  continue exactly as you would otherwise. Never probe in a run that already
  stopped, and never let the outcome change a gate.
```

**One permitted variation.** `/demo-day` has two hard gates rather than one, so
it opens `**Only once both gates above have passed**` and closes with the
browser/app clause instead of the generic one. Everything between is identical.

Three rules the wording exists to enforce:

- **Resolve both facts, not one.** Collapsing this to "available / not available"
  loses two of the four states, and the two hint sentences then become
  unreachable. That is a defect, not a simplification.
- **The probe must exit 0.** A red shell result in the normal absent case is the
  most likely thing an agent volunteers a sentence about — and that sentence is
  precisely the regression this design exists to prevent.
- **Silence means silence.** In the absent state the ceremony says *nothing*: no
  mention, no hint, no note that a tool was looked for.

## The tool file contract

- **Frontmatter** declares `name`, `activation: installation-state`, `phases`
  (which SPARK phases have a slice), and `detect` (the availability shorthand).
- **An `## Availability` block** giving the precedence order, the single probe,
  and every resolved state with exactly what to say — or not say — in each.
- **One slice per declared phase**, so an agent reads only its own.
- **A `## Reading a result` block**: what the answers mean, and what they must
  never be read as. Every tool needs this. An answer that looks clean because
  nothing was consulted is worse than no answer.
- **A `## Not wired (deliberate)` block** for anything deliberately not used,
  with the condition under which it may be reopened — so a deferral is
  revisitable rather than forgotten.
- **Keep it under 150 lines.** An agent reads this on top of its own role and a
  lens; attention is the real budget.

Every slice must say, in its own words, that a result **replaces neither reading
the code nor performing the steps**. A tool that makes a review faster and
shallower has made things worse.

## Adding another tool

A new capability is a new file, nothing else — no new agent, no new ceremony, no
edit to any agent's role text:

1. Create `tools/<name>.md` following the contract above.
2. Add the canonical probe bullet to each ceremony that should offer it, adjusting
   only the tool name and the file path.
3. Add a line to `README.md`'s *Optional Tools* section.

The agent-side paragraphs are deliberately **generic** — they say "if the caller
passed a tool file, read it and apply its slice" and name no product. So a
conforming second tool file is picked up by adding the file and referencing its
path, with no agent edited at all.

## Available tools

| Tool | Phases | Requires |
|---|---|---|
| [`aspark-graph.md`](aspark-graph.md) | plan, review, qa | `aspark-graph` (on PyPI), with a graph built for the repo |
