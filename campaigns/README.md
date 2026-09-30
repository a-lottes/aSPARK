# Campaigns — one goal, one budget, run in iterations

A **campaign** is a second way of working next to the feature loop. A feature answers
"is this story done?". A campaign answers "has this measurable end state been reached?" —
for example "every slice is parity-green" — and it runs in iterations until it has, or
until the budget or a stop rule ends it. The goal is approved by the **user**; the agent
only iterates inside it.

A **campaign kind** is one file in this directory: a ready goal shape with roles, stop rules
and budget defaults. Like a lens, a kind is **knowledge, not a new team member**: adding one
never edits an agent or a skill. Today one kind exists, [`migration-campaign`](migration-campaign.md).

> **Status, stated plainly.** The need for campaigns is *anticipated, not observed*. There is one
> kind. Budgets and stop rules are **followed by the agent, not enforced by Core** — Core is
> Markdown with no runtime; optional enforcement is `aspark-guard`'s concern. Effectiveness is
> unmeasured.

## The contract (what every kind file guarantees)

Frontmatter declares all seven keys. A file missing any of them is reported as **malformed,
naming the key**, and is not used.

| Key | Meaning |
|---|---|
| `name` | The kind's name. Equals the file name without `.md`. |
| `trigger` | What kind of request this kind is for, in one line. |
| `goal-kind` | The shape of the machine-decidable goal, in one line. |
| `roles` | The role briefs the kind defines (they run as fresh subagents; no `agents/*.md`). |
| `stop-rules` | The kind's **additions** to the four Core rules in `templates/campaign.md`. |
| `budget-defaults` | Default iteration and token budget; each labelled unmeasured and overridable. |
| `phases` | Which SPARK phases the kind acts in: `specify`, `plan`, `act`, `review`. |

Below the frontmatter a kind carries whatever the format in [`templates/campaign.md`](../templates/campaign.md)
needs filled in for that kind. It may **tighten** Core's stop rules and budget floors; it may not
loosen them, grant tools, waive a gate or veto condition, or imply approval.

## Discovery is a rule, not a list

A kind is *every `campaigns/*.md` file except this `README.md`, judged by its own frontmatter*.
No skill or agent contains a list of kind names; docs name kinds only as examples. A new kind therefore reaches every
phase it declares in `phases` by adding one file — and only that file.

## Instantiating a campaign

1. Copy `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` to
   **`.spark/campaigns/<campaign-name>/campaign.md`**, then append the chosen kind's body (below its frontmatter) as §8 "Kind-specific"; the kind's added stop rules extend §4. The copy is **frozen at approval**: the user
   approves exactly the text that governs the run, and a later plugin update cannot change it.
2. Fill every element. **Any blank element means the campaign is not startable.**
3. The user records goal approval (their own statement, transcribed by them or, on their instruction, by the agent) and sets `approved`.

Naming rules, because [`aspark-graph`](../tools/README.md) reads `.spark/`:
- The file is always called `campaign.md`. No other stem may contain `spec`, `plan`, `review`,
  `qa` or `release` — the graph reports those as near-misses.
- All campaigns share **one reserved directory**, `.spark/campaigns/`. `campaigns` is therefore a
  reserved name under `.spark/`: a feature folder must not use it.
- The graph does not index a campaign. It sees one extra directory and skips its files; that is
  recorded, not fixed here.

## Activation, and where it stays silent

- **Activation (this increment):** only an explicit user instruction that **names the instance**,
  for example "run the campaign at `.spark/campaigns/<name>/campaign.md`". Nothing switches a
  campaign on by itself and no ceremony proposes one yet.
- **Silence:** a repo without `.spark/campaigns/` sees no change in any ceremony — no notice,
  no question, no mention. The ten ceremonies do not know this directory yet; routing and the
  standing rule for ordinary feature loops arrive in a later increment. Until then, in a repo
  whose only `.spark/` subdirectory is `campaigns`, `/spark` with no argument treats it as a feature.
- **Hand-run:** the user names the instance; the agent reads it, refuses without recorded goal
  approval, iterates one step at a time inside the budget, logs a checkpoint after each iteration
  (`CK-<n>`), and sets `halted` and escalates when a stop rule trips. The agent may set only
  `running` (at the start, and after a halt once its cause is resolved and recorded in a `CK-` entry;
  a goal, threshold or budget change still needs the whole spec approved afresh) and `halted`.
- **Without `aspark-guard`:** nothing changes and nothing is reported. The rules are instructions.
- **No skill reads a campaign definition from the target project.** Only the instantiated
  `campaign.md` is written there.

## Adding a campaign kind

Open an [enhancement issue](../../../issues/new?template=enhancement.yml) or a PR, as for lenses.
Copy [`migration-campaign.md`](migration-campaign.md) as your model and keep the file within its size
cap. A kind is ready when it can answer: what is the **decidable** goal, what observable and
verifier confirm it, which roles it needs and which output each produces, what it adds to the
stop rules, and **where it stays silent**. A goal that can only be judged as "looks good" is not a
campaign — it belongs in the feature loop. See [`CONTRIBUTING.md`](../CONTRIBUTING.md).
