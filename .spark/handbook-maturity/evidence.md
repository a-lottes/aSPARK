# Evidence: handbook-maturity

Build-phase evidence per plan §4 / spec NFR-4. One section per task, appended in
execution order; each records commands actually run and their actual output.

## Baseline

- Working-tree docx SHA-256 at build start:
  `73b1f4468631eabcfdef2f38101a59d3087e956126f57be7532eaab8a20289a1`
  (`shasum -a 256 docs/aSPARK_Enterprise_Architecture_Handbook.docx`, 2026-08-24)
- Plain-text extraction baseline for the delta audit (T7): `/tmp/hm-build/baseline-extract.txt`
  (see T2).

## T1 — Walking skeleton: one inserted label survives extraction on a copy

Harness: `/tmp/hm-build/harness.py` (stdlib only — `re`, `zipfile`, `xml.etree` for a
well-formedness assert; never committed; throwaway per plan §1). New fragments are cloned
from existing element shapes: the label paragraph clones the document's own `Status.`
paragraph shape (`<w:pPr><w:spacing w:after="160" w:line="276"/></w:pPr>`, bold lead run +
body runs, Calibri sz 22), discovered by inspecting the ch. 8 `Status.` paragraph in
`word/document.xml`.

Commands run:

```
cp docs/aSPARK_Enterprise_Architecture_Handbook.docx /tmp/hm-build/work-copy.docx
cd /tmp/hm-build && python3 harness.py          # operates ONLY on work-copy.docx
```

Output:

```
T1 OK: inserted 460 bytes; /tmp/hm-build/t1-output.docx
```

Extraction proof (`textutil -convert txt -stdout t1-output.docx`):

```
596:9  Policy-as-Code
597-Delivery stage: Planned
```

Integrity checks passed inside the harness: `xml.etree` parse of the modified
`word/document.xml` succeeded (well-formed), `zipfile.testzip()` returned None, output
length equals input + exactly the inserted fragment.

Tracked file untouched:

```
$ git status --short docs/
(empty)
```

**T1 DoD: met.** Label survives the `textutil` round-trip in the correct position;
package intact; working-tree docx unmodified.

## T2 — Edit manifest

Baseline extraction: `/tmp/hm-build/baseline-extract.txt`, 1232 lines,
SHA-256 `1190292727a60806400199e42ce233d550ead078152c66cb6a0c857b1efdb962`.
Line numbers below refer to it. Every insertion maps to exactly one verbatim anchor;
harness searches are range-checked inside the owning chapter so duplicate strings
elsewhere cannot hijack an anchor.

### Front matter (before ch. 1 heading, anchor `>1  Executive Summary<`)
- **F1** legend paragraph defining `Shipped / Partial / Planned` (exactly once, document-wide)
- **F2** overview table cloned from ch. 3's `<w:tbl>` shape incl. `tblPr`; header + exactly 17 rows (chapter, stage, marker pointer)

### Chapter labels (bold lead `Delivery stage:` + value), inserted after each heading
L1–L17 at anchors `>1  Executive Summary<` … `>17  Appendix<`
(baseline l. 13, 67, 126, 206, 340, 389, 474, 523, 596, 670, 753, 826, 868, 917, 972, 1029, 1070).
Values per spec §4 binding table: 1P 2P 3P 4P 5P 6P 7P 8P **9 Planned** 10P 11P 12P
**13 Planned 14 Planned** 15P **16 Planned** 17P  (P = Partial; zero Shipped).

