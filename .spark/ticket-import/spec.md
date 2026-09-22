# Spec: ticket-import

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-09-21 |
| **Ticket** | [`#19`](https://github.com/a-lottes/aSPARK/issues/19) |

**Handoff**
- **Status:** `approved` — the user approved the gate 2026-09-21. A2 and A3 (§3) resolved the same day.
- **Summary:** Let `/story-time` take a GitHub issue number as its input and seed the spec from it; let `/go-live` post exactly one status comment back to that issue when its own gate closes, and never in the other direction.
- **Open:** `0 open` — A2 (write-back needs a new constitution field, split from the read half which needs none) and A3 (the write-back positive case is proved in a disposable scratch repo, discarded after) were both ruled by the user on 2026-09-21; see §3.
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what was decided and why.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem.** Two separate frictions, one issue (#19):
  1. **Retyping context that already exists.** A maintainer who tracks work in
     GitHub Issues has already written a title and a description before ever
     touching `/story-time`; today they paste or re-key it, and the PO's
     interrogation runs against a hand-typed summary that can silently drift
     from the ticket.
  2. **The tracker keeps lying after the loop finishes.** `/go-live` (since
     `tracker-handoff`) writes a truthful terminal status into `.spark/`, but
     nothing carries that truth back to wherever the organization's ticket
     actually lives — the issue itself still reads "open," unstated, forever,
     even after `released` or `handed-off`.
- **Goal.** A maintainer can start `/story-time` from a real GitHub issue
  number instead of retyping it, and once, at `/go-live`'s own gate close,
  the loop pushes a single, honest status back — never more than once, never
  the other direction.
- **Success signal.**
  1. **Import, observed live.** A real `/story-time <issue-number>` run on a
     project with GitHub issues shows the PO working from the fetched
     title/body, not from hand-typed text, and the spec's `Ticket` row cites
     the real issue.
  2. **Write-back, observed live.** A real `/go-live` run on that same
     project ends with exactly one `gh issue comment` call, containing the
     terminal status, and zero further tracker calls after it.
  3. **Unchanged, observed on this repo.** A `/story-time` run with no
     argument and a `/go-live` run on a project without the new declaration
     produce output identical to today's, with zero occurrences of "ticket
     import" or "write-back" anywhere in either transcript or report.
- **Why now.** Named "unblocked" in `ROADMAP.md`'s Next list, specifically
  because `tracker-handoff` already shipped the `Ticket` row this feature
  builds on — the precondition the roadmap named is met.

## 2. Target Users

- **The GitHub-issues maintainer** running `/story-time` against their own
  backlog — the primary beneficiary of both halves. US-1, US-2.
- **A future reader of the tracker** (a teammate, or the same maintainer
  later) who currently has no way to tell, from the issue alone, that aSPARK
  finished the work. US-2.
- **Every existing aSPARK user with no tracker** (including this repo's own
  maintainer, per constitution §7's `Ticket-reference format: none`) — gains
  nothing, and requires exactly one thing: nothing changes. US-3, the
  dominant risk, exactly as in `tracker-handoff`'s own US-1.

Explicitly **not** a user: the tracker itself, as a thing to be kept in sync.
It is written to once and never read back from after that write (§6).

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived partly as a solution ("take a ticket number as sole input," "push status back... one direction only"). Underlying need, restated: *a maintainer using GitHub Issues shouldn't have to re-key a ticket's content, and the tracker shouldn't keep saying "open" once the loop has honestly closed.* Original phrasing recorded per the no-solutions rule. | Accepted; drives US-1/US-2 |
| **A2** | **Resolved — 2026-09-21.** Does *read* (import) and *write* (status push) each need a constitution declaration, or can either work from the CLI argument alone? | **Ruled: split, as recommended.** **Read needs no declaration.** Passing an issue number to `/story-time` is itself an explicit, per-run ask — the same standard `tools/README.md`'s placement test applies to installation state applies here to *intent*: a one-off explicit argument is not a stable project fact, so there is nothing for `/charter` to usefully declare, and requiring a declaration first would add friction to the smaller, lower-risk half. **Write needs one new constitution field**, because it is an outward-facing side effect on a third party's system, exactly the class §7 already gates (release mode, approver) — not an ambient, machine-varying fact like "is `gh` installed" (§7's own placement test: "could the constitution know this?" — yes, "does this project want status pushed to its tracker, and how" is a stable, once-decided policy, the same shape as `Ticket-reference format`). Field, for `/charter` to write: **`Tracker write-back:`** `github-issues-comment` \| `none`, default `none`, extending §7 (not a new section) since it fires at the same handoff point as the existing fields there. The write half's touched-file list (§5) is now definite: `templates/constitution.md`, `skills/go-live/SKILL.md`, `agents/release-manager.md`. |
| **A3** | **Resolved — 2026-09-21.** This repo's own constitution declares `Ticket-reference format: none` (§7) specifically because a real ticket ID would be exposed under `.spark/`'s public tracking (constitution §5) — the identical structural problem `tracker-handoff` hit (its C8). Changing that declaration to prove this feature is out of this spec's authority (`/charter`'s, not `/story-time`'s). | **Ruled: yes, create the scratch repo.** The user explicitly authorized a disposable scratch GitHub repository — its own issue, its own constitution declaring `Tracker write-back: github-issues-comment` — to prove the write-back positive case live, then discard it, the same pattern `tracker-handoff` (A4/C8, this repo's own earlier release) used. **The read half's positive case still does not need the scratch repo** — it is proven directly against this repo's own real, already-public issue #19 (no constitution change needed, per A2), read-only, writing the resulting spec draft to an *untracked* scratch path rather than committing it under `.spark/ticket-import/`, so no new private-content-in-public-tree problem is created by the proof itself. Creating the scratch repo is an `/increment`- or `/demo-day`-time action, authorized here but not performed by this fold-in. |
| A4 | Which tracker(s) are in scope for v1? | **GitHub issues only**, via `gh issue view` (read) / `gh issue comment` (write). This repo already depends on `gh` throughout `/go-live` and `agents/release-manager.md`, making it the tightest, most already-proven slice. Jira, Linear, GitLab Issues, Azure DevOps: named, not built — §6 |
| A5 | Is `gh`'s installation/auth state a `tools/` concern (ambient probe, ceremony's own initiative, ships a `tools/gh.md`) or handled inline? | **Handled inline, no `tools/gh.md`.** The `tools/` apparatus (silent probe, four-state hint table) exists for *ambient* enrichment a ceremony offers on its own initiative in every run. Here `gh` is an *explicit* dependency of an *explicitly requested* action (an argument was passed, or write-back was declared) — its absence is reported plainly (AC-1.3, AC-2.3), not silenced, because the user already asked for the thing that needs it. Silencing an explicit failure would itself be the "check that fires where it doesn't apply" failure mode, inverted. |
| A6 | Which repo does a bare issue number refer to? | **The repo `git remote get-url origin` / `gh repo view` resolves to, only.** Cross-repo references (`owner/repo#42`, full issue URLs pointing elsewhere) are out of scope for v1 (§6) — narrower, and it removes an entire class of "wrote to the wrong repo's tracker" risk. |
| A7 | Does fetching or posting need a new agent tool grant? | **No.** `agents/product-owner.md` keeps `Read, Grep, Glob, Write` — the `gh issue view` call runs at the `/story-time` skill/dispatcher level (which already runs shell commands as part of normal orchestration), and the fetched title/body is passed to the PO as part of the idea input, the same shape `tools/` already uses (skill resolves, agent reads the result). `agents/release-manager.md` already declares `Bash` — `gh issue comment` needs no new grant there either. |

## 4. User Stories

### US-1 (Must): Start from a real ticket instead of retyping it

> As a maintainer who tracks work in GitHub Issues, I want to start
> `/story-time` from a real issue number, so that I don't re-key context
> that already exists and risk it drifting from the ticket.

**Acceptance criteria:**

- [ ] AC-1.1: Given a GitHub issue number passed as `/story-time`'s argument, when the ceremony starts, then it runs a real `gh issue view <n>` against the repo resolved from `origin`, and hands the fetched title and body to the Product Owner as the idea input — verified by comparing the drafted spec's Problem & Goal against the actual fetched text in the same session.
- [ ] AC-1.2: Given the fetched issue, when the spec is written, then its `Ticket` row cites the issue reference (e.g. `#42`) and §1 states once, plainly, that it was seeded from that ticket, with the issue URL cited — never pasted as unattributed prose.
- [ ] AC-1.3: Given the issue number doesn't exist, the repo is private without access, or `gh` is missing/unauthenticated, when `/story-time` attempts the fetch, then it STOPS, reports the real error in plain language, and asks whether to proceed with a manually supplied idea instead — it never silently proceeds with an empty or invented brief.
- [ ] AC-1.4: Given the fetched title/body, when the Product Owner interrogates it, then the full forcing-question interrogation still runs (who hurts, smallest slice, success signal, etc.) — the ticket text is a seed for the brief, never a substitute for the interrogation or the Clarify pass.
- [ ] AC-1.5: Given the target project's `.spark/` is tracked in git, when a ticket is imported, then `/story-time` states once, before writing, that the imported title/description is about to become part of a (possibly public) committed artifact — so the maintainer can decide whether that ticket's content belongs there.

### US-2 (Should): The tracker stops lying once the loop closes

> As a maintainer, I want the loop to push one honest status back to the
> ticket when `/go-live`'s gate closes, so that the tracker reflects what
> actually happened instead of sitting silently "open" forever.

**Acceptance criteria:**

- [ ] AC-2.1: Given the constitution declares `Tracker write-back: github-issues-comment` and the feature's `Ticket` row holds a bare issue reference resolvable in this repo, when `/go-live` reaches a terminal status (`released`, `handed-off`, or `aborted` — never `preparing`), then it performs **exactly one** `gh issue comment <n>` call, stating the terminal status, the version/PR reference, and a link to the release artifact.
- [ ] AC-2.2: Given that comment attempt, when the release report is read, then its Release Actions record states whether it was posted or skipped, and why — never silently either way.
- [ ] AC-2.3: Given `gh` is unavailable, unauthenticated, or the API call fails, when `/go-live` reaches its terminal status, then the release still completes and closes normally (the KEEP GATE is never blocked by this), and the report names the skip in one line.
- [ ] AC-2.4: Given the declaration is `none` or absent, when `/go-live` runs, then it makes zero tracker calls and the report never mentions write-back — identical to AC-3.1, not a lighter special case of it.
- [ ] AC-2.5: Given a feature whose `Ticket` row is `none`, when `/go-live` runs even with write-back declared, then no comment is attempted — there is nothing to write back to.
- [ ] AC-2.6: Given the user has not yet given the outward-facing "go" (`skills/go-live/SKILL.md` step 4), when the Release Manager presents the release plan (step 3), then the pending ticket comment is named alongside the other outward-facing actions awaiting that same authorization — never posted before it.
- [ ] AC-2.7: Given a comment has been posted for a feature, when any later ceremony runs on that same feature, then nothing re-posts, edits, or re-checks it — the write happens once, ever, per feature.

### US-3 (Must): Nothing changes for a project that hasn't asked for this

> As any aSPARK user without a declared tracker, or invoking `/story-time`
> without a ticket number, I want the loop to behave exactly as it does
> today, so that someone else's tracker integration never becomes a change
> to my loop.

**Acceptance criteria:**

- [ ] AC-3.1: Given a project with no `Tracker write-back` declaration, or no constitution at all, when `/go-live` runs to completion, then it performs the same steps, sections and gate boxes as before this feature existed, and the report contains zero occurrences of "tracker," "write-back," or a `gh issue` call — checkable by diffing a before/after run on this exact repo.
- [ ] AC-3.2: Given `/story-time` is invoked with no argument, when it runs, then it asks for the idea exactly as today — no prompt about a ticket number, no mention that import is possible.
- [ ] AC-3.3: Given this feature's own evidence record, when it is read, then AC-3.1 and AC-3.2 are recorded as having run **first**, on this repo, before any positive-case run — constitution §1.

## 5. Non-Functional Requirements

**Touched-file list (read half, no declaration needed):** `skills/story-time/SKILL.md`
(accept + validate an optional issue-number argument, run the fetch, pass the
result on), `README.md`/`ROADMAP.md` (docs-in-step). **Touched-file list (write
half, A2 ruled in as scoped):** additionally `templates/constitution.md`
(§7's new field), `skills/go-live/SKILL.md` (probe the declaration), `agents/
release-manager.md` (perform the comment, name it in the release plan). No
file in `templates/spec.md`'s protected structures (constitution §3) changes —
the `Ticket` row already accepts `#123`-shaped values.

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Compatibility & versioning *(library lens §2)* | Purely additive. No protected heading, row, column or ID pattern in constitution §3's table is touched; `templates/spec.md`'s existing `Ticket` row is reused unchanged (AC-1.2); the one new field lives in `templates/constitution.md`, which §3's protected table does not list and `aspark-graph` never parses (same reasoning `tracker-handoff` verified for its own `Delivery & Handoff` fields). Minor bump, no coordinated release. | `/peer-review` + `git diff templates/` |
| NFR-2 | Public surface *(library lens §1)* | Zero new slash commands, agents, lenses or template files. The added surface: one optional CLI argument on an existing command, one optional constitution field, and one existing agent's existing `Bash` grant put to a new use — no new tool grant on `product-owner` or `release-manager` (A7). | `/peer-review` of the diff |
| NFR-3 | Contract clarity *(library lens §4)* | Every touched file states its default when the argument/declaration is absent, right where a reader meets the new behavior — mirroring `tracker-handoff`'s NFR-4 and `right-sizing`'s NFR-3 pattern. | `/peer-review` |
| NFR-4 | Degrade to silence *(constitution §6)* | With no argument and no declaration, the strings "ticket," "tracker" and "write-back" appear zero times in either ceremony's output or report, and no gate outcome differs from the pre-change run. | Dogfood, negative case first, on this repo (AC-3.1–3.3) |
| NFR-5 | No gate blocks on an external tool *(constitution §6)* | Neither the SPEC GATE nor the KEEP GATE is ever conditioned on `gh`'s presence, auth state or API success — a failed fetch or post is reported (AC-1.3, AC-2.3), never a silent or blocking failure. | `/peer-review` + dogfood |
| NFR-6 | Outward-facing authorization *(constitution §6, release-manager Hard Rules)* | The ticket comment is never posted before the same explicit "go" that authorizes publishing, and is named in the pre-go release plan (AC-2.6) — no separate new authorization ceremony added, to keep this lean rather than adding a second confirmation step for one Bash call already covered by an existing one. | `/peer-review` + dogfood |
| NFR-7 | Privacy *(constitution §5, spirit — `security` lens off)* | Imported ticket content lands in a possibly-public `.spark/` artifact; AC-1.5 is the one live mitigation — a stated warning, not a block. No new secret, token or credential is ever written to a committed file; `gh`'s own auth token is never read or echoed by any ceremony step. | `/peer-review` |
| NFR-8 | Traceability *(constitution §4)* | The ticket reference introduces no new ID namespace and is cited by no downstream artifact as an anchor — same rule as `tracker-handoff` AC-4.4. | `/peer-review` |
| NFR-9 | Docs in step *(constitution §4)* | `ROADMAP.md` moves this item from Next to Shipped only once both halves have real positive-case evidence (the read half against issue #19, the write half in the scratch repo A3 authorized) — A2/A3 settling the architecture and venue is not the same as evidence existing yet; until real evidence lands, any doc mention names read/write maturity separately and honestly (constitution §1). | `/peer-review` of `README.md`/`ROADMAP.md` against the evidence record |
| NFR-10 | Security / Accessibility | N/A — `security` lens off, no runtime, no UI (constitution §4). | N/A |

## 6. Out of Scope

- **Any tracker other than GitHub Issues** (Jira, Linear, GitLab Issues, Azure
  DevOps, MCP-based trackers). Named, real, and explicitly future (A4).
- **Reading the tracker's state back, at any point, ever.** No polling, no
  reminder, no re-check of whether the issue was closed, reopened or
  commented on by someone else — constitution §6, the ROADMAP's own "one
  direction only."
- **More than one write per feature.** No running commentary, no per-gate
  comment (not at spec-approved, plan-approved, review-passed or QA-passed —
  only at `/go-live`'s own terminal close), no edit to a comment once posted
  (AC-2.7).
- **Closing or labeling the issue.** A single comment only, in v1 — closing
  someone's tracker item automatically is a stronger, less reversible action
  than commenting and is deferred, not assumed safe.
- **Cross-repo ticket references** (`owner/repo#42`, full URLs to a different
  repo). Only the current repo's own remote (A6).
- **A `tools/gh.md` ambient-probe file.** Deliberately not built (A5) — this
  is an explicit dependency of an explicit ask, not ambient enrichment.
- **A new slash command or agent, or a new tool grant on any existing agent**
  (A7).
- **Validating or normalizing ticket-reference formats** beyond matching a
  bare issue number against this repo's own remote.
- **Backfilling `Ticket` rows or write-back into already-shipped features.**
- **A per-feature override of the declared write-back mode** — the
  constitution declares once; a spec does not re-declare (same ruling
  `tracker-handoff` made for its own delivery-mode field). A2's resolution
  settled that the field exists, not that it can be overridden per feature.
- **This repo's own constitution amendment to enable dogfooding the positive
  case.** A3 ruled a *separate*, disposable scratch repo instead, precisely
  so this repo's own `Ticket-reference format: none` (§7) stays unamended;
  amending a constitution for dogfooding remains `/charter`'s call, not this
  spec's.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-21 | Should ticket-reference *format* (already in §7) also authorize write-back, so one field covers both? | **No — kept separate, deliberately.** A project's `Ticket-reference format` being GitHub-shaped says nothing about whether it *wants* aSPARK to take an outward action against its tracker; conflating the two would silently authorize a side effect just because an ID happens to look right — the "a check that fires where it doesn't apply" failure mode, inverted into an unwanted write. A2 proposes a second, explicit field for exactly this reason. |
| C2 | 2026-09-21 | Does the read half need a `tools/` file, given `gh`'s availability is installation state? | **No (A5).** `tools/`'s silent-probe apparatus exists for *ambient* enrichment offered on the ceremony's own initiative in every run. Here the user's own argument is the ask; `gh`'s absence is reported plainly, not silenced, because silence is for things nobody asked for. |
| C3 | 2026-09-21 | Is `handed-off`/`aborted` also a valid trigger for write-back, or only `released`? | **All three terminal statuses, never `preparing`.** `preparing` means nothing has concluded yet — writing a comment then would be exactly the "commentary as it goes" the ROADMAP rules out. AC-2.1 lists all three explicitly so a reader doesn't have to infer it. |
| C4 | 2026-09-21 | Given constitution §7's `Ticket-reference format: none` for this repo, can the write-back positive case be proven here at all? | **No — same structural block `tracker-handoff` hit (A3).** A3 proposes a disposable scratch repo, requiring the user's explicit authorization before it is created; not assumed here. The read half's positive case can still be proven on this repo's own already-public issue #19, read-only, writing to an untracked scratch path. |

## 8. Design Review

- **Status: N/A — no UI surface.** This feature changes Markdown prompt
  material and one constitution field only (`skills/`, `agents/`,
  `templates/constitution.md`); it renders nothing. The Designer's heuristics
  have no artifact to apply to.

---

## Named Risks

- **R1 — `gh` availability/auth drifts between machines.** A maintainer who
  authored the ticket on one machine may run `/go-live` on another without
  `gh` configured. Mitigated by NFR-5/AC-2.3 (skip, never block); not solved.
- **R2 — Rate limits.** Unauthenticated or heavily-scripted `gh` use can hit
  GitHub's API limits. Named, not designed for — occasional per-feature calls
  are far below any realistic limit; accepted risk.
- **R3 — A2/A3 resolved 2026-09-21.** Closed: write-back requires a new
  constitution field, split from a read half that needs none (A2); the
  write-back positive case is proved in a disposable scratch repo, discarded
  after (A3). No longer a blocker for `approved`.
- **R4 — Write-back as a second escape hatch.** Same shape as
  `tracker-handoff`'s R1: once posted, nothing corrects a comment that turns
  out wrong (e.g. `aborted` posted, then the team ships anyway under a new
  feature). Mitigated only by AC-2.7 (one write, ever) making the risk
  visible rather than hidden; not solved, same as its precedent.

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must — US-1, US-3 Must; US-2 Should (the half-size version is import-only, per "small beats complete")
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason) — NFR-1..10, `library` lens mapped (§1→NFR-2, §2→NFR-1, §4→NFR-3)
- [x] Clarify pass done: no ambiguity left unresolved or unparked — C1–C4 folded
- [x] Open questions are resolved or explicitly accepted as risk — A2 and A3 resolved 2026-09-21 (§3); R3 closes with them
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions — §5/§6 (privacy, degrade-to-silence, no unasked execution, outward-facing authorization) each bind an NFR above; §7's own `Ticket-reference format: none` is the direct source of A3, recorded rather than worked around
- [x] Design review done for UI-facing features (or marked N/A with reason) — N/A, §8
- [x] Line budget respected: Ist 233 / Soll ~250 (excluding HTML comments — none present) — under budget
- [x] Status set to `approved` by the user — **approved 2026-09-21**
