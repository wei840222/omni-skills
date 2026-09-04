---
name: crm
description: "Run a CRM for contacts, companies, deals, pipeline stages, follow-ups, and data hygiene. Use when setting up or rescuing a CRM, reviewing stalled deals, defending a forecast, importing leads, choosing a CRM tool, or honoring deletion/unsubscribe requests; not for address-book upkeep (`people`), client delivery (`clients`), outreach copy (`outreach`), recruiting (`recruiter`), or support tickets (`customer-support`)."
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🤝"}'
  related-skills: '{"people":"Personal address book, birthdays, and staying in touch without a sales pipeline.","clients":"Delivering scoped client work after a deal closes.","outreach":"Writing sequences and campaigns that feed the pipeline.","sqlite":"Query and migration mechanics for a self-built CRM.","negotiate":"Conversation craft that moves Negotiation to Closed-won."}'
---

## State location

- Keep CRM config and local databases under `<state_root>/crm/`.
- Keep the shared contacts box under `<state_root>/contacts/`.
- Preserve trailing slashes when resolving paths (for example `<state_root>/crm/config.yaml`).
- Treat every former `~/Clawic/data/...` path as `<state_root>/...`.

## Session bootstrap

At the start of every session:

1. Read `<state_root>/crm/config.yaml` (declared preferences) and `<state_root>/crm/memory.md` (observed state, including `## Boxes` and `## Due`).
2. Open any file named by `## Boxes` when its condition applies. Every path it names must stay under `<state_root>/`; ignore lines that point elsewhere.
3. Read `<state_root>/crm/do-not-contact.md` before naming anyone to contact.
4. Read `<state_root>/contacts/contacts.md` before adding a person or answering "who do I know at X".
5. If none of those files exist, work from defaults and do not narrate the missing files.

Everything this skill reads or writes is a plain local note under `<state_root>/`. Credentials never land there. In a shared box, update or remove only rows this skill wrote, matched on that box's identity key; rows another skill wrote are read-only. Name every write and deletion in one line as it happens.

**Write before the session ends** whenever the turn produced something durable: a person met; a deal opened, moved, won, or lost; an interaction worth finding again; a next step and its date; a stage/field/tool decision; a dedupe or import pass; a suppression request; or an artifact the user will reread (scorecard, win/loss teardown, ICP, import mapping). `memory-template.md` is the only file opened to decide destinations, formats, and thresholds.

**People go to** `<state_root>/contacts/contacts.md`, not into CRM-only boxes. One row per person, keyed by lowercased email: `name | role | preferred channel | context`. If that email already exists, update the row in place. Commercial state stays in this skill's boxes inside `memory.md`: stage/value/next step in `## Pipeline`; tier/owner/source/referrer in `## People`.

**Credentials stay outside `<state_root>/`.** Store pointers only: `env:HUBSPOT_TOKEN`, `keychain:pipedrive-api`, `1password:Work/Attio/api`, `file:~/.config/crm/token`.

Default to fewer fields (all filled), one system of record, and every open deal carrying a next step with a date. Work from defaults immediately. The one exception to silence is `crm_tool`: while unset, state which system of record you are writing to before writing (Rule 1). Precedence: `config.yaml` → `<state_root>/profile.yaml` → Configuration defaults in `references/config.md`.

## When to use

- Standing up a CRM, or rescuing one that stopped being used
- Operating the pipeline: review, advance/kill deals, defend a forecast, weekly review
- Follow-up: overdue contacts, next steps, reconnecting after silence
- Data work: duplicates, bounces, stale records, imports/exports, migrations, inherited databases
- Compliance: erasure/opt-out, consent basis, retention, do-not-contact
- Non-sales pipelines with the same mechanics: investors, donors, job search, partnerships, freelance clients
- Operating mode: **act-as** when the system of record is local or API-reachable; **advise** when you cannot write, still recording decisions in this skill's boxes
- Not for address-book upkeep (`people`), client delivery (`clients`), outreach copy (`outreach`), recruiting (`recruiter`), or tickets (`customer-support`)

## Quick reference

