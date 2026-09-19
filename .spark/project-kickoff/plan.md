# Plan: project-kickoff

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/project-kickoff/spec.md` (must be `approved`) |
| **Status** | `approved` |
| **Date** | 2026-09-18 |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this plan updates it in the same edit that changes a task's status or
     the plan's own status: overwrite in place, never append. The block holds one
     current state, never a per-round log; a stale block is a defect, not a cosmetic
     issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `approved` — user approved the PLAN GATE 2026-09-18 after walking every row.
- **Summary:** Project Context ships as a **numbered §9** appended after §8 in `templates/constitution.md`; the kickoff questions are stated **once, at project scope, in `agents/facilitator.md`** (the PO's per-feature list is cited, never copied); one evidence-graded flow serves both repo states inside `/charter`'s existing steps 1–3. **A10 ruled: both `Should` paths ship; if only one fits, US-4 (brownfield) first** — §1.
- **Open:** `none` — all 13 tasks `done` 2026-09-18. `.spark/project-kickoff/evidence.md` holds 10 dated, quoted entries: the syntax gate, five negative-case runs, the brownfield dogfood (a real constitution amendment on this repo), the greenfield dogfood (a real constitution written on a scratch repo), and the closing surface/weight/deferral audit. AC-5.4/S3 recorded `deferred` — it measures the next feature, not this one — with no pass/fail claimed. One risk materialized for real (§9's line caps vs. real evidence, Entry 8) and was resolved by the plan's own named mitigation (compression), not a quiet breach.
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

<!-- Budget: ~300 lines. -->

## 1. Architecture Decision

- **Context:** Everything this feature ships is prompt material — one new template
  section plus wording inside eight existing Markdown files. There is no runtime,
  no build and no test suite (constitution §3, §4), so the only architecture levers
  are *where a fact is stated* and *who reads it*. Three constraints bite at once:
  NFR-1 pins the public surface (zero new files, `/charter` stays at 5 steps),
  AC-2.1 freezes §1–§8's numbering because `skills/spark/SKILL.md:74` and
  `skills/demo-day/SKILL.md:28` resolve "§8" by number, and NFR-3 requires the
  kickoff questions and the PO's per-feature forcing questions to live in exactly
  one file each. Constitution §3's pattern *"a new concern is a new file, not an
  edit to the roles"* does **not** bind here: it governs optional capabilities that
  skills load generically (`lenses/<name>.md`, a future capability directory).
  Project Context is a section of an existing document whose sole writer is an
  existing ceremony — the roles are exactly where it belongs, and NFR-1 forbids the
  new file anyway. Recorded as a deliberate, bounded deviation, not an oversight.
- **Decision:** Four rulings.
  1. **Placement — numbered `## 9. Project Context`, appended after §8, before the
     `---`/Amendments block.** Numbered, because AC-5.1 makes the PO and EM cite it
     as `constitution.md §<n>` and AC-2.5 makes a contradicting phase point at it;
     an unnumbered block has no citable anchor. Appended, because §1–§8 then keep
     their numbers byte-for-byte. Its inline HTML comment carries the four contract
     facts NFR-3 demands: default when absent (every reader behaves exactly as today),
     sole writer (`/charter`), the 35/12/25 caps, and what it is not (not a design
     doc, not per-feature, never refreshed automatically).
  2. **Questions — one project-scope list, stated once in `agents/facilitator.md`.**
     The seven AC-3.1 questions are written there in project-level wording; the
     Facilitator *cites* `agents/product-owner.md` §The Interrogation in one
     sentence as the per-feature list it is deliberately not repeating. No copy, no
     cross-file read, no new role — the Facilitator borrows the shape, not the
     persona (C6).
  3. **One evidence-graded flow, no mode step.** A single drafting rule inside the
     Facilitator's existing steps 1 and 3: fill every entry the evidence supports,
     return the rest as numbered questions through `/charter`'s existing step-2
     relay, mark each entry `inferred from <file:line>` / `asked` / `not stated`,
     and record `greenfield` or `brownfield` as a label only (A7, §6 item 2).
     Brownfield and greenfield are the two ends of that one rule, not two branches.
     `/charter` step 1 hands the Facilitator a read-only git-history summary it
     gathered itself, exactly as `skills/next-steps/SKILL.md:28-30` already does —
     the Facilitator keeps `tools: Read, Grep, Glob, Write, Edit` and gains no Bash
     (A4, constitution §6).
  4. **A10 / C9 — both `Should` paths ship in this increment; the cut order, if the
     increment has to shed one, is US-3 (greenfield) out, US-4 (brownfield) in.**
     Both paths are the same drafting rule seen from two ends, so the marginal diff
     cost of the second is a paragraph, not a subsystem; what actually costs is the
     performed run each needs (NFR-5), and those are separable — which is exactly
     what makes a cut possible without redesigning anything. US-4 ranks first for
     three reasons: it is the only path that produces a Project Context **in this
     repo** (AC-4.5), which is the precondition for US-5's measurement (AC-5.4/S3);
     constitution §1 validates a loop change by running the loop, and this repo is
     the only *measured* venue (A2) while the greenfield venue is an unmeasured
     scratch repo; and without US-3 an empty repo still gets asked — ruling 3's rule
     degrades to "ask everything", just unbounded — whereas without US-4 brownfield
     discovery stays the unevidenced "learn the terrain" that spec §1 problem 3
     names as the defect.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Unnumbered preamble above §1, mirroring this repo's improvised paragraph (`.spark/constitution.md:15-19`) | Not citable as `constitution.md §<n>`, which AC-5.1 requires of both reading agents and AC-2.5 of every other phase. The improvised original *is* the failure mode's evidence: no caps, no evidence markers, never amended — copying its shape institutionalises the drift |
  | Insert as §1 and renumber §1–§8 → §2–§9 | Breaks `skills/spark/SKILL.md:74` and `skills/demo-day/SKILL.md:28`, which resolve "§8" by number — a silent breaking change to the consumed contract (constitution §6) and a direct AC-2.1 violation. Read-order is solved by instructing the readers, not by moving the section |
  | Facilitator resolves `${CLAUDE_PLUGIN_ROOT}/agents/product-owner.md` and reads the forcing questions from there | Adds a `${CLAUDE_PLUGIN_ROOT}/…` path that NFR-1 pins at zero new; couples project kickoff to a list that is wrong at project scope (Q6 "what does this displace" has no answer before any feature exists); and makes the Facilitator run the PO's interrogation, which C6 rejects |
  | Inline copy of the six forcing questions into `agents/facilitator.md` | Two copies of one list drift apart within a release. NFR-3's own test — grep the literal first question, get one file — fails by construction |
  | New shared `agents/questions.md` or a `lenses/`-style include | A new tracked file on a surface NFR-1 pins at 10 skills / 7 agents / 8 lenses / 6 templates, and a new path something must resolve. Constitution §3's "new concern is a new file" governs generically-loaded capabilities, not a section of an existing document |
  | Mode detection as its own step with a signal rule (no source / no manifest / trivial history) | Cut by the spec (§6 item 2, A7) and it would be `/charter`'s 6th numbered step, which NFR-1 forbids. Ruling 3 gets the same outcome from evidence grading |
  | Give the Facilitator Bash so it gathers git history itself | Constitution §6 (nothing executed unasked) and A4; `/next-steps` step 1 already shows the ceremony-gathers-it pattern this repo uses |
  | Ship US-3 (greenfield) first and defer US-4 | Leaves this repo without a Project Context, so US-5 is unprovable, AC-4.5 unwritten and the only measured venue untouched — see ruling 4 |
