# Release: handbook-maturity

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`; F1 `fixed r1`, F2 waived/routed), `qa.md` (`passed`; plan §4 override method, E1–E3 user-accepted) |
| **Status** | `preparing` |
| **Version** | v0.7.1 (**confirmed** patch — user go 2026-08-25; committed on `feat/handbook-maturity`; **no tag exists** — tagging happens post-merge, outside this role's control) |
| **Date** | 2026-08-25 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`/`Version`). User go received 2026-08-25 (orchestrator relay): **steps 1–4 executed** — branch carried onto `feat/handbook-maturity`, manifest bumped `0.7.0` → `0.7.1`, exactly the four paths staged, release commit **`a8435fe6969745cead58750e22dbafa01004d845`**, working tree clean after (`git status --porcelain` empty). **Step 5 passed** — user quote: "looked good in Word, push it" (2026-08-25); QA finding E2 adjudicated: overview-table placement acceptable in real rendering. **Step 6 done** — pushed, confirmed live (`* [new branch] feat/handbook-maturity -> feat/handbook-maturity`). **Step 7 denied**: `gh pr create` blocked by the Claude Code auto-mode classifier (quoted reason: "Stage 2 classifier error - blocking based on stage 1 assessment (usually transient — retrying often succeeds)") — a different failure than the two prior releases' standing subagent permission wall, but per standing instruction no retry was attempted; PR creation is handed to the orchestrating session to run with the user watching. **Step 8 stays gated on post-merge**: no PR and no tag exist yet.
- **Summary:** Handbook honesty labelling released-as-prepared as v0.7.1 (patch, confirmed): delivery-stage label on all 17 chapters, overview table up front, 18 inline target-state markers, title page separating the v1.2 revision from the shipped baseline (Core v0.7.0 · graph v0.7.0).
- **Open:** `1 outstanding` — step 5, the open-in-Word visual integrity check (plan §4; adjudicates QA E2). Owner: the user (`a-lottes`). Rulings recorded same day: version **v0.7.1 confirmed**; the NFR-2 residual (title-page pair names judged baseline v0.7.0 while Core's newest release becomes v0.7.1) **accepted by the user** as recorded here — the pair states the AC-3.3 spot-check target and stays true because this diff changes nothing the chapters describe; drift beyond a named baseline is what the scope-designation sentence covers; carried with F2 by the website-sync / handbook-revision follow-up.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch at the next `/go-live`.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE complete; round 1 passed, F1 `fixed r1`, F2 routed/waived, no open findings of any severity.
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE complete; override method recorded in its Input row, not silent; E1–E3 accepted.
- [x] Full test suite green on the release commit — no automated suite exists or is possible (constitution §4). Re-run fresh instead: `claude plugin validate` passed (one pre-existing `autoUpdate` warning; `marketplace.json` untouched by this diff); package re-proven: `testzip()` None, 46 parts in HEAD order, all entries DEFLATE, 26 XML/.rels parts well-formed, exactly `word/document.xml` byte-different from HEAD, `[Content_Types].xml` identical; prose freeze re-proven again: delta 8 removed / 101 added, all manifest layer, fresh extraction SHA `8f2c4e6b…` reproduces the reviewed hash; committed docx = `b46cd684…`, 2,013,907 B, matching evidence/review/QA.
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON + docs only, no build step (constitution §3).
- [x] No uncommitted changes in the working tree — verified fresh after the release commit: `git status --porcelain` empty on `feat/handbook-maturity` at `a8435fe`.
- [x] Diff is exactly the expected paths: `M ROADMAP.md`, `M docs/aSPARK_Enterprise_Architecture_Handbook.docx` (Bin 2012344 → 2013907), `.spark/handbook-maturity/` (six artifacts incl. this report), `M .claude-plugin/plugin.json` (version bump only).
- [x] Title-page pairs true right now: Core `v0.7.0` → `753a793` resolves locally and matches origin's tag; graph `v0.7.0` is the highest remote tag. ROADMAP diff coherent: Shipped row added; #18 entry restated as the `/charter` follow-up; links point at issue #18, not lean-rounds' PR.
- [x] Open-in-Word visual integrity check — **passed 2026-08-25**: user quote "looked good in Word, push it"; booked by plan §4; QA E2 adjudicated — overview-table placement acceptable in real rendering.

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
| Version bump & tag | **Executed (local only).** Confirmed patch `0.7.0` → `0.7.1` inside release commit `a8435fe6969745cead58750e22dbafa01004d845` on `feat/handbook-maturity`. **No tag exists and none is created pre-merge** (`pr` mode; verified: local tags end at `v0.7.0`) — post-merge annotated tag `v0.7.1` on the merge commit stays with the maintainer (step 8). |
| PR / merge | **Push done; PR creation denied.** `git push -u origin feat/handbook-maturity` — confirmed live (new branch, tracking set). `gh pr create` (drafted title/body) denied by the auto-mode classifier — "Stage 2 classifier error … (usually transient)"; unlike both prior releases' stable subagent permission wall, but per standing instruction not retried: runs next from the orchestrating session with the user watching. Declared `pr` mode (constitution §7); approver = self-review-via-PR (`a-lottes`). No CI exists (`.github/` holds templates only), so "CI green" will be N/A by absence at hand-off. |
| Deploy | N/A — no deploy surface (Markdown/JSON plugin, no runtime); in `pr` mode deploy = the merge, which has not happened. |
| Post-release smoke check | N/A until merge. Proposed for after merge: fresh `claude plugin validate` on `main` plus a one-line text-extraction spot-check that the installed handbook carries the labels. |

**Command ledger** — 1–4 done on the 2026-08-25 go; 5 human; 6–8 authorized but gated on 5:

1. ✅ `git switch -c feat/handbook-maturity` — carried the uncommitted feature off the merged `feat/lean-rounds`
2. ✅ Bumped `.claude-plugin/plugin.json` `"version": "0.7.0"` → `"0.7.1"`
3. ✅ `git add ROADMAP.md docs/aSPARK_Enterprise_Architecture_Handbook.docx .spark/handbook-maturity .claude-plugin/plugin.json`
4. ✅ Committed as `a8435fe6969745cead58750e22dbafa01004d845` (verbatim drafted message)
5. ✅ Done 2026-08-25 — user opened the docx in Word: passed ("looked good in Word"); E2 adjudicated acceptable
6. ✅ Done 2026-08-25 — pushed, confirmed live; branch tracking set
7. ⛔ Denied 2026-08-25 — `gh pr create` blocked by the auto-mode classifier (transient-flavored, not the prior releases' standing wall); not retried per standing instruction — **runs from the orchestrating session**, full drafted title/body preserved in the release-preparation conversation record
8. ☐ After merge (maintainer): `git fetch origin && git tag -a v0.7.1 origin/main -m "aSPARK Core v0.7.1 — handbook maturity labels (content-only)" && git push origin v0.7.1`

## 4. Learnings (Keep!)

- **What went well:** Artifacts-as-state carried a killed session — T4–T7 existed as scripts but had never run; the resume reconciliation proved by hash + fresh extraction what the tree actually held before another edit was made. Extraction-based verification made a binary file reviewable at all: the prose freeze was reproduced independently three times (builder, reviewer, QA).
- **What we'd do differently:** The feature started on the previous feature's branch and needed a carry at release — create the feature branch first, always. F1 showed compression belongs on the binary-edit checklist: every integrity check passed while the file quietly grew +48%. Record measured numbers, not adjectives (E1); re-count cited line numbers before publishing them (E3).
- **Patterns worth reusing:** clone-existing-XML-shape + verify-by-re-extraction for any binary-artifact edit; the delta whitelist ("nothing changed but the manifest") as scope proof; mechanical classification rules (the ceiling rule) over judgment calls; offer the QA ceremony-override method — own fresh channel, independent AC walk — as the default on non-UI features; give `gh pr create` a standing narrow permission (denied two releases running).

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [ ] All pre-flight checks passed at release time — one booked human check still open: the open-in-Word visual check (step 5)
- [x] Changelog written in user-facing language — §2
- [ ] Release actions executed and verified — local steps done (`a8435fe`); push/PR/tag gated on step 5; rollback path written below
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 91 / Soll ~100 — **overage explicitly waived by the user, 2026-08-25**, reason verbatim: "verbatim commit message and rollback path are load-bearing; trimming them would remove the audit trail's substance"
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode — currently `preparing`

---

## Rollback path

- **Anchor (nothing published):** `origin/main` untouched at `753a793`; no push, no PR, no tag. The feature lives only in local commits on `feat/handbook-maturity` (`a8435fe` + the report-update commit above it), sitting on top of merged history at `3666787`. Nothing external to unwind.
- **Abandon now:** `git switch feat/lean-rounds && git branch -D feat/handbook-maturity` — back to a clean tree on the previous branch; the dropped commits stay reflog-recoverable (~90 days) if the decision reverses.
- **Pushed / PR open, pre-merge:** `gh pr close <n> && git push origin --delete feat/handbook-maturity`.
- **After merge:** one `git revert -m 1 <merge-sha>` on `main` restores all four paths, including `plugin.json` back to `0.7.0`. Only if tag `v0.7.1` was already pushed: `git push origin :refs/tags/v0.7.1 && git tag -d v0.7.1`, re-tagging only after the revert lands.
