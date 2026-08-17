# Release: <feature-name>

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `preparing` \| `released` \| `aborted` \| `handed-off` |
| **Version** | vX.Y.Z |
| **Date** | YYYY-MM-DD |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report updates it in the same edit that changes status or actions:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** <one-line release summary>
- **Open:** `none` | `<n> outstanding` — see §4 Learnings / KEEP GATE for who owns what remains (relevant in `handed-off` mode)
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

<!-- Verified immediately before releasing — not copied from earlier reports. -->

- [ ] `review.md` status is `passed`
- [ ] `qa.md` status is `passed`
- [ ] Full test suite green on the release commit
- [ ] Build succeeds from a clean checkout
- [ ] No uncommitted changes in the working tree

## 2. Changelog

<!-- User-facing language. What can they do now that they couldn't before? -->

### Added
-

### Changed
-

### Fixed
-

## 3. Release Actions

<!-- What was actually executed, with results. -->

<!-- Direct mode: fill all four. Declared `pr` mode (handed-off): Version bump is
     *proposed only*, no tag before merge; Deploy and Post-release smoke check
     are N/A — write "N/A — handed-off, no deploy" rather than leaving them blank. -->

| Action | Result |
|---|---|
| Version bump & tag | |
| PR / merge | |
| Deploy | |
| Post-release smoke check | |

## 4. Learnings (Keep!)

<!-- The K in SPARK: what does the team keep from this cycle? -->

- **What went well:**
- **What we'd do differently:**
- **Patterns worth reusing:** <!-- candidates for CLAUDE.md / project memory -->

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [ ] All pre-flight checks passed at release time
- [ ] Changelog written in user-facing language
- [ ] Release actions executed and verified (or `aborted` with reason) —
      in declared `pr` mode: PR open on the target branch, CI green, the
      declared approver requested, the ticket linked where one is declared,
      rollback path written; Deploy and Post-release smoke check are N/A
- [ ] Learnings recorded
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode —
      naming in one line what remains outstanding and who owns it
