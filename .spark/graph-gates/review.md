# Review Report: graph-gates

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Uncommitted working-tree diff against `HEAD` (`fb6af66`), `.spark/graph-gates/plan.md` (revision 2) |
| **Status** | `passed` |
| **Date** | 2026-07-26 (round 3; round 2 same day, `changes-requested`; round 1 was 2026-07-25, `changes-requested`) |

> **How to read this report.** Sections 1–6 and the first REVIEW GATE are **round
> 1**, written at T4 of 16 against a partial increment, and are kept unedited as
> the record. The authoritative outcome is **§7 Round 2** at the end — written
> 2026-07-26 against the complete increment — which verifies every round-1
> finding, judges the twelve tasks built since, and carries the binding verdict
> and gate. **§8 Round 3** verifies the fix pass that answered §7 and carries the
> binding ruling; the **binding** REVIEW GATE checklist sits between §7 and §8 and
> was re-ruled in place at round 3, showing both states (the earlier checklist
> under §6 is round 1's, kept as record). §7 supersedes §1–§6 and the
> round-1 gate wherever they differ; §8 supersedes §7 wherever they differ.

## 1. Scope

**Reviewed.** The working-tree diff against `fb6af66`:

| File | What changed |
|---|---|
| `templates/plan.md` | +21 lines, entirely inside the HTML comment above the task table (T2) |
| `agents/engineering-manager.md` | +21 lines inside step 4's bullet list (T2) |
| `tools/aspark-graph.md` | new, untracked, 131 lines (T3) |
| `skills/peer-review/SKILL.md` | +10 lines: a sub-bullet in step 1, a conditional clause in step 2 (T4) |
| `agents/reviewer.md` | +11 lines inside `## How You Work` step 2 (T4) |

Also read as context: `.spark/graph-gates/spec.md`, `plan.md`, `evidence.md`,
`.spark/constitution.md`, `lenses/library.md` (the one active lens), and — read-only,
nothing written — `~/aSPARK-graph/src/aspark_graph/{artifacts,queries,cli,server,model}.py`
and `extractors/base.py`, to check the plan's cross-repo line-number claims and the
external contract this feature hardcodes.

**Deliberately not reviewed as defects.** This is a partial increment: T1–T4 are
built, T6–T15 are unstarted. `tools/README.md` (T8), the `/sprint-plan` and
`/demo-day` wiring (T6, T7), the `README.md` entry (T9), the conformance sweep and
the `0.4.0` version bump (T10) are absent because their tasks have not run. They
are named where relevant and filed as nothing. `.claude-plugin/plugin.json` still
reads `0.3.1`; that is T10's job, not a finding. Untracked noise unrelated to the
feature (`docs/*.docx*`, `.aspark-graph/`, `.spark/BACKLOG.md`) is out of scope.

**One property of this run, recorded because T5 depends on it.** This
`/peer-review` executed the **installed 0.3.1 plugin cache**, not the working
tree: `~/.claude/plugins/cache/aspark/aspark/0.3.1/` has no `tools/` directory,
its `skills/peer-review/SKILL.md` contains zero occurrences of `aspark-graph`, and
its `agents/reviewer.md` has no tool paragraph. No probe ran, no tool file was
passed to me, and this report mentions the tool only because the diff under review
*is* the tool wiring (deviation D3's reading). See F3.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | `evidence.md` holds the base SHA, the 0-hit grep, the three pre-change step lists, the artifact headings, the protected header row, and the AC-1.1 reading quoted verbatim. The self-correction about `.aspark-graph/` being present after all is exactly the honesty bar the constitution §1 asks for |
| T2 | ✅ | The five rules and the rationale paragraph are **word-identical** in `templates/plan.md:34–51` and `agents/engineering-manager.md:66–85` (diffed; only the lead-in clause differs, and it carries the same meaning). AC-5.3 verified byte-level: heading `Task Breakdown`, header row, both `T1`/`T2` example rows unchanged. One factual defect in the shared rationale — F5 |
| T3 | ⚠️ | 131 lines (≤ 150 ✓). Every call form, return shape, failure mode, confidence tier and extension list I checked against the consumer's source is **accurate**. Two DoD items are not delivered: the per-query soundness trace (F7) and `story_trace`'s return shape (F8). The frontmatter still carried D2's *uncorrected* predicate (F6, fixed) |
| T4 | ⚠️ | Wired as designed — no new numbered step (5 before, 5 after), path handed over alongside the lens paths, agent paragraph product-free. But the skill collapses the approved four availability states into two (F1), and its MCP matcher was literal where the plan requires suffix matching (F2, fixed). **Status in `plan.md` still reads `todo`** although the work is in the tree (F9) |
| T5 | ⚠️ | In flight — this report. As executed it does not exercise the changed material (F3) |
| T6–T15 | – | `todo`, not started, correctly reflected in the table |

**Deviations D1–D3** (`plan.md:347–349`) are each justified and each verifiably
matches the tree: D1 — the probe is stated inline and the concrete path
`tools/aspark-graph.md` is passed (`SKILL.md:24–32`, `:40–42`); D2 — the predicate
is `test -f .aspark-graph/graph.json` (`SKILL.md:29`, `tools/aspark-graph.md:23`),
and I confirmed the reason in the consumer's source: `queries.load_graph`
(`~/aSPARK-graph/src/aspark_graph/queries.py:24–31`) raises `GraphNotBuiltError`
on the *file*, not the directory; D3 — this report's mentions of the tool are all
about the diff under review. **A fourth deviation is present but unrecorded** — see
F1.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `skills/peer-review/SKILL.md:24–32` | The approved design (`plan.md` §1 sub-decision 2, user-confirmed as P-Q3) resolves **four** mutually exclusive states, two of which emit exactly one hint sentence. The skill resolves **two**: `Available → pass the tool file … Not available → say nothing at all`. The tool file's state table (`tools/aspark-graph.md:33–38`) is only ever in an agent's context in the `yes/yes` state, so the two hint sentences can never fire. **Why it matters:** AC-2.3 is a Must criterion ("*given the CLI is present but the repo has no built graph … it states this once per ceremony run*") and is unreachable in the only wired ceremony; the fourth state exists precisely because the sole known beneficiary's CLI lives in a venv and is not on `PATH` (`plan.md` §1 fact 1), so that operator now gets silence instead of the one sentence that would tell them what to fix. It fails *toward* silence, so US-1 is not endangered — that is why it is Major and not a Blocker. **Fix:** give the bullet three outcomes — `graph.json` **and** a surface → pass the tool file; surface but no `graph.json` → say once, in one sentence, that the graph is not built and name `aspark-graph build .` without running it; `graph.json` but no surface → say once that graph data exists but no runner is reachable. Neither ever repeats, neither touches a gate. Record it as a deviation if the collapse is intended, and narrow AC-2.3's coverage in `plan.md` accordingly | open |
| F2 | Major | `skills/peer-review/SKILL.md:25` | The MCP branch read `MCP tools named \`staleness\` and \`impact\``. Claude Code exposes MCP tools namespaced as `mcp__<server>__<tool>`, and `plan.md` §1 sub-decision 1 specifies matching on *names that end in* `__staleness`/`__impact`; `tools/aspark-graph.md:20` says "(possibly namespaced)". A literal-name check never matches, so MCP-first is dead in practice, every run falls through to the CLI probe (violating the design's "run no command" for the MCP surface), and for the one operator whose CLI is not on `PATH` the offer never fires at all. **Fixed:** now matches names *ending in* `staleness`/`impact` with the namespaced form given as an example, and "use them" is disambiguated to "treat that as the available surface". T8's canonical wording must be taken from the corrected text | fixed |
| F3 | Major | `.spark/graph-gates/plan.md:220` (T5's DoD) | T5 requires that "exactly one detection probe ran and produced no user-visible output". In this run **no probe ran and none could**: the active plugin is the published `0.3.1` cache, which contains none of the changed files (verified — the cached `skills/peer-review/SKILL.md` has 0 occurrences of `aspark-graph` and there is no `tools/` directory). **Why it matters:** the negative case is the constitution §1 non-negotiable and this feature's dominant risk R2. Evidence gathered from an unmodified plugin proves the *old* material is silent, which was never in doubt; it says nothing about the new material. Checking T5 off on this run would record a proof that was not performed. **Fix:** re-run the negative case against the working-tree material — install/point the plugin at `/Users/andreaslottes/aSPARK` (or execute the modified `SKILL.md` steps explicitly) — and state in `evidence.md` which build was exercised. If that is impossible, record T5 as *not proven* and label it, rather than as passed | open |
| F4 | Minor | `skills/peer-review/SKILL.md:29` | The probe `command -v aspark-graph && test -f .aspark-graph/graph.json` **exits non-zero in the normal (absent) case**, so the ceremony's gate step ends with a visibly failed shell command. The adjacent instruction says "say nothing at all", but R1's whole premise is that instructions are convention, not enforcement — and a red tool result is the single most likely thing an agent volunteers a sentence about. That sentence would be the R2 regression. **Fix:** make the probe always succeed and self-describe, e.g. `command -v aspark-graph >/dev/null 2>&1 && test -f .aspark-graph/graph.json && echo tool=available \|\| echo tool=absent`. Also worth noting in `evidence.md`: under fine-grained permission settings the probe may raise a **permission prompt naming `aspark-graph`** in projects that have never heard of it. P-Q1 excludes detection tool-calls from the AC-1.1 grep, so this is inside the accepted reading — but it is user-visible, and the negative-case record should say whether it happened | open |
| F5 | Minor | `agents/engineering-manager.md:80–85` and `templates/plan.md:46–51` (identical text) | The rationale "*a trailing period **or a second keyword** yields no error and no link*" is **factually wrong for the second keyword**. I ran the consumer's real parser: `_files_note('files: src/a.py — more files: src/b.py')` → `['src/a.py', '—', 'more', 'files:', 'src/b.py']` — both paths resolve and both links are built, because `_files_note` (`~/aSPARK-graph/src/aspark_graph/artifacts.py:351`) splits the greedy capture on `[,\s]+`, not just on commas. The trailing-period case *is* real (`'…, src/b.py.'` → `'src/b.py.'` → dropped by the `has_node` guard at `artifacts.py:189`), and so is punctuation abutting a path mid-cell (`'src/a.py;'` → dropped). **Why it matters:** this block's persuasive weight is the sentence "Rules 2–4 are not style"; an EM who checks the claim finds a third of it untrue and has no reason to trust the rest. **Fix (apply identically in both files — AC-5.4):** attribute the failure to what actually causes it — punctuation attached to a path, and prose that runs on past the last path — and justify rule 3 on its own honest ground: only the *first* `files:` in a cell is anchored, so everything after it is swallowed wholesale and what gets parsed stops being predictable | open |
| F6 | Minor | `tools/aspark-graph.md:5` | The frontmatter `detect:` shorthand still read `cli aspark-graph + .aspark-graph/` — the pre-D2 predicate that the body of the same file (`:23–27`) explicitly warns against, since a `.aspark-graph/` directory can hold only a parse cache. This repo is the live proof: it contains exactly such an orphaned directory (`evidence.md:165–174`). Two predicates in one file is the drift D2 was raised to remove. **Fixed:** the shorthand now reads `.aspark-graph/graph.json` | fixed |
| F7 | Minor | `tools/aspark-graph.md:44–58` | T3's DoD requires that each wired query "is traced to inputs name-identical in a Core-managed and a template-named trail (`spec.md`, `plan.md`, source, mtimes)" — this is AC-4.4's audit trail and the *reason* these three queries are sound while the two deferred ones are not. The `## Calls` table gives call form and return shape but no input trace; the `Not wired` block (`:129–131`) states the filename mismatch without connecting it to why the wired three are unaffected. A maintainer reopening the deferral (AC-4.3) cannot check the boundary. **Fix:** one sentence under `## Calls` — "All three read only `spec.md`, `plan.md`, source files and file mtimes, whose names are identical in an aSPARK-managed trail and a template-named one; that is why the filename mismatch below does not touch them." | open |
| F8 | Minor | `tools/aspark-graph.md:53` and `:113–115` | NFR-3 requires every instructed query to be documented with its return shape. `staleness` and `impact` are (`:50–51`); `story_trace` gets only the prose "story → ACs → tasks → code". Two consequences: an agent cannot recognise the QA leg it is told not to read, because the keys are never named — they are `acceptance_criteria[].qa_checks` and `acceptance_criteria[].latest_result` (`~/aSPARK-graph/src/aspark_graph/queries.py:88–92`) — which weakens AC-4.2 from a rule to a hint; and its distinct failure mode `{"found": false, "reason": "ambiguous", "candidates": [...]}` for a bare `US-n` (`queries.py:65`) is undocumented, so an agent hitting it has no instruction beyond the generic empty-result rule. **Fix:** name the top-level keys (`found`, `story`, `acceptance_criteria[]`, `tasks[]`), name the two QA-leg keys in the QA slice's "do not read it" sentence, and add `ambiguous` to the failure line — the fix costs about four lines against a 19-line budget | open |
| F9 | Minor | `.spark/graph-gates/plan.md:219` | T4's `Status` is `` `todo` `` while its output (`skills/peer-review/SKILL.md`, `agents/reviewer.md`) is in the working tree and deviation D1 is already recorded *against T4*. `/increment`'s stated contract is that it "keeps `Status` current" (`plan.md:204`, `:206`), and `/peer-review`'s own gate reads that column. A reader cannot distinguish "T4 built" from "T4 not started". **Fix:** set T4 to `done` (T5 to `in-progress` if the column admits it) | open |

## 4. Requirements Traceability

Scoped to what T1–T4 claim to deliver. ACs owned by unstarted tasks are marked `–`.

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `skills/peer-review/SKILL.md:30–32`, `agents/reviewer.md:103` | ✅ met *in the diff* — grep over `skills/ agents/ templates/ lenses/ README.md` finds `aspark-graph` in exactly one file (the peer-review skill, per D1) and nowhere in any agent or template; the absent branch says "say nothing at all" and the agent branch says "if no tool file was passed, work as you always do". **Not proven by a run** — F3 |
| AC-1.2 | `skills/peer-review/SKILL.md`, `templates/review-report.md` (untouched) | ✅ met — 5 numbered steps before and after (matches `evidence.md:77–85`); the probe is a sub-bullet of step 1; the reviewer's own steps stay 1–6; no report section added, renamed or dropped |
| AC-1.3 | `skills/peer-review/SKILL.md:31–32` | ✅ met — "never probe in a run that already stopped, and never let the outcome change a gate"; the REVIEW GATE checklist is untouched and no gate item references the tool |
| AC-1.4 | `.spark/graph-gates/evidence.md:31–184` | ⚠️ partial — the baseline is recorded and dated *before* the first edit, and no positive-case run has happened. The negative-case entry itself is still owed, and F3 constrains what it may claim |
| AC-1.5 | — | ✅ met by construction — nothing in the diff asks a target project for a file, a flag or a `CLAUDE.md` block; activation is installation state only |
| AC-2.1 | `skills/peer-review/SKILL.md:24`, `:40–42` | ✅ met — availability is resolved inside the existing step 1, and `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` is handed over exactly like a lens path; no new ceremony, no new agent |
| AC-2.2 | `tools/aspark-graph.md:20–23`, `skills/peer-review/SKILL.md:25–30` | ✅ met after F2's fix — MCP first, CLI second, documented in both places and now matching the namespaced form the plan specifies |
| AC-2.3 | `tools/aspark-graph.md:36` only | ❌ missing in the wired path — the sentence exists in the tool file but the tool file is never delivered in the state that triggers it (F1) |
| AC-2.5 | `agents/reviewer.md:97–98`, `tools/aspark-graph.md:102–103` | ✅ met — the report must name which results scoped the reading and which locations were read as a consequence |
| AC-3.1 | `agents/reviewer.md:100–103`, `tools/aspark-graph.md:103–105` | ✅ met — "a finding that restates a tool's output without a concrete `file:line` and the code behind it is not a finding" |
| AC-3.2 | `tools/aspark-graph.md:64–66` | ✅ met — stale ⇒ say once, treat as absent, cite nothing, fall back, still reach the verdict |
| AC-3.3 | `tools/aspark-graph.md:67–69` | ✅ met — empty ≠ nothing there; one line that scoping was done by hand, then the ordinary method |
| AC-3.6 | `tools/aspark-graph.md:62–63`, `:93–94`, `:103–105`, `:117–118`; `agents/reviewer.md:100–101` | ✅ met — every slice and the agent paragraph each say it in their own words |
| AC-4.1 | `tools/aspark-graph.md:122–126` | ✅ met — `gate_health` occurs exactly once in the whole shipped tree, inside the deferral block, ending "**Do not call it.**"; 0 hits under `skills/` and `agents/` |
| AC-4.2 | `tools/aspark-graph.md:113–115` | ⚠️ partial — the QA leg is declared not-to-be-read and its emptiness declared not a finding, but the keys it lives in are never named (F8) |
| AC-4.3 | `tools/aspark-graph.md:120–131` | ✅ met — both deferrals listed with the reopen condition stated concretely (the `review-report.md`/`qa-report.md`/`release-notes.md` vs `review.md`/`qa.md`/`release.md` mismatch) |
| AC-4.4 | `tools/aspark-graph.md:44–58` | ⚠️ partial — the *property* holds (I traced all three: `staleness` = mtimes, `impact` = source + `plan.md` notes, `story_trace` = `spec.md` + `plan.md` + source), but the trace is not written down as T3's DoD requires (F7) |
| AC-4.5 | `tools/aspark-graph.md:72–75` | ✅ met — empty by construction, "*the plan declared no links*", "never report it as reassurance"; reinforced at `:89–91` |
| AC-5.1 | `templates/plan.md:34–51`, `agents/engineering-manager.md:66–85` | ✅ met — and dogfooded: all 15 DoD cells of this feature's own plan parse clean (keyword once, note last, no trailing punctuation) |
| AC-5.2 | `templates/plan.md:44–45`, `agents/engineering-manager.md:77–78` | ✅ met — "omit … never guess", with the downstream reason given |
| AC-5.3 | `git diff templates/plan.md` | ✅ met — verified byte-level against `HEAD`: `## 3. Task Breakdown`, the header row `\| # \| Task \| Story \| Covers (AC / NFR) \| Depends on \| Status \| Definition of Done \|` and the `T1`/`T2` example rows are unchanged; the only diff is inside the HTML comment |
| AC-6.3 | `agents/reviewer.md:94–103` | ✅ met — the paragraph names no product and no query; it says "whatever tool file the caller passed", and the product name appears in no agent file at all |
| NFR-1 | `templates/plan.md` | ✅ met (structure). The `0.4.0` bump is T10, unstarted |
| NFR-2 | `skills/`, `agents/`, `tools/` | ✅ met — 10 skills, 7 agents (unchanged); the only new public surface is `tools/`, referenced solely as `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md`. `claude plugin validate` passes (one pre-existing, unrelated `autoUpdate` warning in `marketplace.json`, present at `HEAD`) |
| NFR-3 | `tools/aspark-graph.md:44–58` | ⚠️ partial — `staleness` and `impact` fully documented and **verified accurate** against the consumer's `cli.py`/`server.py`/`queries.py`; `story_trace`'s shape is prose only (F8). No registry/PyPI claim anywhere |
| NFR-5 | whole diff | ✅ met in the material, ⚠️ unproven by a run (F3); F4 is the one residual leak vector |
| NFR-6 | `tools/aspark-graph.md:72–75`, `:113–115`, `:120–131` | ✅ met — all three caveats present at the point of use |
| NFR-7 | `tools/aspark-graph.md:40–42` | ✅ met — grep over `skills/ agents/ templates/ lenses/ tools/ README.md` for a mutating invocation returns exactly two hits, both in the tool file: the permitted "named to the user" hint and the prohibition itself. No agent is instructed to run anything but `query` |
| NFR-8 | whole diff | ✅ met — no `US-`/`AC-`/`NFR-`/`T`/`F` ID renumbered; the `files:` note is additive inside an existing cell; both agents' step numbering unchanged |
| NFR-11 | `tools/aspark-graph.md` | ✅ met — `wc -l` = 131 ≤ 150, sliced per phase. F7/F8's fixes cost ~5 lines, comfortably inside the budget |
| NFR-9, NFR-10 | — | – T9/T10–T15, unstarted. NFR-10's record exists and is honest so far |

**Library lens.** §1 public surface: the additions are `tools/` and one file — minimal
and consciously committed (C12); note that `aspark-graph.md` is now hardcoded in a
skill, so the *filename* joined the internal contract too. §2 compatibility: purely
additive, protected structures byte-identical, no deprecation path needed; the bump
to `0.4.0` is still owed by T10. §3 packaging: N/A per the constitution. §4 contract
clarity: the wired query contract is documented and, where I could check it against
the consumer's source, correct — F7 and F8 are its two gaps.

## 5. What Was Checked

- [x] Correctness: every Must AC owned by T1–T4 traced to the line that implements it; all five external-contract claims in `tools/aspark-graph.md` (call forms, return shapes, exit-1-vs-`found:false`, confidence tiers, indexed extensions) verified against `~/aSPARK-graph`'s source rather than taken on trust
- [x] Non-functional: NFR-1/2/3/5/6/7/8/11 checked by diff, grep and `wc`; constitution §3's template contract verified byte-level; §6's degrade-to-silence traced through both branches of the wiring
- [x] Error handling: the absent, unbuilt, stale, empty and `found: false` paths each traced to an instruction; the one uncovered edge is the probe's own non-zero exit (F4)
- [x] Security: no secrets, no credentials, no user input parsed; the only live concern is executing an external command, and the diff instructs exactly one read-only probe plus read-only `query` calls
- [x] Tests: none exist and none are possible for prompt material (constitution §4). The substitute bar — `claude plugin validate` — passes. The real bar is the dogfood record, and F3 says what it does not yet prove
- [x] Readability: the tool file is well sliced and honest about its own limits; the `files:` rationale is the one place where the prose overstates its case (F5)

## 6. Verdict

**Changes requested.** The part that matters most is right: I could not find a way
for this diff to change a gate outcome, block a run, or say one word about the tool
in a project that does not have it — the probe sits after the hard gate as a
sub-bullet of an existing step, both agents' step numbering and the whole review
report template are untouched, the absent branch is an explicit "say nothing at
all", and the product name appears in no agent, template or lens. The `files:` note
is genuinely good work: identical in both places, byte-safe against the template
contract, and already dogfooded across all fifteen of the plan's own DoD cells. The
tool file is the most careful thing in the diff — its caveats are at the point of
use, `gate_health` appears once and only to forbid it, and every external contract
claim I checked against the other repo's source was accurate. What holds it back is
two things and neither is cosmetic. The skill collapses the approved four
availability states into two, so a Must criterion (AC-2.3) and the fourth state the
user personally confirmed can never fire — silently, and with no deviation
recorded, which is how an approved design quietly stops being the shipped one. And
the negative case cannot be considered run: this review executed the installed
0.3.1 plugin, which contains none of the changed files, so the evidence available
today proves the old material is silent and says nothing about the new. Fix F1,
re-run T5 against the working tree, and this is a pass — the remaining Minors are
one factual over-claim and three documentation gaps, all cheap.

**Fixed by the reviewer** (both re-verified: `claude plugin validate` passes,
step count still 5, `wc -l tools/aspark-graph.md` still 131, `gate_health` still
1 occurrence, no product name outside the peer-review skill and the tool file):

- F2 — `skills/peer-review/SKILL.md:25–30`: MCP tools are now matched on names
  *ending in* `staleness`/`impact` with the namespaced form as an example, and the
  ambiguous "use them" is now "treat that as the available surface"; the bullet was
  rewrapped to the file's 76-column convention.
- F6 — `tools/aspark-graph.md:5`: the frontmatter `detect:` shorthand now names
  `.aspark-graph/graph.json`, matching deviation D2 and the file's own body.

**Open question for the Engineering Manager.** T5's DoD ("exactly one detection
probe ran") assumes the ceremony under test is the one executing. It is not, and
nothing in the plan says how a working-tree build of the plugin gets exercised.
That mechanism is a precondition for T5, T11 and T12, and I cannot judge from the
repo which of the options (dev-install, marketplace re-point, manual step
execution) the user prefers.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [ ] No open Major findings — **F1** and **F3** are open. Neither may be waived by an agent; only the user can waive a Major, and the waiver must be recorded here with its reason
- [ ] Every Must AC traces to implementing code; no constitution non-negotiable violated — AC-2.3 has no reachable implementation (F1). No non-negotiable is violated: §6's degrade-to-silence holds in the material, §3's template contract is byte-identical, nothing is executed unasked
- [ ] All plan deviations documented and accepted — D1–D3 are documented and each matches the tree; the four-state collapse (F1) is an undocumented fourth deviation
- [x] Test suite runs green — no test suite exists and none is possible (constitution §4); the substitute bar, `claude plugin validate`, passes with one pre-existing unrelated warning
- [ ] Status set to `passed` — status is `changes-requested`

---

## Fixes applied by `/increment` (fix-mode, 2026-07-25)

Recorded next to the findings per the ceremony's fix-mode rule. F2 and F6 were
already fixed by the Reviewer during the review itself.

| Finding | Status | What was done |
|---|---|---|
| **F1** | **fixed** | `skills/peer-review/SKILL.md` now resolves **both** facts (surface? · `graph.json`?) and acts on all four states from `tools/aspark-graph.md`: pass the tool file only when both hold, emit the one-sentence hint at most once in either mixed state, and stay completely silent when neither holds. AC-2.3 and the P-Q3 fourth state are reachable again. Step count still 5, matching the frozen baseline |
| **F5** | **fixed** | The rationale was factually wrong and shipped identically in two files. Verified against the consumer's real parser: `_files_note` splits on `[,\s]+`, so a second `files:` keyword does **not** break the note — `files: a.py — more files: b.py` resolves **both** paths. Rule 3 ("keyword once") was deleted as unfounded; five rules became four. The two surviving mechanical rules were re-verified: `files: src/a.py.` → `['src/a.py.']` (trailing punctuation is real) and `files: a.py, b.py extra prose` → `['a.py','b.py','extra','prose']` (prose after the paths is real). Corrected in both `templates/plan.md` and `agents/engineering-manager.md`, still byte-identical to each other |
| **F3** | **escalated, not fixed here** | It is not a code defect — it invalidates the plan's test strategy. `/increment` stopped and returned to `/sprint-plan` for a revision, per its rule 4. The user chose to revise the strategy rather than install the working tree as the active plugin or overwrite the plugin cache. T5's evidence entry is **not** written: the run it describes did not exercise this change |
| **F4** | **fixed** | `skills/peer-review/SKILL.md` — the probe now reports both facts and **always exits 0** (`command -v … && echo runner=yes \|\| echo runner=no; test -f … && echo graph=yes \|\| echo graph=no`). Verified in this repo: prints `runner=no` / `graph=no`, exit code `0`. The absent case no longer ends the gate step on a visibly failed command — which was the most likely trigger for the volunteered sentence that *is* the R2 regression |
| **F7** | **fixed** | `tools/aspark-graph.md` gained a *Why these three and not the others* table tracing each wired query to its inputs (`staleness` → mtimes; `impact` → source + `implements` edges from `plan.md`; `story_trace` → `spec.md` + `plan.md` + source), and naming the boundary explicitly: the deferred two read the review and QA artifacts, whose filenames differ between conventions. A maintainer reopening a deferral (AC-4.3) can now check it against a stated rule |
| **F8** | **fixed** | `story_trace`'s return shape is documented, read from `~/aSPARK-graph/src/aspark_graph/queries.py:83-92`. The QA-leg keys AC-4.2 tells an agent not to read are now **named** — `acceptance_criteria[].qa_checks` and `acceptance_criteria[].latest_result` — with the reason their emptiness proves nothing. Its distinct `{"found": false}` failure mode is documented too |
| **F9** | **fixed** | Corrected by the Engineering Manager during plan revision 2: T4 now reads `in-progress`, T5 `in-progress`, and the revised table adds T16 for this fix-mode pass |

---

## 7. Round 2

**Date** 2026-07-26 · **Input** working tree vs `HEAD` (`fb6af66`) — 15 modified
files + untracked `tools/` · **Lens** `library` (§1, §2, §4; §3 N/A) ·
**Verdict** `changes-requested`

### 7.1 Scope

Round 1 saw 5 files at T4 of 16. Round 2 reviews the whole increment: T6–T16
(the `/sprint-plan`, `/demo-day`, QA-tester and EM wiring, `tools/README.md`,
the `README.md` entry, the conformance sweep and the `0.4.0` bump), **plus** a
second workstream the user folded in by explicit decision — the artifact line
budgets and context-hygiene edits in `templates/spec.md`,
`templates/review-report.md`, `templates/plan.md`, `skills/spark/SKILL.md`,
`skills/increment/SKILL.md`, `skills/go-live/SKILL.md`,
`agents/product-owner.md`, `agents/engineering-manager.md`, `agents/reviewer.md`
(all timestamped 2026-07-26 16:11–16:12). That workstream has no spec, no plan
and no task; it is judged on internal coherence, on conflict with graph-gates,
and against the constitution and the lens (§7.8).

Read as context: `spec.md`, `plan.md` (revision 2), `evidence.md`,
`.spark/constitution.md`, `lenses/library.md`, `templates/review-report.md`, and
— read-only, nothing written, no build, no graph — `~/aSPARK-graph`'s
`src/aspark_graph/{artifacts,queries}.py`.

Out of scope: `docs/*.docx*`, `.spark/BACKLOG.md`, `.aspark-graph/` (untracked
noise), and the pre-existing README miscount "the **nine** ceremony skills"
(`README.md:239`), which is at `HEAD` and not touched by this diff.

### 7.2 Round-1 findings, re-derived against the tree

Verified against the files, not against the fix table's claims.

| # | Claimed | Re-derived verdict |
|---|---|---|
| F1 | fixed (T16) | **Confirmed fixed.** `skills/peer-review/SKILL.md:38–43` resolves *both* facts and acts on four states; the hint states are `tools/aspark-graph.md:35` and `:36`. Both are reachable, because the ceremony — not the agent — consults the state table; they are mutually exclusive by construction (two booleans) and capped by "resolve … once" + "at most once". Propagated verbatim to `skills/sprint-plan/SKILL.md:29` and `skills/demo-day/SKILL.md:31`. AC-2.3 is reachable again |
| F2 | fixed by Reviewer | **Fixed, but incompletely propagated.** All three skills and the canonical bullet (`tools/README.md:53–68`) match on names *ending in* `staleness`/`impact` with the namespaced example. `tools/aspark-graph.md:20–21` still carried the loose pre-fix wording → new **F11**, fixed by me in this round |
| F3 | escalated, not fixed | **Resolved as a finding; the limitation it exposed is recorded, not hidden.** Plan revision 2 rewrote §4 around static / parser-in-the-loop / walkthrough evidence and named seven criteria as shipping *not proven*; `evidence.md:315–411` (Entry 3) opens by disclosing that the session's `/peer-review` ran the `0.3.1` cache (`0` vs `3` occurrences, measured) and explicitly **does not count it**, labels its method per entry, and closes with "What this does NOT establish"; `README.md:236` states the proof state to the user. That is exactly the fix F3 asked for ("record T5 as *not proven* and label it, rather than as passed"). One residual → **F14**. Nothing intended is written as delivered |
| F4 | fixed (T16) | **Confirmed fixed.** Probe form at `skills/peer-review/SKILL.md:34–35`; run live in this repo just now → `runner=no`, `graph=no`, `exit=0`. The second half of F4 (record whether a permission prompt naming the tool appeared — also a T16 DoD item) is **not** in `evidence.md`; folded into **F13** |
| F5 | fixed (T16) | **Confirmed fixed, and re-verified with the real parser.** Rule 3 deleted (five rules → four); the surviving rationale claims only true things. Re-ran `_files_note`: `files: src/a.py.` → `['src/a.py.']`; `files: a.py, b.py extra prose` → `['a.py','b.py','extra','prose']`; `files: src/a.py — more files: src/b.py` → both paths resolve, so deleting the second-keyword claim was correct. `templates/plan.md:39–57` and `agents/engineering-manager.md:66–85` are word-identical (AC-5.4) |
| F6 | fixed by Reviewer | **Confirmed fixed.** `tools/aspark-graph.md:5` reads `.aspark-graph/graph.json`. Corroborated live: this repo has `.aspark-graph/` holding only `parse-cache.json`, and the probe still resolves to state 4 — the directory existing does not flip the state, which is the evidence D2 was raised for |
| F7 | fixed (T16) | **Confirmed fixed.** `tools/aspark-graph.md:65–76` traces each wired query to its inputs and states the boundary ("the two deferred queries … read the review and QA artifacts, whose filenames differ between conventions"). Note `staleness` is now traced to **content hashes**, not mtimes — corrected in T13 and true (`queries.py`: `hashlib.sha256(path.read_bytes())`) → see §7.10 |
| F8 | fixed (T16) | **Half fixed.** Return shape and the QA-leg keys are delivered (`:52`, `:131–136`). The `ambiguous` failure mode is **not** documented, although T16's DoD names it explicitly → **F12** |
| F9 | corrected | **Confirmed.** All 16 tasks read `done` in `plan.md:247–262` |

### 7.3 Plan conformance, T6–T16

| Task | As planned? | Note |
|---|---|---|
| T6 | ✅ | `skills/sprint-plan/SKILL.md:29` probe bullet byte-identical to canonical (verified, whitespace-normalised); `:49–51` hand-over; `:57–61` step 3 relay, read-only `query` only, explicit "Never run a build, an install, or anything that writes"; `agents/engineering-manager.md:87–99` prescribes notes-then-query order, cite-or-record-empty, and the empty-≠-nothing-at-risk caveat. EM frontmatter still `tools: Read, Grep, Glob, Write` — no `Bash` (P-Q2) |
| T7 | ⚠️ | Probe placed **after** the browser/app gate (`skills/demo-day/SKILL.md:31`, with "A run that stopped on the browser or app gate **never reaches this sub-step**") — AC-3.5 holds by ordering. `agents/qa-tester.md:49–57` scopes, forbids `Result` cells resting on a tool answer. One DoD item not delivered as written → **F15** |
| T8 | ⚠️ | `tools/README.md` delivers the tool/lens boundary with an example each side, installation-state activation, pickup mechanics, add-another steps, the contract, and the canonical probe bullet with its one documented `/demo-day` variation. The DoD also promised the **hand-over** bullet verbatim; only prose describes it (`:39–40`), and the three skills' hand-over sentences do differ — `/sprint-plan` says "alongside the template" because it passes no lens paths. Correct as built, wider than the DoD claims → noted in **F15** |
| T9 | ⚠️ | `README.md:206` toolbox bullet, `:214–228` *Optional Tools* (optional, install-from-source, no registry claim, map-not-verdict), `:236` Project Status. Link `https://github.com/a-lottes/aSPARK-graph` resolves (HTTP 200) and matches the consumer's own `origin`. The unproven list is not itemised as the DoD requires → **F14** |
| T10 | ⚠️ | Every check re-run by me and every one **passes on the current tree** (§7.6). But the recorded output no longer describes what ships → **F13** |
| T11 | ✅ | `evidence.md:362–380` walks all three ceremonies, records the emit-nothing result per ceremony, and labels itself a walkthrough with its non-discharged ACs named |
| T12 | ✅ | `evidence.md:424–446` runs every documented call form for real, finds three shape mismatches and fixes the doc, adds `unknown_files`, and records a correction to its own mis-measurement of the unbuilt exit code. This is the strongest evidence in the trail |
| T13 | ✅ (D5) | Deviation D5 recorded and correct: `touch` could not have worked, because `staleness` hashes content. Verified in source myself |
| T14 | ✅ | Walkthrough, `AC-2.6` recorded not proven and venue-blocked. One overstated sentence → **F15** |
| T15 | ✅ (D4) | Fixture-based before/after (`evidence.md:486–511`): note present → `declared` `implements` edge and non-empty `affected_stories`/`affected_acs`; note absent → empty with `unknown_files: []`. A7 reproduced as a controlled experiment. D4 recorded, and strictly safer than planned |
| T16 | ⚠️ | F1, F5, F7 fully closed; F4 closed in the material but its evidence note missing (**F13**); F8's `ambiguous` half missing (**F12**) |

**Undocumented deviation.** `plan.md:202–207` lists `skills/spark/SKILL.md` as
**"Untouched on purpose"**. It is modified, and gained a numbered step. No `D6`
row exists → **F10**.

### 7.4 Findings (round 2)

IDs append; F1–F9 are round 1's.

| # | Sev | Location | Finding | Status |
|---|---|---|---|---|
| F10 | **Major** | `skills/spark/SKILL.md:81–91` (new step 5), renumbering old 5→6, 6→7, 7→8 | `/spark` gains a **new numbered step** ("Offer the clean handoff at heavy gates" — tell the user they may `/clear` and resume) and goes from **7 to 8** numbered steps. Measured against `HEAD`, it is the only ceremony whose step count changed. **Why it matters, four ways.** (1) **AC-1.2 is a Must criterion** and reads "when a ceremony runs, then it performs the same numbered steps … as a run of the pre-change version"; as shipped, `/spark` does not. The cause is not the graph wiring, but the AC measures what the user gets after installing `0.4.0`. (2) `plan.md:202–207` states this file is untouched on purpose *and gives the reason* (the orchestrator inherits the wiring via its step 3) — the shipped tree contradicts an approved plan with no `D6` deviation. (3) It is a **new user-visible capability with no spec, no AC, no task and no README or `docs/workflow.md` entry** — `grep -i "clear\|handoff"` over `README.md` and `docs/` returns nothing — against constitution §4 *Docs in step*. (4) `evidence.md`'s AC-1.2 verification (T1 baseline `:71–107`, T10 `:238–246`, T11) froze and compared step lists for **only the three wired ceremonies**; the three ceremonies this workstream actually edits (`/spark`, `/increment`, `/go-live`) were never baselined, so the one AC-1.2 breach in the tree is the one the evidence could not see. **Not a Blocker:** it breaks no constitution non-negotiable — the consumed contract (§2: command names, `${CLAUDE_PLUGIN_ROOT}` paths, protected template structures) is untouched, silence still degrades correctly, and the step *offers* and explicitly forbids acting for the user. The change itself reads like a good idea. **Fix — any one of three, all cheap:** (a) record it as deviation `D6` in `plan.md`, add its `README.md`/`docs/workflow.md` line, extend `evidence.md`'s baseline+comparison to all ten ceremonies, and narrow AC-1.2's reading in writing to *the ceremonies this feature wires*; (b) restructure it as a sub-bullet of the existing step 4 (*Stop at every gate*), which keeps the count at 7 and makes AC-1.2 true as written; (c) the user waives it, with the reason recorded here. I cannot waive it | open |
| F11 | Minor | `tools/aspark-graph.md:20–21` | The tool file described the MCP matcher as tools "named `staleness` and `impact` (possibly namespaced)" — the wording round 1's F2 replaced everywhere else. Two descriptions of one matcher in the same shipped surface, the looser one in the file that is the documented contract (AC-2.2, NFR-3, library lens §4), is the drift this feature exists to prevent. **Fixed by me**, line-neutral against the exhausted 150-line budget: now "tools whose names *end in* `staleness` and `impact` (e.g. `mcp__aspark-graph__staleness`)" | fixed |
| F12 | Minor | `tools/aspark-graph.md:58` | The failure line documents `bad_args` and `not_found` but **not** `ambiguous`. Verified live in the consumer: `queries.py:65` returns `{"found": false, "story": …, "reason": "ambiguous", "candidates": [...]}` whenever a bare `US-n` resolves in more than one feature — the normal case in any repo with several `.spark/<feature>/` trails, which is every mature aSPARK project. **Why it matters:** T16's DoD names this item explicitly, so a DoD is checked off undelivered; and the agent falls through to the generic empty-result rule (safe, but it scopes by hand) when the correct recovery is one clause away — re-ask with `--feature`. NFR-3 requires every instructed query documented with its behaviour on failure. **Fix:** add to `:58` — ambiguous `US-n` → `{"found": false, "reason": "ambiguous", "candidates": [...]}`, re-ask with `--feature`. **Note the bind:** `wc -l` is **exactly 150**, the NFR-11 ceiling, so this needs a compensating compression. Risk P6 already prescribes which: "the deferral block compresses — never a caveat". Left open rather than fixed by me, because choosing what to cut from `## Not wired` touches AC-4.3's reopen condition | open |
| F13 | Minor | `.spark/graph-gates/evidence.md:194–311` (Entry 2, T10) | The recorded conformance sweep no longer describes the tree it certifies. Two concrete drifts: `:276` records `147 tools/aspark-graph.md (cap 150)` and "**3 lines of headroom**" — the file is now **150**, exactly at the ceiling, because T12's doc fixes landed after the sweep (`tools/aspark-graph.md` mtime 2026-07-26 08:07, Entry 2 dated 2026-07-25); and `:251–252` records `git diff --stat templates/` as `templates/plan.md` alone, whereas `templates/spec.md` and `templates/review-report.md` are now modified too. Also missing: F4's second half, which T16's DoD requires ("the evidence notes whether a permission prompt naming the tool appeared") — `grep -i permission` over `evidence.md` returns nothing. **Why it matters:** this file *is* the test suite (constitution §3/§4), so a stale entry is a stale test result. Both checks still **pass** on the current tree — I re-ran every one (§7.6) — but "3 lines of headroom" is now false and is exactly the number the next author will trust, and the templates figure hides that two more templates changed. **Fix:** re-run Entry 2's commands against the final tree and update the two numbers, add a line naming the two extra template files as comment-only diffs, and record the permission-prompt observation (or its absence) | open |
| F14 | Minor | `README.md:236` | T9's DoD requires the unproven criteria "named individually (AC-1.1 at ceremony level, AC-2.1's live hand-over, AC-2.3's and the no-runner hint's firing, AC-2.4, AC-2.5, AC-2.6, AC-3.1, AC-3.2 behaviourally)". The paragraph names four groups in prose — hand-over, hints, graph-assisted review, QA-phase use — and no AC IDs; **AC-2.4** (the Plan-phase relay grounding *Affected Components*) and **AC-3.2** (stale behaviour) appear nowhere. **Why it matters:** the blanket clause "available-case behaviour not yet proven by a live run" does cover them, so nobody is misled and constitution §1 is not breached — this is a DoD miss, not a dishonesty, which is why it is Minor. But the itemisation is what makes the post-release checklist in `plan.md:352–366` checkable from the README, and NFR-9's bar is the README's own claim to reflect the current state. **Fix:** cite the seven AC IDs inline, mapped to the five checklist items; and add the `tools/` layer as its own `- [ ]`/`- [x]` row in the §Project Status list, where every previous layer has one | open |
| F15 | Minor | `agents/qa-tester.md:49–57`; `.spark/graph-gates/evidence.md:513–518`; `plan.md:254` (T7 DoD), `:255` (T8 DoD) | Three DoD cells describe something other than what shipped, none recorded as a deviation. (a) T7 requires the QA paragraph to **name the QA-leg keys** it must not read; it does not — it says "Follow its own rules about results it tells you not to read". **The build is right and the DoD is wrong:** naming `acceptance_criteria[].qa_checks` in an agent file is product-specific detail, which AC-6.3 forbids ("name no specific external product; all product-specific detail lives in the tool file only"). The keys are correctly in `tools/aspark-graph.md:133`. (b) T14's evidence says those three things are "present in `agents/qa-tester.md` and `tools/aspark-graph.md`" — true only across the pair, false of the agent file alone. (c) T8 promises the **hand-over** bullet verbatim in `tools/README.md`; only prose describes it (`:39–40`), and the three copies legitimately differ. **Why it matters:** a DoD that contradicts an AC is a trap for the next reader, who will "fix" the code toward the DoD and break AC-6.3. **Fix:** correct T7's DoD to "defers to the tool file for the key names, per AC-6.3", reword the evidence sentence to "across the two files", and either drop T8's hand-over-verbatim claim or state the permitted per-ceremony variation as `tools/README.md:71–73` already does for the probe | open |
| F16 | Minor | `skills/increment/SKILL.md:24–34` | The new working set is `plan.md` §1–§4 and `spec.md` §4–§6, with everything else declared "material the Plan phase already consumed". For `plan.md` that excludes the **preamble** and everything after §4 — where the user-confirmed planning decisions (`plan.md:37–54`, P-Q1–P-Q5), the **Deviations** table (`:420–431`) and **Review Findings Carried** (`:437–447`) live; for `spec.md` it excludes §3 Assumptions and §7 Clarifications. **Why it matters, demonstrated by this very feature:** P-Q3 — the four availability states — sits in the plan preamble, outside §1–§4, and losing it is precisely round-1 **F1**, a Major. AC-2.3's binding "once per ceremony run" reading is spec §7 C9. Step 4 also tells `/increment` to append deviations to a section the working set never loads. The escape hatch ("Pull a further section only when a task actually calls for it") does not help, because the point of these sections is that the task does not know it needs them. Secondary, same lines: the rule cites template **section numbers**, making `templates/plan.md`'s numbering a consumed reference for the first time — soft, because each number carries its heading name, but new surface (library lens §1) not recorded in the constitution's §3 table. **Fix:** add the plan's header/decision preamble, its *Deviations* and *Review Findings Carried* sections, and the spec's §3 and §7 to the working set — they are short and they are where the binding decisions live; keep the exclusion for personas, the design review and the risk table | open |
| F17 | Minor | `templates/spec.md:10`, `templates/plan.md:11`, `templates/review-report.md:11` | The budgets ship in the same increment as artifacts that overrun them by 1.5–2×, with no exemption recorded anywhere: `spec.md` **422** lines against ~250, `plan.md` **447** against ~300, this report **210 before §7** against ~150. `templates/review-report.md:11` also says "Findings are rows, not essays", while round 1's F1 and F5 are ~300-word cells in the same commit. **Why it matters:** it is not a contract problem — the notes are HTML comments, add no heading, are invisible to the consumer's parser (verified: `_files_note` runs only on task-table DoD cells and the new comments contain no `\|`), and no gate checklist enforces them, so the library lens's "every template heading is a promise" and constitution §3 are both untouched. It is a **credibility** problem, and it is the same failure mode round 1's F5 named: the first reader who checks the new rule against the repo's own newest artifacts learns it is advisory, and a rule that arrives already unenforced does not start being enforced later. Coverage is also uneven with no reason given — `qa-report.md`, `release-notes.md` and `constitution.md` get no budget, and `agents/qa-tester.md`/`release-manager.md` no matching rule. **Fix (cheap, and not "shrink the artifacts"):** add one clause to each note grandfathering artifacts written before it, **or** one line in each of this feature's artifacts stating that it predates the budget; and say in `tools/README.md`-style prose why three templates carry a budget and three do not | open |

### 7.5 Requirements traceability

Every Must AC. "not proven" uses the plan's own §4 wording.

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `skills/{peer-review,sprint-plan,demo-day}/SKILL.md` absent branch; `evidence.md:315–411` | ✅ met in the material — I re-ran the grep: `aspark-graph`/`.aspark-graph` appear in exactly 3 files (the wired skills) + 1 line in `README.md`, and **0** times under `agents/`, `templates/`, `lenses/`. **Ceremony level: not proven** (F3, accepted, post-release item 1) |
| AC-1.2 | step counts 5/6/6 for the wired three | ❌ **not met as shipped** — `/spark` is 7 → 8 numbered steps (**F10**). The wired three are unchanged (verified against `evidence.md:77–107`), gate checklists and template headings untouched |
| AC-1.3 | `skills/*/SKILL.md` "never let the outcome change a gate"; templates' gate checklists untouched | ✅ met — no checklist item anywhere references tool state; `/demo-day` evaluates its hard gates before the probe |
| AC-1.4 | `evidence.md:315–323` | ✅ met — Entry 3 (negative case) is written before every graph-using entry and says so; ordering enforced by the `Depends on` column |
| AC-1.5 | whole diff | ✅ met — nothing asks a target project for a file, flag or `CLAUDE.md` block |
| AC-2.1 | `skills/peer-review:52–54`, `sprint-plan:47–49`, `demo-day:54–56` | ✅ met in the material — hand-over inside the existing step 2, one more path, no new ceremony or agent. **Live hand-over: not proven** (post-release item 2) |
| AC-2.2 | `tools/aspark-graph.md:20–23`; the three probe bullets | ✅ met — one documented precedence order (MCP → CLI), now consistently worded after F11 |
| AC-2.3 | `tools/aspark-graph.md:35` reached via `skills/*:38–43` | ✅ met in the material — reachable again after F1's fix, one sentence, at most once. **Firing: not proven** (post-release item 3) |
| AC-2.4 | `agents/engineering-manager.md:87–99`; `skills/sprint-plan/SKILL.md:57–61` | ✅ met in the material — cite-or-record-empty with the caveat; the relay exists so the EM needs no `Bash`. **Not proven** (post-release item 4) — and **not named in the README** (F14) |
| AC-2.5 | `agents/reviewer.md:94–98`; `tools/aspark-graph.md:120–123` | ✅ met in the material. **Not proven** (post-release item 2) |
| AC-2.6 | `agents/qa-tester.md:49–53`; `tools/aspark-graph.md:125–139` | ✅ met in the material. **Not proven, venue-blocked** (P3) — stated in `plan.md:344`, `evidence.md:520–522`, `README.md:236` |
| AC-3.1 | `agents/reviewer.md:100–103` | ✅ met — "a finding that restates a tool's output without a concrete `file:line` and the code behind it is not a finding". **Behaviour not proven** (post-release item 2) |
| AC-3.2 | `tools/aspark-graph.md:82–84` | ✅ met (contract half, verified in `queries.py`). **Behaviour not proven** (post-release item 5); **not named in the README** (F14) |
| AC-3.3 | `tools/aspark-graph.md:85–87`, `:60–63` | ✅ met — and strengthened beyond the AC by `unknown_files`, which distinguishes "I do not index these" from "nothing depends on these" |
| AC-3.4 | `agents/qa-tester.md:55–57`; `tools/aspark-graph.md:138–139` | ✅ met — "No `Result` cell may rest on a tool answer", in both places |
| AC-3.5 | `skills/demo-day/SKILL.md:27–31`, `:45–47` | ✅ met by **ordering**, not by promise: the probe is placed after the browser/app STOP and says so |
| AC-3.6 | `tools/aspark-graph.md:80–81`, `:111–112`, `:122–123`, `:138–139`; `agents/{reviewer:100–103,qa-tester:55–57,engineering-manager:94–99}` | ✅ met — every slice and all three agent paragraphs, each in its own words |
| AC-4.1 | `tools/aspark-graph.md:143` | ✅ met — re-run: `gate_health` occurs **once** in shipped material, inside `## Not wired (deliberate)`, ending "**do not call it.**"; 0 hits under `skills/`, `agents/`, `templates/`, `lenses/` |
| AC-4.2 | `tools/aspark-graph.md:131–136` | ✅ met — QA leg declared unpopulated, both keys named, emptiness declared not a finding |
| AC-4.3 | `tools/aspark-graph.md:141–150` | ✅ met — both deferrals with a concrete reopen condition |
| AC-4.4 | `tools/aspark-graph.md:65–76` | ✅ met — the trace F7 asked for now exists, with the boundary stated. Reads *content hashes* rather than the spec's "mtimes" (§7.10) |
| AC-4.5 | `tools/aspark-graph.md:90–93`; `agents/engineering-manager.md:96–97` | ✅ met — "empty here means *the plan declared no links*, **not** *nothing is at risk*", in the tool file and in the EM's own words |
| AC-5.1 | `templates/plan.md:39–57`; `agents/engineering-manager.md:66–85` | ✅ met — and dogfooded: I re-ran the consumer's `_files_note` over all 16 DoD cells of this plan → **0 violations** |
| AC-5.2 | `templates/plan.md:48–49`; `agents/engineering-manager.md:76–77` | ✅ met — rule 4, "omit … never guess", with the downstream reason |
| AC-5.3 | `git diff HEAD -- templates/` | ✅ met — verified for **all three** modified templates, not just `plan.md`: every added/removed line falls inside an HTML comment; no heading, header row, column, task ID, story-heading or AC-line form touched |
| AC-5.4 | `templates/plan.md` vs `agents/engineering-manager.md` | ✅ met — whitespace-normalised comparison of the whole four-rule block plus rationale: **identical** |
| NFR-1 | `templates/`, `.claude-plugin/plugin.json:4` | ✅ met — protected structures byte-identical, `0.3.1` → **`0.4.0`**, correct minor bump |
| NFR-2 | `skills/`, `agents/`, `tools/` | ✅ met — **10** skills, **7** agents (re-counted); only new public surface is `tools/`, referenced solely as `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` |
| NFR-3 | `tools/aspark-graph.md:43–76`; `README.md:214–228` | ⚠️ partial — call forms, shapes and failures documented and verified against the live consumer (T12), no registry claim, link resolves. One failure mode still undocumented (**F12**) |
| NFR-4 | — | N/A per constitution |
| NFR-5 | whole diff + live probe | ✅ met in the material — probe exits 0, absent branch is "say nothing at all", no gate conditioned on tool state. **Ceremony level: not proven** (F3, accepted) |
| NFR-6 | `tools/aspark-graph.md:90–93`, `:131–136`, `:141–150` | ✅ met — all three caveats at the point of use |
| NFR-7 | grep of `skills/ agents/ tools/ templates/ README.md` | ✅ met — exactly two hits for a mutating invocation, both in `tools/aspark-graph.md` (`:35` the permitted name-it-to-the-user hint, `:39` the prohibition). No agent is instructed to run anything but `query` |
| NFR-8 | whole diff | ✅ met — no `US-`/`AC-`/`NFR-`/`T`/`F` ID renumbered; the `files:` note is additive inside an existing cell. `/spark`'s step renumbering is not an ID chain, so NFR-8 holds — it lands on AC-1.2 instead (**F10**) |
| NFR-9 | `README.md:206`, `:214–228`, `:236` | ⚠️ partial — entry ships in the same change, optional and install-from-source, proof state stated. Not itemised (**F14**) |
| NFR-10 | `.spark/graph-gates/evidence.md` | ⚠️ partial — a real record: negative case first, method labelled per entry, four documentation defects and one incapable verification method caught **by running things**. Two recorded numbers no longer describe the tree (**F13**) |
| NFR-11 | `wc -l tools/aspark-graph.md` | ✅ met — **150** ≤ 150, sliced per phase. At the ceiling with zero headroom; F12's fix needs the P6 compression |
| NFR-12, NFR-13 | — | N/A per spec and constitution |

### 7.6 The T10 conformance sweep, re-run by me

Not read from `evidence.md` — executed against the current tree.

| Check | Result |
|---|---|
| `.claude-plugin/plugin.json` version | `0.4.0` ✅ |
| `wc -l tools/aspark-graph.md` | **150** — at the ≤150 ceiling, **not** the `147` on record (F13) |
| `gate_health` in shipped material | 1 occurrence, `tools/aspark-graph.md:143`, deferral block only ✅ |
| Probe bullet locations | `skills/peer-review:29`, `sprint-plan:29`, `demo-day:31`, canonical `tools/README.md:53–68` ✅ |
| Probe bullets vs canonical | `/peer-review` and `/sprint-plan` **identical** (whitespace-normalised for nesting depth). `/demo-day` differs in exactly the two places `tools/README.md:71–73` permits — opening clause and closing clause — with **every word between identical**. The DoD's word "byte-identical" is the overstatement, not the code |
| Product name outside the wired skills | 0 in `agents/`, `templates/`, `lenses/` ✅ |
| Skills / agents | 10 / 7 ✅ |
| Step counts vs `HEAD`, **all ten ceremonies** | charter 5, demo-day 6, go-live 7, increment 6, look-and-feel 7, next-steps 6, peer-review 5, sprint-plan 6, story-time 8 — unchanged. **spark 7 → 8** ❌ (F10) |
| `templates/` diff | comment-only in all three modified templates ✅ (two more files than on record — F13) |
| NFR-7 mutating-invocation grep | 2 permitted hits ✅ |
| `_files_note` over this plan's 16 DoD cells | 0 violations ✅ (reproduced) |
| `claude plugin validate .` | ✅ passes; one pre-existing unrelated `autoUpdate` warning — the substitute for a green suite (constitution §4) |
| Probe live, this repo | `runner=no`, `graph=no`, **exit 0**; `.aspark-graph/` present with only `parse-cache.json` → state 4, silence. Evidence for F6/D2 |

Independent agreement on every figure the caller had already confirmed.

### 7.7 Library lens

- **§1 Public surface.** Additions are `tools/` and two files — minimal and
  consciously committed (C12). Two new internal promises to note: the *filename*
  `aspark-graph.md` is hardcoded in three skills, and `skills/increment` now
  cites `templates/` **section numbers** (F16). Counts hold at 10/7.
- **§2 Compatibility.** Purely additive; every protected structure byte-identical
  across all three modified templates; `0.4.0` is the right minor bump; no
  deprecation path needed. `/spark`'s step renumbering is not in the declared
  consumed contract (constitution §2), so it is **not** a semver breach — it is
  an AC-1.2 breach (F10).
- **§3 Packaging.** N/A per the constitution.
- **§4 Contract clarity.** The wired query contract is documented and, where I
  checked it against the consumer's source, correct. Two gaps: F11 (fixed) and
  F12 (open). The budget notes add no heading and therefore no promise (F17).

### 7.8 The folded-in budget / context workstream

Judged on the merits, as asked.

- **Coherent as a workstream.** All nine edits serve one idea — context is the
  scarce resource — and each is internally consistent: three artifact budgets,
  three matching agent rules that carry no competing number, a working-set rule
  for `/increment`, a status-only read rule for `/spark`, `/peer-review` and
  `/go-live`, and a `/clear` offer. The agent rules correctly defer the number to
  the template, so there is exactly one place to change it.
- **No conflict with graph-gates.** `templates/plan.md` carries both new comments
  without collision; the probe sub-bullets and the status-only read rules sit in
  the same step 1 and agree ("read only what the gate asks", then probe). The
  `files:` note is short enough not to fight the plan budget.
- **No contract breach.** Comment-only diffs, verified line by line; no heading
  added; the consumer's parser cannot see comments, and I confirmed the new
  `files: src/auth/session.ts` **example** inside the template comment cannot be
  mistaken for a real note — `_files_note` runs only on task-table DoD cells and
  the comment contains no `|`, so it forms no row.
- **Two things it gets wrong.** The `/spark` step is not a budget note at all: it
  is new behaviour, and it ships untraceable and undocumented (**F10**, Major).
  And the budgets arrive already broken by the artifacts they ship beside
  (**F17**, Minor) — a documentation/credibility problem, not a contract one.
- **The budget note in `templates/review-report.md` does bind this report,** and
  I wrote §7 to it: findings are rows, the tables carry the argument, and prose
  is spent only on the verdict. It does not bind §1–§6, which predate it. The
  file is now well over 150 lines because it is two rounds in one document —
  worth deciding once, in the template, whether the budget is per report or per
  round.

### 7.9 Fixed by the Reviewer in round 2

- **F11** — `tools/aspark-graph.md:20–21`: the MCP precedence step now matches on
  names *ending in* `staleness`/`impact` with the namespaced example, consistent
  with the three skills and the canonical bullet. Chosen to be **line-neutral**:
  `wc -l` still **150**, so NFR-11 is unaffected.

Re-verified after the edit: `wc -l` 150, `gate_health` 1, product name still
absent from `agents/`/`templates/`/`lenses/`, step counts unchanged,
`claude plugin validate .` passes.

Nothing else was touched. F12's fix needs a compensating compression of shipped
caveat text and F13–F17 need content decisions, so all five stay open for
`/increment`.

### 7.10 Open questions

1. **For the Engineering Manager — `mtimes` vs content hashes.** AC-4.4 and A5
   say the wired queries depend on "file **mtimes**". T13 established, and I
   re-verified in `queries.py`, that `staleness` compares sha256 **content
   hashes**. The tool file was corrected; the spec was not (it is `approved` and
   not mine to edit). AC-4.4 still holds on its other limb ("source files"), so
   nothing fails — but the spec now contains a claim the evidence disproves.
   Amend it, or record the correction in a clarification.
2. **For the user — is the `/spark` clean-handoff step in scope?** I can see
   *what* it does but not whether it was meant to ship in this increment or was
   in-flight work caught by the diff. That decision picks between F10's fixes (a),
   (b) and (c), and I cannot make it.

### 7.11 Verdict

**Changes requested.** The graph-gates feature itself is in good shape and round
1's real complaints are genuinely closed: the four availability states are back,
both hint sentences are reachable and mutually exclusive, the probe exits zero,
the `files:` rationale now claims only what the parser actually does — I re-ran
the parser and it does — and `gate_health` still appears exactly once, only to
forbid itself. The evidence trail earned my trust in a way that is rare: T12 and
T13 caught four documentation defects and one verification method that was
incapable of proving what it claimed, by running real code rather than reading
it, and Entry 3 opens by disqualifying the session's own clean `/peer-review` run
as evidence about the wrong plugin build. That is F3's fix, and it is the
strongest thing in this increment: the honest label was chosen over the
comfortable claim, seven criteria are named as shipping not proven, and the
README tells the user so. What blocks the gate is not the graph wiring but what
travelled with it. `skills/spark/SKILL.md` gained a numbered step and a new
user-visible behaviour, taking the orchestrator from seven steps to eight — with
no spec, no task, no README or workflow entry, no deviation row, and against a
plan that names that exact file as untouched on purpose and explains why. It
breaks AC-1.2, a Must criterion, and it breaks it in the one ceremony this
feature's own evidence never baselined, which is why nothing caught it. It is not
a Blocker: the consumed contract is intact, silence still degrades correctly, and
the step asks rather than acts — it may well be a good idea. But it is a Major,
no waiver exists, and I cannot waive my own finding. Fix or waive F10, close the
five open Minors — the conformance sweep needs re-running against the tree it
certifies, and `ambiguous` needs its line — and this passes. The line budgets are
worth shipping and worth writing down; they just cannot arrive already broken by
the artifacts standing next to them.

---

## ✅ REVIEW GATE (binding)

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

**Ruled at round 2 (2026-07-26) as `changes-requested`; re-ruled in place at round
3 (2026-07-26) after the fix pass — see §8.** Each box shows its round-3 state,
with round 2's reason kept after the em-dash so the change is auditable.

- [x] No open Blocker findings — none found at either round; the consumed contract, degrade-to-silence, nothing-unasked and no-agent-passes-its-own-gate re-verified intact after the fix pass
- [x] No open Major findings — **F10 closed** (§8.2). *Round 2:* F10 open. It was not waived: the deviation is recorded as `plan.md` **D6**, AC-1.2's scope is narrowed on the record by spec **C13** with the user's authorisation, and the behaviour is documented in `README.md:196` and `docs/workflow.md:101–105`. The finding was that the step shipped untraceable and undocumented; it is now traceable and documented
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — **26 of 26 trace.** *Round 2:* 25 of 26; AC-1.2 failed as shipped (`/spark` 7 → 8 steps). AC-1.2 now binds the three wired ceremonies, which are verified unchanged at 5/6/6 against T1's baseline; I accept the narrowing as principled (§8.1) and it removes no protection against R2. No non-negotiable is violated. Seven criteria still ship **not proven** by user-accepted design (F3) — labelled, not claimed, and now itemised in `README.md`
- [x] All plan deviations documented and accepted — **D1–D6.** *Round 2:* D6 missing. Each of the six matches the tree (D2 corroborated live, D5 verified in the consumer's source, D6 verified against `git show HEAD:skills/spark/SKILL.md`). F15's three mis-describing DoD cells are **accepted by the user with the reason on the record** — the fix table states that in T7's case the build is right and the DoD is wrong because AC-6.3 forbids what it asks for, which defuses the trap the finding named. That is what makes *accepted* sufficient here rather than merely convenient
- [x] Test suite runs green — no suite exists and none is possible (constitution §3/§4). `claude plugin validate .` passes with one pre-existing unrelated `autoUpdate` warning; the NFR-10 record exists, is method-labelled, and I re-ran its conformance sweep independently at round 2 (§7.6) and again at round 3 (§8.3) with agreement on every figure
- [x] Status set to `passed` — status is **`passed`** as of round 3. Five Minors ship open and named: **F12, F15, F16, F17** accepted as-is by the user, and **F18** raised at round 3. None is a correctness defect in shipped behaviour; each is recorded with its fix

---

## Fixes applied by `/increment` (fix-mode, 2026-07-26)

Recorded next to the findings per the ceremony's fix-mode rule. Routing decisions
were taken by the user at the round-2 gate: **F10 kept and documented**, **F13 and
F14 fixed**, **F12 / F15 / F16 / F17 accepted as-is**.

| Finding | Status | What was done |
|---|---|---|
| **F10** | **resolved by documenting — the change is kept** | The user's decision, and the reason is on the record: the step guards against exactly the failure that opened this session (a previous session left `review.md` claiming `passed` with its verdict section missing). Four edits, none of them to the shipped step itself: **(1)** spec **C13** — AC-1.2 narrowed to the three *wired* ceremonies, with the reasoning that AC-1.2 was written to stop the graph wiring from changing behaviour, not to freeze every file against unrelated concurrent work; AC-1.1/1.3/1.5 explicitly **not** narrowed and still bind every ceremony. **(2)** plan **D6** — the deviation recorded, naming the real defect (it arrived with no task and no row), and correcting §2's reason: NFR-2's counts hold because no skill is *added*, not because the file is unedited. **(3)** `README.md:194` and **(4)** `docs/workflow.md:97` — the behaviour documented, both stating that it offers and never clears, and that statuses must be current first. Spec keeps status `approved`: the amendment narrows scope and adds no requirement |
| **F13** | **fixed** | The T10 sweep was re-run against the tree it certifies, and both stale figures replaced with measured output, each labelling what it supersedes. `wc -l tools/aspark-graph.md` = **150, zero headroom** — not the recorded 147 with "3 lines of headroom" — with the consequence stated: any further addition must displace something (risk P6), which is *why* F12 was left open rather than appended silently. `git diff --stat templates/` now shows **three** files, 36 insertions — and the AC-5.3 check was re-run across all three: no table row, column heading, section heading or task ID touched in any of them, so the template contract holds for the budget comments too. F4's missing DoD leg added: probe output pasted (`runner=no` / `graph=no`, exit 0), with live corroboration of **D2** (this repo's `.aspark-graph/` holds only `parse-cache.json`, and correctly does not flip the state) — and the user-visible-permission-prompt leg labelled **not proven**, because it cannot be attested from inside the session |
| **F14** | **fixed** | `README.md` now itemises the unproven criteria in a table instead of describing them in prose, one row each for AC-1.1 (ceremony level), AC-2.1, **AC-2.3**, **AC-2.4**, AC-2.5, AC-2.6 and AC-3.1/AC-3.2 — the two the finding named as appearing nowhere are now named. Each row says what specifically is not proven, AC-2.6 carries "no venue exists at all", and the AC-3.2 row distinguishes the `staleness` behaviour that *is* verified in the consumer's source from the ceremony reaction that is not |
| **F12** | **accepted as-is by the user** | `ambiguous` / `candidates` stays undocumented this cycle. The bind is real: `tools/aspark-graph.md` is at exactly its 150-line NFR-11 ceiling, so documenting it means choosing shipped caveat text to compress. Carried as the first candidate for the next change to that file |
| **F15** | **accepted as-is by the user** | Three DoD cells still describe something other than what shipped. Note for whoever reopens this: in T7's case **the build is right and the DoD is wrong** — it asks for the QA-leg key names in `agents/qa-tester.md`, which AC-6.3 forbids |
| **F16** | **accepted as-is by the user** | `/increment`'s working set still excludes the plan preamble, *Deviations* and *Review Findings Carried*. The demonstrated cost stands on the record: P-Q3 (the four availability states) lives in the preamble, and losing it *is* round-1 F1 |
| **F17** | **accepted as-is by the user** | The budgets ship beside artifacts at 1.5–2× them, with no grandfathering clause, and the per-report-vs-per-round question for `review-report.md` is left open — this report is 477 lines against a ~150 budget across two rounds |

---

## 8. Round 3 — verification of the fix pass

**Date** 2026-07-26 · **Input** the six record/doc edits made after the round-2
gate, plus a re-verification that shipped behaviour did not move · **Ruling**
`passed`

### 8.0 What actually changed, measured

Confirmed before judging anything: **no shipped skill, agent, template or tool
file moved in this pass.** `git diff --stat HEAD` over `skills/ agents/
templates/ .claude-plugin/` is byte-identical to what I reviewed at round 2, and
`skills/spark/SKILL.md` still has mtime 16:11:09 — i.e. step 5 was deliberately
not touched, as described. `tools/aspark-graph.md` carries only my own
line-neutral F11 edit (`wc -l` **150**). Re-run: `gate_health` 1 occurrence, 0
product-name hits in `agents/`/`templates/`/`lenses/`, 10 skills / 7 agents, step
counts `charter 5 · demo-day 6 · go-live 7 · increment 6 · look-and-feel 7 ·
next-steps 6 · peer-review 5 · spark 8 · sprint-plan 6 · story-time 8`,
`claude plugin validate .` passes with the one pre-existing `autoUpdate` warning.
**So §7's verdict on the shipped material stands unchanged**, and §8 judges only
whether the record now describes it honestly.

Two shipped **docs** files did change and are judged below: `README.md` and
`docs/workflow.md`.

### 8.1 The C13 narrowing of AC-1.2 — accepted

**(a) Principled, not retrofitted — accepted, and here is the test I applied.**
The move is structurally suspicious: a Must AC was narrowed after the code broke
it, by the same session that wrote the code. That is the shape of spec-follows-code,
and it is adjacent to round 1's F1 ("an approved design quietly stops being the
shipped one"). I accept it anyway, on four checks:

1. **The story's own "so that" clause names the cause.** US-1 reads "…so that
   **someone else's optional accelerant** never becomes a change to my loop." The
   subject of the protection is the accelerant. Step 5 is not it. C13 argues on the
   AC's own terms, not on the code's.
2. **The AC's stated check cannot reach `/spark`.** AC-1.2 is "checkable by
   comparing the two runs' **artifacts**", and `/spark` produces no artifact. The
   text was written about artifact-producing ceremonies; the narrowing recovers
   the intent rather than inventing one.
3. **It removes no protection against the risk the AC guards.** R2 is a gate
   mentioning or blocking on the tool. The narrowed AC still binds all three
   ceremonies that carry a probe; the seven it releases contain **0** occurrences
   of the product name and no probe — verified, not assumed. This is the decisive
   check: a narrowing that shrank R2 coverage would be a retrofit whatever its
   reasoning.
4. **The narrowing did not discharge the finding.** F10 is kept, D6 records it,
   and the behaviour is documented. Three separate acts; a retrofit would have
   done only the first. Had AC-1.2 merely been narrowed and the finding closed on
   that alone, I would have refused it.

One thing the narrowing does **not** do, and the record should be read with this
in mind: it correctly removes step 5 from *graph-gates'* scope, but that does not
make step 5 verified — it makes it verified by nobody. What closes that honestly
is edit 4 (the docs), not C13. C13 plus documentation is defensible; C13 alone
would not have been.

**(b) The "not narrowed" claim checks out.** Verified against `skills/spark/SKILL.md:81–91`:

| Claim | Verdict |
|---|---|
| AC-1.1 still binds — step 5 says nothing about the tool | ✅ the step's eleven lines contain no occurrence of `aspark-graph`/`.aspark-graph`; the whole file has 0 |
| AC-1.3 still binds — conditions no gate on tool availability | ✅ its only condition is "After the user approves a gate that followed heavy work"; nothing reads tool state |
| AC-1.5 still binds — writes nothing in a target project to enable/disable the tool | ✅ it writes nothing at all. "Make sure every status on disk is current" refers to aSPARK's own artifact statuses, which every ceremony already maintains, and is unrelated to tool enablement |

**(c) Keeping `approved` is defensible — with one line still owed.**
Constitution §1 requires the approval to be "the user's, given explicitly and
recorded in the artifact". C13 is dated 2026-07-26 and records the authorisation,
so the non-negotiable is satisfied and no re-approval *round* is needed: the
amendment narrows scope, adds no requirement, invalidates no task and forces no
rework downstream — which is materially different from plan revision 2, where §4
was rewritten and the status correctly round-tripped to `draft`. **What is owed:**
the SPEC GATE's last box still reads only "Status set to `approved` by the user"
dated 2026-07-25, so a reader checking the gate sees an approval that predates the
AC-1.2 text it approves. One clause — "…and the C13 narrowing of AC-1.2
authorised 2026-07-26" — closes it. I have not made that edit myself because
`spec.md` was placed off-limits to me; it is a recommendation, not a gate-holder,
because the authorisation *is* recorded, just not where the gate points.

### 8.2 The other five edits

| Edit | Verified | Verdict |
|---|---|---|
| **2 — plan `D6` + §2** | `plan.md:436` (D6), `:202–215` (retitled *Untouched by the graph wiring* + "Superseded in part" note) | ✅ **and it corrects a real error of reasoning**, not just a fact: §2 had justified NFR-2's counts by the files being *unedited*; the corrected sentence justifies them by no skill or agent being *added*. I measured 10 / 7 — the counts hold and the new reason is the right one. D6 is honest about the actual defect ("it arrived without a task or a deviation row, which is the actual defect"), and names the detection gap rather than hiding it ("`/spark` still has no baseline in `evidence.md` T1, which is why nothing caught this"). Verified against `git show HEAD:skills/spark/SKILL.md`: 7 steps before, 8 now |
| **3 — `evidence.md` T10 re-run** | `evidence.md` NFR-11, NFR-1/AC-5.3 and the new F4 sub-entry | ✅ on the figures, with one false claim I corrected (§8.4). Reproduced independently: `wc -l` = **150**, and "zero headroom" is the right reading; `git diff --stat templates/` = 3 files / 36 insertions / 1 deletion, exactly as pasted; the structural grep returns no output. I went further than the recorded check and confirmed **every added line in all three templates falls inside an HTML comment** — the only exceptions are three blank separator lines — so AC-5.3 holds rigorously for the budget comments, not just by the grep's sampling. **Supersession labelling is honest:** each corrected figure ends with "*Superseded original:* …" quoting what it replaces, so history is annotated, not overwritten |
| **4 — `README.md:196`, `docs/workflow.md:101–105`** | against `skills/spark/SKILL.md:81–91` | ✅ accurate, neither over- nor under-claiming. Both say it offers and never clears ("It only ever offers; clearing is your call" / "It offers, never clears for them"), matching "Offer it; never do it for them". `docs/workflow.md` additionally carries the statuses-current precondition *with its reason* ("a resume that reads a stale status resumes into the wrong phase"), which is the one substantive thing the README omits — correctly, since it is an obligation on the orchestrator, not information the user acts on. The division of detail is the right one. Constitution §4's *Docs in step* bar is now met for step 5 |
| **5 — `README.md` unproven table** | against §7.5 | ⚠️ **complete, with three description errors I fixed** (§8.4). Coverage is right: all seven rows of `plan.md` §4's table are present, AC-2.4 and AC-3.2 are named as F14 required, the no-runner hint is carried at `:252`, and nothing is listed as unproven that I found proven. The **AC-3.2 row draws the line correctly** — "The underlying `staleness` behaviour *is* verified in the consumer's source; the ceremony's reaction to it is not" — which is exactly T13's finding and exactly the distinction I drew in §7.5 |
| **6 — the fix-mode table** | against §7.4 | ✅ accurate about my findings, including the two places it would have been easy to shade: F12's row states the 150-line bind as the reason rather than as an excuse, and **F15's row records the reasoning behind the acceptance** — "in T7's case the build is right and the DoD is wrong — it asks for the QA-leg key names in `agents/qa-tester.md`, which AC-6.3 forbids". That sentence is what turns an acceptance into a safe one, and it is why gate box 4 closes. F17's row will read 477 lines; it is now 495+ (§8.5) |

### 8.3 New finding

| # | Sev | Location | Finding | Status |
|---|---|---|---|---|
| F18 | Minor | `.spark/graph-gates/plan.md:190–200` (§2 *Edited files*) | The fix pass edited **`docs/workflow.md`**, which appears in neither §2's *Edited files (9)* table nor its *Untouched* list nor D6's supersession note; and §2's `README.md` row still describes only the graph content ("new `## Optional Tools` … one bullet … one Project Status line") although README now also carries the clean-handoff paragraph and the unproven table. **Why it matters:** an edited file missing from *Affected Components* is precisely the pattern that produced F10, recurring one round later in the pass that fixed it. It is Minor rather than Major because these are review-driven fix-mode edits, which are recorded in the fix table by design and are not plan deviations — so nothing is untraceable, it is just traceable in the other book. **Fix:** add `docs/workflow.md` to §2 with its insertion point, and extend the `README.md` row to name the two additions. **Does not hold the gate:** box 4 is about deviations, and no deviation is missing | open |

Nearly a second finding, and deliberately not raised: `README.md:196` and
`docs/workflow.md:101` describe step 5 in the present indicative with no maturity
label, while nobody has ever observed it fire — formally the same state as AC-2.1.
I judged that labelling it would be wrong. The graph-gates criteria need labels
because they assert things about an **external tool's** behaviour; step 5 only
instructs an agent to say a sentence, whose risk is R1, the standing whole-product
risk that is not labelled per feature. Labelling here would be the check that
fires where it does not apply, which constitution §1 names as its own harm.

### 8.4 Fixed by the Reviewer in round 3

Four factual corrections to the fix pass's own edits. All are in records and docs;
no shipped skill, agent, template or tool file was touched.

- `.spark/graph-gates/evidence.md` (F4 sub-entry) — the sentence "joins the
  post-release checklist in §4" **asserted a record that does not exist**:
  `plan.md` §4's checklist still has five items and its *Ships not proven* table
  seven rows, neither mentioning a permission prompt. Reworded to say the leg is
  owed and *belongs* on that list as a sixth item, that it is **not** on it yet,
  and who found that. This is the one thing in the pass that reproduced the exact
  defect the pass existed to fix — an evidence file describing a state of the
  record rather than the record. **Still owed:** the sixth checklist item in
  `plan.md` §4, which I may not edit.
- `README.md:240` — the table's lead-in said every unproven criterion "needs a run
  of the *installed* plugin **in a repo with a built graph**", contradicting its own
  first row: AC-1.1 needs a run in a repo **without** one. Now split.
- `README.md:248` — the AC-2.5 row described the *hand-over* firing, which is
  AC-2.1's content and already its own row; AC-2.5's actual requirement (the report
  names which results scoped its reading, and which locations it read as a
  consequence) went unstated. A reader working the post-release checklist would
  have verified AC-2.1 twice and AC-2.5 never. Corrected to AC-2.5's own text.
- `README.md:250` — the AC-3.1 clause read "that an agent treats an answer as a map
  not a verdict", which is AC-3.6's wording; AC-3.1's bar is a finding anchored at a
  concrete `file:line` with the code behind it. Tightened.

Re-verified after: `wc -l tools/aspark-graph.md` 150, `gate_health` 1, product name
0 in `agents/`/`templates/`/`lenses/`, 10 / 7, step counts unchanged,
`claude plugin validate .` passes.

### 8.5 On this report's own length

495 lines against `templates/review-report.md`'s ~150 — that is F17, accepted, and
I will not pretend it is fine. Asked directly: **yes, a two-round report at 3×
budget is itself a reason the next feature should split its review.** Not because
the prose is padded — §7 is tables — but because the cause is structural and will
recur. Three rounds of findings, their re-derivations and two gate rulings live in
one file, and the review report is read at the gate, again in fix-mode and again at
re-review, so every round pays for every earlier round's text. Two cheap
structural answers, either of which would have held this report near budget:
decide in the template that the budget is **per round**, or give each re-review its
own file (`review-2.md`) with the earlier one linked. The second also fixes a
latent hazard I checked here: this file now contains two `## …Findings`-matching
headings and two gate checklists, and the sibling repo's parser takes the *first*
`##` section whose heading contains "findings" — so round 1's table is what a graph
would report as this feature's findings, indefinitely. It works today by accident of
ordering, not by design. Worth one line in the template.

### 8.6 Ruling

**Passed.** The fix pass did the harder of the two available things. F10 could have
been closed with a waiver in one sentence; instead the reasoning was written down
in four places, and the one thing I would have rejected — narrowing AC-1.2 and
calling the finding gone — is not what happened: the deviation is recorded as D6,
the criterion's narrowing is argued on the story's own "so that" clause and
authorised by the user in a dated clarification, and the behaviour is now
documented for users in `README.md` and for maintainers in `docs/workflow.md`. I
tested the narrowing against the risk it might have quietly shrunk, R2, and it does
not: the three ceremonies that carry a probe are all still bound, and the seven it
releases contain no probe and no mention of the tool. D6 goes further than it had
to by correcting the *reason* §2 gave for NFR-2 rather than just the fact, and by
naming the detection gap — `/spark` was never baselined — instead of quietly
adding a baseline after the fact, which could not have proven anything anyway. The
evidence corrections reproduce exactly, the supersession labelling annotates
history rather than overwriting it, and the AC-5.3 check survives a stricter
version of itself than the one recorded. What the pass got wrong is small and of
one kind: four statements about the record that were not quite true — an evidence
sentence claiming a checklist item that was never added, and three AC descriptions
in the README's new table that would have sent someone verifying the wrong thing.
I fixed all four and left F18 open, because an edited file still missing from
*Affected Components* one round after that pattern produced a Major is worth
carrying visibly rather than closing quietly. Five Minors ship open and named,
none of them a defect in shipped behaviour. The gate closes on all six boxes and
the feature may go to `/demo-day`.

### Owed items closed after round 3 (2026-07-26)

Round 3 named three record gaps in files it was barred from editing. Closed by the
orchestrator; none touches shipped material, and none was gate-holding.

| Item | Where | What was done |
|---|---|---|
| SPEC GATE predates the text it approves | `spec.md`, last gate box | The box now records the C13 narrowing of AC-1.2 as authorised 2026-07-26, alongside the 2026-07-25 approval, and says why both dates appear |
| F4's leg claimed a checklist entry that did not exist | `plan.md` §4, unproven table | Added as **item 6**, stating what cannot be attested from inside a session and naming that the fix pass first claimed it was already there. This was the one place the fix pass reproduced the defect it existed to fix — recorded rather than quietly corrected |
| **F18** — edited files missing from *Affected Components* | `plan.md` §2 | `docs/workflow.md` added as a row; the `README.md` row extended to cover the F14 table and the clean-handoff paragraph. The row notes this is the same gap that produced F10 one round earlier |
