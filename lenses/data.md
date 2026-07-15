---
name: data
triggers: [has-database]
phases: [specify, review]
---

# Data & Persistence Lens

Active when the project's **characteristics** include a database or persistent
store. Data outlives code: a bad migration corrupts records you can't get back, a
missing index turns a fast feature slow at scale, and unbounded growth is a
production incident waiting for a busy day. This lens keeps the persistence layer
safe to change and sane at scale. It adds the *schema-evolution and
data-lifecycle* concerns beyond the Reviewer's general query red-flags.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.
Where the store holds personal data, coordinate with the `security` lens on
retention and deletion — cite each finding once.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Data lifecycle & scale expectations in the spec | Specify | Product Owner |
| Migrations, indexes, integrity, retention in the diff | Review | Reviewer |

> **No QA row.** Persistence behavior is verified in Review and the increment's
> own tests. Browser-observable data states (empty, large dataset) are already
> the `ux` lens's job — don't double-count them here.

## The checklist

### 1. Schema change safety *(Review)*
- [ ] Every schema change ships as a **migration**, versioned and applied through the same mechanism — no hand-edited production schema.
- [ ] Migrations are **reversible** or have a documented forward-fix; a destructive migration (drop/rename/narrow a column) has a data-preservation or backfill path, not silent loss.
- [ ] Migrations are safe to run online where uptime matters (no table-locking change on a hot table without a strategy).

### 2. Integrity & correctness *(Review)*
- [ ] Constraints enforce invariants at the data layer (not-null, unique, foreign keys) — the DB is the last line of defense, not just the app.
- [ ] Multi-step writes that must not partially apply are wrapped in **transactions**; concurrent-update races are handled (locking/versioning), not assumed away.

### 3. Performance at scale *(Review)*
- [ ] Queries on the feature's access paths are **indexed**; no full scan on a growing table for a common lookup.
- [ ] No N+1 query pattern (cite the Reviewer's baseline once — don't repeat it as a separate finding); list endpoints are bounded/paginated.
- [ ] Large or unbounded columns/collections have a growth story, not "it'll be fine".

### 4. Lifecycle & recovery *(Review)*
- [ ] **Retention and deletion** are defined and implemented where the data warrants it — records don't accumulate forever with no policy (coordinate with `security` for PII).
- [ ] Backup/restore is considered for data that can't be regenerated; a destructive operation has a recovery path.
- [ ] Seed/fixture and empty-state behavior is defined so the feature works from a cold database.

## Phase notes

- **Specify (PO):** capture the lifecycle and scale bars as NFRs — e.g.
  "migrations are reversible", "list queries stay < 200ms at 100k rows",
  "logs/sessions retained N days then purged". Traceable for the Reviewer.
- **Review (Reviewer):** trace the checklist in the diff. An irreversible
  destructive migration, a missing index on a hot path, or a table with no
  retention policy is a finding tied to its NFR — data problems are the ones you
  can't hotfix after they've run.
