# Plan: companion-offer

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/companion-offer/spec.md` (`approved`, 2026-09-14) |
| **Status** | `approved` |
| **Date** | 2026-09-14 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `approved` by the user, 2026-09-14, including T5's ROADMAP "Not planned" row as drafted.
- **Summary:** No architecture — docs-only. The decisions are a *single canonical maturity wording* pinned once in `evidence.md` and quoted by all three prose surfaces, a *hard four-path file fence* (NFR-1 is the spec), and *additive-only edits* (new column, new paragraph, new row; no heading renamed, no existing prose reflowed).
- **Open:** `8 tasks not done` — see §3 Task Breakdown for which
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** There is no architecture to decide. This repo ships Markdown and JSON with no runtime, no build and no executable code (constitution §3), and the spec's NFR-1 asserts the whole deliverable as a diff-scope claim: three prose surfaces change, nothing under `skills/`, `agents/`, `templates/`, `lenses/`, `.claude-plugin/` does, and under `tools/` only `README.md`. What is genuinely at risk is not structure but **wording discipline and sequencing**: one qualified maturity claim (AC-1.3) has to appear consistently in three files (AC-3.3), and the diff has to stay inside its fence while prose is being written (NFR-5 names scope creep as the first constraint that would break).
- **Decision:** Four rules, applied to every task below.
  1. **Pin the wording once, quote it three times.** The canonical qualified maturity statement, its declared short form, and the literal install string are written into `.spark/companion-offer/evidence.md` **before** any prose lands (T1), and every later task quotes that block rather than re-deriving a claim from the guard's README.
  2. **Fence the diff by path, not by intent.** Exactly four tracked files may change: `README.md`, `tools/README.md`, `ROADMAP.md`, and artifacts under `.spark/companion-offer/`. Any task touching a fifth path is a plan defect, not a judgement call. The fence is measured at T7, and its pre-state is captured at T1 so the negative case runs first (constitution §4).
  3. **Additive-only edits.** Add a table column, a paragraph, a status-table row. Do not rename a heading, do not reflow an untouched paragraph: `## Optional Tools` and `## Tool or lens?` are cited by `tools/README.md:114`, `.spark/graph-gates/qa.md:117` and the spec's own AC-2.1, and renaming them makes those citations false for cosmetic gain. It also keeps `git diff` readable as pure additions, which is what makes AC-2.4's byte-identity claim cheap to check.
  4. **The version bump is not in this diff.** NFR-1 forbids `.claude-plugin/`, so `plugin.json` (currently `0.8.1` on `main`) is **not** edited here; NFR-3's patch bump to `0.8.2` is recorded as `/go-live`'s action (T7) with its one-line reasoning: docs only, no optional capability added, so §5's minor-bump trigger is absent.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Write each file's guard wording independently, in each file's own voice | AC-3.3 names exactly this failure. Three independent drafts of a *qualified* claim drift toward the shortest word available (`proven`/`unproven`), and drift here is a §1 honesty defect, not a style nit |
  | Add `tools/aspark-guard.md` so the guard lives where `aspark-graph` lives | Spec §6 item 8. The guard has no probe, no phase slice and nothing to pass by path — a tool file for it is precisely the defect US-2 exists to prevent, and it would break NFR-1's `tools/README.md`-only clause |
  | Rename `## Optional Tools` → "Optional Tools and Companions", and `## Tool or lens?` → "Tool, lens or companion plugin?" | Three live citations (above) point at those literal headings; `README.md#project-status`-style anchors are part of the contract clarity the `library` lens §4 asks for. Widen the section's *intro clause* instead, which costs one sentence and breaks no citation |
  | Carry the patch bump in this feature's own diff so the release is self-contained | Falsifies the feature's own success signal — NFR-1 lists `.claude-plugin/` among the paths the diff must not contain. Recording the decision costs nothing; `/go-live` executes it |
  | Give the guard a **Shipped** row in `ROADMAP.md` | `ROADMAP.md:9` states its own rule: "A thing is Shipped only when it has been exercised, not when it has been written." Core has exercised nothing of the guard (evidence.md, AC-1.3 cross-check: not even installed on this machine). Decision: the **Not planned** table instead, scoped to *Core-side* gate enforcement — see T5, and the risk row that flags it for the user's gate walk |
