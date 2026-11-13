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
   exists, ask the user whether to rework that spec or pick a new name. Exception: a bare issue number whose existing spec has a `Gate comment` URL is a **resume**, not a rework: skip steps 3-7 and continue at step 8 with *Ticket gate question* step 3.
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
3. **Delegate to the Product Owner.** Pick the model first: if
   `.spark/constitution.md` §11 names a model for `product-owner`, pass exactly
   that as the agent call's `model`; if it names none, or there is no
   constitution or no §11, pass no model, so the agent's own default
   (`sonnet`) applies. Then invoke the `product-owner` agent with:
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
   - **Size the route, in the same question as the approval.** A small
     change does not need the whole loop; a change with an open decision
     does. Offer the **light path** only when **every** line below holds,
     each read from the spec or the repo now, not remembered:
     1. the spec has exactly one story and at most four acceptance criteria;
     2. §3 *Assumptions & Open Questions* has no row without a resolution,
        and no assumption that decides behaviour which the user has not
        confirmed in this conversation;
     3. design review is N/A: nothing user-visible in a UI changes;
     4. the change touches no authentication, permission, payment or
        personal-data behaviour, no stored data format or migration, and
        nothing callers outside this repository rely on: a published
        package API, a CLI flag, an HTTP endpoint, a file format;
     5. no **other** feature's trail names the files this change will touch:
        `grep -rlF` each file **path** the change will touch (for example
        `src/greet.py`, never a bare word such as `greet`) across
        `.spark/*/spec.md` and `.spark/*/plan.md`, leaving out this
        feature's own folder. A hit means another feature made a promise
        about that file, so the route is `full`; do not argue a hit away.
        If the spec names no file yet, find the one or two files by reading
        the code first;
     6. `.spark/constitution.md` §11 does not say `Light path: off`.
     If all six hold, tell the user in two lines what the light path skips
     (the Engineering Manager's plan, the QA Tester, a second review round)
     and what it keeps (this spec, a short plan they approve, one review,
     the release gate), and ask: light or full. Only on their explicit
     choice of light, write the header row `Path` as `light`, and name
     `/spark` as the next step: it writes the short plan. `/sprint-plan` run
     on its own always makes a full plan. In every other
     case — a line fails, you could not check one, or the user did not
     choose — write nothing or `full`, and do not mention the light path at
     all when a line fails. Never choose `light` yourself. This rule is
     prompt material: it makes the right sizing likely, not certain.

### Ticket gate question (only when the spec was seeded from a ticket)

Applies when the `Ticket` row names a real issue and step 8 needs a user
decision (approval, or open questions). `Ticket` = `none`: skip this whole
section, behaviour unchanged. Resolve `owner/repo` from `origin` as in
*Input*, and always pass `--repo <owner/repo>`.

1. **Post once.** Read the spec header's `Gate comment` row. If it holds a
   comment URL, post **nothing** (a rerun never posts twice) and go to 3.
   Otherwise run one `gh issue comment <n> --repo <owner/repo>` with: a
   5-10 line spec summary, the open questions each with its recommended
   option, and how to answer (reply in the issue, e.g. "approve, option B";
   only write-access collaborators count). Record the returned comment URL
   in the header's `Gate comment` row in the same edit. If `gh` fails, record
   `Gate comment: skipped, <reason>` and carry on in the conversation only;
   never retry in the same run.
2. **Ask in the conversation as usual.** If no answer can come (autonomous
   run, no one present), stop with the spec `draft` and the comment posted.
3. **On resume, read the answer.** Run
   `gh issue view <n> --repo <owner/repo> --json comments` and take comments
   created **after** the gate comment, oldest first. For each author check
   `gh api repos/<owner/repo>/collaborators/<login>/permission --jq .permission`;
   only `admin`, `maintain` or `write` count. A comment from anyone else, or
   a failed permission check, is **not** a decision: ignore it and say so.
   The latest qualifying comment that approves or picks options is the gate
   decision: fold chosen options into the spec, and record in the spec's
   Clarifications table the quoted comment, its author and its link
   (the gate record). Without a qualifying comment the gate stays open.
   An approval still only sets `approved` per the Rules below.

## Rules

- Never set `approved` without the user's explicit approval in this
  conversation — or, for a ticket-seeded spec, a qualifying ticket comment
  from a user with write access (see *Ticket gate question*).
- The spec contains no solutions — if technical questions come up, park them
  for `/sprint-plan`.

## Handoff

- UI-facing feature → **`/look-and-feel`** (Designer checks the spec)
- Spec approved, no design review needed → **`/sprint-plan`**
- Idea rejected → archive nothing; leave the spec with status `rejected` as
  a documented decision.
