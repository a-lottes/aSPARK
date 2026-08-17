# Plan: lean-artifacts

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/lean-artifacts/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-08-15 |

## 1. Architecture Decision

- **Context:** Five shipped templates each open with `# <Title>` then a two-column
  header metadata table whose `Status`/`Version` rows the sibling parser
  (`aspark-graph/artifacts.py`, A4) locks onto by `re.search`ing the *whole file*
  for the **first** `| **Status** |` / `| **Version** |` row, and by taking the
  **first** `##` heading containing a keyword (`user stories`, `task breakdown`,
  `findings`, `acceptance criteria verification`) and the **first** table in it.
  The block must add a fixed-address handoff summary above the first numbered
  section without tripping any of that, stay ≤12 rendered lines (C5), be
  overwritten in place on every write (C8/C11), and be self-explaining (NFR-3).

- **Decision:** A **heading-less block** placed immediately after the header
  metadata table and before `## 1.`, rendered as a lead line plus a bullet list
  (no `##` heading, no markdown table, no pipe-delimited row). Six fields:
  **Status** (mirrors the header table, which is named authoritative for it),
  **Verdict/summary** (one line), **Open items** (`none`, or total + Blocker/Major
  IDs + a pointer to the section holding the rest — AC-1.7), **Binding ruling**
  (which section carries the binding verdict/gate, latest round on a re-ruled
  report — AC-1.6), **On conflict** (the numbered body is authoritative; a stale
  block is a defect, not cosmetic — AC-1.2/1.3/1.8). An adjacent HTML comment
  (excluded from the line count) states who reads it, that every writing phase
  overwrites it in the same edit, and that the body wins on conflict (NFR-3).

- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Extend the existing header metadata table with `Verdict`/`Open` rows (A1's "extension" option) | Couples a mutable, per-write index to the one protected table that holds the parser's single `Status`/`Version` row. Any refresh risks a second `\| **Status** \|`-shaped row — the exact A4 breakage — and AC-1.7's empty/over-capacity prose does not fit a 2-col cell. Rejected on A4 safety and NFR-3 clarity. |
  | A block under its own `## Handoff` heading (A1's "new element" as a section) | Parser-safe *only* while nobody ever renames the heading into an A4 keyword; adds a numbered-section ambiguity above `## 1.`. A heading-less block removes the entire "new `##`" risk class at no cost. |
  | Restate nothing, just point to the header (`see Status above`) | Violates AC-1.1's floor: the block must itself carry status, a one-line verdict and the open-item IDs. A bare pointer is not a fixed address. |

- **Consequences:** Easier — zero new `##` headings and zero pipe rows means A4's
  three conditions hold by construction, so the compatibility claim (AC-1.4/NFR-1)
  reduces to a static walkthrough; the block generalises unchanged across all five
  templates. Harder — the block is unenforced (A2/NFR-4): freshness depends on every
  writing phase honouring the overwrite instruction, verified only by dogfood, never
  by a gate.

## 2. Affected Components

- **Templates (block added):** `templates/review-report.md`, `templates/qa-report.md`
  (Must, US-1); `templates/spec.md`, `templates/plan.md`, `templates/release-notes.md`
  (Should, US-3). `templates/constitution.md` excluded (C10).
- **Consumers (reading/writing rules — reconciled A6 list):** `agents/reviewer.md`
  (re-review), `skills/increment/SKILL.md` (fix-mode, **writes back**),
  `agents/release-manager.md`, `agents/product-owner.md` **and** its ceremony
  `skills/next-steps/SKILL.md` — the latter is the A6 correction: spec §2 named only
  the agent, but `next-steps/SKILL.md:33-39` is where the across-feature-dir read is
  enumerated. `skills/spark/SKILL.md:36-50` greps `Status` to route — a compatibility
  surface (the block must not shadow the header `Status`), **not** a reading-rule edit;
  covered by the parser/router check in T4.
- **Release housekeeping:** `.claude-plugin/plugin.json` (minor bump 0.5.0 → 0.6.0),
  `README.md` (§Project Status, honest claim per NFR-4).
- **Dogfood record:** `.spark/lean-artifacts/evidence.md` (precedent: `graph-gates`,
  `tracker-handoff`).
- **New dependencies:** none — Markdown/JSON only (constitution §3).
- **Blast radius:** `aspark-graph impact` is empty by construction here (Markdown-only
  repo, no source nodes — tool file's own note), so *Affected Components* was scoped by
  hand from the A6 grep, not from the graph. The `story_trace` baseline in §4 grounds
  AC-3.2's before-image; the plan does not depend on it.

## 3. Task Breakdown

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Confirm/finalise the exhaustive consumer list (A6): re-grep every `agents/*.md` + `skills/*/SKILL.md` for reads of `review`/`qa`/`spec`/`plan`/`release`; reconcile against spec §2; record additions (`next-steps/SKILL.md`) and the `spark/SKILL.md` router as a compat-only surface. Flag any §2 divergence to the PO | US-2 | AC-2.1 | – | `done` | A written, reconciled consumer list exists in the dogfood record, each entry marked reader / writer / compat-only, and every divergence from spec §2 is named for the PO — files: .spark/lean-artifacts/evidence.md |
| T2 | Walking skeleton (1/2): add the heading-less handoff block to `review-report.md` above `## 1.` — six fields, HTML-comment guidance, ≤12 rendered lines (comments excluded), no `##` heading, no pipe `\| **Status** \|` row | US-1 | AC-1.1, AC-1.2, AC-1.6, AC-1.7, AC-1.8, AC-3.3, NFR-1, NFR-3 | T1 | `done` | Block present with all six fields; `claude plugin validate` passes; a grep confirms no new `##` heading and no second `\| **Status** \|` row; rendered block ≤12 lines — files: templates/review-report.md |
| T3 | Walking skeleton (2/2): add the re-review reading rule to `reviewer.md` — read the block first; the **named condition that requires the full body** = verifying fixes on re-review (AC-2.2); on block/body conflict proceed on the body and log the contradiction as a finding (AC-1.8) | US-2 | AC-2.1, AC-2.2, AC-1.8 | T2 | `done` | `reviewer.md` re-review step names what it reads first, names at least one condition demanding the full body, and states the conflict behaviour; `claude plugin validate` passes — files: agents/reviewer.md |
| T4 | Dogfood the skeleton, **negative case first**: reviewer re-review reads an old-shape `review.md` (`.spark/graph-gates/review.md`) → identical behaviour, no error/warning/migration (AC-2.4/1.5/NFR-5); then a new-shape fixture review.md → first read is bounded (offset/limit or the named block), reader states whether it needed the body (AC-2.3); plus a C9 static walkthrough of `_parse_review` against A4's three conditions on the exact block text → no `TemplateDriftError`, same Finding nodes (AC-1.4). If the design fails here, fix T2 before rollout | US-1, US-2 | AC-1.4, AC-1.5, AC-2.3, AC-2.4, NFR-1, NFR-4, NFR-5 | T3 | `done` | Dogfood record holds the negative-then-positive transcript and the static-walkthrough conclusion; no token/byte saving is claimed — files: .spark/lean-artifacts/evidence.md |
| T5 | Roll the block out to `qa-report.md` (second Must template), same shape and constraints | US-1 | AC-1.1, AC-1.7, AC-3.3, NFR-1 | T4 | `done` | Block present, ≤12 lines, no new keyword `##` heading, no second `\| **Status** \|` row; `claude plugin validate` passes — files: templates/qa-report.md |
| T6 | Add the same-shape block to the three US-3 templates | US-3 | AC-3.1, AC-3.3, NFR-1 | T4 | `done` | Each carries a same-shape block ≤12 lines, no new keyword `##` heading, no second `\| **Status** \|` / `\| **Version** \|` row; `claude plugin validate` passes — files: templates/spec.md, templates/plan.md, templates/release-notes.md |
| T7 | Wire the fix-mode **write-back** in `increment/SKILL.md`: the same edit that closes/re-rules a finding overwrites the block in place (never appends — C6/AC-1.3); add the bounded read (findings/block first) | US-1, US-2 | AC-1.3, AC-2.1, NFR-3 | T4 | `done` | Fix-mode step states the in-place block overwrite as part of the write and the bounded first read; `claude plugin validate` passes — files: skills/increment/SKILL.md |
| T8 | Add reading rules to the remaining consumers: `release-manager.md` (block first to check the two gates), `product-owner.md` + `next-steps/SKILL.md` (newest open items from the block across feature dirs), each with the named condition to read further | US-2 | AC-2.1, AC-2.2 | T4 | `done` | Each consumer states what it reads first and the named condition to read on; `claude plugin validate` passes — files: agents/release-manager.md, agents/product-owner.md, skills/next-steps/SKILL.md |
| T9 | Full-rollout dogfood, **negative case first**, over a second consumer pair (`/next-steps` + `/go-live`) against old-shape then new-shape artifacts; verify fix-mode overwrite (AC-1.3); C9 static walkthrough of `_parse_qa`/`_status`/`_release_version` for spec/plan/release → `spec_status`/`plan_status`/`release_status`/`version` unchanged, no `US-`/`AC-`/`T` node added, lost or renamed (AC-3.2) | US-1, US-2, US-3 | AC-1.3, AC-2.3, AC-2.4, AC-3.2, NFR-1, NFR-5 | T5, T6, T7, T8 | `done` | Dogfood record extended with the negative-then-positive transcript for the second pair and the static-walkthrough conclusion for the other four parsers — files: .spark/lean-artifacts/evidence.md |
| T10 | Release housekeeping: minor version bump and honest docs — no claimed token/byte saving, added surface enumerated line by line (NFR-2/NFR-4) | US-1 | NFR-2, NFR-4 | T9 | `done` | `plugin.json` version is `0.6.0`; `README.md` §Project Status names the block + reading rules as shipped, claims no token/byte reduction; `claude plugin validate` passes — files: .claude-plugin/plugin.json, README.md |

## 4. Test Strategy

No automated suite is possible for prompt material (constitution §4). The bar per
task is `claude plugin validate` **plus** a documented dogfood, **negative case first**.

- **US-1 (block correctness & parser safety).** AC-1.4 is verified by a **C9 static
  walkthrough** of `artifacts.py` against A4's three conditions on the exact block
  text — this is the primary method because the graph is *blind to Core's review/qa
  artifacts* (defect 1: it probes `review-report.md`/`qa-report.md`, Core writes
  `review.md`/`qa.md`), so no graph query can ground the review/qa node set. AC-1.5
  and AC-1.2/1.3/1.7 are verified in the T4 dogfood.
- **US-2 (bounded reading).** AC-2.4 (negative) then AC-2.3 (positive), each run in
  T4 (skeleton pair: reviewer re-review) and T9 (second pair: `/next-steps` + `/go-live`).
  The negative run uses a real old-shape artifact (`.spark/graph-gates/review.md`,
  695 lines, no block); nothing may differ from today. The positive run uses a
  new-shape fixture and must show a bounded first read (offset/limit or the named
  block) with the reader stating whether it then needed the body — AC-2.2's body-
  requiring condition (re-review verifying fixes) is exercised here.
- **US-3 (other three templates).** AC-3.2 verified in T9 by static walkthrough of
  `_status`/`_release_version`/`_parse_qa` and the story/AC/task parse — spec/plan/
  release *can* be parsed by the graph (no filename mismatch for spec.md/plan.md),
  so the baseline query below grounds the before-image.
- **Baseline query (run 2026-08-15, non-blocking):**
  `aspark-graph query story_trace US-1 --feature graph-gates` returned `found: true`
  — US-1 (Must), 5 ACs (AC-1.1–1.5), 4 tasks (T1/T5/T10/T11) all `done`, every AC
  `latest_result: null` / `qa_checks: []`. This is the confirmed AC-3.2 before-image
  for the declared spec+plan node set; the `null`/empty QA leg is the known consumer
  defect 1 (the graph is QA-blind for Core-managed repos), not a real gap — exactly
  why AC-1.4 for review/qa rests on the static walkthrough regardless.
- **Deliberately manual only:** everything — there is no runtime to test. Reason:
  constitution §4 forbids assuming a test suite; the mechanism is a prompt instruction
  (NFR-4), so a dogfood transcript is the only honest evidence.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| **Unenforced instruction (A2/NFR-4).** Nothing stops an agent reading the whole file or leaving the block stale. | Feature delivers no guaranteed saving; a stale block could mislead. | Claim only a bounded *first read*, never a token saving (T4/T10). Make staleness a *defect* in-template (T2) and conflict-resolution fall back to the body (AC-1.8), so a stale block never blocks or misroutes. |
| **Conditional parser safety (A4).** A future edit adding a keyword `##` heading or a second `\| **Status** \|`/`\| **Version** \|` row silently breaks `aspark-graph` in a downstream repo. | Silent cross-repo break (constitution §6). | Heading-less, table-less block by design; every template task's DoD greps for the forbidden shapes; T4/T9 static walkthroughs confirm against `artifacts.py`. |
| **A6 consumer list under-inclusive.** AC-2.1 scope is only as good as the list; the grep already surfaced `next-steps/SKILL.md` beyond §2. | A missed consumer keeps hand-rolling whole-file reads. | T1 re-derives exhaustively and reconciles with §2 *before* the reader-rule tasks; divergences flagged to the PO, not silently absorbed. |
| **`/spark` router reads `Status` by grep (found in A6).** The block's `Status` line could shadow the header row for Core's own router. | Mis-routing of the loop. | Block carries `Status` as a bulleted line (no pipe), which the router's `\| … \|` grep cannot match; verified in T4 alongside the parser check. |
| **Fixture realism.** A hand-made new-shape fixture may not match how a real ceremony writes the block. | Dogfood proves less than it appears. | Build the fixture by instantiating the actual edited template; run the real reviewer/PO reading path over it, not a mock.

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft)
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded)
- [x] Every task maps to a user story — no orphan tasks, no story without tasks
- [x] Every Must AC and every applicable NFR is covered by at least one task
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Status set to `approved` by the user — given explicitly by the user on 2026-08-15, after presenting architecture, tasks and risks
