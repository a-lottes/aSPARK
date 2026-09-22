---
name: story-time
description: >
  Start the Specify phase of the SPARK loop: the Product Owner interrogates a
  product idea and turns it into a spec with user stories and testable
  acceptance criteria. Use when the user brings a new feature idea, product
  idea or change request that has no spec yet — or wants an existing spec
  challenged and reworked.
---

# /story-time — Specify (Product Owner)

You are running the **Specify** ceremony. The Product Owner challenges the
idea; the outcome is a spec — or the insight that the idea shouldn't be built.

## Input

The user's feature idea, usually passed as the command argument. If no idea
was provided, ask for it before doing anything else.

Instead of an idea, the argument may be a bare GitHub issue number
(`/story-time 42`). Anything else — `#42`, a full issue URL, prose — is
treated as the idea text itself, not as a ticket reference; only a bare
number triggers the fetch below. Default when no argument is passed: unchanged from
today — ask for the idea, no ticket prompt, no mention that import is
possible. When an issue number **is** passed: resolve the current repo
**once**, from `origin` (`git remote get-url origin` / `gh repo view`), and
echo the resolved `owner/repo` to the user before fetching — this is the
only network-facing step in this ceremony, and the user should see which
repo it's about to read. If `origin` can't be resolved unambiguously (no
`origin`, or several remotes and no `origin`), **STOP** and report that
plainly — never guess a repo. Otherwise run
`gh issue view <n> --repo <resolved owner/repo> --json number,title,body,url`
— pinned to the same repo just echoed, never left for `gh` to re-resolve on
its own. If the issue doesn't
exist, the repo is private without access, or `gh` is missing or
unauthenticated, **STOP**, report the real error in plain language, and ask
whether to proceed with a manually supplied idea instead — never proceed
silently with an empty or invented brief. On success, pass the fetched
`title`+`body`+`url` into step 3 as **the idea** — everything downstream
(interrogation, Clarify pass, gate) proceeds exactly as it would for a typed
idea; a ticket is a seed for step 3's input, never a substitute for what
steps 3–8 do with it. If the target project's `.spark/` is tracked in git,
state once, before writing, that the imported title/description is about to
become part of a (possibly public) committed artifact, so the maintainer can
decide whether that ticket's content belongs there.

## Steps

1. **Name the feature.** Derive a short kebab-case feature name from the idea
   (e.g. `weekly-stats-dashboard`). If `.spark/<feature-name>/` already
   exists, ask the user whether to rework that spec or pick a new name.
2. **Resolve active lenses.** The constitution is the single source of truth. If
   `.spark/constitution.md` has a *Project Profile & Active Lenses* section, take
   the active lenses from it and pass their paths in step 3. If there's **no
   constitution**, do **not** resolve or apply lenses for this run — only give a
   lightweight **nudge**: glance at the repo (signals in
   `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`), name the likely type(s) in one line
   (e.g. "this looks like a public `website` — an `seo` lens would apply"), and
   point the user to `/charter` to record the profile so the lens activates for
   every phase. No lens is applied off a fallback guess; nothing is switched on
   without a constitution entry the user confirmed.
3. **Delegate to the Product Owner.** Invoke the `product-owner` agent with:
   the user's idea verbatim (or the fetched title+body, if this run started
   from an issue number — say so explicitly to the agent, don't let it
   rediscover the source), the feature name, the path
   `.spark/<feature-name>/spec.md`, and the spec template from
   `${CLAUDE_PLUGIN_ROOT}/templates/spec.md`. Point it at
   `.spark/constitution.md` if that file exists — the spec must live within it.
   Pass the paths of any active lenses (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`)
   so the PO captures their concerns as measurable NFRs. If this run started
   from an issue number, also tell it to cite the reference in the spec's
   `Ticket` row and state once, in §1, that the spec was seeded from that
   issue, with its URL.
4. **Relay, don't guess.** If the agent returns open questions instead of a
   spec, put them to the user (use AskUserQuestion where the options are
   enumerable), then re-invoke the agent with the answers. Repeat until the
   spec is drafted.
5. **Run the Clarify pass.** Once a draft exists, have the PO scan it for
   ambiguity against its taxonomy (functional boundaries, data, permissions,
   error/edge cases, NFRs, integrations, UX states, out-of-scope). Put the
   returned clarification questions to the user — AskUserQuestion for
   enumerable choices — and re-invoke the agent to fold each answer into the
   right section and log it in the spec's *Clarifications* table. Repeat until
   no high-impact ambiguity is left unresolved or unparked. Don't skip this
   because the draft "looks complete" — that's exactly when a whole category
   is silently missing.
6. **Present the result.** Show the user: the sharpened problem statement,
   the story list with MoSCoW priorities, the non-functional requirements,
   the named risks/assumptions, what was clarified, and what was cut to Out of
   Scope. If the PO recommends *not* building the feature, lead with that
   recommendation and its reasons.
7. **Iterate.** Fold the user's feedback back into the spec via the agent
   until the user is satisfied.
8. **Walk the gate.** Go through the SPEC GATE checklist at the bottom of
   the spec together with the user:
   - If the feature is UI-facing, the *Design Review* section is still empty
     — the gate stays open. Set status `draft` and hand off to
     `/look-and-feel`.
   - If design review is N/A (record why), ask the user for approval. Only
     on their explicit yes: set status `approved` and check the gate boxes
     that are genuinely true.

## Rules

- Never set `approved` without the user's explicit approval in this
  conversation.
- The spec contains no solutions — if technical questions come up, park them
  for `/sprint-plan`.

## Handoff

- UI-facing feature → **`/look-and-feel`** (Designer checks the spec)
- Spec approved, no design review needed → **`/sprint-plan`**
- Idea rejected → archive nothing; leave the spec with status `rejected` as
  a documented decision.
