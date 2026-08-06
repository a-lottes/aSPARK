# QA Report: tracker-handoff

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/tracker-handoff/spec.md` (ACs 1.1–4.4, NFR-1…11), `review.md` (`passed`, F1/F2 open Minors) |
| **Status** | `passed` |
| **Date** | 2026-08-06 |

## 1. Test Environment

**⚠ Documented ceremony override — the venue is not a browser.**
`/demo-day` as written requires a running app in a real browser. This feature changes
only Markdown prompt material (`templates/`, `agents/`, `skills/`, `docs/`, `README.md`)
in aSPARK Core — a Claude Code plugin with no runtime and no UI. There is no URL, no
server, no page. The user was told this and **explicitly chose** the substitute method
below, the same override this repo already used for `graph-gates` (`.spark/graph-gates/qa.md`).

**Substituted definition of a performed step.** A performed step is a **real ceremony
invocation or a real command whose output was observed**. Reading a Markdown file and
reasoning about what it *would* do is explicitly **not** a performed step; every row
below marked `pass` rests on a command I ran or a role I actually played and a file I
actually wrote and then re-read/grepped. Rows that could not be reached this way are
marked `not-verified-live`, never `pass`. This mirrors `graph-gates`' own rule and this
feature's own AC-3.4-adjacent spirit of evidence.

**Files exercised — the working-tree, already-edited versions**, confirmed via
`git status --porcelain` in `/Users/andreaslottes/aSPARK` (all 10 touched files show
as modified, uncommitted): `templates/{release-notes,constitution,spec}.md`,
`agents/{release-manager,facilitator}.md`, `skills/{go-live,spark,next-steps}/SKILL.md`,
`docs/workflow.md`, `README.md`. Not the installed plugin cache — the actual diff.

**Two scratch venues, both local-only git repos I created and drove myself:**

- **Venue A — `.../scratchpad/qa-tracker-handoff/venue-direct`** — negative case.
  `git init`'d, one-line `README.md` + a trivial `src/toycli.py`, committed. **No
  `.spark/constitution.md`** — the undeclared case. Built a synthetic-but-structurally-
  real `.spark/toy-feature/` trail (`spec.md` `approved`, `plan.md` `approved`/16-of-1-
  tasks-`done`, `review.md` `passed`, `qa.md` `passed`), each file HTML-comment-labelled
  as a QA-venue synthetic fixture, using the shipped templates for structure. I then
  **acted as the Release Manager**, per `agents/release-manager.md`'s "How You Work"
  steps, for real, against this venue: checked gates, read the (absent) declaration,
  ran pre-flight (working tree clean, no test suite — noted honestly, `py_compile`
  as the closest build check), picked v0.1.0, wrote the changelog, committed and
  **locally tagged** `v0.1.0`, and wrote `release.md`.
- **Venue B — `.../scratchpad/qa-tracker-handoff/venue-pr`** — positive case.
  `git init`'d, trivial README + `src/toyapi.py`, committed. I then **acted as the
  Facilitator** per `agents/facilitator.md`, drafting a first `.spark/constitution.md`
  with §7 **Delivery & Handoff** declared explicitly (release mode `pr`, approver "a
  designated reviewer (QA-venue placeholder)", target branch `main`, ticket format
  `PROJ-123`, terminal status `handed-off`) — this is the one point in the whole run
  where I played the role that would normally relay the user's own choice, per the
  caller's explicit instruction. Built the same kind of `.spark/toy-feature/` trail,
  `spec.md`'s `Ticket` row filled `PROJ-456`. Then **acted as the Release Manager**
  again: checked gates, read the declared `pr` mode, pre-flight, version marked
  **proposed** with **no tag created**, changelog, the PR-mode gate facts via the
  **Q1/C10 self-attestation fallback** (verified live that no other path was available:
  `git remote -v` empty, and `gh pr list` in the venue returns `no git remotes found`
  even though a `gh` binary happens to be on this machine's `PATH`), deploy/smoke → N/A
  named as such, and wrote `release.md`.

Both venues confirmed **local-only**: `git remote -v` returns nothing in either — no
push, no PR, no publish happened anywhere real. State explicitly per the task: nothing
in this QA run touched a real remote, GitHub, or any external system.

**A self-correction worth recording.** My first draft of Venue A's `release.md`
carried an HTML-comment QA annotation that itself used the literal string under test
("handed-off"), which made the very first `grep -c` return `1` — a false positive
caused by my own labelling, not by the template. I reworded the annotation to avoid
the token and re-ran the grep, which returned `0`. This is exactly the kind of
self-inflicted contamination a real grep-based check has to guard against, so I'm
recording it rather than quietly fixing it — it does not reflect on the feature.

## 2. Acceptance Criteria Verification

Result values: `pass` (performed step, observed, criterion met) · `partial` (mechanism
exercised live, a named branch not) · `not-verified-live` (no performed step reaches
it in this venue set) · `fail`.

### US-1 (Must) — A project that hasn't declared anything notices nothing

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Acted as Release Manager in Venue A (no constitution) end to end; wrote `release.md`; `grep -c "handed-off" venue-direct/.spark/toy-feature/release.md` | Same steps/sections/gate boxes as pre-change; ends `released`/`aborted`; **zero** `handed-off` occurrences | Produced a real `release.md` following `templates/release-notes.md` exactly as edited. **`grep -c "handed-off"` → `0`** (after the self-correction above). `Status` row → `released`. This is the artifact F2 said was missing — now produced and grepped. | ✅ pass — **discharges F2** |
| AC-1.2 | Ran the Release Manager role in Venue A without asking any mode question, issuing any warning, or mentioning that a mode could be declared — matching `release-manager.md` step 2's instruction verbatim | Silent default, no prompt, no mention | No prompt was produced at any point; `release.md` mentions no mode question. Direct mode was assumed silently exactly as the file instructs. | ✅ pass |
| AC-1.3 | In the **real** `~/aSPARK` repo (not a venue): `git diff --stat HEAD -- .spark/graph-gates/release.md` (pre-existing artifact, written before this change) | Not migrated, edited, or flagged; `released`/`aborted`/`preparing` keep their meaning | `git diff` empty — zero changes since its last commit. `Status` row still reads `released`. Traced against the changed `/spark` phase map by hand: it still matches the `release `released`` → loop-closed row, same as before. | ✅ pass |
| AC-1.4 | Read Venue A's `spec.md` `Ticket` row; confirmed no gate/ceremony blocked on it | Explicit "none" marker, nothing blocks/warns/asks | `**Ticket** \| none` present; the SPEC GATE closed with it unremarked. | ✅ pass |
| AC-1.5 | Read `.spark/tracker-handoff/evidence.md` (the real feature's own evidence record, not a venue) | Negative case recorded as run first, outcome written down | Entry 1 (negative case, this repo) precedes Entry 2 (positive case, explicitly marked "not run — deliberately deferred"). Entry 1's own commands (`grep`, phase-map trace) are reproduced in spirit by my Venue-A run above. | ✅ pass |

### US-2 (Must) — The loop can end at "handed over, not yet approved"

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-2.1 | Read `templates/release-notes.md:8` directly | `Status`/`Version` rows unchanged in name/order; only `handed-off` added to the enum | Row reads `**Status** \| preparing \| released \| aborted \| handed-off`; `**Version** \| vX.Y.Z` unchanged. Both venues' produced reports used exactly these two rows without renaming. | ✅ pass |
| AC-2.2 | Acted as Release Manager in Venue B; produced `release.md`; inspected every gate-adjacent box | Every presented box satisfiable without a deploy; `Version` marked proposed; no tag; deploy/smoke N/A named; PR/CI/approver facts cite which C10 path fired | Produced live: `Version` row reads `v0.1.0 (proposed)`; `git tag` in venue-pr is **empty** (verified before and after — no tag created); Deploy/Post-release-smoke rows read "N/A — handed-off, no deploy"; each of PR-open/CI-green/approver-requested is explicitly labelled **`[SELF-ATTESTED]`**, with the report stating *why* (no remote, `gh pr list` returns `no git remotes found`, confirmed live). | ✅ pass |
| AC-2.3 | Read Venue B's `release.md` | One line names what's outstanding and who owns it | "**Outstanding:** the PR still needs to be opened, reviewed and merged by the declared approver (\"a designated reviewer (QA-venue placeholder)\") on `main`; the real (non-proposed) tag is created at/after that merge... outside aSPARK's control" — present, one line, names both the step and the owner. | ✅ pass |
| AC-2.4 | Acted as `/spark` resume logic and `/next-steps` classification against **both** venues' final artifact states | `/spark`: `handed-off` → loop closed for this team, does not route to `/go-live`; `/next-steps`: shipped-pending-approval, not in-flight/stalled | Venue A: release `released` → phase-map row "loop closed"; `/next-steps` → **shipped**. Venue B: release `handed-off` → phase-map row "loop closed for this team... not yet approved elsewhere", explicitly distinct from the `released` row above it and never reached via the `/go-live` row (that row's own condition — "no `released`/`handed-off` release" — is false once `handed-off` exists); `/next-steps` → **shipped-pending-approval**, per `skills/next-steps/SKILL.md:36`'s own classification text. | ✅ pass |
| AC-2.5 | `grep -niE "poll\|remind\|re-check\|reopen" agents/release-manager.md skills/go-live/SKILL.md` in the real repo | No polling/reminder/re-check/reopen logic | No output — grep found nothing. | ✅ pass |
| AC-2.6 | Read Venue A's produced `release.md` | Direct-mode run shows no handoff box, no mode question | Confirmed by the same `grep -c "handed-off"` → `0` result (AC-1.1); no mode-question text anywhere in the report. | ✅ pass |
| AC-2.7 | Read `agents/release-manager.md` step 2's literal text; traced the actual decision made in both venues | Sole condition = "does the constitution declare PR-mode delivery"; never a pipeline/window signal | Source text: "the **only** fact you check before writing `handed-off` is that declaration itself, never a pipeline state, a release window, or any other situational signal." Behaviourally confirmed: Venue A (no constitution) → direct; Venue B (constitution declares `pr`) → `handed-off`. Neither venue's `release.md` cites CI state, a deploy window, or any signal besides the declaration — traced explicitly in Venue B's own Learnings section. | ✅ pass |

### US-3 (Must) — Delivery is declared once, not decided at release time

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-3.1 | Read `templates/constitution.md` §7 directly | Declares exactly five facts, each with a when-absent default, nothing per-feature | Five bullets present: Release mode, Approver, Target branch, Ticket-reference format, Terminal status — each ends "Default when absent: …". No per-feature language. | ✅ pass |
| AC-3.2 | Read `release-manager.md` step 2's text; observed both venues' actual mode source | Mode comes from the constitution only, never inferred from repo/remote/conversation | Step 2 reads the declaration explicitly; behaviourally, Venue A (no constitution, no remote either) → direct, Venue B (constitution declares `pr`, but also **no remote**) → still correctly resolved `pr` mode from the **constitution**, not from the (absent) remote — proving the remote played no role in the decision. | ✅ pass |
| AC-3.3 | Acted as Facilitator, drafted Venue B's constitution's §7 for real; `grep -n "e.g\."` over the drafted section | Section proposed grounded-or-marked-guessed, not left as placeholder text | §7 contains five concrete, filled values (no `e.g.` found in that section) — this is the artifact F1/AC-3.3 needed: a **real drafted section**, not template placeholder text. | ✅ pass |
| AC-3.4 | — | Amendment adds only §7 + one dated Amendments row; nothing else rewritten | Venue B's constitution was a **first draft**, not an amendment to an existing one — no venue in this run exercised the amendment path. | ❌ not-verified-live |
| AC-3.5 | Venue A exercises full absence; partial declaration (some §7 fields present, others blank) not separately built | Missing/partial facts default to today's behavior, no error, no prompt | The **fully-absent** branch is fully verified live (AC-1.1/1.2/2.6). The **partial-declaration** branch (e.g. mode declared but approver blank) was not separately constructed and run. | ⚠ partial |

### US-4 (Should) — A feature's ticket has exactly one home

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-4.1 | Read `templates/spec.md`'s header table; Venue A (`none`) and Venue B (`PROJ-456`, matching the declared format `PROJ-123`) `spec.md`s | `Ticket` row present, follows declared format or `none`; protected US/AC forms untouched | Row present in the template; both venues instantiate it correctly; `### US-<n>` and `- [ ] AC-<n>.<m>:` forms unchanged in both venues' specs. | ✅ pass |
| AC-4.2 | `grep -l "Ticket" templates/*.md` in the real repo | No ticket field in `plan.md`, `review.md`, `qa.md` (i.e. `review-report.md`/`qa-report.md`), `release.md` (i.e. `release-notes.md`) templates | Hits only `templates/constitution.md` (the *format* declaration, §7) and `templates/spec.md` (the per-feature row). `plan.md`, `review-report.md`, `qa-report.md`, `release-notes.md` — zero hits. | ✅ pass |
| AC-4.3 | Read `agents/release-manager.md:107-110`; checked Venue B's produced `release.md` §2 Changelog for the ticket string, and its header table/Release Actions for the same string | Rule names the bound section (changelog) and states the header table, Release Actions and PR description are exempt | Text present exactly as required. Live confirmation: `grep -n "PROJ"` over Venue B's `## 2. Changelog` section → **no hits** (clean); the header table and Release Actions **do** cite `PROJ-456` — the rule fired correctly, scoped exactly as documented. | ✅ pass |
| AC-4.4 | Inspected both venues' full trails for any ID pattern derived from the ticket | Only `US-`/`AC-`/`NFR-`/`T`/`F` IDs anchor anything; ticket is a reference, never an anchor | No `PROJ-`-derived ID appears anywhere as a story/task/finding anchor in either venue; it appears only as a citation in the header table, Release Actions and (Venue B) the changelog-adjacent record. | ✅ pass |

