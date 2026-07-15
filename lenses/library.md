---
name: library
applies-to: [library]
phases: [specify, review]
---

# Library Lens

Active when the project profile includes **`library`** — code other projects
import as a dependency. Its public API is a promise: every exported name is
something consumers will depend on and you'll have to support. The cost of a
library isn't writing it, it's *maintaining the surface you exposed*. This lens
keeps that surface small, intentional and stable. It adds the *API-surface and
release-discipline* concerns a generic review doesn't weigh.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Public-surface intent & compatibility policy in the spec | Specify | Product Owner |
| Exports, semver, types, packaging in the diff | Review | Reviewer |

> **No QA row.** A library has no UI for `/demo-day`. Its verification lives in
> Specify (NFRs), Review (the diff), and the increment's own consumer-facing
> tests — ideally exercising the package as an installed dependency would.

## The checklist

### 1. Public API surface *(Review)*
- [ ] Every new export is **intentional and minimal** — internals stay internal; nothing is public just because it wasn't marked private.
- [ ] The public API is coherent and small: one obvious way to do the common thing, not five overlapping entry points.
- [ ] Type definitions are exported and accurate (typed languages); consumers get autocomplete and compile-time safety, not `any`.

### 2. Compatibility & versioning *(Review)*
- [ ] The diff's effect on **semver** is explicit: a removed/renamed export, a changed signature, a tightened type or a changed default is a **breaking change** and must bump major (or ship behind a deprecation).
- [ ] Removed API goes through a **deprecation path** (marked, warned, documented) before deletion — not yanked in a minor.
- [ ] Additions are backward compatible; new required parameters on existing functions are breaking.

### 3. Packaging & footprint *(Review)*
- [ ] The package exports are correct (entry points, ESM/CJS as declared, `sideEffects` for tree-shaking) so bundlers can drop unused code.
- [ ] Dependencies are justified — each new runtime dependency is a supply-chain and size cost the consumer inherits; heavy or single-use deps get challenged.
- [ ] The build ships only what's needed (no tests, no source-only files) and declares its supported runtimes/engines.

### 4. Contract clarity *(Review)*
- [ ] Public API has usage docs/examples; the README or doc comments show the intended call, not just the type signature.
- [ ] Error behavior is documented: what throws, what returns null/undefined, what's async — consumers shouldn't reverse-engineer it.

## Phase notes

- **Specify (PO):** state the surface intent and the compatibility policy as
  NFRs — e.g. "public API additions only this release; no breaking change to
  `parse()`", "zero new runtime dependencies", "supports Node ≥ 18". Traceable
  for the Reviewer.
- **Review (Reviewer):** trace the checklist in the diff. An accidental export
  or an unflagged breaking change is a finding tied to its NFR — semver drift is
  exactly how a library loses its consumers' trust.
