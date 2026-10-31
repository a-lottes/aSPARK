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

> **aSPARK is in real use well beyond the author's projects. What's still missing is public, checkable runs, because most of that use is on closed-source code.**

Adoption figures and their source: [`docs/status.md` § Adoption](docs/status.md#adoption--snapshot-2026-09-30). Public, checkable evidence is the gap now; the [aSPARK reads](https://aspark.lottes.dev/en/blog/aspark-reads-flask/) series is one way it gets closed, field reports are the other. The lens layer was dogfooded on aSPARK itself and dry-run on two
sample apps, but its own spec defines success as a UI lens firing and being QA-verified on a real
`website` **and** a Review lens firing and being Review-verified on a real `api`. The `website` half now has one **partial** public run (2026-10-28, StartBootstrap Agency at a pinned commit, the `accessibility` lens activated from a declared constitution profile and QA-verified live in a browser; one run, one model, an assumed profile, an orchestrator-run dispatch, no screen reader): [`.spark/website-lens-public-run/evidence.md`](.spark/website-lens-public-run/evidence.md). It is not a rate and not a closed proof. The `api` half has one **partial** Review-only run (2026-10-26, spring-petclinic-rest PR #329 at `7690a61`): [`.spark/api-lens-public-run/`](.spark/api-lens-public-run/evidence.md). The lens text was passed by hand and a per-item trace was requested, so lens *activation* from a constitution and an unprompted firing rate are not shown; the target was not built, so two checks stay not-verified-live. **Second `website` run (2026-10-27):** on 11ty/eleventy-base-blog at `cf0cc1f`, built (`npm ci && npm run build`) and browser-verified, the constitution was written by `/charter` (Facilitator agent, dark mode, no person confirmed it) and put `seo`, `ux` and `security` on; they were dispatched by their `phases` fields, fired in Specify and QA (`ux` correctly silent in Review), with no per-item trace requested; trail in [`.spark/website-lens-seo-ux-run/`](.spark/website-lens-seo-ux-run/evidence.md). Misses are recorded (Review missed a failing code-block focus case that QA found; the spec was wrong about headers). Still not shown: a firing rate (n=1, one model), a lens-free control, Design and Act, an interactive site for `ux`, and a person confirming the profile.

There is a standing caveat behind it: lens compliance is instruction-driven. **No test enforces that a
lens actually fired** — only a person running the loop can tell us whether it did, and whether it was
right to.

If you use aSPARK on anything real, [a field report](https://github.com/a-lottes/aSPARK/issues/new?template=field_report.yml)
is worth more than a patch. Reports where it went badly are worth the most.

---

**Written, not yet Shipped:** `/next-steps` ticket triage, gap finding and typed recommendation (issue #110) exist in `skills/next-steps/SKILL.md` and `agents/product-owner.md`, exercised only as 4 single product-owner sessions on written fixtures (`docs/status.md`); the no-ticket path and a live `gh` run are unrun, so it stays here, **partial**, until they are.

## Shipped

| | |
|---|---|
| **The SPARK loop** | Five phases, five gates, ten ceremonies, seven agents. End-to-end on a sample app: PO → Designer → EM → build → review → real-browser QA → release. |
| **Spec-driven core** | Project constitution (`/charter`), the Specify-phase Clarify pass, non-functional requirements, and the `US-` / `AC-` / `NFR-` / `T` / `F` ID chain running unbroken from spec through plan, review and QA. |
| **Situational lenses** | Eight lenses activated by project **type** and **characteristics**, applied by the agents who already own each phase. New concerns are add-a-file: no agent is rewritten. |
| **Optional tools** | `tools/`, wired into `/sprint-plan`, `/peer-review` and `/demo-day`. Dogfooded in both directions — the absent case first, in a repo without the tool, where nothing may change. |
| **Honest PR-mode delivery** | `/go-live` reaches a `handed-off` terminal status where the project delivers by pull request instead of by tag. Proven on this repo's own release. |
| **Maturity labels in the handbook** | Every chapter of the architecture handbook carries a visible Delivery stage label, an overview table up front splits ambition from delivery, inline `Status.` markers name each target-state claim, and the title page separates the handbook revision from the shipped baseline (Core v0.7.0 · graph v0.7.0). Built as the `handbook-maturity` loop on this repo itself. |
| **No executable code, the method published instead** | `scripts/spark-metrics.py` is gone along with the directory, closing the constitution's own exception for it. `docs/metrics.md` now prints four `python3` commands over the committed machine reports, each with its observed output — the same figures README publishes stay checkable by a stranger holding nothing but this repository, though they can no longer be refreshed from it. Built as the `metrics-script-removal` loop on this repo itself. |
| **`/charter` as the single start-here, plus a Project Context (constitution §9)** | `/spark` and `/next-steps` now route a constitution-less project to `/charter` first, instead of pointing at each other; `/charter` runs a bounded greenfield kickoff interview or a brownfield discovery pass and writes one shared, evidenced `§9 Project Context` the Product Owner and Engineering Manager cite instead of each re-deriving the system. Each path proven once, on a different venue — greenfield on an empty scratch repo, brownfield on this repo's own constitution. Neither on an external project. Built as the `project-kickoff` loop on this repo itself. |
| **Ticket import and status write-back** | `/story-time <issue-number>` seeds the spec from a GitHub issue; `/go-live` posts one status comment to it when a release reaches a terminal status, only where the constitution's `Tracker write-back` field opts in. One direction only, GitHub Issues only. Read half proven on this repo's own issue #19; write half proven in a disposable scratch repo, including that a second release pass does not post again. The failure-skip and `Ticket: none` branches are not proven live, and neither half has run on an external project — [`docs/status.md`](docs/status.md) has the detail. Built as the `ticket-import` loop on this repo itself. |
| **Gate-evasion search, no rebuttal rows** | The repo's 51 review, QA and evidence files were searched under rules committed before the scan ([`.spark/adversarial-gates/evidence.md`](.spark/adversarial-gates/evidence.md)); it found 1 recorded gate evasion where the bar was 2 at the same gate, so **no rebuttal rows shipped** and no skill gained a row. In-repo trails, not field reports; effectiveness unmeasured, and whether a row would fire cannot be tested in Core; gates remain prompt-enforced. |
| **Visual QA review, binding design deviations, start-up robustness** | `/demo-day` asks for a screenshot per UI state at a wide and a phone viewport with one observation row each; a deviation from a `binding` design direction is at least `Major` and not QA-acceptable; the `ux` lens checks start-up with throwing storage, reload and resize; the Designer's visual craft check names scale and space use. Prompt-enforced, unmeasured: likely, not certain; one scratch dry run per case; only 2 of 6 Visual Review rows were imaged, then 4 of 4 after a follow-up rule, one session each ([`.spark/visual-qa-review/evidence.md`](.spark/visual-qa-review/evidence.md)). Code enforcement is `aspark-guard`'s. |
| **Stricter verdict rules for review and QA** | [`standards/anti-generosity.md`](standards/anti-generosity.md) (34 lines) is handed to the Reviewer and QA Tester by `/peer-review` and `/demo-day` on every run, with no setting: each item binary PASS/FAIL with its deciding observable, a partial check written exactly `⚠ not-verified-live`, the evaluation mode stated, no finding downgraded without a cited reason, a short banned-phrase list. **It changes verdicts for already-installed projects.** Prompt material only: it makes a strict verdict likely, not certain; its effect is unmeasured and the live dry runs were not performable in the build environment ([`.spark/adversarial-gates-standard/evidence.md`](.spark/adversarial-gates-standard/evidence.md)). Gates stay prompt-enforced; code enforcement belongs to [`aspark-guard`](https://github.com/a-lottes/aSPARK-guard). A second, independent reviewer is not built; re-open only on a new argument or observation, such as a recorded single-reviewer miss. |

---

## Next

**An observability lens** · [#15](https://github.com/a-lottes/aSPARK/issues/15)
Between the `api` lens (the contract) and the `security` lens (what must never be logged) sits a concern
nobody owns: whether a correct, secure, well-specified service can be diagnosed once it is running.
**Written, not yet Shipped:** `lenses/observability.md` exists and was dry-run once on a sample `api`
project (not a public run), so by this file's own vocabulary it stays under Next until a real `api`
exercises it. **Update, 2026-10-28:** a public Review-only run now exists
([`.spark/observability-lens-public-run/`](.spark/observability-lens-public-run/evidence.md), spring-petclinic-rest PR #302,
pinned at `c2cdc05`): one prompted session, 4 of 12 items fired, 8 silent, 4 lens findings of 10 (one Major: the rewritten error handler
records the cause nowhere). Partial only — the lens text was passed by hand with a requested trace, the target was not built, the
Specify half and the constitution activation were not exercised, and the unprompted firing rate is not shown; the lens therefore
stays under Next. The accessibility lens (#6) has since shipped; the performance lens
([#7](https://github.com/a-lottes/aSPARK/issues/7)) is still a proposal.

**In-flight doubt inside `/increment`** · [#14](https://github.com/a-lottes/aSPARK/issues/14)
Doubt is currently a *phase*: `/peer-review` runs after the build. So a wrong premise adopted in task 2
is not challenged until task 12 stands on it. Task-level verification cannot catch this — a task built on
a wrong assumption passes its own definition of done perfectly. Carries a real risk of making the longest
phase longer; if it cannot be kept cheap and rare, it should not ship.

---

## Blocked

**A template version handshake** · `template-version-marker`
Artifacts shaped by `templates/` are parsed outside this repo by two consumers, on a contract with
three repos in all (Core plus both):
[`aspark-graph`](https://github.com/a-lottes/aSPARK-graph), which pins `SUPPORTED_TEMPLATE`, and
[`aspark-guard`](https://github.com/a-lottes/aSPARK-guard), which re-encodes the same structures a
second time (story heading, AC line, findings-table columns, `Status` header row) and checks them at
write time. That write-time check is a second structural guess, not a handshake.
**Core's side is shipped:** every template carries `<!-- aspark-template: aspark/0.1.0 -->`. Still open,
in the consuming repos: `aspark-graph` asserting it (replacing its structural guess with a named version
conflict) and `aspark-guard` reading it instead of its own copy. Until both do, the marker is read by
nobody; the rule stands that all repos ship the reading side together.

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
| **Code-enforced SPARK gates inside Core** | Belongs in the sibling plugin [`aspark-guard`](https://github.com/a-lottes/aSPARK-guard), where a runtime exists to enforce with — Core ships Markdown and JSON only, with no runtime of its own (constitution §3). Self-tested by its own author (142 tests / 22 replayed artifacts), not independently verified by Core, never run through a third-party loop — see [README §Optional Tools](README.md#optional-tools). |

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