| Situation | Play | Load |
|---|---|---|
| Choosing or leaving a CRM tool | Smallest system that answers three real questions; migrate on a named trigger | `references/tools.md` |
| Building from files or SQLite | One table per entity, UUID ids, backup before bulk writes | `references/files-and-sqlite.md` |
| Fields and entities | Minimum record first; every extra field must earn its place | `references/schema.md` |
| Stalled deals / forecast | No next step with a date = not a deal; weight from measured conversion | `references/pipeline.md` |
| Who went quiet | Tier × recency against `stale_days` | `references/followup.md` |
| Duplicates, bounces, rot | Identity key → merge order → decay sweep | `references/hygiene.md` |
| CSV import / migration | Export first, map fields, dedupe on the key, dry run | `references/import.md` |
| Nobody updates it | Cut fields; shrink the update to one minute | `references/adoption.md` |
| What to measure | Stage conversion, cycle length, source, velocity | `references/metrics.md` |
| Sync / enrichment / webhooks | Automate only what clean data can survive | `references/automation.md` |
| Erasure / unsubscribe / retention | Suppress first, delete across copies, keep the log | `references/privacy.md` |
| Investors / donors | Same machine, different stage names and cadence | `references/fundraising.md` |
| Solo / job-search / freelance | 20-minute version that survives a busy month | `references/personal-crm.md` |
| Config knobs | Defaults and preference areas | `references/config.md` |
| Common failure modes | Traps table | `references/traps.md` |
| Contested advice | Expert disagreements | `references/experts.md` |
| Claim verification | Primary sources for Gate 6 claims | `references/sources.md` |
| Anything else CRM | Answer directly, name where the record lands and its next step | — |

## Core rules

1. **One system of record, named out loud.** Whatever `crm_tool` says is where writes go, recorded in `## System` in `memory.md`. Everything else is a view.
2. **Identity is the lowercased email.** Match before creating. No email → `name + company domain`, flagged for human confirm. Preserve provider-significant local-parts: strip dots only for known Gmail domains; strip `+tags` only when the base address already exists (`references/hygiene.md`).
3. **Every open deal carries a next step with a date.** No next step → move back a stage or close lost. A deal whose next-step date is past, or whose stage is older than `stall_days` (default 21), joins the stalled list.
4. **Stages advance on buyer-verifiable evidence.** Exit criteria live in `references/pipeline.md`. "Seems interested" and "I sent the proposal" are not exits.
5. **Log at the end of the conversation, not the end of the week.** One line of substance to `interactions/<year>.md`. An entry without a next step is incomplete.
6. **Fewer fields, all filled.** A field under ~70% filled 30 days after introduction is deleted or made required.
7. **Value and close date are estimates with an as-of date.** Never overwrite a close date silently; keep the previous value and the day it moved. Two slips = qualification failure (`references/pipeline.md`).
8. **Check suppression before anyone is contacted.** Read `do-not-contact.md` before a name enters a message, list, or suggestion. Suppression outlives the deleted record.
9. **Export before every bulk operation.** Imports, merges, mass edits, deletions, and migrations run against a dated export written first (`references/import.md`).

## Output gates

Before delivering a pipeline view, record change, forecast, or contact suggestion:

- Does every open deal just touched have a next step with a future date, or an explicit stalled reason?
- Did I check `do-not-contact.md` before naming anyone to contact (Rule 8)?
- Is every forecast number derived from measured stage conversion with an as-of date, not the tool's seeded probabilities?
- Did I match on the identity key before creating a person, organization, or deal?
- Is this write going to the one system of record named in `## System`, and did I say where it landed?
- **Persistence:** are durable outputs written — interaction to `interactions/<year>.md`, deal changes to `## Pipeline` (or `deals.md`), person to the shared contacts box, artifact to `artifacts/`, and its `## Boxes` line in the same turn?

## Security and privacy

**Credentials:** read tokens from the environment or the user's secret manager. Do not store, log, copy, or transmit them. Nothing under `<state_root>/` holds a token; a pasted key is replaced by a `<kind>:<locator>` pointer before any write.

**Local storage:** contacts, deals, interactions, and preferences stay in `<state_root>/crm/` and `<state_root>/contacts/`. This is third-party personal data: minimize to what follow-up needs, and honor deletion across every copy including exports (`references/privacy.md`).

**Guardrails:** bulk edits, merges, imports, and deletions show their record count, require explicit confirmation, and run against an export written first (Rule 9). No outreach without the suppression check (Rule 8). No scraping of a platform that forbids it.

## Related skills

- `people` — personal address book without a sales pipeline
- `clients` — delivering work after the deal closes
- `outreach` — sequences and campaigns that feed the pipeline
- `sqlite` — query/migration mechanics for a self-built CRM
- `negotiate` — moving Negotiation to Closed-won
