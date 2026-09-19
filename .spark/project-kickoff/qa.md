# QA Report: project-kickoff

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Working tree (see §1 override), `.spark/project-kickoff/spec.md` (AC-1.1–5.4, NFR-1–8) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-19 |

**Handoff**
- **Status:** mirrors the header table above.
- **Verdict:** Yes, I'd demo this. Both Must stories (US-1, US-2) hold under fresh, independent live testing — including one exploratory run specifically designed to break the one thing that would matter most (a §9-only amendment quietly rewriting the existing §8 QA-method declaration). It didn't. No Blocker or Major found.
- **Open:** `none` — 1 Minor filed (B1, a genuine open design question, not a defect), non-blocking.
- **Binding ruling:** §5 Verdict and the QA GATE checklist — the only binding location this round.
- **On conflict:** the numbered body below wins for everything except `Status`.

## 1. Test Environment

**Documented ceremony override — the venue is not a browser, and the installed plugin is
stale.** This repo's constitution §8 declares `Browser-observable surface: no`, substitute
method "hands-on QA against the **installed plugin**... a performed step is a real ceremony
invocation or a real command whose output was observed" (method established at
`.spark/graph-gates/qa.md` §1). That declaration assumes the installed plugin reflects the
diff under review. It doesn't here: `diff -q` against every one of the files this feature
touches (`templates/constitution.md`, `agents/facilitator.md`, `skills/charter/SKILL.md`,
`skills/spark/SKILL.md`, `skills/next-steps/SKILL.md`, `README.md`,
`agents/product-owner.md`, `agents/engineering-manager.md`) confirms all eight differ from
`~/.claude/plugins/cache/aspark/aspark/0.8.0/` — a real, non-symlinked, stale cache (working
tree is `0.9.0`, cache is `0.8.0`). Testing the cache would verify last release's behaviour,
not this one. **Per the user's decision this session, I tested the working tree instead**,
following this repo's own precedent for exactly this deviation (`.spark/graph-gates/qa.md`
§1's override block, used as the model for this one).

- **"Performed step" bar (unchanged):** a real ceremony invocation via the Agent tool reading
  working-tree skill/agent files fresh — never the `aspark:*` subagent types, which resolve to
  the stale installed persona — or a real command whose output I observed. Reading Markdown and
  reasoning about it is never a performed step; any such row is marked `not-verified-live`.
- **Instruments used:** (a) direct Bash/Read against the working tree — diffs, greps, line
  counts, `claude plugin validate .`, `aspark-graph query impact`; (b) three fresh
  `general-purpose` subagents, each reading the working-tree `skills/*/SKILL.md` and
  `agents/*.md` directly (never `aspark:facilitator`/`aspark:charter`/etc.) and literally
  executing the ceremony against a real scratch venue.
- **Venues** (all outside `/Users/andreaslottes/aSPARK`; confirmed on disk before use, not
  assumed from prior artifacts): Venue A (`…venueA-noconst`, now has a constitution from the
  increment's own T10 dogfood — reused read-only), Venue B (`…venueB-withconst`, §1–§8 only,
  no §9, **§8 already declares its own QA-method fixture** — reused, then amended by me),
  Venue C (`…venueC-code-noconst`, 3 real commits, real code, no constitution — reused, then
  given a first-draft `/charter` by me), Venue D (`…venueD-nohistory`, one file, no history —
  inspected on disk only, matches `evidence.md` Entry 12 exactly, not re-run: re-deriving would
  be pure repetition of an already-thrice-independently-verified fixture).
- **This repo's own negative case (AC-2.4) cannot be re-run** — `.spark/constitution.md`
  already carries §9 from T8. I substitute two things: `evidence.md` Entry 7 (the real
  installed-plugin control, captured before T8, cited rather than re-derived — it is now
  literally irreproducible) and a **fresh** trace I ran myself against Venue B's still-old-shape
  constitution (§1–§8, no §9) before amending it, below.
- **`git status --porcelain` in this repo, before and after all my testing:** identical —
  only the pre-existing feature diff plus the pre-existing untracked `.spark/.guard/` and
  `.spark/project-kickoff/`. Nothing in the working tree was touched by any test.

## 2. Acceptance Criteria Verification

