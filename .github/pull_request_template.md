<!-- Thanks for contributing. Delete any section that genuinely doesn't apply. -->

## What and why

<!-- What changes, and what problem it solves. -->

Closes #

## Which path

<!-- See "Two contribution paths" in CONTRIBUTING.md. -->

- [ ] **Path A** — scoped change (a lens, docs, a fix in one file). No `.spark/` artifacts needed.
- [ ] **Path B** — a change to the loop (new skill or agent, gate behaviour, templates, phase hand-over). `.spark/<feature>/` is committed with this PR.

## How I verified it

<!-- Required. This repo has no test suite, so this section IS the evidence.
     What did you run, what came out, what did you expect? -->

- [ ] `claude plugin validate .` passes
- [ ] I exercised the affected phases against a real or scratch project — result below

<!-- If this adds an optional capability: the negative case runs first. In a project
     where the new thing is absent, nothing may change — no error, no warning, no mention. -->

## Checks

- [ ] English throughout — docs, skills, agents, templates and any `.spark/` artifacts
- [ ] No protected template heading, column or ID pattern renamed or removed (§3 of `.spark/constitution.md`) — appending a column is fine
- [ ] No slash command renamed or removed
- [ ] No new dependency on a package, tool or sibling repo
- [ ] Plugin-internal paths use `${CLAUDE_PLUGIN_ROOT}/…`, never relative
- [ ] IDs (`US-` / `AC-` / `NFR-` / `T` / `F`) appended, never renumbered
- [ ] README updated in this PR if it adds or changes a capability
- [ ] Nothing private committed — `.spark/` is tracked and public

## Breaking change?

<!-- If yes: what breaks for someone who already has aSPARK installed?
     Leave the version alone — the maintainer sets it at release. -->
