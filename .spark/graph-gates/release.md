# Release: graph-gates

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3), `qa.md` (`passed`, round 2 final) |
| **Status** | `released` |
| **Version** | v0.4.0 |
| **Date** | 2026-07-27 |

> **Two passes, this conversation.** Pass 1 was prepare-only, per
> `skills/go-live/SKILL.md` step 2: pre-flight, version, changelog, staged
> commit/tag, rollback path — no outward-facing action. Pass 2 (this
> revision) executed the outward-facing steps after the caller relayed the
> user's explicit go. Both passes' pre-flight and changelog content below are
> unchanged from pass 1 except where noted (§1a, §3).

## 1. Pre-Flight Checks

<!-- Verified immediately before releasing — not copied from earlier reports. -->

- [x] `review.md` status is `passed` — round 3, binding ruling at §8.6: *"Passed
      ... the feature may go to `/demo-day`."*
- [x] `qa.md` status is `passed` — round 2 final, binding QA GATE: 25/30 Must-ACs
      pass, 6 partial (each with a named structural reason, none an unexamined
      gap), 0 not-verified-live, 0 fail. Set `passed` by the user's explicit
      decision with the six partials disclosed, not closed.
- [x] Full "test suite" green on the release commit, per this project's own bar
      (constitution §4: no automated suite exists or is possible for prompt
      material). `claude plugin validate .` run fresh on the working tree
      *before* committing and again *on the pushed commit* (§4 below) — both
      identical: `✔ Validation passed with warnings` (one pre-existing,
      unrelated warning on `marketplace.json`, untouched by this feature).
      `plugin.json` and `marketplace.json` parse as valid JSON in both checks.
- [x] Build succeeds from a clean state — N/A in the literal sense (no build
      step exists, constitution §0/§3), satisfied by the validate check above.
- [x] No uncommitted changes in the working tree, at commit time — confirmed
      by `git status --short` immediately before `git commit` (only this
      feature's 27 files staged, nothing else pending except the two
      out-of-scope untracked files, left alone throughout).

### 1a. Drift and scope check (fresh, this session)

- **Touched-file list matched scope**; nothing appeared or vanished since
  round 3 review / round 2 QA.
- **Timestamp check:** nothing under version control was newer than
  `.spark/graph-gates/qa.md`'s final edit — no undocumented post-gate change.
- **Two untracked files, unrelated to this feature, noticed and left
  alone, start to finish:** `docs/aSPARK_Enterprise_Architecture_Handbook.docx`
  and `.docx.bak` — not part of this release's diff or commit (tracked
  separately as `handbook-maturity` in `.spark/BACKLOG.md`).
- **`README.md`'s "Project Status" staleness — found in pass 1, fixed before
  publish.** Pass 1 of this release flagged that `README.md`'s proof table
  predated `qa.md`'s final reconciliation (understated proof, six ACs shown
  as unproven that QA's later record marks `pass`). Before authorizing
  publish, the user rewrote the section directly to match `qa.md`'s final
  25/30-pass, six-named-partials accounting, and re-staged it. **Re-verified
  in this pass:** `README.md`'s current table lists exactly the same six
  criteria, with matching reasons, as `qa.md`'s Full Reconciliation
  (AC-1.2, AC-2.2, AC-2.3, AC-3.2, AC-3.5, AC-5.2) — and is internally
  consistent with this report's own changelog (§3), which states the same
  six in plain language. No remaining mismatch found between `README.md`,
  `qa.md` and this file; nothing further to adjust.

## 2. Version