- **Consequences:** Easier — a late wording change is one edit in `evidence.md` plus three quote updates; the diff is auditable against NFR-1 with a single `git diff --name-only`; AC-2.4 holds by construction because no task lists `tools/aspark-graph.md` or the probe-bullet section. Harder — every prose task is blocked on T1, so there is no parallel start; T6's cross-file pass is real work, not a formality; and the plan carries one product judgement (the ROADMAP status word) that only the user can confirm.

## 2. Affected Components

Scoped **by hand**, deliberately. The `aspark-graph` tool is available this run, but its own tool file states that only source files are indexed (`.py .ts .tsx .js .jsx .mjs .cjs .java .go .rs`) and that "a Markdown-only or config-only project has no file nodes at all, so `impact` is legitimately empty there — that is this case, not a defect". An `impact` query over `README.md`, `tools/README.md`, `ROADMAP.md` would therefore return those paths under `unknown_files` with empty `affected_stories` / `affected_acs`, which means *the graph does not index these files*, never *nothing is at risk*. No graph result is cited below. If the query is run anyway, its result is recorded in `evidence.md`, not used to widen or narrow this list.

| File | What changes | What must not change |
|---|---|---|
| `README.md` | §Optional Tools (currently 216–231): intro clause widened to name two shapes; one new paragraph for `aspark-guard` after the `aspark-graph` paragraph. §Project Status table: `Optional tools` row (302) scoped explicitly to `aspark-graph`; one new row for the companion plugin | The `## Optional Tools` and `## Project Status` headings; the `aspark-graph` paragraph; the 2026-09-10 snapshot block (258–295) and every other status row |
| `tools/README.md` | §"Tool or lens?" (13–30): table (19–24) gains a third column; one new paragraph after it | The `## Tool or lens?` heading; §"The canonical probe bullet" (46–84) **byte-identical**; §Available tools (121–125) exactly one row; §"The tool file contract"; §"Adding another tool" |
| `ROADMAP.md` | One new row in the **Not planned** table (94–101), per T5 | The status-vocabulary paragraph (7–10); the Shipped / Next / Blocked sections, including the `template-version-marker` Blocked entry (#44) and the #13 Next entry |
| `.spark/companion-offer/evidence.md` | Appended sections: canonical wording, baselines, clause-for-clause comparison, diff-scope + validate output, live install result | The existing Specify-phase sections (Provenance, AC-1.2, AC-1.3) — appended to, never rewritten |
| `.spark/companion-offer/plan.md` | Task statuses, per `/increment` | — |

**Explicitly not touched, and a task that touches one is a plan defect:** `tools/aspark-graph.md`, anything under `skills/`, `agents/`, `templates/`, `lenses/`, `.claude-plugin/` (including `plugin.json` and `marketplace.json`), `docs/status.md`, `docs/metrics.md`, `docs/reports/`. No new dependency, no new file, no new service — this change adds three prose blocks and zero files.

## 3. Task Breakdown

The walking skeleton is T1→T2: after two tasks the feature's Must story is end-to-end true — the guard is documented where the first companion is, and AC-1.1's `grep` flips from zero tracked `.md` files to `README.md`. Everything after T2 is consistency and proof.

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Pin the canonical wording and capture the pre-change baseline (negative case first) | US-1 | AC-1.1, AC-1.3, AC-3.3, NFR-6 | – | `done` | `evidence.md` gains a **Canonical wording** section holding, verbatim and quotable: (a) the qualified maturity statement naming the guard's self-reported evidence (142 tests over 22 real gated artifacts; author-verified install dated 2026-09-11, per the guard's own `docs/evidence.md` §4), that it is self-reported and not independently verified by aSPARK Core, and that it has never run a full third-party feature loop; (b) a declared short form for table cells; (c) the literal install string `/plugin install aspark-guard@aspark`; each with its source cited to this file's existing Specify-phase sections. Plus a **Baseline (pre-change)** section recording the observed output of `grep -rl 'aspark-guard' --include='*.md' . ` with `.spark/` excluded (expected: nothing) and `git diff --name-only main...HEAD` (expected: only paths under `.spark/companion-offer/`), each with its date — files: .spark/companion-offer/evidence.md |
| T2 | Document the guard in `README.md` §Optional Tools (walking skeleton) | US-1 | AC-1.1, AC-1.2, AC-1.4, AC-1.3, NFR-4 | T1 | `done` | The section intro (218–220) gains one clause naming that this section covers two shapes — an optional tool a ceremony probes, and a companion plugin the user installs in the host — without renaming the heading. One new paragraph for `aspark-guard` follows the `aspark-graph` paragraph and carries, clause for clause against it: what the plugin does; that it is optional; that nothing in aSPARK installs, builds or runs it on the user's behalf; the literal command from T1; T1's qualified maturity statement; and what its evidence must never be read as (gate enforcement aSPARK Core has itself observed). It names the concrete gap it addresses — prompt-enforced gates — cross-referenced to [#13](https://github.com/a-lottes/aSPARK/issues/13) / ROADMAP §Next, and does not restate the `marketplace.json` description. The body of the guard paragraph is at most four sentences. `grep -rl 'aspark-guard' --include='*.md' .` with `.spark/` excluded now returns `README.md` — files: README.md |
| T3 | Account for both companions in `README.md` §Project Status | US-3 | AC-3.1, AC-3.3 | T1, T2 | `done` | The `Optional tools (tools/, aspark-graph)` row (302) states explicitly that it covers `aspark-graph` only, and one new row for the companion plugin `aspark-guard` carries T1's declared short form plus a pointer to §Optional Tools where the full statement lives. No other row, and no line of the 2026-09-10 snapshot block, is modified; the section's own assertion that it "always reflects the current state" is now true for both companions — files: README.md |
| T4 | Add the third shape to `tools/README.md` §"Tool or lens?" | US-2 | AC-2.1, AC-2.2, AC-2.3, AC-2.4, NFR-2 | T1 | `done` | The comparison table (19–24) gains a third column, **Companion plugin (`.claude-plugin/marketplace.json`)**, with a cell on each of the four existing axes (what it is · activated by · who decides · example) and `aspark-guard` as the Example. One paragraph after the table states that a companion plugin is installed by the user in the host, is never passed by path, has no tool file and no probe, and that adding a `tools/<name>.md` for one is a defect. §Available tools still lists exactly one row (`aspark-graph.md`). `git diff main -- tools/README.md` shows no hunk inside §"The canonical probe bullet" (46–84) and no renamed heading; `git diff main -- tools/aspark-graph.md` is empty — files: tools/README.md |
| T5 | Account for the guard in `ROADMAP.md` using its literal status vocabulary | US-3 | AC-3.2, AC-3.3 | T1 | `done` | The **Not planned** table (94–101) gains one row — *Code-enforced SPARK gates inside Core* — whose why-cell states in one sentence that Core ships Markdown and JSON only and has no runtime to enforce with (constitution §3), so gate enforcement is distributed as the optional sibling plugin `aspark-guard`, whose maturity is T1's short form, with a pointer to README §Optional Tools. It uses one literal status word from line 7's vocabulary, does not restate issue #45, and leaves the Shipped, Next and Blocked sections byte-unchanged. `grep -n 'guard' ROADMAP.md` returns at least this row — files: ROADMAP.md |
| T6 | Cross-file consistency pass | US-1, US-2, US-3 | AC-3.3, NFR-4 | T2, T3, T4, T5 | `done` | The guard's maturity claim in `README.md` §Optional Tools, `README.md` §Project Status and `ROADMAP.md` is T1's statement or its declared short form in each — no fourth wording, no looser claim anywhere. A five-row comparison table in `evidence.md` lays the `aspark-graph` and `aspark-guard` README entries side by side on NFR-4's five clauses (what it does · optional · nothing installs it for you · exact user-run command · what its answer must never be read as) and records a hit or a gap per clause; any gap is fixed in the source file before this task closes — files: .spark/companion-offer/evidence.md, README.md, ROADMAP.md |
| T7 | Diff-scope sweep and `claude plugin validate` | US-1, US-2, US-3 | NFR-1, NFR-2, NFR-5, NFR-7, NFR-3, AC-1.1 | T6 | `done` | `git diff --name-only main...HEAD` is run and its output pasted into `evidence.md`: it lists exactly `README.md`, `tools/README.md`, `ROADMAP.md` and paths under `.spark/companion-offer/` — no path under `skills/`, `agents/`, `templates/`, `lenses/` or `.claude-plugin/`, and under `tools/` only `README.md`. `git diff main -- tools/aspark-graph.md` is empty (AC-2.4's other half). `claude plugin validate` is run and its observed output recorded. AC-1.1's post-change `grep` is re-run and recorded against T1's baseline. The NFR-3 decision is recorded in one line — `plugin.json` stays at `0.8.1` in this diff by NFR-1; `/go-live` proposes `0.8.2`, patch because docs-only adds no optional capability — files: .spark/companion-offer/evidence.md |
| T8 | Execute the install command live and close the evidence trail (`/demo-day`) | US-1 | AC-1.5, AC-1.6, NFR-5, NFR-6 | T7 | `done` | **Only after the user's explicit go in the conversation** (constitution §6 — nothing installed on the user's behalf unasked), `/plugin install aspark-guard@aspark` is run against the live marketplace and its outcome — success, failure, or observed prompt behaviour — is recorded in `evidence.md` with date and result, explicitly independent of the guard's own self-reported 2026-09-11 verification. Every URL added by this feature is opened and its result recorded with date and method. Whether the guard was kept installed or removed afterwards is recorded. With the guard present, one real ceremony invocation is observed and the count of prompts, questions or sentences it adds relative to the same ceremony without the guard is recorded as **0** (NFR-5's both-present leg; the both-absent leg is T7's diff scope) — files: .spark/companion-offer/evidence.md |

## 4. Test Strategy

There is no automated test suite and none is possible for prompt material (constitution §4) — no NFR here assumes one. The bar is `claude plugin validate` plus a documented dogfood, **negative case first**, per constitution §1 and §8's substitute method: a performed step is a real ceremony invocation or a real command whose output was observed; reading a Markdown file and reasoning about it is never a performed step.

- **Negative case, first and last (NFR-1, NFR-2, NFR-5, US-1…US-3).** This feature touches no phase, so the negative case is the *whole* dogfood: the diff itself. Its pre-state is captured at T1 before a word is written, and it is re-measured at T7 as `git diff --name-only main...HEAD` plus an empty `git diff main -- tools/aspark-graph.md`. A consumer who has aSPARK installed and neither companion present sees an identical loop, because no file any ceremony reads changed.
- **Positive, executable checks (US-1).** AC-1.1 is a `grep` with a recorded before and after (T1, T7). AC-1.6 is a real `/plugin install aspark-guard@aspark` run at `/demo-day` (T8) — the one step here that changes the user's machine, hence gated on the user's explicit go, with the keep-or-remove outcome recorded. NFR-7 is `claude plugin validate` with its output pasted (T7).
- **Read-and-compare checks, deliberately not automated (US-2, US-3, NFR-4, NFR-6).** AC-1.2/1.3/1.4, AC-2.1/2.2/2.3, AC-3.1/3.2/3.3 are prose properties. They are verified by the T6 side-by-side table in `evidence.md` — a written comparison with a hit-or-gap per clause, not an assertion that it was checked — and re-verified by the Reviewer against the diff at `/peer-review`. Manual is the only option: there is no linter for "is this claim honestly qualified", and inventing one would be the tracked executable code constitution §3 forbids.
- **No `/demo-day` browser leg.** Constitution §8: `Browser-observable surface: no`. `/demo-day`'s role here is T8's install execution and the NFR-5 both-present observation, nothing else.
- **Not tested, on purpose.** Whether the guard actually enforces gates. Core cannot verify that without a third-party loop (evidence.md, AC-1.3), and AC-1.3 exists precisely so the docs never claim it.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| The AC-1.3 maturity framing lands wrong — the self-reported evidence reads as Core's own proof, or the qualification is flattened to `proven`/`unproven` while copy-editing | A §1 honesty-bar defect in the repo's most-read file, and the exact failure the feature exists to fix, committed in the fix | T1 pins the sentence before any prose; T2/T3/T5 quote it; T6 compares all three surfaces and records gaps per clause. The user is asked to read the exact sentence at the plan gate, since A3/C6 were flagged as a judgment call, not a mechanical resolution |
| Wording drift between `README.md`, `README.md` §Project Status and `ROADMAP.md` (AC-3.3) — three files, three editing sessions, a shorter word each time | The repo contradicts itself about the same plugin, which is a worse version of the defect being fixed | Only two permitted wordings exist (statement + declared short form), both in `evidence.md`; T6 is a dedicated task, not a checkbox on another one |
| Scope creep back toward the cut offer while writing — "one line in `/charter` would help here" | Breaks NFR-5 and NFR-1, charges every consumer's setup, and reopens a decision the user already made | The path fence is mechanical (§1 rule 2, T7's `git diff --name-only`), and spec §6 lists all ten cuts with their reopen conditions. Any such idea becomes a note in the release's follow-ups, never a hunk |
| The ROADMAP status word (T5) is a product judgement, not a mechanical one — "Not planned" for Core-side gate enforcement could read as declining issue #13 | A false statement about Core's own roadmap, in the file that governs order | T5's row is scoped narrowly to *enforcement inside Core*, grounded in constitution §3 (no runtime, no executable code) rather than in a new decision, and leaves #13 untouched. **Flagged for the user's call at the plan gate** — see the open question below |
| T8 installs a gate-enforcing plugin into the user's live host mid-loop; it could change how this repo's own remaining ceremonies behave | An unasked-for change to the user's environment — constitution §6's non-negotiable | T8 runs only after the user's explicit go, at `/demo-day` (after the increment's writes), and records whether the guard was kept or removed. If the user declines, AC-1.6 is recorded as `not-verified-live` with the reason, which is an honest outcome, not a failure to grind past |
| An edit slips into `tools/aspark-graph.md` or the canonical probe bullet while adding the third shape (AC-2.4) | Silent change to material three skills duplicate verbatim; the four-state degrade-to-silence contract is §6 non-negotiable | No task lists `tools/aspark-graph.md`; T4's DoD requires an empty diff for it and no hunk inside §"The canonical probe bullet"; T7 re-checks both |
| Inherited from the spec (A2/A3): all guard-side facts are **relayed**, verified by the coordinator session rather than by an agent in this loop | A README entry grounded on a second-hand check | `evidence.md`'s Provenance block already says so. T8 re-verifies the load-bearing one by executing the install; anything still unexecuted stays marked researched-but-not-run (AC-1.5), never smoothed into "verified" |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess) — five, including why there is no architecture to decide
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded) — §3 Markdown+JSON, no new tracked code, template contract untouched; §4 negative-case-first; §5 patch bump; §6 degrade-to-silence and nothing installed unasked
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task — AC-1.1…AC-1.6 (T1, T2, T7, T8); NFR-1…NFR-7 (T1, T4, T7, T8)
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies — T1 gates all prose; T6 gates T7; T7 gates T8
- [x] Test strategy covers every Must story
- [x] Line budget respected: Ist 102 / Soll ~300 (excluding HTML comments)
- [x] Status set to `approved` by the user — T5's "Not planned" row confirmed, 2026-09-14

## Deviations (recorded during `/increment`)

- **T2 — guard paragraph runs 5 sentences, not the DoD's stated "at most four."**
  This task's own DoD (T3 row) carries an unconditional cap — "The body of the
  guard paragraph is at most four sentences" — and AC-1.2's text separately caps
  "at most four sentences" for its four named clauses (what it does · optional ·
  nothing installs it for you · exact command). Both are missed by one sentence.
  All four AC-1.2 clauses land within the first 3 sentences; AC-1.3's qualified
  maturity statement (pinned in `evidence.md` T1, two sentences) is a separate
  requirement, and compressing it into fewer sentences was rejected: that is the
  exact flattening risk 1 in plan §5 warns against. Small, obvious correction;
  recorded here per `/increment` rule 4a, not escalated. (Noted at review as F6:
  the original note here cited only AC-1.2's cap, not T2's own — both now named.)