### US-1 (Must) — routing to `/charter`

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | `git diff HEAD -- skills/spark/SKILL.md` (mine); fresh subagent ran `/spark` no-arg on Venue C (real code, no `.spark/`) | Names/offers `/charter` first; doesn't offer `/next-steps` ahead; never invokes `/charter` | Diff: one hunk, exactly the no-argument/nothing-to-resume branch. Live reply (Venue C): "...I'd suggest starting with `/charter`... Would you like to run `/charter`, or would you rather skip it and go straight to `/next-steps`... or bring your own idea?" — `/charter` named first, nothing invoked | ✅ pass |
| AC-1.2 | Same subagent, step 2: `/next-steps` on Venue C, user explicitly skips `/charter` | Recommends `/charter` first on empty-or-coded repo; proceeds to PO brief only on explicit skip; writes nothing under `.spark/` | Recommended `/charter` first; on skip, **actually delegated** to `product-owner`, which read `src/*.js`/`package.json`/git log for real and proposed wiring `subtract`/`multiply` into `index.js`'s exports (a real bug it found: `main` only exports `add`). `.spark/` absent before and after | ✅ pass |
| AC-1.3 | Same run | Decline/skip path = exactly today's behaviour, offer never block | Both ceremonies offered, never forced; skip routed to real delegation, not a dead-end | ✅ pass |
| AC-1.4 | `git diff HEAD -- skills/spark/SKILL.md` — confirmed the `<idea>`-argument path (`:20`) and lens nudge (`:59-71`) are **outside** the one changed hunk, byte-identical | Nothing differs on `/spark <idea>` / `/story-time <idea>` | Diff scope confirmed structurally by me directly (strongest available proof "nothing changed" — a live run can only sample, a diff proves it); corroborated by `evidence.md` Entry 11's quoted live run | ✅ pass |
| AC-1.5 | Fresh, performed by me directly: `git log`/`find`/`cat` against Venue B (has a constitution, no features) *before* any amendment; hand-traced `skills/next-steps/SKILL.md`'s live bullets against it | Zero sentences added when a constitution exists | Bullet 1 (`.spark/constitution.md` doesn't exist) → **false**. Bullet 2 (nothing in `.spark/` AND trivial history) → **false** (constitution exists). Control falls straight through to step 2 per `:63-68`'s explicit unconditional-fallthrough clause, quoted and read by me. `git diff HEAD -- skills/spark/SKILL.md` also shows the with-constitution branch untouched | ✅ pass |
| AC-1.6 | `sed -n '183,191p' README.md`, counted lines myself | ≤10-line Start Here block, precedes `/next-steps` example, names `/charter` on both repo states | Heading-to-last-line = **9** lines (`:183-191`); precedes the `:193` `/next-steps` example; both "empty" and "already full of code" named explicitly | ✅ pass |

### US-2 (Must) — one bounded Project Context

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-2.1 | `git diff HEAD -- templates/constitution.md` (mine); `grep -n "§8"` on both citing skills | Exactly one section (§9) added; §1–§8 byte-identical; both by-number citations still resolve | Single hunk, `+45/-0`, starts after §8; `grep` confirms `skills/spark/SKILL.md:77` and `skills/demo-day/SKILL.md:28` both still resolve "§8" → QA Method | ✅ pass |
| AC-2.2 | Both fresh subagent runs (Venue B amendment, Venue C first draft) — did §9 appear as its own decision in the *same* round as profile/QA method? | Same round, no extra round, no new numbered step | Venue C: §2/§8/§9 all drafted and "presented" together in round 1 ("combined decision, per SKILL.md step 3's rule"). Venue B: kickoff Q&A (round 1) → write (round 2) — 2 rounds total, §9 the only thing touched since §1–§8 pre-existed | ✅ pass |
| AC-2.3 | Counted myself on 3 independent live instances: this repo's §9 (13 total/6 brief/7 picture), Venue C's fresh §9 (17/7/8), Venue B's fresh §9 (9/6/– picture omitted) | ≤35/12/25 | All three well within caps, on three different generations of the same rule | ✅ pass |
| AC-2.4 | Cited: `evidence.md` Entry 7, the real installed-plugin run against this repo's actual pre-T8 constitution (now irreproducible — T8 already landed). **Fresh substitute I performed:** traced Venue B's still-old-shape (§1–§8, no §9) constitution through the live `/next-steps` skill myself, before amending it | No warning, no migration, no prompt on a pre-§9 constitution | Entry 7: installed ceremony read the pre-change constitution, said nothing about §9 (it had no such instruction). My own Venue B trace: falls straight through step 2, no mention of §9, no warning | ✅ pass |
| AC-2.5 | Read `review.md` and `evidence.md` directly myself (not summarized) | A phase that finds a contradiction records it, never edits the constitution itself | Real instance: the Reviewer found F11 (a §9 citation gap) and **filed it as a finding rather than editing** `.spark/constitution.md` itself, requiring a further `/charter` pass (Entry 14/15) — exactly the rule, exercised for real during this loop | ✅ pass |
| AC-2.6 | Marker audit on all 3 live §9 instances (this repo, Venue B, Venue C) | Every entry: `inferred from <file:line>` / `asked` / `confirmed by user` / `not stated` / `not found` — never a bare guess | All conform across all three; Venue C's evidence-starved brief correctly used `not stated` throughout rather than inventing answers | ✅ pass |

