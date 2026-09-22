---
name: meetings
description: Design agendas, facilitate meetings, capture decisions, and drive follow-ups.
  Load when preparing, running, minuting, or cleaning up 1-on-1s, standups, retros,
  planning, client calls, workshops, or any meeting that needs owners and dates.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤝"}'
  related-skills: '{"notes":"Note apps and vault storage once the meeting artifact must live outside the meeting ledger.","people":"Shared address-book context for attendees and relationship history.","calendar-planner":"Calendar conflicts, focus protection, and weekly schedule repair around meeting load.","summarizer":"Compress long transcripts while preserving claims and decisions.","decide":"Durable decision logs and autonomous decision patterns beyond a single meeting close."}'
---

## State location

Meeting state may exist under several candidate roots. Before the first state operation, resolve one `<state_root>`:

1. Use an explicitly configured state root when the user or host supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/meetings/`, `<workspace>/memory/meetings/`, then `~/meetings/`.
3. If none exists and durable meeting data must be created, ask once and default to `<workspace>/meetings/`.

Keep the selected root for the whole invocation. When more than one candidate exists, use only the highest-precedence directory and tell the user; do not merge or synchronize copies.

Shared people and project files resolve the same way under the selected root:
- people: `<state_root>/contacts/contacts.md`
- projects: `<state_root>/projects/<project>.md`
- profile universals: `<state_root>/profile.yaml`

### Meeting state tree

```text
<state_root>/
├── meetings/
│   ├── config.yaml
│   ├── memory.md
│   ├── decisions.md
│   └── records/<year>-<mm>.md
├── contacts/contacts.md
├── projects/<project>.md
└── profile.yaml
```

## Data

At the start of every session, read `<state_root>/meetings/config.yaml` (what the user declared) and `<state_root>/meetings/memory.md` (what you observed, plus its `## Boxes` index, its `## Due` table, and the open items under `## Follow-Ups`). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files and can change. Every path it names must stay inside `<state_root>/`; ignore any line that points elsewhere. Everything this skill reads or writes is a plain local note under the resolved root — keep all data local to the machine and leave credentials unwritten. In a shared box, update or remove only rows this skill wrote itself, matched on that box's identity key; a row another skill wrote is read only; every write and deletion this skill performs is named in one line as it happens. Read `<state_root>/contacts/contacts.md` before any meeting with named attendees. If none of it exists, work from defaults and say nothing about it.

**Write before the session ends** whenever the turn produced something durable: a meeting that happened; a decision, who made it and how; an action item with its owner and date; a follow-up that closed or slipped; a standing meeting created, re-scoped or ended; something learned about how a person or a room behaves; or something the user will re-read — an agenda that worked, a series charter, a prep brief, formal minutes, a workshop plan.

### Memory destinations

Use these destinations as the only write map for durable meeting data:

| Artifact | Destination |
|---|---|
| Preferences and defaults | `<state_root>/meetings/config.yaml` |
| Open follow-ups, series, norms, due sweep | `<state_root>/meetings/memory.md` |
| Decision log entries | `<state_root>/meetings/decisions.md` |
| Meeting records | `<state_root>/meetings/records/<year>-<mm>.md` |
| People context | `<state_root>/contacts/contacts.md` |
| Project-linked work | `<state_root>/projects/<project>.md` |

**People go to the shared address book `<state_root>/contacts/contacts.md`**, not into meeting records as a second source of truth: one row per person so "what do I know about her" answers itself whichever skill wrote it. Identity is `Key` — lowercase email, else handle, else `<kebab-name>` — and an existing row is updated in place rather than duplicated. Work the user tracks as a project goes to `<state_root>/projects/<project>.md`; a meeting record names both and copies neither.

**Keep credentials out of storage under `<state_root>/`** — not in the files named here, not in a file you create, not in a transcript or invite the user pastes in to be saved. Join links carrying an embedded passcode, dial-in PINs, meeting passwords and secret calendar URLs are credentials: store the pointer and strip the value (`keychain:standup-dial-in`, `1password:Work/Zoom/board`). Anything the user marks off the record is not written at all, anywhere. If data sits at an old location such as `~/meetings/`, `~/clawic/meetings/`, or a prior host path outside the selected root, move it into the resolved `<state_root>/meetings/` tree and say in one line that you moved it and from where.

