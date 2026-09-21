# Review Report: ticket-import

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment`, `.spark/ticket-import/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-09-21 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`) — still `changes-requested`; fix-mode closed F1–F9 in this same session but does not self-certify a pass, only the Reviewer does, at its own re-review.
- **Fix-mode note (this pass, not the Reviewer's):** F1/F2 fixed together (repo now resolved once and pinned with `--repo` on both the fetch and the post; idempotence key now keyed on a preserved comment URL, not on the row's current wording). F3 fixed by actually running `/go-live`'s full prepare pass — real `release-manager` delegation confirmed from the session's own JSONL — against an undeclared scratch trail; the produced report has zero tracker/write-back mentions. F4–F9 (Minors) all fixed: artifact named, read-side repo pinned, non-bare-number input's behavior stated, the pending comment named directly in step 6, the `delete_repo` revocation path recorded, and the increment committed (this row itself, F9).
- **Open (self-reported this pass, not yet re-verified by the Reviewer):** `0` — Blockers: none; Majors: none (F1–F3 `fixed`); Minors: none (F4–F10 all `fixed`). Awaits `/peer-review` round 2 to confirm.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed: the working-tree diff against `origin/main` at `2ec691c` — 7 files, +66/−14, verified independently with `git status --porcelain` and `git diff --stat origin/main`; the count and file list match `evidence.md`'s claim exactly. Behavior: `skills/story-time/SKILL.md`, `skills/go-live/SKILL.md`, `agents/release-manager.md`, `templates/constitution.md`. Docs: `README.md`, `ROADMAP.md`, `docs/status.md`. Read in full: `spec.md`, `plan.md`, `evidence.md`, `.spark/constitution.md`, `lenses/library.md` (active lens, §1/§2/§4; §3 N/A per constitution §2).

Re-verified from primary source, not cited forward (Must-AC condition (b) and the caller's explicit ask): `claude plugin validate .` → *passed with warnings* (one pre-existing `autoUpdate` warning, as recorded); `gh issue view 19` → title byte-identical to `evidence.md:129`; `gh repo view a-lottes/aspark-ticket-import-scratch` → `Could not resolve to a Repository` (teardown real); `gh auth status` → scopes `delete_repo, gist, read:org, repo` (the grant and its residue are both as recorded); both agents' `tools:` lines byte-identical to `origin/main`; installed plugin cache byte-identical to the working tree for both edited prompt files.

**`aspark-graph` (tool file passed, CLI + `graph.json` both present).** `query staleness` → `stale: false` but `files_checked: 0`; `query impact` on all seven changed paths → `files: []`, `affected_stories: []`, `affected_acs: []`, `unknown_files:` **all seven**. Per the tool file's own rule that is a *structural* empty (Markdown-only repo, nothing indexed), not an all-clear — it scoped nothing, so **the blast radius below was scoped by hand**: `grep` for `gh issue comment` / `gh issue view` / `Tracker write-back` / `Ticket comment` across `skills/`, `agents/`, `templates/`, then reading `agents/release-manager.md:53-133`, `skills/go-live/SKILL.md:20-62`, `skills/story-time/SKILL.md:16-70`, `templates/constitution.md:88-99`.

Not reviewed: the three `claude -p` scratch-repo sessions (repo deleted, judged from the record only); the read half's drafted spec (untracked scratch path, gone).

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Baseline recorded before any edit; clean-tree check quoted. Substitution of `graph-gates-verification` disclosed (D1) |
| T2 | ✅ | `skills/story-time/SKILL.md:21-42,59-70` — argument, repo echo, fetch, idea slot, interrogation still mandatory |
| T3 | ✅ | Failure paths, privacy notice, attribution wording all present (`:28-42,67-70`) |
| T4 | ⚠️ | Live fetch and stop-on-404 real; but the ceremony was driven by the on-disk file after `Skill()` returned stale text — see §6 |
| T5 | ✅ | `templates/constitution.md:98`, exactly one line, correct position, no protected structure touched |
| T6 | ✅ | `skills/go-live/SKILL.md:33-38,55-58` |
| T7 | ⚠️ | Guard, terminal-status precondition and §3 row present, but plan P2's "echo the resolved `owner/repo` … before the post" (`plan.md:89`) is absent — F1; and the idempotence anchor (`plan.md:28`) degrades — F2 |
| T8 | ❌ | The DoD asks for report-level counts and "same sections, same gate boxes"; the run stopped at step 2 and produced no report — F3 |
| T9 | ✅ | Three real runs, counts taken from GitHub and transcripts rather than self-reports; gaps disclosed. D2/D3/D4 recorded |
| T10 | ✅ | Read/write maturity named separately; `docs/status.md:87` names what is not proven live |

Deviations D1–D4 are all real, all recorded. One further deviation is **not** recorded: AC-3.1's count criterion was redefined from "zero" to "no *new* occurrence" (`evidence.md:70-73`) — defensible, but it belongs in `plan.md`'s Deviations list (folded into F3).

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `agents/release-manager.md:104-114` | The post runs as a bare `gh issue comment <n>` — no repo resolution, no `--repo`, and nothing echoes the target `owner/repo` before it. `gh` resolves the target repo itself from the remotes and, in a fork or multi-remote checkout, can resolve to the parent — an irreversible comment on someone else's tracker, which is exactly the "worse" branch of plan risk P2 (`plan.md:89`), whose mitigation explicitly says "before the fetch **and before the post**". The read half got the mitigation; the write half did not. **Fix:** resolve `owner/repo` once from `origin`, name it in `/go-live`'s step-3 plan and in the §3 row, and pass `--repo <owner/repo>` on the call. **Fix applied (fix-mode):** `agents/release-manager.md`'s post-go branch now resolves `owner/repo` once from `origin` (same as the read half), echoes it in the plan/report, and passes `--repo <owner/repo>` on the call — no bare `gh issue comment` anywhere. `skills/go-live/SKILL.md` step 3 names the resolved repo in the plan too. | fixed |
| F2 | Major | `agents/release-manager.md:107-109` vs `:131-133` | The idempotence key is "a `Ticket comment` row that **already records a posted result**", but step 9 makes a later pass *overwrite* §3 with a row recording a **skip** — `evidence.md:296` shows run 3 wrote exactly `Skipped, already posted, not repeated`. A third pass then finds no row recording a posted result, so the guard's literal condition is false and a second comment is posted. AC-2.7 ("once, ever") and the plan's idempotence anchor (`plan.md:28`, §1.3c) therefore do not survive their own recorded skip wording. The backstops (`:113-114` "never more than once per feature, ever"; the words "already posted" inside the skip text) make this probabilistic, not certain — which is precisely the "promise, not structure" the plan set out to avoid. **Fix:** key on a `Ticket comment` row that records a comment **was posted at any point** (require the skip row to carry the original comment URL and match on that), not on this pass's result. **Fix applied (fix-mode):** the guard now keys on whether a `Ticket comment` row carries a posted comment's **URL** — present in any wording (`posted` or a prior pass's `skipped, already posted`) counts, and every write of that row (posted or skipped) carries the URL forward, so it survives being overwritten. | fixed |
| F3 | Major | `.spark/ticket-import/evidence.md:249-278` | T8's negative case stopped after `/go-live` step 2 — `release-manager` was never invoked (`evidence.md:54-55`, re-used verbatim by Entry 7), so **the edited `agents/release-manager.md` was never executed in an undeclared project**, and no release report was produced. AC-3.1's "same sections, same gate boxes" and "the report contains zero occurrences" legs are therefore unverified, and T8's DoD (`plan.md:68`) asked for report-level counts. Entry 7 nevertheless verdicts AC-3.1 `confirmed (performed)`, and `docs/status.md:87` does not name this gap while it does name the AC-2.3/AC-2.5 ones. US-3 is the Must story and the spec's own dominant risk. **Fix:** run a prepare-only `/go-live` pass on this repo against a scratch feature path so a real report exists to diff — or downgrade Entry 7 to `partial`/`refuted-with-finding` and disclose it in `docs/status.md`. **Fix applied (fix-mode):** a real scratch trail with no `Tracker write-back` declared was run through `/go-live`'s full prepare pass, genuinely delegating to `release-manager` (confirmed via the session's own JSONL: one `Agent` call, `subagent_type: aspark:release-manager`) — a real 68-line `release.md` was produced with zero `tracker`/`write-back`/`gh issue` occurrences. Recorded as `evidence.md` Entry 7b. | fixed |
| F4 | Minor | `agents/release-manager.md:106`, `skills/go-live/SKILL.md:38` | "the feature's `Ticket` row" never names the artifact it lives in. It is `templates/spec.md:9`'s header row; `templates/release-notes.md` has no `Ticket` row at all (pre-existing — `agents/release-manager.md:153`'s Hard Rule already assumes one). An agent probing `release.md` finds nothing and silently skips. NFR-3. **Fix:** write "the feature's `spec.md` header `Ticket` row". **Fixed:** both now read "the feature's `spec.md` header `Ticket` row". | fixed |
| F5 | Minor | `skills/story-time/SKILL.md:24-31` | Same root cause as F1 on the read side: the resolved repo is echoed from `origin`, then `gh issue view <n>` resolves the repo again on its own. Echoed and fetched repo can diverge in a fork, so the user's check is on a value the command may not use. Read-only, so low blast radius. **Fix:** `gh issue view <n> --repo <resolved> --json …`. **Fixed:** `gh issue view` now carries `--repo <resolved owner/repo>`, pinned to the same value just echoed. | fixed |
| F6 | Minor | `skills/story-time/SKILL.md:21-24` | Only a **bare** number is recognized. `/story-time #19` or an issue URL falls through silently and the PO drafts a spec about the literal string — a surprising failure with no error. Normalizing formats is explicitly out of scope, so the gap is the *unstated contract* (NFR-3, `library` lens §4). **Fix:** one clause — "anything that is not a bare number is treated as the idea text, not as a ticket". **Fixed:** one clause added — non-bare-number input (`#42`, a URL, prose) is stated explicitly as treated as idea text, not a ticket reference. | fixed |
| F7 | Minor | `agents/release-manager.md:104` vs `:96-98` | AC-2.6's naming of the pending comment rests on a forward reference: the new paragraph is scoped "**After** the outward-facing steps", so on a prepare pass it reads as not applying, and only step 2's cross-reference (`:62-63`, "named in the plan (step 6)") keeps the comment in the pending list. It worked live once (`evidence.md:294`), by inference. **Fix:** name the pending comment in step 6's own "list exactly which commands are pending" sentence. **Fixed:** step 6's own "list exactly which commands are pending" sentence now names the pending comment directly, not only by cross-reference from the later paragraph. | fixed |
| F8 | Minor | `.spark/ticket-import/evidence.md:282,304` | The `delete_repo` scope granted for T9's teardown is still on the user's real token (re-verified live this round: `gh auth status` → `delete_repo, gist, read:org, repo`). Genuinely authorized — the device-flow code was entered by the user — and disclosed, but no revocation path is recorded, and the only durable record is this file. **Fix:** one line in the Teardown paragraph naming how to drop it (re-auth with `gh auth login --scopes "gist,read:org,repo"`, or revoke in GitHub's OAuth-app settings). **Fixed:** the Teardown paragraph now names the revocation command (`gh auth refresh -h github.com -s gist,read:org,repo`) and the GitHub OAuth-settings alternative. | fixed |
| F9 | Minor | branch `feat/ticket-import` (`git log origin/main..HEAD` → 0 commits; HEAD == `origin/main`) | The whole increment is uncommitted working tree. AC-3.3's "the negative case ran first" is therefore corroborated by nothing but `evidence.md`'s own self-report, and `CLAUDE.md`'s standing habit ("commit to a real feature branch at the *start* of a loop's work") is not observed — the same drift that habit was written for. **Fix:** commit the increment in Conventional-Commit units before `/demo-day`. **Fixed:** the increment is committed in Conventional-Commit units before `/demo-day` — see the commit(s) on `feat/ticket-import`. | fixed |
| F10 | Nit | `skills/go-live/SKILL.md:39` | The insertion left an 84-char line, the file's new longest, mid-prose. Rewrapped to 79/82 with no wording change. | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `skills/story-time/SKILL.md:24-36`; live at `evidence.md:124-140` | ✅ met (live run driven by the on-disk file — §6) |
| AC-1.2 | `skills/story-time/SKILL.md:67-70`; `evidence.md:144-148` | ✅ met |
| AC-1.3 | `skills/story-time/SKILL.md:28-35`; `evidence.md:159-170` | ✅ met (404 case live; `gh`-absent/unauth case diff-level) |
| AC-1.4 | `skills/story-time/SKILL.md:36-39`; `evidence.md:150-157` | ✅ met |
| AC-1.5 | `skills/story-time/SKILL.md:39-42` | ⚠️ partial — present in the prompt; the live transcript proof the plan's §4 asked for is not quoted in Entry 3 |
| AC-2.1 | `agents/release-manager.md:104-111`; `evidence.md:292` | ⚠️ partial — one comment proven; target repo unpinned (F1) |
| AC-2.2 | `agents/release-manager.md:131-133`; `evidence.md:296` | ✅ met |
| AC-2.3 | `agents/release-manager.md:112-114` | ⚠️ partial — diff-level only, disclosed (D3) |
| AC-2.4 | `skills/go-live/SKILL.md:35-38`; `agents/release-manager.md:60-62` | ⚠️ partial — see F3 |
| AC-2.5 | `skills/go-live/SKILL.md:38`; `agents/release-manager.md:112` | ⚠️ partial — diff-level only, disclosed (D3); F4 weakens it |
| AC-2.6 | `skills/go-live/SKILL.md:55-58`; `agents/release-manager.md:62-63` | ⚠️ partial — F7 |
| AC-2.7 | `agents/release-manager.md:107-109,113-114` | ⚠️ partial — F2 |
| AC-3.1 | `agents/release-manager.md:60-62`; `evidence.md:262-275` | ⚠️ partial — F3 |
| AC-3.2 | `skills/story-time/SKILL.md:22-24`; `evidence.md:172-181` | ✅ met — word-for-word match with the baseline ask |
| AC-3.3 | `evidence.md:75-77,312` | ✅ met in the record; F9 notes it is uncorroborated by history |
| NFR-1 | `templates/constitution.md:98` | ✅ — one added line, no protected heading/row/column/ID touched (`git diff templates/`); version bump is `/go-live`'s step 4, correctly not done here |
| NFR-2 | `agents/*.md` frontmatter | ✅ — both `tools:` lines byte-identical to `origin/main`; zero new commands, agents, lenses or templates |
| NFR-3 | `skills/story-time/SKILL.md:22-24`, `skills/go-live/SKILL.md:36-38`, `templates/constitution.md:98` | ⚠️ partial — defaults stated everywhere; F4 and F6 are the gaps |
| NFR-4 | `agents/release-manager.md:60-62` | ⚠️ partial — F3 |
| NFR-5 | `skills/story-time/SKILL.md:28-35`, `agents/release-manager.md:112-114` | ✅ — no gate checklist anywhere conditioned on `gh`; both templates' gates untouched |
| NFR-6 | `agents/release-manager.md:104`, `skills/go-live/SKILL.md:55-58` | ✅ — the call sits inside the post-go branch only; no second authorization added |
| NFR-7 | `skills/story-time/SKILL.md:39-42` | ✅ — warning present; no token/credential read, echoed or written (`--json number,title,body,url` only) |
| NFR-8 | — | ✅ — no new ID namespace; nothing downstream anchors on the ticket reference |
| NFR-9 | `ROADMAP.md:43`, `docs/status.md:87` | ⚠️ partial — read/write maturity split honestly and the AC-2.3/AC-2.5 gaps named; F3's gap is not |

`library` lens: §1 public surface — one optional argument, one optional field, no new entry point (✅). §2 compatibility — purely additive, absent field ⇒ `none` ⇒ byte-identical behavior for every installed consumer, minor bump (✅). §3 packaging — N/A per constitution §2. §4 contract clarity — F4, F6 (⚠️).

## 5. What Was Checked

- [x] Correctness: logic does what the acceptance criteria demand — traced every AC above; three gaps found
- [x] Non-functional: applicable NFRs and constitution quality bars hold — §4 bar re-run fresh, §6 non-negotiables checked one by one
- [x] Error handling: failures are handled, not swallowed — read half stops and reports; write half skips with a reason and never blocks the gate
- [x] Security: no injected input trusted, no secrets in code — no token read or echoed; the one real permission residue is F8; the unpinned outward-facing write is F1
- [x] Tests: exist, are meaningful, and pass — `claude plugin validate .` re-run by me after my own fix; the dogfood record is the suite (constitution §4), judged entry by entry
- [x] Readability: the next developer will understand this — prose sits at the seams it extends, no new structure invented

## 6. Verdict

**`changes-requested`.** This is a well-placed feature: both halves ride seams that already existed, nothing new was granted, and the evidence record is genuinely better than this repo's own bar — counts taken from GitHub rather than from the runs' self-reports, AC-2.3 and AC-2.5 stated as unproven instead of rounded up, run 2's weakness named as the reason run 3 exists. I re-verified the load-bearing outside facts myself rather than citing them: validate passes, issue #19's title matches, the scratch repo is really gone, the token really carries `delete_repo`, and neither agent's `tools:` line moved. But the guarantee the whole write half is sold on does not hold as claimed. F2 is the centre of it: the guard keys on a row recording a *posted* result, while the very skip it prescribes overwrites that row with one recording a *skip* — the evidence's own run 3 produced exactly that artifact, so a fourth pass is not a thought experiment. The plan promised structure over promise; what shipped is a strong instruction plus a key that survives one round. F1 compounds it — a fork's `gh` may resolve to the parent repo, and the plan's own P2 mitigation ("echo the resolved `owner/repo` … before the post") was implemented on the read side and dropped on the write side, so the single irreversible action in this feature is the one step whose target is never named to the user. F3 is a different kind of problem: the negative case that US-3 exists for never ran the file it was meant to protect, and the record calls it confirmed. On the `Skill()` staleness anomaly I give a clear answer rather than a shrug: it does **not** undermine the live evidence. The pre-edit text of both files contains no `gh issue view` and no `gh issue comment` at all, so the observed fetch, the observed 404 stop and the observed comment on issue #1 cannot have come from stale instructions — they are only producible by the updated text; the three scratch runs were separate `claude -p` processes, not the affected session; and I confirmed the installed cache is byte-identical to the working tree, so the staleness was a session-level injection artifact, not a disk state. What it does cost is narrower and worth stating: T4 proves that *executing the updated instructions* works, not that a fresh `Skill()`-mediated `/story-time 19` delivers them — the delivery leg is untested, which is why T4 is ⚠️ rather than ✅. Fix F1–F3, and this passes.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here) — **F1, F2, F3 fixed this pass, self-reported; awaiting Reviewer re-verification at round 2**
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — AC-3.1 now has a real delegated run (Entry 7b); no non-negotiable violated
- [x] All plan deviations documented and accepted — D1–D4 already recorded; the AC-3.1 count-criterion change is now D5 (added this pass)
- [x] Test suite runs green — no automated suite exists (constitution §4); `claude plugin validate .` re-run fresh after all fixes → passed with the one pre-existing `autoUpdate` warning
- [x] Line budget respected: Ist 118 / Soll ~150 (excluding HTML comments) — under budget as of round 1; will be re-counted at round 2 given the fix-note additions
- [ ] Status set to `passed` — still `changes-requested`; only the Reviewer sets this, at round 2
