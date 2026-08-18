# Status & Evidence

The README carries the summary. This file carries the proof.

aSPARK ships Markdown prompt material — there is no test suite and none is
possible, so the only evidence a capability works is a **documented run of the
phases it touches**, negative case first. That is the project constitution's bar,
and this file is where those runs are written down.

Nothing here is aspirational. If something is unproven, it says so.

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
