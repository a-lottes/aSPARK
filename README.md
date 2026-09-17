<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/aspark-logo-dark.png" />
    <img src="assets/aspark-logo.png" alt="aSPARK — an agile AI product team for Claude Code" width="440" />
  </picture>
</div>

> **An agile AI product team for Claude Code.**
> One person plus aSPARK works like a whole team: a Product Owner who challenges your idea, a Designer who spots bad design, an Engineering Manager who locks the architecture, a Reviewer who finds your bugs, a QA Tester who clicks through your app in a real browser, and a Release Manager who ships it.

aSPARK turns Claude Code from a coding copilot into a **gated delivery process**. Every feature travels through five phases — **S**pecify, **P**lan, **A**ct, **R**eview, **K**eep — and may only move forward when the previous phase's quality gate is green.

---

## The SPARK Loop

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/aspark-loop-dark.png" />
    <img src="assets/aspark-loop.png" alt="The SPARK loop: Specify → Plan → Act → Review → Keep, with feedback loops" width="720" />
  </picture>
</div>

| Phase | What happens | Gate to pass |
|---|---|---|
| **S**pecify | The idea is challenged, clarified against a coverage taxonomy, turned into user stories with acceptance criteria and non-functional requirements, and design-checked. | Spec approved: stories testable, NFRs measurable, ambiguity resolved, design risks named. |
| **P**lan | Architecture is decided, the work is cut into ordered tasks. | Plan approved: every task maps to a story, risks addressed. |
| **A**ct | The increment is built — strictly following the plan. | All planned tasks done, project builds and tests pass. |
| **R**eview | Code review by a senior eye, then hands-on QA in a real browser against the acceptance criteria. | No blocking findings, all acceptance criteria verified. |
| **K**eep | The increment is released — or, in a declared PR-mode project, handed off for approval — and learnings are kept. | Released (or handed off) and documented. |

---

## Meet the Team

| Command | Role | What they do |
|---|---|---|
| `/charter` | 📜 **Facilitator** | Grounds the project's standing principles and constraints in `constitution.md` — the ground rules every phase inherits, decided once. |
| `/next-steps` | 🧭 **Product Owner** | No idea in hand? Surveys shipped, in-flight and stalled work plus the constitution, and proposes one concrete next feature. Advisory only — nothing is written or approved. |
| `/story-time` | 🧭 **Product Owner** | Interrogates your idea with hard questions — no yes-man. Runs a Clarify pass, writes user stories, acceptance criteria and NFRs into `spec.md`. |
| `/look-and-feel` | 🎨 **Designer** | Detects bad design: usability heuristics, visual consistency, accessibility. Adds a design section to the spec. |
| `/sprint-plan` | 🏗️ **Engineering Manager** | Locks the architecture, makes the technical decisions, cuts the work into an ordered task breakdown in `plan.md`. |
| `/increment` | 💻 **Developer** | Builds a potentially shippable increment — strictly following the plan, no scope creep. |
| `/peer-review` | 🔍 **Reviewer** | Reviews the diff with a staff-engineer eye and writes findings into `review.md`. |
| `/demo-day` | 🧪 **QA Tester** | Clicks through the running app **in a real browser**, verifies every acceptance criterion, files bugs in `qa.md`. |
| `/go-live` | 🚀 **Release Manager** | Final checks, changelog, version tag, PR/deploy — or, in a declared PR-mode project, hands off for approval (`handed-off`). Blocked while QA has open blockers. |
| `/spark` | 🤹 **Orchestrator** | Runs the whole loop end-to-end, enforcing every gate on the way. |

---

## How It Works

aSPARK keeps all decision artifacts **inside your project**, so the process is transparent and reviewable — just like a real team's ticket trail.

For each feature, a working directory is created:

```
your-project/
└── .spark/
    ├── constitution.md   ← written by /charter — project-wide, read by every phase
    └── <feature-name>/
        ├── spec.md       ← written by /story-time (+ /look-and-feel)
        ├── plan.md       ← written by /sprint-plan
        ├── review.md     ← written by /peer-review
        ├── qa.md         ← written by /demo-day
        └── release.md    ← written by /go-live
```

