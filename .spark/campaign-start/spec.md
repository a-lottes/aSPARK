# Spec: campaign-start

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-10-04 |
| **Ticket** | none |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** Starting a campaign today means naming the installed plugin folder in a prompt and hand-assembling `campaign.md`; a bare prompt makes the agent invent a structure (QA B14). Add one command, `/campaign <name> [kind]`, that resolves the plugin path inside a skill, interviews only what the chosen existing kind leaves open, and writes a **draft** instance, never approving or running it; it stops at the draft and names the next step (user-confirmed, C8/C13). Kind-less campaigns, new kinds, listing instances, routing and the standing rule are cut. The release also depends on the user's `/charter` amendment of the "ten" count (US-4).
- **Open:** `none` — Q1 to Q7 are ruled by the user (C6 to C9, C11 to C13). The C10 defaults stay visible for the gate walk.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed since the last round and why
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** Campaigns shipped in `v0.13.0` as "hand-started" (`README.md:136`): the user must find the installed plugin folder under `~/.claude/plugins/` and name it in the prompt, because an agent outside a skill cannot resolve `${CLAUDE_PLUGIN_ROOT}` (`campaigns/README.md:46`, `constitution.md §9` for the skill/command structure). Without that, QA session `b3b` showed the agent asking, then recommending a self-invented tracker at `.spark/campaigns/old-to-new/` (`.spark/campaign-core/qa.md` B14, accepted as a Nit). Then every element is filled by hand and the user must know which are theirs (approval) and which are not. Who hurts: (a) the maintainer, who asked in this session how a campaign is even started, days after shipping it; (b) the intended user, a Claude Code user on a consumer project, who will not hand-copy plugin paths. **Anticipated, not observed:** no campaign has run on a real project; no outsider has tried to start one (A1).
- **Goal:** One explicit, user-invoked command takes a user from "I have a measurable goal" to a **draft** `campaign.md` for an existing kind, with every blank listed, nothing approved, nothing run.
- **Success signal:** (1) Recorded dry run on a scratch repo: from the command and a stated goal, a draft exists at `.spark/campaigns/<name>/campaign.md` with Status `draft`, the approval row unfilled, and the user never typed a plugin path. (2) Recorded misuse runs are bounced (story-shaped request, undecidable goal, existing name, no fitting kind, no name). (3) Observed rates for the best-effort checks are written down (NFR-3). (4) Beyond this cycle and stated as such: the first real campaign on a real project is started this way without structural repair of the draft.
- **Why now / never:** If never built, the hand-start stays documented and works, but costs a path ritual an outsider will not perform and that the agent has been seen to improvise around. Not an emergency. The user ruled to build the minimal slice now (C6). Sequencing: routing (US-3 of `campaign-core`) hands a user *somewhere*; without a start target it can only say "name the instance by hand", so this precedes routing. Displaces: Inc 2 routing, the first real campaign run, or a second kind (A5).

## 2. Target Users

