# Plan: adversarial-gates

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/adversarial-gates/spec.md` (must be `approved`) |
| **Status** | `approved` |
| **Date** | 2026-10-04 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Inc 1 (T1–T9) commits a schema-first corpus at `.spark/adversarial-gates/evidence.md`, forks at T4 on the ≥2 `agent-evaded-gate` threshold, and adds rebuttal tables (≤ 8 lines each) only at qualifying gates. Each table goes at the `SKILL.md` step that the *acting context* of the evasion actually reads. Docs are updated to the true state. Inc 2 (T10–T15, `deferred`) adds one always-on file, `standards/anti-generosity.md`. `/peer-review` and `/demo-day` pass it by a named path, unconditionally. No agent, template or constitution edit.
- **Open:** `0 tasks open` (T1–T5, T8, T9 `done`; T6, T7 `N/A — AC-1.7`). T10–T15 are `deferred`, not open work of this loop. Q1 ruled **A** (Inc 2 runs as a new feature folder); Q2 ruled: reword AC-2.2 later via `/story-time` (2026-10-04).
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** Markdown + JSON only, no runtime, no new tracked executable code (constitution §3). Every effect this feature has is agent-followed. Repo facts checked for this plan:
  - **Stack and layout** are cited from `constitution.md §9` (Stack, Module structure) and not re-derived. **Exception (a):** this feature touches the dispatch steps, so those were read from source.
  - **Dispatch.** `/peer-review` step 2 (`skills/peer-review/SKILL.md:45-57`) and `/demo-day` step 2 (`skills/demo-day/SKILL.md:79-93`) are the only places that invoke `reviewer` and `qa-tester` (grep over `skills/`, 0 other hits; `/spark` invokes neither directly). Both pass *active lens* paths, gated on the constitution, plus a tool path, gated on installation state. Neither dispatches anything unconditionally today.
  - **Agents.** `agents/reviewer.md:87,128` and `agents/qa-tester.md:158,174` know only "lens file" and "tool file". A third kind of path reaches them only through the wording of the delegation prompt, because `agents/` is off-limits (spec §6, AC-2.5).
  - **`not-verified-live` ships nowhere.** It is defined only in this repo's `constitution.md §8` and its trails. It appears in 0 files under `agents/ skills/ templates/ lenses/ docs/` and `README.md`. The QA `Result` vocabulary that ships is `✅ pass / ❌ fail` (`templates/qa-report.md:52`).
  - **Graph parser.** `aspark-graph` normalises a `Result` cell by its marker first: `❌`, then `⚠`, then `✅`. After that it falls back to the regex `\bpass\b` (`~/aSPARK-graph/src/aspark_graph/artifacts.py:417-432`). So a cell reading "partial pass" counts as **pass**, while `⚠ not-verified-live` counts as `unknown`.
  - **Context budget.** `docs/workflow.md:30-43` has no numeric cap (C6 re-checked). NFR-1's cap of ≤ 12 added lines per `SKILL.md` binds, **cumulatively across both increments**.
- **Prompt material can only make these ACs likely, never certain (stated up front, per `CLAUDE.md`):**
  - AC-1.5 ("behaves as before"; runs are nondeterministic, so they are compared by routing and questions, not bytes);
  - AC-1.6 and NFR-8 (an n=1 anecdote);
  - AC-2.1–AC-2.4 (agent behaviour);
  - AC-2.8: both halves, because the skill passing the path is itself instruction-following.

  These are verified by recorded runs, with an **observed rate** where k > 1 (T13, T14), and the docs state that rate.
  **Structurally checkable (`grep`, `wc`, `git diff`):** AC-1.1–1.4, AC-1.7, AC-1.8, AC-2.5, AC-2.7, AC-2.9, AC-4.x, and NFR-1, NFR-3, NFR-6, NFR-7.
- **Decision:**
  1. **Corpus (D1).** One file, `.spark/adversarial-gates/evidence.md`. Its schema, class definitions and search terms are committed **before** the scan (T2), so the threshold cannot be reached by loosening the classification after the fact.
     - Entry fields: `E<n>`, verbatim quote, `file:line`, gate (skill + step), class, acting context (`ceremony session` or `<role> agent`), and a US-2 flag.
     - The scan uses only the session's Grep and Read tools, with no script (§3). It is labelled a search, not a census.
  2. **Threshold unit (D2).** A *gate* is one ceremony's gate step: the gate check or gate close in a named `SKILL.md`. Only `agent-evaded-gate` counts (C10).
  3. **Placement follows the reader (D3).** A row sits in the `SKILL.md` of the gate's ceremony (AC-1.2, AC-1.3), at the step the acting context reads:
     - *Ceremony session* acted: the row goes inline at that gate step.
     - *Role agent* acted (a context that never opens `SKILL.md`): the row goes in the delegation step with one line, "quote these rows verbatim into the agent's prompt". This is the only path that reaches an agent without editing `agents/`. Either way, placement is per `CLAUDE.md` "put a rule in the file the agent actually reads".
  4. **Row shape (D4).** One label line, then a two-column table, at most 8 lines in total:
     - Label line: "Observed rationalizations — in-repo, not field-validated (`${CLAUDE_PLUGIN_ROOT}/.spark/adversarial-gates/evidence.md`)".
     - Columns: `| Excuse | Rebuttal |`, at most 5 rows.
     - Each rebuttal is inline and ends `(E<n>)`.
     - The citation resolves in an installed copy too: `marketplace.json` `source: "./"` ships `.spark/` (constitution §3).
     - Capping Inc 1 at 8 lines leaves 4 for Inc 2's dispatch sentence in `/peer-review` and `/demo-day`, which keeps both inside NFR-1's 12.
  5. **Fork (D5).** If T4 finds zero qualifying gates, T6 and T7 are recorded `N/A — AC-1.7`, the outcome is **refuted-with-finding**, and docs state "no rows shipped". All other tasks run unchanged.
  6. **Docs (D6).** The three docs and what each gets:
     - `README.md`: a `### Gate hardening` subsection under *The loop*, at most 8 lines.
     - `ROADMAP.md`: the #13 entry is split. The shipped part moves to Shipped; the anti-generosity standard stays planned under Next.
     - `docs/status.md`: a Scope/Evidence/State section.
     - `docs/family.md:51-54` stays true ("gates are prompt-enforced") and is left untouched.
  7. **Standard file (D7, Inc 2, decides A4 / AC-2.5).**
     - **Location.** `standards/anti-generosity.md`, at most 40 lines. Frontmatter: `name`, `phases: [review, qa]`, `activation: always`. The file is self-contained: it tells the agent to name it in the verdict as applied (AC-2.8).
     - **Partial results.** It prescribes the exact partial-result cell, `⚠ not-verified-live`, which never contains `✅` or the word "pass". Reason: the parser fact in Context.
     - **Dispatch.** Each of the two skills names the path **literally**, with no constitution read and no flag, and tells the agent to read it in full before writing any verdict.
     - **Templates.** No template edit, so AC-2.7 holds by an empty diff.
  8. **Loop boundary (D8, Q1 ruled A by the user).** This loop builds Inc 1 and closes at T9 (`handed-off`). T10–T15 fix the Inc 2 decisions and their order, so AC-2.5 and AC-2.6 are decided at *this* `/sprint-plan`. **Recommended:** run them as a later feature folder, following the precedent `.spark/campaign-core/plan.md:87`.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Standard in `lenses/` (spec A4 option) | A lens is switched on by the constitution profile (`lenses/README.md:15-27`) and must declare `applies-to`/`triggers`. `/charter` would offer it as declarable. Both contradict C9/AC-2.8 (no opt-in). It would also falsify every "nine lenses" count (README:120, §9). |
  | Standard under `tools/` or `templates/` | `tools/` is installation-state optional (`tools/aspark-graph.md:3`). `templates/` holds instantiated artifact blueprints under the protected contract; a non-instantiated rule file there blurs that boundary. |
  | Standard text inline in both `SKILL.md`s or in the report templates | ~40 lines × 2 breaks NFR-1's 12-line cap and AC-2.5 ("one file"). Templates are protected (AC-2.7). The template is the file the agent reads, which is the strongest argument for it; it stays the fallback if T14's rate is poor, and that fallback would need a spec change. |
  | Standard in a skill's own folder (`skills/peer-review/…`) | Two skills share it. Referencing across skill folders couples them; a copy drifts. |
  | Dispatch by a generic rule ("every `standards/*.md` whose `phases` includes `review`"), like lenses | Speculative: only one standard exists. It adds a listing step that can silently miss, the same failure `lenses/README.md:116-118` warns of. A named path is the most reliable form of an *unconditional* pass. |
  | Rows from every class, or at every gate | Ruled out by C10 and spec §6: imagined rows train skimming (constitution §1, suppression). |
  | Rows always inline at the gate step, regardless of acting context | An evasion inside `reviewer`/`qa-tester` would get a row its context never loads, and nobody would notice. That is the `campaign-core` F24/B15 lesson. |
  | A corpus scanner script, untracked | Allowed by §3, but ~50 files is a reading job. Grep/Read with the search terms recorded is reproducible enough, and leaves nothing to explain. |
  | Build both increments in this loop | C8: two PRs, two bumps, Inc 2 only after Inc 1 ships. One folder cannot hold two `review.md`/`qa.md` rounds for two releases without muddying the phase map. |