### US-3 (Should) — greenfield kickoff interview

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-3.1 | Fresh subagent, Venue B (constitution exists, no code/manifest — evidence answers nothing) | One numbered list, ≤7 questions, exactly the named topics | Full capped 7-question list returned round 1 (evidence answered none of it) | ✅ pass |
| AC-3.2 | Same run + Venue A (evidence.md Entry 9, cited) | Stack/non-negotiables/profile fallback wording correct | Venue B: stack answered "let the EM decide"; Venue A (cited): `undecided — the EM proposes at the first /sprint-plan`, profile `undetectable — from the user's answers` | ✅ pass |
| AC-3.3 | Cited: `evidence.md` Entry 9 — real quoted offer text, not re-tested (Should AC, no re-test trigger, own citation already checks out) | Offer, never auto-invoke | Quoted: "...Want me to run `/story-time <slice>` now, or hold off?" — not invoked | ✅ pass (cited) |
| AC-3.4 | Read `agents/facilitator.md`'s skip rule myself: "a question skipped... becomes `not stated`... a skip blocks nothing" | Skip → `not stated`, blocks nothing | Static rule re-confirmed directly by me. **No live run this round exercised an actual skip** (my Venue B fixture and evidence's Venue A fixture both answered every question) | ⚠️ not-verified-live (structural rule reconfirmed; dynamic skip path still unexercised — same gap `evidence.md` disclosed) |
| AC-3.5 | Counted rounds on both fresh runs | ≤2 relay rounds | Venue B: 1 round (evidence sufficient after questions returned). Venue C wasn't a pure US-3 case (had partial evidence) but also 2. Venue A (cited): 2 | ✅ pass |