Each phase **reads the artifact of the previous phase** and refuses to start if the gate isn't met. Example: `/go-live` will not release while `qa.md` lists open blocking bugs — it sends you back to `/increment` instead. That's the whole point: the team doesn't just produce code, it makes sure **the product actually works**.

Requirements carry **stable IDs** (`US-`, `AC-`, `NFR-`) from the spec all the way through: the plan cites which AC each task covers, the review traces each Must AC to code, and QA verifies it under the same ID. Nothing silently falls out of the chain. The project-wide `constitution.md` (optional, set once via `/charter`) holds the principles and constraints every feature inherits, so they aren't re-argued each cycle.

### The loop adapts to what you're building

Not every concern applies to every project. So aSPARK detects **what kind of software this is** and switches on the matching **lenses**: situational checklists that give the *existing* team extra things to check, only where they apply. Lenses activate two ways — from the project **type** and from its **characteristics** (what it does with data):

| Lens | Turns on for | What it adds |
|---|---|---|
| **seo** | a public `website` | Discoverability NFR, semantic structure, SSR + per-page metadata, Core Web Vitals in the browser |
| **ux** | an app-like `web-app` | Flow efficiency, every empty/loading/error state, forms, mobile |
| **api** | an `api` service | Error-envelope consistency, versioning & breaking-change detection, auth per endpoint |
| **cli** | a `cli` tool | Help clarity, stdout/stderr discipline, exit codes, safety flags |
| **library** | a `library` | Public API surface, semver/deprecation discipline, packaging & footprint |
| **security** | *handles auth · public · payments · PII* | Header hardening, auth lifecycle, the authz matrix, supply chain, PII/privacy — depth beyond the Reviewer's baseline |
| **i18n** | *multilingual* | Externalized strings, locale-aware formatting, text-expansion & RTL layout |
| **data** | *has a database* | Migration safety, integrity/transactions, indexing at scale, retention & recovery |
| **accessibility** | *must be accessible* | Specify-through-QA a11y depth beyond the Designer's baseline: grounded NFR, semantic HTML/ARIA, keyboard-trap/focus checks, keyboard-only + measured-contrast QA |

The Facilitator grounds the type and characteristics in the repo during `/charter` and the user confirms them. The constitution is the **single source of truth** — it's the only place a lens is switched on, so no phase can drift from another. Without a constitution, **no lens is applied**: each phase just gives a one-line nudge ("this looks like a `website` — run `/charter` to record it") and nothing more. When 4+ lenses come out active, the profile flags the elevated load — there's no cap, the visibility *is* the throttle.

A lens is **knowledge, not a new role** — the concern rides the same gates and the same `NFR-` traceability as everything else, so it's verified, never just asserted. Adding a new concern is a new file in [`lenses/`](lenses/), nothing more.

---

## The aSPARK Family

Core is one repo of five. Everything else is **optional** — Core has no hard
dependency on any of them (constitution §3), and a project that installs none
behaves exactly as documented above. The column that matters is the third one:
two of the four siblings do not touch the loop at all today.

