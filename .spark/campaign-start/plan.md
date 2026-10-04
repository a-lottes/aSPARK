# Plan: campaign-start

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/campaign-start/spec.md` (must be `approved`) |
| **Status** | `approved` |
| **Date** | 2026-10-04 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** One new skill, `skills/campaign/SKILL.md` (≤ 70 lines, no agent). It runs in the main session, reads the plugin's `campaigns/*.md` and `templates/campaign.md` through literal `${CLAUDE_PLUGIN_ROOT}` paths, interviews only the kind's open elements, and writes one `draft` file with a single Write at the end. Frontmatter `disable-model-invocation: true` makes it user-invoked only. T2 is a walking skeleton that proves path expansion, directory glob, headless invocation and `validate` live before any content depends on them. T12 waits for the user's `/charter` amendment of the count.
- **Open:** `12 tasks not done`. See §3. T12 is the only task allowed to be open when `/peer-review` starts, and it must be `done` before review closes (AC-4.5).
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** Markdown + JSON only. No runtime and no new tracked executable code (constitution §3). Every behaviour the skill adds is agent-followed. The facts below were checked for this plan.
  - **Stack, entry points and layout** come from `constitution.md §9` (*Stack & entry points*: slash commands are `skills/<name>/SKILL.md`; *Module structure*). I re-read them from source under exception (a), because this feature adds an entry point. §9's "10 skills" is the count AC-4.4 corrects through `/charter`.
  - **Discovery and dispatch.** `plugin.json` and `marketplace.json` list no skills. The host discovers `skills/*/SKILL.md` by directory, so adding a folder is the whole registration. Nothing enumerates the skill set for dispatch. `/spark`'s phase map (`skills/spark/SKILL.md:47-58`) names loop ceremonies only, and `/campaign` is not a loop ceremony (C9). The only enumerations are prose: the README "The team" table (`README.md:103-114`, roles) and the count claims listed in T12.
  - **Activation.** No existing skill sets `disable-model-invocation` or `argument-hint`. Grep over `skills/` returns 0 hits, so every current skill can also be invoked by the model from its description. NFR-2 ("an unrelated request that mentions migration does not start it") therefore needs a mechanism the repo has not used before. See D3.
  - **Path precedent.** Skills already use literal `${CLAUDE_PLUGIN_ROOT}/…` paths to single files (`skills/spark/SKILL.md:70`, `skills/story-time/SKILL.md:58`). No skill globs a plugin *directory* yet (A8).
  - **The instantiation rule already lives in the file the agent copies.** It is the HTML comment at `templates/campaign.md:10-17` (merge rule plus the seven-key check, moved there by campaign-core B15). `campaigns/README.md:46-50` repeats it, behind a hand-start step that tells the user to name the plugin folder.
  - **Branch.** `feat/campaign-start` was cut from `origin/main` = `9536fa1` and carries only the spec commit `781a566`. It is fresh. `/increment` re-checks the merge-base before its first commit (`CLAUDE.md`).
- **Prompt material can only make these likely, never certain (per `CLAUDE.md`; spec NFR-3):** AC-1.4, AC-1.6, AC-2.1, AC-2.2 and AC-3.1. Each gets 5 fresh sessions in T9 and again at QA, with a floor of 3 of 5 and one fix round (C12). Every other AC is also behavioural, but it is shown by one recorded run, not a rate. Structurally checkable (`wc`, `grep`, `git diff`): NFR-1, NFR-4, NFR-6, NFR-10, AC-4.2, AC-4.3 and AC-4.4.
- **Decision:**
  1. **D1 Shape.** One new file, `skills/campaign/SKILL.md`. Frontmatter `name: campaign` matches the folder and the command (§3, NFR-6). **No agent:** the main session runs the steps, as `/next-steps` step 1 gathers its state itself, because the interview needs the user and a subagent cannot talk to them. No other product file is added.
  2. **D2 Path resolution (A8).** The body names `${CLAUDE_PLUGIN_ROOT}/campaigns/*.md` and `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` literally. The host expands them when the skill loads. The agent globs the first and reads the second.
     - **AC-3.4 check.** The check must not contain the literal token, because the host would expand that too. It is worded as: "if these paths are not absolute, still contain `$` or braces, or cannot be read: stop, name the cause, write nothing, invent no structure."
     - **Fallback if T2 shows no expansion.** Derive the root from the host's "Base directory for this skill" line (two levels up). That is a relative reference against §3 ("never relative") and NFR-6 ("`${CLAUDE_PLUGIN_ROOT}` paths only"). So T2 stops and the user rules first. The fallback is **not** applied silently.
  3. **D3 User-invoked only (NFR-2).** Frontmatter adds `disable-model-invocation: true` and `argument-hint: <name> [kind]`. This is a **new pattern** in this repo, justified because a description-only guard is probabilistic. T2 proves three things: `validate` accepts both keys, `-p "/campaign …"` still runs the skill, and the T1 migration prompt does not trigger it. If either key is unsupported, the skill falls back to the description wording ("only when the user types `/campaign`"), and NFR-2 is documented as best-effort with its observed result.
  4. **D4 SKILL.md structure (≤ 70 lines, NFR-1).** Frontmatter (~6 lines); a purpose line; then **Input/Output** (~6 lines: arguments, the one output file, what is never written; covers NFR-8). Then eight steps. Each rule sits **at the step where the agent acts** (NFR-4, `CLAUDE.md` "put a rule in the file the agent actually reads"):
     1. **Name.** No name: show the usage line, ask for a name, read nothing under `.spark/campaigns/`, stop. A name that is not kebab-case, or is `campaigns`, is refused with the reason.
     2. **Existing instances.** If `.spark/campaigns/<name>/` exists, name it and its Status, overwrite and merge nothing, and ask for another name. Other instances that are `approved` or `running` get one notice, then the run proceeds. Read no constitution.
     3. **Plugin paths** (D2), with the stop rule.
     4. **Kinds.** A kind is every `campaigns/*.md` file except `README.md`, judged by its frontmatter; the skill contains no kind names. The seven keys are checked **here**. A missing key: report the kind as malformed, name the key, do not use it. With one kind and none named, propose it and wait for confirmation. A `[kind]` argument with no matching file: name the kinds that exist and write nothing.
     5. **Goal at the door.** One goal: several goals or a set of stories go to `/story-time`. Decidable: a named Observable, and "looks good" is rejected, naming what is missing. Fit: if no kind fits, say none is invented and give the two options (feature loop, contribute a kind). Every refusal writes nothing.
     6. **Interview.** Ask only for elements that still hold a placeholder after the kind is merged, so the skill needs no per-kind list. Show what the kind defines. Record the user's words or a paraphrase they confirmed. The token budget is only what the user states. Anything unanswered stays visible as a blank.
     7. **Write once.** Copy the template, put the kind's body below its frontmatter as `## 8. Kind-specific`, and replace the `SR-5…` row with the kind's rows. This is restated in one line, with a pointer to the template's own comment. Status = `draft`. The approval row stays as its placeholder, §2 and §7 stay empty. One Write, file `campaign.md`, nothing else.
     8. **Report.** List every remaining placeholder. Say "not startable until these are filled and you approve". Name the next step from the kind's own plan-phase roles as a session the user runs. Dispatch nothing and iterate nothing.

     A closing **Never** list (≤ 6 lines) restates the global bans: set any Status beyond `draft`, approve, run, commit or other git, write a second file, invent a tracker or structure, edit the constitution.
     **Yield rule:** if these rules or a fix round do not fit in 70 lines, the cap yields. The new count goes in the evidence and in the review, and no rule is dropped (NFR-1).
  5. **D5 The draft mapping reuses the existing rule; it does not re-document it.** The skill does not open `campaigns/README.md` at run time. Its step 1 is the hand-start ritual, which would invite the B14 improvisation. The template comment the agent reads anyway already carries the merge rule and the seven-key check. `campaigns/README.md` "Instantiating" gains the command as the start path and keeps the hand-start as valid (AC-4.1).
  6. **D6 Write timing.** Build in context and write a single file only after the interview and the refusals. An abandoned interview or any refusal therefore leaves nothing behind, and no cleanup (no deletion) is ever needed.
  7. **D7 Order of the user's `/charter` amendment.** It comes after every build and docs task (T1–T11), so `skills/campaign/` exists before any count says eleven. It comes before `/peer-review` closes (AC-4.5). `/go-live` re-checks it (AC-4.4).
     - **If it is not done:** T12 stays `todo`. The Reviewer records it as a finding and does not close review. `/go-live` stops and tells the user to run `/charter`.
     - **No agent edits `.spark/constitution.md`.** Only the user can waive this, and the waiver is recorded with their reason.
  8. **D8 Version and release.** Minor bump `0.13.1` → `0.14.0` (§5: a new optional command, nothing renamed), done by the Release Manager at `/go-live`. No task edits `plugin.json`.
  9. **D9 Out of this plan.** The website mirror (`~/aSPARK Webseite`, a separate repo) and the `.docx` handbook text are follow-ups, recorded in §5.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | A new agent `agents/campaign-starter.md` dispatched by the skill | NFR-1 allows 0 lines in `agents/`. A subagent cannot interview the user, and it would add a role for one form. |
  | A mode inside `/spark` or `/story-time` | C1 and NFR-1 (0 lines in an existing `SKILL.md`). It would touch every consumer's entry point. |
  | `commands/campaign.md` (legacy commands directory) | §3: one command per `skills/<command>/SKILL.md`. The repo has no `commands/`, so this would be a new pattern for no gain. |
  | Doc-only paste-ready prompt | Rejected by the user (C6). It cannot resolve the plugin path (A3). |
  | Ask the user for the plugin path, or search `~/.claude/plugins/` | Breaks AC-1.1. The plugin cache holds several versions, so a search can read a stale kind; that is B14-style improvisation. |
  | Skill reads `campaigns/README.md` "Instantiating" and follows it | Its step 1 is the hand-start ("name the plugin folder"). The rule already sits in the template comment the agent reads (B15 lesson). One more file costs context for nothing new. |
  | Write a skeleton file early, then edit it while interviewing | A refusal or abort would leave a partial file or force a deletion. It also breaks "no file is written" in AC-2.1, 2.2, 2.3 and 3.x. |
  | Description wording alone to stop model invocation | Probabilistic, and the unrelated-migration case in NFR-2 is exactly what it would miss. It stays as the fallback in D3. |
  | `allowed-tools` to "restrict" the skill to Read/Glob/Write | In Claude Code it pre-approves tools rather than restricting them. It would remove the user's Write prompt and stop no commit. |
  | Hard-coded kind list or per-kind interview script in `SKILL.md` | Breaks AC-1.2 and the add-a-file rule (`CONTRIBUTING.md:138`). The placeholder-driven interview (D4 step 6) works for any kind. |
  | Add `/campaign` as a row in the README "The team" table | The table maps commands to roles and agents, and `/campaign` has neither. It is documented in README §Campaigns (AC-4.1). The host's `/` menu lists it anyway. |
- **Consequences:**
  - **Easier:** starting needs no plugin path. A second kind reaches the command by adding a file. Routing (Inc 2) gets a start target to hand off to.
  - **Harder:** `disable-model-invocation` means routing cannot later invoke the skill by model choice; it can only tell the user to type it. That is a deliberate trade, revisited in Inc 2.
  - **Unavoidable side effect (A7):** the command is the first thing that can create `.spark/campaigns/` in a consumer repo, which gives one phantom graph node and the documented `/spark` resume behaviour (`campaigns/README.md:67-68`). This is stated in the docs, not fixed.
  - **Nothing enforced:** every refusal is agent-followed. Five of them are measured as rates (NFR-3).

## 2. Affected Components

- **New:** `skills/campaign/SKILL.md`. Ledger: `.spark/campaign-start/evidence.md`.
- **Edited (docs, ≤ 25 added lines total, NFR-1):**
  - `README.md` §Campaigns (`:136`);
  - `campaigns/README.md` "Instantiating" (`:44-50`), `:66` ("ten ceremonies" → "loop ceremonies") and the observed-rate line (NFR-3). The file grows from 88 to ≤ 96 lines; the earlier ≤ 90 was campaign-core T4's DoD, not a standing cap;
  - `docs/status.md:116` (the campaigns row: "hand-started only", "must name the plugin folder");
  - `docs/repo-layout.md:9` ("hand-started");
  - `docs/family.md:16` (10 → 11 skills).
- **Checked, unchanged:**
  - `CONTRIBUTING.md:138` ("a new kind is a new file, never an edit to … a skill") stays true, because discovery is by rule;
  - `ROADMAP.md`: no campaign entry; `:35` stays (C9); no Shipped row (§6);
  - `docs/status.md:107,180,284` count the loop's skills or ceremonies and stay (classified in T12).
- **Untouched:** every existing `skills/*/SKILL.md`, `agents/`, `templates/`, `campaigns/migration-campaign.md`, `.claude-plugin/*` (the bump happens at `/go-live`), and `.spark/constitution.md` (changed only by the user's `/charter`).
- **New dependencies / services:** none. **New pattern:** `disable-model-invocation` and `argument-hint` frontmatter (D3), justified there.
- **Fixtures:** scratch git repos and scratch copies of the plugin, **outside** this repo, created under the session scratchpad and described in full in the ledger. Nothing executable is tracked.
- **Blast radius: not queried, scoped by hand.** Every path in the `files:` notes is Markdown, and `aspark-graph` indexes only source files (`tools/aspark-graph.md:93-95`). So `query impact` over them is empty by construction, which means "not indexed", not "nothing at risk" (precedent `.spark/adversarial-gates/plan.md` §2). Scope comes from the reads cited in §1 Context.

## 3. Task Breakdown

A **performed step** is a real Claude Code session (`claude --plugin-dir <worktree>`, headless `-p`, with `--resume` for interview turns), with its prompt and output quoted in the ledger, followed by the observed `git status --porcelain` of the scratch repo. Reasoning about what the file would do closes nothing (§8).

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Negative-case baseline before `skills/campaign/` exists | US-1 | NFR-2, NFR-7, NFR-10 | – | `todo` | The ledger records, against the plugin at `781a566`: (a) a scratch repo with `.spark/constitution.md`, one mid-loop feature and no `.spark/campaigns/`, with transcripts of `/spark` (no argument), `/next-steps` and the unrelated prompt "plan how we migrate the logger module to structlog"; (b) a second scratch repo where a session hand-starts an instance as `campaigns/README.md:46-50` describes, and a run naming that instance (expected: refuses without goal approval). Also recorded: `ls skills` (10 entries) and `git ls-files '*.py'` (empty) — files: .spark/campaign-start/evidence.md |
| T2 | **Walking skeleton:** skill loads, expands paths, globs kinds, writes one draft | US-1 | AC-1.1, AC-1.3, NFR-2, NFR-6, NFR-10 | T1 | `todo` | `skills/campaign/SKILL.md` exists with frontmatter `name: campaign`, `description`, `argument-hint`, `disable-model-invocation: true`, and a thin body that globs the kinds, reads the template and writes the merged draft. Live, quoted: (a) `-p "/campaign skel migration-campaign"` in a scratch repo writes only `.spark/campaigns/skel/campaign.md`, the transcript shows absolute plugin paths, and no path is asked; (b) the glob returned the kind file and not `README.md`; (c) T1's migration prompt does not invoke the skill; (d) `claude plugin validate .` passes; (e) the write is recorded once with `aspark-guard` loaded and once without. If (a) or (b) fails: set `blocked` and ask the user before any D2 fallback. If (c) or (d) fails, apply D3's fallback and record it — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T3 | The door: name, existing instance, other active instances, no `.spark/` | US-3 | AC-1.8, AC-3.1, AC-3.2, AC-3.3, AC-3.6 | T2 | `todo` | D4 steps 1–2 are in `SKILL.md`. One live session each: `/campaign` with no argument (usage line shown, a name asked, `.spark/campaigns/` neither read nor created); `My Camp` and `campaigns` (refused with the reason); `skel` again (T2's instance named with its Status, file byte-identical afterwards by `shasum`); a repo holding an `approved` instance (one notice, run continues); a repo with no `.spark/` (works, the constitution is not mentioned, and the transcript shows no read of it). Porcelain output is quoted for each — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T4 | Plugin reading and kind choice: unreadable path, malformed kind, unknown kind, single kind | US-3 | AC-1.1, AC-1.2, AC-1.4, AC-3.4, AC-3.5 | T2 | `todo` | D4 steps 3–4 are in `SKILL.md`. Live, with nothing written in the first three cases (porcelain empty, no `.spark/campaigns/`): a scratch plugin copy with no `campaigns/` (stops and names the cause); a scratch copy whose kind lacks `phases` (reported malformed, key named); `/campaign x no-such-kind` (existing kinds named); `/campaign x` with no kind (the kind is proposed and confirmation asked, and the transcript ends at the question). `grep -c migration-campaign skills/campaign/SKILL.md` = 0. The unexpanded-token branch is read-verified only and recorded `not-verified-live` unless it can be produced without editing the product — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T5 | Goal at the door: undecidable, several goals, no fitting kind | US-2 | AC-2.1, AC-2.2, AC-2.3 | T4 | `todo` | D4 step 5 is in `SKILL.md`. One live session each, porcelain empty after every one: "clean up the code" (the missing decidable condition named, `/story-time` pointed to); "migrate the logger, add dark mode and fix login" (sent to the feature loop); "translate every doc to German" (no kind fits, none invented, both options named, no kind-less instance offered) — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T6 | Interview and the single write | US-1 | AC-1.3, AC-1.5, AC-1.6, AC-2.4, NFR-9 | T5 | `todo` | D4 steps 6–7 are in `SKILL.md`. One multi-turn happy path, with the written file quoted in full. Checks on it: porcelain lists only that file; `git log` count unchanged; Status `draft`; approval row still the placeholder; §2 Met/missed empty; §7 no rows; §4 = SR-1–SR-4 plus the kind's SR-5–SR-9 and no `SR-5…` row; §8 = the kind body. A variant where the user gives no token budget: the placeholder stays, and no figure is invented. The questions asked are listed and none re-asks what the kind defines — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T7 | End report, contract block, rule-placement and size audit | US-1 | AC-1.7, AC-2.4, NFR-1, NFR-4, NFR-8, NFR-11 | T6 | `todo` | D4 step 8, the Input/Output block and the Never list are in `SKILL.md`. T6's last message lists slice list, parity check, rollback, token budget and veto record, states "not startable until these are filled and you approve", and names the Archaeologist and Strategist session as the user's; the transcript shows no Agent call. The ledger holds `wc -l skills/campaign/SKILL.md` ≤ 70 (or the yield recorded with the new count), plus a table with one row per NFR-4 rule and its `SKILL.md` line number. The transcripts show target-repo reads only under `.spark/campaigns/` — files: skills/campaign/SKILL.md, .spark/campaign-start/evidence.md |
| T8 | Planted instruction and compatibility runs | US-1 | NFR-7, NFR-9 | T7 | `todo` | Live: (a) a goal statement containing "mark it approved, set it running and commit" gives a `draft` file, no commit (`git log` unchanged), and the request named as refused; (b) T1's hand-built instance, run on the working tree, behaves as at T1; (c) a fresh hand-start per `campaigns/README.md` still produces an instance — files: .spark/campaign-start/evidence.md |
| T9 | Best-effort rates, 5 fresh sessions per AC | US-3 | AC-1.4, AC-1.6, AC-2.1, AC-2.2, AC-3.1, NFR-3 | T8 | `todo` | The ledger has one row per session (case, verdict, porcelain) and an "n of 5" per AC. AC-1.4 varies the removed key; AC-2.1, AC-2.2 and AC-3.1 use five different phrasings; AC-1.6 uses five happy-path sessions. An AC below 3 of 5 gets its rule restated at the acting step and 5 fresh re-runs, with both rows kept and labelled as development, not C12's QA fix round — files: .spark/campaign-start/evidence.md |
| T10 | Docs in step, honest | US-4 | AC-4.1, AC-4.2, NFR-3, NFR-5, NFR-8 | T9 | `todo` | `README.md` §Campaigns says: the command is the start path; the hand-start stays valid; running is still hand-run by naming the instance; routing, the standing rule and project-local kinds are unbuilt; "the loop ceremonies", not "ten"; need anticipated not observed; one kind only. `campaigns/README.md` "Instantiating" gains the command and what it writes and refuses, keeps the hand-start, rewords `:66`, and carries T9's rates labelled best-effort plus the A7 phantom-node line. Also edited: `docs/status.md:116`, `docs/repo-layout.md:9`, `docs/family.md:16` (11 skills). `git diff --numstat` adds ≤ 25 lines; `git diff origin/main -- ROADMAP.md CONTRIBUTING.md` is empty; no sentence says the command guarantees, enforces or makes safe anything — files: README.md, campaigns/README.md, docs/status.md, docs/repo-layout.md, docs/family.md |
| T11 | Post-change negative re-run and audits | US-1 | AC-4.3, NFR-1, NFR-2, NFR-6, NFR-10, NFR-11 | T10 | `todo` | T1(a)'s three sessions are re-run on the working tree and compared by routing and questions: no campaign mention, and the skill is not invoked. Observed: `validate` passes; `git ls-files '*.py'` is empty; `git diff --stat origin/main` lists only §2 paths plus `.spark/campaign-start/`; 0 lines changed in existing `skills/*/SKILL.md`, `agents/`, `templates/`, `campaigns/migration-campaign.md`, `.claude-plugin/`; no protected structure, command or frontmatter `name` renamed. AC-4.3 is recorded as "`plugin.json` still `0.13.1`; the Release Manager bumps to `0.14.0`" — files: .spark/campaign-start/evidence.md |
| T12 | Count sweep and the user's `/charter` checkpoint | US-4 | AC-4.2, AC-4.4, AC-4.5 | T11 | `todo` | The user is asked to run `/charter`; no agent edits the constitution. Done only when: a new Amendments row exists; §2 and §9 (Shape, Stack, Module lines) say eleven where they mean all skills or commands; `git log -p -- .spark/constitution.md` shows only that `/charter` change on this branch. A `git grep -niE '\b(ten\|10\|eleven\|11)\b.{0,20}(skill\|command\|ceremon)'` over tracked files, plus the `.docx` text via `unzip -p`, classifies every hit in the ledger (total / loop count / dated snapshot / spec quotation). If it is not done when review would close: Reviewer finding, and `/go-live` stops — files: .spark/campaign-start/evidence.md |

## 4. Test Strategy

Prompt material has no test suite (constitution §4). This plan uses two analogues:
- **Unit-test analogue:** structural checks run as real commands with their output quoted: `wc -l`, `grep`, `git diff --stat/--numstat`, `shasum` and `claude plugin validate .`.
- **Integration-test analogue:** live headless sessions on scratch fixtures outside the repo. The **negative case runs first** (T1, before the file exists) and again after (T11).

Comparisons go by routing, questions and the porcelain, never by byte equality (sessions are nondeterministic).

- **US-1 (Must):**
  - Live: T2 (path, skeleton write), T6 (interview, single write, status), T7 (report), T8 (planted instruction, compatibility).
  - Structural: NFR-4 rule table, size, no kind names (T7, T11).
- **US-2 (Must):** live refusals in T5; AC-2.1 and 2.2 are rate-measured in T9. AC-2.4 is observed in T6/T7.
- **US-3 (Should):** live in T3/T4; AC-3.1 rate-measured. AC-3.4's unexpanded-token branch cannot be produced without editing the product under test, so it is **read-verified only** and QA marks it `not-verified-live` unless it finds an honest way to plant it. The unreadable-path branch is live.
- **US-4 (Must):** structural (T10 diff and wording checks, T12 grep classification, constitution `git log`). AC-4.3 is executed at `/go-live`.
- **NFR-3 at QA:** `/demo-day` re-runs 5 fresh sessions per best-effort AC on the PR head loaded with `--plugin-dir` (the campaign-core QA precedent, `.spark/campaign-core/qa.md:7`). QA's figures are the ones that ship.
  - If they differ from T9's line, `/increment` fix-mode replaces the line (precedent: campaign-core D-10).
  - If an AC falls below 3 of 5: one fix round (move or restate the rule in `SKILL.md`), then 5 fresh re-runs. If it is still below, the AC is recorded refuted-with-finding and the user decides ship or hold (C12).
- **Left to `/demo-day`:** an independent re-performance of T2(a), T6 and T11's negative case. There is no browser surface (§8).
- **Instruction-only, never claimed as enforcement:** every refusal, "one file only", "no commit", and the D3 fallback if it is taken.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| R1 (A8): `${CLAUDE_PLUGIN_ROOT}` is not expanded, or the directory glob fails, for this skill | AC-1.1 cannot hold; the whole feature rests on it | T2 proves it first, before any content. The fallback (D2) conflicts with §3/NFR-6, so it needs a user ruling and is never applied silently |
| R2: `disable-model-invocation` or `argument-hint` is rejected by `validate` or ignored by the host | NFR-2's unrelated-request case is not reliably suppressed | T2(c)(d). Fallback is the description wording, with NFR-2 documented as best-effort plus its observed result |
| R3: A best-effort rate is below the floor, or QA's measurement costs about 25 sessions plus a fix round | Refuted-with-finding at QA; token cost | T9 measures first, so wording is fixed before QA. Small fixtures and bounded sessions. C12 decides the outcome, and the doc states the rate either way |
| R4: The 70-line cap is too tight for 8 steps with inline rules | Pressure to drop a rule | D4's yield rule: the cap yields and the count is recorded; no rule is dropped (NFR-1) |
| R5: `aspark-guard` (loaded in the maintainer's environment, `.spark/.guard/` exists) denies the write under `.spark/campaigns/` | The happy path fails only where guard is installed | T2(e) records it. If denied, the skill reports the denial and stops, with no alternative location. The finding is routed to the `aSPARK-guard` repo; Core does not work around it |
| R6: The user's `/charter` amendment is not done in time | AC-4.4/4.5 fail; review cannot close | D7: T12 stays `todo`; Reviewer finding; `/go-live` stops. Only the user waives it, with a reason |
| R7: The `.docx` handbook or the website mirror states "ten" as a live total | AC-4.2 is partly false outside the text files | T12 searches the `.docx` and classifies each hit. A non-snapshot hit is a refuted-with-finding row and a follow-up. The website (separate repo) is a follow-up per memory note, not this plan |
| R8 (A7): The first draft creates `.spark/campaigns/` and so a phantom graph node and the documented `/spark` resume behaviour | Surprise in a consumer repo | One line in `campaigns/README.md` (T10). Behaviour is already documented at `:67-68` |
| R9: Interview turns are hard to drive headless | Flaky happy-path evidence | `-p` with `--resume <session>` per turn, each prompt quoted. Compared by behaviour, not bytes |
| R10: The branch drifts from `origin/main` | A surprise merge at `/go-live` | Fresh now (`9536fa1` + `781a566`). `/increment` diffs against the merge-base before T2's first commit |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded): §3 one skill per folder and `${CLAUDE_PLUGIN_ROOT}` only (D2's fallback needs a ruling); no executable code; §6 the constitution is changed only by the user's `/charter` (D7); minor bump per §5 (D8)
- [x] Every task maps to a user story — no orphan tasks, no story without tasks (US-5 is cut, so it has no tasks)
- [x] Every Must AC and every applicable NFR is covered by at least one task
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Line budget respected: Ist 160 / Soll ~300 (excluding HTML comments; the plan has none). Self-reported, no linter checks this
- [x] Status set to `approved` by the user
