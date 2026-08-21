# Review Report: <feature-name>

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/<feature-name>/plan.md` |
| **Status** | `in-review` \| `changes-requested` \| `passed` |
| **Round** | 1 |
| **Date** | YYYY-MM-DD |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report — including `/increment` in fix-mode, which is not this
     report's owner — updates it in the same edit that closes or re-rules a finding:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue.

     Re-review: bump `Round` yourself (only the owner bumps it, never `/increment`) at
     the start of the pass, then overwrite every section below in place — §1 Scope, §2
     Plan Conformance, §3 Findings, §4 Traceability, §6 Verdict and the gate checklist
     all hold exactly one current state, never a `## Round N` heading or a second gate.
     History lives in git, not in this file. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** <one-line ruling — not "looks good">
- **Open:** `none` | `<n> open` — Blockers: `<F..>`; Majors: `<F..>` (Minors/Nits: see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

<!-- Budget: ~150 lines. Findings are rows, not essays: location, what's wrong, why it matters, in a
     cell. The report is read back at the gate, again in fix-mode, and once more at re-review — a
     finding that takes three paragraphs to state is a finding nobody rereads. §6 Verdict is the one
     place prose is worth it. -->

## 1. Scope

<!-- What was reviewed: commit range / files. What was NOT reviewed, and why. Re-review:
     overwrite this section to the current round's scope — never append a new one. -->

## 2. Plan Conformance

<!-- Did the implementation follow plan.md? Deviations are findings, even if the code is fine.
     Re-review: overwrite each row's verdict in place. -->

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ / ⚠️ / ❌ | |

## 3. Findings

<!-- Severity: Blocker = broken/dangerous, must fix. Major = will bite us soon. Minor = should fix. Nit = style.
     Obvious, low-risk fixes may be applied directly by the reviewer — status then says "fixed".

     Round vocabulary — overwrite the Status cell in place, never add a row for the same issue:
       `open`                  — currently open. Always exactly this word, never "reopened rN" — a
                                  downstream consumer matches it by exact equality, and a suffixed
                                  or renamed value silently drops the finding from every
                                  open-findings view.
       `fixed`                 — `/increment` fix-mode applied a fix but the owner hasn't
                                  confirmed it yet.
       `fixed r<n>`            — the owner confirmed the fix in round n (overwrites `fixed`).
       `not reproducible r<n>` — a later round found it was never a real problem; the Finding cell
                                  gets at most a one-line amendment that replaces, not appends to,
                                  the part it contradicts.
       `accepted`              — the user chose to ship with this Minor finding present, or
                                  explicitly waived a Major (reason recorded in §6 Verdict); not a
                                  status the reviewer writes unprompted.
     A finding closed then broken again reverts to exactly `open` — never a new word. A genuinely
     new issue gets the next unused `F<n>`, appended as a new row in this same table. -->

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Blocker | `file.ts:42` | | open / fixed |

## 4. Requirements Traceability

<!-- Trace each Must AC and each NFR you can judge from the code back to where it's implemented.
     An AC with no implementing code is a Blocker; an NFR silently dropped is a finding.
     Re-review: overwrite a row's Verdict cell in place; append `r<n>` to the cell only when the
     value changed since the previous round — leave an unchanged cell exactly as it was. -->

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `file.ts:42` | ✅ met / ⚠️ partial / ❌ missing |
| NFR-2 | `auth.ts:88` | ✅ / ⚠️ / ❌ |

## 5. What Was Checked

- [ ] Correctness: logic does what the acceptance criteria demand
- [ ] Non-functional: applicable NFRs and constitution quality bars hold
- [ ] Error handling: failures are handled, not swallowed
- [ ] Security: no injected input trusted, no secrets in code
- [ ] Tests: exist, are meaningful, and pass
- [ ] Readability: the next developer will understand this

## 6. Verdict

<!-- One honest paragraph. "Looks good" is not a verdict. Re-review: overwrite this
     paragraph to the current round's verdict — it is the one binding verdict, always. -->

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [ ] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here)
- [ ] Every Must AC traces to implementing code; no constitution non-negotiable violated
- [ ] All plan deviations documented and accepted
- [ ] Test suite runs green
- [ ] Line budget respected: Ist _N_ / Soll ~150 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [ ] Status set to `passed`
