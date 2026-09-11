# Spec: metrics-script-removal

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-09-11 |
| **Ticket** | `none` |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). **Approved by the user at the spec gate, 2026-09-11**, together with the ruling that the library lens's *Packaging & footprint* section applies to this feature (§5 note accepted; `/charter` to revisit §2's N/A as a follow-up). Next ceremony step: `/sprint-plan`.
- **Summary:** The repo tracks a 32 KB Python counter that its own §3 forbids and that the next release ships to every consumer. Remove it; replace README's headline figure with a claim that does not rot; keep every published figure *checkable* from the committed reports while stating plainly that they are no longer *refreshable*.
- **Open:** `none` — A1–A5 and C1–C9 resolved; A6/A9 resolve as verified-downstream, named as such. **Note on C8/C9's authority:** both are `/peer-review` findings (F3, F14) corrected by `/increment` fix-mode against the factual record — neither required inventing a requirement or changing scope, and both are the kind of "small, obvious correction" fix-mode is authorised to make directly. Neither carries an explicit fresh user re-approval of the gate the way the constitution's A8 does; flagged here for the user to ratify or reopen, rather than silently presented as equivalent to A8's authority.
- **Binding ruling:** §4 User Stories (US-1…US-7); §6 Out of Scope holds three rulings (the `.docx.bak`: not a story; the `/go-live` pre-flight: next feature, scoped to the GitHub path; the `aspark-insights` port: follow-up with a stated precondition). §7 logs what changed and why.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Problem & Goal