| Repo | What it is | Hooks into Core today? | How you get it |
|---|---|---|---|
| **aSPARK** (this repo) | The loop: 10 skills, 7 agents, 9 lenses, 6 templates | — it *is* Core | `/plugin install aspark@aspark` |
| [**aspark-guard**](https://github.com/a-lottes/aSPARK-guard) `v0.1.0` | Denies a `.spark/` write that violates a gate precondition; records every write with its hash | **Yes** — as a second plugin from the same marketplace | `/plugin install aspark-guard@aspark` |
| [**aspark-graph**](https://github.com/a-lottes/aSPARK-graph) `v0.7.0` | Deterministic graph over your `.spark/` artifacts and source code | **Yes** — `/sprint-plan`, `/peer-review` and `/demo-day` probe for it and pass it by path | `pip install aspark-graph` (PyPI) |
| [**aspark-insights**](https://github.com/a-lottes/aSPARK-insights) `v0.12.0` | Metrics over the graph's facts: traceability coverage, an offline HTML report, a release board, MCP queries | **No** — standalone; it reads the graph, not Core | source only, not on PyPI |
| [**aspark-policy**](https://github.com/a-lottes/aSPARK-policy) `v0.2.0` | Policy-as-code: a documented format, a tested JSON Schema, 11 catalog packs including `pci-dss`, `un-r155` and `misra` | **No** — a format and a catalog; the `validate` CLI and the Facilitator integration are unbuilt | Git submodule, no tooling to run |

Versions are the repos' latest git tags, not their own status prose — checkable
with `git ls-remote --tags`. Overview and docs for the whole family:
**[aspark.lottes.dev](https://aspark.lottes.dev)**.

The two that *do* hook in are described in full — including what their evidence
does and does not cover — under [§Optional Tools](#optional-tools) below.

---

## Installation

**Requirements:** [Claude Code](https://claude.com/claude-code) and Git. For `/demo-day` you additionally need a browser integration (Claude in Chrome, or a Playwright / Chrome DevTools MCP server) — unless the project's constitution declares a substitute QA method, which `/charter` sets once for a project that has no browser-observable surface.

### The easy way — inside an interactive Claude Code session (recommended)

Do this in a **normal** (interactive) `claude` terminal session, using the built-in `/plugin` command. Dummy-proof version:

**1. Open Claude Code** in your terminal:

```
claude
```

**2. Add the marketplace** (the "shop" where the plugin lives — you only ever do this once):

```
/plugin marketplace add a-lottes/aSPARK
```

**3. Install the plugin** — read it as `pluginname@marketplacename`:

```
/plugin install aspark@aspark
```

> This marketplace carries **two** plugins: `aspark` (Core, above) and the
> optional `aspark-guard` — see [§The aSPARK Family](#the-aspark-family).
> Core works on its own; install the guard only if you want it.

**4. Restart Claude Code** — close and reopen your session (or `/exit`, then `claude` again). Plugins only activate after a restart.

**5. Check it worked:**

```
/plugin
```

This opens a menu of your installed plugins — you should see **aspark** listed and enabled.

### The non-interactive way — from a plain terminal

The `/plugin` menu command only works in an interactive session. In scripts, CI, or a non-interactive shell, use the full CLI equivalents — they do exactly the same thing:

```bash
claude plugin marketplace add a-lottes/aSPARK
claude plugin install aspark@aspark
```

### Local development install

To hack on aSPARK itself, point Claude Code at a local clone:

```bash
git clone https://github.com/a-lottes/aSPARK.git
claude --plugin-dir /path/to/aSPARK
```

> **One-line takeaway:** in a normal terminal → `/plugin marketplace add a-lottes/aSPARK` → `/plugin install aspark@aspark` → restart. Done. ✅

---

## Usage

No idea in hand? Let the Product Owner propose one from the project's current state:

```
You:     /next-steps
Claude:  [PO surveys shipped/in-flight/stalled work + constitution, proposes a feature]

You:     /story-time <the proposal you picked>
```

A typical feature, step by step:

```
You:     /story-time I want a dashboard where users see their weekly stats
Claude:  [PO challenges the idea, asks the hard questions, writes spec.md]

You:     /look-and-feel
Claude:  [Designer reviews the planned UI, flags design risks in spec.md]

You:     /sprint-plan
Claude:  [EM locks architecture, cuts tasks into plan.md]

You:     /increment
Claude:  [builds the increment, task by task, following plan.md]

You:     /peer-review
Claude:  [reviews the diff, writes findings, fixes what's obvious]

You:     /demo-day http://localhost:3000
Claude:  [clicks through the app in a real browser, checks every acceptance criterion]

You:     /go-live
Claude:  [changelog, tag, PR — only if all gates are green]
```

In a hurry? Run the whole loop with one command:

```
You:     /spark I want a dashboard where users see their weekly stats
```

`/spark` pauses at each gate and shows you the artifact before moving on — you stay the decision maker.

After a gate that followed heavy work — Act, QA, or any fix round — `/spark` also points out that you can `/clear` and pick the loop back up with `/spark`. The artifacts on disk *are* the state, so a fresh context resumes exactly where you stood, without carrying everything the last phase read and edited. It only ever offers; clearing is your call.

---

## How to Read This Toolbox

If you're new to Claude Code plugins, this is all there is to it:

- **`agents/`** — the team members. Each file defines one persona (a *subagent*): its mindset, its standards, and which tools it may use. Agents are the "who".
- **`skills/`** — the ceremonies. Each folder holds one slash command (`SKILL.md`): what to do, which agent to involve, which template to fill, and which gate to enforce. Skills are the "how".
- **`templates/`** — the artifacts. Blueprints for `constitution.md`, `spec.md`, `plan.md`, `review.md`, `qa.md` and `release.md`, each (bar the constitution) ending in an explicit gate checklist. Templates are the "what".
- **`lenses/`** — situational concern checklists (`seo`, `ux`, …). Activated by the project profile in the constitution and applied by the existing agents in the phases they own. Lenses are the "when it applies".
- **`tools/`** — guidance for optional external programs a ceremony may use *if you happen to have them installed*. Activated by installation state rather than by the constitution. Tools are the "if it's there".
- **`docs/`** — deep-dives: [`workflow.md`](docs/workflow.md) (the gate hand-over rules), [`status.md`](docs/status.md) (per-criterion proof state), [`metrics.md`](docs/metrics.md) (the method behind the figures below) and the [Enterprise Architecture Handbook](docs/aSPARK_Enterprise_Architecture_Handbook.docx) (`.docx`), which carries a delivery-stage label per chapter so ambition and delivery stay separable.
- **`.claude-plugin/`** — plugin metadata so Claude Code can discover and install all of the above. `marketplace.json` is also what publishes the optional `aspark-guard` alongside Core.

Alongside the folders, three documents at the repo root: [`ROADMAP.md`](ROADMAP.md) (what ships next, what's blocked, what was declined), [`CONTRIBUTING.md`](CONTRIBUTING.md) (how to add a skill, agent, lens or template without breaking the contract) and [`CLAUDE.md`](CLAUDE.md) (working habits kept across loops, distinct from the constitution's standing principles).

Reading order for newcomers: this README → `docs/workflow.md` → one template → one skill → one agent. After that you'll understand every file in the repo.

---

## Optional Tools

Some ceremonies can go faster when an external program is available. They **never
require one.** If it isn't installed, the loop behaves exactly as it does
today — no error, no warning, no mention. Two shapes exist: a **tool** a
ceremony probes for and passes by path (`tools/`), and a **companion plugin**
you install yourself, alongside Core, from the same marketplace.

These are the two siblings from [§The aSPARK Family](#the-aspark-family) that do
hook into the loop. *What* each one is stands in that table; what follows is how
it plugs in, and what its evidence does and does not cover.

**[`aspark-graph`](https://github.com/a-lottes/aSPARK-graph)** — when present,
`/sprint-plan` uses it to ground *Affected Components*, `/peer-review` to scope a
diff, and `/demo-day` to scope a test plan. It is **optional** — published on
PyPI as `aspark-graph` (`pip install aspark-graph`, or `uvx aspark-graph build .`
with no install step at all) — and nothing in aSPARK installs, builds or runs it
on your behalf. A result from it is treated as a map, never a verdict: it says
where to look, and the agent still reads the code and still performs the steps.

**[`aspark-guard`](https://github.com/a-lottes/aSPARK-guard)** — it addresses the
gap this project's own roadmap names: the gates are prompt-enforced, and hold
only until an agent under context pressure reasons its way around one
([#13](https://github.com/a-lottes/aSPARK/issues/13)). It is **optional** —
install it yourself with `/plugin install aspark-guard@aspark` — and nothing in
aSPARK installs, builds or runs it on your behalf. `aspark-guard` reports
substantial self-tested evidence — 142 tests replayed over 22 real gated
artifacts with no false positive, and an author-verified marketplace install
dated 2026-09-11 (its own `docs/evidence.md` §4) — but that evidence is
self-reported by the guard's own author, has not been independently verified by
aSPARK Core, and has never been exercised through a full third-party feature
loop, the same gap `ROADMAP.md` names about this project itself. This entry
makes no claim about gate enforcement that aSPARK Core has observed directly.

See [`tools/README.md`](tools/README.md) for how this works and how to add another.

---

## Project Status

> **What's next** is in [ROADMAP.md](ROADMAP.md) — what ships next, what's blocked, and what was deliberately declined. This section is what exists *today*.

aSPARK is feature-complete — everything below ships today. The column that matters
is **how well each part is proven**, because prompt material has no test suite: the
only evidence is a documented run, written down. This section always reflects the
current state.

### Dogfooding to date

The loop has been run on real projects, and the evidence for that is committed
rather than asserted: three machine reports sit in [docs/reports/](docs/reports/),
and [docs/metrics.md](docs/metrics.md) prints four `python3` commands that
re-derive every figure below from those files. Standard library only — no
install, no dependency, and no tool of this project's. So the arithmetic here is
checkable without trusting this page, and without any of the machines.

What that evidence cannot do is refresh itself. The counter that produced it is
no longer in this repository (constitution §3 allows Markdown and JSON only), so
the figures below are a closed measurement rather than a running total, and they
are dated for that reason.

#### Snapshot — 2026-09-10

Dated **evidence**, taken 2026-09-10 and not updated since:

| Spec | Plan | Review | QA | Release | Git tags | Role-agent runs | Human gate decisions |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 77 | 76 | 75 | 64 | 71 | 84 | 429 | 377 |

The gaps are real and left in. QA reached 64 of 77 — eight of the shortfall sit
in one library project with no browser surface, where `/demo-day` ran once across
nine features. Release reached 71 of 77 — three unreleased features sit in one
project that specified, planned, reviewed and QA'd them and shipped nothing, and
this repository's own `situational-lenses` has a spec and a verify-only sweep, not a shipped increment — see below.

**77 is a merge, not a sum.** The three machines report 51, 14 and 31 features,
which would add to 96 — but 3 projects sit on more than one machine (aSPARK on
all three) and 19 of their features are the same features, aSPARK's own 8 among
them. Adding the totals would have overstated the count by about a fifth.
Projects are matched on the hash of a repository's root commit, identical in
every clone, which is what makes that deduplication checkable rather than
claimed.

The first six columns come from `.spark/` artifacts and git on disk — verifiable
with `ls`, inferred from nothing. The last two come from Claude Code's own session
logs, summed across machines, since a session elsewhere is genuinely another
session; those logs are local to each machine and are the one input here a reader
cannot audit back to its source. The projects are deliberately not named: a count
needs no name to be checked. None of it is a token count, and
[docs/metrics.md](docs/metrics.md) explains why not, along with the method, the
four rules several reports combine under, and the honest `n/a`s.

The tool that produced these figures was removed in this repository's own
`metrics-script-removal` loop. It remains recoverable from git history at commit
`a2c0541` for anyone who wants to read what computed them.

The snapshot ends here. What follows is not dated and not frozen — it tracks
each part's proof state and is updated whenever that state changes, independent
of the 2026-09-10 figures above.

| Area | State |
|---|---|
| The loop — 10 skills, 7 agents, 6 templates, `/spark` | **Proven** — full end-to-end run on a sample app, all five gates enforced, shipped as `v0.1.0` |
| Spec-driven core — constitution, Clarify pass, NFRs, traceability | **Proven through Plan** — live review/QA traceability awaits a full `/increment` |
| Situational lenses (`lenses/`) | **Shipped; verified against aSPARK itself and three real external projects' own completed loop history** — not a fresh run, a read of loops that already ran. Both success-signal legs confirmed, each via a substitute lens (no project here declares `seo`-on-`website` or `api`); suppression confirmed in aggregate, with one active-lens project's own gap checked properly rather than taken at the first read — that project has no feature at all postdating its profile, so the honest verdict is unproven, not refuted; the add-a-file guarantee refuted for one skill file. Full ledger: [`.spark/situational-lenses/evidence.md`](.spark/situational-lenses/evidence.md) |
| Optional tools (`tools/`, `aspark-graph` only) | **25 of 30 criteria proven live** pre-sweep, six shipped `partial`; a 2026-08-26 verify-only sweep closed three of those six live, refuted one with a finding, and left two out of scope (still `unproven`) — see below |
| Companion plugin (`aspark-guard`) | Self-tested by its own author (142 tests / 22 replayed artifacts), not independently verified by Core, never run through a third-party loop — see [§Optional Tools](#optional-tools) for the full statement |
| PR-mode delivery (`handed-off`) | **Proven** on this repo's own release ([PR #3](https://github.com/a-lottes/aSPARK/pull/3)) |
| QA-method declaration (constitution §8) | **Shipped; declared path first exercised by this feature's own `/demo-day` and `/go-live`** — until then the fall-backs (absent, incomplete, unperformable, and a `yes`-surface project) are checked against constructed fixtures in `.spark/right-sizing/evidence.md`, and the declared path itself has not run. Not dogfooded on any other project. It removes one recurring per-feature question on a project that has no browser surface; it makes no other loop shorter and is not claimed to |

**What the lens layer's verify-only sweep found:** the generalized form of both
success-signal legs is confirmed from real project history — a UI lens QA-verified
and a Review-owned lens Review-verified, each under its own `NFR-n`, on a real
project's own completed loop. The literal legs stay unproven: no project
accessible to the sweep declares type `website` with `seo` active, or type `api`
— those two venues are still missing, not substituted for. Suppression holds in
aggregate (zero SEO/UX NFRs where no UI lens is active, non-zero where one is). The
sweep also found a real gap the aggregate hides, and checked it properly rather
than taking the first read: one project with an active UI lens shows zero
evidence the lens was ever applied to a real feature — but that project turns out
to have **no feature at all** that postdates its own profile, so there was never a
chance for the lens to fire or fail to. The honest verdict is unproven, not
refuted — the missing venue is a feature running after the profile exists, which
nobody has shipped yet. The add-a-file guarantee is refuted for one skill file,
which enumerates four lens filenames by name instead of the generic form every
sibling instruction uses. None of this was fixed in the sweep — verify-only by
design, findings routed onward — full ledger in
[`.spark/situational-lenses/evidence.md`](.spark/situational-lenses/evidence.md).
Lens compliance is still instruction-driven — no test enforces that a lens fires.
If you run aSPARK
on a real `website` or `api` project, [#4](https://github.com/a-lottes/aSPARK/issues/4)
and [#5](https://github.com/a-lottes/aSPARK/issues/5) are still waiting for you —
those two venues remain genuinely untested.

**Post-sweep proof state for issues #8–#11** (verify-only sweep, 2026-08-26 —
**[.spark/graph-gates-verification/evidence.md](.spark/graph-gates-verification/evidence.md)**):
**proven** — [#9](https://github.com/a-lottes/aSPARK/issues/9) (`/demo-day`'s
no-browser stop path) and [#11](https://github.com/a-lottes/aSPARK/issues/11)
(the `aspark-graph build` hint fires exactly once; a stale graph is announced
once, then treated as absent) both held live, start to finish, with a stated
counting method. [#10](https://github.com/a-lottes/aSPARK/issues/10) (browser
backends) is now **proven** for Playwright MCP and Chrome DevTools MCP, one
real navigation-plus-assertion each; Claude in Chrome remains the only backend
proven in an actual project run. **Refuted-with-finding** —
[#8](https://github.com/a-lottes/aSPARK/issues/8) (MCP-first precedence): the
MCP branch is real and is taken when tools are exposed, but repeated fresh
sessions against an identical registered environment did not reliably
reproduce the documented zero-probe-command guarantee, and the sweep's own
evidence points at a specific fix: the tool file's "run no command" and the
ceremony skills' "resolve both facts" give the MCP branch no documented,
command-free way to satisfy both at once. **Unproven, out of this sweep's
scope** — AC-1.2 (byte-identical output vs. the pre-change version) and AC-5.2
(omitting a `files:` note for a genuinely unknowable-at-plan-time task): this
feature never attempted either; they remain exactly as unproven as before.
`docs/status.md`'s full criterion table predates this sweep and is not yet
reconciled with it — a follow-up, not part of this diff.

Full evidence — every run, every `partial` and why it ships that way:
**[docs/status.md](docs/status.md)**.

---

## License

[MIT](LICENSE) © 2026 Andreas Lottes