- **Consequences:** *Easier:* one `git diff` on `templates/constitution.md` answers
  AC-2.1; `constitution.md §9` becomes a stable citation target for every later
  phase; the two dogfood paths are independently cuttable, so a scope emergency has
  a pre-decided answer. *Harder:* the Facilitator's prompt grows in the same step
  that already carries profile, lens and QA-method drafting — agent attention is
  this repo's real cost (constitution §4), so the caps have to be enforced in the
  template comment, not only in the agent. Appending §9 also puts it *below* §8,
  so read-order depends entirely on the PO/EM instruction landing (T11). And the
  brownfield dogfood mutates this repo's own constitution mid-increment, which
  makes the negative case unrepeatable after T8 — hence the hard ordering below.

## 2. Affected Components

**Graph grounding — `impact` was run and returned a structural empty.** The Plan
slice's order was followed: the tasks below were cut **with** their `files:` notes
first, then the blast radius of the union of those eleven paths was queried against
the built graph (`runner=yes`, `graph=yes`, probed 2026-09-18):
`aspark-graph query impact <the 11 paths> --repo .` → `found: true`, `files: []`,
`affected_stories: []`, `affected_acs: []`, and **all eleven paths listed under
`unknown_files`** (run 2026-09-18). Read correctly, that is the graph saying *"I do
not index these"*, **not** *"nothing depends on them"*: it indexes only
`.py .ts .tsx .js .jsx .mjs .cjs .java .go .rs` (`tools/aspark-graph.md:93-95`) and
this repo is Markdown + JSON (constitution §3), so it holds no file node for any
path this feature touches. The empty story and AC lists carry the same meaning —
no indexed node exists for a `files:` note to reach — and neither list is
reassurance. **The blast radius below is therefore scoped by hand**, from the spec's
own `file:line` evidence and from reading each file named.

