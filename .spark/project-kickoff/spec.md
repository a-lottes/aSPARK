# Spec: project-kickoff

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-09-18 |
| **Ticket** | `none` (constitution §7) |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `approved` — user approved the SPEC GATE 2026-09-18 after walking every row.
- **Summary:** Two entrances dead-end on a project without a constitution (`/spark` → `/next-steps` → "bring an idea"), and on an existing codebase three agents each re-derive the same system understanding because nothing user-confirmed records it. Fix: `/charter` becomes the single start-here, fills one bounded, evidenced **Project Context** section — a product brief always, a system picture where there is code — and PO/EM read that instead of "enough code". No new ceremony, no new role, no graph slice (cut by the user, §6 item 1).
- **Open:** `none` — A3, A5, A6, A7, A8 resolved 2026-09-18 (§3). A10 is parked for the plan gate by design, not a spec blocker.
- **Binding ruling:** §4 User Stories US-1…US-5; §6 for the cuts, each with its reopen condition; §7 C1–C9 for what the user decided and why.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Problem & Goal

- **Problem.** Three things, all verified 2026-09-18 against `main`:
  1. **No entrance for a project that has nothing yet.** `/spark` without an argument and nothing to resume offers `/next-steps` or "bring your own idea" (`skills/spark/SKILL.md:25-29`); `/next-steps` on an empty `.spark/` with trivial git history "asks the user for the first idea" (`skills/next-steps/SKILL.md:48-50`). Neither names `/charter`, and `README.md` §Usage (`:183-192`) starts at `/next-steps`. The one ceremony that could ask what the project *is* — `/charter` — is reached only by someone who already knows it exists.
  2. **The Facilitator has nothing to ground on in an empty repo.** Its method is "learn the terrain" (`agents/facilitator.md:43-45`); when it cannot ground a default it returns an ad-hoc question list (`:96-100`) aimed at constitution sections, not at the product. A structured interview exists nowhere; the PO's forcing questions live only per feature (`agents/product-owner.md:38-44`).
  3. **On an existing codebase, no shared system picture exists.** The PO reads "enough code" (`agents/product-owner.md:48-50`), the EM reads it again (`agents/engineering-manager.md:45-47`), the Facilitator a third time — each into its own context, none confirmed by the user. `templates/constitution.md` has no "what this project is" section; this repo's own constitution improvised one (`.spark/constitution.md:15-19`).
  **Who hurts:** the sole maintainer, on this repo (three agents re-reading per feature) and on his own first greenfield run — the only *measured* user (A2). A future consumer starting from the README is the intended user but unproven: no field report exists (`ROADMAP.md` "the one gap that matters most").
