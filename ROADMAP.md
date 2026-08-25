# Roadmap

**Where work is tracked:** [GitHub Issues](https://github.com/a-lottes/aSPARK/issues). This file is the
*why* and the *order* — it does not restate the issues, and it is not the place to propose something.
If an item here interests you, the issue is where it gets discussed.

Status vocabulary, used literally: **Shipped** · **Next** · **Blocked** · **Not planned**.
A thing is Shipped only when it has been exercised, not when it has been written —
[README §Project Status](README.md#project-status) carries the detail, including what ships as a
documented `partial`.

---

## The one gap that matters most

> **aSPARK has never been proven by a full loop run on someone else's real project.**

Everything below is secondary to this. The lens layer was dogfooded on aSPARK itself and dry-run on two
sample apps, but its own spec defines success as a UI lens firing and being QA-verified on a real
`website` **and** a Review lens firing and being Review-verified on a real `api`. Neither has happened.

There is a standing caveat behind it: lens compliance is instruction-driven. **No test enforces that a
lens actually fired** — only a person running the loop can tell us whether it did, and whether it was
right to.

If you use aSPARK on anything real, [a field report](https://github.com/a-lottes/aSPARK/issues/new?template=field_report.yml)
is worth more than a patch. Reports where it went badly are worth the most.

---

## Shipped

| | |
|---|---|
| **The SPARK loop** | Five phases, five gates, ten ceremonies, seven agents. End-to-end on a sample app: PO → Designer → EM → build → review → real-browser QA → release. |
| **Spec-driven core** | Project constitution (`/charter`), the Specify-phase Clarify pass, non-functional requirements, and the `US-` / `AC-` / `NFR-` / `T` / `F` ID chain running unbroken from spec through plan, review and QA. |
| **Situational lenses** | Eight lenses activated by project **type** and **characteristics**, applied by the agents who already own each phase. New concerns are add-a-file: no agent is rewritten. |
| **Optional tools** | `tools/`, wired into `/sprint-plan`, `/peer-review` and `/demo-day`. Dogfooded in both directions — the absent case first, in a repo without the tool, where nothing may change. |
| **Honest PR-mode delivery** | `/go-live` reaches a `handed-off` terminal status where the project delivers by pull request instead of by tag. Proven on this repo's own release. |
| **Maturity labels in the handbook** | Every chapter of the architecture handbook carries a visible Delivery stage label, an overview table up front splits ambition from delivery, inline `Status.` markers name each target-state claim, and the title page separates the handbook revision from the shipped baseline (Core v0.7.0 · graph v0.7.0). Built as the `handbook-maturity` loop on this repo itself. |

---

## Next

**Anti-rationalization tables at every gate** · [#13](https://github.com/a-lottes/aSPARK/issues/13)
The gates are prompt-enforced, not code-enforced. They hold until an agent under context pressure
reasons its way around one — and a good-sounding reason is, from the agent's own view, a passed gate.
Sequenced *after* field reports on purpose: written from imagination, the tables would list excuses no
agent ever makes while the real ones go unlisted.

**Close the handbook honesty exception** · follow-up to [#18](https://github.com/a-lottes/aSPARK/issues/18)
The labels have landed (see Shipped): the handbook now carries the ambition/delivery split itself.
What remains is constitutional bookkeeping — the constitution still names the unlabelled handbook as a
known open exception to its own honesty principle. Close that exception via `/charter`, now that the
labels exist; post-release follow-up, not part of the labelling diff.

**An observability lens** · [#15](https://github.com/a-lottes/aSPARK/issues/15)
Between the `api` lens (the contract) and the `security` lens (what must never be logged) sits a concern
nobody owns: whether a correct, secure, well-specified service can be diagnosed once it is running.
Alongside the accessibility ([#6](https://github.com/a-lottes/aSPARK/issues/6)) and performance
([#7](https://github.com/a-lottes/aSPARK/issues/7)) lens proposals.

**In-flight doubt inside `/increment`** · [#14](https://github.com/a-lottes/aSPARK/issues/14)
Doubt is currently a *phase*: `/peer-review` runs after the build. So a wrong premise adopted in task 2
is not challenged until task 12 stands on it. Task-level verification cannot catch this — a task built on
a wrong assumption passes its own definition of done perfectly. Carries a real risk of making the longest
phase longer; if it cannot be kept cheap and rare, it should not ship.

**Ticket import and status write-back** · `ticket-import` · [#19](https://github.com/a-lottes/aSPARK/issues/19)
Take a ticket number as the sole input to `/story-time`, read the ticket as the brief, and push status
back to the tracker when a gate closes. One direction only — aSPARK never polls a tracker for its state.
Unblocked now that PR-mode delivery has shipped the `Ticket` field it builds on. Optional and never
blocking, like every external integration here.

---

## Blocked

**A template version handshake** · `template-version-marker`
Artifacts shaped by `templates/` are parsed by [`aspark-graph`](https://github.com/a-lottes/aSPARK-graph),
which pins a supported template version — but no template carries a version marker, so drift surfaces as
a structural guess rather than a named version conflict. Adding the marker here is a harmless comment
until the consuming side reads it. **Both repos ship it together or neither does**, otherwise the result
is a marker nobody reads.

**Machine-readable release evidence** · `release-evidence`
Turning release notes into a real `Release` node with a date and a commit, so delivery metrics become
possible. Blocked on the consuming repo defining that schema first — starting earlier means building
against a shape that does not exist yet.

---

## Not planned

Considered and deliberately declined. Reopening any of these needs a new argument, not a repeat of the
old one.

| | Why not |
|---|---|
| **Abstracting over model providers** | Not an abstraction but a rewrite: aSPARK *is* a Claude Code plugin, and the skills/agents format is Claude-specific. This is a strategy decision, not a feature. |
| **Portfolio entities above story level** (epics, initiatives, SAFe-style) | Declined. It would add exactly the ceremony weight this project exists to avoid. |
| **TOGAF / ArchiMate mapping** | Deferred. Two pages of appendix if a real user ever asks for it. |
| **Splitting deterministic from human-judgment checks** | A policy-layer concern, not a Core one. |
| **Delivery metrics (DORA)** | Belongs in the graph repo, where commits and releases already live. |
| **Security architecture and MCP threat modelling** | Belongs in the graph repo, which is where an MCP server actually runs. Core has no runtime and no network surface. |

---

## The wider picture

aSPARK Core — this repo — is Markdown prompt material with no runtime and no dependencies. It is designed
to be installed into arbitrary projects, which is why **no sibling repo, package or tool is ever a hard
requirement.** An optional integration degrades to silence: when the tool is absent, every gate behaves
exactly as it does without it — no error, no warning, no mention.

[`aspark-graph`](https://github.com/a-lottes/aSPARK-graph) is the one such integration wired up today: a
deterministic graph over `.spark/` artifacts and source code, used to *scope* work rather than to judge
it. A result from it is treated as a map, never a verdict. See [`tools/README.md`](tools/README.md).

---

*Ordering here is dependency order and honest priority — not a schedule. This is a small project and
nothing on this page carries a date.*
