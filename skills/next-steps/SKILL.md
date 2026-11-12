---
name: next-steps
description: >
  Have the Product Owner survey the project's current state — shipped
  features, in-flight work, open findings, standing goals — and propose one
  concrete next feature ready to hand to /story-time or /spark. Use when the
  user has no idea in hand and asks "what should we build next", when a loop
  just closed and the next cycle needs a starting point, or when the backlog
  feels stale and needs a grounded suggestion instead of a guess.
---

# /next-steps — Propose the Next Feature (Product Owner)

You are running an **advisory** ceremony, not a gated one. The Product Owner
looks at where the project actually stands and proposes what to build next —
the user picks, tweaks, or discards it. Nothing here gets written to
`.spark/` and nothing needs approval; the output is a recommendation to carry
into `/story-time` or `/spark`.

## Input

None required. Optionally the user may point at a theme or constraint (e.g.
"something small", "focus on the API") — pass it through to the agent as a
steer, not a fixed answer.

## Steps

1. **Gather the loop state yourself — don't delegate this.** The
   `product-owner` agent cannot run `git` or walk `.spark/`. Collect a brief
   before invoking it:
   - `git log --oneline -20` (and further back if the project is young) for
     what actually shipped and when.
   - Every `.spark/<feature-name>/` directory: for `spec.md`, `plan.md`,
     `review.md`, `qa.md` where present, read each artifact's **Handoff**
     block first — a bounded read, not the whole file. Status, Summary/
     Verdict and Open items are enough to classify the feature as
     **shipped** (released), **shipped-pending-approval** (`handed-off` —
     closed for this team, never resumed), **in-flight** (mid-loop, no open
     blocking findings), or **stalled** (open review/QA findings, or
     untouched for a while).
   - Any *unresolved* findings sitting in the newest `review.md` or `qa.md` —
     these are open points, not just status flags. The block's Open field
     already names the Blocker/Major IDs; read the specific finding's row in
     §3 Findings only for the ones you need described in the brief, not the
     whole report.
   - `.spark/constitution.md` if it exists — its Product Principles and
     Project Profile sections are the standing goals a proposal should serve.
   - **If `.spark/constitution.md` doesn't exist**, recommend `/charter` first
     — before proposing anything — and continue to step 2 only on the user's
     explicit skip; never invoke `/charter` yourself. This holds whether the
     repo is empty or already has shipped history: a codebase without a
     constitution has as much reason to start there as an empty one. On an
     empty `.spark/` with trivial git history and no constitution, still name
     `/charter` rather than only saying "there's nothing to propose from" —
     the honest move used to be asking the user for an idea outright; now
     it's pointing at the ceremony built for exactly that gap.
   - If nothing exists yet in `.spark/` and git history is empty or trivial,
     say so plainly — there is no "state" to read yet — and ask the user for
     the first idea rather than fabricate one. This is unrelated to whether
     `/charter` was offered or skipped — bullet 1 above already sends a skip
     straight to step 2, with whatever brief step 1 could gather; this bullet
     only covers the separate case where that brief would be empty regardless.
     **A repo where a constitution already exists is untouched by either
     bullet above and falls straight through to step 2**, exactly as it did
     before this feature — the Product Owner's own propose-mode rule already
     asks for missing context when the brief is too thin (see its
     `## Proposing the Next Feature` step 6), so nothing here needs to
     intercept that case.
   - **Ticket system (best effort).** Try `gh issue list --state all --json
     number,title,state,labels,milestone,body,closedAt --limit 200` (or `glab
     issue list`, or a ticket MCP) and `gh pr list --state all --json
     number,title,state,body,mergedAt,headRefName --limit 200`. Capture labels, "blocked
     by" / "depends on" / "#N" references, milestones and linked PRs. If no
     tool works, note once for the closing report: "Could not see the
     tickets" (one line by design, aSPARK issue #110: a deliberate exception
     to aSPARK's own silent-fallback rule, waived by its maintainer) — then
     **skip the maturity ticket count, triage and gap bullets below** (no
     issue list means every function would look like a gap) and behave as
     before this feature.
   - **Project maturity.** Classify as **greenfield** (a constitution exists,
     little or no code, few or no tickets), **building** or **mature**, from
     `git ls-files` size, `git log` depth, `.spark/` history and ticket count.
     State the class and the evidence for it in the brief.
   - **Ticket triage.** From the open issues: drop any whose linked PR is
     merged (report as "done, close it" — never recommend it, never close it
     yourself, AC-4). An open issue is *ready* when everything it is blocked
     by / depends on is closed. Among ready issues prefer the one that
     unblocks others and fits the current phase. A blocked issue is never the
     pick while its blocker is open: the blocker is (AC-2).
   - **Ticket gaps.** Compare the constitution (Product Principles, §9,
     quality bars, active lenses), `ROADMAP.md` and `.spark/` specs with the
     open *and closed* issues. A function described there that no issue
     covers is a gap; a function an open issue covers is not (AC-3). Each gap
     carries its source, e.g. `constitution.md §3`.
