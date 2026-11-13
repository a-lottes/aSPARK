# Release: release-0.18.0

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `.spark/visual-qa-review/review.md` and `qa.md`; `.spark/trail-closing-and-cost-controls/evidence.md`; `.spark/light-path/evidence.md` |
| **Status** | `handed-off` |
| **Version** | v0.18.0 |
| **Date** | 2026-11-13 |
| **Commit** | release commit on `claude/project-thread-6tuvqo`, on top of `f601177` (PR #128); tag `v0.18.0` is made on the merge commit after the merge |
| **PR** | https://github.com/a-lottes/aSPARK/pull/129 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** a bundle release of everything merged since v0.17.0: visual QA review, a closing table built from the trail, `sonnet` as the default model with per-role overrides, a cap of two Reviewer rounds, and a light path for small changes.
- **Open:** `2 outstanding` — merge by a person, then tag `v0.18.0`; two of the three changes have no spec, plan, review or QA of their own (disclosed in §2).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

- [x] `visual-qa-review`: `review.md` `passed`, `qa.md` `passed` (B1 Minor, `claude plugin validate` not run, accepted)
- [ ] `trail-closing-and-cost-controls` (#127) and `light-path` (#128): no `review.md` or `qa.md`. Both were made directly on the maintainer's instruction; each has an `evidence.md` with dry runs (one session per case, no rate observed). Disclosed, not hidden
- [x] Test suite: none by constitution §4; `plugin.json` and `marketplace.json` parse as JSON; `git ls-files '*.py'` empty. `claude plugin validate .` not run (no CLI here)
- [x] Build: N/A, Markdown-only plugin
- [x] Working tree clean before the release edit
- [x] Branch fresh: cut from `origin/main` at `f601177`
- [x] Version: `plugin.json` 0.17.0 → 0.18.0. Minor: new optional behaviour (light path, §11 overrides, visual review) and a changed default model; no artifact format removed (constitution §5)
- [x] Diff fence: this report, `.spark/releases.md`, `plugin.json`, the companion versions in `docs/family.md` and the companion marker in `tools/README.md`

## 2. Changelog

### Added
- **Light path for small changes** (`light-path`, #128): at the spec gate `/story-time` runs six sizing checks and, only if all hold, offers a light path. The user chooses. The spec stays; `/spark` writes a short plan for approval, then build, one review, no `/demo-day`, then `/go-live`. Any open decision, a sixth task, a file outside the plan or an open Major after review returns the feature to the full loop. Switch off with `Light path: off` in constitution §11.
- **Visual QA review** (`visual-qa-review`, #124, issue #1): QA records one Visual Review row per screenshot of each UI state at wide desktop and phone width; a deviation from a `binding` design direction is at least Major; the `ux` lens checks start-up robustness; the Designer's craft check names scale and use of space.
- **Constitution §11 Models & Limits** (#127): optional per-role model overrides and limits.

### Changed
- **Default model is `sonnet` for every agent** (#127). Up to 0.17.0 the Engineering Manager and the Reviewer were pinned to `opus`. This lowers cost and may change review depth; name `reviewer: opus` in §11 to keep the old behaviour.
- **Reviewer rounds are capped at two** (#127), one on the light path. What is still open after the cap goes to the user.
- **The closing table is built from the trail** (#127): `/spark` reads the `Status` rows on disk instead of the session's own account of what passed.
- Companion marker in `tools/README.md` moves to `0.18.0`, because aspark-guard 0.3.0 adds a rule (`code-requires-approved-plan`) and aspark-graph 0.8.0 adds `impact --brief`. Users who have not declared both companions installed are offered them once more.

### Fixed
- Nothing claimed as fixed.

### Known limitations
- #127 and #128 have no review or QA of their own; their evidence is dry runs, one session per case, with no rate observed.
- The light path's token saving is not measured, and no full light loop through to a release has run yet.
- The Factory does not read the spec's `Path` row yet; a Factory line runs every ticket through the full loop.
- This is prompt material: a best-effort check, not a guarantee.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | `plugin.json` 0.17.0 → 0.18.0. No tag yet; tag `v0.18.0` on the merge commit after the merge (set locally; the cloud sandbox cannot push tags). |
| PR / merge | Prepared on request of the person. PR opened into `main`; a person merges it. |
| Deploy | N/A — handed-off; Factory lines pick it up with `./factoryctl aspark latest` after the tag |
| Post-release smoke check | N/A — handed-off |

Rollback: before merge, close the PR; after merge, `git revert -m 1 <merge-sha>` via a new PR (removes this record and the version bump only; the features themselves need their own reverts), and delete the tag if created.

## 4. Learnings (Keep!)

- **What went well:** the measurement runs that cost the most also produced the change: the light path and the `sonnet` default come straight from the token counts.
- **What we'd do differently:** two of three features skipped their own trail. Running them through the light path itself would have produced a review at least.
- **Patterns worth reusing:** state in the changelog which default changed and how to get the old one back.

---

## ✅ KEEP GATE

- [ ] All pre-flight checks passed at release time — no: #127 and #128 have no review or QA, disclosed above
- [x] Changelog written, known limitations named
- [ ] Merged and tagged — waits for a person
