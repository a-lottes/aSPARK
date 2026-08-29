# Spec: graph-gates-verification

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-25 |
| **Ticket** | none |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this spec updates it in the same edit that resolves a clarification or
     changes status: overwrite in place, never append. The block holds one current
     state, never a per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). **Approved by the user at the spec gate, 2026-08-25** — Q6 ruled (C15) alongside C9–C13; Clarify pass fully folded (C14); zero open questions. Next ceremony step: `/sprint-plan`.
- **Summary:** Verify live what the graph-gates release could only verify on paper — issues #8–#11 plus AC-3.2's ceremony side — under a verify-only fence: the deliverable is written evidence, not code.
- **Open:** `0 open` — nothing from clarify; next stop = user gate.
- **Binding ruling:** §4 User Stories (execution order = ID order, negative case first; sole sanctioned exception: AC-3.3 runs after US-4); §7 Clarifications for decisions already folded.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem.** The graph-gates release (v0.4.0) shipped six acceptance criteria as
  documented `partial`s, each with a structural reason it could not be verified live
  at the time. Four are re-opened as GitHub issues: #8 (MCP-first precedence,
  AC-2.2 — no session ever had the server registered), #9 (`/demo-day`'s no-browser
  stop path, AC-3.5 — overridden by the user in the only run that reached it),
  #10 (Playwright MCP and Chrome DevTools MCP as browser backends — named in shipped
  skill prose, never once confirmed to drive a page), #11 (installed-but-unbuilt hint
  fires exactly once, AC-3.2's sibling AC-2.3 — reproduced at tool level, never
  counted inside a live ceremony transcript). After the release, the blocking
  environment defect (QA finding B2: runner stranded in a venv off `PATH`) was fixed,
  so the Offer state is reachable and the "no venue exists" reason has expired.
  Meanwhile `README.md` §Project Status publishes "six ship as a documented
  `partial`" — a true statement that ages into a false one if the proofs are never run.
- **Who hurts.** The solo maintainer-operator (population ≈1, the same dual-tool
  operator graph-gates serves), and every future `/demo-day` user on a web-app
  project who reads the gear-check line naming three browser backends and trusts it.
- **Goal.** Each of #8–#11 becomes closeable with a link to a written evidence row
  whose observation is a performed step and a counted number — or, where verification
  surfaces a defect, the defect is precisely recorded and routed. Honesty about
  maturity is upgraded in both directions: proven where proven, refuted where refuted.
- **Success signal.** An evidence record in this feature's `.spark/` trail in which:
  the silence case ran first; every claim cites a command or ceremony invocation with
  captured output; the counts are literal (zero probe commands in the MCP session;
  exactly one hint sentence; zero tool mentions on the stop path; per-backend
  recognized-and-interacted verdicts); and the environment is restored. Any AC that
  fails becomes a finding, not a fix.
- **Why now.** The venue blocker expired after release; the issues are open debt on a
  published honesty claim; and the MCP branch of the precedence rule is today a
  plausible fiction — if `aspark-graph serve` is broken, degradation is silent by
  design and only a live attempt will say so.

## 2. Target Users

- **The dual-tool operator (primary, ≈1).** Runs Core and install-from-source
  `aspark-graph` together; relies on the precedence rule, the hint and the stale rule
  behaving as documented. Issues #8, #9, #11.
- **The maintainer (primary for the process).** Published "six partials" in the
  README and wants that line either retired by proof or sharpened by refutation.
- **The future web-app adopter of `/demo-day`.** Reads "Claude in Chrome, Playwright
  MCP, Chrome DevTools MCP — whatever the session offers" and plans tooling around it.
  Issue #10.

