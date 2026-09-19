# Status & Evidence

The README carries the summary. This file carries the proof.

aSPARK ships Markdown prompt material — there is no test suite and none is
possible, so the only evidence a capability works is a **documented run of the
phases it touches**, negative case first. That is the project constitution's bar,
and this file is where those runs are written down.

Nothing here is aspirational. If something is unproven, it says so.

---

## At a glance

Moved here from the README on 2026-09-19 so the README can stay short; the
content is unchanged and continues to be updated here.

aSPARK is feature-complete — everything below ships today. The column that matters
is **how well each part is proven**, because prompt material has no test suite: the
only evidence is a documented run, written down. This section always reflects the
current state.

### Dogfooding to date

The loop has been run on real projects, and the evidence for that is committed
rather than asserted: three machine reports sit in [docs/reports/](reports/),
and [docs/metrics.md](metrics.md) prints four `python3` commands that
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
[docs/metrics.md](metrics.md) explains why not, along with the method, the
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
| Situational lenses (`lenses/`) | **Shipped; verified against aSPARK itself and three real external projects' own completed loop history** — not a fresh run, a read of loops that already ran. Both success-signal legs confirmed, each via a substitute lens (no project here declares `seo`-on-`website` or `api`); suppression confirmed in aggregate, with one active-lens project's own gap checked properly rather than taken at the first read — that project has no feature at all postdating its profile, so the honest verdict is unproven, not refuted; the add-a-file guarantee, refuted for one skill file at the time of this sweep, has since been closed across all eight resolved-instruction sites by `lens-dispatch-registry` — see [`.spark/lens-dispatch-registry/evidence.md`](.spark/lens-dispatch-registry/evidence.md). Two prose lens-count copies (`docs/status.md`, `docs/workflow.md`) remain stale as of that feature's own sweep — a separate, named documentation-accuracy finding, not a reopened dispatch gap. Full ledger: [`.spark/situational-lenses/evidence.md`](.spark/situational-lenses/evidence.md) |
| Optional tools (`tools/`, `aspark-graph` only) | **25 of 30 criteria proven live** pre-sweep, six shipped `partial`; a 2026-08-26 verify-only sweep closed three of those six live, refuted one with a finding, and left two out of scope (still `unproven`) — see below |
| Companion plugin (`aspark-guard`) | Self-tested by its own author (142 tests / 22 replayed artifacts), not independently verified by Core, never run through a third-party loop — see [`family.md` §Optional tools](family.md#optional-tools) for the full statement |
| PR-mode delivery (`handed-off`) | **Proven** on this repo's own release ([PR #3](https://github.com/a-lottes/aSPARK/pull/3)) |
| QA-method declaration (constitution §8) | **Shipped; declared path first exercised by this feature's own `/demo-day` and `/go-live`** — until then the fall-backs (absent, incomplete, unperformable, and a `yes`-surface project) are checked against constructed fixtures in `.spark/right-sizing/evidence.md`, and the declared path itself has not run. Not dogfooded on any other project. It removes one recurring per-feature question on a project that has no browser surface; it makes no other loop shorter and is not claimed to |
| `/charter` as the single start-here + Project Context (constitution §9) | **Shipped; each path proven once, on a different venue.** The greenfield kickoff interview ran real, start to finish, on an empty scratch repo outside this tree — not a real product, not a field report. The brownfield discovery pass ran real on this repo's own constitution, migrating its improvised preamble into §9. Neither path has run on an external project; no saving is claimed beyond these two venues, and no first-run field report exists yet. Full ledger: [`.spark/project-kickoff/evidence.md`](../.spark/project-kickoff/evidence.md) |

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
nobody has shipped yet. The add-a-file guarantee was refuted for one skill file
at the time of this sweep — findings routed onward, not fixed here, verify-only
by design. That routed finding has since been closed: `lens-dispatch-registry`
replaced every closed lens-name enumeration this sweep found (and two more of
the same shape it didn't) with a rule read from `lenses/README.md`'s own
registry and each lens's own frontmatter, across all eight resolved-instruction
sites — see [`.spark/lens-dispatch-registry/evidence.md`](.spark/lens-dispatch-registry/evidence.md)
for the worked proof against all 9 shipped lenses. Two prose lens-count copies
outside any dispatch or activation path (`docs/status.md`, `docs/workflow.md`)
remain stale as a separate, named documentation-accuracy finding — full ledger
in
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



---

## The loop

| | |
|---|---|
| **Scope** | 10 ceremony skills, 7 agents, 6 templates, the `/spark` orchestrator |
| **Evidence** | Full end-to-end loop run on a vanilla-JS `quick-todo` app: PO → Designer → EM → build → review → real-browser QA → release. All five gates enforced. Shipped as `v0.1.0`. |
| **State** | Proven |

## Spec-driven core

| | |
|---|---|
| **Scope** | Project constitution (`/charter`), Specify-phase Clarify pass, non-functional requirements, `US-` / `AC-` / `NFR-` traceability from spec through plan, review and QA |
| **Evidence** | Dry run on a vanilla-JS `quicknote` app: `/charter` → `/story-time` (with Clarify pass) → `/look-and-feel` → `/sprint-plan`. The constitution bound every phase; NFRs and the ID chain flowed spec → plan with full Must-AC coverage; the spec and plan gates were enforced. |
| **State** | Proven through the Plan phase. Live review/QA traceability tables still await a full `/increment` build. |

## Situational lenses

| | |
|---|---|
| **Scope** | `lenses/` — the constitution profile detects project **type** (`website`, `web-app`, `api`, `cli`, `library`) and **characteristics** (auth, PII, public, database, multilingual), activating concern checklists (`seo`, `ux`, `api`, `cli`, `library`, `security`, `i18n`, `data`) that the existing agents apply in the phases they own. The constitution is the single source of truth — no constitution means a nudge, never an applied lens. Four or more active lenses flag elevated load. A new concern is add-a-file; no agent is rewritten. |
| **Evidence** | Dogfooded through aSPARK's own `/story-time` ([`.spark/situational-lenses/spec.md`](../.spark/situational-lenses/spec.md)). The PO's Clarify pass caught two real defects in the first cut — per-phase fallback detection was over-built and drift-prone, and lens load had no visibility — both fixed before commit. |
| **State** | **Shipped, unproven in the field.** See *The open gap* below. |

### The open gap

The lens layer's own spec defines success as **a UI-lens firing and being
QA-verified on a real `website`**, *and* **a Review-lens firing and being
Review-verified on a real `api`** — both under the same `NFR-n`.

Neither has been demonstrated by a full loop run on a real project.

**Standing caveat:** lens compliance is instruction-driven. No test enforces that a
lens actually fired, and none can. A field report from someone else's project is
the only evidence that counts here — which is why it is the most valuable thing
you can contribute right now.

## Optional tools layer

| | |
|---|---|
| **Scope** | `tools/`, wired into `/sprint-plan`, `/peer-review` and `/demo-day` |
| **Evidence** | Dogfooded end to end against the *installed* plugin, across two QA rounds ([`.spark/graph-gates/qa.md`](../.spark/graph-gates/qa.md)): the **absent** case by real ceremony invocations in a graph-less repo, and the **available** case by direct agent runs against an isolated graph-built scratch copy. (The designated real-project venue was left untouched — it had independent work in flight.) |
| **State** | **25 of 30 acceptance criteria pass live; zero remain unverified.** Six ship as a documented `partial`. |

Every documented call form, return shape and failure mode was run against the tool
itself, and the `files:` note format was validated by running the consuming parser.

All other wiring claims are proven by a real run rather than a walkthrough: the
tool-file hand-over firing live, the QA slice scoping a real test plan via
`story_trace`, a review citing concrete `file:line` evidence, and an EM agent
correctly classifying an empty `impact` result as "no declared link" rather than
"nothing at risk".

### The six `partial` criteria

Each ships `partial` for a specific, named reason rather than as an open gap. This
was an explicit, informed shipping decision, not an oversight.

| Criterion | What is not (yet) proven, and why | Tracked as |
|---|---|---|
| AC-1.2 | Byte-identical output vs. the pre-change version — needs a direct 0.3.1-vs-0.4.0 artifact diff, one more full ceremony pair | — |
| AC-2.2 | MCP-first precedence — no MCP server existed in any environment used for testing so far | [#8](https://github.com/a-lottes/aSPARK/issues/8) |
| AC-2.3 | The installed-but-unbuilt hint firing exactly once inside a live ceremony transcript (verified at the tool level, not yet caught mid-ceremony) | [#11](https://github.com/a-lottes/aSPARK/issues/11) |
| AC-3.2 | The ceremony's own reaction to a stale graph — say once, then treat as absent. The underlying `staleness` behaviour itself *is* verified live, twice | [#11](https://github.com/a-lottes/aSPARK/issues/11) |
| AC-3.5 | `/demo-day`'s existing no-browser stop path — this project has no browser surface to re-prove it against. A pre-existing exception, not a new one | [#9](https://github.com/a-lottes/aSPARK/issues/9) |
| AC-5.2 | Omitting a `files:` note for a genuinely unknowable-at-plan-time task — this feature's own plan has no such task to exercise the path on | — |

## Delivery mode

| | |
|---|---|
| **Scope** | PR-mode delivery with `handed-off` as the loop's terminal status |
| **Evidence** | Proven live on this repo's own release: the constitution declares PR-mode delivery, [PR #3](https://github.com/a-lottes/aSPARK/pull/3) was opened, self-reviewed and merged, and `.spark/tracker-handoff/release.md` reached status `handed-off` with **no tag created before merge**. |
| **State** | Proven |

## Lean artifacts

| | |
|---|---|
| **Scope** | A heading-less **Handoff** block (status, one-line verdict/summary, open items, which section binds, conflict precedence) above the first numbered section of all five artifact templates (`review-report.md`, `qa-report.md`, `spec.md`, `plan.md`, `release-notes.md`), so a downstream phase can route off a bounded read instead of the whole file. Reading/writing rules were added to every consumer that acts on a predecessor artifact: `agents/reviewer.md` (re-review), `skills/increment/SKILL.md` (fix-mode write-back — not the report's owner, but overwrites the block in place on every fix), `agents/release-manager.md`, `agents/product-owner.md` and `skills/next-steps/SKILL.md`. |
| **Evidence** | Dogfooded negative-case-first ([`.spark/lean-artifacts/evidence.md`](../.spark/lean-artifacts/evidence.md)): old-shape artifacts keep working unchanged, a real fix-mode edit overwrote the block in place instead of appending, and the sibling `aspark-graph` parser was read directly and confirmed structurally blind to the block (no new `##` heading, no second `Status`/`Version` row) — independently re-verified by both the Reviewer and the QA Tester against the parser's actual source, not each other's citation of it. |
| **State** | **Proven**, with a recorded, user-accepted waiver: two Must ACs (the zero-open-items rendering, an exact block/body value-contradiction) are `partial` rather than `pass` — neither has a naturally-occurring specimen in this repo yet, only the mechanism exercised on adjacent/constructed cases. **No token or byte saving is claimed anywhere** — the mechanism is a prompt instruction, not an enforced one. |

## Browser backends for `/demo-day`

| | |
|---|---|
| **Scope** | Claude in Chrome, Playwright MCP, Chrome DevTools MCP |
| **Evidence** | Only **Claude in Chrome** has been used in a real QA run. |
| **State** | The other two are documented but unproven — tracked as [#10](https://github.com/a-lottes/aSPARK/issues/10). |

---

## Build checklist

- [x] Repo scaffold, plugin manifest, license
- [x] README with concept, team and usage guide
- [x] Artifact templates (`templates/`) — constitution, spec, plan, review-report, qa-report, release-notes, each (bar the constitution) with its gate checklist
- [x] The seven team agents (`agents/`) — facilitator, product-owner, designer, engineering-manager, reviewer, qa-tester, release-manager
- [x] The ten ceremony skills (`skills/`) — charter, next-steps, story-time, look-and-feel, sprint-plan, increment, peer-review, demo-day, go-live, spark
- [x] Spec-driven core — constitution, Clarify pass, NFRs, `US-`/`AC-`/`NFR-` traceability
- [x] Situational lenses (`lenses/`), dogfooded through aSPARK's own loop
- [x] The `/spark` orchestrator — full loop with gate stops, resume support and feedback-loop escalation
- [x] Optional tools layer (`tools/`) — dogfooded against the installed plugin
- [x] Workflow deep-dive ([`workflow.md`](workflow.md)) — constitution, artifact chain, gate invariants, traceability, feedback loops, role boundaries
- [x] Plugin structure validated (`claude plugin validate` ✔, skill/agent naming consistent)
- [x] End-to-end test on a sample project (`quick-todo`)
- [x] Spec-driven dry run on a sample project (`quicknote`)
- [x] `tracker-handoff`'s positive case proven on this repo's own release
- [x] Lean artifacts — a Handoff block in all five templates plus reading/writing rules in every consumer; see *Lean artifacts* above
- [ ] **Success signal proven on real projects** — see *The open gap* above