- **Consequences:**
  - **Easier:** a future rebuttal row is a cited corpus entry plus at most 1 line. Corpus quality is checkable entry by entry from `file:line`. A second standard is one file plus one dispatch line per skill.
  - **Harder:** rows reach a role agent only if the skill quotes them into the prompt. The standard depends on the delegation prompt's wording, because no agent knows "standard files".
  - **Inc 2 effects.** `standards/` is a **new directory pattern**, always on and passed by name, which is unlike the optional-capability directories in §3. It is recorded here as an architecture decision and needs no amendment (§3 "new concern = new file" is honoured; AC-2.5). Constitution §9 *Module structure* goes stale (it already omits `campaigns/`). That is `/charter`'s job, flagged and not done here.

## 2. Affected Components

- **New, Inc 1:** `.spark/adversarial-gates/evidence.md`.
- **Edited, Inc 1:**
  - `skills/<s>/SKILL.md`, only for gates that qualify at T4. Which skills is unknowable at plan time, so T6 carries no `files:` note (rule 4).
  - `README.md`, `ROADMAP.md`, `docs/status.md`.
- **New, Inc 2:** `standards/anti-generosity.md`.
- **Edited, Inc 2:** `skills/peer-review/SKILL.md`, `skills/demo-day/SKILL.md`, `README.md`, `ROADMAP.md`, `docs/status.md`, `docs/repo-layout.md`, `CONTRIBUTING.md`.
- **Deliberately untouched (both increments):**
  - `agents/`, `templates/` (all six; AC-2.7 by empty diff), `lenses/`, `.spark/constitution.md`;
  - `docs/family.md` (still true);
  - `.claude-plugin/plugin.json`: the minor bump is the Release Manager's at `/go-live`, once per increment (NFR-4).
