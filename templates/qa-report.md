# QA Report: <feature-name>

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Running app (URL), `.spark/<feature-name>/spec.md` (the acceptance criteria) |
| **Status** | `in-testing` \| `failed` \| `passed` |
| **Round** | 1 |
| **Date** | YYYY-MM-DD |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report updates it in the same edit that closes or re-rules a bug:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue.

     Re-test: bump `Round` yourself (only the owner bumps it) at the start of the pass,
     then overwrite every section below in place — §1 Test Environment, §2 AC
     Verification, §3 Exploratory Findings, §4 Console & Network, §5 Verdict and the
     gate checklist all hold exactly one current state, never a `## Round N` heading or
     a second gate. History lives in git, not in this file. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** <one-line ruling — would you demo this right now?>
- **Open:** `none` | `<n> open` — Blockers: `<B..>`; Majors: `<B..>` (Minors: see §3)
- **Binding ruling:** §5 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/demo-day` and proceed — don't stop on it.

<!-- Budget: ~130 lines. Five sections, prose-heavier than review-report.md's (Steps/Expected/
     Observed columns carry real test narrative) — a few more lines per section, not a different
     shape. Exploratory findings are rows, not essays, same discipline as §3 Findings elsewhere. -->

## 1. Test Environment

<!-- Re-test: overwrite this section to the current round's environment — never append a new one. -->

- **App URL:**
- **Browser / viewport(s):** <!-- test desktop AND mobile viewport for UI features -->
- **Test data / accounts used:**

## 2. Acceptance Criteria Verification

<!-- One row per AC from the spec, plus every browser-observable NFR (performance, accessibility,
     reliability on empty/large data). Same AC-n.m / NFR-n IDs as the spec — that closes the
     traceability chain. Every row gets clicked through in the real browser — no "should work".
     Re-test: overwrite a row's Result cell in place; append `r<n>` to the cell only when the value
     changed since the previous round — leave an unchanged cell exactly as it was. -->

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | | | | ✅ pass / ❌ fail |
| NFR-1 | | | | ✅ pass / ❌ fail |

## 3. Exploratory Findings

<!-- Beyond the ACs: what happens on double-click, empty input, refresh mid-action, back button, slow network?

     Round vocabulary — overwrite the Status cell in place, never add a row for the same issue:
       `open`                  — currently open. Always exactly this word, never "reopened rN" — a
                                  downstream consumer matches it by exact equality, and a suffixed
                                  or renamed value silently drops the finding from every
                                  open-findings view.
       `fixed`                 — `/increment` fix-mode applied a fix but the owner hasn't
                                  confirmed it yet.
       `fixed r<n>`            — the owner confirmed the fix in round n (overwrites `fixed`).
       `not reproducible r<n>` — a later round found it was never a real problem; the Steps/
                                  Expected-vs-Observed cell gets at most a one-line amendment that
                                  replaces, not appends to, the part it contradicts.
       `accepted`              — the user chose to ship with this Minor bug present; not a status
                                  a tester writes unprompted.
     A bug closed then broken again reverts to exactly `open` — never a new word. A genuinely new
     issue gets the next unused `B<n>`, appended as a new row in this same table. -->

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Blocker / Major / Minor | | | open / fixed / accepted |

## 4. Console & Network

<!-- Errors/warnings in the browser console, failed requests observed during testing. Empty section = checked and clean.
     Re-test: overwrite this section to the current round's findings. -->

## 5. Verdict

<!-- Would you demo this to a stakeholder right now? If not, it fails. Re-test: overwrite this
     paragraph to the current round's verdict — it is the one binding verdict, always. -->

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run
`/demo-day`. On re-test, edit this same checklist in place — never duplicate it as a second gate.*

- [ ] Every Must-story acceptance criterion verified in the real browser and passed
- [ ] Every browser-observable NFR verified and passed
- [ ] No open Blocker or Major bugs (Minor bugs listed and accepted by the user)
- [ ] Browser console free of errors on the tested flows
- [ ] Tested on all agreed viewports
- [ ] Line budget respected: Ist _N_ / Soll ~130 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [ ] Status set to `passed`