- **Problem.** `scripts/spark-metrics.py` (32,654 B, executable bit set, **tracked**) sits in a repo published as a plugin. Two people hurt, neither of them today's README reader:
  1. **The next consumer who installs aSPARK** — they asked for Markdown prompt material from a plugin whose README and constitution both say "no executable code", and the next release hands them an executable Python file they did not ask for (§6: nothing is installed on the user's behalf unasked). The script is tracked, so it reaches a consumer by either install path. The cache installed today predates it, so this is a *pending* breach — which is exactly the window to close it.
  2. **The sole maintainer** — §3's first technical constraint is falsified by the repo that states it, and the constitution carries a "ruled for removal" paragraph that only a deletion can close. A ruling that never lands teaches the next agent that rulings are decorative.
- **The part that is not a chore.** Four documents instruct readers to run the script, and the project's only quantitative honesty evidence (54 features / 10 projects, 2026-09-09) is attributed to it. Deletion without repair turns all four into §1 honesty defects. The load-bearing asymmetry, tested before this spec was written rather than assumed:
  - **Checkable survives.** Every headline figure is reproducible from the two committed `schema: 2` reports alone — they carry `projects[].id`, per-project `features[].key` and a `reached` map, plus `git.tags/added/deleted`, `transcripts.*` and `days[]`. A set union plus a few sums gets 10 / 54 / 54-53-52-41-48 / 429 / 377 exactly. §3's assertion ("reproducible from the committed reports, not from a script shipped here") is **true**.
  - **Refreshable dies.** `--write-report` is the only producer of a report. After deletion no machine can generate one, so the figures are frozen at 2026-09-09 — permanently checkable, never again current. `docs/reports/README.md`'s "Add yours" workflow and "rerun whenever the figure should be refreshed" become impossible.
  - **Reader-runnable dies outright.** "Count your own with `python3 scripts/spark-metrics.py --totals-only`" invited a reader to measure *their own* projects. No rewording preserves it, and no external home carries the tool today (C3), so the invitation is dropped rather than redirected.
- **Goal.** Nothing in the published tree is executable; README's §Project Status leads with a claim that stays true as time passes, with the numeric snapshot kept below it as dated evidence; and every statement the repo makes about its figures is performable by a stranger.
- **Success signal.** (a) `git ls-files '*.py'` and a listing of the refreshed install both print nothing; (b) a stranger reproduces **all fourteen** published figures from `docs/reports/*.json` following only what `docs/metrics.md` prints, with no step of their own — or any that fails is relabelled and recorded as a finding; (c) no sentence in §Project Status outside the dated evidence block contains a count, so none of it rots.
- **Why now.** The breach activates at the next release, whichever feature that is. The same `/charter` session that ruled this closed the handbook honesty exception; leaving a second open exception behind reproduces the staleness that session paid to fix.

## 2. Target Users

- **A developer installing aSPARK** — inherits the tracked tree; has no include/exclude to protect them.
- **A reader evaluating the dogfooding claim** (README §Project Status) — wants to check the numbers without trusting the author, and needs a method they can perform.
- **The sole maintainer (`a-lottes`)** — owns the constitution this repo violates and pays the interest on every stale exception.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The figures freeze permanently: after this, the dogfooding figure can never be refreshed from within this repo, so a dated snapshot would age against §4's "this README always reflects the current state" bar | **resolved (user, 2026-09-11)** — replace the headline with a non-rotting claim, keep the table below as dated evidence. US-7, C1 |
| A2 | Venue of the constitution edits — §3 pre-authorises deleting its own paragraph, but the preamble, §2's `cli` row and §8's inventory are not pre-authorised, and normally only `/charter` amends the constitution | **resolved (user, 2026-09-11)** — all four land in this PR; the repo is never in a state where the constitution describes a script that is not there. Recorded deviation: see A8. US-4, C2 |
| A3 | Six published figures were unverified as reproducible (tags 61; +114,630/−12,589 lines; 42 of 114 sessions; 51 active days; 116 ceremonies) | **resolved (user, 2026-09-11)** — derive all six; relabel or drop any that fails **and** record it as a finding (`refuted-with-finding` is a valid outcome, project `CLAUDE.md`). AC-2.4, AC-2.5, C5 |
| A4 | `transcripts.root` holds absolute home paths in both committed reports while `docs/reports/README.md:27` claims "no hostname, no path" | **resolved (user, 2026-09-11)** — strip the field and correct the text. This edits committed evidence deliberately: the reports become the project's sole evidence here, §6's test is *presence in the working tree at release*, and no published figure reads the field (re-verified). US-5, C4 |
| A5 | Whether the installed plugin can be refreshed from the branch before merge, so AC-1.3 is evidence rather than a stale tautology | **resolved (from disk)** — `known_marketplaces.json` registers `aspark` as `{"source":"directory","path":"/Users/andreaslottes/aSPARK"}`; `installed_plugins.json` pins `aspark@aspark` at `gitCommitSha 9c47bc95…` (`v0.8.0`). A local directory install can be refreshed pre-merge, so AC-1.3 runs at `/demo-day`. C6 |
| A6 | The script is **not part of the consumed contract** — nothing under `skills/`, `agents/`, `templates/`, `lenses/`, `tools/`, `.claude-plugin/` references it, so removal is not breaking (§6) | verified downstream by AC-1.4, which runs **before** the deletion commit |
| A7 | The idea arrived as a solution ("remove the script and repair every document that depends on it"). The underlying need, against which scope is judged: *the published tree must match what the repo claims to ship, and its figures must stay checkable* | recorded |
| A8 | **Recorded deviation:** this feature edits `.spark/constitution.md`, which §1 and `/charter` otherwise reserve to the user's own ceremony. Authority is the user's ruling of 2026-09-11 (A2) plus §3's own instruction to delete the paragraph when the deletion lands. Flagged here so `/peer-review` reads it as authorised, not as a finding | accepted, authority named |
| A9 | **Consumer exposure of ignored files is unverified and probably nil.** Five `.gitignore`-matched artifacts are present in the installed cache (`docs/…docx.bak` 1.9 MB, `.DS_Store`, `.claude/settings.local.json`, `.aspark-graph/{graph,parse-cache}.json`) — but that cache is a *local directory* install that copied this working tree. The GitHub path clones, and a clone carries tracked files only. So this is a confirmed **dev-surface** leak, not a confirmed consumer leak | accepted as a stated unknown; AC-1.5 narrows it, the follow-up in §6 owns it. Nothing in this spec asserts consumer exposure. C7 |

## 4. User Stories

### US-1 (Must): The script leaves the published tree

> As a developer installing aSPARK, I want the plugin to contain no executable file, so that installing Markdown prompt material does not put a 32 KB Python program in my plugin cache unasked.

**Acceptance criteria:**

- [ ] AC-1.1: Given the feature branch checked out, when `git ls-files '*.py'; ls scripts` is run at the repo root, then the first prints nothing and the second reports that `scripts` does not exist (the directory is removed, not emptied).
- [ ] AC-1.2: Given the branch, when `grep -rn 'python3 scripts/' --include='*.md' . | grep -v '/\.spark/'` is run, then it prints nothing.
- [ ] AC-1.3: Given the local directory install refreshed from this branch (A5), when the install path under `~/.claude/plugins/cache/aspark/aspark/` is listed with `find … -name '*.py'`, then it prints nothing — and the listing is taken *after* the refresh, shown by the install's recorded commit matching the branch head.
- [ ] AC-1.4: Given the branch **before** the deletion commit, when `grep -rln 'spark-metrics' skills agents templates lenses tools .claude-plugin` is run, then it prints nothing — the §4 negative case: no ceremony invokes the script, so no ceremony changes behaviour.
- [ ] AC-1.5: Given the branch pushed to `origin`, when it is cloned fresh into a throwaway directory and that clone is listed, then no `.py` and none of A9's five ignored artifacts are present. This settles what a *clone* carries; it does **not** claim to prove what a marketplace install from GitHub carries — that question is named in §6.

### US-2 (Must): Every published figure stays checkable without the script

> As a reader evaluating the dogfooding claim, I want a method I can perform on the committed reports, so that the numbers remain checkable after the tool that produced them is gone.

**Acceptance criteria:**

- [ ] AC-2.1: Given only `docs/reports/*.json` and the method as printed in `docs/metrics.md`, when a QA tester performs it (with `jq` or an untracked scratch script per §3/§5), then the observed output equals 10 projects, 54 features, Spec 54, Plan 53, Review 52, QA 41, Release 48, 429 role-agent runs, 377 human gate decisions.
- [ ] AC-2.2: Given that method, when the tester executes it **literally, supplying no step of their own**, then it runs to completion without error — every field name (`projects[].id`, `features[].key`, `reached.*`, `transcripts.agent_runs_total`, `transcripts.gates`) and every combination rule (union on ids, OR on `reached`, sum on transcript counts) it needs is printed in the doc. A step the tester has to invent fails this AC.
- [ ] AC-2.3: Given the rewritten §Project Status, when its provenance sentence is followed, then it dates the snapshot, names `docs/reports/` as the evidence, names the commit from which the removed script can be recovered, and `git show <that-commit>:scripts/spark-metrics.py | head -1` succeeds — and `grep -n '\-\-merge' README.md` prints nothing.
- [ ] AC-2.4: Given `docs/reports/*.json` only, when the remaining five published figures are derived (lines +114,630/−12,589; 42 of 114 sessions; 51 active days; 116 ceremonies; tags per AC-2.5) with an untracked scratch script whose **output alone** is committed as this feature's evidence, then each value is either reproduced exactly with the rule that reproduces it printed in `docs/metrics.md`, or corrected/dropped in the docs **and** recorded as a finding carrying the observed value.
- [ ] AC-2.5: Given the published `61` git tags against the naive machine sum `52 + 27 = 79`, when the per-project `git.tags` values are combined under the dedup rule stated in `docs/metrics.md`, then the result is exactly 61; if no stated rule yields 61, the figure is corrected in `README.md` and `docs/metrics.md` and the discrepancy recorded as a finding. A documented refutation passes this AC; publishing 61 with a caveat does not.

### US-3 (Must): No document promises a capability that no longer exists

> As a maintainer, I want every instruction that depended on the script removed rather than reworded, so that no reader is sent after a tool this repo does not have (§1: presenting an intention as delivered is a defect).

**Acceptance criteria:**

- [ ] AC-3.1: Given the branch, when `grep -rn 'write-report\|Add yours\|should be refreshed\|Count your own' README.md docs/metrics.md docs/reports/README.md` is run, then it prints nothing.
- [ ] AC-3.2: Given `docs/reports/README.md`, when a reader looks for how to contribute a report, then the file states the directory is a closed 2026-09-09 snapshot and that this repo contains no tool to produce another — verified by the absence in AC-3.1 plus the snapshot statement standing in the paragraph that once held the workflow.
- [ ] AC-3.3: Given `docs/metrics.md`, when the flag table and the cross-machine transport workflow are looked for, then both are absent (`grep -c '^| \`--' docs/metrics.md` returns 0) and the remaining method text is the hand-checkable method of AC-2.1/AC-2.4, not a description of a program.
- [ ] AC-3.4: Given the branch, when `grep -rn 'aspark-insights\|aSPARK-insights' README.md docs/metrics.md` is run, then no hit presents that repo as a place to get this counter (C3: the tool is not there today, so such a pointer would be a false claim under §3).

### US-4 (Must): No document names the script as existing

> As the constitution's owner, I want the removal reflected in every document that asserts the script's existence, in the same PR, so that closing one honesty defect does not open four more.

**Acceptance criteria:**

- [ ] AC-4.1: Given the repo at the moment this feature's PR is opened, when `grep -rn 'spark-metrics' . --include='*.md' | grep -v '/\.spark/[a-z-]*/'` is run, then the only hits are past-tense provenance statements (AC-2.3), and `grep -n 'spark-metrics' .spark/constitution.md` prints nothing.
- [ ] AC-4.2: Given the constitution's §8 inventory, when `git ls-files | wc -l`, `git ls-files '*.md' | wc -l` and `git ls-files '*.py' | wc -l` are run, then each printed number equals the number §8 states, and the `.py` count is 0.
- [ ] AC-4.3: Given the preamble and the §2 `cli` row, when compared against AC-4.2's output, then neither cites a script as an existing exception, the preamble's "no executable code" claim holds without qualification, and §3's known-open-exception paragraph is gone with the rest of §3 unchanged.
- [ ] AC-4.4: Given the constitution's Amendments table, when its newest row is read, then it records this deletion and cites the user's 2026-09-11 ruling as the authority for editing the constitution outside `/charter` (A8).

### US-5 (Must): The reports' description of themselves is true

> As a reader, I want `docs/reports/` to contain exactly what its README says it contains, so that the evidence this project now rests on entirely does not misdescribe itself — and so that no username ships in a public repo.

**Acceptance criteria:**

- [ ] AC-5.1: Given the branch, when `grep -rn '/Users/' docs/` is run, then it prints nothing.
- [ ] AC-5.2: Given that edit, when AC-2.1 and AC-2.4 are re-performed, then every figure is unchanged — no published number depended on the removed field.
- [ ] AC-5.3: Given `docs/reports/README.md`, when its "what is in a report" paragraph is tested against the files by `grep -rn '"root"\|/Users/\|hostname' docs/reports/*.json`, then the grep is empty and the paragraph's claim is therefore true as written.

### US-6 (Could): Roadmap bookkeeping follows reality

> As the maintainer, I want `ROADMAP.md` to stop listing a finished item and to name this work, so that *Next* is a plan rather than a log.

**Acceptance criteria:**

- [ ] AC-6.1: Given `ROADMAP.md` on the branch, when `grep -n 'handbook honesty exception' ROADMAP.md` is run, then no hit falls under `## Next`, and the script removal appears under `## Next` before release and `## Shipped` at `/go-live`.

### US-7 (Must): The README's headline claim does not rot

> As a reader, I want §Project Status to lead with a statement that is still true next month, so that the project's honesty bar does not depend on someone remembering to re-run a tool that no longer exists.

**Acceptance criteria:**

- [ ] AC-7.1: Given the rewritten §Project Status, when `grep -n '^\*\*54 features' README.md` is run, then it prints nothing — the numeric figure is no longer the headline.
- [ ] AC-7.2: Given that section, when the numeric table is located, then it is still present and the block containing it carries a date and the word `evidence` (or equivalent) in the same paragraph — verified by `grep -n -A4 '#### Snapshot' README.md` showing the dated heading, a line carrying both a date and `evidence`, and the table, all inside four lines of each other.
- [ ] AC-7.3: Given every sentence in §Project Status **outside** that dated block, when each is checked for a count of projects, features, runs or days, then none contains one — so no sentence there requires editing as time passes. A single undated count falsifies this AC.
- [ ] AC-7.4: Given the new headline claim, when a stranger performs the check it implies (AC-2.1), then the claim holds — the headline asserts only what `docs/reports/` contains and that anyone can recount it.

## 5. Non-Functional Requirements

Constitution §4's bars are inherited, not restated: no test suite exists, so the evidence is `claude plugin validate` plus a documented run, negative case first (NFR-7).

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Library lens §1 — public surface | The consumed contract is untouched: `git diff --name-status main` shows no add, rename or delete under `skills/`, `agents/`, `lenses/`, `templates/`, `tools/`, `.claude-plugin/`; changes are confined to `README.md`, `ROADMAP.md`, `docs/**`, `.spark/**` and the deletion of `scripts/` | /peer-review |
| NFR-2 | Library lens §2 — compatibility & versioning | The removal is **not breaking**: AC-1.4 shows zero references from the contract surface, so no deprecation path is owed and the release is a minor/patch bump, never major. No protected template structure (§3) is touched — the diff includes no file under `templates/` | /peer-review |
| NFR-3 | Library lens §3 — packaging & footprint (**applies; §2's N/A is wrong for this feature**) | The **tracked** tree — what a clone and therefore a consumer receives — contains zero executable files and requires zero interpreters (AC-1.1, AC-1.5). The net tracked footprint does **not** drop: `git ls-tree -r --format='%(objectsize)'` summed over `main` vs. this branch shows a net *increase* — the 32,654 B script leaves, and this feature's own `.spark/` evidence (spec, plan, evidence, review — Markdown documenting the removal) outweighs it by a wide margin. That is the correct trade for a feature whose entire claim is auditability, not a defect: the bytes that replace the script are proof, not bloat, and a reader can verify the exact delta with the command above rather than trust this row. Separately, five `.gitignore`-matched artifacts are present in the *local directory* install; that is a confirmed dev-surface leak whose consumer reach is **unverified and probably nil** (A9) and is not asserted anywhere in this spec or in any document it changes | /demo-day + /peer-review |
| NFR-4 | Library lens §4 — contract clarity | Every command printed in a changed document is runnable exactly as printed and was observed to run during QA; no printed command names a file the repo does not contain | /demo-day |
| NFR-5 | Honesty (§1) | All fourteen figures published in §Project Status and `docs/metrics.md` are derived live from `docs/reports/*.json` during this feature; any that cannot be reproduced is corrected or dropped **and** recorded as a finding — never restated unchanged, and never published with a caveat in place of a rule | /demo-day + /peer-review |
| NFR-6 | Security & privacy (§6) | No absolute path, username or hostname remains in any committed file under `docs/` — `grep -rn '/Users/' docs/` prints nothing. §6's test is presence at release, not tracking | /peer-review |
| NFR-7 | Reliability / testing (§4) | `claude plugin validate` passes on the branch; the negative case (AC-1.4) is run and written down **before** the deletion commit; every derivation script stays untracked with only its output committed (§3/§5) | /peer-review |
| NFR-8 | Performance, accessibility, observability | N/A — no UI, no runtime, nothing to log; this change removes the repo's only process | — |

**Note on lens §3.** Constitution §2 marks the library lens's *Packaging & footprint* section N/A ("no bundle, no dependencies"). For this feature that call is wrong and I do not treat it as binding: with `"source": "./"` and no include/exclude, the shipped artifact is the tree, so footprint is this repo's most concrete question — it is *why* this feature exists. Recommend `/charter` revisit §2's N/A; flagged, not silently overridden. **Accepted by the user at the spec gate, 2026-09-11** — NFR-3 stands as written and the `/charter` revisit is a follow-up, not a blocker.

## 6. Out of Scope

- **`docs/…Handbook.docx.bak` (1.9 MB, untracked) — not a story here.** (a) It is one of five `.gitignore`-matched artifacts in the local install, so removing one closes an audit line without closing the hole. (b) Being untracked, its removal produces **no diff** — nothing for `/peer-review` to review, nothing a PR can carry, no AC QA can verify from the branch. It is a maintainer `rm`; the *assertion* is what needs a feature.
- **A `/go-live` pre-flight asserting what an install actually ships — next feature, and scoped to the right question.** It must assert what a **GitHub marketplace install** ships, not what a local directory copy ships: those differ (A9), and a pre-flight built on the local-copy observation would inherit an overstatement. It changes a shipped skill, a different risk class from deleting maintainer tooling, and folding it in would make this PR's honesty-repair claim unreviewable on its own.
- **Porting the counter to `aSPARK-insights`** (`git@github.com:a-lottes/aSPARK-insights.git`, public, ships `aspark_insights`) — a worthwhile follow-up, explicitly *not* this feature's. Honest precondition: README may point there **only once the counter actually lands there**; today the repo contains no `spark-metrics` reference, so a pointer would be a false claim under §3. Enforced negatively by AC-3.4.
- **Any in-repo replacement for refreshing the figures** — no script, no CI, no automation. The loss recorded in A1 is accepted; US-7 is the mitigation, not a restoration.
- **Re-deriving the 2026-09-09 measurements.** The reports stay as the evidence; only the stated method, provenance and framing change. A figure the reports contradict is corrected (AC-2.4/AC-2.5), which is not the same as re-measuring.
- **Rewriting historical `.spark/<feature>/` artifacts.** Immutable records (the `lean-rounds` precedent: an artifact is overwritten only in place by its own ceremony, never retro-edited by a later feature). `.spark/constitution.md` is the sole exception, authorised in A8.
- **Branch protection, the template-contract handshake, the two `aspark-graph` consumer defects** — named in the constitution, none of them this feature's.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-11 | Accept a figure frozen at 2026-09-09, or replace the README headline with a claim that stays true? | **Replace the headline** (user). Numeric table retained below it as dated evidence → new US-7; §1 Goal and Success signal rewritten |
| C2 | 2026-09-11 | Constitution edits — this PR, or a `/charter` run before merge? | **All four in this PR** (user). US-4 gains AC-4.4; the ceremony-ownership deviation recorded as A8 so `/peer-review` sees it as authorised |
| C3 | 2026-09-11 | Drop "Count your own", or point at an external home — and does that home exist today? | **Drop it.** `aSPARK-insights` exists and is public, but contains no `spark-metrics` reference, so a pointer would be false under §3 → negative AC-3.4; the port moved to §6 with its precondition |
| C4 | 2026-09-11 | `transcripts.root`: strip the field, correct the text, or both? | **Both** (user). US-5 raised from Should to **Must** — a false privacy claim in what is now the sole evidence belongs in this diff; AC-5.3 added. No figure reads the field (re-verified) |
| C5 | 2026-09-11 | Reproduce all six unverified figures, or let them carry a provenance note? | **Reproduce all six; relabel what fails and record it as a finding** (user) → AC-2.4, AC-2.5, NFR-5 tightened to "never published with a caveat in place of a rule". Derivation runs as untracked scratch, output committed (§3/§5) |
| C6 | 2026-09-11 | Is the installed plugin refreshable pre-merge, so AC-1.3 is evidence? | **Yes** — it is a local *directory* install (A5), so AC-1.3 runs at `/demo-day`, not deferred to `/go-live` |
| C7 | 2026-09-11 | Does the `.gitignore`-matched leak actually reach consumers, as the first draft implied? | **Unverified and probably nil** — the observed cache is a local directory copy; the GitHub path clones, and a clone carries tracked files only. NFR-3 and §1 reworded to claim only the dev-surface leak; A9 records the unknown; AC-1.5 narrows it; the follow-up in §6 re-scoped to the GitHub path |
| C8 | 2026-09-11 | `/peer-review` round 1 (F3, Major): NFR-3 claimed the tracked footprint *drops* 32,654 B. Does it? | **No — it is a net increase.** `git ls-tree` blob sums show the feature's own `.spark/` evidence outweighs the removed script. **NFR-3 reworded** to state the correct direction and frame the growth as the feature's intended evidence, not a defect |
| C9 | 2026-09-11 | `/peer-review` round 2 (F14, Minor): AC-2.3 and AC-7.2 hardcoded `2026-09-09` as literal text — F1's rebase moved the snapshot to `2026-09-10`, so both ACs' own wording was wrong, and AC-7.2's embedded verification command printed nothing. | **Both generalised.** AC-2.3 now says "dates the snapshot" without naming one; AC-7.2's command anchors on the `#### Snapshot` heading text instead of a date string, so neither can go stale the same way again |

## 8. Design Review

*N/A — see SPEC GATE.*

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C7 all resolved at the spec gate; C8/C9 added post-approval from `/peer-review` findings, both resolved the same round they were raised
- [x] Open questions are resolved or explicitly accepted as risk — A1–A5 resolved; A6 verified by AC-1.4 before the deletion commit; A7 recorded; A8 authorised; A9 accepted as a stated unknown and routed to §6
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution respected; two deviations are stated rather than hidden — the constitution edit (A8, user's 2026-09-11 ruling) and the library lens §3 call (§5 note, routed to `/charter`)
- [x] Design review N/A — project type `library`, constitution §8 `Browser-observable surface: no`; this change ships no UI and no browser-observable surface, so `/look-and-feel` has nothing to review
- [x] Line budget respected: Ist 189 / Soll ~250 (excluding HTML comments; +2 from C8/C9, both post-approval `/peer-review` corrections)
- [x] Status set to `approved` by the user — **approved 2026-09-11**, after the gate was walked box by box; the library lens §3 deviation (§5 note) was put to the user and accepted, and A9 was accepted as a stated unknown rather than answered first