2. **Delegate to the Product Owner.** Pick the model first: if
   `.spark/constitution.md` §11 names a model for `product-owner`, pass exactly
   that as the agent call's `model`; if it names none, or there is no
   constitution or no §11, pass no model, so the agent's own default
   (`sonnet`) applies. Then invoke the `product-owner` agent in its
   *propose* mode (see its `## Proposing the Next Feature` section): give it
   the brief from step 1 verbatim (shipped list, in-flight/stalled features
   with their open points, constitution excerpt or "none", the project
   maturity class with its evidence, the open issues with their blockers and
   linked PRs, the "done, close it" list, the gap list with sources, and
   whether the tickets were reachable), plus any user steer. Point it at `.spark/constitution.md` if present.
3. **Relay, don't guess.** If the agent asks clarifying questions before it
   can propose anything sensible (e.g. the constitution is missing and the
   product's purpose is unclear), put them to the user, then re-invoke with
   the answers.
4. **Present the result as a conversation, not a report dump.** Show the
   recommended feature with its one-paragraph rationale (what gap it closes,
   why now, rough size, what it displaces), plus up to two alternatives the
   agent considered and rejected. Lead with the recommendation, not the list.
   **Type the recommendation** on its first line as exactly one of
   `existing #N`, `gap` (new ticket, with `source`) or `foundation`. Then list
   up to two alternatives, then the remaining gaps as a short list (each with
   its source), then any "done, close it" issues. If the tickets were not
   reachable, say so once, here in this closing report and nowhere else. If
   the issue list loaded but the PR list did not, say that merged PRs could
   not be checked.
   **Machine-readable block for the Factory.** Only when `agent.yaml` exists
   in the repo or the caller asks for it (a plain interactive run stays
   free of it): end the report with one JSON
   object in a fenced `json` block:
   `{"type": "existing|gap|foundation", "title": "...", "summary": "...",
   "source": "constitution.md §x", "existing_issue": 42}`.
   `existing_issue` (integer) is optional and set only when `type` is
   `existing`; the Factory then labels and works that issue instead of
   filing a duplicate. Omit the key entirely otherwise (never `null`). (The Factory-side parsing lives in
   the aSPARK-Factory repo.)
5. **Let the user decide.** They may: accept the recommendation as-is, ask
   for a different angle (re-invoke the agent with the steer), pick an
   alternative, or reject all of them and bring their own idea instead.
6. **Hand off on confirmation.** Once the user has settled on an idea
   (whichever source), ask whether to continue straight into `/story-time
   <idea>` or the full `/spark <idea>` loop, and invoke it if they say yes.
   Do not invoke either automatically — this skill only produces the idea.

## Rules

- **Foundation first on greenfield.** Before any feature, propose foundation
  work derived from the constitution's stack and quality bars: an architecture
  decision or walking skeleton, project layout, test harness and CI. Reuse an
  open foundation ticket if one exists (`existing #N`).
- **An existing ticket wins** over a new idea of the same size.
- Never close issues and never file gap tickets here; a backlog is filed only
  on explicit request (`/backlog`).
- Ticket reading is best effort prompt material, not a guarantee.
- If the user wants a whole backlog filed as issues rather than one
  recommendation, point to `/backlog`; this skill stays read-only.
- Never write or modify files under `.spark/` — this ceremony produces a
  recommendation in conversation, not an artifact.
- Never treat the agent's proposal as chosen. It is a suggestion until the
  user says which one (or their own idea) to run with.
- If every existing feature is `released` or `handed-off` and nothing is stalled, say that explicitly before proposing something new — a clean state is worth naming,
  not skipped past.
- If a stalled feature (open review/QA findings, or a plan sitting unbuilt)
  exists, the agent must weigh *finishing it* against *starting something
  new* as one of the candidates — half-shipped work is a real cost.

## Handoff

- User picks a proposal or brings their own idea → **`/story-time <idea>`**
  or **`/spark <idea>`**, on their explicit go.
- No idea survives, or the user wants to think first → stop here; nothing to
  persist.