- `templates/constitution.md` — new §9 (T1). The one file in the plugin's protected
  `templates/` directory; **not** in constitution §3's protected-structure table, and
  no protected heading, column or ID pattern is touched (NFR-2 ⇒ minor bump).
- `agents/facilitator.md` — drafting rule, kickoff question list, discovery entries
  (T2, T7, T9). Largest single edit; no tools line change.
- `skills/charter/SKILL.md` — steps 1–3 only; step count stays 5 (T3, T7, T9).
- `skills/spark/SKILL.md` (`:25-29`, `:58-59`) and `skills/next-steps/SKILL.md`
  (`:48-50`) — routing to `/charter` (T4).
- `README.md` — Start-here block before §Usage (`:181-190`), §Project Status
  (`:285`) maturity rows (T5, T12); `ROADMAP.md` — maturity labels (T12).
- `agents/product-owner.md` (`:48-50`) and `agents/engineering-manager.md`
  (`:45-47`) — read §9 first, with the AC-5.2 conditions (T11).
- `.spark/constitution.md` — this repo's own, amended **by a performed `/charter`
  run**, never hand-edited (T8).
- `.spark/project-kickoff/evidence.md` — new artifact, the three runs (T6, T8, T10,
  T13).
- **External consumers:** `aspark-graph` and `aspark-guard` both re-verified as
  non-readers of `constitution.md` (spec A3/C8) — no coordinated release.
- **New dependencies:** none. No new package, service, file, command, agent, lens,
  template or `${CLAUDE_PLUGIN_ROOT}/…` path is introduced by any task.

## 3. Task Breakdown