- **What is *not* the problem.** The loop is not broken without a constitution — that is a documented guarantee (`docs/workflow.md:18`, `skills/spark/SKILL.md:59`) and stays one. Nothing here may turn the offer into a block.
- **Goal.** One start-here command on both repo states, ending in ≤ 2 rounds with a constitution that carries a bounded, evidenced, user-confirmed Project Context; and the PO and EM cite it instead of re-deriving it.
- **Success signal.** (S1) Live on a repo with no constitution and nothing to resume: `/spark` and `/next-steps` each name `/charter` as the first step, verified by invocation. (S2) Greenfield, on an empty scratch repo: one `/charter` run ends with the section filled and a first slice named; the following `/story-time` on that slice asks **zero** questions the brief already answers. (S3) Brownfield, on aSPARK itself: in the first feature after the section exists, the count of system facts re-derived from source in `spec.md`/`plan.md` **without** a named AC-5.2 condition is **zero** (same counting method as `right-sizing` S2).
- **Why now.** Honestly: nothing breaks if this is never built. The cost is recurring (re-derivation per feature) and adoption-shaped (a first run that dead-ends is the cheapest reason nobody files the field report ROADMAP wants). It displaces the ROADMAP *Next* items (#13, #14, #15, #19), none of which addresses the first five minutes.

## 2. Target Users

- **The sole maintainer (`a-lottes`)** running `/spark` on this repo and starting new repos with aSPARK.
- **A developer installing aSPARK on a repo that already has code** — wants the team to understand the system before it specs anything. Unproven (no field report).
- **A developer installing aSPARK on an empty repo** — wants to be asked a few hard questions, not handed an empty template. Unproven.
- **The `facilitator`, `product-owner` and `engineering-manager` agents**, which today each build their own picture.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived as a solution: *"/charter detects the mode from repo signals … the user confirms, like the lens profile"*, *"a new bounded 'Project Context' section"*, *"aspark-graph gets a `charter` phase slice"*. Underlying need judged here: **a fast, uncomplicated start on both an empty and an existing repo, and one shared system understanding the team does not rebuild per feature** | recorded per PO rule; the solution parts are assessed in §4/§6, not adopted as given |
| A2 | The only measured user is the maintainer; the consumer pain is inferred from the README's entrance, not observed | accepted risk, bounded by NFR-7 (no claim beyond the two dogfood venues) |
| A3 | Neither sibling parses `constitution.md`. `aspark-graph`: `grep -r constitution ~/aSPARK-graph/src` → 0 hits (verified 2026-09-18; the fact `right-sizing` NFR-1 rested on). `aspark-guard`: not checked out here, so initially unknown | **RESOLVED 2026-09-18** from the installed guard source, `~/.claude/plugins/cache/aspark/aspark-guard/0.1.0`: `tests/test_rules.py:136-138` (`test_the_project_wide_constitution_is_never_blocked`) shows a constitution write is never gated, and `src/aspark_guard/templates.py:28-32` lists only `spec.md`, `plan.md`, `review.md`, `qa.md`, `release.md` for drift checks. An additive section is safe for both consumers; NFR-2 needs no coordinated release. Re-verified by the PO 2026-09-18 |
| A4 | The Facilitator has no Bash (`agents/facilitator.md:9`) and never will get one here (constitution §6: nothing executed unasked). "Git history is mandatory reading" therefore means the ceremony gathers it, as `/next-steps` step 1 does, and hands it over | accepted; AC-4.1 states the obligation, the plan decides the mechanics |
| A5 | `aspark-graph`'s whole query surface is `story_trace`, `impact`, `gate_health`, `staleness` (`~/aSPARK-graph/src/aspark_graph/cli.py:141-144`, verified 2026-09-18). None answers "what is this system"; `impact` needs file paths the discovery pass would already have found by hand | **RESOLVED 2026-09-18 — cut.** This contradicts the user's original wish (item 6 of the idea); the user decided the cut after seeing the query surface. §6 item 1 carries the reopen condition |
| A6 | Size caps for the Project Context: ≤ 35 lines total; product brief ≤ 12; system picture ≤ 25 | **RESOLVED 2026-09-18** — confirmed by the user as proposed (AC-2.3, NFR-6) |
| A7 | "Mode detection" collapses into the Facilitator's existing rule: fill what the evidence supports, ask for the rest in the interview, user confirms in one round. `greenfield`/`brownfield` is a recorded label on the section, not a detection step with a signal rule | **RESOLVED 2026-09-18** — accepted as recommended; no separate signal-rule step (§6 item 2) |
| A8 | `/next-steps` on a repo **with** code but **no** constitution: recommend `/charter` first, proceed on the user's explicit "skip" | **RESOLVED 2026-09-18** — accepted; offer, never block (AC-1.2, AC-1.3) |
| A9 | The greenfield dogfood venue is an empty git repo created as untracked scratch **outside** this working tree (constitution §3: the published surface is the whole tree) with results written to `.spark/project-kickoff/evidence.md` | accepted |
| A10 | If the increment cannot carry both `Should` paths, which ships first — US-3 (greenfield, the user's first-stated pain) or US-4 (brownfield, the one this repo proves on itself)? | **Parked for `/sprint-plan`** by the user's ruling 2026-09-18 — a plan-gate decision, not a spec blocker. The spec is complete with either order |

## 4. User Stories

### US-1 (Must): A project without a constitution is routed to `/charter` first

> As a developer starting aSPARK on a repo, I want the first command I try to point me at `/charter`, so that I am not bounced between two ceremonies that each assume the other has run.

**Acceptance criteria:**

- [ ] AC-1.1: Given a repo with no `.spark/constitution.md` and nothing to resume (empty `.spark/`, or every feature `released`/`handed-off`), when `/spark` runs without an argument, then its reply names `/charter` as the first step and offers it, and does not offer `/next-steps` ahead of it. It never invokes `/charter` itself.
- [ ] AC-1.2: Given any repo with no `.spark/constitution.md` — empty or with code — when `/next-steps` runs, then it recommends `/charter` first instead of asking for the first idea, proceeds to the PO brief only on the user's explicit skip, and still writes nothing under `.spark/`.
- [ ] AC-1.3: Given the user declines or skips `/charter` in AC-1.1 or AC-1.2, when the ceremony continues, then it does exactly what it does today (`/next-steps` or "bring your own idea"; the PO brief with "constitution: none") — an offer, never a block.
- [ ] AC-1.4: Given a repo with no constitution, when `/spark <idea>` or `/story-time <idea>` runs, then nothing differs from today: the one-line lens nudge, no new question, no stop. The loop still runs without a constitution.
- [ ] AC-1.5: Given a repo **with** a constitution, when `/spark` (no argument) or `/next-steps` runs, then the reply contains no sentence added by this feature.
- [ ] AC-1.6: Given `README.md`, when read top-down, then a **Start here** block of at most 10 lines precedes §Usage's `/next-steps` example and names `/charter` as the first command on both an empty and an existing repo.

### US-2 (Must): `/charter` writes one bounded, evidenced, user-confirmed Project Context

> As the user running `/charter`, I want the constitution to record what this project is — in the shape the repo supports — so that every later phase reads one confirmed picture instead of building its own.

**Acceptance criteria:**

- [ ] AC-2.1: Given `templates/constitution.md` diffed against `main`, when read, then exactly one section is added — **Project Context** — holding two blocks: a **product brief** (always) and a **system picture** (only where the repo has source files or a manifest to picture), plus a one-word label `greenfield` or `brownfield`. Sections §1–§8 keep their numbers and headings; `skills/spark/SKILL.md:74` and `skills/demo-day/SKILL.md:28` still resolve "§8" to QA Method.
- [ ] AC-2.2: Given a first-draft `/charter` on any repo, when the Facilitator's draft is presented (existing step 3), then the Project Context is shown as its own decision, each entry marked `inferred from <file:line>` or `asked`, and the user confirms or corrects it in the **same** round as the profile and QA method — no extra round, no new numbered step, no separate mode-detection step (A7).
- [ ] AC-2.3: Given the confirmed section, when its lines are counted, then it is ≤ 35 lines in total, the brief ≤ 12 and the picture ≤ 25 (A6); what does not fit is pointed to (README, `CLAUDE.md`, docs) rather than duplicated.
- [ ] AC-2.4: Given a constitution written before this change (this repo's at `main`, any consumer's), when any ceremony reads it, then nothing differs from today: no warning, no migration, no prompt. The section is added only by a `/charter` amendment the user asks for.
- [ ] AC-2.5: Given the section exists and a later phase finds the code contradicts an entry, then that phase records the contradiction where it works (spec §3 / plan risk / review finding) and points to `/charter`; it never edits the constitution.
- [ ] AC-2.6: Given any entry in the section, when checked, then it is falsifiable: a system-picture line carries a `file:line` or a command whose output is quoted; a brief line is `confirmed by user` or `inferred from <file>`; an unknown reads `not stated` / `not found`, never a guess.

### US-3 (Should): On an empty repo, `/charter` runs a structured kickoff interview

> As a developer starting from nothing, I want `/charter` to ask me the few hard product questions in one go, so that the constitution and the first slice come out of my answers instead of an empty template.

**Acceptance criteria:**

- [ ] AC-3.1: Given a first-draft `/charter` on a repo where the evidence answers none of the product questions (typically: no source files, no manifest), when the Facilitator returns, then it returns **one** numbered list of at most 7 questions covering exactly: who the user is, what problem they have today, the smallest version that helps, the success signal, stack (a choice or "let the EM decide"), non-negotiables, and the first slice to build — and asks nothing else in that round. On a repo where the evidence answers some of them, only the unanswered ones are asked (A7).
- [ ] AC-3.2: Given the answers, when the constitution is drafted, then the brief is filled from them; §3 stack reads either the named stack or `undecided — the EM proposes at the first /sprint-plan`; §6 carries the named non-negotiables; §2 profile reads `undetectable — from the user's answers` with the lens decision still explicit (constitution §1: no lens on silently).
- [ ] AC-3.3: Given a first-slice answer, when `/charter` ends, then it offers `/story-time <first slice>` and invokes it only on the user's explicit go — never automatically (mirrors `skills/next-steps/SKILL.md:66-70`).
- [ ] AC-3.4: Given a question the user skips, when the draft is written, then that entry reads `not stated` and the ceremony continues; nothing blocks on a skipped answer.
- [ ] AC-3.5: Given the greenfield dogfood (A9), when the transcript is counted, then `/charter` completed in at most 2 relay rounds (interview, then confirmation) — recorded in `evidence.md`.

### US-4 (Should): On an existing repo, `/charter` runs a short discovery pass the user confirms once

> As a developer installing aSPARK on a codebase, I want the team to write down what it found — with evidence — and let me correct it once, so that the first feature starts from a picture I vouch for.

**Acceptance criteria:**

- [ ] AC-4.1: Given a repo with source files or a manifest, when `/charter` first-draft runs, then the ceremony hands the Facilitator a git-history summary it gathered itself (A4), and the Facilitator reads `README.md`, `CLAUDE.md` and `.spark/` specs where present before drafting; the draft names what was read and what was `absent`.
- [ ] AC-4.2: Given the draft, when the system picture is read, then it carries exactly these seven entries: stack & entry points · module structure · data model · test practice · conventions · how to run · known pain points — each with ≥ 1 `file:line` or `not found`.
- [ ] AC-4.3: Given the draft, when the user corrects an entry, then the correction is folded in without a second discovery pass, and the whole `/charter` completes in at most 2 rounds (AC-3.5's bar, brownfield venue).
- [ ] AC-4.4: Given a repo with no README, no `CLAUDE.md`, or no git history, when the pass runs, then each missing input is recorded `absent` and the pass continues on what exists.
- [ ] AC-4.5: Given the brownfield dogfood on aSPARK, when `/charter` amends this repo's constitution, then the improvised "What this project is." paragraph (`.spark/constitution.md:15-19`) moves into the new section unchanged in meaning, an Amendments row records it, and no other line of the constitution changes.

### US-5 (Should): The PO and the EM read the Project Context instead of re-deriving it

> As the PO or EM starting a feature, I want to cite the confirmed picture and read code only for what the feature touches, so that the loop stops paying three times for one understanding.

**Acceptance criteria:**

- [ ] AC-5.1: Given a constitution with a Project Context, when `/story-time` or `/sprint-plan` runs, then the agent reads it before any code and cites it (`constitution.md §<n>`) for system facts used in spec §1/§2 and in the plan's ADR context / Affected Components.
- [ ] AC-5.2: Given the rule, when the agent instructions are read, then they name the conditions under which reading source is still required: (a) the feature touches that area, (b) the entry is `not stated`/`not found`, (c) the agent has a concrete reason to doubt the entry — and an artifact that re-derives names which condition applied.
- [ ] AC-5.3: Given a constitution without the section, or no constitution, when `/story-time` or `/sprint-plan` runs, then the PO and EM behave exactly as today (`agents/product-owner.md:48-50`, `agents/engineering-manager.md:45-47`).
- [ ] AC-5.4: Given the first feature on aSPARK after AC-4.5 lands, when its `spec.md` and `plan.md` are read, then the count of system facts re-derived from source without a named AC-5.2 condition is zero (S3).

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | `library` §1 — public surface | Zero new slash commands, agents, lenses, tools or template files; zero new `${CLAUDE_PLUGIN_ROOT}/…` paths resolved by any skill. `skills/` still holds 10, `agents/` 7. `/charter`'s numbered steps stay at 5 — the interview, discovery and confirmation live inside its existing steps 1–3 | /peer-review |
| NFR-2 | `library` §2 — compatibility & versioning | Additive only: the §3 protected-structure table is untouched, and `constitution.md` is not in it. Neither consumer reads the constitution — `aspark-graph` (0 hits in `src/`) and `aspark-guard` (`tests/test_rules.py:136-138`, `src/aspark_guard/templates.py:28-32`; A3) ⇒ **minor** bump, no coordinated release. §1–§8 numbering is a de-facto contract (cited by skills) and is preserved (AC-2.1) | /peer-review; the A3 citations re-checked and recorded in `evidence.md` |
| NFR-3 | `library` §4 — contract clarity | The new section's own template comment states: default when absent (readers behave as today), sole writer (`/charter`), the size caps, and what it is not (not a design doc, not per-feature). The kickoff questions and the PO's per-feature forcing questions are each stated in exactly one file; `grep` for the literal first question of each returns one file | /peer-review |
| NFR-4 | Degrade to silence (constitution §6) | No constitution, declined or skipped `/charter`, pre-change constitution: every ceremony behaves as today, verified **negative case first** — one run in a repo without a constitution and one on this repo's constitution before AC-4.5 amends it | documented dry run in `evidence.md`, then /demo-day |
| NFR-5 | Testing bar (constitution §4, §8) | `claude plugin validate` passes on the branch; then three performed runs, each with quoted output: negative case (NFR-4), greenfield on the scratch repo (A9), brownfield on aSPARK. A read of a Markdown file is never a performed step | /demo-day |
| NFR-6 | Ceremony weight (ROADMAP: no new ceremony weight) | Interview ≤ 7 questions, `/charter` ≤ 2 rounds on both venues, Project Context ≤ 35 / 12 / 25 lines (A6). No new numbered step in any skill. On a project that already has a constitution, the number of sentences this feature adds to any ceremony run is 0 (AC-1.5, AC-2.4) | /peer-review (diff) + /demo-day (transcript counts) |
| NFR-7 | Honesty of claim (constitution §1, §4) | README §Project Status and ROADMAP label the greenfield path as proven on a sample repo only and the brownfield path on aSPARK only; no sentence claims a saving on external projects or a field-verified first run | /peer-review |
| NFR-8 | Nothing executed unasked (constitution §6) | `/charter` never invokes `/story-time`, never builds a graph, never writes outside `.spark/constitution.md`; git commands it runs are read-only | /peer-review + /demo-day |

- **Accessibility / performance:** N/A — no UI, no runtime (constitution §4).
- **`library` §3 packaging & footprint:** N/A per constitution §2 — no bundle, no dependencies.

## 6. Out of Scope

Each cut names what would reopen it.

1. **An `aspark-graph` `charter` phase slice.** The graph's four queries (A5) answer traceability and blast-radius questions, not "what is this system"; a slice would tell the Facilitator to call `impact` on entry points it already found by hand. **This contradicts the user's original wish (idea item 6); the user decided the cut on 2026-09-18 after seeing the query surface.** **Reopens** when the graph ships a repo-summary query; then per `tools/README.md` — canonical probe bullet, four states, negative case first.
2. **Mode detection as a step with a signal rule** (no source / no manifest / trivial history). Replaced by "fill what the evidence supports, ask the rest" (A7, user-accepted). **Reopens** if the dogfood shows the Facilitator proposing the wrong shape.
3. **A new `kickoff` ceremony or a new role.** The Facilitator asks the product-level questions; the PO's per-feature interrogation in `/story-time` is unchanged.
4. **Auto-invoking `/story-time` after `/charter`** — constitution §6.
5. **Keeping the system picture fresh automatically.** It is dated and amended via `/charter`; a phase that finds it wrong points there (AC-2.5). **Reopens** with a field report showing staleness bites.
6. **Changing `/story-time`'s or `/spark <idea>`'s no-constitution behaviour** beyond today's nudge (AC-1.4).
7. **Migrating other projects' constitutions** — only this repo's, as the brownfield dogfood (AC-4.5).
8. **A general constitution line budget or gate** (`right-sizing` A4 routed it to `/charter`); only the new section is capped.
9. **Website/handbook sync** (`~/aSPARK Webseite` mirrors the handbook) — a separate obligation, tracked in memory, not this diff.
10. **Lens detection signals** (`lenses/README.md`) — unchanged; the profile decision stays as it is.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-18 | Is "mode detection" needed, or does one interview that degrades by evidence suffice? | **User: one flow, as recommended.** The Facilitator fills what the evidence supports, asks the rest in the interview, confirms in one round; `greenfield`/`brownfield` is a recorded label only (AC-2.1, AC-2.2, AC-3.1). No signal-rule step (§6 item 2) |
| C2 | 2026-09-18 | Should the optional `aspark-graph` slice be built? | **User: cut**, deciding against their own original wish after seeing that no discovery-shaped query exists (A5). §6 item 1 with reopen condition |
| C3 | 2026-09-18 | How big may the Project Context be? | **User: confirmed** 35 / 12 / 25 lines (A6, AC-2.3, NFR-6) |
| C4 | 2026-09-18 | Does a "Project Context" violate "principles and constraints only, never per-feature"? | No — it is project-wide, like the profile in §2, and this repo's constitution already carries one (`:15-19`). The risk is it growing into a design doc, hence AC-2.3/AC-2.6 |
| C5 | 2026-09-18 | `/next-steps` on a repo with code but no constitution — route to `/charter` or leave as today? | **User: recommend `/charter` first, proceed only on explicit skip** — offer, never block; the "loop runs without a constitution" guarantee stays (AC-1.2, AC-1.3, NFR-4) |
| C6 | 2026-09-18 | Which persona asks the greenfield questions? | The Facilitator, in `/charter` — no new role. The questions are stated once (NFR-3); how the Facilitator reaches the PO's list is the plan's call |
| C7 | 2026-09-18 | Roles & permissions | N/A — no actor beyond the user, no data; `/charter` remains the sole writer of the section (AC-2.5) |
| C8 | 2026-09-18 | Does this feature touch the sibling parsers? | **No, both verified.** `aspark-graph`: 0 hits. `aspark-guard`: `tests/test_rules.py:136-138`, `templates.py:28-32` (A3). NFR-2's coordinated-release condition removed |
| C9 | 2026-09-18 | Which `Should` path ships first if only one fits the increment? | **Parked for `/sprint-plan`** (A10) — a plan-gate decision, not a spec blocker |

## 8. Design Review

*N/A — not UI-facing. aSPARK Core ships Markdown prompt material with no rendered surface (constitution §4 "N/A — no UI", §8 "Browser-observable surface: no"); what this feature changes is the wording of ceremony replies and one template section, which `/look-and-feel`'s heuristics have nothing to inspect. Verification is by performed ceremony runs (NFR-5), not by a Designer pass.*

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C8 resolved, C9 parked for the plan gate by the user's ruling
- [x] Open questions are resolved or explicitly accepted as risk — A2 accepted risk; A3, A5–A8 resolved 2026-09-18; A10 explicitly parked for `/sprint-plan`
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review done for UI-facing features (or marked N/A with reason)
- [x] Line budget respected: Ist 180 / Soll ~250 (excluding HTML comments; the file carries none)
- [x] Status set to `approved` by the user
