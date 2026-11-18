# Release: release-0.20.0

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | PR #134 (`ux lens: judge lists against the expected usage volume`) and its trail `.spark/ux-volume-findability/` |
| **Status** | `handed-off` |
| **Version** | v0.20.0 |
| **Date** | 2026-11-18 |
| **Commit** | release commit on `release/v0.20.0`, on top of `1e38d12` (PR #134); tag `v0.20.0` is made on the merge commit after the merge |
| **PR** | pending |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** a release of one change since v0.19.0: the `ux` lens judges lists, grouped pages and pickers against a declared expected usage volume.
- **Open:** `1 outstanding` — merge by a person, then tag `v0.20.0`.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

- [ ] #134 is a Path B change with `spec.md`, `plan.md` and `evidence.md`; `review.md` and `qa.md` were not produced (no `/peer-review` or `/demo-day` ran on it). Disclosed in the PR and here, not hidden
- [x] Test suite: none by constitution §4; `plugin.json` and `marketplace.json` parse as JSON; `claude plugin validate .` passes with warnings
- [x] Build: N/A, Markdown-only plugin
- [x] Working tree clean before the release edit
- [x] Branch fresh: cut from `origin/main` at `1e38d12`
- [x] Version: `plugin.json` 0.19.0 → 0.20.0. Minor: the change adds a lens section and a constitution table and removes nothing (constitution §5)
- [x] Diff fence: this report, `.spark/releases.md` and `plugin.json`

## 2. Changelog

### Added
- **Volume & findability in the `ux` lens** (#134). A project with `ux` active declares its expected usage volume in constitution §2 (today, after one year, upper bound per entity); `/charter` drafts and confirms it. `lenses/ux.md` §7 judges every list, grouped page and choice control against the after-one-year numbers, never against fixture size: an item reachable in at most three actions, bounded lists, no "n more not shown" line that leads nowhere, search or a context pre-filter for pickers with more than about 15 options, navigation for more than about 7 groups.
- **A QA volume run.** `/demo-day` walks each list screen with an after-one-year dataset at desktop and phone width and counts the actions to a chosen item; fixture-only is `⚠ not verified`.

### Changed
- **Cutting search, filter, sort or pagination is a decision.** For a list that fails §7, the cut needs a named follow-up or the user's recorded waiver; otherwise the Designer raises a `Major`, and the PO's Clarify pass asks it. This changes Design and QA verdicts for installed web projects that declare a volume.

### Fixed
- Nothing fixed.

### Known limitations
- Prompt-enforced and unmeasured. The evidence is one hinted Designer session per arm (old lens vs new) on a copy of one field project; Specify and QA were not exercised.
- In that run the old lens already found the three worst problems once the volume table was present; the declared volume is the load-bearing part, §7 adds the undecided-cut and missing-volume findings.
- Existing constitutions have no volume table until `/charter` runs again; until then §7's Specify row asks for it.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | `plugin.json` 0.19.0 → 0.20.0. No tag yet; tag `v0.20.0` on the merge commit after the merge. |
| PR / merge | Prepared on request of the person. PR opened into `main`; a person merges it. |
| Deploy | N/A — handed-off; Factory lines pick it up with `./factoryctl aspark v0.20.0` after the tag |
| Post-release smoke check | N/A — handed-off |

Rollback: before merge, close the PR; after merge, `git revert -m 1 <merge-sha>` via a new PR (removes this record and the version bump only; #134 needs its own revert), and delete the tag if created.

## 4. Learnings (Keep!)

- **What went well:** a dry run on a copy of the field project, old lens against new, separated what the lens text adds from what the declared numbers add.
- **What we'd do differently:** a lens that names a quality ("large data holds up") without a number to judge it by gets judged against the fixtures; give every scale check a reference number from the constitution.
- **Patterns worth reusing:** when a field report says "the lens was ignored", read the trails first; here it was applied every time and the gap was in what it asked.

---

## ✅ KEEP GATE

- [ ] All pre-flight checks passed at release time — no: #134 has no `review.md` or `qa.md`, disclosed above
- [x] Changelog written, known limitations named
- [ ] Merged and tagged — waits for a person
