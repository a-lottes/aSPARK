# Review Report: <feature-name>

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/<feature-name>/plan.md` |
| **Status** | `in-review` \| `changes-requested` \| `passed` |
| **Date** | YYYY-MM-DD |

## 1. Scope

<!-- What was reviewed: commit range / files. What was NOT reviewed, and why. -->

## 2. Plan Conformance

<!-- Did the implementation follow plan.md? Deviations are findings, even if the code is fine. -->

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ / ⚠️ / ❌ | |

## 3. Findings

<!-- Severity: Blocker = broken/dangerous, must fix. Major = will bite us soon. Minor = should fix. Nit = style.
     Obvious, low-risk fixes may be applied directly by the reviewer — status then says "fixed". -->

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Blocker | `file.ts:42` | | open / fixed |

## 4. Requirements Traceability

<!-- Trace each Must AC and each NFR you can judge from the code back to where it's implemented.
     An AC with no implementing code is a Blocker; an NFR silently dropped is a finding. -->

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

<!-- One honest paragraph. "Looks good" is not a verdict. -->

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [ ] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here)
- [ ] Every Must AC traces to implementing code; no constitution non-negotiable violated
- [ ] All plan deviations documented and accepted
- [ ] Test suite runs green
- [ ] Status set to `passed`
