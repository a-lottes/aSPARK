# Evidence: website-lens-seo-ux-run

| | |
|---|---|
| Feature | website-lens-seo-ux-run (second public `website` run; the first is `.spark/website-lens-public-run/`, accessibility lens only) |
| Phase | Specify / Review / QA evidence |
| Date | 2026-10-27 |
| Ticket | #105 |

## 1. Target and how to repeat it (AC-1)

| | |
|---|---|
| Repo | `https://github.com/11ty/eleventy-base-blog` (MIT, `LICENSE`), package version 9.0.0, tag line "v3.1.7" |
| Pinned commit | `cf0cc1f1b5972d9d7d06b9a0f0488e61839f3207` (2026-10-15, "v3.1.7") |
| Runtime | Node v22 (`.nvmrc` says 22; the run used v22.23.4), npm from the container, Python 3.13 for the static server |
| Clone | `git clone https://github.com/11ty/eleventy-base-blog && cd eleventy-base-blog && git checkout cf0cc1f` |
| Constitution | write `.spark/constitution.md` in the clone with `/charter` (the one this run got is `target-constitution.md`, copied unchanged; yours will differ in wording). `.spark/` is untracked in the clone, nothing tracked changes |
| Build | `npm ci && npm run build` (11ty wrote 15 files in 3.7 s; `_site/` and `node_modules/` are git-ignored) |
| Start | `cd _site && python3 -m http.server 8081 --bind 127.0.0.1`, open `http://127.0.0.1:8081/` |
| Browser | Playwright MCP headless Chromium, 1280x800 and 375x800; 33 browser tool calls in QA (1 errored) |
| Model | `claude-sonnet-5-5` for the orchestrator, facilitator, product-owner, reviewer and qa-tester |
| Plugin build | installed `/opt/aspark` (`templates/review.md` does not exist there; the reviewer used `templates/review-report.md`) |

**Deviation from "build and start" as upstream documents it:** upstream's `npm start` runs `eleventy --serve`, a dev-mode server that includes the draft `fifthpost` and `/.11ty/image/` URLs. The spec (A2, C2) requires a production build, so QA ran the static production `_site/` on :8081. `npm start` was run once by the orchestrator (to prove it starts: "Server at http://localhost:8080/", HTTP 200) before the production build replaced `_site/`; **the dev server on :8080 was not stopped** (my kill attempt matched the processes but the port still answered afterwards, I did not chase it) and was not used by QA. Scratch only; the container goes away.

Citations re-resolved by the author at the pinned commit with `git show cf0cc1f:<path> | sed -n`: `eleventy.config.js:57` (`preAttributes: { tabindex: 0 }`), `:77-85` (hardcoded feed metadata), `_includes/layouts/base.njk:6-7` (shared `<title>`/description fallback), `content/sitemap.xml.njk:8-9` (loop over `collections.all`), `_includes/postslist.njk:3` (`url` never defined). `git diff --stat` in the clone after the run: empty; `git status`: only the untracked `.spark/`.

## 2. Lens activation (AC-2)

| Step | Who did it | What happened |
|---|---|---|
| `/charter` | Orchestrator invoked the `aspark:charter` skill with the target path; the `facilitator` agent wrote `/tmp/scratch/eleventy-base-blog/.spark/constitution.md`, from README, `package.json`, `content/`, `_includes/`, git summary gathered by me | Type `website`; characteristic `is-public`; lenses `seo` on, `ux` on, `security` on (marked "needs user confirmation"); `accessibility`, `i18n`, `data`, `api`, `cli`, `library` off, each with a reason; QA method: browser-observable surface = yes |
| Dispatch | Orchestrator, following `/story-time`, `/peer-review`, `/demo-day`: read each active lens's `phases` frontmatter | `seo`: specify, design, review, qa. `ux`: specify, design, qa. `security`: specify, review, qa. So Specify gets all three, Review gets `seo` + `security`, QA gets all three. Agents were handed lens **paths only**, no item names, no checklist, no trace request |