- **New dependencies / services:** none.
- **New patterns, each justified:**
  - (a) `standards/` as an always-on directory, passed by literal path (D7).
  - (b) Rebuttal rows quoted into a delegation prompt when the acting context is an agent (D3).
- **Fixtures:** scratch repos outside this repo, with their full text quoted in `evidence.md`. Nothing executable is tracked.
- **Blast radius (graph not queried; scoped by hand).** Every path in the `files:` notes is Markdown. The graph indexes only source extensions (`tools/aspark-graph.md:93-95`), so `impact` is empty *by construction* here. The identical query for `campaign-core` returned every path under `unknown_files` (`.spark/campaign-core/plan.md:83`). Scope comes from the reads in §1 Context. An empty answer would mean "not indexed", never "nothing at risk".

## 3. Task Breakdown

**Scope of this loop:** T1–T9 (Inc 1, one PR, one minor bump). **The loop closes at T9.** `deferred` rows are not worked by `/increment` here, and a `/spark` resume must not route to them (Q1). A *dry run* is a performed step: a real Claude Code session (`claude --plugin-dir <path>`, headless or interactive), with its prompt and output quoted verbatim in `evidence.md`. Reasoning about what a file would make an agent do closes nothing. "Base" means a git worktree of `origin/main` at the SHA recorded in T1.

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | **Inc 1.** Walking skeleton: fresh branch, run harness, baselines | US-1 | AC-1.5, NFR-6 | – | `done` | `feat/adversarial-gates` is cut from `origin/main` (not from `docs/campaign-core-released`), and spec + plan are committed on it as the first commit. `evidence.md` records:<br>• the base SHA;<br>• `claude plugin validate .` passing, output quoted;<br>• `git ls-files '*.py'` empty;<br>• `wc -l skills/*/SKILL.md`;<br>• one headless `claude -p --plugin-dir <base worktree>` session in a scratch repo, completing `/next-steps` with its output quoted, which proves the dry-run harness works end to end before any content exists — files: .spark/adversarial-gates/evidence.md |
| T2 | **Inc 1.** Corpus method, written before scanning | US-1 | AC-1.1, AC-1.8 | T1 | `done` | `evidence.md` §Method holds:<br>• the scope, as the `ls .spark/*/{review,qa,evidence}.md` list with its count;<br>• the search terms;<br>• the D1 entry schema;<br>• a decision rule for each of `agent-evaded-gate` / `verdict-rounded-up` / `other`, with one boundary example each;<br>• the D2 gate unit;<br>• "a search, not a census".<br>Committed in its own commit, before any entry exists (`git log` shows the order) — files: .spark/adversarial-gates/evidence.md |
| T3 | **Inc 1.** Corpus scan and counts | US-1 | AC-1.1, AC-1.8, NFR-9 | T2 | `done` | Every in-scope file was searched with T2's terms. Each entry has all D1 fields, and its quote matches the cited `file:line` verbatim (checkable by opening it). A count table gives entries per class and per gate. Every `verdict-rounded-up` entry is flagged "input for US-2 (Inc 2)". Quotes come only from `.spark/` and hold no customer material — files: .spark/adversarial-gates/evidence.md |
| T4 | **Inc 1.** Qualification ruling (the D5 fork) | US-1 | AC-1.2, AC-1.7 | T3 | `done` | `evidence.md` lists each gate with ≥ 2 `agent-evaded-gate` entries, with the cited `E<n>` and their acting contexts, and its D3 placement (inline vs delegation step). With zero qualifying gates, it records **refuted-with-finding** per `CLAUDE.md`, and T6/T7 become `N/A — AC-1.7` in this table. Either way, it names the uncovered ceremony T5 will run — files: .spark/adversarial-gates/evidence.md |
| T5 | **Inc 1.** Negative baseline, before any `SKILL.md` edit | US-1 | AC-1.5 | T4 | `done` | One dry run of an uncovered ceremony (recommended: `/next-steps` on a scratch mid-loop feature) against the base worktree. The transcript is quoted verbatim, and `git diff --stat origin/main -- skills` is empty at that moment — files: .spark/adversarial-gates/evidence.md |
| T6 | **Inc 1.** Rebuttal tables at qualifying gates only | US-1 | AC-1.3, AC-1.4, NFR-1, NFR-3 | T5 | `N/A — AC-1.7` | For each T4 gate, a D4 block placed per D3:<br>• at most 5 `Excuse \| Rebuttal` rows, with the rebuttal inline;<br>• each row ends `(E<n>)` pointing at a T3 entry of class `agent-evaded-gate` for that gate;<br>• the label reads "in-repo, not field-validated".<br>`git diff --numstat` shows ≤ 8 added lines per touched `SKILL.md`. No frontmatter, command name or other step changes. `N/A — AC-1.7` if T4 found none |
| T7 | **Inc 1.** Replay, n=1 | US-1 | AC-1.6, NFR-8 | T6 | `N/A — AC-1.7` | One T4 entry is replayed. The scratch fixture reproduces its preconditions and is quoted in full. Two fresh headless sessions, base worktree vs branch, get identical prompts. Both outcomes are quoted verbatim and labelled "n=1 anecdote, not proof". If the base run does not evade, that is recorded as "not reproduced", never as "row works". `N/A — AC-1.7` if T4 found none — files: .spark/adversarial-gates/evidence.md |
| T8 | **Inc 1.** Docs to the true Inc 1 state | US-4 | AC-4.1, AC-4.2, AC-4.3, AC-4.4, AC-4.5, NFR-2, NFR-5, NFR-8 | T4, T7 | `done` | **README** (D6, ≤ 8 lines), **ROADMAP** #13 and **docs/status.md** each state:<br>• rows at N gates, naming them, or "none, refuted-with-finding";<br>• grounding is in-repo trails, not field reports;<br>• effectiveness is unmeasured, and whether a row fires cannot be tested in Core;<br>• gates stay prompt-enforced, and code enforcement is `aspark-guard`'s;<br>• where rows apply and where they stay silent.<br>The anti-generosity standard is listed as planned only. Dual review appears, if at all, only as "not built", with spec §6's re-open condition. `grep -n -i "anti-generosity"` over the three docs shows no shipped/active wording — files: README.md, ROADMAP.md, docs/status.md |
| T9 | **Inc 1.** Negative re-run and audits. **Last task of this loop** | US-1 | AC-1.2, AC-1.5, NFR-1, NFR-3, NFR-4, NFR-6, NFR-7 | T6, T8 | `done` | T5 is re-run on the branch and compared by routing and questions asked: no difference, and no mention of rebuttals. Observed:<br>• `git diff --stat origin/main` lists only §2 Inc 1 paths;<br>• every skill outside T4's list has an empty diff;<br>• `git diff origin/main -- agents templates lenses .spark/constitution.md` is empty;<br>• no slash command, frontmatter `name` or ID changed;<br>• `claude plugin validate .` passes;<br>• `git ls-files '*.py'` is empty.<br>All outputs quoted — files: .spark/adversarial-gates/evidence.md |
| T10 | **Inc 2.** Gate check and negative baseline | US-2 | AC-2.6, NFR-2 | T9 | `deferred` | Gate: Inc 1 is `handed-off`/`released`, and a fresh branch is cut from `origin/main`; otherwise stop. Before any Inc 2 edit:<br>• `grep -rn "anti-generosity\|standards/" skills agents` is empty;<br>• one non-review ceremony (`/sprint-plan` on a scratch spec) is recorded, to be re-run in T15 (NFR-2 silence) |
| T11 | **Inc 2.** The standard file | US-2 | AC-2.1, AC-2.2, AC-2.3, AC-2.4, AC-2.5, AC-2.9 | T10 | `deferred` | `wc -l` ≤ 40, with D7 frontmatter. The file:<br>• names the agent's tendency toward generosity;<br>• gives an exact banned-phrase list;<br>• makes every rubric item PASS/FAIL with its deciding observable, and bans "mostly"/"partially";<br>• requires a partial check to be written exactly `⚠ not-verified-live`;<br>• requires the report to state the evaluation mode available and that a static-only result is degraded;<br>• bans withdrawing or downgrading a finding without a recorded, cited reason, and gives effort no credit;<br>• requires the verdict to name the standard as applied;<br>• limits its scope to review/QA verdicts, and never sets `approved` or waives.<br>Each corpus-derived element cites `E<n>`; every other element reads "not grounded in the corpus" — files: standards/anti-generosity.md |
| T12 | **Inc 2.** Unconditional dispatch in both claimed phases | US-2 | AC-2.5, AC-2.8, NFR-1, NFR-3 | T11 | `deferred` | Step 2 of each skill gains at most 4 lines. They pass `${CLAUDE_PLUGIN_ROOT}/standards/anti-generosity.md` by literal path, with no constitution read and no flag, and tell the agent to read it in full before writing any verdict. The step that presents the report says: if the report does not name the standard as applied, tell the user. Cumulative `git diff --numstat` against the pre-Inc 1 base is ≤ 12 per file, T6's lines included — files: skills/peer-review/SKILL.md, skills/demo-day/SKILL.md |
| T13 | **Inc 2.** Dispatch and activation proof, per claimed phase | US-2 | AC-2.5, AC-2.6, AC-2.7, AC-2.8 | T12 | `deferred` | A table covers `review` and `qa` (a column each).<br>**Activation:** `grep -rn "standards/"` over `skills agents templates lenses` hits only the two T12 lines, so `/charter`, the facilitator, `templates/constitution.md` and `lenses/README.md` neither declare nor gate the standard.<br>**Dispatch:** real `/peer-review` and `/demo-day` runs on a scratch feature, 3 in a repo with no constitution and 3 with a constitution that has no related setting, so k=6 per skill. The observed rate of "the report names the standard" is recorded.<br>`git diff -- agents templates .spark/constitution.md` is empty — files: .spark/adversarial-gates/evidence.md |
| T14 | **Inc 2.** Verdict-behaviour dry runs | US-2 | AC-2.1, AC-2.2, AC-2.3, AC-2.4 | T13 | `deferred` | A planted fixture has one partial check, one static-only check, one real finding and a "good effort" temptation. Each skill runs k=3 on it. The rate of each is recorded: no banned phrase; the partial check written exactly `⚠ not-verified-live`; the evaluation mode stated; the finding not withdrawn. The result is labelled "likely, not certain" — files: .spark/adversarial-gates/evidence.md |
| T15 | **Inc 2.** Docs, negative re-run, audits | US-4 | AC-4.6, AC-4.1, AC-4.3, NFR-2, NFR-4, NFR-5, NFR-6, NFR-7 | T14 | `deferred` | The README says the standard is always active in every `/peer-review` and `/demo-day` run, is stricter for already-installed projects (partial checks become `⚠ not-verified-live`), is unmeasured, and gives T13/T14's rates. The same docs give its degraded mode, ROADMAP #13 moves to match, and repo-layout and CONTRIBUTING name `standards/`. Inc 1 claims are re-read as still true. T10's run is re-run with no mention of the standard. `validate` passes; `*.py` is empty — files: README.md, ROADMAP.md, docs/status.md, docs/repo-layout.md, CONTRIBUTING.md |