Not a user: end users of products built with aSPARK; this feature ships no runtime
surface and changes no behavior.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived solution-shaped ("run a live-verification sweep for #8–#11"). Underlying need, restated: *the shipped capability's claims must be upgraded from paper to performed evidence, or the defects beneath them named and routed.* Original phrasing kept here per the no-solutions rule. | Accepted framing — verify-only, evidence is the deliverable |
| A2 | Prompt material has no automated test suite (constitution §4); the written record of performed runs *is* the test suite. Reading Markdown and reasoning about it is never a performed step — the standard the graph-gates QA itself set. | Standing assumption — Risk R3/R5 |
| A3 | Environment baseline, asserted from the graph-gates QA trail but **to be re-verified, not trusted**, at sweep start: `~/.local/bin/aspark-graph` symlink present (runner on `PATH`); `~/aSPARK` resolves `runner=yes, graph=no`; `~/aSPARK-graph` is `stale:false` and must remain untouched — all stale-graph work happens in disposable scratch copies (round-2 precedent). | Accepted — Risk R6 |
| A4 | Issue↔target mapping: #8→AC-2.2, #9→AC-3.5, #11→AC-2.3, #10→the gear-check prose claim (no single AC). Of the remaining three partials: AC-3.2 included as Should (US-6); AC-1.2 and AC-5.2 excluded (§6). | Confirmed by user — C11/C12 |
| A5 | This feature produces closeable evidence; closing issues #8–#11 is the user's act at `/go-live`, not part of the diff. | Accepted |
| Q1 | **Venue for #10:** which HTTP app may `/demo-day` target for the backend confirmations? | **Ruled (C9):** throwaway locally served static page — proposed default confirmed; detection plus one real navigation/assertion suffices. Page and server live in declared disposable scratch *outside* this repo, keeping the NFR-1 fence intact. |
| Q2 | **Authorization for #8:** registering the `aspark-graph` MCP server is environment mutation the tool file forbids agents to perform unasked (`serve`). Authorized, scoped project-local to the positive venue? | **Ruled (C10):** authorized, project-scoped to the positive venue only; user accepts a `serve` failure routes to the consumer repo as a finding. Grant originally limited to this server; browser-backend registration was split into Q6 and granted on the same terms (C15). |
| Q3 | **Scope ruling:** include AC-3.2's ceremony side as US-6 (Should)? | **Ruled (C11):** included as US-6 (Should). |
| Q4 | **Exclusion confirmation:** AC-1.2 and AC-5.2 cut per §6? | **Ruled (C12):** confirmed — both stay cut, recorded reasons stand. |
| Q5 | **README permission:** may this feature edit `README.md` §Project Status? | **Ruled (C13):** granted — the proof statement follows the evidence in the same change; it remains the ONLY non-`.spark/` edit. NFR-1/NFR-9 worded accordingly. |
| Q6 | **Browser-backend registration (surfaced by the Clarify pass):** US-4 needs Playwright MCP and Chrome DevTools MCP available in their sessions. Does Q2's grant extend to the sweep registering them (project-scoped, logged/restored per AC-1.2) — or will the user register them beforehand (agents then perform zero registration mutations) — or is backend registration unauthorized (US-4 restructures)? Not stretched by analogy because backend registration executes third-party packages (`npx …`), a stronger mutation than serving a local build. | **Ruled (C15):** the sweep registers Playwright MCP and Chrome DevTools MCP itself, under exactly the terms of #8's grant (C10): registration authorized, project-scoped to the positive venue only, every mutation logged with authorization and restoration per AC-1.2's pattern. No user pre-registration; US-4 keeps its structure. |

## 4. User Stories

### US-1 (Must): The sweep's environment preparation leaves the absent case silent

> As a user on a project without `aspark-graph`, I want the negative case re-proven
> first and the environment left as found, so that collecting evidence for someone
> else's optional tool never regresses the normal loop.

**Acceptance criteria:**