<!-- Ordered; /increment works top to bottom. The negative case (T6) is a hard barrier:
     T8 mutates this repo's constitution and the negative case cannot be re-run after it. -->

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | **Walking skeleton (part 1).** Append `## 9. Project Context` to `templates/constitution.md` after §8, before the `---`/Amendments block: a `greenfield \| brownfield` label line, a **product brief** block (≤ 12 lines) and a **system picture** block (≤ 25 lines, omitted where the repo has no source files or manifest), each entry carrying `inferred from <file:line>` / `asked` / `confirmed by user` / `not stated` / `not found`. Inline HTML comment states the four contract facts: default when absent (every reader behaves exactly as today), sole writer `/charter`, the 35/12/25 caps, and what it is not (not a design doc, not per-feature, never auto-refreshed; a phase that finds it wrong records the contradiction where it works and points to `/charter`, never edits) | US-2 | AC-2.1, AC-2.3, AC-2.5, AC-2.6, NFR-1, NFR-2, NFR-3 | – | `done` | `git diff templates/constitution.md` shows exactly one added section and no changed line in §1–§8; `grep -n "^## " templates/constitution.md` lists §1–§8 with unchanged numbers and headings; the two by-number citations still resolve (`skills/spark/SKILL.md:74`, `skills/demo-day/SKILL.md:28` → "§8" = QA Method); no row of constitution §3's protected-structure table is touched; all four contract facts present in the comment — files: templates/constitution.md |
| T2 | **Walking skeleton (part 2).** `agents/facilitator.md`: one drafting rule inside existing steps 1 and 3 — fill every §9 entry the evidence supports, mark it `inferred from <file:line>`, return the unanswered ones as numbered questions via the existing STOP path, never guess (`not stated`/`not found` instead), record the `greenfield`/`brownfield` label, obey the 35/12/25 caps by pointing at README/`CLAUDE.md`/docs rather than duplicating, and never edit a constitution entry a later phase disputes. No new numbered step, no tools-line change | US-2 | AC-2.2, AC-2.3, AC-2.5, AC-2.6, NFR-1, NFR-6 | T1 | `done` | The rule sits inside steps 1/3 — `grep -c "^[0-9]\. " agents/facilitator.md` unchanged from `main`; frontmatter `tools:` line byte-identical (no Bash); every entry form (`inferred from`, `asked`, `not stated`, `not found`) named; the caps are stated with the overflow-by-pointer instruction — files: agents/facilitator.md |
| T3 | **Walking skeleton (part 3).** `skills/charter/SKILL.md`: step 1 also hands the Facilitator a read-only git-history summary the ceremony gathered itself (pattern of `skills/next-steps/SKILL.md:28-30`); step 3 surfaces the Project Context as its **own** decision alongside profile, lenses and QA method — same round, showing each entry's `inferred from`/`asked` marker for confirmation or correction. Steps stay at 5; nothing is written outside `.spark/constitution.md` | US-2 | AC-2.2, AC-4.1, NFR-1, NFR-8 | T1, T2 | `done` | `grep -c "^[0-9]\. " skills/charter/SKILL.md` = 5; step 3 names the Project Context as a separate user decision in the same round as the profile and QA method; step 1 names the git summary as the ceremony's job and the commands as read-only; no `${CLAUDE_PLUGIN_ROOT}/…` path added (`git diff` shows none). **Skeleton closed:** a `/charter` first draft on any repo can now produce a confirmed, evidenced, capped §9 end to end — files: skills/charter/SKILL.md |
| T4 | **Routing.** `skills/spark/SKILL.md` no-argument/nothing-to-resume branch (`:25-29`) names and offers `/charter` as the first step ahead of `/next-steps`, never invoking it; the `/spark <idea>` path and the existing lens nudge (`:58-68`) are untouched; a repo **with** a constitution gains no sentence. `skills/next-steps/SKILL.md` step 1's empty-state clause (`:48-50`) recommends `/charter` first instead of asking for the first idea, proceeds to the PO brief only on the user's explicit skip, and still writes nothing under `.spark/` | US-1 | AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-1.5, NFR-1 | T3 | `done` | Both branches state the offer-never-block rule and the explicit-skip continuation; the `<idea>`-argument path in `skills/spark/SKILL.md` and the "never write under `.spark/`" rule in `skills/next-steps/SKILL.md` are unchanged (`git diff` touches no other clause); neither file invokes `/charter`; the with-constitution path adds zero sentences — files: skills/spark/SKILL.md, skills/next-steps/SKILL.md |
| T5 | **Start here (docs in step, constitution §4).** `README.md` gains a **Start here** block of ≤ 10 lines immediately before §Usage's `/next-steps` example, naming `/charter` as the first command on both an empty and an existing repo | US-1 | AC-1.6, NFR-1 | T4 | `done` | The block precedes the §Usage `/next-steps` example and is ≤ 10 lines counted from its heading to its last line; it names both repo states; no new command name appears anywhere in `README.md` — files: README.md |
| T6 | **Negative case — runs first (constitution §1, §4).** With T1–T5 shipped and this repo's constitution still §9-free, `claude plugin validate`, then **performed** runs recorded with quoted output: `/spark` (no argument) and `/next-steps` on this repo → not one sentence added by this feature; a run on a repo with no constitution where the user **declines/skips** `/charter` → exactly today's behaviour (`/next-steps` or "bring your own idea"; the PO brief with "constitution: none"); a read of this repo's pre-change constitution by a ceremony → no warning, no migration, no prompt. Any ceremony that cannot be invoked live is recorded `not-verified-live` with the reason, never passed by reading the Markdown (constitution §8) | US-1, US-2 | AC-1.3, AC-1.5, AC-2.4, NFR-4, NFR-5 | T1, T2, T3, T4, T5 | `done` | `evidence.md` carries `claude plugin validate` green plus one quoted transcript per case above, each judged against the action bar — no new sentence, no error, no warning, no migration prompt — and names explicitly any case recorded `not-verified-live` and why. This task is a **barrier**: no later task may amend `.spark/constitution.md` before it is `done` — files: .spark/project-kickoff/evidence.md |
| T7 | **US-4 discovery method.** `agents/facilitator.md`: the brownfield end of T2's rule — read `README.md`, `CLAUDE.md` and `.spark/` specs where present plus the handed-in git summary, name in the draft what was read and what was `absent`, and fill exactly seven system-picture entries (stack & entry points · module structure · data model · test practice · conventions · how to run · known pain points), each with ≥ 1 `file:line` or `not found`, within the 25-line cap. A missing input is recorded `absent` and the pass continues. `skills/charter/SKILL.md`: the step-1 summary explicitly covers the brownfield inputs | US-4 | AC-4.1, AC-4.2, AC-4.4, NFR-6, NFR-8 | T6 | `done` | All seven entries are named in that order with the `≥ 1 file:line or not found` requirement; the `absent` handling is stated for each of README / `CLAUDE.md` / git history; the draft is required to list what it read; still no Bash in the Facilitator's `tools:` line and no numbered step added to either file — files: agents/facilitator.md, skills/charter/SKILL.md |
| T8 | **US-4 dogfood — the brownfield run (NFR-5).** Invoke `/charter` on aSPARK itself as an **amendment**: the improvised "What this project is." paragraph (`.spark/constitution.md:15-19`) moves into §9 unchanged in meaning, the seven system-picture entries are drafted from evidence, the user corrects entries in the confirmation round, and a dated Amendments row records the migration. No other constitution line changes | US-4, US-2 | AC-4.3, AC-4.5, AC-2.2, AC-2.3, AC-2.6, NFR-5 | T6, T7 | `done` | `.spark/constitution.md` carries §9 written by the performed run, `:15-19`'s paragraph no longer duplicated, an Amendments row dated with its reason; `git diff .spark/constitution.md` changes only the removed paragraph, the new §9 and that row; §9 measures ≤ 35 lines total with the picture ≤ 25 and the brief ≤ 12; `evidence.md` quotes the transcript and counts the relay rounds (≤ 2) — files: .spark/constitution.md, .spark/project-kickoff/evidence.md |
| T9 | **US-3 kickoff interview.** `agents/facilitator.md`: the greenfield end of T2's rule — **one** numbered list of at most 7 project-scope questions (who the user is · what they do today · the smallest version that helps · the success signal · stack, a choice or "let the EM decide" · non-negotiables · the first slice), asked once and nothing else that round, and only the ones the evidence has not already answered; one sentence citing `agents/product-owner.md` §The Interrogation as the per-feature list this deliberately does not repeat; drafting rules for the answers (§3 stack = the named stack or `undecided — the EM proposes at the first /sprint-plan`; §6 = the named non-negotiables; §2 profile = `undetectable — from the user's answers` with the lens decision still explicit); a skipped question writes `not stated` and blocks nothing. `skills/charter/SKILL.md` step 5 offers `/story-time <first slice>` and invokes it only on the user's explicit go | US-3 | AC-3.1, AC-3.2, AC-3.3, AC-3.4, NFR-3, NFR-6, NFR-8 | T6 | `done` | The list holds exactly the seven named topics, is capped at 7 and is stated as one round; `grep -rn "Who exactly hurts today" agents/ skills/ templates/` returns exactly one file and the same grep for the Facilitator's own first question returns exactly one, different, file (NFR-3); the three drafting rules and the skip rule are present; `/charter`'s step count is still 5 and the `/story-time` offer is explicit-go only — files: agents/facilitator.md, skills/charter/SKILL.md |
| T10 | **US-3 dogfood — the greenfield run (NFR-5, A9).** Create an empty git repo as untracked scratch **outside** this working tree, invoke `/charter` there, answer the interview, and record the transcript: the section filled from the answers, a first slice named, the `/story-time` offer made and not taken automatically | US-3 | AC-3.1, AC-3.3, AC-3.4, AC-3.5, NFR-5, NFR-8 | T9 | `done` | `evidence.md` quotes the run, states the venue's absolute path and that it is outside `/Users/andreaslottes/aSPARK`, shows `git status` in this repo unchanged by the run (constitution §3 — the published surface is the whole working tree), counts the relay rounds (≤ 2) and the questions asked (≤ 7), and shows `/story-time` was offered, not invoked — files: .spark/project-kickoff/evidence.md |
| T11 | **US-5 readers.** `agents/product-owner.md:48-50` and `agents/engineering-manager.md:45-47`: read the constitution's Project Context **before** any code and cite it as `constitution.md §<n>` for system facts used in spec §1/§2 and in the plan's ADR context / Affected Components; name the three conditions under which reading source is still required — (a) the feature touches that area, (b) the entry is `not stated`/`not found`, (c) a concrete reason to doubt the entry — and require an artifact that re-derives to name which condition applied; no section, or no constitution, means behave exactly as today | US-5 | AC-5.1, AC-5.2, AC-5.3, AC-2.5 | T8 | `done` | Both agents carry the same rule with all three conditions verbatim and the cite-by-`§<n>` form; both state the unchanged fallback for a constitution without the section; neither gains an instruction to skip reading code for the area it is changing; `git diff` touches only the "Understand the context first" / "Learn the terrain" step in each file — files: agents/product-owner.md, agents/engineering-manager.md |
| T12 | **Docs in step + honesty of claim (constitution §4, NFR-7).** `README.md` §Project Status and `ROADMAP.md` record the capability with its real maturity: the greenfield path proven on a sample repo only, the brownfield path on aSPARK only, no claim of a saving on an external project and no claim of a field-verified first run | US-1, US-3, US-4 | NFR-7, AC-1.6 | T8, T10 | `done` | Both files name both venues and their limits; `grep -n` over the added lines finds no sentence claiming external-project savings or a field report; each claim matches what `evidence.md` actually recorded — files: README.md, ROADMAP.md |
| T13 | **Surface, weight and deferral audit.** Record in `evidence.md`: the NFR-1 counts (`ls skills/` = 10, `ls agents/` = 7, `ls lenses/`, `ls templates/` unchanged; `/charter` steps = 5; zero new `${CLAUDE_PLUGIN_ROOT}/…` paths in the diff); NFR-2's A3 citations re-checked live (`aspark-graph` 0 hits, `aspark-guard` `tests/test_rules.py:136-138` + `src/aspark_guard/templates.py:28-32`); NFR-3's two greps; NFR-6's measured line/round/question counts; and **AC-5.4/S3 recorded as `deferred`** — it measures the *first feature after* this one, so it cannot be verified inside this increment; name the counting method (`right-sizing` S2) and the venue, and claim no result | US-2, US-5 | NFR-1, NFR-2, NFR-3, NFR-6, AC-5.4 | T11, T12 | `done` | Every count above is present with the command that produced it and its observed output; the A3 citations are re-verified at their current line numbers, not copied from the spec; AC-5.4 is written as `deferred` with its method and venue and **no** pass/fail verdict; `claude plugin validate` green on the finished branch — files: .spark/project-kickoff/evidence.md |

## 4. Test Strategy

No automated tests exist and none is possible for prompt material (constitution §4).
The bar is `claude plugin validate` **plus** a documented performed run of every phase
touched, **negative case first** (constitution §1), written to
`.spark/project-kickoff/evidence.md` — the method used by the last four features. A
read of a Markdown file and reasoning about what it *would* do is never a performed
step (constitution §8); such a row is marked `not-verified-live` with its reason.

- **US-1 (Must) — routing.** T6's performed runs: `/spark` (no argument) and
  `/next-steps` on this repo (AC-1.5: zero added sentences) and on a constitution-free
  repo with the user skipping (AC-1.2, AC-1.3). AC-1.4 (`/spark <idea>`) is verified by
  a performed invocation in the same run. AC-1.6 is a diff check (T5), not a run.
- **US-2 (Must) — the section.** Static verification where the criterion is structural
  (AC-2.1 by `git diff` + the two by-number citations, AC-2.3 by line count, T1/T8) and
  performed where it is behavioural (AC-2.2 and AC-2.6 in T8's real `/charter` round;
  AC-2.4 in T6's pre-change read). §9's own confirmation round is the test for AC-2.2 —
  there is no other way to prove "same round, no extra round" than to run it.
- **US-4 (Should).** T8, on aSPARK itself — the only measured venue (A2). Its output is
  simultaneously the AC-4.5 migration and the evidence for AC-4.1/4.2/4.3. AC-4.4
  (missing README / `CLAUDE.md` / git history) has no venue here, where all three exist:
  it is verified in T10's scratch repo, which has none, and that cross-use is stated in
  `evidence.md` rather than left implicit.
- **US-3 (Should).** T10, on an untracked scratch repo outside this tree (A9). Counts —
  questions ≤ 7, rounds ≤ 2 — are read off the transcript, not asserted.
- **US-5 (Should).** AC-5.1–5.3 are diff checks on two agent files (T11). **AC-5.4 is
  deliberately not verified in this increment** and is recorded `deferred` (T13): it
  measures the next feature's `spec.md`/`plan.md`, which do not exist yet. Marking it
  passed by inspection would be exactly the fraud constitution §8 names.
- **Deliberately left to `/demo-day`:** the live re-performance of all three runs
  against the *installed* plugin, per constitution §8's substitute method — this
  increment's runs are against the working tree. Nothing is left to "manual testing
  only" without a reason, and there is no browser surface to leave anything to.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| T8 amends this repo's constitution, after which the negative case can never be re-run in its original state | High — NFR-4's evidence would be unobtainable, and constitution §1's "negative case first" unsatisfiable for this feature | T6 is a hard barrier with an explicit dependency edge into T7/T8; its DoD states the barrier in the plan itself so `/increment` cannot reorder it innocently |
| §9 is appended next to the `---`/Amendments block; a careless edit renumbers §1–§8 or displaces Amendments | High — silently breaks `skills/spark/SKILL.md:74` and `skills/demo-day/SKILL.md:28` (constitution §6, AC-2.1) | T1's DoD requires the heading grep and both citation checks; T8's DoD bounds its own diff to three regions |
| Seven system-picture entries, each needing a `file:line`, inside a 25-line cap is tight — the cap and AC-4.2 can collide on a real repo | Medium — either the cap is breached or an entry loses its evidence | T7 states the overflow rule (point at README/`CLAUDE.md`/docs, never duplicate); T8 measures the cap on a real run and the collision, if it happens, is a spec finding routed back to `/story-time` — not a quiet cap breach |
| The Facilitator's step 3 already carries profile, lenses, load and QA method; adding Project Context makes the confirmation round long enough that the user skims | Medium — a rubber-stamped section is worse than none (constitution §1: a constitution nobody follows) | NFR-6's counts are measured in T13 from the real transcript; the caps live in the template comment so they bind the artifact, not just the agent's memory |
| A ceremony may not be invocable live in this session (the `claude -p` auth failure recorded at `.spark/right-sizing/qa.md:59-61`) | Medium — parts of T6/T8/T10 could become read-and-reason | T6's DoD requires any such case to be recorded `not-verified-live` with its reason and claimed as no coverage; it is never converted into a pass |
| The greenfield scratch repo leaks a file into this working tree | Medium — the published surface is the whole tree, `.gitignore` is no shield (constitution §3) | T10's DoD requires the venue's absolute path outside `/Users/andreaslottes/aSPARK` and an unchanged `git status` here |
| Inherited A2: the consumer-facing benefit is inferred, not observed — no field report exists | Medium — the README could overstate a first-run improvement nobody has measured | NFR-7 is its own task (T12) with a grep-checkable bar; both venues are named with their limits |
| The graph can ground nothing here — `impact` returned all 11 paths as `unknown_files`, so no tool can catch a file that reads a changed prompt | Low–Medium — this holds for every Core feature, not just this one; the scope rests entirely on hand-reading | §2 records the structural empty verbatim rather than as an all-clear; scope was derived from the spec's `file:line` evidence plus a read of each named file, and T1's citation checks, T9's NFR-3 greps and T13's surface audit are the mechanical backstop |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (eight, in §1)
- [x] Architecture respects the constitution's technical constraints — Markdown/JSON only, no new tracked executable code, no new file; §3's "a new concern is a new file" is recorded in §1 as deliberately not binding here, with its reason
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task (AC-1.1–1.6, AC-2.1–2.6, NFR-1–NFR-8 all appear in the Covers column)
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies — T6 is an explicit barrier before T7/T8
- [x] Test strategy covers every Must story (§4), and names the one AC deliberately deferred (AC-5.4) rather than claiming it
- [x] Line budget respected: Ist 216 / Soll ~300 (excluding HTML comments — 224 lines total, 8 of them comment)
- [x] Status set to `approved` by the user
