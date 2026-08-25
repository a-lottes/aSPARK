# Spec: handbook-maturity

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-08-24 |
| **Ticket** | none |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this spec updates it in the same edit that resolves a clarification or
     changes status: overwrite in place, never append. The block holds one current
     state, never a per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** `approved` — mirrors header table. All clarify rounds resolved (§7 C1–C10, `Open: none`). Approved by the user on 2026-08-24; SPEC GATE fully checked; design review N/A (document-labelling feature, no UI). Next: `/sprint-plan`.
- **Summary:** The tracked architecture handbook presents a seven-product platform with only two buried admissions; this feature adds per-chapter delivery-stage labels (`Shipped / Partial / Planned`, confirmed), a front-matter overview table, and separates the target-architecture revision from the shipped-product baseline. Labelling, never rewriting. The baseline bumps to each existing product's *current released* versions — but only after a documented prose spot-check performed during build (AC-3.3).
- **Open:** `none`
- **Binding ruling:** §4 User Stories (incl. the binding per-chapter stage assignment table); §7 Clarifications C1–C10 for every decision taken this round.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Problem & Goal

- **Problem:** `docs/aSPARK_Enterprise_Architecture_Handbook.docx` (tracked, v1.1) describes a
  seven-product enterprise platform as one uniform architecture. Exactly two inline `Status.`
  admissions exist (ch. 8 `.aspark/`, ch. 11 gate files) plus seven scattered "planned" mentions.
  No chapter carries a stage label; no front matter summarizes delivery state. A reader of this
  public marketplace repo cannot tell that only 2 of the 7 described products exist (Core, graph).
  Constitution §1 names this a *known open exception* to its honesty principle — a self-declared
  defect (#18). Chapter 3's existing "Maturity" column compounds the problem: it labels
  aSPARK-policy/insights/ci "Platform", identical to shipped aSPARK-graph.
- **Goal:** After this feature, ambition and delivery are distinguishable from the document's
  surface alone — title page, overview table, and a visible stage on every chapter — with zero
  prose rewritten. Labelling only: stage labels, inline target-state markers generalizing the
  existing `Status.` pattern, a legend, the overview table, and version separation.
- **Success signal:** In a documented dry run, a reader unfamiliar with the handbook answers, from
  title page + overview table alone and within 2 minutes: (a) which products exist today,
  (b) which chapters are safe to rely on as shipped behavior. All probes correct. Expected sharp
  result under the §4 rule: zero chapters qualify as fully Shipped today.
- **Why now:** The exception is standing debt against the constitution's own honesty principle, in
  a publicly tracked file; every release that ships without labels widens the gap the document
  denies.

## 2. Target Users

1. **Evaluating engineering leaders / enterprise architects** reading the public repo's `docs/`
   to decide whether to adopt or pilot aSPARK — they feel the pain today: the document oversells.
2. **The maintainer** — the honesty principle is self-governance; the exception is a standing lie
   the maintainer has declared against their own constitution.
3. *(Secondary)* Contributors and AI agents orienting from the handbook as their first reference.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The tracked v1.1 docx is the only document this feature edits | Confirmed. The untracked `aSPARK_Enterprise_Architecture_Handbook_v1.0.docx` was **deleted permanently with the user's explicit go**, executed by the orchestrator on 2026-08-24 (C8) — no work remains for any phase |
| A2 | Taxonomy `{Shipped, Partial, Planned}` + mechanical ceiling rule replaces ch. 3's Foundation/Platform/Future/Distribution column values | Confirmed by the user (C7) |
| A3 | Labels are inserted by direct document editing; no script, generator or linter is added to the repo | Fixed by constitution §3 (Markdown + JSON only, no toolchain) |
| A4 | The revised edition states each existing product's *current released* version pair, bumped only after a documented prose spot-check | Confirmed by the user (C6); the spot-check is build-phase (`/increment`) work, gated by AC-3.3 |

No open questions remain. Every former open item is recorded with its resolution in §7 (C6–C10).

## 4. User Stories

### US-1 (Must): Every chapter carries a visible, truthful delivery-stage label

> As an evaluator deciding on aSPARK, I want every chapter to show a visible delivery-stage label
> from a single defined taxonomy, so that I can tell ambition from delivery without reading
> mid-chapter prose.

**Taxonomy (confirmed, C7):**
- **Shipped** — no target-state capability is described in the chapter; every claim holds in the shipped baseline named on the title page.
- **Partial** — a reader can complete the chapter's core workflow today with shipped products, but named pieces of the chapter are target state; each such piece carries an inline target-state marker (the generalized `Status.` pattern already used in ch. 8 and ch. 11).
- **Planned** — nothing in the chapter is usable today; the chapter names the roadmap stage/product (ch. 16) expected to deliver it.
- **Ceiling rule (mechanical, removes judgment calls):** if a chapter describes *any* target-state capability, its stage is at most Partial — never Shipped.

**Stage assignment (binding for this edition; revisited at each handbook revision):**

| Ch | Chapter | Stage | Target-state items that must carry inline markers |
|---|---|---|---|
| 1 | Executive Summary | Partial | seven-product platform claims (only Core + graph exist) |
| 2 | Product Strategy | Partial | "dedicated product" answers for policy/insights/ci (§2.2) |
| 3 | Product Family | Partial | Maturity column relabelled to this taxonomy; memory "(future)", Enterprise |
| 4 | Domain Model | Partial | gates.yaml evidence shape (today: evidence.md); ADR entity |
| 5 | Architectural Principles | Partial | P3/P6/P7 consequences awaiting aSPARK-policy |
| 6 | C4 Architecture | Partial | containers for policy/insights/ci/memory; Core "IDE adapters" |
| 7 | Product Dependencies | Partial | policy-resolution, validation and metrics contracts (§7.3) |
| 8 | Repository Architecture | Partial | `.aspark/` configuration (existing `Status.` kept) |
| 9 | Policy-as-Code | Planned | names Stage 3 / aSPARK-policy |
| 10 | Knowledge Graph | Partial | shared-service mode (§10.6); provenance sealing (§10.3) |
| 11 | Workflow Engine | Partial | declarative gate files; blocking graph checks (existing `Status.` kept) |
| 12 | Agent Architecture | Partial | policy-constrained generation (§12.5); lens-as-context-filter caveat (§12.4) |
| 13 | Enterprise Governance | Planned | names Stages 3–4 |
| 14 | CI/CD Integration | Planned | names Stage 4 / aSPARK-ci |
| 15 | Deployment Scenarios | Partial | team/on-prem/cloud scenarios need shared services (§10.6) |
| 16 | Roadmap | Planned | entirely forward-looking by design |
| 17 | Appendix | Partial | A.1 `.aspark/config.yaml`; A.2 pack manifests |

**Acceptance criteria:**

- [ ] AC-1.1: Given the revised handbook, when any of the 17 chapters' first page is opened, then a visible stage label is present, drawn only from `{Shipped, Partial, Planned}`.
- [ ] AC-1.2: Given the full document text extracted to plain text, then each of the 17 chapters carries exactly one stage label, a single legend defines the three allowed values in one place, and no fourth value appears anywhere as a chapter stage.
- [ ] AC-1.3: Given a chapter assigned Partial above, when its inventoried target-state items are checked, then each item carries an inline target-state marker naming it as not part of the shipped baseline.
- [ ] AC-1.4: Given a chapter assigned Planned above, then the chapter names the roadmap stage or product expected to deliver its capability.
- [ ] AC-1.5: Given chapter 3's product-family table, then its Maturity column uses the taxonomy values and distinguishes the two shipped products (Core, graph) from the five that do not exist today (policy, insights, ci, memory, Enterprise).

### US-2 (Must): Front-of-document maturity overview table

> As a decision maker skimming the handbook before adoption, I want one table up front listing
> every chapter with its stage and divergence pointers, so that I can see the ambition/delivery
> split in under a minute.

**Acceptance criteria:**

- [ ] AC-2.1: Given the revised handbook's front matter, then one overview table appears before chapter 1 with exactly 17 rows — one per chapter — showing each chapter's stage and a pointer to that chapter's target-state markers.
- [ ] AC-2.2: Given the overview table, then no stage value in it disagrees with the label inside the corresponding chapter.
- [ ] AC-2.3: Given a reader unfamiliar with the handbook, when they read only the title page and this table, then they correctly answer the §1 success-signal probes in a documented dry run within 2 minutes.

### US-3 (Should): Target-architecture revision separated from the shipped baseline

> As a reader comparing the handbook to installed software, I want the document's revision
> identity visually separated from the shipped-product baseline it claims to reflect, so that a
> mismatch between ambition and installed versions is detectable at a glance.

**Acceptance criteria:**

- [ ] AC-3.1: Given the title page, then three separately identifiable statements appear: the handbook revision identifier (incremented for this edition, per C6); each existing product's *current released* version as a product:version pair; and a designation that content beyond that baseline is target architecture.
- [ ] AC-3.2: Given any stage label anywhere in the document, then the baseline it is judged against is discoverable from the title page or the overview table without opening other chapters.
- [ ] AC-3.3: Given the baseline version pairs on the title page, then they were updated only after a documented spot-check pass — build-phase (`/increment`) work — that walked the handbook's chapter prose against what the current Core and graph releases actually ship, using the §4 marker inventory as its checklist; any contradiction found became either an inline target-state marker or a separately filed finding, never a silent prose edit.

## 5. Non-Functional Requirements

Library lens (§2 constitution): packaging/footprint checks are N/A (no bundle, no deps); the
applicable slices are contract clarity, version discipline and public-surface restraint.

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Contract clarity (lens §4) | Only the three taxonomy values appear as chapter stages, and each is defined exactly once in the document (legend or glossary) | /peer-review against extracted text |
| NFR-2 | Compatibility / versioning (lens §2) | At merge, the title page states each existing product's current released version, verified against release notes, updated only after the documented pre-bump spot-check (AC-3.3); no baseline is claimed without a corresponding release | /peer-review + release-notes history |
| NFR-3 | Public-surface restraint (lens §1) | The diff adds no executable code, script, dependency or build step; changes confined to `docs/` content plus ROADMAP/constitution bookkeeping | /peer-review diff inspection |
| NFR-4 | Reliability / reviewability | Every stage label, the legend and the full overview table survive plain-text extraction of the docx (selective text, not images or text boxes); the change is exercised by a documented dry run per constitution §4, recorded in `.spark/handbook-maturity/evidence.md` | Dry run + /peer-review |
| NFR-5 | Performance | N/A — static document, no runtime | — |
| NFR-6 | Security & privacy | N/A — content-only change to an already-public tracked file; no new surface, no secrets (constitution §6 applies globally) | — |
| NFR-7 | Observability / ops | N/A — no runtime to observe | — |

Accepted limitation: the docx is binary and unfriendly to diff; reviewers verify via text
extraction (NFR-4) rather than line diffs. Converting the handbook to a Markdown source of truth
is deliberately out of scope (§6).

## 6. Out of Scope

- **Any prose rewrite** beyond labels, inline target-state markers, the legend, the overview
  table and the title-page version statements. Contradictions the AC-3.3 spot-check uncovers
  become markers or separately filed findings — never silent prose fixes in this diff.
- **Tooling:** no script, generator, validator or CI step for the docx; no conversion of the
  handbook to Markdown/generated output (a separate architecture-of-docs decision).
- **Website sync** — the sibling aSPARK website restates the same architecture claims; confirmed
  out of scope here (C9) as an **immediate follow-up feature**: this handbook's corrections must
  carry over there.
- **The untracked v1.0 docx** — fully resolved: deleted permanently with the user's explicit go,
  executed 2026-08-24 (C8). Recorded here only so no phase wonders where the file went; nothing
  remains to plan or verify.
- **Closing the constitution §1 exception** via `/charter` amendment — a post-release process
  step, not part of this feature's diff.
- **Refreshing chapter prose to newer Core behavior** beyond what labelling requires (baseline
  bump is metadata per C6; prose follows only through markers/findings).

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-08-24 | Which stage vocabulary? Ch. 3's Foundation/Platform/Future/Distribution cannot distinguish shipped graph from nonexistent policy; repo statuses (`released`/`handed-off`) are loop-internal jargon | Default `{Shipped, Partial, Planned}` + ceiling rule proposed; superseded by C7's confirmation |
| C2 | 2026-08-24 | Is relabelling ch. 3's Maturity column "rewriting"? | No — the cell values are labels; changing them is in scope (AC-1.5). Adding/removing rows or columns would not be |
| C3 | 2026-08-24 | Do strategy chapters (1, 2, 16) need labels? | Yes — all 17 chapters labelled; strategy chapters inherit the platform's stage (Partial); Roadmap is Planned. Keeps the taxonomy mechanical |
| C4 | 2026-08-24 | Tie-break for contested chapters? | Ceiling rule (§4): any target-state capability described ⇒ at most Partial; core workflow not runnable today ⇒ Planned. Applied to yield the §4 table |
| C5 | 2026-08-24 | Docx reviewability risk? | Accepted limitation recorded in §5/NFR-4: verification via text extraction, not diffs. Markdown conversion cut to §6 |
| C6 | 2026-08-24 | Q1 — keep printed baseline (Core 0.4.0 / graph 0.7.0) or bump? | User: **bump to each existing product's current released version pair**, but only after a spot-check that chapter prose doesn't contradict what those releases ship. The spot-check is build-phase (`/increment`) work, made traceable as AC-3.3. Side default adopted: the handbook revision identifier increments for this edition |
| C7 | 2026-08-24 | Q2 — taxonomy scale? | User: **accepted as proposed** — `Shipped / Partial / Planned`, ceiling rule, binding 17-row assignment table (§4) |
| C8 | 2026-08-24 | Q3 — fate of untracked `docs/aSPARK_Enterprise_Architecture_Handbook_v1.0.docx`? | User: **delete permanently**. Executed by the orchestrator immediately after the answer (user's explicit go recorded here); the file is gone from the working tree. Resolved-and-executed — no open work for any phase |
| C9 | 2026-08-24 | Q4 — website sync in or out of this feature? | User raised no objection to the stated default: **Out of Scope**, flagged as immediate follow-up feature (website restates the same architecture claims; corrections must carry over) |
| C10 | 2026-08-24 | Q5 — adjudicate ch. 13 and ch. 16 individually? | User: **accept the mechanical ruling** — both `Planned`; the §4 table's "(may contest)" annotations removed |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **Overall impression:**
- **Heuristics findings:** (visibility of status, consistency, error prevention, recognition over recall, …)
- **Accessibility notes:** (contrast, keyboard navigation, focus order, labels)
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked
- [x] Open questions are resolved or explicitly accepted as risk *(all resolved — C6–C10)*
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review done for UI-facing features (or marked N/A with reason) *(N/A — document-labelling feature, no UI)*
- [x] Status set to `approved` by the user *(explicitly, 2026-08-24)*