**v0.4.0** — minor bump, per NFR-1 and constitution §5 ("a new optional
capability is a minor bump"). The change is purely additive, touches no
protected structure in `templates/`, and needs no coordinated release with
any consuming repo. Sequential after `v0.1.0` → `v0.2.0` → `v0.3.0` →
`v0.3.1` → **`v0.4.0`**.

## 3. Changelog

<!-- User-facing language. What can they do now that they couldn't before? -->

### Added
- If you also have the companion tool `aspark-graph` installed and built for
  your repo, `/sprint-plan`, `/peer-review` and `/demo-day` now notice it on
  their own and use it to get a faster, better-scoped starting point — which
  files a plan's tasks touch, which code a review should read first, which
  stories and acceptance criteria a QA pass should focus on. You don't
  install, configure or flag anything to turn this on or off; it's detected,
  not switched.
- If you don't have it installed, nothing changes at all — every ceremony
  behaves exactly as it did before this release, with zero mention of the
  tool anywhere in its output.
- When the tool is present but its answer is out of date, empty, or the
  install is incomplete, ceremonies say so plainly (once, in one sentence)
  and fall back to reading the project by hand — the same way they always
  have. A tool answer is always offered as a map to help you look faster,
  never as a verdict that replaces looking.
- Plan tasks can now carry a short `files:` note in their Definition of Done,
  naming the files a task is expected to touch. This makes the link between
  a task and the code it produces explicit and readable — by a person or by
  a tool — instead of left implicit. It's added only when the files are
  actually knowable when the plan is written; a task whose files can't be
  predicted yet simply omits the note rather than guessing.
- A short guide (`tools/README.md`) documents how to wire up the next
  optional external tool the same way, so this doesn't become a one-off.

### Changed
- The plan template's guidance text was updated to explain the new `files:`
  note format. Nothing about the plan's structure changed: same headings,
  same columns, same task-numbering.
- The project's own status page (`README.md`) now states plainly what's
  proven about this feature and what's still open, matching the final QA
  record exactly.

### Fixed
- A stray working file the optional tool can leave behind in an interrupted
  state is now excluded from what gets tracked, so it can no longer end up
  committed and published by accident.

### Known limitations — disclosed, not hidden

This release ships with the QA gate set to `passed` by explicit user decision,
with **six acceptance criteria left in a documented "partial" state** rather
than closed. None is a broken feature; each has a specific, named reason it
wasn't fully proven this round, and every one falls back safely to
pre-release behavior if untested:

- Whether a fresh ceremony run's output is byte-for-byte identical to the
  previous version's, given the same input, hasn't been directly diffed
  run-to-run yet (would need one more full ceremony pair to check).
- If you have both an MCP connection *and* the command-line tool available
  at once, which one gets used first is documented but hasn't been tested
  live — no environment with an MCP server exists yet to test it against.
- The rule "mention the tool at most once per ceremony run" was verified at
  the tool level, but not yet inside an actual live ceremony conversation.
- What a ceremony does when the tool's answer is stale hasn't been tested on
  the ceremony's own reaction (the tool correctly reports "stale," twice
  over, but the ceremony's fallback-to-manual behavior after that point is
  untested live).
- `/demo-day`'s existing requirement for a real, working browser is
  untouched by this change — but this project itself has no browser
  surface, so that specific untouched behavior couldn't be re-proven live
  here (a pre-existing, documented exception for this repo, not a new gap).
- Omitting a `files:` note for a task whose files genuinely can't be known
  ahead of time is implemented and reasoned through, but this feature's own
  plan happened to have no such task, so the omission path itself wasn't
  exercised live.

Additionally, five small, non-blocking documentation gaps are known and
filed for a later pass (not fixed here, out of scope for release prep):
two are spec-wording items that belong with `/story-time`, not a developer
fix; three are one-line clarifications missing from the tool's own
documentation file. See `qa.md` §"Round 2 final counts" for the full list
with exact locations.

## 4. Release Actions

<!-- What was actually executed, with results. -->

| Action | Result |
|---|---|
| Version bump & tag | `.claude-plugin/plugin.json` at `0.4.0`. Release commit created on `main` (27 files: the 17 modified + `.spark/BACKLOG.md`, `.spark/constitution.md`, `.spark/graph-gates/{PATCH-PLAN,evidence,plan,qa,review,spec}.md`, `tools/{README,aspark-graph}.md`). Annotated tag `v0.4.0` created locally, pointing at that commit. **Executed.** |
| PR / merge | Not applicable — this repo releases directly on `main` (established pattern: `v0.1.0`–`v0.3.1`, no per-release PR). |
| Deploy | Pushed `main` to `origin` (fast-forward, `fb6af66..8eadc99`) and pushed tag `v0.4.0` to `origin`. Both confirmed reachable on the remote after a fresh `git fetch` (see exact record below). **Executed.** |
| Post-release smoke check | Re-ran `claude plugin validate .` on the pushed commit (identical result to pre-flight: passes, one pre-existing unrelated warning); confirmed `plugin.json` reports `0.4.0` on the released tree; confirmed `origin/main` and `refs/tags/v0.4.0` on the remote match local exactly via `git ls-remote`/`git fetch`; confirmed the working tree is clean of anything belonging to this feature. This project has no running app or server to curl — the equivalent "is it alive" check for a Markdown-plugin artifact is: *is the published ref fetchable, does it parse, does it report the right version* — all confirmed. **Passed.** |

### What was executed (exact record)

```
$ git commit -m "feat: wire aspark-graph as an optional, silent accelerant into the gates ..."
[main 8eadc99] feat: wire aspark-graph as an optional, silent accelerant into the gates
 27 files changed, 3984 insertions(+), 15 deletions(-)

$ git tag -a v0.4.0 -m "v0.4.0 - Graph-gates: an optional accelerant for the loop ..."

$ git push origin main
   fb6af66..8eadc99  main -> main

$ git push origin v0.4.0
 * [new tag]         v0.4.0 -> v0.4.0

$ git fetch origin --tags -q
$ git rev-parse origin/main            → 8eadc9934a4d939116f8ec8a59008d0bd682c25d
$ git rev-parse HEAD                   → 8eadc9934a4d939116f8ec8a59008d0bd682c25d   (match)
$ git ls-remote --tags origin v0.4.0   → c8b413741dd5610856db77a41563fe50990f3592  refs/tags/v0.4.0
```

