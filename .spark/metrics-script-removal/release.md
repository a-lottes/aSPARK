# Release: metrics-script-removal

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3), `qa.md` (`passed`, round 1) |
| **Status** | `handed-off` |
| **Version** | v0.8.1 — **applied**, `.claude-plugin/plugin.json` bumped at `fa2cf36`; `pr` mode, tag (if any) happens at/after merge, outside this ceremony's control |
| **Ticket** | `none` — no tracker for this project (constitution §7) |
| **Date** | 2026-09-11 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`). **Post-merge, recorded 2026-09-14:** the prepared sequence in §3 was carried out after this report was last written — `fa2cf36` (version bump + ROADMAP move) landed on `feat/metrics-script-removal`, the branch was pushed, [PR #42](https://github.com/a-lottes/aSPARK/pull/42) was opened and **merged into `main`** at `10f6299` (2026-09-12T17:04:20Z, merge commit, per the rollback path's own requirement). This status update was made at a later `/spark` resume that found the artifact stale against the actual GitHub state — see the note at the bottom of §3.
- **Summary:** The repo stops shipping an executable: `scripts/spark-metrics.py` is deleted and the published figures are re-grounded on four printed `python3` commands over the committed reports, so every number stays checkable by a stranger — and is never refreshable from here again.
- **Open:** `none` — the publish go was given and executed (see above). All three prior rulings (AC-1.3's gap, QA `B1`, QA `B2`) **accepted by the user, 2026-09-12**; see §3.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — round 3; REVIEW GATE fully checked, F1–F20 all closed (F20 by the user's explicit ratification of C8–C10, 2026-09-11)
- [x] `qa.md` status is `passed` — verified by this project's standing QA method, declared once at `/charter` in constitution §8: hands-on QA against the installed plugin, where a performed step is a real observed command output and reading a file is never one. That is how QA is performed on this project, not a per-feature substitution; `qa.md` records every `AC-`/`NFR-` ID as always. Its first gate box is open by design: **AC-1.3 `not-verified-live`** (§3, awaiting the user's ruling)
- [x] Full test suite green on the release commit — none exists and none is possible for prompt material (§4); the declared substitute, re-run by me at `6295631` just now: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning on a file this diff does not touch), plus all four command blocks extracted from `docs/metrics.md` and run: exit 0, stdout byte-identical to the output printed beneath each
- [x] Build succeeds from a clean checkout — no build step exists; the equivalent was performed fresh: `6295631` cloned into the scratchpad, `claude plugin validate` passes in the clone, `find -name '*.py'` → nothing, `find -type f -perm -u+x` → nothing, 109 tracked files. The four printed commands were run **from the clone**, not from the working copy
- [x] No uncommitted changes in the working tree — `git status --porcelain` empty before and after this pass; `git merge-base HEAD origin/main` = `origin/main` (`8e7b078`), 23 commits ahead, no rebase owed
- [x] Contract surface untouched — `git diff --name-status origin/main...HEAD` has no path under `skills/ agents/ lenses/ templates/ tools/ .claude-plugin/`; no subject on the branch carries a `!` marker
- [x] Recovery path live — `git show a2c0541:scripts/spark-metrics.py | head -1` → `#!/usr/bin/env python3`, and `a2c0541` is an ancestor of `origin/main`

## 2. Changelog

### Added
- `docs/metrics.md` now prints four `python3` commands plus the four rules for combining results across machines — everything that produced every published figure. With only a clone of this repository you can recount all of them yourself and compare against the published numbers.
- README's project status carries a dated snapshot block: the numeric table is still there, labelled as evidence taken on a date and not updated since.

### Changed
- Installing aSPARK no longer puts any executable file in your plugin cache. The 32 KB Python counter and the whole `scripts/` directory are gone; what you receive is Markdown and JSON and nothing else.
- The dogfooding headline no longer leads with a count that goes stale. It now says what the committed reports contain and that anyone can recount them — a claim that stays true as time passes.
- The reports directory describes itself honestly: a closed, dated snapshot, with the "contribute your own report" workflow removed, because nothing here can produce another report.
- The project's own constitution matches the repository again — four edits close the standing exception for tracked executable code that was opened earlier the same day.

### Removed — what you lose, with nothing back
- **The figures can never be refreshed from inside this repository again.** They are permanently checkable and permanently frozen at their snapshot date; producing a newer one would need a tool that no longer lives here.
- **The "count your own projects" invitation is gone, with no replacement.** There is no external home for that tool today, so pointing you anywhere would be a false promise rather than a redirect.

### Known gap
- One acceptance criterion was never performed in this cycle: that the *installed* plugin, refreshed from this branch, contains no Python file. The repository-side evidence holds (no tracked `.py`, a clean clone with zero executables), but the install refresh itself was never run — see §3.