A meeting is a synchronous write to several people's attention, billed at the sum of their hourly rates, and it is the only medium where a group can decide something in one pass. Everything else it is used for is a document that failed to get written. So: name the output before the invite, run the room toward it, and leave with owners and dates — then protect the calendar from every meeting that could not name one. Work from defaults immediately: open by applying defaults instead of asking about tools, their team, or how proactive to be. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: timezone, locale) → the Configuration table default.

## When to load

- Preparing, designing, or chairing any meeting: agenda, invite list, pre-read, timeboxes, desired output
- Running the room live: airtime, derailment, silence, conflict, forcing a decision, closing on time
- Turning a transcript, recording, or raw notes into a record: decisions, action items, open questions, recap, formal minutes
- Follow-through: action items with owners and dates, the weekly sweep, chasing what slipped, escalating what stalled
- Meeting hygiene at the calendar level: killing standing meetings, declining, replacing a meeting with a written update
- Standing formats — 1-on-1s, standups, retros, planning, demos, all-hands, board and client calls, offsites — each with its own output and failure mode
- Mode: **act-as** by default (drafts the agenda, writes the record, sends the chase) and **advise** on request (coaches the user to run it themselves). Live-room moves in **Facilitation** and **Difficult conversations** are scripts for the human, not actions to take
- Not for note apps, vaults and sync (`notes`), day and calendar planning (`calendar-planner`), or maintaining the address book itself (`people`) — this covers the meeting, from the decision to hold it to the last closed action item

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| Meeting tomorrow and no idea what to bring | Prep brief: open items from last time, their likely asks, your three outcomes | **Preparation** |
| Asked to run a meeting with no agenda | Purpose type → one named output → timeboxes summing to ≤80% of the slot → cut the invite list | **Agendas** |
| Should this be a meeting at all? | Decide, generate, or build trust = meet. Inform, review, or update = write it | **Meeting load** |
| The calendar is full and nothing gets built | Load audit, the cost formula (Rule 2), decline and replace scripts | **Meeting load** |
| The room is talking in circles | Name the loop, restate the question on the table, apply the decision method | **Facilitation** |
| One person is taking all the airtime, or nobody speaks | Written-first round, direct redirect, silence held to 7 seconds | **Facilitation** |
| You are in the room but not the chair | Pre-wire before, first question in, objection in writing after | **Facilitation** |
| Meeting ended with no decision | The decider was absent, or nobody said who decides — fix the input, not the discussion | **Decision rights** |
| A decision is being relitigated for the third time | Decision log entry with its date, owner and rejected options; reopen only on new information | **Decision rights** |
| Transcript, recording, or scribbled notes to turn into a record | Decisions → actions → open questions; everything else is context and gets cut | **Recaps and minutes** |
| A recap, a summary email, or formal minutes has to go out | Recap shape by audience, and what formal minutes must contain | **Recaps and minutes** |
| Action items disappear after every meeting | Owner + date + definition of done, one ledger, one weekly sweep | **Follow-through** |
| Somebody owes you something and it is late | Escalation ladder: nudge → state the impact → involve the chair → re-scope | **Follow-through** |
| A standing meeting nobody wants to attend | Kill review: purpose, quarterly person-hour cost, what breaks if it is discontinued (Rule 7) | **Recurring meetings** |
| 1-on-1 that keeps turning into a status report | The report owns the agenda; status goes async; the manager brings one thing | **One-on-ones** |
| Standup, retro, planning, demo, or all-hands | Per-ritual timebox, output, and the specific way each one rots | **Team rituals** |
| Client, sales, vendor, investor, or board meeting | Pre-read, who speaks, minutes formality, follow-up SLA, next-step close | **External meetings** |
| Offsite, brainstorm, design review, or decision workshop | 1-2-4-all, brainwriting, dot voting, pre-mortem, and the facilitator's clock | **Workshops** |
| Remote or hybrid room where half the people are silent | One person one screen, chat as a first-class channel, rotate the painful slot | **Remote and hybrid** |
| Bad news, conflict, escalation, or a hostile stakeholder | Headline first, then sequence, ownership, and what is not negotiable | **Difficult conversations** |
| Anything else about a meeting | Name its purpose type and its single output, then work backwards from the output to the agenda | — |