**Release commit:** `8eadc9934a4d939116f8ec8a59008d0bd682c25d` on `main`.
**Tag object:** `v0.4.0` → `c8b413741dd5610856db77a41563fe50990f3592`, pointing at
the release commit above.

## 5. Rollback Path

If this release needs to be undone after publishing:

1. **Before anyone has updated:** `git revert` the release commit (`8eadc99`)
   on `main` (not `reset --hard` — this repo is public and other clones may
   already have fetched) and push the revert. Delete the remote tag
   (`git push origin :refs/tags/v0.4.0`) and the local one
   (`git tag -d v0.4.0`), then re-tag the prior commit (`fb6af66`, `v0.3.1`)
   if a marker is needed.
2. **After someone has updated:** the integration is opt-in and degrades to
   silence by construction (constitution §6) — a consumer with no
   `aspark-graph` installed sees no behavior change either way, so most
   installs are unaffected by a rollback delay. For an install that *does*
   have `aspark-graph` and hits a real problem, reverting to `v0.3.1`
   (`/plugin install aspark@aspark` pinned to the prior tag, or
   `git checkout v0.3.1 -- .` for a source install) restores the pre-change
   behavior exactly — no data migration, no schema, nothing to unwind.
3. **Template contract check before any rollback or forward-fix:** confirm
   `templates/` wasn't the trigger (`git diff v0.3.1 v0.4.0 -- templates/`
   shows only guidance-comment text, no heading/column/ID changes) — a
   rollback that also had to touch a protected structure would need
   coordination with `aspark-graph`, per constitution §3; this release's
   diff does not.
4. **No irreversible side effect exists to unwind.** No external account, no
   deployed service, no database row, no billing change — the only
   "irreversible" step was the push/tag itself, covered by steps 1–2.

## 6. Learnings (Keep!)

<!-- The K in SPARK: what does the team keep from this cycle? -->

- **What went well:** The negative case ran first and was recorded before any
  positive-case work (constitution §1's own rule, followed under real
  pressure). The six-partial disclosure in `qa.md` is a strong pattern:
  naming *why* something is untestable (no MCP server exists here; this repo
  has no browser; this plan has no unknowable-file task) is more honest and
  more useful than forcing a binary pass/fail on criteria that are
  genuinely environment-limited. The release pre-flight's own drift check
  (comparing file timestamps against the gate artifacts) caught a real,
  if non-blocking, documentation staleness in `README.md` before publish —
  the user chose to fix it rather than ship it stale, which is the loop
  working as intended.
- **What we'd do differently:** `README.md`'s "Project Status" table was
  edited mid-increment and QA then kept working past that edit, producing
  a real (if harmless, understating-not-overclaiming) staleness by the time
  release prep started. A rule of thumb worth adopting: the user-facing
  status doc should be the *last* thing touched before a gate closes, not
  the internal QA/review artifact, or the two will drift by construction.
- **Patterns worth reusing:**
  - **Add-a-file for optional tools** (`tools/<name>.md`, generic agent
    wiring, no product name outside the tool file itself) is now proven
    exactly once (`aspark-graph`) and documented as a repeatable recipe
    (`tools/README.md`). Strong candidate to reference from
    `.spark/constitution.md` §3 directly as "the pattern," not just as an
    example.
  - **Structural partials over forced binaries in QA.** `qa.md`'s
    "Full reconciliation" table (named reason per partial AC, counted
    separately from `not-verified-live`) is a reusable QA-report shape worth
    naming as a convention in `templates/qa-report.md`'s own guidance.
  - **Timestamp-based drift check at pre-flight** (nothing tracked newer
    than the last QA edit) cheaply catches "quiet edit after the gate
    closed" and, this cycle, caught a real doc-currency gap before it
    shipped — worth a one-line mention in `skills/go-live/SKILL.md`'s
    pre-flight step.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time (§1)
- [x] Changelog written in user-facing language (§3) — Added/Changed/Fixed
      plus known limitations stated plainly, six partials named without
      jargon or internal IDs beyond what a curious user could look up
- [x] Release actions executed and verified (§4) — commit `8eadc99`, tag
      `v0.4.0` (`c8b4137`), both pushed to `origin` and confirmed present on
      the remote via `git ls-remote`/`git fetch`; smoke check passed
- [x] Learnings recorded (§6)
- [x] Status set to `released`