## 3. Release Actions

*Prepared, awaiting go. Nothing in this table has been executed.*

| Action | Result |
|---|---|
| Version bump & tag | **Applied: `0.8.0` → `0.8.1`** (patch) at `fa2cf36`. No capability is added and no consumed contract changes — `AC-1.4`'s zero-hit negative case was re-run at all three review rounds, so the deleted file was never part of the public surface; removing a non-contract file is therefore a patch, never major, and "minor" would overstate it (constitution §5, spec NFR-2). In `pr` mode no tag was created before merge; whether a tag was cut at/after merge is outside this ceremony's visibility — not re-checked as part of this stale-artifact correction |
| PR / merge | **Merged.** [PR #42](https://github.com/a-lottes/aSPARK/pull/42), merge commit `10f6299`, 2026-09-12 |
| Deploy | N/A — handed-off, no deploy |
| Post-release smoke check | Not performed at the time by this ceremony (the executing session did not return through `/go-live` to close this report). Superseded: `main` has since had two further features merged on top (`situational-lenses` PR #43, `companion-offer` PR #46), each starting its own pre-flight from `main` and passing `claude plugin validate` — which is itself live evidence the merged state was healthy |

**Post-merge note (2026-09-14, added at a later `/spark` resume):** every command below was in fact run, in this order, in a session this report was never updated by. Left verbatim as the historical record of what was planned and then executed — not rewritten into past tense line by line.

**Commands, as planned and (per the note above) executed:**

```bash
# local, reversible — still pending, this pass wrote only release.md
#   1) bump .claude-plugin/plugin.json to 0.8.1; move ROADMAP's entry from ## Next to ## Shipped
#   2) git commit -m "chore(release): v0.8.1 — remove the metrics counter, publish the method"
git push -u origin feat/metrics-script-removal                      # outward
gh pr create --base main --head feat/metrics-script-removal \
  --title "feat: remove the metrics counter and publish the method instead" --body "<drafted below>"
gh pr edit <n> --add-reviewer a-lottes    # approver request; see note
gh pr merge <n> --merge                   # MERGE COMMIT — never --squash, never --rebase
```

**The merge commit is load-bearing, not a style preference.** A squash would collapse this branch's 23 commits into one new SHA and orphan every commit this feature made — including `62b4318`, which `.spark/constitution.md` §8 pins its file inventory to, and `e8eb42c`, which carries the pre-deletion negative case. This feature has already paid for that failure mode once: round 1 fix-mode reworded a commit, the SHA moved, the constitution's pin went dead, and round 2 had to catch and repair it (F11). Use `--merge`.

**Establishing the `handed-off` checkpoint (constitution §7: PR open, `claude plugin validate` passing locally, approver requested).** `validate` is established by my own read-only run above. PR-open will be established the same way — I open it, I read it back. **Approver-requested cannot be**: GitHub does not accept a self-review request, and the declared approver is the sole maintainer. That fact will be recorded as explicit, visibly-labelled **self-attestation relayed by the caller**, never as a silent assumption.

**Rollback path.** *Before merge:* nothing is published — `gh pr close <n>` and `git push origin --delete feat/metrics-script-removal`; `main` is untouched. *After merge:* `git revert -m 1 <merge-sha>` restores the script and every document in one commit, which is only possible because the merge is a merge commit. Independently of any of that, the script's bytes survive at `git show a2c0541:scripts/spark-metrics.py` — verified live today, and `a2c0541` is already an ancestor of `origin/main`, so it cannot be orphaned by this PR however it lands.

**Three rulings only the user can give — the go is blocked on these, not on me:**

| # | What needs ruling | My position | **User's ruling, 2026-09-12** |
|---|---|---|---|
| AC-1.3 | **The one Must AC never verified live in this loop.** Cause is environmental, not a decision and not a work avoided: the user *gave* their go for the install refresh, and this session's own permission classifier then denied `claude plugin marketplace update aspark` before step 2 of the prepared sequence. QA correctly refused both fallbacks — reading the install directory and reasoning about it (invalid under §8) and banking the cache's pre-existing zero `.py` files (a tautology before the recorded commit moves, `evidence.md` Entry 9). **What closes it:** a session whose `Bash` permissions allow `claude plugin …`, re-running Entry 9's sequence steps 2–5. I did not re-attempt it — I have no more standing to write into `~/.claude` unasked than `/increment` or `/demo-day` had | Accept as an honest gap: the plan and `evidence.md` R1 both anticipated exactly this, and the repository-side claim rests on two things verified live (`git ls-files '*.py'` empty, a clean clone with zero executables). **Not** a reason to send the increment back through the loop — but accepting it is the user's call, not mine | **Accepted as an honest gap.** Release proceeds; AC-1.3 stays `not-verified-live`, named for whoever next holds the right `Bash` permissions |
| `B1` | QA Minor: `AC-2.4`/`AC-2.5`'s *Given* clauses still cite pre-rebase figures, though both ACs pass via their own "or corrected and recorded" branch regardless of the stale premise. Artifact wording, no verdict turns on it | Accept, or send back for a spec-wording pass. Either is defensible; I am not treating it as accepted merely because it is Minor | **Accepted as recorded.** No further spec edit |
| `B2` | QA Minor/informational: the ignored `docs/…Handbook.docx.bak` is confirmed present in the **local** install cache. Spec A9 already scopes this as a dev-surface leak; consumer reach via a real GitHub marketplace install is unverified and probably nil, and spec §6 routes it to a follow-up | Accept as informational and out of scope here | **Accepted as recorded.** `.bak` removal and the GitHub-install pre-flight remain named follow-ups, not this release's |

## 4. Learnings (Keep!)

- **What went well:** The feature's central claim survived being performed by a stranger — QA cloned the branch fresh and reproduced every published figure from the printed method alone, supplying nothing. Verify-before-delete held: the negative case (`AC-1.4`) was recorded two commits *before* the deletion, so "not breaking" was evidence, not a hope. And the refutation habit did its job three times (`AC-1.2`, `AC-4.1`, `AC-1.3`) — each recorded as refuted or unperformed with a reason, none ground into a false pass.
- **What we'd do differently:** The version decision was correctly deferred to this gate (D3), but three rounds of review went by with the bump unasserted anywhere — worth naming the deferral in the plan's own handoff next time, so nobody reads `0.8.0` on a release branch as an oversight. And `C8` edited an approved spec's only measurable NFR clause in fix-mode and asked afterwards: that ratification should have been sought before the edit, which is what cost F20 a whole round.
- **Patterns worth reusing** — two process patterns, offered for the user's decision on whether either earns a `CLAUDE.md` entry. I have not edited that file:
  1. **Branch staleness has a mid-build case the existing entry doesn't name.** `CLAUDE.md` already tells us to check staleness *before* committing a new feature's work or at `/go-live`'s pre-flight. This feature hit it differently: the branch went stale **during** `/increment`, when PR #40 landed a third machine report while the script-removal work was in flight, which falsified every published figure on the branch at once (F1, Blocker). A narrow addition — re-check the merge-base when a ceremony *ends*, not only when one begins — would cover it. Your call whether that is worth a line.
  2. **Fixing a review finding can create the next round's finding — and it converged.** Round 1's fixes (a rebase, one commit reword) orphaned a cited SHA and broke date literals that round 2 had to repair; round 2's fixes (the re-pin, the four-commands sweep) left two more hardcoded ACs and three un-struck historical entries that round 3 had to repair. The interesting part is the shape: each round's collateral was smaller than the last and round 3 produced none, so fix-mode drift on this project is **self-correcting, three rounds to exhaustion** — not a process failure, but a reason to budget a re-review round after any multi-finding fix-mode pass rather than expecting one to close it. The feature's own staleness observation is already in `CLAUDE.md` and is deliberately **not** re-added.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time — §1, every check re-run by me at `6295631`; nothing cited from `review.md` or `qa.md`
- [x] Changelog written in user-facing language — §2, including what a consumer loses and the one gap, with no commit hashes, IDs or internal jargon
- [x] Release actions executed and verified — **executed, confirmed 2026-09-14 at a later `/spark` resume.** `pr` mode checkpoint established: version bumped (`fa2cf36`), PR #42 opened and **merged** (`10f6299`, 2026-09-12). `claude plugin validate` passed locally at prepare-time (§1); no fresh post-merge smoke check was run by this ceremony at the time (§3 note), but two later features have since built and validated cleanly on top of this merge. Deploy N/A — handed-off, no deploy
- [x] Learnings recorded — §4, with two process patterns routed to the user for a `CLAUDE.md` decision rather than written there by me
- [x] Line budget respected: Ist 106 / Soll ~100 (excluding HTML comments; this file contains none) — counted with `wc -l`, not estimated. The 6-line overage is recorded here with its reason: §3 carries a ruling table the template does not budget for, because three decisions belong to the user and naming them is the point of this pass
- [x] Status set to `released`, or `handed-off` in declared `pr` mode — **`handed-off`**, corrected 2026-09-14. The user gave the publish go and all three §3 rulings (2026-09-12); the declared approver (`a-lottes`, self-review via PR) reviewed and merged PR #42 (`10f6299`). This report was left at `preparing` after that happened and is corrected here, at a later `/spark` resume that found the mismatch — see the Handoff note above
