# The aSPARK family — companions and optional tools

Core is one repo of five. This page carries the full account of the siblings:
what each one is, whether it hooks into the loop today, how you get it, and
what its evidence does and does not cover. The README carries only the summary.

## The family

Core is one repo of five. Everything else is **optional** — Core has no hard
dependency on any of them (constitution §3), and a project that installs none
behaves exactly as documented in the README. The column that matters is the third one:
two of the four siblings do not touch the loop at all today.

| Repo | What it is | Hooks into Core today? | How you get it |
|---|---|---|---|
| **aSPARK** ([Core](https://github.com/a-lottes/aSPARK)) | The loop: 10 skills, 7 agents, 9 lenses, 6 templates | — it *is* Core | `/plugin install aspark@aspark` |
| [**aspark-guard**](https://github.com/a-lottes/aSPARK-guard) `v0.1.0` | Denies a `.spark/` write that violates a gate precondition; records every write with its hash | **Yes** — as a second plugin from the same marketplace | `/plugin install aspark-guard@aspark` |
| [**aspark-graph**](https://github.com/a-lottes/aSPARK-graph) `v0.7.0` | Deterministic graph over your `.spark/` artifacts and source code | **Yes** — `/sprint-plan`, `/peer-review` and `/demo-day` probe for it and pass it by path | `pip install aspark-graph` (PyPI) |
| [**aspark-insights**](https://github.com/a-lottes/aSPARK-insights) `v0.12.0` | Metrics over the graph's facts: traceability coverage, an offline HTML report, a release board, MCP queries | **No** — standalone; it reads the graph, not Core | source only, not on PyPI |
| [**aspark-policy**](https://github.com/a-lottes/aSPARK-policy) `v0.2.0` | Policy-as-code: a documented format, a tested JSON Schema, 11 catalog packs including `pci-dss`, `un-r155` and `misra` | **No** — a format and a catalog; the `validate` CLI and the Facilitator integration are unbuilt | Git submodule, no tooling to run |

Versions are the repos' latest git tags, not their own status prose — checkable
with `git ls-remote --tags`. Overview and docs for the whole family:
**[aspark.lottes.dev](https://aspark.lottes.dev)**.

The two that *do* hook in are described in full — including what their evidence
does and does not cover — under [Optional tools](#optional-tools) below.

---

## Optional tools

Some ceremonies can go faster when an external program is available. They **never
require one.** If it isn't installed, the loop behaves exactly as it does
today — no error, no warning, no mention. Two shapes exist: a **tool** a
ceremony probes for and passes by path (`tools/`), and a **companion plugin**
you install yourself, alongside Core, from the same marketplace.

These are the two siblings from [the family table](#the-family) that do
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

See [`tools/README.md`](../tools/README.md) for how this works and how to add another.

---
