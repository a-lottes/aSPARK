# Spec: graph-mcp-verification

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-09-21 |
| **Ticket** | none |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this spec updates it in the same edit that resolves a clarification or
     changes status: overwrite in place, never append. The block holds one current
     state, never a per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** `approved` — the user approved the gate 2026-09-21, explicitly accepting
  the ~16-line budget overage as-is rather than asking for a trim. Q1–Q5 (§3) are
  resolved per the user's explicit answers the same day, folded into §3, §4, §5, §6,
  §7 below.
- **Summary:** Re-verify three still-open documented claims about the optional
  `aspark-graph`/MCP integration — issues #11 (installed-but-unbuilt hint fires
  exactly once), #10 (Playwright MCP + Chrome DevTools MCP as `/demo-day` browser
  backends), #8 (MCP-first precedence) — against live behavior, under the same
  verify-only, refuted-with-finding-capable fence `graph-gates-verification` used.
- **Open:** `0 open` — Q1–Q5 resolved in §3 (see C9–C13, §7). The gate's remaining
  red boxes are only the user's final `approved` status and the line-budget overage
  noted below.
- **Binding ruling:** §4 User Stories for the current stories; §3 for what blocks the
  gate; §3/§7 record every resolution reached so far.
- **On conflict:** the numbered body below wins for everything except `Status`; log
  the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem.** Three GitHub issues document optional-integration behavior that has
  never been checked against a live run: #11 and #8 cite AC-2.3 and AC-2.2 of the
  original `graph-gates` release spec directly by ID; #10 cites the gear-check prose
  naming Playwright MCP and Chrome DevTools MCP as `/demo-day` browser backends.
  `graph-gates-verification` (2026-08-25) covered similarly-numbered claims for its
  own #8/#10/#11, yet these three issues remain open today — so either that evidence
  never closed them or state has drifted since. Per this repo's own working habit
  ("a disclosed limitation stays honest only if re-verified at every gate"), the
  honest move is fresh evidence, not citing the prior sweep's word.
- **Who hurts.** The solo maintainer-operator, who needs each issue closeable with
  linked evidence instead of open indefinitely; the dual-tool operator relying on
  MCP-first precedence and the hint firing correctly; a future `/demo-day` user on a
  web-app project who trusts the two named browser backends actually work.
- **Goal.** Each of #8, #10, #11 becomes closeable with a performed-step evidence
  row — or, where the claim doesn't hold live, a precisely routed finding (never a
  silent fix, never a silent pass).
- **Success signal.** A written evidence record where: the absent-tool case is
  reconfirmed silent first; the hint-count claim carries a literal counted number and
  its counting method; the MCP-vs-CLI precedence claim is observed taking one branch
  twice and the other branch once, not asserted from prose; and the two browser
  backends each carry an explicit verdict (`confirmed`, `refuted-with-finding`, or
  `not-verified-live` with the missing venue named) — never a claimed pass without a
  captured command or ceremony invocation behind it.
- **Why now.** These are the only three open issues in this cluster; honesty about
  maturity (constitution §1) degrades every day they sit undecided while `README.md`
  and `tools/README.md` continue to assert the underlying behavior as fact.

## 2. Target Users

- **The maintainer (primary).** Wants #8/#10/#11 either closed with evidence or
  reopened with a routed, precisely located fix.
- **The dual-tool operator.** Relies on MCP-first precedence and the unbuilt-graph
  hint behaving exactly as documented.
- **The future `/demo-day` user on a web-app project.** Reads the gear-check line
  naming two MCP browser backends and plans tooling around it.