### Inline target-state markers (`Status.` clone), 18 insertions
| ID | Ch | Verbatim anchor (baseline) | Marker names as outside shipped baseline |
|---|---|---|---|
| M1 | 1 | "standardizes how organizations specify, plan, build" | seven-product platform claims — only Core + graph exist today |
| M2 | 2 | "addresses each structural problem with a dedicated product" | dedicated-product answers for policy/insights/ci |
| M3 | 3 | "Memory extends the platform's time horizon." (§3.7 body) | aSPARK-memory future/persistent memory |
| M4 | 3 | "3.8  aSPARK Enterprise" heading block | packaged supported distribution not a shipping product |
| M5 | 4 | "gate id, phase, verdict, timestamp" (evidence entity) | gates.yaml evidence shape — today `.spark/<feature>/evidence.md` |
| M6 | 4 | "ADR-xxx" (decision entity) | ADR entity arrives with aSPARK-memory |
| M7 | 5 | "P7 — Versioned policy packs" | P3/P6/P7 consequences awaiting aSPARK-policy |
| M8 | 6 | "aSPARK-memory (future)" within §6.2 container list (range-checked) | policy/insights/ci/memory containers not built |
| M9 | 6 | "Core exposes a CLI and IDE adapters towards developers" | IDE adapters do not ship in Core today |
| M10 | 7 | "corresponds to exactly one published contract" (§7.3) | policy-resolution/validation/metrics contracts are future |
| M11 | 10 | "Full provenance sealing" (§10.3) | provenance sealing planned, not yet shipped |
| M12 | 10 | "Shared-service mode (indexing many repositories" (§10.6) | shared-service mode planned |
| M13 | 12 | "A lens is a focused checklist for a concern" (§12.4) | lenses are instruction-driven today, not declarative context filters |
| M14 | 12 | "12.5  Policy-Constrained Generation" | policy-constrained generation awaits the effective policy set (aSPARK-policy) |
| M15 | 13 | "aSPARK's governance model has three pillars" | **deviation D1** — supplies the missing roadmap naming (see plan Deviations) |
| M16 | 15 | "The reference deployment places all shared services" | team/on-prem/cloud scenarios depend on unbuilt shared services |
| M17 | 17 | "A.1  Complete Project Configuration" | `.aspark/config.yaml` schema is target state |
| M18 | 17 | "A.2  Policy Pack Manifest" | pack manifests consumed by aSPARK-policy, not Core |

Kept, asserted byte-unchanged after build: existing `Status.` paragraphs ch. 8
(l. 582, `.aspark/`) and ch. 11 (l. 808, declarative gate files).

### In-place edits (labelling of existing label cells — spec C2)
- **R1–R7** ch. 3 Maturity column: Core `Foundation`→`Shipped`; graph `Platform`→`Shipped`;
  policy/insights/ci `Platform`→`Planned` ×3; memory `Future`→`Planned`; Enterprise `Distribution`→`Planned`.

### Title page (T6)
- Replace l. 5 paragraph `Version 1.1  ·  July 2026  ·  reflects aSPARK Core v0.4.0 and aSPARK-graph v0.7.0`
  with three separately identifiable statements: handbook revision `Version 1.2 · August 2026`;
  confirmed shipped-baseline pairs from T3; designation of everything beyond as target architecture.

### AC-1.4 verification (Planned chapters must name deliverer in prose)
- Ch. 9 names `aSPARK-policy` ×3 ✅ · Ch. 14 names `aSPARK-ci` ✅ · Ch. 16 names Stages 1–4 ✅
- **Ch. 13 FAILS** — no `Stage`, no product name in 868–916 → finding, resolved as deviation D1
  (marker M15 supplies the naming; labelling-layer addition, no prose rewritten).

Count reconciliation: 18 markers derive directly from spec §4's inventory column —
ch13 contributes 0 items in the spec table but gains D1/M15; ch6 splits into two
(M8, M9); ch5 consolidated to one (M7). No anchor without an item, no item without
an anchor.

**T2 DoD: met** (manifest complete + reconciled; AC-1.4 checked; one finding raised
per DoD and dispositioned as D1).

## T3 — Baseline spot-check (gates any version bump)

Sources actually read (not assumed):
- **aSPARK-graph releases:** `gh api repos/a-lottes/aSPARK-graph/releases` — latest tag
  `v0.7.0` ("aspark-graph on PyPI"; pip install, `uvx aspark-graph serve`, nine read-only
  tools + build, incremental parse cache, Go/Rust support). Cross-checked against
  `git ls-remote --tags`: highest tag is v0.7.0, annotated.