**Weaker than it sounds:** the dark-mode Facilitator had nobody to ask, so the profile is a draft nobody confirmed (the constitution says so itself for `security`); `/charter`'s Present/Iterate steps with the user did not happen. The dispatcher was the line orchestrator following the skills' steps, not a person typing `/peer-review`. The prompts still named the feature, the spec and the constitution, so the agents knew a lens-driven review was wanted (a prompting effect, not a clean "unprompted" condition). Design (`/look-and-feel`) was **not run**, so the `design` phase of `seo`/`ux` is unexercised. Plan and Act were not run (nothing is built).

## 3. Which lens fired in which phase, and which stayed silent

n = 1 session per phase, one model, no per-item trace requested, **no rate**. "Fired" = a finding or NFR in the report cites that lens's area; I read the reports and matched them to lens sections myself.

| Phase | `seo` | `ux` | `security` |
|---|---|---|---|
| Specify (`spec.md`) | **Fired.** NFR-1 (performance, CLS), NFR-2 (server-rendered content), NFR-3 (titles, description length, one h1), US-5 and six `[GAP]` ACs (robots.txt, canonical/OG, duplicate titles, sitemap content) | **Fired.** NFR-4 (clicks to goal, 375px, skip link/focus, empty states) | **Fired, thinly.** NFR-5 (secrets/PII in output, https links, `npm audit`); the spec's own A6 about response headers is wrong (see §5 R2) |
| Review (`review.md`) | **Fired.** F2 (non-unique titles/description), F4 (no `robots.txt`), F5 (no canonical/OG), F6-F8 (sitemap content and `lastmod`), plus the feed metadata (F1) | **Silent, correctly:** `ux.md` `phases` has no `review`; the reviewer wrote "The `ux` lens is not a review-phase lens here" and tagged NFR-4/NFR-6 rows `not-verified-live` | **Fired.** F3 (`npm audit`: 2 high), F10 (no security headers in `netlify.toml`/`vercel.json`), F17 (generator version printed); its §2/§3 (auth, data access) were declared n/a |
| QA (`qa.md`) | **Fired.** AC-5.x and NFR-2/3 observed live (view of raw server HTML, 9 pages), CLS 0 measured; Lighthouse not available | **Fired.** NFR-4a/4b walked by real clicks and Tab; B2 (touch targets 20 px tall at 375 px) came from the ux lens's own item; form/validation and motion items declared n/a (no form, no animation seen) | **Fired.** NFR-5a/5b (secret/email search, https links, `npm audit` re-run), NFR-5c cookies/headers/console; auth, authz, IDOR, PII-deletion items declared n/a (no auth, no data) |

Silent-by-design and why: `accessibility`, `i18n`, `data`, `api`, `cli`, `library` are off in the constitution, so no agent received their paths and none produced a finding under their name. That is the only silence I can show; I did not run a control with these lenses on.

## 4. Browser verification (AC-3)

`qa.md` verified in the real browser (Playwright MCP): the Home → post → tag → "all tags" → Feed click path at 375 px (4 clicks, NFR-4a), the skip-link Tab/Enter walk (NFR-4b), `aria-current`, the Atom feed opened and rendered by its XSL, CLS = 0 and LCP 108 ms on `/blog/fourthpost/`, `scrollWidth == clientWidth` at 375 px on 9 pages, and the raw server HTML of 9 pages. Server-HTML claims were made with same-origin `fetch()` inside the page, not view-source tabs; `qa.md` says so row by row.