- **The aSPARK maintainer (solo, `a-lottes`)**, who has built campaigns and has not yet run one on a real project.
- **A Claude Code user with a consumer project** and a checkable mechanical goal (today only a migration fits the one kind) who has installed aSPARK and has not read `campaigns/README.md` end to end.
- Not targeted: users who want to author a new campaign kind (a contributor action, `CONTRIBUTING.md`); anyone wanting a campaign to start or run unattended.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The start friction is real for people other than the maintainer. Evidence: B14 (a fixture session, not a real user) and the maintainer's own question. No real-user evidence. | Risk, accepted only if docs say "anticipated, not observed" (NFR-5) |
| A2 | The user's phrase was "a simple way to individual campaigns via a skill or similar" (`einfachen Weg zu individuellen Campagnen über einen Skill oder ähnliches`). "Individual" was read three ways: own instance of an existing kind, a kind-less instance, a new kind. | Resolved: own instance of an existing kind (C7) |
| A3 | A skill is the only Core mechanism that resolves `${CLAUDE_PLUGIN_ROOT}`; the one reason a skill, not a doc, is the shape. | Kept; doc-only alternative rejected by the user (C6) |
| A4 | Running an instance needs no plugin path: the kind body is copied into the instance and frozen (`campaigns/README.md:47`). Only *starting* has the path problem. | Checked against `campaigns/README.md:44-50` and `templates/campaign.md` §8 |
| A5 | With exactly one kind, the command serves migrations only (`campaign-core` A7: one kind is one data point). Value is conditional on someone running a migration campaign. A second upstream kind would widen it more than any skill. | Accepted risk; stated in docs |
| A6 | The command does not touch the constitution: the active-campaign flag is `/charter`'s and arrives with Inc 2. Until then nothing stops a second approved campaign in one repo. | Accepted known limit, stated in docs; see AC-3.3 |
| A7 | `aspark-graph` shows one phantom Feature node once `.spark/campaigns/` exists (`campaign-core` A6/C11). The command is the first thing that can create that directory in a repo that lacked it. | Known; one line in the docs |
| A8 | `${CLAUDE_PLUGIN_ROOT}` written in a skill body is expanded by the host when the skill loads; existing skills rely on it (`skills/spark/SKILL.md:70,94`). Not verified for a skill that reads a *directory* of files. | Risk; AC-3.4 covers the unexpanded case; verified in the recorded dry run |
| Q1 | Build now, or run a first campaign by hand first? | Resolved: build the minimal slice now (C6) |
| Q2 | Scope of "individual". | Resolved: instance of an existing kind only (C7) |
| Q3 | Command name and shape. | Resolved: `/campaign <name> [kind]`, no mode word (C7) |
| Q4 | Stop at the draft, or also run the kind's planning roles? | Resolved by the user: stop at the draft, name the next step (C8, C13) |
| Q5 | Constitution says "ten slash commands" (§2) / "10 skills" (§9); `ROADMAP.md:35`. | Resolved: the user runs `/charter` in the same release; `ROADMAP.md:35` stays (C9, AC-4.2, AC-4.4) |
| Q6 | `/campaign` with no argument: show usage and ask for a name, or list instances first. | Resolved by the user: usage line, ask for a name, write nothing; US-5 cut (C11, AC-1.8, §6) |
| Q7 | If a best-effort check holds poorly (NFR-3): record the rate only, a floor, or 5 of 5. | Resolved by the user: floor 3 of 5, one fix round, then refuted-with-finding and the user decides (C12, NFR-3) |

## 4. User Stories

### US-1 (Must): One command writes a draft instance from an existing kind

> As a Claude Code user with a measurable goal, I want one command to build my `campaign.md` draft, so that I never name a plugin folder or hand-assemble the file.

**Acceptance criteria:**