Coverage map: **Meeting load** whether to meet at all · **Preparation** prep briefs · **Agendas** design and invite hygiene · **Facilitation** running the room · **Decision rights** who decides, the methods, the log · **Recaps and minutes** capture, recap, formal minutes · **Follow-through** action items, the sweep, chasing · **Recurring meetings** standing meetings and kill reviews · **One-on-ones** 1-on-1s, skip-levels, your own manager · **Team rituals** standup, retro, planning, demo, all-hands, incident review · **External meetings** client, sales, vendor, investor, board · **Workshops** offsites, generative sessions, design reviews · **Remote and hybrid** remote, hybrid, timezones, recording · **Difficult conversations** conflict, bad news, escalation, debriefs.

## Core Rules

1. **One owner, one purpose type, one named output.** Purpose types: **decide** (a named choice), **generate** (options that do not exist yet), **align** (a shared plan that survives contact), **build trust** (relationship, no artifact). If nobody can finish "after this meeting we will have ___", it is a document. The chair must be a single person — an unowned meeting drifts to whoever talks first.
2. **Price the room before you fill it.** Cost = `attendees × duration_hours × cost_per_attendee_hour`. Eight people for an hour at 80 USD/h is 640 USD, so a weekly one costs ~33k USD a year — that is the number that makes a fifth attendee a decision. Ceilings: decision rooms ≤8 (two-pizza rule); generative sessions ≤12 and only with breakouts; above that it is a broadcast and belongs in writing with a comment thread.
3. **Agenda and pre-read land ≥24h ahead, or the meeting is a status update in disguise.** Each agenda line is `output — owner — minutes`, rather than a topic noun. A pre-read is read *in the room*, in silence: budget ~2 minutes per page of dense narrative, so a 6-page memo buys 12-15 minutes of silence and saves the 20 minutes of someone reading it aloud badly.
4. **Timebox to 80% of the slot.** `sum(item minutes) ≤ 0.8 × slot`; the remaining 20% is the close (Rule 5), not slack. Default lengths are 25 and 50 minutes, not 30 and 60 — the gap is what makes the next meeting start on time. Parkinson is the mechanism: a 60-minute slot for a 20-minute decision fills to 60.
5. **Nothing leaves the room without owner, date, and definition of done.** "The team will look into it" is not an action item; "Priya sends the vendor comparison to the channel by Thu 30 Jul" is. Read them back out loud in the last five minutes while everyone can still object — an action item nobody heard assigned gets refused by email two days later.
6. **Decide who decides before the debate, not after it.** Set the method up front (`decision_method`): owner-decides after input, DACI, RAPID, or consent. Consensus is a legitimate choice for cheap reversible decisions in a group of ≤6; as a standing requirement it hands a veto to the most stubborn person in the room. One-way doors get the slow method; reversible calls get the fast one.
7. **Every standing meeting carries an expiry date.** Default review at 90 days, or ~13 occurrences for a weekly. Compute what it costs to keep: a weekly 1h with 8 attendees is `8 × 1 × 13` = 104 person-hours per quarter. It continues only if someone re-argues it against that number (**Recurring meetings**).
8. **Recap the same day, and send it wider than the room.** The recap is the minutes: decisions, actions with owners and dates, open questions, and nothing else. Send it to everyone affected, not just to attendees — the person who was not invited is exactly the one who will reopen the decision.

## Meeting Types

Defaults, not ceremony. Each row's failure mode is the reason it has its own page.

| Type | Output | Default length | Attendees | Depth |
|---|---|---|---|---|
| 1-on-1 | The report's blockers handled; one piece of feedback each way | 30 min weekly | 2 | **One-on-ones** |
| Standup | Blockers surfaced and picked up by name | 15 min, timeboxed (Scrum Guide) | ≤10 | **Team rituals** |
| Retrospective | 1-3 owned experiments, not a feelings log | 60-90 min per 2-week sprint | The team, no managers by default | **Team rituals** |
| Planning | A committed scope with named owners | ≤2h per 2-week sprint (Scrum Guide: 8h max per month of sprint) | The team | **Team rituals** |
| Decision meeting | One decision, recorded with its rejected options | 25-50 min | ≤8 | **Decision rights** |
| Design or code review | Accept, accept-with-changes, or reject, with the reason | 50 min | 3-6 | **Workshops** |
| Kickoff | Scope, roles, decision rights, and the first milestone | 60-90 min | Core team + sponsor | **Agendas** |
| Client status | Their risk register updated and the next step dated | 25 min | 2-4 per side | **External meetings** |
| Discovery / sales call | Their problem in their words, plus the qualifier answers | 25-50 min | 1-3 | **External meetings** |
| Board or steering | Decisions requiring the body, minuted formally | 90-120 min quarterly | Members + invited | **External meetings** |
| All-hands | Questions answered live that could not be answered in writing | 30-45 min | Everyone | **Team rituals** |
| Workshop / offsite | A tangible artifact by the end of the day | Half-day blocks | ≤12, in breakouts of 3-5 | **Workshops** |
| Interview debrief | Hire / no-hire per interviewer, written before anyone speaks | 25 min | The panel | **Difficult conversations** |
| Incident review | Timeline and systemic causes; write-up owned in the incident record | 60 min | Responders + one outsider | **Team rituals** |
| Any type not listed | Whatever "after this we will have ___" completes to | 25 or 50 min | Deciders and contributors only | Match its purpose type: decide → **Decision rights**, generate → **Workshops**, align → **Agendas**, build trust → **One-on-ones** |