- **aSPARK Core v0.7.0:** tagged today (2026-08-24) at merge commit `753a793` — this
  repository is the release; every claim below was verified against the actual tree during
  this session's loop runs (constitution §2, `.spark/*/` artifacts, templates, plugin manifests).

### Confirmed baseline pairs (title page may assert exactly these)

| Product | Current released version | Evidence |
|---|---|---|
| aSPARK Core | **v0.7.0** | tag pushed to origin today; lean-rounds release notes |
| aSPARK-graph | **v0.7.0** | GitHub releases API response above |

### Per-item spot-check (marker inventory vs. shipped reality)

| Item | Checked against | Contradiction? |
|---|---|---|
| M1 only Core+graph exist | ROADMAP "wider picture": "aspark-graph is the one such integration wired up today"; no policy/insights/ci/memory repo referenced anywhere | none |
| M2 dedicated-product answers future | same as M1 | none |
| M3 memory future | no aSPARK-memory artifact exists | none |
| M4 Enterprise distribution | no distribution exists | none |
| M5 gates.yaml vs evidence.md | every real `.spark/<feature>/` here uses `evidence.md`; no gates.yaml anywhere | none |
| M6 ADR entity | no ADR records in any `.spark/` feature dir | none |
| M7 P3/P6/P7 awaiting policy | no policy component ships in Core (§2 constitution: single Markdown loop) | none |
| M8 containers unbuilt | same | none |
| M9 IDE adapters absent | plugin.json/marketplace.json publish skills+agents only; no bin, no adapter code | none |
| M10 contracts future | only artifact+query contracts exist (graph v0.7.0 API); policy/validation/metrics contracts have no producer | none |
| M11 provenance sealing | graph v0.7.0 release notes: determinism promise *and its limits* — sealing not among shipped features; staleness query is the available check | none |
| M12 shared-service mode | graph v0.7.0 notes: local CLI/MCP only; no service mode mentioned in any release 0.3.0–0.7.0 | none |
| M13 lenses instruction-driven | constitution §2 active-lens table; lens files under plugin `lenses/`; no declarative filter config | none |
| M14 policy-constrained generation | no effective-policy-set mechanism exists in Core | none |
| D1/M15 ch13 deliverer naming | ch13 prose names neither stages nor products (T2 finding) | gap handled by D1 |
| M16 deployment scenarios need shared services | follows from M12 | none |
| M17 .aspark/config.yaml | repo has no `.aspark/` directory; dials live in `.spark/constitution.md` prose | none |
| M18 pack manifests | no policy.yaml anywhere in Core or graph trees | none |

No contradictions found → zero findings filed from the spot-check; every inventoried
item remains correctly "outside the shipped baseline". The bumped pairs above are the
only title-page values T6 may write.

**T3 DoD: met** (per-item table recorded; both pairs confirmed against real releases;
no value asserted without a corresponding release).

### Recorded user go (first overwrite of the working-tree docx)

Per plan §5 risk row 6, the first overwrite of `docs/aSPARK_Enterprise_Architecture_Handbook.docx`
required T1's evidence to be shown and an explicit user go. **The user selected
"Go — apply to tracked file" on 2026-08-24**, after being shown the T1 extraction proof,
the untouched working tree (`git status docs/` empty), and the confirmed T3 baseline pairs.
Rollback path: `git checkout -- docs/aSPARK_Enterprise_Architecture_Handbook.docx`.

## Resume reconciliation — 2026-08-25

Session interrupted on 2026-08-24 after writing `t5.py`–`t7.py` but before running any
of them or recording results. Found on resume: working-tree docx modified although T4–T7
were `todo`. Reconciliation performed before continuing:

- Working-tree docx SHA-256 `54669464dc25aaca678f2650d371ce1393c9988cd8c9f33077f7db54cd98b3e8`
  — **byte-identical to `/tmp/hm-build/t4-output.docx`** (the prior session's T4 product;
  copied to the working tree later — file mtimes 2026-08-25 05:52 vs 2026-08-24 21:28 —
  under the user go recorded above).
