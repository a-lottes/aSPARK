# How to read this repository

If you're new to Claude Code plugins, this is all there is to it:

- **`agents/`** — the team members. Each file defines one persona (a *subagent*): its mindset, its standards, and which tools it may use. Agents are the "who".
- **`skills/`** — the ceremonies. Each folder holds one slash command (`SKILL.md`): what to do, which agent to involve, which template to fill, and which gate to enforce. Skills are the "how".
- **`templates/`** — the artifacts. Blueprints for `constitution.md`, `spec.md`, `plan.md`, `review.md`, `qa.md` and `release.md`, each (bar the constitution) ending in an explicit gate checklist. Templates are the "what".
- **`lenses/`** — situational concern checklists (`seo`, `ux`, …). Activated by the project profile in the constitution and applied by the existing agents in the phases they own. Lenses are the "when it applies".
- **`tools/`** — guidance for optional external programs a ceremony may use *if you happen to have them installed*. Activated by installation state rather than by the constitution. Tools are the "if it's there".
- **`docs/`** — deep-dives: [`workflow.md`](workflow.md) (the gate hand-over rules), [`status.md`](status.md) (per-criterion proof state), [`metrics.md`](metrics.md) (the method behind the figures in [`status.md`](status.md)) and the [Enterprise Architecture Handbook](aSPARK_Enterprise_Architecture_Handbook.docx) (`.docx`), which carries a delivery-stage label per chapter so ambition and delivery stay separable.
- **`.claude-plugin/`** — plugin metadata so Claude Code can discover and install all of the above. `marketplace.json` is also what publishes the optional `aspark-guard` alongside Core.

Alongside the folders, three documents at the repo root: [`ROADMAP.md`](../ROADMAP.md) (what ships next, what's blocked, what was declined), [`CONTRIBUTING.md`](../CONTRIBUTING.md) (how to add a skill, agent, lens or template without breaking the contract) and [`CLAUDE.md`](../CLAUDE.md) (working habits kept across loops, distinct from the constitution's standing principles).

Reading order for newcomers: the [README](../README.md) → `docs/workflow.md` → one template → one skill → one agent. After that you'll understand every file in the repo.