Not a user: end users of products built with aSPARK — this feature ships no runtime
surface and changes no behavior.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | Idea arrived solution-shaped ("verify-only sweep on three issues"). Underlying need: the three claims must become performed evidence or a precisely routed finding, so the issues can close on a real basis. | Accepted framing |
| A2 | QA method is already declared (constitution §8): no browser-observable surface in this repo; substitute method is hands-on QA against the installed plugin; a performed step is a real ceremony invocation or an observed command's output. Reading a file and reasoning about it is never a performed step and never satisfies an AC. Not renegotiated here. | Standing, cited not restated |
| A3 | The environment baseline (runner on `PATH`, this repo's own `runner=yes, graph=no` resolution, `aspark-graph` PyPI availability) must be re-probed fresh at sweep start, not inherited from `graph-gates-verification`'s now month-old probe — this repo's own `CLAUDE.md` habit. | Standing — Risk R1 |
| A4 | Despite `graph-gates-verification` covering similarly-ID'd claims for its own #8/#10/#11, today's live GitHub issues #8/#10/#11 remain open — treated here as needing fresh evidence, not a reuse of that sweep's aging record. | Accepted — see §1 |
| **Q1** | **#11's fixture.** Verifying "fires exactly once" needs a disposable scratch project with `aspark-graph` installed (PyPI, constitution §3) but its build/index step deliberately not run. Does the user authorize this sweep to create that scratch venue and install `aspark-graph` into it (never build/index it), per constitution §6's nothing-unasked rule? | **Resolved — 2026-09-21.** User authorized (explicit answer, not a guess): create the disposable scratch project outside this repo, `aspark-graph` installed via PyPI, its build/index step (`aspark-graph build`) deliberately not run, used only to observe the hint firing. See C9. |
| **Q2** | **MCP/browser-backend registration for #8 and #10.** Verifying MCP-first precedence and the two browser backends needs the `aspark-graph` MCP server, Playwright MCP and/or Chrome DevTools MCP registered in a session. Does the user grant this sweep the same authorization `graph-gates-verification` had (project-scoped, logged, restored) — or will these be pre-registered — or is live registration out of reach this cycle, in which case the affected ACs fall back to `not-verified-live (venue named)` rather than a claimed pass? | **Resolved — 2026-09-21.** User authorized this sweep to register the needed MCP servers itself — `aspark-graph` MCP for #8, and Playwright MCP / Chrome DevTools MCP for #10 — project-scoped, logged, and torn down afterward, same terms `graph-gates-verification` used. See C10. |
| **Q3** | **#10's venue, given constitution §8.** §8 (added *after* `graph-gates-verification` ran) declares this repo has no browser-observable surface. That sweep worked around an identical gap by standing up a disposable, locally served static page entirely outside the repo and performing a real navigate + assert. Is that same workaround still sanctioned now that §8 formally exists — or should this sweep confine itself to tracing the resolution logic in the skill/tool-file prose and mark the live-interaction leg `not-verified-live`? | **Resolved — 2026-09-21.** User authorized the same scratch-page workaround `graph-gates-verification` used: a disposable, outside-repo static page proves live browser-backend recognition, rather than confining this sweep to resolution-logic tracing alone. See C11. |
| **Q4** | **README permission.** Does this sweep get the same narrow grant `graph-gates-verification` had (Q5/C13 there) to edit `README.md` §Project Status so the proof/refutation state lands in the same change — or does every edit stay confined to `.spark/graph-mcp-verification/**`? | **Resolved (default) — 2026-09-21.** Not asked directly; default applied since this is a verify-only sweep announcing no new capability. All edits stay confined to `.spark/graph-mcp-verification/**`; `README.md` is untouched. See C12. |
| **Q5** | **#11's "exactly once" unit.** Once per triggering ceremony *run*, or once per *session/trail* spanning several ceremonies? AC-2.1 below is drafted as "once per triggering run" — confirm or correct. | **Resolved — 2026-09-21.** Per run, as drafted. AC-2.1 unchanged. See C13. |

## 4. User Stories

### US-1 (Must): The sweep's environment preparation leaves the absent case silent

> As a user on a project without `aspark-graph` or the two browser MCP servers, I
> want the negative case re-proven first and every mutation restored, so that
> collecting evidence for someone else's optional tool never regresses the normal
> loop.

**Acceptance criteria:**

- [ ] AC-1.1: Given a fresh probe in a neutral shell at sweep start, when a wired
  ceremony's first step runs in this repo (resolving `graph=no`, no browser MCP
  registered), then the transcript contains zero ceremony-emitted mentions of
  `aspark-graph`/browser-backend hints, and no gate outcome differs from today's.
- [ ] AC-1.2: Given every environment mutation this sweep performs (installs,
  registrations, scratch builds — authorized per Q1/Q2, §3), when the evidence is
  written, then each entry names its authorization and its restoration, and a
  post-sweep neutral-shell probe resolves identically to the pre-sweep baseline.
- [ ] AC-1.3: Given the finished evidence record, when its runs are read in order,
  then the silence case (AC-1.1) precedes every positive-case run for #8/#10/#11.