- [ ] AC-1.1: Given an installed plugin and a repo, when the user runs `/campaign <name> [kind]`, then the command reads `${CLAUDE_PLUGIN_ROOT}/campaigns/*.md` and `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` itself and the user is never asked for a path.
- [ ] AC-1.2: Given `campaigns/*.md`, when a kind is chosen, then the kinds offered are every file there except `README.md`, judged by frontmatter; the skill contains no list of kind names. With one kind and none named, that kind is proposed and confirmed with the user, not assumed; a named kind is used only if its file exists (AC-3.5).
- [ ] AC-1.3: Given a kind, when it is used, then the instance is `.spark/campaigns/<name>/campaign.md`, built as `campaigns/README.md` "Instantiating" describes: the template, then the kind's body as §8, its stop-rule rows replacing the `SR-5…` placeholder. The file is always named `campaign.md`, and it is the **only** file written (parent directories aside).
- [ ] AC-1.4: Given a kind missing any of the seven frontmatter keys, when chosen, then it is reported malformed, naming the key, and not used. *Best-effort (NFR-3).*
- [ ] AC-1.5: Given the interview, when the user has answered, then the command has asked only for what the chosen kind leaves open; what the kind defines (goal shape, stop rules, budget formula) is copied and shown, not re-asked. The user's subject, Observable, Verifier, Thresholds and budget are written as the user's words or a paraphrase they confirmed. The token budget is only what the user states (no invented default). Anything unanswered stays a visible blank.
- [ ] AC-1.6: Given the written draft, when the run ends, then Status is `draft`; "Goal approved by / date" is unfilled; the veto record (§2) is blank, because no check was run; the checkpoint table is empty. The command never sets `approved`, `running`, `halted`, `complete` or `abandoned`, and makes no git commit. *Best-effort (NFR-3).*
- [ ] AC-1.7: Given the draft, when the run ends, then the user is shown every element still holding a placeholder (for migration: slice list, parity check if unnamed, rollback, token budget, veto record), the statement "not startable until these are filled and you approve", and the next step by name (for migration: the kind's Archaeologist and Strategist planning session, run by the user; the command runs neither, C8). Nothing is iterated.
- [ ] AC-1.8: Given `/campaign` with no name, when run, then nothing is written and nothing under `.spark/campaigns/` is read or created; the usage line (`/campaign <name> [kind]`) is shown and a name is asked for. Instances are not listed (US-5 cut, §6).

### US-2 (Must): The command refuses what is not a campaign

> As the maintainer, I want the start command to apply the campaign tests at the door, so that a story or a wish does not enter as a campaign.

**Acceptance criteria:**

- [ ] AC-2.1: Given a stated goal that is not machine-decidable ("clean up the code", "looks good"), when the interview reaches the Observable, then no file is written; the missing decidable condition is named, and the user is pointed to the feature loop (`/story-time`). *Best-effort (NFR-3).*
- [ ] AC-2.2: Given a request with several independent goals or a set of stories, when started, then no file is written and it is directed to the feature loop (the one-goal rule, `templates/campaign.md` §1). *Best-effort (NFR-3).*
- [ ] AC-2.3: Given a goal that fits no existing kind, when started, then nothing is written; the user is told no kind fits, that none is invented, and the options: the feature loop, or contributing a kind (`campaigns/README.md` "Adding a campaign kind"). No kind-less instance is offered.
- [ ] AC-2.4: Given the kind's own "not startable" conditions (empty slice list, unset parity check, unset token budget), when the draft is written with them open, then they appear in AC-1.7's list. The command does not fill them to make the draft look complete.

### US-3 (Should): The command is safe to run twice and in the wrong place

> As a user, I want a second run or a bad name to be harmless, so that an existing instance is never lost.

**Acceptance criteria:**

- [ ] AC-3.1: Given `.spark/campaigns/<name>/` already exists, when the command is run with that name, then nothing is overwritten or merged; the existing instance and its Status are named and the user is asked for another name. *Best-effort (NFR-3).*
- [ ] AC-3.2: Given a name that is not kebab-case or is `campaigns`, when started, then it is refused with the reason before any file is written.
- [ ] AC-3.3: Given other instances under `.spark/campaigns/` with Status `approved` or `running`, when a new draft is requested, then the user is told once (a notice, not a block) and the draft may proceed; one-active-campaign is not enforced here (A6).
- [ ] AC-3.4: Given `${CLAUDE_PLUGIN_ROOT}` appears unexpanded in what the command sees, or `campaigns/` or `templates/campaign.md` cannot be read, when started, then nothing is written, the cause is stated, and no structure or tracker is invented (B14).
- [ ] AC-3.5: Given a `[kind]` argument naming no file in `campaigns/`, when started, then nothing is written and the kinds that do exist are named.
- [ ] AC-3.6: Given a repo with no `.spark/constitution.md`, or no `.spark/` at all, when started, then the command works the same and mentions neither; it creates `.spark/campaigns/<name>/` and reads no constitution (C10).

### US-4 (Must): Docs and the constitution say what is true when this ships

> As a reader of the README or the constitution, I want the start instructions and the command count to be correct, so that no document presents the old hand-start as the only way or the old count as current.

**Acceptance criteria:**

- [ ] AC-4.1: Given the change ships, when `README.md` §Campaigns and `campaigns/README.md` "Instantiating" are read, then they describe the command as the start path, the hand-start as still valid, and say: starting is the command's; **running** an instance is still hand-run by naming it; routing, the standing rule and project-local kinds remain unbuilt.
- [ ] AC-4.2: Given the release's PR head, when tracked files are searched for the count, then no statement says ten where it means all skills or commands; each hit is classified in evidence. Rule: a count of the plugin's skills as a total becomes eleven (`docs/family.md:16`; constitution §2 "ten slash commands", §9 "10 skills" at the Shape, Stack and Module lines); "ten ceremonies" of the loop stays ten, because `/campaign` is the eleventh skill but not a loop ceremony. `ROADMAP.md:35` ("five phases, five gates, ten ceremonies, seven agents") describes the loop and was read: it **stays**. `README.md:136` and `campaigns/README.md:66` ("the ten ceremonies have no campaign logic") are reworded by AC-4.1 to say the loop ceremonies. `docs/status.md:107,180,284` are classified at Plan; a dated v0.1.0 snapshot row is not edited (C9). This spec's own quotations of the old count are classified, not edited.
- [ ] AC-4.3: Given the release, when the version is read, then `.claude-plugin/plugin.json` carries a minor bump (a new optional command; nothing renamed or removed).
- [ ] AC-4.4: Given the release, when `/go-live` starts, then `.spark/constitution.md` §2 and §9 at the PR head state eleven where they mean all skills or commands, via an `Amendments` row written by `/charter` at the user's instruction. The feature's agents never edit the constitution (NFR-9); if it is stale at `/go-live`, the agent stops and tells the user to run `/charter`, and does not edit it. Only the user may waive this, recorded with their reason.
- [ ] AC-4.5: Given the order of work, when the loop runs, then the amendment sits **after `/increment`** (the skill must exist before any count says eleven) and **before `/peer-review` closes**, so the Reviewer sees the final tree; `/go-live` re-checks it. Until then no tracked doc says eleven.

### US-5 (Won't, cut by the user, C11): The command lists existing campaigns

> As a user returning to a repo, I want to see the instances and their Status, so that I know what exists. **Cut**: ID kept, not built, see §6.

- AC-5.1 (cut, not testable, not in scope): listing name, kind and Status when run without a name. Replaced by AC-1.8.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Attention budget | The new `SKILL.md` ≤ 70 lines (existing skills run 57 to 125); docs edits ≤ 25 added lines in total; zero lines added to any existing `SKILL.md`, to `agents/`, `templates/` or `campaigns/migration-campaign.md`. The constitution amendment is the user's `/charter` act, outside this count. If NFR-4's rules, or an NFR-3 fix round, cannot fit in 70 lines, the cap yields with the new count recorded, never a rule. | `git diff --stat` + `wc -l`, /peer-review |
| NFR-2 | Suppression | The command acts only when invoked. Recorded negative case, run first: in a repo that never runs it, the loop ceremonies' output has no diff, and an unrelated request that mentions migration does not start it. A repo without `.spark/campaigns/` is unchanged by installing this version. | Recorded dry run + /peer-review |
| NFR-3 | Honesty / reliability | Prompt material makes these checks likely, never certain: AC-1.4, AC-1.6, AC-2.1, AC-2.2, AC-3.1. QA runs each in 5 fresh sessions, each presenting the case the AC guards against (AC-1.6: every happy-path session), and writes the observed "n of m" per AC into `campaigns/README.md`, whatever the result. Floor: 3 of 5. An AC below it gets **one fix round**: the rule is moved or restated in `SKILL.md` at the step where the agent acts, then re-measured in 5 fresh sessions. Still below 3 of 5: that AC is recorded refuted-with-finding and the user decides ship or hold. The doc calls the checks best-effort, never "the command guarantees". Precedent: 13 of 19 for AC-1.4 under `campaign-core`. | /demo-day + /peer-review |
| NFR-4 | Rule placement | Each rule an AC depends on appears in the new `SKILL.md` from the first build, the file open when the agent must act, not only in a README: never approve or run; no overwrite; the one-goal and named-observable tests; the seven keys; file name `campaign.md` and reserved directory; exactly one file written; unresolved path means stop, no invented tracker; no commit. An NFR-3 fix round tightens a rule's wording or position there, it does not first introduce it. | /peer-review: grep each rule in `SKILL.md` |
| NFR-5 | Docs truth | Docs state: need anticipated not observed; one kind exists, so the command serves it only; no outside proof; effectiveness unmeasured. No doc claims the command makes a campaign safe, or that Core enforces anything. | /peer-review |
| NFR-6 | Library: public surface | Exactly one command added (`skills/campaign/SKILL.md`, frontmatter `name` = folder = slash command `campaign`); none renamed or removed; no change to the template's structure or any protected structure (constitution §3); `${CLAUDE_PLUGIN_ROOT}` paths only. The addition is a promise supported from release. | /peer-review |
| NFR-7 | Library: compatibility | An already-installed consumer on the old version loses nothing: hand-start and every existing instance work unchanged, including instances built before this command. | Recorded dry run (instance built by hand, run unchanged) |
| NFR-8 | Library: contract clarity | The new `SKILL.md` and README state input, output file, what is written, what is never written, and what happens on each refusal. | /peer-review |
| NFR-9 | Approval | Nothing this feature adds lets an agent set goal approval, a waiver or any Status beyond `draft`, edit the constitution, or commit. Constitution §6. | /peer-review + recorded planted-instruction run |
| NFR-10 | Stack | Zero new tracked executable code; `git ls-files '*.py'` empty; `claude plugin validate .` passes. | /peer-review |
| NFR-11 | Security / other lenses | `security` off (constitution §2). The kind body copied in is plugin-owned text, not project input; the skill reads nothing campaign-related from the target project except existing instances for AC-3.1/3.3. `.spark/campaigns/` is public: no secrets (§3). a11y/perf N/A (no UI or runtime). | /peer-review |

Active lens `library` (constitution): public surface, compatibility and contract clarity are NFR-6, NFR-7, NFR-8; its packaging section is N/A (no bundle, no dependencies).

## 6. Out of Scope

- **Scaffolding a new kind**, or reading any project-local kind: `campaign-core` US-6 and its gates; a kind is a contributor's file (ruled, C7).
- **A kind-less / generic campaign:** needs its own spec. A second upstream kind is the cleaner route and a separate feature (ruled, C7).
- **A second kind** (for example "close every open Major finding"): its own feature.
- **A doc-only paste-ready prompt** instead of the command: rejected by the user (C6).
- **Listing existing instances** (US-5, AC-5.1): cut by the user (C11). A second mode on a one-purpose command, for a need no one has shown; instances are plain files under `.spark/campaigns/` and a no-name run only asks for a name.
- **Running a campaign**, iterating, or picking up a halted one: still hand-run by naming the instance.
- **Routing** (proposing a campaign from `/spark` or `/story-time`) and the **standing rule / constitution flag**: Inc 2, and `/charter`'s.
- **Running the kind's planning roles** (Archaeologist, Strategist) from the command, and cutting the slice list (confirmed by the user, C8, C13).
- **Running the user's observable** to fill the veto record; the user, or the first run, does that.
- **The command editing the constitution**; the count correction is the user's `/charter` (AC-4.4). Other stale constitution facts (§2 cites version `0.8.0`) are not this feature's.
- **A `ROADMAP.md` Shipped row** for the command: a thing is Shipped only when exercised; the row is a later edit.
- **Enforcing** one active campaign per repo; any `aspark-guard` coupling; any `aspark-graph` change.
- **Approving**, setting `running`, committing, branching or any git action; migrating existing instances.
- Effectiveness claims, and reconciling the maturity contradiction (`campaign-core` A3).

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-10-04 | Is a skill the right shape? | Kept, narrowly: the skill is the only mechanism that resolves the plugin path (A3). Not routing, not a mode inside an existing skill: those touch every consumer's entry points (Inc 2) |
| C2 | 2026-10-04 | Does a start command make routing (US-3) or the standing rule (US-4) redundant? | No. Routing recognises and proposes; a start command creates. It precedes routing, which can then hand off to it. It never writes the constitution (A6) |
| C3 | 2026-10-04 | What must stay the user's? | Goal approval, every Status beyond `draft`, the token budget figure, any waiver, the veto record, the contract step, git commits (AC-1.5, AC-1.6) |
| C4 | 2026-10-04 | Edge cases | Existing name, bad name, unreadable plugin path, malformed kind, no fitting kind, several goals: AC-2.x, AC-3.x |
| C5 | 2026-10-04 | Truth-in-docs for the count | AC-4.2 and Q5; the constitution is the user's via `/charter` |
| C6 | 2026-10-04 | Q1 timing | **User: build the minimal slice now**, not a doc-only prompt, not wait for a real hand-run. The risk that the interview is guesswork stays in A1 |
| C7 | 2026-10-04 | Q2 "individual", Q3 command | **User:** an own instance of an existing kind only; kind-less and new-kind scaffolding are out (§6). Command `/campaign <name> [kind]`, no mode word; a later mode is additive, a rename is breaking (NFR-6) |
| C8 | 2026-10-04 | Q4 stop at the draft? | **Confirmed by the user** (C13). Stops at the draft and names the next step (AC-1.7); the kind's planning roles stay a user-run session. Reason: the kind already defines that session and an empty slice list is "not startable" anyway |
| C9 | 2026-10-04 | Q5 the count | **User:** correct the constitution with `/charter` in the same release. US-4 becomes Must, because the release depends on it (AC-4.4, order in AC-4.5). `ROADMAP.md:35` read: it counts the loop's ceremonies, `/campaign` is not one, so it stays |
| C10 | 2026-10-04 | Clarify pass defaults (PO, user may overrule at the gate walk) | Path resolution = the skill reads `${CLAUDE_PLUGIN_ROOT}` paths and stops if unexpanded or unreadable (AC-1.1, AC-3.4). Interview asks only what the kind leaves open (AC-1.5). Veto record blank, budget only as the user states it. No constitution needed (AC-3.6). B14's tracker invention is blocked by AC-3.4 and the one-file rule (AC-1.3), both written into `SKILL.md` (NFR-4). Docs rule: dated snapshot rows are not edited |
| C11 | 2026-10-04 | Q6 `/campaign` with no argument | **User:** show the usage line, ask for a name, write nothing (AC-1.8). US-5 (list instances) cut to §6, ID kept, not renumbered; no hedging left in AC-1.8 or NFR-11 |
| C12 | 2026-10-04 | Q7 poor rate on a best-effort check | **User:** floor 3 of 5 with one fix round (move or restate the rule in `SKILL.md`, re-measure); still below, the AC is recorded refuted-with-finding and the user decides ship or hold. The observed "n of m" goes into `campaigns/README.md` either way (NFR-3) |
| C13 | 2026-10-04 | Q4 confirmation | **User confirmed** stop at the draft and name the next step; planning roles are not run (AC-1.7, §6). Not a default awaiting overrule |

## 8. Design Review

- **Overall impression:** N/A. No UI: no screen, no markup; the artifact is a prompt file and Markdown docs; the accessibility lens is off per the constitution.
- **Heuristics findings:** N/A (no UI).
- **Accessibility notes:** N/A (no UI).
- **Design risks & required changes:** N/A (no UI).

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked
- [x] Open questions are resolved or explicitly accepted as risk
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review done for UI-facing features (or marked N/A with reason)
- [x] Line budget respected: Ist 186 / Soll ~250 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [x] Status set to `approved` by the user
