# Spec: ux-volume-findability

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-11-18 |
| **Ticket** | none (field report from a private project, given in conversation) |

**Handoff**
- **Status:** mirrors the header table above.
- **Summary:** The `ux` lens judges lists, grouped pages and choice controls against the expected usage volume a project declares, not against fixture size; cutting search/filter/pagination for such a list needs a follow-up or a recorded waiver; QA walks every list screen with an after-one-year dataset.
- **Open:** `none`

**Field report.** On a real web-app built by an aSPARK line (closed source, 13 trails, `ux` active), every spec cited the lens, yet at the user's real volume (50 customers) the briefing page, the customer record and the capture form were unusable: a participant picker listing every person of every customer as checkboxes, a "n more not shown" line leading nowhere, no jump list across 50 customer groups. The trails show why: `ux.md` §2 only asks that large data does not *break* layout; scale was specified only as render time; six specs cut search/filter/pagination to *Out of Scope* without anyone deciding it; QA ran only against fixtures with four customers. The user approved this change in conversation (2026-11-18).

**Prompt material.** Every check here is an instruction to an agent, not an enforcement: the effect is likely, not certain. No hold rate is claimed.

## US-1 (Must): A project declares its expected usage volume
- [ ] AC-1.1: When `ux` is active, the constitution template's §2 carries an *Expected usage volume* table (entity, today, after one year, upper bound); `/charter` drafts it via the Facilitator and surfaces it for confirmation. Fixture size is never taken as the volume.
- [ ] AC-1.2: When `ux` is off, the bullet and table are deleted; nothing else changes.

## US-2 (Must): The lens judges findability at that volume
- [ ] AC-2.1: `lenses/ux.md` §7 *Volume & findability* holds falsifiable checks: volume stated per list, item reachable in ≤ 3 actions, bounded lists, no dead-end cap, choice controls > ~15 options have search or context pre-filter, > ~7 groups navigable, four sizes designed.
- [ ] AC-2.2: Cutting search/filter/sort/pagination for a list failing §7 needs a named follow-up or a recorded user waiver; otherwise the Designer raises a `Major`. The PO's Clarify pass returns such a cut as a question.

## US-3 (Must): QA walks list screens at volume
- [ ] AC-3.1: The QA Tester walks every list, grouped page and choice control with an after-one-year dataset at desktop and phone width, counts actions to a chosen item and records a screenshot; fixture-only is `⚠ not verified`.

## Non-functional
- NFR-1: No protected template heading, column or ID pattern renamed or removed; the constitution change appends a bullet and a table inside §2. No new agent, lens file or code; `phases` frontmatter of `ux.md` unchanged (specify, design, qa), so dispatch is unchanged.
- NFR-2: Honest maturity labels: README and `docs/status.md` say "prompt-enforced, unmeasured"; the evidence is n=1 per arm.

## 8. Design Review
N/A: no UI (constitution: Markdown only).
