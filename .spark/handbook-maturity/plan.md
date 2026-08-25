# Plan: handbook-maturity

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/handbook-maturity/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-08-24 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). Approved by the user on 2026-08-24; PLAN GATE fully checked. Next: `/increment` — its two in-plan stop rules stand (first overwrite of the tracked docx only after T1 evidence + recorded user go; T3 confirms graph's release number or stops to ask).
- **Summary:** Labels reach the binary docx via a throwaway /tmp editing harness (stdlib Python OOXML surgery, clone-existing-element-shapes, verify-by-re-extraction) — nothing added to the repo, every addition proven against plain-text extraction.
- **Open:** `8 tasks not done` — see §3 Task Breakdown for which
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Architecture Decision

- **Context:** The work object is a tracked binary docx. Constitution §3 forbids adding any script, toolchain or build step to the repo (spec A3 fixes this); no agent can edit a binary file directly; NFR-4 requires every addition to survive `textutil` plain-text extraction (rules out text boxes/images); AC-2.1 requires a real 17-row docx table; review evidence is extraction-based because git cannot line-diff a docx. The mechanism must therefore mutate the OOXML package from outside the repo, verifiably and repeatably across review fix rounds.
- **Decision:** A one-off, throwaway editing harness living entirely in `/tmp` — Python 3 stdlib only (`zipfile` + `xml.etree` over the docx package's `word/document.xml`), never committed, never installed. The harness inserts new elements by **cloning the XML shape of existing siblings** (chapter-label paragraphs cloned from an existing body paragraph with direct bold run formatting; the overview table cloned from ch. 3's existing table including its `tblPr`), always operating on a copy, always verified by `textutil` re-extraction before the result touches the working-tree file; git is the rollback path. All content (label strings, anchors, table rows, title-page lines) comes from an explicit edit manifest recorded in `.spark/handbook-maturity/evidence.md`.
- **Alternatives considered:**

  | Alternative | Why rejected |
  |---|---|
  | Manual editing by the user in Word/Pages following a written edit script | ~50 discrete edits into a binary file, repeated at every review fix round; high miss-risk; not executable inside the agent-driven Act phase. Retained as the **declared fallback** if T1 disproves harness fidelity — decided by evidence, not preference |
  | One-off `python-docx` script | Needs `pip install` on the user's machine (constitution §6: nothing installed unasked) or lucky pre-installation; the stdlib route needs neither |
  | LibreOffice headless / AppleScript Word automation | External application whose presence is unverified and whose scripting is fragile; heavyweight for paragraph/table inserts |
  | Pandoc Markdown↔docx round-trip | Destroys figures and layout; is effectively the Markdown-source-of-truth conversion deliberately cut to spec §6 (C5) |
  | Committed generator/validator for the docx | Forbidden outright by A3 / NFR-3 |

- **Consequences:** Easier — edits become repeatable and auditable; fix rounds re-apply a manifest instead of re-doing ~50 manual edits; the old extraction serves as a byte-baseline so review can prove *nothing changed except the manifest*. Harder — hand-built OOXML carries a real corruption risk (mitigated: copy-first, clone-shapes, verify-after-every-step, user opens the file before release); inserted labels carry plain bold formatting rather than bespoke design; the harness is ephemeral, so a future handbook revision rebuilds it from this plan's description.

## 2. Affected Components

- `docs/aSPARK_Enterprise_Architecture_Handbook.docx` — the only content object; binary, tracked. Internal touch points: title page (extraction l. 5), position before ch. 1 (l. 13), ch. 3 Maturity column (l. 130–153), ch. 8 `Status.` (l. 582, kept), ch. 11 `Status.` (l. 808, kept), 17 chapter headings, ~19 marker anchors per spec §4 inventory.
- `.spark/handbook-maturity/evidence.md` — created by `/increment`: edit manifest, spot-check record, extraction audits, dry run.
- `ROADMAP.md` — issue #18 entry updated at bookkeeping time (NFR-3 permits docs/ + ROADMAP bookkeeping only; constitution `/charter` amendment is post-release, out of scope).
- **Out-of-repo tooling (justified):** macOS stock `textutil` (extraction channel, proven this session) and stdlib Python 3 in `/tmp`. No repo dependency, no install, nothing committed — satisfies A3/NFR-3 while making the edit repeatable.
- **Out (spec §6):** no prose rewrite beyond the whitelisted additions (enforced by the T7 delta audit); no website sync (C9 — immediate follow-up feature); no Markdown conversion.
- **Graph scoping note (result recorded):** this repo is Markdown+JSON+docs only; the graph indexes source-code extensions only. The requested `aspark-graph query impact docs/aSPARK_Enterprise_Architecture_Handbook.docx ROADMAP.md .spark/handbook-maturity/evidence.md --repo .` returned exit 0, `found: true`, empty `files`/`affected_stories`/`affected_acs`, all three paths in `unknown_files` — meaning *these paths are not indexed*, not *nothing depends on them*. Blast radius was therefore scoped by hand from the extraction map above; that hand scoping stands as the authoritative Affected Components.

## 3. Task Breakdown

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Walking skeleton: build the /tmp stdlib harness; clone an existing paragraph's XML shape; insert one label line under the ch. 9 heading on a **copy** of the docx; re-extract with `textutil` and assert the label survived and the package is intact; tracked file untouched | US-1 | AC-1.1, NFR-4 | – | `done` (2026-08-24) | `evidence.md` records the exact commands, the extracted proof line, and `git status` showing the docx unmodified — files: .spark/handbook-maturity/evidence.md |
| T2 | Edit manifest: take a fresh `textutil` extraction of the current tracked docx as the byte baseline (hash recorded); list every insertion point with its verbatim anchor quote — 17 chapter headings, legend + overview-table position before ch. 1, the 7 ch. 3 Maturity cells, every spec §4 target-state item, the kept ch. 8/ch. 11 `Status.` paragraphs, title-page lines; verify each Planned chapter already names its roadmap stage/product in prose (AC-1.4), else raise it as a finding | US-1, US-2, US-3 | AC-1.4, AC-1.5 | T1 | `done` (2026-08-24; one AC-1.4 miss → deviation D1) | Manifest complete in `evidence.md`; count reconciles against spec §4's inventory — every item maps to exactly one anchor, no anchor without an item — files: .spark/handbook-maturity/evidence.md |
| T3 | Baseline spot-check (gates any version bump): walk the §4 marker inventory as checklist against what current Core and graph releases actually ship — Core release notes (v0.7.0, tagged 2026-08-24) and graph release notes (**current graph release number is unverified at plan time; confirm it here or STOP and ask the user**); each contradiction becomes a manifest marker addition or a filed finding, never a prose edit; output the confirmed `product:version` pairs | US-3 | AC-3.3, NFR-2 | T2 | `done` (2026-08-24; graph v0.7.0 confirmed from its GitHub releases — no STOP needed) | `evidence.md` holds a per-item spot-check table and the two confirmed pairs — or a recorded STOP with the question to the user; no pair asserted without a corresponding release — files: .spark/handbook-maturity/evidence.md |
| T4 | Apply front matter + chapter labels: insert the 17 `Delivery stage: <Shipped/Partial/ Planned>` label lines (cloned paragraphs, bold runs), the legend defining the three values exactly once, and the overview table (header + exactly 17 rows: chapter, stage, pointer to that chapter's markers) cloned from ch. 3's table XML, positioned before ch. 1 | US-1, US-2 | AC-1.1, AC-1.2, AC-2.1 | T1, T2 | `done` (applied 2026-08-24 by interrupted session; re-verified & recorded on resume 2026-08-25) | Re-extraction shows all 17 `Delivery stage:` lines, the legend once, and 17 data rows appearing before `1  Executive Summary`; the package re-opens cleanly — files: docs/aSPARK_Enterprise_Architecture_Handbook.docx |
| T5 | Apply inline markers + ch. 3 relabel: insert a `Status.`-pattern marker at every manifest anchor (including T3 additions) naming the item as outside the shipped baseline; relabel the 7 Maturity cells to the taxonomy (Core Shipped, graph Shipped, policy/insights/ci/memory/Enterprise Planned); assert the kept ch. 8 and ch. 11 `Status.` paragraphs are byte-unchanged | US-1 | AC-1.3, AC-1.5, NFR-1 | T3, T4 | `done` (2026-08-25; two anchor fixes → deviation D2) | Extraction shows every §4 inventory item adjacent to a `Status.` marker; the ch. 3 column contains only `{Shipped, Planned}` and none of the old `Foundation/Platform/Future/Distribution` values — files: docs/aSPARK_Enterprise_Architecture_Handbook.docx |
| T6 | Title page: replace the version line with three separately identifiable statements — the incremented handbook revision (`Version 1.2 · August 2026`), the shipped-baseline pairs from T3 verbatim, and the target-architecture designation for content beyond that baseline | US-3 | AC-3.1, AC-3.3, NFR-2 | T3 | `done` (2026-08-25) | Extraction of page 1 shows all three statements distinctly; the pairs equal T3's confirmed values; no claimed baseline lacks a release — files: docs/aSPARK_Enterprise_Architecture_Handbook.docx |
| T7 | Full audit + dry run: near-diff the revised extraction against T2's baseline — the delta must be exactly the manifest additions, nothing else (prose-freeze proof); walk every AC (AC-1.1–AC-3.2) and NFR-1/NFR-3/NFR-4; run the §1 success-signal dry run — a fresh-context reader receives only the extracted title page + overview table and must answer (a) which products exist today, (b) which chapters are safe as shipped behavior, within 2 minutes, all correct; record the expected sharp result (zero chapters Shipped) | US-1, US-2, US-3 | AC-1.2, AC-2.2, AC-2.3, AC-3.2, NFR-1, NFR-3, NFR-4 | T4, T5, T6 | `done` (2026-08-25; audit exit 0, AC walk + user dry run recorded) | `evidence.md` records the delta audit (whitelist holds), the AC walk, and the dry-run transcript (material shown, answers, elapsed time, verdict) — files: .spark/handbook-maturity/evidence.md |
| T8 | Bookkeeping: update ROADMAP.md issue #18 (labels landed; exception closure via `/charter` noted as post-release follow-up) | US-1 | NFR-3 | T7 | `done` (2026-08-25) | ROADMAP row reflects the shipped state; the branch diff is confined to `docs/` content, ROADMAP, and the `.spark/` trail — files: ROADMAP.md |

## 4. Test Strategy

No automated tests exist or are possible (constitution §4); the bar is documented, extractable verification:

- **Build-time (per task):** every mutating task's DoD is an assertion over a fresh `textutil` extraction — the same channel review will use, so nothing is ever verified by "trust me, Word shows it".
- **Prose freeze:** T7's near-diff against the T2 baseline extraction is the strongest check in the plan: the entire diff against the old document must equal the manifest whitelist. This is how "labelling, never rewriting" (spec §1/§6) is *proven*, not promised.
- **Review (`/peer-review`):** extraction-based by accepted limitation (NFR-4, C5) — reviewer re-extracts independently and checks the delta whitelist, label counts (17/17), single legend, table-vs-chapter agreement (AC-2.2), plus optional screenshots of title page/table.
- **QA gate — proposed ceremony-appropriate override** (following the recorded lean-rounds precedent, `release.md` §1 and its "offer the override before a skip" learning): QA's browser/demo gate is meaningless for a docx. Proposed equivalent: the QA Tester performs its **own** fresh extraction (not the builder's artifact), independently re-walks the AC checklist, and validates the recorded dry run (AC-2.3) — then the box is marked passed on that method; failing that, `N/A / user override` with reason recorded, never a silent skip.
- **`/demo-day` equivalent:** the T7 dry run plus the user opening the revised docx in Word/Pages once before release (visual integrity check the extraction cannot give).
- **Merge-time (NFR-2):** release pre-flight re-confirms the title-page pairs against release-notes history.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| OOXML surgery corrupts the docx | Tracked public document unusable | Harness works on copies, clones existing element shapes only, verifies by re-extraction after every step; git checkout is the rollback; user opens the file before release |
| Inserted elements look foreign or drop styling | Labels/table visibly off-brand | Clone `pPr`/run properties and `tblPr` from existing siblings instead of inventing formatting |
| `textutil` drops content (text boxes/images) | Silent loss of additions (NFR-4 breach) | All additions are body-level paragraphs and a real table; every task's DoD asserts presence in extraction; pre-existing image-only figures (A.5) are untouched |
| Graph's current release number mis-stated on the title page | False baseline claim (NFR-2, honesty violation) | T3 must confirm it from actual release notes or STOP and ask the user; no value is carried from plan time |
| Marker inflation turns labelling into rewriting | Scope breach of §1/§6 | Fixed `Status.` marker template; manifest pins every anchor verbatim; T7's delta whitelist rejects anything else |
| Harness mutates the tracked file without explicit consent | Constitution §6 non-negotiable breach | First overwrite of the working-tree docx happens only after T1's evidence is shown and the user's go is recorded in `evidence.md` |

---

## Deviations

- **D1 (2026-08-24, during T2):** Spec §4's assignment table asserts ch. 13 "names Stages
  3–4"; the actual document does not — no roadmap stage or delivering product is named
  anywhere in ch. 13 (verified against baseline l. 868–916). Small, obvious correction inside
  labelling scope: marker M15 (a `Status.`-clone insertion at ch. 13's intro) names the
  delivering stages/products explicitly, satisfying AC-1.4 for ch. 13 without touching a word
  of existing prose. No architecture, scope or story change. Flagged for `/peer-review` attention.
- **D2 (2026-08-25, during T5):** Two manifest anchor misattributions surfaced when T5's
  range-checked searches ran against the real XML (T5 was written but never executed by the
  interrupted 2026-08-24 session): **M9** was booked under ch. 6, but the sentence "Core
  exposes a CLI and IDE adapters towards developers…" physically lives in §3.2.2 Interfaces,
  ch. 3 (baseline l. 164; sole document-wide occurrence) — marker insertion point corrected
  to ch. 3, directly adjacent to the only place the claim is made. **M12**'s verbatim anchor
  quote crosses an OOXML formatting-run boundary (`Shared-service` sits in its own run), so it
  can never match in XML; the search needle was shortened to `indexing many repositories`
  (unique document-wide, ch. 10 only). Marker texts unchanged in both cases; AC-1.3 is
  satisfied by a marker adjacent to the actual claim. No architecture, scope or story change.
  Flagged for `/peer-review` attention.

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded) *(harness lives outside the repo — §3/A3 honored)*
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task *(AC-1.1–2.3, AC-3.1–3.3; NFR-1–4; NFR-5/6/7 N/A per spec)*
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Status set to `approved` by the user *(explicitly, 2026-08-24)*
