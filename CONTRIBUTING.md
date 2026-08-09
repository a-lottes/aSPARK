# Contributing to aSPARK

Thanks for being here. aSPARK is a small project with a specific shape, and the
few things that are unusual about it are worth knowing before you write a line.

**This repo has no code.** It ships Markdown prompt material plus two JSON
manifests — no runtime, no build step, no dependencies, no test suite. That single
fact drives most of what follows: there is nothing to `npm install`, nothing to
run green, and *verification has to be done by hand and written down.*

**aSPARK is built with aSPARK.** The loop in the README is the loop this repo
uses on itself. You do not always have to run it (see below), but it explains why
the repo is full of `.spark/` directories.

---

## Ways to contribute

| | Where to start |
|---|---|
| Something behaves wrong | [Open a bug report](../../issues/new?template=bug_report.yml) |
| Add a lens for a concern aSPARK doesn't cover | [Propose a lens](../../issues/new?template=new_lens.yml) — and read *[Adding a lens](#adding-a-lens)* |
| An idea for the loop, a skill or an agent | [Open an enhancement](../../issues/new?template=enhancement.yml) |
| You ran aSPARK on a real project | [File a field report](../../issues/new?template=field_report.yml) — **the most valuable thing you can send us right now** |
| Docs are wrong or unclear | A PR straight away is fine |

Look for [`good first issue`](../../issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
if you want something scoped and ready to go.

> **Field reports really are the gap.** [`docs/status.md`](docs/status.md) lists
> exactly one thing as unproven: the lens layer has never been through a full loop
> run on someone else's real project. A report saying "I ran this on my API and
> here's where it got annoying" is worth more to aSPARK than most patches.

**Before you start on something sizeable,** comment on the issue (or open one).
Not for permission — so two people don't build the same thing, and so a design
disagreement surfaces before you've written it.

---

## Two contribution paths

How much process your change needs depends on what it touches.

### Path A — a scoped change

A lens, a docs fix, a wording correction, a bug fix inside one file.

**No `.spark/` artifacts required.** Open a normal PR. It must state:

- what you changed and **why**
- **how you verified it** — see below

### Path B — a change to the loop itself

A new skill or agent, a change to gate behaviour, anything touching `templates/`,
or a change to how phases hand over to each other.

**Run the loop on it and ship the artifacts.** Commit `.spark/<your-feature>/`
alongside the change: `spec.md`, `plan.md`, `review.md`, `qa.md`, `evidence.md`.
[PR #3](https://github.com/a-lottes/aSPARK/pull/3) is the reference shape.

This isn't ceremony for its own sake — the project constitution requires it:

> *A change to the loop is validated by running the loop.*

If you're unsure which path applies, ask in the issue. Guessing A when it's B just
means we'll ask for the artifacts in review; nothing is lost.

---

## How to verify a change

There are no tests to run. The bar, from the constitution, is two things:

**1. The plugin still validates.**

```bash
claude plugin validate .
```

**2. You exercised the change and wrote down what happened.**

Install your working copy and actually use the affected commands:

```bash
git clone https://github.com/a-lottes/aSPARK.git
claude --plugin-dir /path/to/aSPARK
```

Then run the phases you touched, on a real project or a scratch one, and put the
result in the PR — what you ran, what came out, what you expected.

**If your change adds an optional capability, run the negative case first.** In a
project where the new thing is *absent*, nothing may change: no error, no warning,
no mention. That's a non-negotiable, and it's the case most likely to be broken by
a well-meaning patch.

> "It reads correctly" is not verification. Prompt material fails in ways that only
> show up when an agent actually runs it.

---

## Adding a lens

The most self-contained way to contribute, and the reason `lenses/` exists as a
directory: **a new concern is a new file, never an edit to the agents.** Skills
pass lens paths generically, so a lens plugs in without rewriting anyone's role.

Copy [`lenses/cli.md`](lenses/cli.md) as your model. A lens needs:

1. **Frontmatter** — `name`, `applies-to` (the project types or characteristics
   that switch it on), `phases` (which SPARK phases own its checks).
2. **An activation statement** — and, just as importantly, **where it stays
   silent.** From the constitution: *suppression is a feature.* A check that fires
   where it doesn't apply teaches users to skim, which erodes trust in every other
   check. A lens that can't name where it's off isn't ready.
3. **A "Who owns what" table** — each area mapped to a phase and the agent who
   runs it. If a phase has no role here, say so explicitly and why (see the "No QA
   row" note in the CLI lens).
4. **The checklist** — every item tagged with its owning phase, every item
   falsifiable. "Consider performance" is not a check; "no render-blocking
   resource above 50 KB on the critical path" is.
5. **Phase notes** — what the PO should turn into ACs/NFRs, what the Reviewer
   should trace in the diff.

Then wire it up: add the lens to the activation table in
[`lenses/README.md`](lenses/README.md) and to the lens list in `README.md`.
Docs ship in the same change as the capability.

A lens **flags concerns and proposes NFRs. It never invents scope.**

---

## Things that will get a PR sent back

Not style nits — these are load-bearing.

- **Renaming or removing a protected template structure.** A sibling repo parses
  artifacts shaped by `templates/` and there is *no version handshake*, so a rename
  is a silent breaking change in someone else's tool. The protected headings,
  columns and ID patterns are listed in §3 of
  [`.spark/constitution.md`](.spark/constitution.md). **Appending a column is
  fine**; renaming one is not.
- **Renaming or removing a slash command.** Same reason — people have it installed.
- **A hard dependency on anything.** No npm, no Python, no sibling repo, no
  external tool. aSPARK installs into arbitrary projects that have none of it. An
  optional integration must degrade to *silence*, never to an error.
- **Relative plugin paths.** Always `${CLAUDE_PLUGIN_ROOT}/…`.
- **Renumbering IDs.** `US-` / `AC-` / `NFR-` / `T` / `F` identifiers are permanent
  and append-only. Breaking a downstream citation is a defect, not a cosmetic issue.
- **Anything but English.** Everything committed is English without exception —
  docs, skills, agents, templates and `.spark/` artifacts — whatever language the
  conversation happened in.
- **Anything private.** `.spark/` is tracked in this repo, so everything under it
  is published. No secrets, no credentials, no customer material, anywhere.
- **A capability without its README entry.** Docs ship in the same PR.

---

## Commits, branches, PRs

- **[Conventional Commits](https://www.conventionalcommits.org/)** — `feat:`,
  `fix:`, `docs:`, `chore:`.
- **One branch per change, prefixed with its type** — `feat/performance-lens`,
  `docs/fix-install-steps`.
- **PRs go into `main`.** This repo delivers by pull request, never by direct push
  — that applies to the maintainer too.
- **Don't bump the version.** `.claude-plugin/plugin.json` holds the single version
  and the maintainer sets it at release time.
- Link the issue your PR closes (`Closes #7`).

Small PRs get reviewed fast. A PR that changes one thing and explains how it was
verified is close to unrejectable.

---

## Questions

Open an issue with the `question` label, or ask on the issue you're working from.
If something in this document is wrong or unclear, that's a docs bug — file it.

By contributing you agree that your work is licensed under the
[MIT License](LICENSE), like the rest of the project.