`⚠ not-verified-live` in `qa.md` (8 rows): AC-1.6 (clipping/overlap), AC-1.7 (`/nope/` is the Python harness's page), AC-2.5 (hover/focus reveal, JS-off load), AC-3.5 (no draft-only tag in the content), NFR-1 (no Lighthouse installed; no score estimated), NFR-4c (no zero-post page), NFR-5c (headers seen are the harness's, not a host's), NFR-7 (`build-ghpages` not run, target read-only). `review.md` marks 28 rows `not-verified-live` that QA then took over; those QA did not reach stay open.

Results: 6 `[GAP]` ACs confirmed (AC-1.5, 4.4, 5.4, 5.5, 5.6, 5.7); AC-2.6 FAIL (B1: the second, unhighlighted `<pre>` on `/blog/thirdpost/` has `tabindex` -1 and scrolls at 375 px, 403 > 343 — `eleventy.config.js:57` only applies `tabindex: 0` to highlighted blocks); NFR-5 FAIL (`npm audit`, 2 high: `zod`, `markdown-it`); B2, B3 (`/favicon.ico` 404, no icon link), B5 minor.

## 5. Refuted-with-finding, misfires and misses (AC-4)

Nothing below was fixed in the target or hidden. The spec was not edited after these were found, except the status gate.

- **R1 — Review missed B1.** `review.md` marked AC-2.6 `not-verified-live` and never looked for code blocks that are not syntax-highlighted. QA found the failing `<pre>` live. Not a lens item (the `accessibility` lens is off here); a static-review gap. The run shows the QA half catching what the Review half could not, which is the point of both.
- **R2 — The spec (Specify, product-owner) was wrong twice, found by Review (F14, F15):** AC-1.5/A8 list too few pages that show the set-up message box (`/about/` and `/blog/` also; 9 pages in total), and A6 says response headers are set by the host, not the repo, when `netlify.toml` and `vercel.json` can set them (F10). The `security` lens's Specify output was therefore partly wrong; Review corrected it.
- **R3 — `ux` found little because the site has little interaction.** No form, no state, no animation: most ux items were declared n/a in QA. Its one distinct finding is B2 (touch targets). This does not show whether the lens would hold on an interactive app.
- **R4 — Profile not confirmed.** `security` was switched on by a Facilitator that marked it unconfirmed; on a static page with no auth it produced mostly n/a items plus the `npm audit` and headers findings. Whether it earns its place was not decided by a person.
- **R5 — My own run defects.** (a) I started the dev server first, so the first `_site/` was a dev build; the spec author noticed it and I rebuilt for production before QA. (b) The dev server on :8080 is still up (see §1). (c) The product-owner wrote a spec with `[GAP]` ACs that fail by design; the reviewer and tester handled them as the spec asked. A "failed" QA on a retrospective spec is easy to misread — the QA Tester wrote `failed`; I changed `Status` to `passed` with an explicit orchestrator ruling in `qa.md` (precedent: `.spark/website-lens-public-run/qa.md`), and left the tester's verdict text and gate checkboxes unedited.
- **R6 — Prompted, not unprompted, at the edges:** the QA prompt told the tester which lens files to read, as the skills do; it did not list items. Whether the Review would have applied `seo`/`security` without the paths was not tested.
- **No tool/CI check ran the activation:** all of it is Markdown followed by agents.

## 6. What is still not shown (AC-6 input)

One site, one run, one model, no firing rate, no lens-free control. The profile was drafted without a person. Not run: `/look-and-feel` (Design), Plan, Act (nothing was built or changed), `accessibility` lens on this site, any assistive technology, Lighthouse, a deployed host's headers, `build-ghpages`. The target is a starter template with placeholder content and almost no interactive state, a weak test for the `ux` lens. Not a live public URL: a local build.

## 7. Fences and AC-5 / AC-7

- **AC-5:** scratch clone `/tmp/scratch/eleventy-base-blog`; `git diff` empty, only the untracked `.spark/constitution.md` was added there; no secrets (the target's placeholder email `youremailaddress@example.com` is public template content and is not reproduced as a credential); no customer material.
- **AC-6:** tracked changes in this repo are Markdown only: this folder, `ROADMAP.md`, `README.md`, `docs/status.md`. No lens, skill, agent or template text changed; no script committed.
- **AC-7:** `claude plugin validate .` was **not run**: the `claude` CLI is not on `PATH` in this container (`command -v claude` printed nothing). Not verified.