- Fresh `textutil` extraction → `/tmp/hm-build/resume-extract.txt` (1305 lines):
  - 17/17 `Delivery stage:` lines, each immediately under its chapter heading;
    values match spec §4 binding table exactly (13 Partial, 4 Planned: ch. 9/13/14/16).
  - Legend present exactly once (l. 68), defining all three values, directly before
    `1  Executive Summary` (l. 69).
  - Overview table: header (Chapter / Delivery stage / Target-state markers) + exactly
    17 data rows, stage values agreeing with in-chapter labels; Partial chapters point
    at `Status.` markers, Planned chapters at ch. 16 Roadmap.
  - T5/T6 content absent: `Status.` lines = 16 (13 table pointers + legend mention +
    2 kept paragraphs — no inline markers inserted); ch. 3 Maturity column still carries
    old values; title page still reads `Version 1.1 · July 2026 · …`.
- Integrity: `zipfile.testzip()` None; `word/document.xml` parses well-formed; 46 parts.
- Delta audit preview: `diff baseline-extract.txt resume-extract.txt` contains **zero**
  deletion/change lines — pure insertions only (front-matter block incl. table header,
  legend, 17 label lines).

**Verdict:** working tree holds precisely T4's manifest application, nothing else.
T4 marked `done` retroactively (applied 2026-08-24; independently re-verified and
recorded 2026-08-25). Next: T5 via the surviving `/tmp/hm-build/t5.py` after script
review against the manifest.

## T5 — Inline target-state markers + ch. 3 Maturity relabel

`t5.py` (written by the interrupted session, never run) was reviewed line-by-line against
the manifest before execution; two anchor defects surfaced and were fixed (see plan
Deviations **D2**): M9's chapter corrected 6→3 (claim lives in §3.2.2, sole document-wide
occurrence), M12's needle shortened to `indexing many repositories` (verbatim quote crossed
an XML formatting-run boundary; unique document-wide, ch. 10 only). A pre-flight pass then
validated all 18 anchors: 16 already OK, M8's ch.-3 duplicate correctly disambiguated by
the chapter range check.

```
cd /tmp/hm-build && python3 t5.py
→ T5 built: /tmp/hm-build/t5-output.docx | markers: 18 | relabels: 7
```

In-script integrity: every insertion range-checked to exactly one hit inside its chapter;
ch. 3 table asserted at 8 rows with per-product cell assertions; kept ch.8/ch.11 `Status.`
fragments asserted byte-present and unique post-mutation; `ET.fromstring` well-formed;
`testzip()` None. Chains from `t4-output.docx` (byte-identical to working tree, proven
in the reconciliation section above).

Extraction verification (`textutil` → `t5-extract.txt`):

- `^Status\. ` lines = 33 = 18 new markers + 2 kept originals + 13 overview-table pointers.
  All 18 marker texts match the manifest; adjacency enforced structurally (each marker
  paragraph inserted immediately after its anchor paragraph) and spot-checked at M1 (ch. 1
  intro), M9 (§3.2.2), M12 (§10.6), M15/D1 (three-pillars sentence), M17 (A.1).
- ch. 3 Maturity column now reads Core `Shipped`, graph `Shipped`, policy/insights/ci/
  memory/Enterprise `Planned` — only `{Shipped, Planned}`; none of
  Foundation/Platform/Future/Distribution remains as a maturity value (remaining grep hits
  are unrelated prose: figure captions, §14.3 "Platform Adapters", ch. 9 policy-level table).
- No T4 regression: labels 17/17, legend once.
- Package: 46 parts, document.xml well-formed.

Applied to working tree: SHA-256 of `/tmp/hm-build/t5-output.docx` =
`9ffdaaaadfea0f635a006b51101c1881186a43e3c73b2740ce0236bc7a64e1c4` — identical hash on
`docs/aSPARK_Enterprise_Architecture_Handbook.docx`.

**T5 DoD: met.**

## T6 — Title page: revision / baseline / scope designation

`t6.py` (prior session, never run) reviewed against the manifest: replaces the single
`Version 1.1  ·  July 2026  ·  reflects aSPARK Core v0.4.0 and aSPARK-graph v0.7.0`
paragraph with three bold-led, separately identifiable statements; pPr/rPr cloned from the
original paragraph (centered, grey Calibri 22); integrity checks in-script.

