# Release: accessibility-lens

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 1) |
| **Status** | `preparing` — commits landed, PR not yet open |
| **Version** | v0.9.0 (proposed only — `pr` mode) |
| **Date** | 2026-09-15 |

**Handoff**
- **Status:** mirrors the header table above. `preparing` — pre-flight is fresh-verified green and everything reversible/local is drafted below; nothing outward-facing, and no commit, has run yet.
- **Summary:** `accessibility-lens` adds `lenses/accessibility.md`, the 9th lens — characteristic-triggered (`must-be-accessible`), giving Specify/Design/Act/Review/QA each a falsifiable check. Both gates `passed`; minor bump `0.8.1` → `0.9.0` proposed; PR mode, awaiting the user's explicit go to commit, push and open the PR.
- **Open:** `2 outstanding` — (1) the working tree still carries this feature's uncommitted/untracked changes — owner: whoever runs the two commits drafted in §3. (2) NFR-6's dispatch/activation gap (5 sites, `refuted-with-finding`) is routed to a follow-up increment, not fixed here — owner: a future `/increment`.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on the exact uncommitted release content — not copied from `review.md`/`qa.md`.*

- [x] `review.md` status is `passed` — REVIEW GATE checklist read at `.spark/accessibility-lens/review.md:111-117`: no open Blocker/Major (round 1's F1–F3 Major, `fixed r2`, re-verified against source, not the fix summary), all plan deviations documented, line budget 117/150, status `passed`.
- [x] `qa.md` status is `passed` — QA GATE checklist read at `.spark/accessibility-lens/qa.md:86-92`: every Must AC and every QA-owned NFR verified (12/12 AC ✅); NFR-6 `refuted-with-finding` by design, not a bug; no open Blocker/Major; status `passed`. **QA method:** constitution §8 carries a complete declaration (surface `no`, substitute method named — hands-on QA against the installed plugin) — QA ran by that declared method as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID it owns, same as always.
- [x] Full test suite green — N/A, none exists or is possible for prompt material (constitution §4). Substitute bar re-run fresh just now: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning, unrelated to this diff, present on every prior release).
- [x] Build succeeds from a clean checkout — N/A, no build step (constitution §3/§4); `claude plugin validate .` is the equivalent bar and passed, above.
- [ ] No uncommitted changes in the working tree — **currently false, by design at this point in the ceremony.** Re-verified fresh: `git status --porcelain` → `M README.md`, `M lenses/README.md`, `M lenses/seo.md`, `M lenses/ux.md`, `?? lenses/accessibility.md`, `?? .spark/accessibility-lens/`, plus the pre-existing, unrelated `?? .spark/.guard/` (the loop's own session ledger — out of scope for this feature, same treatment `companion-offer`'s and `situational-lenses`' own releases gave it: untracked scratch this diff didn't create and won't commit). `git diff --name-only main -- .` → exactly `README.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md` — matches `review.md`'s and `qa.md`'s recorded diff byte-for-byte; nothing drifted since QA closed. `git diff --name-only main -- skills/ agents/ templates/ .claude-plugin/` → empty, re-confirmed (AC-1.4/NFR-6 fence). Stays unchecked until the commits in §3 land.

**Branch staleness (project `CLAUDE.md` house rule).** `git fetch origin` then `git rev-parse main origin/main` → both `2846739`, identical to `git merge-base HEAD origin/main`. Not stale — nothing landed on `main` since this branch was cut, and `companion-offer`'s own release (PR #46, proposing `v0.8.2`) is still open on its own unmerged branch, confirmed not on `main`.

**Version confirmed.** `.claude-plugin/plugin.json` reads `"version": "0.8.1"` on `main` right now (re-read directly, not assumed) — untouched by this feature's diff.

## 2. Changelog

### Added
- A new **accessibility lens** is available for any project that needs to meet an accessibility standard (WCAG, ADA, EAA, Section 508, etc.), regardless of what kind of project it is — not just websites. Once turned on, it grounds a real, measurable accessibility target at spec time, checks it again during design, during implementation, during code review, and once more with a hands-on keyboard-only pass before ship.
- **Known limitation, disclosed honestly:** turning the lens on today still requires a maintainer to hand-edit two of the loop's own instruction files before its design-review and hands-on-testing checks actually run — that wiring isn't automatic yet for this 9th lens the way it is for the first eight. This is written up openly (see `README.md`'s status table and this feature's own evidence ledger) and queued as follow-up work, not silently shipped as if it already worked end to end.

### Changed
- `seo` and `ux`'s existing "this doubles as the accessibility check" notes now point at the new lens by name instead of a vague phrase.

### Fixed
- Nothing was previously broken — this closes a coverage gap: until now, only a one-time design-stage review touched accessibility, and nothing afterward re-checked it.

## 3. Release Actions

*Prepared, not executed. Outward-facing steps require the user's explicit go, relayed by the invoking session — none has been given yet.*

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only:** `0.8.1` → `0.9.0`, **minor** — a genuinely new optional capability (the 9th lens) triggers constitution §5's stated minor-bump rule, unlike `companion-offer`'s docs-only `0.8.1`→`0.8.2` patch (still open, unmerged). Nothing protected in §3 renamed or removed (NFR-5). No tag — `pr` mode creates the tag at/after merge, outside this ceremony's control. Not yet executed. |
| PR / merge | **Not opened.** Title/body drafted below, target `main`, ready once the user gives the go. No merge — approver is self-review-via-PR (solo maintainer), per constitution §7. |
| Deploy | N/A — no deploy surface; this repo *is* the distributed artifact, consumers pull it via `/plugin install`/marketplace update, not a push from here. |
| Post-release smoke check | N/A — nothing has merged or deployed. This ceremony's local analogue, `claude plugin validate .`, already re-ran fresh above and passed. |

**Exact commit #1 — the increment's changes:**
```
feat: accessibility-lens — add the 9th lens, triggered by must-be-accessible

Adds lenses/accessibility.md, giving Specify, Design, Act, Review and QA
each a falsifiable accessibility check grounded in a traceable NFR,
closing the gap where only the Designer's one-time baseline critique
existed. Registered in lenses/README.md's Available-lenses and
Characteristics tables; seo.md and ux.md's pointer lines now name it by
path (US-3). README.md's lens table and Project Status section updated
in the same diff (constitution §4 docs-in-step; plan Q1 ruling adds this
as a deliberate 5th file beyond AC-1.4's literal four).

No agent or skill file is edited (C6: /increment already reads spec.md's
NFR-n unconditionally) -- but the add-a-file promise this exercises is
not fully whole: two skill files' closed lens lists (look-and-feel,
demo-day) and /charter's own activation vocabulary
(agents/facilitator.md, templates/constitution.md) don't yet know this
lens exists, so its Design and QA checks ship undispatched today and the
characteristic itself isn't offered by /charter yet. Recorded
refuted-with-finding against NFR-6 at five sites and routed to a
follow-up increment, not fixed here (plan Q2; CLAUDE.md's routing
ceremony) -- disclosed in README.md and lenses/README.md, not left
implicit in .spark/ alone.

review.md passed round 2 (round 1: 3 Major + 4 Minor found and fixed;
round 2: all seven re-verified against source, 3 further collateral
Minors found and fixed). qa.md passed round 1, 12/12 AC verified
hands-on; NFR-6's disclosure independently reconfirmed accurate and
current (4th re-verification of the same five sites, no drift).

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
Files: `lenses/accessibility.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md`, `README.md`, `.spark/accessibility-lens/{spec.md,plan.md,evidence.md,review.md,qa.md}`.

**Exact commit #2 — prepare the release (version bump; separate from the increment, mirroring `companion-offer`'s own precedent):**
```
chore: prepare accessibility-lens release, propose v0.9.0 (pr mode, awaiting go)

Bumps .claude-plugin/plugin.json 0.8.1 -> 0.9.0 (minor: a genuinely new
optional capability, the 9th lens, per constitution §5's stated
minor-bump trigger -- unlike companion-offer's docs-only 0.8.1 -> 0.8.2
patch, still open on its own unmerged branch/PR #46 and not yet on
main). review.md (passed, round 2) and qa.md (passed, round 1) both
fresh-verified green at pre-flight; branch confirmed not stale against
origin/main (both at 2846739, matching this branch's own cut point). No
tag, no push, no PR yet -- pr mode, prepared and awaiting the user's
explicit go. See .spark/accessibility-lens/release.md.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
Files: `.claude-plugin/plugin.json`, `.spark/accessibility-lens/release.md`.

**Draft PR (target `main`, ticket format `none` per constitution §7):**
- **Title:** `feat: add the accessibility lens, the 9th situational lens`
- **Body:**
  ```
  ## Summary
  - Adds `lenses/accessibility.md`: a characteristic-triggered lens
    (`must-be-accessible`, structured like `security.md`) that gives
    Specify, Design, Act, Review and QA each a falsifiable accessibility
    check under a traceable NFR -- the first lens to own an Act-phase
    check, at zero new wiring cost (C6).
  - Registers the lens in `lenses/README.md`'s Available-lenses and
    Characteristics tables; `seo.md`/`ux.md`'s existing "doubles as the
    accessibility check" notes now name it by path (US-3).
  - `README.md`'s lens table and Project Status section updated in the
    same diff (Q1: constitution §4's docs-in-step bar outranks AC-1.4's
    literal four-file list).
  - Proposes a minor bump, `0.8.1` -> `0.9.0` (new optional capability,
    constitution §5).

  ## Known limitation (disclosed, not fixed here)
  The add-a-file promise this lens exercises is not fully whole: two
  skill files' closed lens lists (`look-and-feel`, `demo-day`) and
  `/charter`'s own activation vocabulary (`agents/facilitator.md`,
  `templates/constitution.md`) don't yet know `accessibility` exists, so
  its Design and QA checks ship **undispatched today**, and the
  `must-be-accessible` characteristic isn't yet offered by `/charter`'s
  own vocabulary. Recorded `refuted-with-finding` against NFR-6 at five
  sites (`.spark/accessibility-lens/evidence.md`) and routed to a
  follow-up increment -- not repaired in this diff, per this project's
  own `CLAUDE.md` routing convention. `README.md`'s Project Status table
  and `lenses/README.md`'s "Adding a lens" section both carry this
  disclosure for a reader who hits it directly, not just this ledger.

  ## Test plan
  - [x] `review.md` passed, round 2 (`.spark/accessibility-lens/review.md`)
        -- round 1: 3 Major + 4 Minor found and fixed; round 2: all seven
        re-verified against source, 3 further collateral Minors found and
        fixed
  - [x] `qa.md` passed, round 1, 12/12 AC + all QA-owned NFRs verified
        hands-on against the installed plugin
        (`.spark/accessibility-lens/qa.md`); NFR-6's disclosure
        independently reconfirmed accurate, no drift since review round 2
  - [x] `claude plugin validate .` passes locally (re-run at `/go-live`
        pre-flight; one pre-existing, out-of-scope warning)
  - [x] `git diff --name-only main -- skills/ agents/ templates/
        .claude-plugin/` empty -- no agent or skill file touched
  - [ ] Self-review and merge by the declared approver (`a-lottes`)
  ```

**Rollback path.** Purely additive (NFR-5): no protected template structure, slash command, or consumed-contract path is renamed or removed, so a straight revert needs no coordination with the `aspark-graph` consumer. Before merge: close the PR / stop short of merge — `origin/main` stays exactly at `2846739`, unchanged by anything here. After merge: `git revert -m 1 <merge-commit-sha>` on `main` restores `README.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md`, removes `lenses/accessibility.md`, and reverts `.claude-plugin/plugin.json` to `0.8.1` in one commit; then `git push origin :refs/tags/v0.9.0 && git tag -d v0.9.0` if a tag was already cut. Safe because the lens is dormant on every profile that doesn't declare `must-be-accessible` (NFR-4, re-confirmed live on this repo's own profile) — removing it returns every consumer to exactly its prior behavior, not a degraded one.

## 4. Learnings (Keep!)

- **What went well:** the negative case ran twice (T2 before any positive claim, T9 after registration) and NFR-6's `refuted-with-finding` disclosure was independently re-derived from primary source four separate times across the loop (plan, review r1, review r2, QA) with zero drift in either the five `file:line`s or their consequence — the routing ceremony held up under real adversarial pressure, not just a first pass.
- **What we'd do differently:** the plan's own add-a-file scope check (C6) examined only `/increment`, found it clean, and stopped — Review then had to discover, across *two separate rounds*, that `look-and-feel`, `demo-day`, `peer-review`'s parenthetical and even `/charter`'s own activation vocabulary shared the identical closed-enumeration defect. Checking dispatch *and* activation for every phase a new lens's `phases:` frontmatter claims to own — at plan time, not review time — would have caught 4 of 5 sites before the diff ever reached a reviewer.
- **Patterns worth reusing (candidates for `CLAUDE.md`):**
  1. **An add-a-file scope check must examine every ceremony phase the new artifact's frontmatter claims to own, not just the one already wired generically.** This loop's own worked example — see above — is the concrete case to cite.
  2. **A disclosed limitation stays honest only if it's re-verified at every gate it survives, not just written once.** Four independent re-derivations of the same five sites, never trusted from the prior gate's word, is what kept this feature's one known gap from going stale between Plan and QA.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time — four of five; the fifth ("no uncommitted changes") is expected-false at this stage of the ceremony, not a failure, per §1.
- [x] Changelog written in user-facing language — no commit hashes, ticket IDs or internal jargon (§2).
- [ ] Release actions executed and verified — **not yet**; prepared only. In `pr` mode: PR not yet open, `claude plugin validate` already green locally, approver (self-review-via-PR) not yet requested, ticket format `none` (nothing to link), rollback path written (§3). Deploy and post-release smoke check correctly N/A.
- [x] Learnings recorded (§4).
- [x] Line budget respected: Ist 146 / Soll ~100 (excluding HTML comments) — over by ~48%, driven by the two full commit-message blocks and the PR draft body the caller asked for verbatim; no waiver requested, flagged here per the rule.
- [ ] Status set to `released`/`handed-off` — **not yet.** Status stays `preparing`. What remains outstanding: (1) the two commits above need to be created (increment, then release-prepare); (2) the user's explicit go to push the branch and open the PR against `main`; (3) once the PR is open and `claude plugin validate .` is confirmed green on that exact commit, this report's status becomes `handed-off` — the real merge and tag happen after that, outside this ceremony's control, owned by the declared approver (`a-lottes`, self-review-via-PR, constitution §7).
