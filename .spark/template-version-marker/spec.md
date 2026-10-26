# Spec: template-version-marker

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |

## User Story

**US-1** As a maintainer of a consumer of aSPARK artifacts (`aspark-graph`,
`aspark-guard`), I want every template to carry a version marker, so that template
drift surfaces as a named version conflict instead of a structural guess.

Issue: #44. Roadmap item: "A template version handshake".

## Acceptance Criteria

- **AC-1** Every file in `templates/` carries `<!-- aspark-template: aspark/0.1.0 -->`
  on line 3, directly after the title.
- **AC-2** The marker is an HTML comment only: no protected heading, table row or
  field of any template is renamed or removed.
- **AC-3** The constitution's template-contract note states that the marker is the
  contract version (not the plugin version) and when to bump it.
- **AC-4** `ROADMAP.md` states that core's side is shipped and that the reading
  side (items 2 and 3 below) is still open.

## Scope

In this repo (core): item 1, the marker in all templates.
Not in this repo: item 2 (`aspark-graph` asserts the marker, replacing its
structural guess with a named version conflict) and item 3 (`aspark-guard` reads
the marker instead of its own copy). These are delivered in the consuming repos.

## Release coordination (items 2 and 3)

The ROADMAP rule is that all repos ship the reading side together. A marker that
nobody reads is inert, and this change alone must not reach a release. Plan:

1. **Hold the release.** This change merges to `main` but is not tagged or
   released (`/go-live` not run) while items 2 and 3 are open. The ROADMAP entry
   stays under **Blocked** until both land.
2. **Track the other halves.** File one issue each in `aSPARK-graph` (assert
   `aspark-template` against `SUPPORTED_TEMPLATE`, raise a named version
   conflict on mismatch, keep the structural check as fallback for unmarked
   artifacts) and `aSPARK-guard` (read the marker instead of its own copy).
   Each links back to #44.
3. **Agree the value.** All three repos use `aspark/0.1.0`. Any change to a
   protected structure bumps the marker in core and both consumers in lockstep.
4. **Release together.** When both consumer PRs are approved, release core,
   `aspark-graph` and `aspark-guard` in one coordinated window, core's tag
   referencing the two consumer versions. Only then does the ROADMAP item move
   from Blocked to shipped.
5. **Compatibility.** Consumers must tolerate a missing marker (older artifacts
   already in target projects), so release order within the window is not
   critical.

## Not verified here

The consumers' behaviour cannot be verified from this repo.