```
cd /tmp/hm-build && python3 t6.py
→ T6 built: /tmp/hm-build/t6-output.docx
```

Extraction of page 1:

```
Handbook revision: Version 1.2 · August 2026
Shipped baseline: aSPARK Core v0.7.0 · aSPARK-graph v0.7.0
Scope designation: Content beyond the shipped baseline stated above is target architecture.
```

- All three statements present and distinct (AC-3.1); the pairs are byte-equal to T3's
  confirmed table (AC-3.3, NFR-2 — no baseline claimed without a release).
- `grep -c 'Version 1.1'` → 0: the old mixed revision+baseline line is gone.
- Package: testzip None, document.xml well-formed.

Applied to working tree: `t6-output.docx` SHA-256
`0f1f84e6a7911a332a7b550d3baf4f9fc8b7e816b3e50ffe6b415fee6266fe90`
(`shasum -a 256 t6-output.docx`; `cp` to `docs/aSPARK_Enterprise_Architecture_Handbook.docx`).

**T6 DoD: met.**

## T7 — Full audit: prose-freeze delta proof + AC/NFR walk

`t7.py` (prior session, never run) reviewed first; two bookkeeping bugs fixed before it
could judge anything honestly: (1) the `markers == 18` counter also counted the 13
overview-table pointer cells (`Status. markers in this chapter`) — now excluded by exact
string; (2) `expected_added` did not contain T6's three title statements nor R1–R7's seven
replacement cell values, so the script's own whitelisted outputs would have been flagged
"unexplained" — both now expected explicitly with exact counts (3 statements byte-equal to
T6 output; `Shipped`×2 + `Planned`×5 per RELABELS).

Final extraction of the working-tree docx → `/tmp/hm-build/final-extract.txt`;
near-diff vs `/tmp/hm-build/baseline-extract.txt` (difflib SequenceMatcher):

```
removed lines: 8          → exactly the whitelist: v1.1 title line + 7 old Maturity values
added lines: 101 (1 spacer) → 51 overview-table data cells + 3 header cells, 17 labels,
                              1 legend, 18 markers, 3 title statements,
                              7 relabel replacement values
all checks OK — exit 0    → PROSE FREEZE PROVEN: nothing changed but the manifest layer
```

AC walk (extraction-based unless noted):
- **AC-1.1 ✅** 17/17 visible labels under headings; values ⊆ {Shipped, Partial, Planned}
  (13 Partial, 4 Planned). Visual rendering check reserved for the pre-release open-in-Word.
- **AC-1.2 ✅** each chapter exactly one label; legend once document-wide; no fourth value.
- **AC-1.3 ✅** all 18 inventoried items adjacent to a `Status.` marker naming them outside
  the baseline (M9 per D2 at its physical location §3.2.2).
- **AC-1.4 ✅** ch. 9 names aSPARK-policy ×3, ch. 14 aSPARK-ci, ch. 16 Stages 1–4 (prose,
  T2); ch. 13 via D1/M15 naming Stages 3–4.
- **AC-1.5 ✅** Maturity column = {Shipped×2 (Core, graph), Planned×5}; old values gone.
- **AC-2.1 ✅** one table before ch. 1, header + exactly 17 rows, stage + marker pointer each.
- **AC-2.2 ✅** mechanical cross-check: parsed 17 table rows vs 17 in-chapter labels —
  zero mismatches (script in evidence above).
- **AC-2.3 ⏳** dry run — performed after this section (transcript below); reader = user.
- **AC-3.1 ✅** three separately identifiable title statements.
- **AC-3.2 ✅** every label judged against "the shipped baseline named on the title page"
  (legend wording); pairs are on page 1 — discoverable without opening chapters.
- **AC-3.3 ✅** T3 spot-check recorded; pairs asserted only from confirmed releases.
- **NFR-1 ✅** only {Shipped, Partial, Planned} as stages; defined exactly once (legend).
- **NFR-3 ✅ (pending final diff)** no executable code/script/build step added; so far the
  branch touches docs/, .spark/handbook-maturity/ only — re-asserted at T8 against git.
