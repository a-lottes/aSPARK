# Release: handbook-maturity

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`; F1 `fixed r1`, F2 waived/routed), `qa.md` (`passed`; plan §4 override method, E1–E3 user-accepted) |
| **Status** | `preparing` |
| **Version** | v0.7.1 (**proposed only** — `pr` mode, no tag before merge) |
| **Date** | 2026-08-25 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`/`Version`). Both gates green; every check below re-run fresh today on the exact working tree. Nothing published: no branch created, no commit, no tag, no PR — the pending list in §3 awaits the user's go.
- **Summary:** Handbook honesty labelling prepared for release as v0.7.1 (patch, proposed): delivery-stage label on all 17 chapters, overview table up front, 18 inline target-state markers, title page separating the v1.2 revision from the shipped baseline (Core v0.7.0 · graph v0.7.0).
- **Open:** `1 outstanding` — the user's go for the §3 pending list, which includes the open-in-Word visual check booked by plan §4. Owner: the user (`a-lottes`). Noted residual: after this merges, Core's newest release is v0.7.1 while the title-page pair names v0.7.0 — the pair states the *judged baseline* (AC-3.3's spot-check target) and stays true because this diff changes nothing the chapters describe; drift beyond a named baseline is what the scope-designation sentence covers; carried with F2 by the website-sync / handbook-revision follow-up.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch at the next `/go-live`.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE complete; round 1 passed, F1 `fixed r1`, F2 routed/waived, no open findings of any severity.
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE complete; override method recorded in its Input row, not silent; E1–E3 accepted.
- [x] Full test suite green on the release commit — no automated suite exists or is possible (constitution §4). Re-run fresh today instead: `claude plugin validate` passed (one pre-existing `autoUpdate` warning; `marketplace.json` untouched by this diff); package re-proven: `testzip()` None, 46 parts in HEAD order, all entries DEFLATE, 26 XML/.rels parts well-formed, exactly `word/document.xml` byte-different from HEAD, `[Content_Types].xml` identical; prose freeze re-proven again: delta 8 removed / 101 added, all manifest layer, fresh extraction SHA `8f2c4e6b…` reproduces the reviewed hash; working-tree docx = `b46cd684…`, 2,013,907 B, matching evidence/review/QA.
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON + docs only, no build step (constitution §3).
- [ ] No uncommitted changes in the working tree — **open by design**: the whole feature sits uncommitted on `feat/lean-rounds` (previous feature's merged branch). Carry onto `feat/handbook-maturity` + release commit = pending-list steps 1–4; rollback anchor stays HEAD `3666787`.
- [x] Diff is exactly the expected paths: `M ROADMAP.md`, `M docs/aSPARK_Enterprise_Architecture_Handbook.docx` (Bin 2012344 → 2013907), untracked `.spark/handbook-maturity/` (five artifacts + this report); nothing staged.
- [x] Title-page pairs true right now: Core `v0.7.0` → `753a793` resolves locally and matches origin's tag; graph `v0.7.0` is the highest remote tag. ROADMAP diff coherent: Shipped row added; #18 entry restated as the `/charter` follow-up; links point at issue #18, not lean-rounds' PR.
- [ ] Open-in-Word visual integrity check — **pending, human**: booked for release by plan §4 and adjudicates QA E2 (overview table sits close under the bare "Contents" heading); owner: user; pending-list step 5.

## 2. Changelog

### Added
- Every chapter of the architecture handbook now carries a visible delivery-stage label — Shipped, Partial or Planned — so you can tell from the page itself whether what you are reading exists today. The sharp result is stated, not hidden: no chapter qualifies as fully Shipped.
- A maturity overview table before chapter 1 lists all seventeen chapters with their stage and a pointer to where each chapter's target-state claims are marked.
- Every claim describing unbuilt capability now has an inline marker beside it naming it as target state, instead of sitting indistinguishable amid shipped behavior.

### Changed
- The title page separates three things that shared one misleading line before: the handbook's own revision (Version 1.2 · August 2026), the product versions its claims were verified against (Core v0.7.0 · graph v0.7.0), and a statement that everything beyond those versions is target architecture.
- The product-family overview now distinguishes the two products that actually exist from the five it describes but that are not built — previously all seven wore the same maturity label.
- The roadmap marks the labelling work shipped and restates what remains: closing the project charter's honesty exception, now that the labels exist.

### Fixed
- A reader could previously not tell ambition from delivery anywhere on the document's surface — two buried admissions across sixteen chapters of platform description. The split is now legible from the front matter alone in under two minutes.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only.** Patch `0.7.0` → `0.7.1`: adds no optional capability, touches no protected structure (constitution §5) — a content-only increment riding in the plugin artifact. The bump lands in the release commit (lean-rounds precedent, `b0d0761`); **no tag exists or is created** — the post-merge annotated tag `v0.7.1` on the merge commit is proposed for the maintainer (step 8). |
| PR / merge | **Not started — awaiting the user's go.** Declared `pr` mode (constitution §7); approver = self-review-via-PR (`a-lottes`). No branch, commit, push or PR exists yet. No CI exists (`.github/` holds templates only), so "CI green" will be N/A by absence at hand-off, as in lean-rounds. Warning from precedent: `gh pr create` was permission-denied at subagent level in both prior releases — if denied again, run from the orchestrating session. |
| Deploy | N/A — no deploy surface (Markdown/JSON plugin, no runtime); in `pr` mode deploy = the merge, which has not happened. |
| Post-release smoke check | N/A until merge. Proposed for after merge: fresh `claude plugin validate` on `main` plus a one-line text-extraction spot-check that the installed handbook carries the labels. |

**Pending list** — steps 1–4 are local and reversible; 5 is human; 6–8 are outward-facing and wait for the explicit go:

1. `git switch -c feat/handbook-maturity` — uncommitted changes travel along; undo: `git switch feat/lean-rounds && git branch -D feat/handbook-maturity`
2. Bump `.claude-plugin/plugin.json` `"version": "0.7.0"` → `"0.7.1"`
3. `git add ROADMAP.md docs/aSPARK_Enterprise_Architecture_Handbook.docx .spark/handbook-maturity .claude-plugin/plugin.json`
4. Commit (message below)
5. User opens the revised docx in Word/Pages once — the visual integrity check (plan §4; adjudicates QA E2)
6. `git push -u origin feat/handbook-maturity`
7. `gh pr create --base main --head feat/handbook-maturity --title "docs: label handbook ambition vs delivery per chapter (v0.7.1, proposed)" --body "<§2 changelog; Gates: review passed (F1 fixed r1, F2 waived/routed), QA passed via plan §4 override, E1–E3 accepted; Version 0.7.1 proposed only, no tag; Approval: self-review-via-PR (a-lottes, constitution §7); Test plan: claude plugin validate passed, dogfood evidence in evidence.md>"`
8. After merge (maintainer): `git fetch origin && git tag -a v0.7.1 origin/main -m "aSPARK Core v0.7.1 — handbook maturity labels (content-only)" && git push origin v0.7.1`

Step 4 commit message:

```
docs: label handbook ambition vs delivery per chapter (v0.7.1, proposed)

Every chapter of docs/aSPARK_Enterprise_Architecture_Handbook.docx carries a
visible Delivery stage label (Shipped/Partial/Planned, mechanical ceiling rule);
an overview table before chapter 1 splits ambition from delivery; 18 inline
Status. markers name each target-state claim; the title page separates the v1.2
revision from the shipped baseline (Core v0.7.0 · graph v0.7.0), spot-checked
against both real releases (AC-3.3). Prose freeze proven independently three
times: delta vs baseline is exactly 8 removed / 101 added, all manifest layer.
Package healthy: 46 parts in HEAD order, all DEFLATE (F1 repack), only
word/document.xml differs from HEAD, net +1,563 bytes. ROADMAP #18 moves to
Shipped, remainder restated as the /charter follow-up. Manifest bumps to 0.7.1
(proposed): content-only, no capability or contract change.

Gates: review passed (round 1 + scoped fix re-review; F1 fixed, F2 waived/routed);
QA passed via the plan §4 override method; E1–E3 user-accepted.
```

## 4. Learnings (Keep!)

- **What went well:** Artifacts-as-state carried a killed session — T4–T7 existed as scripts but had never run; the resume reconciliation proved by hash + fresh extraction what the tree actually held before another edit was made. Extraction-based verification made a binary file reviewable at all: the prose freeze was reproduced independently three times (builder, reviewer, QA).
- **What we'd do differently:** The feature started on the previous feature's branch and needed a carry at release — create the feature branch first, always. F1 showed compression belongs on the binary-edit checklist: every integrity check passed while the file quietly grew +48%. Record measured numbers, not adjectives (E1); re-count cited line numbers before publishing them (E3).
- **Patterns worth reusing:** clone-existing-XML-shape + verify-by-re-extraction for any binary-artifact edit; the delta whitelist ("nothing changed but the manifest") as scope proof; mechanical classification rules (the ceiling rule) over judgment calls; offer the QA ceremony-override method — own fresh channel, independent AC walk — as the default on non-UI features; give `gh pr create` a standing narrow permission (denied two releases running).

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [ ] All pre-flight checks passed at release time — two boxes intentionally open: the release commit does not exist yet; the visual check is a booked human step
- [ ] Changelog written in user-facing language — written (§2); closes at publish
- [ ] Release actions executed and verified — pending the go; rollback path written below
- [x] Learnings recorded — §4
- [ ] Line budget respected: Ist 113 / Soll ~100 (excluding HTML comments — this file contains none) — **13 lines over**, recorded with reason per the template's rule: the verbatim commit message block and the five-step rollback path are load-bearing for the pending go, and trimming them into summaries would move exactness out of the artifact; a trim or waiver is the user's call at the go
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode — currently `preparing`

---

## Rollback path

- **Anchor (today, nothing published):** HEAD `3666787` on `feat/lean-rounds`; remote untouched; no commits, no tag, no PR. Working tree holds exactly this feature's edits over that anchor. Aborting costs nothing external.
- **Abandon outright:** `git checkout -- ROADMAP.md docs/aSPARK_Enterprise_Architecture_Handbook.docx` restores both files; delete `.spark/handbook-maturity/` only if the feature is truly dead — the artifacts are the only copy of the trail.
- **If steps 1–4 ran:** `git switch feat/lean-rounds && git branch -D feat/handbook-maturity` — back to the anchor, edits travel along, no history rewritten.
- **Pushed / PR open, pre-merge:** `gh pr close <n> && git push origin --delete feat/handbook-maturity`.
- **After merge:** one `git revert -m 1 <merge-sha>` on `main` restores all four paths, including `plugin.json` back to `0.7.0`. Only if tag `v0.7.1` was already pushed: `git push origin :refs/tags/v0.7.1 && git tag -d v0.7.1`, re-tagging only after the revert lands.
