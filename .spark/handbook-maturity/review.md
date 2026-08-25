# Review Report: handbook-maturity

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/handbook-maturity/plan.md` |
| **Status** | `passed` |
| **Date** | 2026-08-25 |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report — including `/increment` in fix-mode, which is not this
     report's owner — updates it in the same edit that closes or re-rules a finding:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). Round 1 passed; scoped re-review of fix round 1 **passed** (2026-08-25) — F1 closed as `fixed r1`. Next ceremony step: QA per plan §4 override method (QA's own fresh extraction + dry-run validation), then `/demo-day` with the open-in-Word visual check.
- **Verdict:** Prose freeze independently proven (round 1, reconfirmed unchanged on the repacked package); F1 fixed by DEFLATE repack — content neutrality re-proven by this office, not taken from the builder: 45/45 non-document parts byte-identical to HEAD, 46 entries in identical order, `word/document.xml` byte-identical to the pre-repack state (surviving `t6-output.docx`), fresh extraction byte-identical to round-1's, delta audit re-run exit 0 on reviewer-only extractions, installed file byte-equal to the asserted candidate; size now 2,013,907 B (+1,563 vs pre-feature HEAD). F2 waived and routed to follow-up by user decision.
- **Open:** `none` — Blockers: none; Majors: none; Minors: none. F1 `fixed r1`; F2 closed as routed/waived.
- **Binding ruling (fulfilled):** the scoped re-review verified ONLY the repack's content-neutrality claim chain plus updated statuses here; no round-1 adjudicated finding was reopened.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Working tree of `feat/lean-rounds` vs HEAD (`3666787`): `docs/aSPARK_Enterprise_Architecture_Handbook.docx` (binary — reviewed by independent `textutil` extraction per plan §4/NFR-4/C5), `ROADMAP.md`, untracked `.spark/handbook-maturity/{spec,plan,evidence}.md`. Nothing committed yet. Builder artifacts under `/tmp/hm-build/` consulted only for comparison; every verdict rests on the reviewer's own extraction (`/tmp/hm-review-extract.txt`) and own delta audit.

Graph tool resolved (runner + `graph.json` present): `staleness` returned `files_checked: 0` — per the tool's own rule this means *nothing indexed*, not *fresh*; consistent with the plan's recorded `unknown_files` result for these exact paths. Scoping was done by hand from the extraction map; no graph answer is cited as evidence.

Not reviewed: the visual rendering of the docx in Word/Pages (deliberately reserved for the pre-release open-in-Word check, plan §4); the AC-2.3 dry run itself (performed with the user as fresh reader — transcript recorded in evidence; QA validates it per plan §4).

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Harness proof recorded; tracked file untouched at that stage (HEAD docx hash still matches evidence's build-start hash today) |
| T2 | ✅ | Manifest complete; anchor count reconciles against spec §4 inventory; AC-1.4 miss found and dispositioned as D1 |
| T3 | ✅ | Per-item spot-check table present; both version pairs independently re-verified by reviewer (graph `v0.7.0` via releases API; Core tag `v0.7.0` → `753a793` via ls-remote) |
| T4 | ✅ | Resume reconciliation section honestly reconstructs the interrupted session; T4 output byte-verified against working tree |
| T5 | ✅ | All 18 markers adjacent to their claims; kept ch.8/ch.11 `Status.` paragraphs byte-identical; D2 anchors verified in real XML (see below) |
| T6 | ✅ | Three separately identifiable statements on page 1; pairs equal T3 values; old mixed line gone |
| T7 | ✅ | Delta audit independently reproduced by reviewer (plain diff AND multiset whitelist): 8 removed / 101 added, all whitelisted; AC walk confirmed; dry-run transcript recorded |
| T8 | ✅ | ROADMAP row truthful (#18 is a real open issue, not a PR; PR #23 confirmed to be lean-rounds'); idiom matches neighboring entries; diff confined per NFR-3 |

**Deviations adjudicated:**

- **D1** (ch. 13 names no deliverer, contra spec §4's assertion): correctly classified. Verified myself — ch. 13 prose contains no Stage/product naming outside the inserted M15 marker, which names Stages 3–4, aSPARK-policy and points at ch. 16. Pure labelling-layer insertion, inside approved scope; stopping for a plan revision would have added process without changing the fix. Accepted.
- **D2** (M9 relocated ch. 6→3; M12 needle shortened): correctly classified, and both claims verified against the real XML — the marker sits directly under the sole "Core exposes a CLI and IDE adapters…" sentence in §3.2.2 Interfaces (extraction l. 227–229); the original M12 needle occurs 0 times contiguously (split across formatting runs) while the shortened needle occurs exactly once document-wide. Accepted.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Minor | `docs/aSPARK_Enterprise_Architecture_Handbook.docx` (root cause `/tmp/hm-build/harness.py:73`) | Harness rewrote all 46 zip parts as `ZIP_STORED` instead of preserving DEFLATE (`writestr` without `compress_type`; its docstring even claims to mirror entry types). Tracked binary grows 2012344 → 2972610 bytes (+48%) for ~50 KB of actual content growth. No integrity impact (part set identical; only `word/document.xml` bytes differ; `[Content_Types].xml` unchanged; `testzip` None; XML well-formed), but it is permanent public-repo weight the plan §5 risk table never anticipated, and evidence.md records hashes without mentioning the jump. Fix: repack deflated before merge, or record acceptance of the size cost — either way the user's go is required (second overwrite of the working-tree docx). | **fixed r1** (scoped re-review 2026-08-25 — all six claim-chain points independently re-executed): container vs HEAD: 46 entries in identical order; 45/45 non-document parts byte-identical; `word/document.xml` byte-identical to the pre-repack state (`t6-output.docx`, its recorded SHA `0f1f84e6…` reproduced); `testzip()` None; all 26 XML/.rels parts well-formed; every entry DEFLATE. Own fresh `textutil` extraction byte-identical to round-1's (SHA `8f2c4e6b…`). Delta audit re-run exit 0 on reviewer-only extractions: 8 removed / 101 added, diff byte-identical to the round-1-reviewed delta. Installed working-tree docx byte-equal to the candidate the script asserted on (SHA `b46cd684…`, 2,013,907 B, net +1,563 vs HEAD). User go for the second overwrite recorded in evidence.md fix-round-1 section. |
| F2 | Nit | `docs/aSPARK_Enterprise_Architecture_Handbook.docx` (extraction l.455 §3.3.2 cell; also l.241, l.902) | Pre-existing prose cites stale product versions ("…planned for a future release; **v0.4.1** supports local mode only"; "since Core v0.4.0"; "Core v0.4.0 wires…") beside the new v0.7.0 title-page baseline. Checked: none contradicts what v0.7.0 actually ships, so no AC-3.3 breach — T3's inventory-driven checklist could not have caught these, and the prose freeze (spec §6) forbids fixing them here. Route to the website-sync follow-up (C9) or mark at the next handbook revision. | **routed** (user decision 2026-08-25): waived for this diff with reason — pre-existing prose protected by the prose freeze; carried by the already-planned website-sync follow-up (spec §6/C9) and flagged for the next handbook revision. No fix in this loop. |
| F3 | Minor | `.spark/handbook-maturity/evidence.md:295` | T7 breakdown read "54 overview-table cells **+ 3 header cells**" — components summed to 104 vs the actual 101 added lines; 54 already includes the header cells. Whitelist conclusion unaffected (independently reproduced). Reworded to "51 overview-table data cells + 3 header cells". | fixed |

## 4. Requirements Traceability

Locations cite the reviewer's own extraction (`textutil` of the working-tree docx).

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | 17 `Delivery stage:` lines each directly under its chapter heading (first at l.72) | ✅ met |
| AC-1.2 | One label per chapter; legend exactly once (l.70); no fourth stage value anywhere | ✅ met |
| AC-1.3 | All 18 markers adjacent to their inventoried claims (l.74 … l.1216), incl. relocated M9 at §3.2.2 | ✅ met |
| AC-1.4 | ch.9 names aSPARK-policy ×3, ch.14 aSPARK-ci, ch.16 Stages ×11; ch.13 via D1/M15 (l.958) | ✅ met |
| AC-1.5 | ch.3 Maturity column = Shipped×2 (Core, graph) + Planned×5; Foundation/Platform/Future/Distribution gone as maturity values | ✅ met |
| AC-2.1 | Overview table l.15–68 (header + exactly 17 rows) before ch.1 heading (l.71) | ✅ met |
| AC-2.2 | Mechanical cross-check parsed from extraction: 17/17 table stages agree with in-chapter labels | ✅ met |
| AC-2.3 | Dry-run transcript in evidence.md (fresh reader = user; both probes correct, zero chapters Shipped) | ✅ met |
| AC-3.1 | Title page l.5–7: revision / shipped baseline / scope designation, three distinct statements | ✅ met |
| AC-3.2 | Legend judges stages against "the shipped baseline named on the title page"; pairs on page 1 | ✅ met |
| AC-3.3 | evidence.md T3 per-item table; pairs re-verified against real releases by reviewer | ✅ met |
| NFR-1 | Only {Shipped, Partial, Planned} as stages; taxonomy defined exactly once (legend) | ✅ met |
| NFR-2 | Pairs = real releases (graph `v0.7.0` latest release; Core tag `753a793`); spot-check gates bump | ✅ met |
| NFR-3 | Diff confined to docs/, ROADMAP.md, `.spark/handbook-maturity/`; zero scripts leaked into repo tree | ✅ met |
| NFR-4 | Labels, legend, full table survive plain-text extraction; dry run recorded; review channel extraction-only throughout | ✅ met |
| NFR-5/6/7 | N/A per spec (static document, no runtime/secrets/surface) | ✅ n/a |

Library lens (active): §1 public surface — no command, template heading, ID pattern or plugin path touched; the consumed contract is unchanged. §2 versioning — handbook revision bumped 1.1→1.2 deliberately (C6); both asserted baselines correspond to real releases; no breaking change to anything a consumer depends on. §4 contract clarity — taxonomy defined once and referenced from every label. Lens §3 N/A per constitution §2.

## 5. What Was Checked

- [x] Correctness: every AC traced from spec to my own fresh extraction; delta audit reproduced twice (plain diff + multiset whitelist)
- [x] Non-functional: NFR-1/2/3/4 verified; library-lens §1/§2/§4 slices applied; NFR-5/6/7 N/A with reason
- [x] Error handling: package integrity — `testzip()` None, `word/document.xml` well-formed, 46 parts, part set and `[Content_Types].xml` byte-identical to HEAD, only `word/document.xml` content differs
- [x] Security: content-only change to an already-public file; no secrets in docx, ROADMAP or `.spark/` trail; ROADMAP links point at real issue #18, not another feature's PR
- [x] Tests: no automated suite possible (constitution §4); the documented-verification bar was re-executed end-to-end by me — every hash in evidence.md reproduced (build-start docx = HEAD docx; baseline extract = HEAD extraction; final extract = my fresh extraction; working-tree docx = T6 output)
- [x] Readability: artifact trail (spec → plan → evidence) reconstructs every edit without archaeology

## 6. Verdict

The core promise of this feature — labelling, never rewriting — is proven, not promised: my own near-diff of a fresh extraction against an independently rebuilt baseline shows exactly 8 removed lines (the v1.1 title line and the 7 old Maturity values) and 101 additions, every one of which maps to the recorded manifest layer; there is not one prose word changed beyond it. All 17 chapters carry correct labels matching the binding assignment (13 Partial, 4 Planned, zero Shipped), the legend appears exactly once, the overview table sits before chapter 1 and agrees with the in-chapter labels 17/17, all 18 markers sit next to the actual claims they name (including the two D2-corrected anchors, which I verified against the raw XML), and the title page separates a real revision identity from two baselines I confirmed exist as releases. Both deviations were genuinely small obvious corrections and are fully documented. Two items remain open, neither blocking: F1 asks for a user decision on the uncompressed-package size (+48%) before merge — a one-line harness parameter fixes it if unwanted — and F2 logs pre-existing stale version citations for the already-planned follow-up work. Passed; next stop is QA per the plan §4 override method (QA's own fresh extraction + dry-run validation), with the visual open-in-Word check at release as planned.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here)
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated *(AC-1.x–3.x traceable in §4; harness stayed in /tmp per A3/§6 — user go for the first overwrite recorded in evidence.md)*
- [x] All plan deviations documented and accepted *(D1, D2 adjudicated in §2)*
- [x] Test suite runs green *(no automated suite exists or is possible — constitution §4; the documented verification bar was independently re-executed, see §5)*
- [x] Status set to `passed`
- [x] Fix round 1 re-reviewed and confirmed (F1 `fixed r1`, 2026-08-25) — no open findings remain