## When A Meeting Fails

Decode rule: the symptom names the phase that broke. No output was named → design. Wrong people or no decider → invite list. Ran out of time → timeboxing. Nothing happened afterwards → the close.

| Symptom | Most likely cause | First move |
|---|---|---|
| Ended with "let's take it offline" | No decision method was set, or the decider was not in the room | Name the decider and the method at the top next time (Rule 6) |
| Same discussion as last month | The decision was made but left unrecorded, so it is not findable | Decision log entry, then reopen only on new information (**Decision rights**) |
| Ran 15 minutes over | Timeboxes summed to 100% of the slot, or the pre-read was read aloud | 80% rule (Rule 4); silent read for anything over one page |
| Everyone attended, nobody spoke | Broadcast disguised as a discussion, or the senior person spoke first | Written-first round; the chair speaks last (**Facilitation**) |
| Actions agreed, nothing shipped | No dated owner, or the ledger lives in the notes instead of one list | One ledger, one weekly sweep (**Follow-through**) |
| The real meeting happened afterwards in a DM | Someone could not disagree safely in the room | Pre-wire the objection, or make dissent a named agenda item (**Difficult conversations**) |
| The remote attendees ceased contributing | Room audio plus a shared laptop; chat unread | One person one screen, a chat monitor by name (**Remote and hybrid**) |
| Decision reversed a week later by someone absent | The recap went only to attendees | Send to everyone affected, ask for objections by a date (Rule 8) |
| Nobody prepared | The pre-read arrived under 24h before, or has arrived late so often that nobody looks | Send at ≥24h; if it slipped, read it in the room and say so |
| The client heard a commitment you did not make | No written next step went out same day | Recap with dates within 24h, theirs to correct (**External meetings**) |
| Anything else | Ask what the meeting was supposed to produce, and whether that thing exists now | Work backwards from the missing output |

## The Last Five Minutes

The close is what separates a meeting from a conversation. Reserve the final 20% of the slot (Rule 4) and run it in this order, out loud:

1. **Decisions**: "We decided X. Owner: Y. Method: owner-decides after input." Silence is not agreement — ask for objections by name if the decision is expensive.
2. **Actions**: read each one back as `owner — verb + object — date — done means`. Anything without all four is not an action item; either fix it now or drop it.
3. **Open questions**: what stayed unresolved, who chases the answer, by when.
4. **Next**: the next occurrence, or explicitly no next meeting. "We'll find time" is how a series dies quietly and reappears as a crisis.
5. **Record**: write the meeting record to `<state_root>/meetings/records/<year>-<mm>.md`, decisions to `<state_root>/meetings/decisions.md`, actions to `## Follow-Ups` in `<state_root>/meetings/memory.md`, and anyone new to the shared contacts — in the same turn, before the session ends.

## Output Gates

Before sending an agenda, a recap, minutes, or a chase:

