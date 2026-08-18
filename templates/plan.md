# Plan: <feature-name>

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/<feature-name>/spec.md` (must be `approved`) |
| **Status** | `draft` \| `approved` |
| **Date** | YYYY-MM-DD |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this plan updates it in the same edit that changes a task's status or
     the plan's own status: overwrite in place, never append. The block holds one
     current state, never a per-round log; a stale block is a defect, not a cosmetic
     issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Summary:** <one-line architecture-decision digest>
- **Open:** `none` | `<n> tasks not done` — see §3 Task Breakdown for which
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

<!-- Budget: ~300 lines. The plan is /increment's backlog and the Reviewer's yardstick — both read it
     in full, repeatedly, and a fix round reads it again. Argue the architecture in §1 tightly; the
     task table earns the space, the prose around it usually doesn't. A plan that needs far more than
     this is describing an increment too large to review in one pass — cut scope, don't cut detail. -->

## 1. Architecture Decision

<!-- Mini-ADR. The EM decides — but shows the alternatives that were rejected and why. -->

- **Context:** What technical situation does the spec put us in?
- **Decision:** The chosen approach, in two or three sentences.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | | |
- **Consequences:** What becomes easier, what becomes harder?

## 2. Affected Components

<!-- Files, modules, services, external dependencies. New dependencies need a justification. -->

## 3. Task Breakdown

<!-- Ordered. Every task maps to the spec by ID (the story and the specific AC-n.m / NFR-n it serves)
     and has its own definition of done. The "Covers" column is the traceability spine: every Must AC
     and every applicable NFR must appear against at least one task.
     /increment works through this table top to bottom — nothing else — and keeps Status current.

     End each Definition of Done with a `files:` note naming the files the task is expected to
     touch, so the task→code link is declared instead of guessed by whoever reads the plan later:

         … and a test proves it — files: src/auth/session.ts, src/auth/session.test.ts

     Four rules:
     1. Repo-relative POSIX paths, comma-separated.
     2. The note is the **last** thing in the cell — nothing after the paths.
     3. **No** trailing punctuation after the last path.
     4. If the touched files are not knowable at plan time, **omit** the note —
        never guess.

     Rules 2 and 3 are not style. A tool reading this note matches greedily to
     the cell's closing pipe and then splits on commas **and whitespace**, so
     `files: src/a.py.` yields the path `src/a.py.` — which resolves to nothing
     — and any prose after the paths becomes junk entries. Either way the link
     is silently dropped: no error, no warning, no edge. Rule 4 matters because
     a declared link outranks an inferred one downstream, so a wrong note is
     worse than no note. -->

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | | US-1 | AC-1.1, AC-1.2 | – | `todo` | |
| T2 | | US-1 | AC-1.3, NFR-1 | T1 | `todo` | |

## 4. Test Strategy

<!-- What gets unit tests, what gets integration tests, what is left to /demo-day in the browser. -->

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| | | |

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [ ] Spec status is `approved` (never plan against a draft)
- [ ] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [ ] Architecture respects the constitution's technical constraints (or a conflict is recorded)
- [ ] Every task maps to a user story — no orphan tasks, no story without tasks
- [ ] Every Must AC and every applicable NFR is covered by at least one task
- [ ] Every task has a checkable definition of done
- [ ] Task order respects dependencies
- [ ] Test strategy covers every Must story
- [ ] Status set to `approved` by the user