- [ ] AC-1.1: Given the baseline probe recorded at sweep start in a neutral shell, when a wired ceremony's step 1 runs in a repo resolving `surface=no, graph=no`, then the transcript contains zero ceremony-emitted mentions of `aspark-graph`/`.aspark-graph`, the probe exits 0, and no gate outcome differs.
- [ ] AC-1.2: Given every environment mutation this sweep performs (symlink use, MCP registration, scratch builds), when the evidence is written, then each entry names its authorization and its restoration, and a post-sweep neutral-shell probe resolves identically to the baseline.
- [ ] AC-1.3: Given the finished evidence record, when its runs are read in order, then the silence case precedes every positive-case run, and each row cites what was actually executed.

### US-2 (Must): MCP-first precedence is observed, not just documented (#8)

> As a dual-tool operator, I want the documented precedence seen deciding a real
> resolution in a session where both surfaces exist, so that determinism is an
> observation rather than a paragraph.

**Acceptance criteria:**

- [ ] AC-2.1: Given a session with the `aspark-graph` MCP server registered (project-scoped, per Q2) exposing its tools under whatever names registration produces (cited literally in the evidence), and a source-indexed scratch repo with a built graph passing the ceremony gate, when a wired ceremony resolves availability, then it takes the MCP branch — names those MCP tools as the surface and executes zero probe commands (counted, == 0).
- [ ] AC-2.2: Given the same environment, when a second run resolves availability, then it resolves identically (same branch, same declared surface).
- [ ] AC-2.3: Given a no-MCP session on the same scratch repo, when resolution runs, then it takes the CLI branch — the two branches together demonstrate the order, not one data point.
- [ ] AC-2.4: Given the registration attempt fails or the tools never appear, when the evidence is written, then the exact failure (command, output, traced cause in the consuming repo) is recorded as a finding for that repo — #8 is never silently skipped.

### US-3 (Must): The no-browser stop path holds with the graph available (#9)

> As a `/demo-day` user without browser tooling, I want the ceremony to stop with
> exact setup instructions regardless of graph availability, so that an available
> accelerant never papers over a missing prerequisite.

**Acceptance criteria:**