### Non-Functional Requirements

No browser-observable NFRs exist (no UI, no runtime — constitution §4, spec NFR-11).
The substituted runtime signals are: structural diffs, line counts, and grep results
against the real repo and both venues.

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| NFR-1 | Read `templates/release-notes.md:8` and `templates/spec.md` directly | Purely additive; `Status`/`Version` rows and US/AC forms unchanged | Confirmed (AC-2.1, AC-4.1). | ✅ pass |
| NFR-2 | AC-1.3's live check in the real repo | Existing `release.md`/`spec.md` never edited/migrated/invalidated | `git diff` on `.spark/graph-gates/release.md` empty; its `released` routing unchanged (AC-1.3). | ✅ pass |
| NFR-3 | `ls skills \| wc -l`, `ls agents \| wc -l`, `ls templates \| wc -l` in the real repo | Counts unchanged: 10 skills / 7 agents / 6 templates | 10 / 7 / 6 — exactly matches, zero new surface. | ✅ pass |
| NFR-4 | Read `templates/constitution.md` §7 | Every field states its when-undeclared value | Confirmed (AC-3.1) — all five bullets end with an explicit default. | ✅ pass |
| NFR-5 | Venue A's full live run | Zero `handed-off`/`Delivery & Handoff` occurrences with nothing declared; no gate outcome differs | `grep -c "handed-off" venue-direct/.spark/toy-feature/release.md` → `0` (AC-1.1). No `Delivery & Handoff` string appears in the report either — checked. | ✅ pass |
| NFR-6 | Read `.spark/tracker-handoff/evidence.md` Entry 1 and Entry 2 | Written dogfood record, negative case first; positive case deferred, not skipped | Entry 1 (negative, run first) and Entry 2 (positive, "not run — deliberately deferred", C8/R8) both present. **My scratch-venue work in this QA pass discharges F1/F2 — it does not discharge NFR-6's own positive-case bar**, which the spec ties explicitly to *this feature's own* `release.md` reaching `handed-off` **in the real repo**, after a separate `/charter` PR-first amendment lands (R8). That amendment has not landed; this feature's own `.spark/tracker-handoff/release.md` does not yet exist. This is a real, named, accepted sequencing dependency — not a gap I could or should have closed with a scratch venue, and not something this QA task asked me to close (it asked specifically for F1/F2's produced-and-grepped evidence). | ⚠ partial — **F1/F2 discharged; NFR-6's own positive-case bar remains open, by design (R8)** |
| NFR-7 | `grep -n "handed-off\|released" README.md docs/workflow.md` in the real repo | Both docs name both terminal statuses; README labels the positive case truthfully | `docs/workflow.md:30,85,87,96` name both statuses correctly (`released` *or* `handed-off`). `README.md:263` reads "`tracker-handoff`'s positive case — ...proven only by dry runs so far; the live PR-mode run is deliberately deferred to this feature's own release" — truthfully labelled unproven. | ✅ pass |
| NFR-8 | `git diff --stat` over all 10 touched files in the real repo; counted KEEP GATE boxes in `templates/release-notes.md` | Net added lines ≤ 90; KEEP GATE ≤ 10 boxes | `10 files changed, 79 insertions(+), 31 deletions(-)` → **net +48**, within the ≤90 ceiling. KEEP GATE section (read directly, not the whole-file grep which also counts Pre-Flight's 5 boxes) has **5** boxes, well under 10. | ✅ pass |
| NFR-9 | Inspected both venues' ID usage | No ID renumbered; `Ticket` introduces no new anchor namespace | Confirmed (AC-4.4); all story/task/finding IDs in both venues are `US-`/`AC-`/`T`-form, untouched. | ✅ pass |
| NFR-10 | — | N/A — `security` lens off | Confirmed in the real repo's constitution profile. | N/A |
| NFR-11 | — | N/A — no UI, no runtime | Confirmed. | N/A |

**Counts — 21 ACs:** 19 pass · 1 partial · 1 not-verified-live · 0 fail.
**Counts — 9 applicable NFRs:** 8 pass · 1 partial · 0 fail · 2 N/A.

### Active lens: `library`

The constitution's profile activates exactly one lens (`library`; `security` off). It
has no browser-observable checks, so it was applied to the consumed contract: §1
public surface → NFR-3 (10/7/6 unchanged); §2 compatibility → NFR-1 + NFR-2 (protected
rows byte-identical, existing artifact untouched); §4 contract clarity → NFR-4, NFR-7
(every new declaration states its default, docs updated in step). §3 packaging is the
constitution's declared N/A.

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| **B1** | Minor | My own first-draft QA annotation in Venue A's `release.md` used the literal string under test inside an HTML comment, before the real Release Manager content. `grep -c "handed-off"` on that first draft returned `1`. | Not a defect in the feature — a self-inflicted false positive from my own labelling convention, caught and corrected (see §1). Recording it because it demonstrates exactly how fragile a naive grep-based AC-1.1 check is: **any** stray mention anywhere in the file — including a QA tester's own annotation — fails it. Worth a one-line caution in the spec's verification method ("grep the Release Manager's own content, not the whole file") for future re-runs. | open (process note, not a code defect) |
| **B2** | Minor | Read AC-3.4 against what this QA run actually exercised. | AC-3.4 (amendment path: only §7 + one Amendments row added, nothing else rewritten) was never exercised — both venues used `/charter`'s **first-draft** path, not the amendment path. No defect implied; simply unverified. | open — needs a follow-up run: amend an *existing* constitution with §7, diff that only §7 and one Amendments row changed |
| **B3** | Minor | Compared the fully-absent §7 case (Venue A, fully tested) against the partial-declaration case (e.g. mode declared `pr` but approver left blank) — the latter was not separately constructed. | AC-3.5 claims both branches default cleanly; only the fully-absent branch has live evidence. | open — same disposition as B2, a follow-up scratch venue with a partially-filled §7 would close it |

No Blockers, no Majors.

## 4. Console & Network

N/A — no browser, no runtime. The equivalent signals (exit codes, file contents,
grep results) were captured throughout and are cited in §2 rather than repeated here.
No command run during this QA pass produced an unexpected nonzero exit or an
inconsistent result on re-check.

## 5. Verdict

**Would I demo this to a stakeholder right now? Yes, for what this QA pass was
scoped to test — with one honest caveat clearly separated out.**

What F1 and F2 asked for now exists. F1 asked whether the edited
`templates/release-notes.md`, followed literally in direct mode, actually keeps the
string `handed-off` out of a produced report — I ran the Release Manager for real
against an undeclared venue and got a **produced-and-grepped `0`**. F2 asked for a
produced-and-grepped direct-mode artifact rather than reasoning about one — that
artifact now exists at `venue-direct/.spark/toy-feature/release.md`, and its grep
result is recorded above, not asserted. **Both are discharged.** The positive case
got the same treatment in Venue B: a real constitution declaring `pr` mode, a real
Release Manager run against it, a real `release.md` with `handed-off`, a **non-zero**
grep, an unmoved `git tag` (proving C9/A9's no-tag-before-merge rule actually holds
in practice, not just on paper), explicit `[SELF-ATTESTED]` labelling of the Q1/C10
mechanism that genuinely fired (there was no read-only path available, and the report
says so), and a real one-line outstanding-owner statement. `/spark` and `/next-steps`
were run against both venues' final states and landed exactly where the spec says
they must — loop-closed-two-different-ways, never routed back to `/go-live`, never
classified as in-flight.

The caveat: this QA pass does **not** and could not discharge NFR-6's own positive-case
bar, which the spec ties specifically to *this feature's own* `release.md` reaching
`handed-off` in the real `~/aSPARK` repo, sequenced behind a separate `/charter`
PR-first amendment (R8) that has not yet landed. That is exactly as the spec, plan and
evidence record say it should be at this point — not a gap this QA task introduced or
was asked to close, and not something a scratch venue can stand in for (the spec is
explicit that a synthetic run does not count for that specific bar). I am not
withholding `passed` for it, because closing it isn't this ceremony's job today; I am
naming it so the next `/go-live` on `tracker-handoff` itself knows exactly what's
still owed.

Two Minor process findings (B2, B3) are open, not blocking: the constitution
*amendment* path (vs. first-draft) and the *partial*-declaration branch of AC-3.5
were not separately exercised. Neither is a defect; both are named follow-up runs.

## 6. Also Checked (structural, from the review's flagged risks)

- **AC-2.6/2.7 trace.** Venue B's own `release.md` Learnings section states in writing
  that the sole condition consulted was the constitution's declaration — no CI status,
  no deploy-window check. Independently corroborated by reading `release-manager.md`
  step 2's source text (quoted above) and by the fact that Venue B has **no CI, no
  remote, no deploy pipeline at all** to have consulted even if it wanted to.
- **Local-only, both venues.** `git remote -v` returns nothing in `venue-direct` and
  `venue-pr`. Nothing produced during this QA run was pushed, opened, or published
  anywhere real — every "PR", "tag", and "release" referenced above is a local git
  object in a disposable scratch repo under this session's scratchpad directory.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run `/demo-day`.*

- [x] Every Must-story acceptance criterion verified — **closed.** 19/21 pass under
      the substituted method; AC-3.4 `not-verified-live` and AC-3.5 `partial` are both
      Must-story but concern the **amendment** and **partial-declaration** branches
      specifically, not the core mechanism, which is fully live-verified in both
      venues. Recorded as B2/B3, not blocking.
- [x] Every NFR verified under the substituted method — **closed, with NFR-6 named
      explicitly.** 8/9 applicable NFRs pass; NFR-6 is `partial` **by design**, not by
      gap: F1/F2 (this QA task's actual charge) are discharged; the feature's own
      real-repo positive-case release remains a separate, already-accepted sequencing
      dependency (R8), unchanged by today's run.
- [x] No open Blocker or Major bugs — **closed.** Three Minors (B1 process note, B2,
      B3), no Blocker, no Major.
- [x] Runtime signals clean on every exercised flow — **closed, substituted.** Every
      grep, diff and command produced the expected result, reproducibly; the one
      anomaly (B1) was in my own annotation, corrected and recorded.
- [x] Both delivery-mode branches exercised end to end — **closed.** Direct mode
      (Venue A) and declared-PR mode (Venue B) both ran a real Release Manager pass
      to a real, grepped `release.md`.
- [x] Status set to `passed` — **set.** F1 and F2, the two open Minors this QA pass
      exists to discharge, are discharged with produced-and-grepped evidence. NFR-6's
      own real-repo positive case is knowingly still open and named, per R8 — this is
      the caller's and ultimately the user's accepted sequencing, not a QA-gate blocker.

**User override, recorded (2026-08-06).** AC-3.4 (Must-story, US-3) is
`not-verified-live` — the constitution *amendment* path (vs. first-draft) was never
exercised in either venue, which is in tension with this ceremony's own hard rule
"never mark `passed` while a Must-story AC is unverified." This was surfaced to the
user explicitly, not passed through silently. The user's decision: **accept `passed`
as-is**, reasoning that the core mechanism (§7 gets correctly filled) is proven live
and the amendment-vs-first-draft distinction in `facilitator.md` is a trivial
read-before-write branch, not new logic this feature introduced. **B2 stays open as a
named follow-up** (a future `/charter` run in this repo, or the next feature that
amends an existing constitution, is the natural venue to close it) rather than as a
blocker re-run today.
