---
name: clients
description: 'Manages client relationships end to end for freelancers, consultants, and agencies. Core value: Maintains professional boundaries, handles scope creep, and ensures you get paid. Primary triggers: When a prospect enquires, when scoping proposals, managing scope creep, getting paid, or handling renewals and endings. Common use cases: Covers retainers versus project work, change orders, and referrals. Alternative skills: drafting (`skills/contract`) the contract itself (`skills/contract`), issuing invoices (`skills/invoice`), filing received invoices (`skills/invoices`), a personal contact book (`skills/people`), running an agency (`skills/agency`), or Upwork tactics (`skills/upwork`).'
metadata:
  openclaw: '{"emoji": "\ud83d\udcbc", "requires": {"config": ["<state_root>/data/clients/", "<state_root>/data/contacts/", "<state_root>/data/projects/", "<state_root>/profile.yaml"]}}'
  related-skills: '["skills/projects", "skills/people", "skills/negotiate"]'
---
**Data.** At the start of every session, read `<state_root>/data/clients/config.yaml` (what the user declared) and `<state_root>/data/clients/memory.md` (what you observed, plus its `## Boxes` index and its `## Due` table). Open any file `## Boxes` names the moment the condition written on its line applies — that index *is* the list of files; work exclusively from the file index (`## Boxes`) when identifying resources, because most boxes are created after this skill was written. Before saying anything about a named person, read `<state_root>/data/contacts/contacts.md`; before anything about a live engagement, read its `<state_root>/data/projects/<project>.md`. If none of it exists, work from the defaults below and say nothing about it. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, never rewritten and never deleted, and every write and deletion is named in one line as it happens.

