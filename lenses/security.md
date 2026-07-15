---
name: security
triggers: [handles-auth, is-public, handles-payments, handles-pii]
phases: [specify, review, qa]
---

# Security Lens

Active when the project's **characteristics** include handling authentication,
exposure to the public internet, processing payments, or holding personal data
(PII) — regardless of whether it's a website, web-app or api. Security isn't a
shape of software, it's a property of what the software *does with data*, so this
lens is triggered by characteristics, not type.

The Reviewer already hunts the security basics on every diff (injection, secrets,
authorization). This lens adds the **depth beyond that baseline** — the hardening
and lifecycle concerns a generic pass doesn't reach. It does not repeat the
baseline; it deepens it, the way the `ux` lens deepens base heuristics. It also
covers **privacy/PII**: how personal data is stored, logged, retained and
deleted.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Security & privacy expectations as measurable NFRs | Specify | Product Owner |
| Hardening, auth lifecycle, supply chain, PII handling in the diff | Review | Reviewer |
| Headers, cookies, transport, leaks observable in the browser | QA | QA Tester |

## The checklist

### 1. Transport & headers *(QA-observable, set in Review)*
- [ ] HTTPS everywhere; no mixed content; HSTS set for public sites.
- [ ] A **Content-Security-Policy** is present and not trivially `unsafe-inline`/`*`; clickjacking defense (`X-Frame-Options`/`frame-ancestors`), `X-Content-Type-Options: nosniff`.
- [ ] Cookies carrying auth are `HttpOnly`, `Secure`, and `SameSite` set deliberately.

### 2. Authentication & session lifecycle *(Review)*
- [ ] Sessions/tokens expire, can be revoked, and rotate on privilege change; no eternal token.
- [ ] **CSRF** protection on state-changing requests that rely on cookies.
- [ ] Passwords/secrets are hashed with a modern KDF (never reversible/plain); no credential logged.
- [ ] Auth failures are generic (no "user exists but wrong password" oracle); brute-force is rate-limited/locked out.

### 3. Authorization *(Review)*
- [ ] **Every** data access checks the caller may see/change *this* record — no object-level access left to the client (IDOR). The authz matrix (role × resource × action) has no accidental hole.
- [ ] Privilege escalation paths (mass-assignment of `role`/`isAdmin`, hidden admin routes) are closed.

### 4. Input, output & supply chain *(Review)*
- [ ] Input validated and output encoded for its sink (SQL/NoSQL injection, XSS, path traversal, SSRF, command injection) — deeper than the baseline spot-check, across the diff's new surfaces.
- [ ] Secrets come from a vault/env, never committed; lockfile present and a dependency **audit** is clean (no known-vuln transitive deps introduced).

### 5. Privacy & PII *(Review; deletion QA-observable if there's UI)*
- [ ] PII is minimized (only what's needed), and **never written to logs, error traces or analytics** in the clear.
- [ ] Retention and **deletion** are implemented and honest — a "delete my account" actually removes/anonymizes the data, not just hides it.
- [ ] Personal data isn't leaked into URLs/query strings or third-party requests without basis.

## Phase notes

- **Specify (PO):** turn the relevant risks into measurable NFRs — e.g. "every
  record access is authorized server-side", "PII never appears in logs",
  "account deletion removes personal data within N days", "dependency audit is
  clean at release". These are `NFR-n` the Reviewer and QA trace.
- **Review (Reviewer):** the bulk. Go past your baseline security hunt into the
  hardening and lifecycle items above. A missing authz check on a data access, a
  reversible password store, or PII in logs is a **Blocker**, not a nit — and a
  constitution non-negotiable it violates makes it so by definition.
- **QA (QA Tester):** in the browser, verify the observable surface — response
  security headers and cookie flags (network tab), HTTPS, no secrets/PII in the
  client bundle or console, and that URL/ID tampering can't reach another user's
  data. Report what you saw, under the matching `NFR-n`.