## 4. Test Strategy

Prompt material has no test suite (constitution §4).
- **Unit analogue:** structural checks run as real commands, with output quoted: `grep`, `wc -l`, `git diff --stat/--numstat`, quote-vs-`file:line` matching, and `claude plugin validate .`.
- **Integration analogue:** dry runs in real sessions on scratch fixtures, **negative case first** in each increment (T5 before T6; T10 before T11).
- **`/demo-day`** follows §8's substitute method (hands-on against the installed plugin, not a browser). It re-performs T9's negative re-run and T7's replay, or T4's refuted-with-finding check. Any row it cannot perform is recorded `⚠ not-verified-live`, never passed by reading.

- **US-1 (Must).**
  - *Structural:* AC-1.1 and AC-1.8 (T2/T3), AC-1.2 (T9 empty diffs), AC-1.3 and AC-1.4 (T6: every row cites an `agent-evaded-gate` entry), AC-1.7 (T4).
  - *Live:* AC-1.5 (T5 → T9) and AC-1.6 (T7, n=1, likely-only).
  - *Corpus classification:* `/peer-review` must **re-derive** every entry counted toward a threshold from its `file:line`, under reviewer condition (b), because it decides a Must AC. It cannot cite T3's word for it.
- **US-4 (Must).** All ACs are structural reads of the docs at branch head (T8, T9), re-read at the PR head by `/go-live`'s pre-flight (AC-4.5). AC-4.6 is checked in Inc 2 (T15).
- **US-2 (Should, Inc 2).**
  - *Structural:* AC-2.5, AC-2.7 and AC-2.9 (T11–T13).
  - *Live with an observed rate:* AC-2.1–2.4 (T14) and AC-2.8 (T13).
  - *Dispatch and activation* are proven for **both** claimed phases (`CLAUDE.md`, accessibility-lens lesson).