- Does the agenda name one output per line, with an owner and minutes, and do the minutes sum to ≤80% of the slot?
- Does every action item carry owner, date, and definition of done — no "we should" and no team-as-owner?
- Is every decision recorded with who decided, by which method, and what was rejected?
- Is the recap going to everyone affected, not just to those who attended?
- For a remote or hybrid room: does each remote attendee have an equal channel, and is the recording question settled per `recording_consent`?
- Is anything in this text off the record, or a credential (join passcode, dial-in PIN, meeting password)? Then it is not written, or it is written as a pointer.
- Did anything durable come out of this — a meeting record, a decision, an action item, a series change, a person's context, an artifact? Then it is written to the matching Memory destinations row, with its `## Boxes` line when needed, in this same turn.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/meetings/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| default_role | chair \| participant | chair | Whether output is the agenda and the record, or a prep brief and influence moves for someone else's meeting (**Facilitation**) |
| meeting_length_default | 25-50 \| 30-60 \| 15-45 | 25-50 | The slot lengths every agenda and suggestion is built on, and the gap between back-to-back meetings (Rule 4) |
| decision_method | owner-decides \| daci \| rapid \| consent | owner-decides | The method stated at the top of a decision agenda and enforced in the close (Rule 6, **Decision rights**) |
| cost_per_attendee_hour | text (amount + currency) | none | Feeds the cost formula in Rule 2 and every kill review; while unset, state the assumed rate out loud instead of quoting a total |
| record_location | path | `<state_root>/meetings/records/` | Where meeting records are written; point it at a vault folder if the user keeps notes elsewhere |
| record_style | decisions-first \| full-notes \| verbatim | decisions-first | Shape of every record and recap in **Recaps and minutes**; `verbatim` keeps quotes for legal or board contexts |
| recap_policy | always \| when-decisions \| on-request | when-decisions | Whether a recap is drafted after every meeting, only after ones that produced a decision or action, or only on request |
| recording_consent | ask \| announce \| team-default-ok | ask | Whether recording or transcribing is proposed, announced, or assumed inside the team (**Remote and hybrid**) |
| follow_up_sweep_day | weekday | Friday | The day the `## Due` sweep of open action items runs (**Follow-through**) |
| series_review_days | number (30-365) | 90 | The expiry clock on every standing meeting (Rule 7, **Recurring meetings**) |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — video, calendar and chat platforms, where transcripts come from, whether invites carry the agenda in the body — affects the shape of every example and where the record is expected to live
- **Conventions** — invite title scheme, agenda template, action-item syntax, record file naming, tags for series and clients — affects generated agendas, recaps and record filenames
- **Platform** — timezone, working hours, week start, the language records are written in, distributed vs co-located team — affects scheduling suggestions and **Remote and hybrid**
- **Confidentiality posture** — which series are exempt from recording or stored, what gets redacted before a recap, who is allowed on the distribution list — affects the Output Gates and what is written at all
- **Output register** — recap length, bullets vs prose, whether the reasoning is kept or only the conclusion, first person vs third — affects every artifact this skill emits
- **Cadence** — follow-up sweep, series kill review, 1-on-1 frequency per report, meeting-load audit, skip-level rhythm — every accepted cadence becomes a row in the `## Due` table of `<state_root>/meetings/memory.md`
- **Escalation** — how many nudges before naming the impact, who the escalation path runs through, how hard to push on a late external party — affects the ladder in **Follow-through**

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Round-robin status as the agenda | N people each speak to 1 person while N−2 wait; the information was writable | Written status before; the meeting handles only what the writing exposed (**Team rituals**) |
| Inviting people "for visibility" | Every optional attendee reads themselves as required, and the room crosses the decision ceiling | Send them the recap instead; visibility is a distribution problem (Rule 8) |
| An agenda of topic nouns | "Roadmap" has no end state, so the item ends when the clock does | `output — owner — minutes` per line (Rule 3) |
| Booking 60 minutes because the calendar suggests it | Parkinson fills it, and back-to-backs eat the buffer | 25/50 defaults; ask what the 20-minute version would cut |
| Deciding by consensus to defer a hard call | The most stubborn person gets a veto and the decision surfaces again in a month | Name the decider and the method up front (Rule 6) |
| Letting the most senior person speak first | Anchors the room; juniors then confirm rather than contribute | Written-first, then round, chair last (**Facilitation**) |
| The chair also takes the notes | Facilitating and scribing compete; one of them collapses, usually the notes | Rotate a scribe, or record the close only and write the record after (**Recaps and minutes**) |
| Recording the meeting instead of deciding | A recording nobody rewatches replaces a decision nobody made | Record decisions, not audio; the transcript is raw material, leaving the record solely for decisions |
| Chasing action items in DMs | Invisible to everyone else, so the same item gets chased twice or forgotten entirely | One ledger, one weekly sweep (**Follow-through**) |
| "Any other business" left open at the end | Reopens settled items when everyone is tired and the decider has left | AOB collected at the start and timeboxed, or dropped |
| Treating silence as agreement | Disagreement moves to the corridor and returns as a reversal | Ask by name; make dissent a named agenda item (**Difficult conversations**) |
| Rescheduling a 1-on-1 more than once | The report reads it as a ranking, and the honest conversation ceases to arrive | Shorten it instead of moving it; ensure consecutive ones remain scheduled (**One-on-ones**) |
| Always taking the timezone slot that suits you | The same people join at 22:00 every week and quietly disengage | Rotate the painful slot on a fixed schedule; the schedule goes in `## Meeting Norms` and the series row in `## Series` (**Remote and hybrid**) |
| Sending the recap only to attendees | The absent decision-maker reopens it a week later | Everyone affected, with an objection deadline (Rule 8) |
| A standing meeting with no end date | It outlives its purpose by quarters because cancelling it is nobody's job | Expiry date at creation, kill review on the clock (Rule 7) |