### US-2 (Must): The installed-but-unbuilt hint fires exactly once (#11)

> As an operator with the runner installed but no graph built, I want one hint
> sentence and a normal completion, so that I get the pointer without nagging and
> without an unrequested build.

**Acceptance criteria:**

- [ ] AC-2.1: Given the Q1-authorized disposable scratch project outside this repo —
  `aspark-graph` installed via PyPI per constitution §3, its build/index step
  (`aspark-graph build`) deliberately not run, yielding `runner=yes, graph=no`
  verified by a direct probe immediately beforehand — and a wired ceremony run start
  to finish, when its complete emitted output — ceremony messages, produced
  artifact, subagent reports — is counted, then it contains exactly **1** occurrence
  of the one-sentence hint naming `aspark-graph build` (once per run, per Q5).
- [ ] AC-2.2: Given the same run, when it completes, then no `build`/`install`/
  `serve` was executed by any participant beyond the Q1-authorized install, and no
  `graph.json` came into existence.
- [ ] AC-2.3: Given that loaded skill/tool files legitimately contain the tool's own
  name, when the count in AC-2.1 is taken, then the method counts ceremony-emitted
  output and artifacts only — never file contents loaded into context — and the
  counting method is stated in the evidence so the number is reproducible.

### US-3 (Must): MCP-first precedence is observed, not just documented (#8)

> As a dual-tool operator, I want the documented precedence seen deciding a real
> resolution in a session where both an MCP path and a CLI/file-read path could
> answer, so that determinism is an observation rather than a paragraph.

**Acceptance criteria:**

- [ ] AC-3.1: Given a session with the `aspark-graph` MCP server registered — this
  sweep's own Q2-authorized, project-scoped registration, logged and torn down
  afterward — and a scratch repo with a built, passing graph where both the MCP tool
  and a direct CLI/file-read could answer the same query, when a wired ceremony
  resolves how to answer, then it takes the MCP branch — names the MCP tool(s) as
  the surface and runs zero CLI/file-read probes for that query (counted, == 0).
- [ ] AC-3.2: Given the same environment, when the same query is resolved a second
  time, then it resolves identically — one data point is not a precedence claim.
- [ ] AC-3.3: Given a no-MCP session on the same scratch repo and query, when
  resolution runs, then it takes the CLI/file-read branch — the two branches
  together demonstrate an order, not an assumed one.
- [ ] AC-3.4: Given the registration attempt fails or the tools never appear despite
  Q2's authorization, when the evidence is written, then the exact failure (command,
  output, traced cause) is recorded as a finding — #8 is never silently skipped for
  lack of a working server.

### US-4 (Must): Each named browser backend is confirmed, refuted or honestly unproven (#10)

> As a `/demo-day` user on a web-app project, I want Playwright MCP and Chrome
> DevTools MCP each proven able to drive a real page, using the same scratch-page
> workaround `graph-gates-verification` used for an identical gap.

**Acceptance criteria:**

- [ ] AC-4.1: Given the resolution logic that determines which backend names
  `/demo-day`'s gear check accepts, when it is read and traced, then the evidence
  cites the exact `file:line` naming Playwright MCP and Chrome DevTools MCP as
  recognized backends — a documentation-level confirmation, explicitly labelled as
  such and never conflated with a live pass.
- [ ] AC-4.2: Given the Q2/Q3-authorized scratch-page workaround — a disposable
  static page served outside this repo, with Playwright MCP (then, separately,
  Chrome DevTools MCP) registered project-scoped per Q2 — when the session drives
  that page, then the log records ≥ 1 navigation and ≥ 1 content assertion
  attributable to the backend's own action identifiers, and the verdict is
  `confirmed (performed)`.
- [ ] AC-4.3: Given the authorized live attempt (AC-4.2) fails for a backend —
  registration fails or no attributable interaction can be produced — when the
  evidence is written for that backend, then the verdict is `not-verified-live
  (reason and venue named)` with the exact failure recorded as a finding — never
  rounded up to `confirmed`.
- [ ] AC-4.4: Given either path, when a backend's verdict is written, then it is
  recorded independently for Playwright MCP and for Chrome DevTools MCP — a
  passing/failing/unproven verdict for one is never extended to the other.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Public surface *(library §1)* | Zero new slash commands, agents, skills or exported names; `git diff --name-only` over the whole feature touches only `.spark/graph-mcp-verification/**` — `README.md` stays untouched per Q4's resolved default (§3, C12). | `/peer-review` + `git diff` |
