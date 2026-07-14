# Spec: <feature-name>

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `draft` \| `design-checked` \| `approved` \| `rejected` |
| **Date** | YYYY-MM-DD |

## 1. Problem & Goal

<!-- The PO's interrogation result. Not what the user asked for — what they actually need. -->

- **Problem:** What hurts today? Who feels the pain?
- **Goal:** What outcome makes this feature a success?
- **Success signal:** How do we know it worked? (metric, observable behavior)
- **Why now:** What breaks or is lost if we don't build this?

## 2. Target Users

<!-- Concrete personas or roles. "Everyone" is not an answer. -->

## 3. Assumptions & Open Questions

<!-- Every assumption is a risk. Open questions block the gate until answered or explicitly accepted. -->

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | | |

## 4. User Stories

<!-- MoSCoW priority: Must / Should / Could / Won't. Every story needs testable acceptance criteria.
     Story and AC IDs (US-n, AC-n.m) are stable — they are the traceability anchor the plan, review
     and QA all cite. Never renumber an existing ID; add new ones at the end. -->

### US-1 (Must): <title>

> As a <role>, I want <capability>, so that <benefit>.

**Acceptance criteria:**

- [ ] AC-1.1: Given <context>, when <action>, then <observable result>.
- [ ] AC-1.2: …

## 5. Non-Functional Requirements

<!-- Cross-cutting qualities the feature must meet, separate from functional behavior. Each NFR is
     falsifiable and downstream-traceable (NFR-n). Delete a row only if it genuinely does not apply —
     "N/A" with a one-line reason is better than a silent gap. -->

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Performance | e.g. dashboard renders within 2s on a mid-range laptop | /demo-day |
| NFR-2 | Security & privacy | e.g. only the owning user can read their stats | /peer-review |
| NFR-3 | Accessibility | e.g. WCAG 2.1 AA: contrast, keyboard nav, focus order | /look-and-feel + /demo-day |
| NFR-4 | Reliability / scale | e.g. handles an empty and a 10k-row dataset without error | /demo-day |
| NFR-5 | Observability / ops | e.g. failures are logged with enough context to debug | /peer-review |

## 6. Out of Scope

<!-- Explicitly cut. Prevents scope creep in /increment. -->

## 7. Clarifications

<!-- The record of the Specify-phase Clarify pass: ambiguities the PO surfaced and how they were
     resolved. Each resolution either sharpens a story/NFR above or lands in Out of Scope. An
     unresolved clarification is an open question — move it to §3 and keep the gate closed. -->

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | YYYY-MM-DD | | |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **Overall impression:**
- **Heuristics findings:** (visibility of status, consistency, error prevention, recognition over recall, …)
- **Accessibility notes:** (contrast, keyboard navigation, focus order, labels)
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [ ] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [ ] Every story has testable Given/When/Then acceptance criteria
- [ ] Stories are prioritized (MoSCoW) and at least one is a Must
- [ ] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [ ] Clarify pass done: no ambiguity left unresolved or unparked
- [ ] Open questions are resolved or explicitly accepted as risk
- [ ] Out-of-scope section is filled (something was consciously cut)
- [ ] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [ ] Design review done for UI-facing features (or marked N/A with reason)
- [ ] Status set to `approved` by the user