**Write before the session ends** whenever it produced something durable: a lead in or out, a client won, paused, or retired, a rate or terms change, a stakeholder learned, a meeting or decision, a change order, an invoice sent, chased, or paid, a renewal or end date, a concentration number — or something the user will read again: a winning proposal, an onboarding checklist, a rescue plan, a script that worked, a handover, a post-mortem. `memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**People and projects live in shared boxes, not here.** Every human at a client goes to `<state_root>/data/contacts/contacts.md` — one row, `name | role | preferred channel | context`, identified by **email or handle**. Read that file before adding: if the address is already there, update that row in place, and only update rows that this skill explicitly created. When someone leaves, delete their row and note the date in `memory.md` — a contact list that only grows stops being one. Table until ~15 people; past that, one file per person at `<state_root>/data/contacts/<name>.md`, with `contacts.md` left as the index. If the file already exists with different columns, match its columns and add anything missing as a trailing note; append any missing data as a trailing note instead of altering the header. Every engagement with a start, an end and milestones goes to `<state_root>/data/projects/<project>.md`, one file from the first, identified by the project name; the client is referenced there **by name only**. Duplicating a person or a project into the clients box is the fastest way to make two skills contradict each other.

**No credential is ever written anywhere under `<state_root>/data/`** — not in the files named here, not in a file you create, not in text the user pastes in to be kept. Clients hand over logins constantly at kickoff; store the pointer and drop the value: `1password:Clients/Acme/wp-admin`, `keychain:acme-sftp`, `env:ACME_API_TOKEN`.

Client work fails at the seams, not in the craft: the thing that was left unwritten, the favour that became the baseline, the invoice nobody chased. Be specific and dated — a name, an amount with its currency, a date, a next step with an owner. Draft what the user will send; leave sending, pricing, and final acceptance exclusively to the user. Work from defaults immediately: skip asking about their business, their rates, or how they like to work. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: currency, locale, timezone) → the Configuration table default.

## When To Use

- Mode: **act-as** — this skill runs the user's client system and drafts what goes to the client. The user sends, signs, and commits; it leaves transmission to the user
- A lead arrived and the decision is whether to take it, what to charge, and what to write back
- Kicking off: scope document, access, stakeholder map, approval chain, working agreement
- Running a live engagement: status cadence, decisions, change orders, expectation management, bad news
- Money: deposits, terms, a late invoice, a stop-work call, a rate rise, collections
- The relationship itself: a client going quiet, a rescue, a firing, a renewal, an ending, a referral, a testimonial
- Portfolio questions: concentration, capacity, which clients to keep, whether to take one more
- Alternative skills: drafting (`skills/contract`) or reviewing contract language (`contract`), issuing or numbering invoices (`invoice`), archiving invoices received from suppliers (`invoices`), a personal address book (`people`) or personal relationship tracking with no commercial engagement behind it (`crm`), running an agency as a business — hiring, utilisation, team structure (`agency`), or the consulting problem-solving method itself (`consultant`). This skill is the commercial relationship with a paying client, from lead to ending

## Reference Map

| File | Purpose | When to load |
|---|---|---|
| `references/engagement-models.md` | Breakdowns of engagement types (fixed, retainer, hourly). | When scoping a new client, deciding on pricing strategy, or changing models. |
| `references/traps.md` | Common pitfalls in client management and how to avoid them. | When dealing with tricky situations, scope creep, or difficult clients. |
| `references/where-experts-disagree.md` | Nuances on firing vs fixing clients, retainers vs projects, and niching. | When evaluating the overall portfolio strategy or handling extreme client disputes. |
| `references/research.md` | Domain knowledge on CRM, pricing models, and risk management. | When needing foundational context on client management best practices. |
| `references/output-gates.md` | Checklist before sending anything to a client. | Before ending a session or sending a message to a client. |
| `references/configuration.md` | User-dependent variables, preferences, and defaults. | When evaluating rules around deposits, status cadence, payment terms, risk posture. |

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| "Someone enquired — should I take it?" | Score against the decline list before pricing anything; the answer is often no | `pipeline.md` |
| Writing the proposal or statement of work | Three-option ladder, deliverables as nouns, exclusions section longer than you want | `proposals.md` |
| Setting or raising a price | Effective hourly rate first, then the model; rises get a date and a reason, presented as a final statement | `pricing.md` |
| Just won it — what now | Deposit before calendar; access, stakeholders, approval chain, working agreement, kickoff | `onboarding.md` |
| Enterprise procurement, vendor portal, security questionnaire | Treat it as its own mini-project with its own timeline; it delays first payment, not first work | `onboarding.md` |
| "Who actually decides here?" | Map champion, economic buyer, blocker, and user; the org chart is not the map | `stakeholders.md` |
| Running the week: status, meetings, decisions | Status on cadence unasked; every decision written back within a day | `delivery.md` |
| Delivering bad news, a delay, or a no | Bad news early is a status update; bad news late is a breach | `delivery.md` |
| "Can you just add one small thing?" | Change order, priced or logged — always explicitly priced or logged | `scope.md` |
| Invoice is late, or the client stopped paying | The ladder in Payment Ladder below, on dates, no improvisation | `getting-paid.md` |
| Client is hostile, chaotic, ghosting, or abusive | Rescue plan with a review date, or the exit procedure; both are written | `difficult-clients.md` |
| Renewal, expansion, referral, testimonial | Ask at the moment of delivered value, not at the moment of need | `retention.md` |
| Engagement is ending, well or badly | Handover pack, final invoice, access revoked, post-mortem, reference secured | `offboarding.md` |
| One client is most of the income; capacity is full | Concentration share, utilisation, and the replace-or-shrink decision | `portfolio.md` |
| Anything else about a client | Answer from the roster and the contact log, then name the next step, its owner, and its date | — |

Coverage map: `pipeline.md` leads and qualification · `proposals.md` scoping and winning · `pricing.md` rates and models · `onboarding.md` kickoff and procurement · `stakeholders.md` client-side politics · `delivery.md` running the engagement · `scope.md` creep and change orders · `getting-paid.md` cash · `difficult-clients.md` rescue and exit · `retention.md` renewals and referrals · `offboarding.md` endings · `portfolio.md` client mix and capacity.

## Core Rules

1. **Read the roster before you speak about a named client.** `## Roster` in `memory.md` (or the file its `## Boxes` line points to), the contact rows, the project file, and the client's `contact-log/` entry. Answering from the conversation alone recreates the amnesia the user installed this to end — and the second time you ask what their payment terms are, you have taught them the system does not work.
2. **Nothing starts before the paper and the deposit.** Signed scope plus `deposit_pct` of the fee received (default 50% on a first engagement, 30% once a client has paid twice on time) before a calendar slot is held. The deposit is not about cash flow; it is the cheapest test of whether the buyer can actually buy. Skip it only when `contract_required` is false and the amount is below one day of work.
3. **Anything not in the scope document is a change order.** Price it or log it, always explicitly priced or logged. A logged free favour still gets its estimated hours written into the project's change log — that ledger is the whole argument at renewal, and it is why "we've done 40 unbilled hours" beats "it feels like a lot" (`scope.md`).
4. **Chase on dates, not on feeling.** The ladder below runs on the calendar from the due date, with no step skipped and no step delayed because the conversation feels awkward. Each rung is written; a chase that happened only in your head did not happen.
5. **Concentration is a number you compute, not a feeling.** Share = client revenue over the trailing 12 months ÷ total revenue over the same 12 months. Above `concentration_limit_pct` (default 30%) it is a standing risk item in `## Due`; above 50% the user has an employer without any of employment's protections, and the fix is pipeline, not loyalty (`portfolio.md`).
6. **Status goes out unasked, on `status_cadence`.** A client who has to ask how it is going has already spent a day worrying, and worry converts into scope questions and slow approvals. Cheapest insurance in the whole domain: three lines — done, next, blocked-on-you — on a fixed day.
7. **Every decision gets written back the same day, to the person who made it.** "Confirming: we're going with B, which moves the launch to the 14th; tell me by Thursday if that's wrong." Silence against a written, dated restatement is worth something later; a verbal agreement is worth nothing.
8. **Price changes get notice and a reason, presented as a final statement in the moment.** Announce 30-60 days out, in writing, effective at the next renewal or next project — not mid-delivery. "From 1 October my rate is X" is a statement; "would you be okay with a rise?" invites a counter you then have to accept.