## Where Experts Disagree

- **Async-first vs high-frequency sync.** Distributed, writing-strong teams replace most status meetings with documents and keep sync for decisions and trust; teams with weak writing or high ambiguity move faster with short daily contact. The frontier is whether a written update actually gets read and answered within a day — if it does not, the meeting is doing work the document cannot.
- **Who owns the notes.** Rotating human scribe (best comprehension, costs an attendee), the chair (worst: facilitation collapses), or a transcript turned into a record afterwards (cheapest, but only if someone edits it — a raw transcript is not minutes). Pick per meeting type, not per team.
- **Cameras on.** On builds the trust that carries hard conversations; off reduces fatigue and levels bandwidth-poor participants. Defensible boundary: on for 1-on-1s, first meetings and conflict; optional for recurring internal syncs.
- **Recording by default.** Full recording gives absent people fidelity and settles "who agreed to what"; it also measurably flattens candour on personnel, legal and strategy topics. Exclude 1-on-1s and performance conversations from recording or a performance conversation, and note that some jurisdictions require every participant's consent, not just the host's (**Remote and hybrid**).
- **Standups daily or not at all.** Daily suits work with tight coupling and frequent handoffs; twice-weekly or async suits senior teams with independent workstreams. The signal to change is not boredom, it is whether blockers get picked up the same day.
- **Consensus vs single-owner decisions.** Consent-based rooms (object only if you can name a harm) move faster than consensus and slower than an owner deciding; the frontier is reversibility. One-way doors earn the slower method.

## Essential Practices

- Name one owner, one purpose type, and one output before the invite goes out.
- Price the room, keep decision rooms small, and send visibility through the recap instead of the invite list.
- Close every meeting with decisions, dated owners, open questions, and the next occurrence or an explicit stop.
- Write durable records, decisions, and follow-ups into the resolved `<state_root>` tree in the same turn.
- Propose recording only under the configured consent rule, and store join secrets as pointers rather than raw credentials.

## Related Skills

- `notes` — note apps, vaults, and retrieval once the meeting artifact must live outside the meeting ledger
- `people` — durable attendee context, birthdays, and relationship history in the shared address book
- `calendar-planner` — calendar conflicts, focus protection, and weekly schedule repair around the meeting load
- `summarizer` — compress a long transcript or document while preserving claims and decisions
- `decide` — durable decision logs and autonomous decision patterns beyond a single meeting close

## Security & Privacy

**Third-party data:** meeting records hold other people's names, roles and words. Names, roles, companies, decisions and action items are working data: people go to `<state_root>/contacts/contacts.md`, what happened to `<state_root>/meetings/records/<year>-<mm>.md`, decisions to `<state_root>/meetings/decisions.md`, commitments to `## Follow-Ups` in `<state_root>/meetings/memory.md`. Anything the user marks off the record, plus compensation figures, performance ratings, health details, legal advice and unannounced personnel changes, is not written to disk at all — summarize the decision without the content, or keep nothing.

**Credentials:** join links with embedded passcodes, dial-in PINs, meeting passwords and secret calendar URLs are credentials and must remain excluded from under `<state_root>/`. Store the pointer, strip the value.

**Local storage:** preferences, memory, records, decisions and follow-ups stay in `<state_root>/meetings/` on this machine, plus attendee rows in the shared `<state_root>/contacts/` and project references in `<state_root>/projects/`. Nothing is transmitted anywhere.

**Recording:** governed by `recording_consent`, default `ask`. Recording or transcribing is proposed to the user and announced to the room, requiring explicit confirmation — some jurisdictions require consent from every participant.
