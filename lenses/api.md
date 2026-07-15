---
name: api
applies-to: [api]
phases: [specify, review]
---

# API Lens

Active when the project profile includes **`api`** — a backend service other
software talks to over the wire. The contract *is* the product: a well-built
endpoint with a surprising shape, an inconsistent error, or a silent breaking
change costs every consumer downstream. This lens keeps the contract honest as
it's built. It does **not** re-run the Reviewer's generic correctness/security
hunt — it adds the *interface-design* concerns that a general review misses.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Contract expectations make it into the spec as NFRs | Specify | Product Owner |
| Endpoint design, versioning, error shape, auth in the diff | Review | Reviewer |

> **No QA row.** `/demo-day` is browser-shaped; an API has no UI to click. Its
> verification lives in Specify (NFRs), Review (the diff), and the increment's
> own contract/integration tests. If the project is *only* an `api`, expect the
> Review gate — not `/demo-day` — to carry the weight.

## The checklist

### 1. Resource & method design *(Review)*
- [ ] Resources are nouns, methods carry the verb; no `GET /getUser?action=delete`-style RPC smuggled over REST.
- [ ] Status codes are used honestly: `2xx` success, `4xx` client error (with which field), `5xx` only for real server faults — not `200 {error: ...}`.
- [ ] Collections support pagination (and it's consistent across endpoints); no unbounded list that returns the whole table.
- [ ] Mutating endpoints that can be retried are **idempotent** or documented as not (idempotency keys where a double-submit would double-charge).

### 2. Contract consistency *(Review)*
- [ ] One **error envelope** shape across the whole API (code, message, field/details) — not three different error shapes on three endpoints.
- [ ] Naming, casing and date/enum formats are consistent everywhere (pick `snake_case` *or* `camelCase`, one timezone/ISO-8601 rule).
- [ ] If an OpenAPI/schema exists, it **matches the implementation** — a spec that lies is worse than none.

### 3. Versioning & compatibility *(Review)*
- [ ] The API is versioned (path, header, or media type) so a change has somewhere to land.
- [ ] The diff introduces **no silent breaking change** to an existing endpoint: removed/renamed fields, tightened validation, changed status codes and altered defaults are breaking — flag them explicitly, they need a version or a deprecation path.
- [ ] New fields are additive and optional where consumers might not send them.

### 4. Security & robustness surface *(Review — coordinate with the `security` lens if active)*
- [ ] **Every** endpoint states its auth requirement; none is accidentally public. Authorization is checked where data is touched, not only at the gateway.
- [ ] All input is validated server-side (type, range, size) before use; no trusting the client.
- [ ] Rate limiting / payload-size limits exist on public or expensive endpoints, or are a conscious, recorded N/A.

## Phase notes

- **Specify (PO):** capture the load-bearing contract facts as measurable NFRs —
  e.g. "list endpoints paginate at ≤100 items", "errors use the standard
  envelope", "no breaking change to v1 without a v2". That gives the Reviewer a
  traceable `NFR-n` instead of a taste debate.
- **Review (Reviewer):** the whole checklist is yours. Trace it in the diff;
  breaking changes and inconsistent error shapes are findings tied to the NFR
  they violate, not style nits. Where a `security` lens is also active, its
  header/authz depth complements this lens — cite each finding once.
