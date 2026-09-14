# Release: companion-offer

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `preparing` |
| **Version** | v0.8.2 (proposed only — `pr` mode) |
| **Date** | 2026-09-14 |

**Handoff**
- **Status:** mirrors the header table above. `preparing` — pre-flight is fresh-verified green and everything reversible/local is drafted below; nothing outward-facing has run.
- **Summary:** `companion-offer` documents the previously-undocumented `aspark-guard` companion plugin across `README.md`, `tools/README.md` and `ROADMAP.md`. Docs-only; both gates `passed`; patch bump `0.8.1` → `0.8.2` proposed; PR mode, awaiting the user's explicit go to commit, push and open the PR.
- **Open:** `2 outstanding` — (1) F5 (`review.md` Nit) not yet closeable: no commit exists yet on this branch, so `git diff --name-only main...HEAD` is currently empty by construction, not by verification — owner: whoever runs the commit below, then re-runs that diff. (2) The working tree still carries the increment's own uncommitted/untracked changes — owner: same commit.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on the exact uncommitted release content — not copied from `review.md`/`qa.md`.*

- [x] `review.md` status is `passed` — REVIEW GATE checklist read at `.spark/companion-offer/review.md:96-102`: no open Blocker/Major, four Minors fixed r1, two Nits open (F5 named above, F6 closed), status `passed`.
- [x] `qa.md` status is `passed` — QA GATE checklist read at `.spark/companion-offer/qa.md:78-84`: every Must/Should AC and every QA-owned NFR verified live, no Blocker/Major/Minor, status `passed`. QA method: this project's standing constitution §8 declaration — no browser-observable surface exists here, so QA runs hands-on against the installed plugin instead of in a browser, a project-wide decision made once at `/charter`, not a per-feature waiver. `qa.md` records every AC-/NFR- ID against that method, same as always.
- [x] Full test suite green — N/A, none exists or is possible for prompt material (constitution §4). Substitute bar re-run fresh just now: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning, confirmed out of this diff's scope — `.claude-plugin/` untouched, see NFR-1 below).
- [x] Build succeeds from a clean checkout — N/A, no build step (constitution §3/§4); `claude plugin validate .` is the equivalent bar and passed, above.
- [ ] No uncommitted changes in the working tree — **currently false, by design at this point in the ceremony.** Re-verified fresh: `git status --porcelain` → `M README.md`, `M ROADMAP.md`, `M tools/README.md`, `?? .spark/companion-offer/`. `git diff --name-only main -- .` → exactly `README.md`, `ROADMAP.md`, `tools/README.md` — matches `review.md`'s and `qa.md`'s NFR-1 rows byte-for-byte; nothing drifted since QA closed. Stays unchecked until the commit in §3 lands.

**Branch staleness (project `CLAUDE.md` house rule).** `git rev-parse HEAD`, `main` and (post-fetch) `origin/main` are all `d1337a3` — the branch carries zero commits of its own yet, only local working-tree edits. Not stale; nothing to rebase.

**Version confirmed.** `.claude-plugin/plugin.json` reads `"version": "0.8.1"`, untouched by this feature's diff (confirmed above) — matches spec/plan/evidence's stated starting point.

## 2. Changelog

### Added
- `README.md` now documents the second optional companion, `aspark-guard` — what it does, that it's optional, and the exact command to install it yourself.

### Changed
- `README.md` and `tools/README.md` now distinguish three kinds of optional extras — a lens the project profile turns on, a tool a ceremony detects automatically, and a companion plugin you install yourself — so it's clear at a glance which one applies to something new you're considering.
- `README.md`'s status table and `ROADMAP.md` now both account for `aspark-guard`, with an honest, qualified maturity note (substantial self-tested evidence from its own author; not yet independently verified by this project; never exercised through a third party's own feature loop) rather than a bare "proven" or "unproven" label.

### Fixed
- Nothing was previously broken; this closes a documentation gap — the second companion plugin was shipped and installable but named in no tracked doc.

*(No behavior, command, or file any ceremony reads changed — verified below, NFR-1/NFR-5.)*