## Payment Ladder

Canonical for this skill; run from the invoice due date, one rung per step, every rung recorded in `## Receivables`. Detail, escalation letters, and what to do when they simply will not pay: `getting-paid.md`.

| Day | Move | Channel |
|---|---|---|
| Due date | "Invoice 0042 is due today, here it is again" — one line, no apology, attachment re-sent | Email to accounts payable, cc the client contact |
| +3 | Confirm it was *received and entered*, not whether it was paid — most late invoices are lost, not refused | Email, reply in the same thread |
| +7 | Second notice naming the late-payment term from the contract and the date interest starts | Email, new subject line |
| +14 | Phone the AP contact, then email a one-line summary of the call — the call is what moves it, the email is what proves it | Phone, then email |
| +21 | Written stop-work notice: work pauses on a named date until the balance clears; keep it factual and unemotional | Email to the client contact and their manager |
| +45 | Formal demand, then a collections agency or small-claims filing; statutory interest and fixed recovery costs apply in the UK and the EU (see `getting-paid.md`) | Letter or legal channel |

## Warning Signals

The domain's tell is that every disaster announces itself weeks early in a way that looks like nothing. Each row is a signal you can observe, not a mood.

| Signal | What it usually means | Move |
|---|---|---|
| "We'll sort the paperwork later, can you start Monday?" | The buyer cannot sign, or intends the terms to stay negotiable | No start without paper; offer a small paid discovery instead (`pipeline.md`) |
| Deposit is "in process" for more than a week | They cannot pay, or you are not in their AP system yet | Stop before delivery, not after; check procurement onboarding (`onboarding.md`) |
| The approver is absent from the call | You are talking to a messenger; every decision will be re-litigated | Get the economic buyer into one meeting or reprice for the delay (`stakeholders.md`) |
| Requests arrive by direct message at night, outside the tracker | The working agreement was never really adopted | Restate the channel once, in writing, then only answer in it (`delivery.md`) |
| Three "quick things" in a fortnight | Scope is drifting by accretion; nobody will notice until margin is gone | Log the hours, then convert the fourth into a change order (`scope.md`) |
| Approval times doubling | Priority is dropping internally, or your champion is losing standing | Ask the champion directly what changed; check for a reorg (`stakeholders.md`) |
| An invoice is late for the first time from a client who never was | Their cash has turned, and you are a supplier they can stretch | Tighten terms on the *next* invoice immediately (`getting-paid.md`) |
| Feedback shifts from the work to your process or attitude | Someone internal is building a case, usually to justify a switch | Rescue plan with a named review date (`difficult-clients.md`) |
| Silence from an active client for longer than the status cadence | Project deprioritised, budget frozen, or your contact has left | One direct question, then a dated pause proposal (`retention.md`) |
| They want set hours, their equipment, and exclusivity | Employment dressed as contracting; classification exposure for both sides | Push back on control terms, not on the fee (`pipeline.md`) |
| Anything else that feels off | Write down the observable behaviour and its date in the contact log | Two entries of the same behaviour is a pattern; act on the second, not the fifth |

## State Location

**Stateful Skill**: This skill manages local state for clients, configs, and projects.

- **Candidate locations**:
  1. `<state_root>/data/clients/`
  2. `<state_root>/data/contacts/`
  3. `<state_root>/data/projects/`
- **Lookup order**: The skill uses the workspace-first convention, preferring the `<state_root>` directory.
- **Creation behavior**: If the configuration or state files (e.g. `config.yaml`, `memory.md`) do not exist, the skill will initialize them with defaults in the `<state_root>` directory upon first relevant use.
