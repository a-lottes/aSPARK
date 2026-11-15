# Release: release-0.19.0

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | PR #130 (`fix(agents): give engineering-manager and reviewer the aspark-graph MCP tools`) and its verification in the PR description |
| **Status** | `handed-off` |
| **Version** | v0.19.0 |
| **Date** | 2026-11-15 |
| **Commit** | release commit on `release/v0.19.0`, on top of `fa67fa5` (PR #130); tag `v0.19.0` is made on the merge commit after the merge |
| **PR** | https://github.com/a-lottes/aSPARK/pull/131 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** a release of one fix since v0.18.0: the Engineering Manager and the Reviewer can call aspark-graph's MCP tools when a session connects them.
- **Open:** `1 outstanding` — merge by a person, then tag `v0.19.0`.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

- [ ] #130 is a Path A fix (two agent files) with no `.spark/` trail of its own. Its evidence is in the PR: before and after runs of `aspark:reviewer` in a scratch repo, with and without the aspark-graph MCP server. Disclosed, not hidden
- [x] Test suite: none by constitution §4; `plugin.json` and `marketplace.json` parse as JSON; `claude plugin validate .` passes with warnings
- [x] Build: N/A, Markdown-only plugin
- [x] Working tree clean before the release edit
- [x] Branch fresh: cut from `origin/main` at `fa67fa5`
- [x] Version: `plugin.json` 0.18.0 → 0.19.0. Minor on the maintainer's call; the change adds a capability to two agents and removes nothing (constitution §5)
- [x] Diff fence: this report, `.spark/releases.md` and `plugin.json`

## 2. Changelog

### Added
- Nothing new beyond the fix below.

### Changed
- Nothing changed.

### Fixed
- **The Engineering Manager and the Reviewer can use aspark-graph** (#130). Both agents list their tools explicitly, so a session that connected the aspark-graph MCP server left them without it: on a Factory line, `plan.md` and `review.md` recorded the graph tools as missing while the session reported the server connected, and both agents scoped the blast radius by hand. The eight read-only graph tools and `build_graph` are now in both agents' `tools:`; each agent calls them itself when they are in its tool list. Without the server, nothing changes.

### Known limitations
- No rate is measured for how often the agents now call the graph; the evidence is one session per case.
- `/sprint-plan`'s own text still describes the Engineering Manager as asking the caller for the query; the agent file now says it calls the tools itself when they are connected.
- The companion marker in `tools/README.md` stays at `0.18.0`: what a companion buys did not change, so nobody is re-offered.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | `plugin.json` 0.18.0 → 0.19.0. No tag yet; tag `v0.19.0` on the merge commit after the merge. |
| PR / merge | Prepared on request of the person. PR opened into `main`; a person merges it. |
| Deploy | N/A — handed-off; Factory lines pick it up with `./factoryctl aspark v0.19.0` after the tag |
| Post-release smoke check | N/A — handed-off |

Rollback: before merge, close the PR; after merge, `git revert -m 1 <merge-sha>` via a new PR (removes this record and the version bump only; #130 needs its own revert), and delete the tag if created.

## 4. Learnings (Keep!)

- **What went well:** the Factory's own metrics line (`graph_server=connected`) next to the trail's "tool missing" pointed straight at the agents' frontmatter.
- **What we'd do differently:** an agent with an explicit `tools:` list does not inherit MCP tools; a companion that works through MCP has to be named in every such list it should reach.
- **Patterns worth reusing:** test an agent's tool surface by asking it to list its tools, with and without the companion, before and after the change.

---

## ✅ KEEP GATE

- [ ] All pre-flight checks passed at release time — no: #130 has no trail of its own, disclosed above
- [x] Changelog written, known limitations named
- [ ] Merged and tagged — waits for a person