## 3. Release Actions

*Prepared, not executed. Outward-facing steps require the user's explicit go, relayed by the invoking session — none has been given yet.*

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only:** `0.8.1` → `0.8.2`, **patch** — docs-only change, adds no optional capability (constitution §5's minor-bump trigger absent); same shape as the `0.8.0`→`0.8.1` `situational-lenses` precedent. No tag — `pr` mode creates the tag at/after merge, outside this ceremony's control. Not yet executed. |
| PR / merge | **Not opened.** Title/body drafted below, target `main`, ready once the user gives the go. No merge — approver is self-review-via-PR (solo maintainer), per constitution §7. |
| Deploy | N/A — no deploy surface; this repo *is* the distributed artifact, consumers pull it via `/plugin install`/marketplace update, not a push from here. |
| Post-release smoke check | N/A — nothing has merged or deployed. This ceremony's local analogue, `claude plugin validate .`, already re-ran fresh above and passed. |

**Exact commit #1 — the increment's changes (closes F5 once run and re-diffed):**
```
docs: companion-offer — document aspark-guard across README, tools/README, ROADMAP

Closes the AC-1.1 discovery gap (aspark-guard was named in zero tracked
.md files): README.md #Optional Tools gains a companion-plugin entry with
the qualified maturity statement, the nothing-installs-for-you clause and
the exact install command; #Project Status scopes the existing row to
aspark-graph and adds one for the guard. tools/README.md's "Tool or
lens?" table gains a third shape, companion plugin, with aspark-guard as
its example, and states that a tool file for one is a defect.
ROADMAP.md accounts for Core-side gate enforcement in the Not planned
table, pointing at the sibling plugin. Docs-only: no path under skills/,
agents/, templates/, lenses/ or .claude-plugin/ changes, and under
tools/ only README.md does (NFR-1). review.md passed round 1 (4 Minors
fixed); qa.md passed round 1, 16/16 AC verified hands-on, including a
live `/plugin install aspark-guard@aspark`.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
Files: `README.md`, `ROADMAP.md`, `tools/README.md`, `.spark/companion-offer/{spec.md,plan.md,evidence.md,review.md,qa.md}`.
**After this commit, re-run** `git diff --name-only main...HEAD` — expected: exactly those eight paths. That closes F5.

**Exact commit #2 — prepare the release (version bump; separate from the increment per NFR-1/T7):**
```
chore: prepare companion-offer release, propose v0.8.2 (pr mode, awaiting go)

Bumps .claude-plugin/plugin.json 0.8.1 -> 0.8.2 (patch: docs-only, no new
optional capability added, no protected structure touched -- same shape
as the 0.8.0 -> 0.8.1 situational-lenses precedent). review.md (passed,
round 1) and qa.md (passed, round 1) both fresh-verified green at
pre-flight; branch confirmed not stale against origin/main. No tag, no
push, no PR yet -- pr mode, prepared and awaiting the user's explicit
go. See .spark/companion-offer/release.md.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
Files: `.claude-plugin/plugin.json`, `.spark/companion-offer/release.md`.

**Draft PR (target `main`, ticket format `none` per constitution §7):**
- **Title:** `docs: document aspark-guard across README, tools/README, ROADMAP`
- **Body:**
  ```
  ## Summary
  - Documents the second optional companion, `aspark-guard`, in README.md
    Optional Tools and Project Status -- previously named in zero tracked
    .md files despite being shipped in marketplace.json.
  - Adds a third shape (companion plugin) to tools/README.md's "Tool or
    lens?" table, distinct from a lens or a tool, so a contributor doesn't
    create a tools/aspark-guard.md that no ceremony could ever pick up.
  - Accounts for the guard in ROADMAP.md's Not planned table, scoped to
    Core-side gate enforcement, pointing at the sibling plugin.
  - Docs-only: no path under skills/, agents/, templates/, lenses/ or
    .claude-plugin/ changes; under tools/ only README.md does. Proposes a
    patch bump, 0.8.1 -> 0.8.2 (no new optional capability added).

  ## Test plan
  - [x] review.md passed, round 1 (.spark/companion-offer/review.md)
  - [x] qa.md passed, round 1, 16/16 AC + all QA-owned NFRs verified live,
        hands-on against the installed plugin (.spark/companion-offer/qa.md)
  - [x] `claude plugin validate .` passes locally (re-run at /go-live
        pre-flight; one pre-existing, out-of-scope warning)
  - [x] `git diff --name-only main -- skills/ agents/ templates/ lenses/
        .claude-plugin/` empty; under tools/ only README.md changed
  - [ ] Self-review and merge by the declared approver (a-lottes)
  ```

**Rollback path.** Docs-only, single-file-set change, no data migration, no version dependency from another feature. If something's wrong post-merge: `git revert <merge-commit-sha>` on `main` restores `README.md`, `ROADMAP.md`, `tools/README.md` and `.claude-plugin/plugin.json` (back to `0.8.1`) in one commit, no coordination with the `aspark-graph` consumer needed (no protected template structure touched). Before merge, rollback is simpler still: close the PR / stop short of merge. Nothing external depends on `0.8.2` existing.

## 4. Learnings (Keep!)

- **What went well:** the T1 "pin the canonical wording once, quote it three times" pattern (plan §1 rule 1) worked exactly as designed — `evidence.md`'s long form, short form and install string, each cited to its own source, meant T2/T3/T5 never re-derived a claim from the guard's own README, and AC-3.3 (no wording drift across three files) closed clean, with only one benign reordering (F4) caught and fixed.
- **What we'd do differently:** nothing on this branch is committed until `/go-live` — every phase's artifact sat uncommitted through Specify, Plan, Increment, Review and QA. That cost nothing here (a small, single-session feature), but for a longer-running feature it would mean five phases of work with no recovery point if the session were interrupted. Committing incrementally per phase (as `situational-lenses` did) is the safer default.
- **Patterns worth reusing (candidates for `CLAUDE.md`):**
  1. **Re-derive, don't cite, for evidence that lives outside this repo.** Both `review.md` and `qa.md` independently re-fetched `aspark-guard`'s own README (via `gh api` and `curl` respectively) rather than trusting `evidence.md`'s citation of it — the Must-AC condition that named "re-derive" explicitly. Worth generalizing: any AC whose grounding evidence lives in another repo should name *who* re-derives it and how, not just who cites it, since a cited chain of citations is how a stale or fabricated claim survives three gates unnoticed.
  2. **Pin-once, quote-many for any claim repeated across files.** T1's canonical-wording block (long form + short form + literal command, each source-cited) is a reusable shape for the next feature that needs the same fact stated in more than one surface — cheaper to maintain and mechanically checkable for drift (T6's `grep` pass), instead of trusting each prose author to match the others by eye.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time — four of five; the fifth ("no uncommitted changes") is expected-false at this stage of the ceremony, not a failure, per §1.
- [x] Changelog written in user-facing language — no commit hashes, ticket IDs or internal jargon (§2).
- [ ] Release actions executed and verified — **not yet**; prepared only. In `pr` mode: PR not yet open, `claude plugin validate` already green locally, approver (self-review-via-PR) not yet requested, ticket format `none` (nothing to link), rollback path written (§3). Deploy and post-release smoke check correctly N/A.
- [x] Learnings recorded (§4).
- [x] Line budget respected: Ist 118 / Soll ~100 (excluding HTML comments) — over by ~18%, driven by the two full commit-message blocks and the PR draft body the caller asked for verbatim; no waiver requested, flagged here per the rule.
- [ ] Status set to `released`/`handed-off` — **not yet.** Status stays `preparing`. What remains outstanding: (1) the two commits above need to be created (increment, then release-prepare) and F5 re-verified; (2) the user's explicit go to push the branch and open the PR against `main`; (3) once the PR is open and `claude plugin validate .` is confirmed green on that exact commit, this report's status becomes `handed-off` — the real merge and tag happen after that, outside this ceremony's control, owned by the declared approver (`a-lottes`, self-review-via-PR).