- [ ] AC-3.1: Given a feature whose review is `passed` (so the review gate is not the stopper), no browser backend in the session, and an unreachable app URL, when `/demo-day` runs its step-1 gates, then it stops at the gear check with a message naming exactly what to set up or start, and no `qa-tester` delegation occurs.
- [ ] AC-3.2: Given the same stop-path run performed where the environment would resolve `surface=yes, graph=yes` (verified by a direct probe beforehand), when the stop fires, then the tool-resolution sub-step is never reached: zero probe executions, zero hint sentences, zero tool-file handovers — each counted, == 0.
- [ ] AC-3.3: Given a control run using a backend confirmed under US-4, when `/demo-day` passes the gear gate, then it proceeds past step 1 — showing the stop tracks the missing prerequisite, not ceremony refusal. *(Depends on US-4; the one sanctioned break of ID-order execution — it runs after US-4 and is cited back into US-3's evidence.)*

### US-4 (Must): Each named browser backend is confirmed or refuted by a performed interaction (#10)

> As a `/demo-day` user on a web-app project, I want every backend the gear check
> names to be proven able to drive a real page, so that the promise rests on
> evidence instead of plausible names.

**Acceptance criteria:**

- [ ] AC-4.1: Given a session where Playwright MCP is available because the sweep registered it itself under the C10/C15 grant (project-scoped, logged and restored per AC-1.2), and an HTTP app serving on localhost — a throwaway static page from disposable scratch outside this repo (Q1) — when `/demo-day` evaluates the gear check, then the transcript records Playwright MCP as the detected browser tooling and the gate passes on that basis.
- [ ] AC-4.2: Given the same session, when the QA interaction proceeds minimally, then the log contains ≥ 1 navigation to the app URL and ≥ 1 assertion of on-page content, each attributable to the backend's own action identifiers.
- [ ] AC-4.3: Given a separate session where Chrome DevTools MCP is available (self-registered under the same C10/C15 grant), when AC-4.1 and AC-4.2 are repeated, then the same two observations are recorded for that backend.
- [ ] AC-4.4: Given any backend failing at any step (availability, detection, interaction), when the evidence is written, then every failed attempt is logged with failure mode and reproduction steps; a backend is confirmed only if some attempt completes the full pass, refuted only if no attempt does, and instability across attempts is recorded in the verdict — never silently dropped.

### US-5 (Must): The installed-but-unbuilt hint fires exactly once (#11)

> As an operator with the runner installed but no graph built, I want one hint
> sentence and a normal completion, so that I get the pointer without nagging and
> without an unrequested build.

**Acceptance criteria:**

- [ ] AC-5.1: Given a scratch Core-managed trail whose plan gate passes, with `runner=yes, graph=no` (verified beforehand), when a wired ceremony runs start to finish, then its complete emitted output — ceremony messages, produced artifact, subagent reports — contains exactly **1** occurrence of the one-sentence hint naming `aspark-graph build`.
- [ ] AC-5.2: Given the same run, when it completes, then no `build`/`install`/`serve` was executed by any participant, and no `graph.json` came into existence.
- [ ] AC-5.3: Given that loaded skill/tool files legitimately contain the tool's name, when the count is taken, then the method counts ceremony-emitted output and artifacts only — not file contents loaded into context — and the method is stated in the evidence so the number is reproducible. *(B7 lesson.)*

### US-6 (Should): A stale graph is announced once and then treated as absent (AC-3.2, ceremony side)

> As a dual-tool operator, I want a ceremony meeting a stale graph to say so once
> and fall back to reading, so that confidently wrong graph answers never enter a
> review. *(Tool side verified twice in the graph-gates QA; only the ceremony's
> reaction remains.)*

**Acceptance criteria:**

- [ ] AC-6.1: Given a scratch source-indexed repo with a built graph whose indexed source is edited afterwards (`staleness` → `stale:true`, verified by a performed query), when `/peer-review` runs with the tool file handed over, then the report states the staleness once and cites zero graph results as evidence thereafter (counted).
- [ ] AC-6.2: Given the same run, when it concludes, then the verdict rests on at least one finding or verification anchored at a concrete `file:line` read directly — the fallback demonstrated, and the normal verdict still reached.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Footprint *(library §1)* | `git diff --name-only` over the whole feature touches `.spark/graph-gates-verification/**` and `README.md` §Project Status — the latter granted under Q5 as the sole non-`.spark/` change — and nothing else. Zero new commands/agents/ceremonies; counts stay 10 skills / 7 agents. | `/peer-review` + `git diff` |
| NFR-2 | Compatibility *(library §2)* | Verify-only: `skills/`, `agents/`, `tools/`, `lenses/`, `templates/`, `.claude-plugin/plugin.json` byte-identical; no version bump, no protected structure touched (constitution §3). A surfaced defect routes to findings — it never widens this diff. | `/peer-review`: empty diffs over those paths |
| NFR-3 | Contract clarity *(library §4)* | Wherever evidence contradicts documented behavior (tool-file §Availability rows, `/demo-day` gear-check prose), the finding quotes the contradicting text verbatim with `file:line` — drift is named, not absorbed. | Findings in the evidence record |
| NFR-4 | Evidence bar *(constitution §1, §4)* | Every AC's evidence is a performed step with captured output (command/ceremony, venue, timestamp, resolved availability facts, exit codes); reading or reasoning is labelled as such and never passes an AC. Negative case first (US-1). | QA-gate read of the evidence record |
| NFR-5 | Countability | Every "zero"/"exactly once" claim is stated as a counted number with its counting method named — including the exclusion of loaded-file contents from transcript counts (AC-5.3). | Evidence record, reproducible by re-count |
| NFR-6 | Safety — nothing unasked *(constitution §6)* | No `build`/`install`/`serve` executed on any user repo; writes confined to declared disposable scratch venues; every environment mutation — including the sweep's own registrations of `aspark-graph`, Playwright MCP and Chrome DevTools MCP — logged with authorization and restoration (AC-1.2). | Evidence audit + before/after probes |
| NFR-7 | Reliability / scale | N/A — no runtime; the cost is spend and agent attention, bounded by preferring single-step observations over full ceremony runs wherever an AC allows. | N/A (recorded) |
| NFR-8 | Accessibility | N/A — no UI. | N/A |
| NFR-9 | Observability / honesty *(constitution §1)* | `README.md` §Project Status states the post-sweep proof state literally: proven becomes proven, refuted becomes refuted-with-finding, anything not run stays labelled unproven. | `/peer-review` of README against the evidence |

*Lens coverage: `library` is the only active lens — §1→NFR-1, §2→NFR-2, §4→NFR-3;
its §3 (packaging) is the constitution's declared N/A. All other lenses are off.*

## 6. Out of Scope

Consciously cut. Each line is a documented "no".

- **Any fix for anything the sweep surfaces.** Defects route back through findings to
  a later `/increment`; no repair is pre-authorized in this feature.
- **Every edit to `skills/`, `agents/`, `tools/`, `lenses/`, `templates/`,
  `plugin.json`** — including the open one-line doc gaps B9/B10/B11 and the parked
  `bad_range` documentation in `tools/aspark-graph.md`: real Core-side fixes that
  need their own change, not a smuggle into a verify-only diff. `templates/` is
  additionally protected by the constitution §3 cross-repo contract.
- **Consumer-repo defects** (artifact-filename mismatch, `_parse_qa` column, anything
  #8's MCP attempt uncovers) — constitution §3: neither Core's to fix; filed where
  they live.
- **AC-1.2** (byte-level artifact diff between 0.3.1 and 0.4.0 runs): the residual
  half costs two full ceremony pairs on outdated plugin versions; its information
  gain over the live step-count, gate-order and silence evidence already recorded is
  marginal, and C13 narrowed it to the wired ceremonies US-1 re-covers anyway.
- **AC-5.2** (the `files:` omission branch): needs a manufactured plan containing a
  genuinely unknowable task — a contrived venue tests the fixture, not the behavior;
  the honest venue is a future real plan that happens to contain one.
- **Repeating the hint-count across the second and third wired ceremonies** (state 3):
  diminishing returns against documented spend limits; reopen if the first count
  surprises.
- **Closing or editing GitHub issues #8–#11** — the user's act at `/go-live`; this
  feature produces the evidence that makes closing defensible.
- **A full `/demo-day` QA ceremony against a real product**: #10 asks whether the
  backends work, not for a product QA; the minimal detection-plus-one-interaction
  proof is the slice.
- **Automated tests** — impossible for prompt material (constitution §4).
- **Any configuration, opt-in or opt-out** — verification changes no behavior, so
  there is nothing to toggle.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-25 | Functional scope: do the four issues cover all outstanding partials? | No — six exist. Four map to the issues (A4); AC-3.2 added as US-6 (Should, Q3 confirms); AC-1.2 and AC-5.2 cut with reasons (§6, Q4 confirms). |
| C2 | 2026-08-25 | Data & evidence: what counts as "the deliverable"? | A written evidence record in this feature's `.spark/` trail; every row a performed step with counted numbers (NFR-4/5). No artifact of the verified feature is modified. |
| C3 | 2026-08-25 | Roles & permissions: who registers the MCP server and mutates `PATH`-adjacent state? | Agents must not; these are user-authorized environment preparations (Q2), logged per AC-1.2, project-scoped, restored after. |
| C4 | 2026-08-25 | Error & edge-case behavior: what if verification *fails* — does the sweep fix? | No. A failed AC is itself a valid outcome: record reproduction, route as a finding (AC-2.4, AC-4.4). Refutation upgrades honesty exactly as proof does. |
| C5 | 2026-08-25 | Integrations: what if `aspark-graph serve` (never exercised) is broken? | Then #8's honest outcome is a consumer-repo finding, not a Core workaround (§6); the attempt and failure trace are still evidence. Risk R1. |
| C6 | 2026-08-25 | UX flows/states: N/A — no UI. Counting domains for transcript greps defined at AC-5.3 instead (B7 lesson: subject-matter repos make naive grep unusable). |
| C7 | 2026-08-25 | Venues: why scratch copies instead of the real repos? | Round-2 precedent: no writes into live projects (R6), full control of availability states, disposability. `~/aSPARK-graph` is probed read-only, never written. |
| C8 | 2026-08-25 | Out-of-scope sanity: is anything tempting adjacent? | Yes — fixing B9/B10/B11, closing issues, full product QA runs, AC-1.2/AC-5.2 coverage: all cut above. |
| C9 | 2026-08-25 | Q1 — venue for #10? | **Ruled:** throwaway locally served static page; detection + one real navigation/assertion suffices (AC-4.1/AC-4.2). Page and server live in disposable scratch outside the repo. |
| C10 | 2026-08-25 | Q2 — `aspark-graph` MCP registration authorized? | **Ruled:** yes, project-scoped to the positive venue only; a `serve` failure becomes a consumer-repo finding (accepted). Grant not extended beyond this server — browser backends split to Q6, later granted separately (C15). |
| C11 | 2026-08-25 | Q3 — include AC-3.2 as US-6? | **Ruled:** included, priority Should. |
| C12 | 2026-08-25 | Q4 — confirm the exclusions? | **Ruled:** confirmed — AC-1.2 and AC-5.2 stay cut; reasons stand in §6. |
| C13 | 2026-08-25 | Q5 — README permission? | **Ruled:** granted for `README.md` §Project Status only, so the proof statement follows the evidence in the same change; remains the only non-`.spark/` edit. NFR-1/NFR-9 made unconditional. |
| C14 | 2026-08-25 | Clarify pass on the draft: what did it surface? | Fixed in place: attempt semantics in AC-4.4 (confirmed vs refuted vs unstable across attempts); AC-3.3 named as the sole exception to ID-order execution; demo-page venue pinned to scratch outside the repo; AC-2.1 cites actual registered tool names. One gap needed the user → Q6. |
| C15 | 2026-08-25 | Q6 — may the sweep register the browser backends itself? | **Ruled:** yes — the sweep registers Playwright MCP and Chrome DevTools MCP itself, under exactly the terms of #8's grant (C10): registration authorized, project-scoped to the positive venue only, every mutation logged with authorization and restoration per AC-1.2's pattern. Mechanism now stated plainly in AC-4.1/AC-4.3; NFR-6 names all three registrations. |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **N/A — no UI surface.** Deliverable is evidence Markdown under `.spark/` plus one
  README paragraph; no screens, flows or states exist to review (PO, 2026-08-25).

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria — counts and outputs, not feelings
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — 5 Must, 1 Should; execution order = ID order, negative case first (exception: AC-3.3 after US-4)
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason) — NFR-1…9, `library` lens mapped
- [x] Clarify pass done: no ambiguity left unresolved or unparked — **Q6 resolved (C15); user-approved at the gate, 2026-08-25**
- [x] Open questions are resolved or explicitly accepted as risk — **zero open (Q6 → C15); user-approved at the gate, 2026-08-25**
- [x] Out-of-scope section is filled (something was consciously cut) — ten documented cuts, two user-confirmed (C12)
- [x] Constitution (`.spark/constitution.md`) respected — §1 negative-first (US-1), §3 verify-only fence + consumer-defect boundary, §4 evidence bar (NFR-4), §6 nothing-unasked (NFR-6); no conflict found
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A: no UI surface (see §8)
- [x] Line budget respected: Ist ~250 / Soll ~250 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [x] Status set to `approved` by the user *(explicitly, 2026-08-25)*