| NFR-2 | Compatibility *(library §2)* | Verify-only: `skills/`, `agents/`, `tools/`, `lenses/`, `templates/`, `.claude-plugin/plugin.json` byte-identical; no version bump, no protected structure touched (constitution §3). A surfaced defect routes to a finding, never widens this diff. | `/peer-review`: empty diffs over those paths |
| NFR-3 | Contract clarity *(library §4)* | Wherever evidence contradicts documented behavior (tool-file prose, gear-check text, README claims), the finding quotes the contradicting text verbatim with `file:line`. | Findings in the evidence record |
| NFR-4 | Evidence bar *(constitution §1, §4, §8)* | Every AC's evidence is a performed step per A2 (real command/ceremony, captured output); a reading-only observation is labelled `not-verified-live` and never counted as a pass. Negative case first (US-1). | QA-gate read of the evidence record |
| NFR-5 | Countability | Every "zero"/"exactly once" claim (US-2, US-3) states a counted number with its counting method named. | Evidence record, reproducible by re-count |
| NFR-6 | Safety — nothing unasked *(constitution §6)* | No `build`/`install`/`serve`/MCP registration performed beyond the specific grants recorded at Q1/Q2 (§3, C9–C10); writes confined to declared disposable scratch venues; every mutation logged with authorization and restoration (AC-1.2). | Evidence audit + before/after probes |
| NFR-7 | Degrade-to-silence stays intact *(constitution §6)* | This sweep's own probing produces zero change to how any gate behaves for a project without `aspark-graph`/the two browser MCPs — no gate anywhere starts blocking on, or warning about, an optional tool's availability as a side effect of this sweep. | AC-1.1 + `/peer-review` |
| NFR-8 | Reliability / scale | N/A — no runtime; the cost is spend and agent attention, bounded by preferring single-step observations over full ceremony runs wherever an AC allows. | N/A (recorded) |
| NFR-9 | Accessibility | N/A — no UI. | N/A |
| NFR-10 | Observability / honesty *(constitution §1)* | N/A this cycle for README specifically — Q4 resolved to no README edit (§3, C12). The evidence record itself states the post-sweep state literally: proven stays proven, refuted becomes `refuted-with-finding`, anything not run stays `not-verified-live` — never rounded up. | `/peer-review` of the evidence record |

*Lens coverage: `library` is the only active lens — §1→NFR-1, §2→NFR-2, §4→NFR-3; its
§3 (packaging) is the constitution's declared N/A, unchanged by a verify-only sweep.*

## 6. Out of Scope

- **Any fix for anything the sweep surfaces.** Defects route to findings for a later
  `/increment`; no repair is pre-authorized here.
- **Every edit to `skills/`, `agents/`, `tools/`, `lenses/`, `templates/`,
  `plugin.json`** — a real Core-side fix needs its own change; `templates/` is
  additionally protected by the constitution §3 cross-repo contract.
- **Editing `README.md`.** Q4 resolved to the default (§3, C12): a verify-only sweep
  announces no new capability, so every edit stays confined to
  `.spark/graph-mcp-verification/**`.
- **Consumer-repo (`aspark-graph`) defects** uncovered by #8/#10/#11's attempts —
  neither Core's to fix; filed where they live (constitution §3).
- **Closing or editing GitHub issues #8/#10/#11** — the user's act at `/go-live`;
  this feature produces the evidence that makes closing defensible.
- **A full `/demo-day` QA ceremony against a real product.** #10 asks whether the
  two backends work, not for a product QA; the minimal detection-plus-interaction
  proof is the slice.
- **A permanent fixture project inside this repo.** Every scratch venue for
  Q1/Q2/Q3 is disposable and lives outside `~/aSPARK`.
- **Automated tests** — impossible for prompt material (constitution §4).
- **Any configuration, opt-in or opt-out toggle** — verification changes no
  behavior, so there is nothing to add a switch for.
- **Re-litigating `graph-gates-verification`'s own already-closed claims** — this
  sweep targets only the three issues still open today.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-21 | Functional scope: do the three issues cover everything in this cluster still open? | Yes, per the user's brief — #8, #10, #11 only; no fourth claim named. |