- **Instruction-only, never claimed as enforced:** a row firing (NFR-8), the skill quoting rows into a prompt (D3), the agent applying the standard, and the report naming it.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| R1: A2, too few `agent-evaded-gate` entries (most grep hits are verdict corrections) | No table ships | D5 fork at T4. Refuted-with-finding is a valid outcome. Docs say so (AC-1.7) |
| R2: The classifying agent rounds a borderline case up to reach ≥ 2: the exact failure this feature names | Rows built on weak evidence | Rules committed before the scan (T2, own commit). `/peer-review` re-derives every counted entry (§4) |
| R3: The evasion happened inside a role agent, which never reads `SKILL.md` | A row nobody's context loads | D3 delegation-step placement. T7 replays at the real acting context. Disclosed as instruction-only |
| R4: The replay does not reproduce the original evasion | Nothing learned | Recorded verbatim as "not reproduced". No effectiveness claim either way (NFR-8) |
| R5: NFR-1's 12 lines are shared by Inc 1 tables and Inc 2 dispatch in `/peer-review` and `/demo-day` | Cap overrun in Inc 2 | Inc 1 capped at 8 per skill (D4), Inc 2 at 4 (T12). T12 measures cumulatively |
| R6: Spec text: AC-2.2 calls `not-verified-live` an "existing" status, but it exists only in this repo's constitution §8, not in the shipped vocabulary. A free-text partial cell can parse as `pass` (`artifacts.py:428`) | Consumers get an undefined value. The graph overstates a partial check | D7 defines the exact cell `⚠ not-verified-live` inside the standard itself. **Q2** routes the wording to the PO |
| R7: The always-active standard makes verdicts stricter for installed consumers | A surprise change of behaviour | Own minor bump plus README statement (AC-4.6, NFR-4). The standard never blocks on anything but its own rules |
| R8: Branch staleness. Work currently sits on `docs/campaign-core-released`, with `.spark/adversarial-gates/` untracked | A surprise merge at `/go-live` | T1 cuts `feat/adversarial-gates` from `origin/main` and commits spec + plan first (`CLAUDE.md`) |
| R9: An untracked `.spark/.guard/` is present in the working tree, and `source: "./"` ships it | Unvetted content reaches consumers (constitution §6) | Out of this feature's diff. Flagged for `/go-live`'s presence check, never assumed safe |
| R10: Dry runs are nondeterministic and cost tokens | Flaky evidence | Small fixtures. Compare by routing and questions. Rates, not single runs, where k > 1 |