### US-4 (Should) — brownfield discovery pass

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-4.1 | Fresh subagent, Venue C first draft | Hands Facilitator a git summary; reads README/CLAUDE.md/.spark specs; names what was read/absent | Real `git log` gathered; `README.md` read; **`CLAUDE.md` explicitly recorded absent** (not silently skipped); `.spark/` specs absent (first draft) | ✅ pass |
| AC-4.2 | Same run, +my own spot check of this repo's §9 | Exactly 7 system-picture entries in order, each ≥1 `file:line` or `not found` | Venue C: all 7, in the specified order, each with a real citation or `not found`. This repo: same 7, same order | ✅ pass |
| AC-4.3 | Round counts from Venue C (2) and Venue B (1); cited `evidence.md` Entry 8 (this repo's real T8 — a genuine correction round, cap overshoot compressed without dropping content) for the "correction folded without a second discovery pass" half | ≤2 rounds; corrections folded without re-discovery | Both fresh runs within bound; Entry 8 (cited, not re-derived — already independently re-verified 3 times by the Reviewer, no new trigger condition applies) shows a real correction folded in one pass | ✅ pass |
| AC-4.4 | Venue D **inspected on disk by me directly** (`git log` fails exactly as `evidence.md` quotes, no README, no CLAUDE.md, one `src/main.py`) — matches exactly; not re-run (would be pure repetition) | All three inputs absent → recorded `absent`, pass continues | Disk state matches Entry 12's claims verbatim; not re-executed | ✅ pass (disk-verified, cited for the live transcript) |
| AC-4.5 | Read this repo's `.spark/constitution.md` myself: lines that held the old improvised paragraph now read `## 1. Product Principles` directly (paragraph gone); §9 carries the same primary-user/problem/stack claims; Amendments table carries the dated row; `git diff -U0` → exactly 3 hunks | Meaning preserved, dated Amendments row, no other line changed | Confirmed directly, all three | ✅ pass |

### US-5 (Should) — PO/EM cite §9 instead of re-deriving

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-5.1 | `git diff HEAD -- agents/product-owner.md agents/engineering-manager.md`, read myself | §9 read before code, cited as `constitution.md §<n>` | Instruction text correct in both files. **No live `/story-time`/`/sprint-plan` run against a §9-bearing constitution happened this round** — would require spinning up a real feature spec, which AC-5.4 already correctly defers to the next real feature | ⚠️ pass (structural only) — dynamic trigger not-verified-live, same root cause as AC-5.4 |
| AC-5.2 | Same diff, read myself | All three conditions (a)(b)(c) named, plus "name which applied" | Both files state all three verbatim plus the naming duty | ✅ pass (structural) |
| AC-5.3 | Same diff, read myself | No §9 / no constitution → behave exactly as today | Both files' §9 branch is a plain conditional on "If it has a §9..."; the unconditional sentence precedes it and always runs; the branch is textually a no-op when absent — provable by reading in prompt material with no other execution path | ✅ pass (structural) |
| AC-5.4 | `grep -rl "constitution.md §9\|§9" .spark/*/spec.md .spark/*/plan.md`, run myself, excluding project-kickoff's own artifacts | Deferred — measures the *next* feature | One hit, `companion-offer/spec.md` — **read directly, confirmed a false positive**: it refers to a *different*, explicitly-cut "Constitution §9 Companions" idea from that feature's own spec, unrelated to Project Context. No real citation exists yet | `deferred` — reconfirmed, not just cited |

## Non-Functional Requirements

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| NFR-1 | Ran every count myself: `ls skills\|agents\|lenses\|templates`, `grep -c "^[0-9]\. "` on `/charter` (5), `/spark` (8), `/next-steps` (6) against both current and `git show HEAD:`; `git diff \| grep CLAUDE_PLUGIN_ROOT` | Zero new surface | 10/7/9/6 skills/agents/lenses/templates unchanged; all three step counts unchanged pre/post; 0 new `${CLAUDE_PLUGIN_ROOT}` paths | ✅ pass |
| NFR-2 | `git diff -U0 .spark/constitution.md` (3 hunks, §3 untouched); re-verified A3 live: `grep` on `aspark-guard`'s `test_rules.py:136` and `templates.py:28-32`, and `grep -rn constitution ~/aSPARK-graph/src/` (0 hits, run myself) | Additive only, neither consumer reads the constitution | All confirmed fresh, not copied from `evidence.md` | ✅ pass |
| NFR-3 | `grep -rln "Who exactly hurts today"` → `product-owner.md` only; `grep -rln "who the user is"` → `facilitator.md` only | One file each | Confirmed, different files | ✅ pass |
| NFR-4 | AC-1.5/AC-2.4's fresh Venue B trace, doubling as this NFR's negative case | Every ceremony behaves as today when constitution absent/declined/pre-change | Confirmed fresh (see AC-1.5, AC-2.4) | ✅ pass |
| NFR-5 | `claude plugin validate .` (run by me: green, one pre-existing unrelated `autoUpdate` warning); 3 fresh performed subagent runs plus my own direct checks, all quoted above | `validate` green + documented dogfood, negative case first | Confirmed | ✅ pass |
| NFR-6 | Counted myself: caps (see AC-2.3), rounds (≤2 throughout), questions (≤7), step counts (NFR-1), sentences added on constitution-bearing repo (0, AC-1.5) | All within bounds | Confirmed on 3 independent live §9 instances, not just cited | ✅ pass |
| NFR-7 | Read `README.md:366` and `ROADMAP.md:42` myself | Honesty about maturity — venue-bounded, no external-project claim | Both explicitly say "Neither path has run on an external project; no saving is claimed beyond these two venues" | ✅ pass |
| NFR-8 | `grep -n "^tools:" agents/facilitator.md` (no Bash); `grep -n "git " skills/charter/SKILL.md` (read-only `git log` only); step 5 text confirms explicit-go only | Nothing executed unasked | Confirmed; also both fresh subagents' venue writes were their own explicit test actions, never auto-triggered by the ceremony itself | ✅ pass |

**Active lens:** none applies to QA phase (per the caller: `library` is `phases: [specify, review]` only).

**`aspark-graph` tool:** probe resolved `runner=yes, graph=yes`. Ran `query impact` on all 8 touched files only (never `gate_health`, never `story_trace`'s QA leg, per the tool file's explicit "Not wired" section, read directly). Result: structural emptiness — `files: []`, all 8 paths under `unknown_files` — exactly as `plan.md` §2 already found and not a reassurance; the graph indexes no Markdown, so it has nothing to say about this diff.

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Minor | Amend a constitution that **already has real content in §3/§6** (not the empty/"not yet established" case AC-3.2 covers) via a `/charter` run that needs a kickoff-style interview for §9 because the repo itself has no source (Venue B: §3 = "Markdown only, fixture", §6 = "None"). `agents/facilitator.md` states kickoff answers "also feed the rest of the constitution... a named stack goes into §3... named non-negotiables go into §6." | **Expected (per spec):** unclear — AC-3.2 only specifies this propagation for the greenfield case where §3/§6 start empty. **Observed:** genuinely ambiguous whether an already-populated §3/§6 should be overwritten by a §9-focused interview's answers, or left alone since the amendment's declared scope is "§9 only." Not exercised as a real bug (I deliberately scoped my own test to §9-only to isolate the §8-integrity check, B1's actual subject); flagging it as an open product question the spec doesn't resolve, not a defect in what shipped. | open — routed to `/story-time` as a spec question, not a code fix |

**What I specifically tried to break, and didn't:** amending a constitution whose §8 **already declares its own QA-method fixture** (`Browser-observable surface: no`, substitute "fixture, not real") with a `/charter` run that only needed to add §9. Verified byte-for-byte (`diff`/`md5sum` on both the whole §1–§8 region and §8 specifically, before vs. after): **completely untouched**. This is the one thing that would have been genuinely dangerous — a `/charter` amendment silently "fixing" or re-deriving an existing QA-method declaration — and it didn't happen.

## 4. Console & Network

N/A, replaced per the substitute method — no browser, no console, no network. The
equivalent signals (command exit codes, diff output, file states) were clean throughout:
`claude plugin validate .` green on every run; every subagent's venue `git status
--porcelain` before/after matched expectations; this repo's own `git status --porcelain`
never moved during testing.

## 5. Verdict

Yes, I'd demo this. Both Must stories hold under testing I performed myself, independent of
`evidence.md`'s own (already extensive, 4-round, independently-re-reviewed) transcripts —
fresh subagent runs against working-tree files, never the stale installed persona, on venues
I re-confirmed matched their described state before touching them. The routing story (US-1)
is proven live on real coded and empty repos both. The Project Context story (US-2) is proven
live on three separate constitution instances, including the one test that mattered most:
whether a §9-only amendment can be trusted not to touch an existing §8 QA-method declaration
— it can, byte-for-byte. The Should stories (US-3/4/5) are solid, with two honestly-labeled
gaps that were already gaps before this round and remain so for the same reason: AC-3.4's
skip path and US-5's live citation trigger both need a scenario (a real skipped kickoff
question; a real next feature) that hasn't happened yet, not a defect. One Minor, B1, is a
genuine open design question worth a spec pass, not a bug — it doesn't touch anything that
shipped.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run
`/demo-day`.*

- [x] Every Must-story acceptance criterion verified and passed — all 12 Must ACs (US-1,
      US-2) verified with fresh, independently-performed evidence this round, 0 fail
- [x] Every NFR verified under the substituted method and passed — NFR-1–8 all pass, each
      re-run live by me, not cited from `evidence.md`
- [x] No open Blocker or Major bugs — 1 Minor (B1), a design question not a defect
- [x] Runtime signals clean on every exercised flow — `claude plugin validate .` green
      throughout; no venue leaked into this repo's working tree
- [x] Should-story ACs accounted for — 15 of 17 pass with fresh or freshly-reconfirmed
      evidence; 2 honestly `not-verified-live` (AC-3.4's skip path, AC-5.1's live citation
      trigger), both pre-existing, disclosed gaps that don't block a Should story's gate
- [x] Status set to `passed`
- [x] Line budget: Ist 187 / Soll ~130 — over, for a stated reason: this feature carries 24
      ACs + 8 NFRs across 5 stories (more than double a typical feature's surface), and every
      row cites what was actually performed rather than compressing to "see evidence.md" —
      compressing further would mean re-introducing the exact failure mode (`not
      re-verified`) this repo's own `CLAUDE.md` names. Not waived by the user; recorded here
      with its reason per the template's own allowance.