- **NFR-4 ✅** labels, legend, full table all present in plain-text extraction; dry run
  recorded here; review channel is extraction throughout.

### AC-2.3 dry run — transcript (2026-08-25)

Method per plan §4: a fresh-context reader (the user — not the builder) receives ONLY the
extracted title page + legend + overview table (`final-extract.txt` l. 1–69, shown verbatim
in conversation) and answers two probes.

| Probe | Answer given | Verdict |
|---|---|---|
| (a) Which aSPARK products exist today? | **Core and graph** | correct — equals the title-page shipped-baseline pairs |
| (b) Which chapters are safe to read as shipped behavior? | **No chapter** | correct — the expected sharp result: zero chapters Shipped |

All correct. The ambition/delivery split is legible from the front matter alone in well
under 2 minutes of reading — AC-2.3 met; US-2's "under a minute" skim goal supported.

**T7 DoD: met** (delta audit exit 0 with whitelist holding; full AC walk recorded above;
dry-run transcript recorded).

## NFR-3 final diff assertion

Deferred from the AC walk until T8 completes the ROADMAP edit; re-checked there against
`git status`.

## T8 — Bookkeeping: ROADMAP.md issue #18

Edits to `ROADMAP.md` (matching its own idiom — Shipped table rows for released features,
Next paragraphs for open work):

1. **Shipped** table gains a row "Maturity labels in the handbook": stage label on every
   chapter, overview table up front, inline `Status.` markers, title page separating the
   v1.2 revision from the shipped baseline (Core v0.7.0 · graph v0.7.0). An earlier draft
   of this row wrongly linked PR #23 (that is lean-rounds' PR); corrected before any commit
   — this feature has no PR yet.
2. The #18 **Next** entry is replaced by the post-release follow-up it leaves behind:
   "Close the handbook honesty exception" via `/charter`, explicitly noted as not part of
   the labelling diff.

NFR-3 final assertion (deferred from T7): `git status --porcelain` after T8 shows exactly
` M ROADMAP.md`, ` M docs/aSPARK_Enterprise_Architecture_Handbook.docx`,
`?? .spark/handbook-maturity/` — the branch diff is confined to docs/ content, ROADMAP,
and the .spark/ trail. No script, generator or build step added anywhere.

**T8 DoD: met.**

## Fix round 1 — F1 (review finding): DEFLATE repack of the docx package

Review finding F1 (Minor): the T1 harness's `save()` rewrote all 46 zip parts as
ZIP_STORED (`writestr` without `compress_type`), inflating the tracked binary
2,012,344 → 2,972,610 bytes (+48%) for ~50 KB of real content.

**Recorded user go for this second overwrite of the working-tree docx:** the user selected
"Fix: repack" on 2026-08-25 after being shown the finding, the sizes and the fix
description. Rollback path unchanged: `git checkout -- docs/aSPARK_Enterprise_Architecture_Handbook.docx`.

Fix: `/tmp/hm-build/f1-repack.py` — rewrites the package with `zipfile.ZipFile(...,
zipfile.ZIP_DEFLATED, compresslevel=9)`, copying every entry's **bytes unchanged**, in
order; content neutrality asserted inside the script before it prints (per-entry byte
equality across all 46 parts, entry-order equality, `testzip()`, XML well-formedness).

Verification output:

```
parts: 46 | bytes identical per part: True
size: 2972610 -> 2013907            (net vs pre-feature HEAD 2012344: +1,563 bytes)
EXTRACTION BYTE-IDENTICAL           cmp repack-extract.txt final-extract.txt
t7 exit: 0                          prose-freeze delta audit re-run on the repacked file
```

Applied to working tree: `docs/aSPARK_Enterprise_Architecture_Handbook.docx`
SHA-256 `b46cd684cc2a50d6b2f11b20c928049f6c32b10533ef2224dce498f5fa2eebdf`,
2,013,907 bytes (2026-08-25 08:14).

**F1 fixed; scoped re-review of this fix before QA.**