| C2 | 2026-09-21 | Data & evidence: what counts as "the deliverable"? | A written evidence record under `.spark/graph-mcp-verification/`; every row a performed step with a counted number where the AC calls for one (NFR-4/5). No artifact of the verified feature is modified. |
| C3 | 2026-09-21 | Roles & permissions: who installs/registers the tools this sweep needs? | Not the agents unasked — moved to §3 as Q1/Q2, blocking. |
| C4 | 2026-09-21 | Error & edge-case behavior: what if a claim doesn't hold live? | It's a valid outcome: `refuted-with-finding`, routed, never fixed inline (AC-3.4, this repo's own `CLAUDE.md` habit). |
| C5 | 2026-09-21 | Integrations: what if this repo's declared no-browser-surface (§8) makes #10 genuinely unprovable this cycle? | Not resolved here — moved to §3 as Q3; US-4 drafted so it survives either ruling. |
| C6 | 2026-09-21 | UX flows/states: N/A — no UI; counting-method discipline carried from `graph-gates-verification`'s own lesson into AC-2.3. |
| C7 | 2026-09-21 | Out-of-scope sanity: anything tempting adjacent? | Yes — fixing anything surfaced, closing the issues, a full product QA run, a permanent fixture: all cut in §6. |
| C8 | 2026-09-21 | #11's "exactly once" — per run or per session? | Not resolved here — moved to §3 as Q5; AC-2.1 drafted with the "per run" reading pending confirmation. |
| C9 | 2026-09-21 | Q1 resolved by the user (explicit answer): authorize the #11 scratch fixture? | Yes — create a disposable scratch project outside this repo, `aspark-graph` installed (PyPI), its build/index step deliberately not run, used only to observe the hint firing. Folded into §3 Q1, AC-2.1, AC-1.2, NFR-6. |
| C10 | 2026-09-21 | Q2 resolved by the user (explicit answer): who registers the MCP servers for #8/#10? | The sweep registers them itself — `aspark-graph` MCP, Playwright MCP, Chrome DevTools MCP — project-scoped, logged, torn down afterward, same terms `graph-gates-verification` used. Folded into §3 Q2, AC-3.1, AC-4.2, NFR-6. |
| C11 | 2026-09-21 | Q3 resolved by the user (explicit answer): is the scratch-page workaround still sanctioned given constitution §8? | Yes — same precedent as `graph-gates-verification`: a disposable outside-repo scratch page proves live browser-backend recognition. AC-4.2 rewritten as the primary path (no longer an "if authorized" branch); AC-4.3 narrowed to genuine technical failure of the authorized attempt. |
| C12 | 2026-09-21 | Q4 not asked directly — README §Project Status edit scope? | Default applied: this is a verify-only sweep with no new capability to announce, so all edits stay confined to `.spark/graph-mcp-verification/**`; `README.md` untouched. Folded into §3 Q4, §6 Out of Scope, NFR-1, NFR-10. |
| C13 | 2026-09-21 | Q5 resolved by the user (explicit answer): per-run or per-session unit for #11's "exactly once"? | Per run, as drafted — AC-2.1 unchanged. Folded into §3 Q5. |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **N/A — no UI surface.** Deliverable is evidence Markdown under `.spark/`; no
  README edit (Q4 resolved to the default, §3/§6) and no screens, flows or states
  exist to review (PO, 2026-09-21).

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — 4 Must, 0 Should/Could/Won't
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — Q1–Q5 resolved by
  the user's explicit answers on 2026-09-21, folded into §3/§4/§5/§6 (see C9–C13, §7)
- [x] Open questions are resolved or explicitly accepted as risk — Q1–Q5 resolved
  (§3); R1 (A3) remains a standing, accepted risk, not a blocking question
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions — §6 nothing-unasked and §8 QA method were the live tensions; both resolved via the user's Q1–Q3 answers (C9–C11)
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A, §8
- [x] Line budget respected: Ist ~266 / Soll ~250 (excluding HTML comments) — **over
  budget by ~16 lines**, entirely the direct result of folding Q1–Q5's five
  resolutions into §3/§4/§5/§6/§7; the user explicitly accepted this overage as-is
  at the gate (2026-09-21) rather than asking for a trim
- [x] Status set to `approved` by the user — **approved 2026-09-21**