**Questions for the user (neither blocks T1–T9; both should be ruled before approval):**
1. **Q1, Inc 2 venue:**
   - **A** (recommended, as in campaign-core R10-Q1): this loop closes at T9, and Inc 2 runs as a new feature folder carrying US-2 with its existing IDs and re-cutting T10–T15.
   - **B:** Inc 2 runs later in *this* folder, so `review.md`/`qa.md` get a second release cycle's rounds.
2. **Q2, spec wording (to the PO, not changed here):** AC-2.2's "existing `not-verified-live` status" is true only for aSPARK's own constitution. Should the spec say "defined by the standard"? The plan does not depend on the answer: D7 defines it either way.

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded). No executable code. No agent, template or constitution edit. `standards/` is recorded as a new pattern (D7). Optional-tool rules are untouched
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task (NFR-10 N/A per spec)
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Line budget respected: Ist 173 / Soll ~300 (excluding HTML comments; the plan has none). Self-reported, no linter checks this
- [x] Status set to `approved` by the user

## Deviations

- **T8 / DoD wording.** The DoD asks that "the anti-generosity standard is listed as planned". The ROADMAP entry for #13 is retitled "Stricter verdict rules for review and QA" and the docs describe the planned standard under that name, so `grep -i "anti-generosity"` over the three docs is empty. It is planned, not shipped; the plain-language name keeps the docs readable. No scope change.
- **T3 / terms.** The Method's terms were not edited. One extra sweep (`| Blocker |` rows) was added at T3 to catch acts the terms miss; it is recorded in `evidence.md` and found E2 and E7. It does not change any class decision.
- **Plan row status `N/A — AC-1.7`** for T6 and T7 follows D5 (zero qualifying gates).
