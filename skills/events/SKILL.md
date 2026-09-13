---
name: events
description: Track and organize personal events, concerts, conferences, parties, appointments, multi-day itineraries, hosting RSVPs, and annual recurring dates. Use when the user wants to log an upcoming event, surface what is coming up, capture tickets or confirmation numbers, plan hosting guest lists, maintain birthday/annual lists, or migrate a personal event workspace. Route calendar CRUD on macOS to `apple-calendar-macos`, timed nudges to `remind`, free-form life writing to `journal`, and whole-life capacity planning to `productivity`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📅"}'
  related-skills: '{"remind":"Fires timed nudges for known commitments; events owns durable event records and logistics.","apple-calendar-macos":"Creates or edits macOS Calendar entries when the user wants system calendar sync.","journal":"Reflective writing and memories after an event ends.","habits":"Recurring practices and streaks rather than dated one-off events.","productivity":"Whole-life capacity and priority tradeoffs beyond a single event.","notes":"General retrieval notes unrelated to dated event logistics.","travel-planning":"Trip design and booking research that may feed multi-day event folders."}'
---

## State location

Resolve `<state_root>` once per invocation before any event read or write:

1. Use an explicitly configured events-state path when the host or user supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/events/`, `<workspace>/memory/events/`, `~/events/`, then migrate-from candidates `~/Clawic/data/events/` and `~/clawic/events/` only when moving legacy data.
3. If multiple candidates exist, keep the highest-precedence directory, leave others independent, and tell the user which location was selected.
4. If none exists and the user asks to persist an event, create `<workspace>/events/` and use it as `<state_root>`.

Use only the selected `<state_root>` for every state path in this skill. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path. If legacy data sits only under `~/Clawic/data/events/` or `~/clawic/events/`, move it into the selected `<state_root>` and say in one line that you moved it and from where.

```text
<state_root>/
├── upcoming/
│   ├── concerts/
│   ├── conferences/
│   ├── social/
│   └── appointments/
├── hosting/
├── past/
├── annual/
│   └── recurring.md
└── calendar.md
```

## When to use

- User mentions a concert, conference, party, appointment, show, or meetup and wants it tracked
- User asks what is coming up this week/month, or needs doors/ticket/RSVP details surfaced
- User is hosting and needs guest lists, checklists, or follow-ups
- User wants birthday/anniversary/annual conference dates kept as recurring anchors
- Multi-day events need an overview plus day-by-day schedule folder
- Not for creating timed notification jobs (`remind`), editing the OS calendar directly (`apple-calendar-macos`), or free-form life journaling (`journal`)

## Operating loop

1. **Capture first** — if the user is describing an event, write or update the entry before long planning monologues.
2. **Resolve state** — select `<state_root>`, create missing category folders only when writing.
3. **Classify** — concert / conference / social / appointment / hosting / multi-day / annual; load `references/templates.md` for file shape.
4. **Required fields** — date/time, location or venue, tickets or confirmation numbers when they exist, logistics (doors, parking, dress code), companions, and RSVP state when hosting.
5. **Surface lightly** — upcoming prompts should lead with the soonest actionable detail (doors time, registration deadline, guest count).
6. **Lifecycle** — after the event ends, move the file to `past/` (or archive the hosting folder) and offer one optional memory note via `journal` only if the user wants reflection.
7. **Calendar bridge** — when the user wants the same item on macOS Calendar, hand off create/update to `apple-calendar-macos` after the durable file exists here.
8. **Reminder bridge** — when the user wants a timed nudge (registration closes, leave-for-venue), hand the commitment to `remind` with the exact fire time; keep logistics ownership here.

## Quick reference

| Need | Action | Load |
|---|---|---|
| New single event | Write under `upcoming/<category>/` | `references/templates.md` |
| Hosting party | Folder under `hosting/` with overview + guests + details | `references/templates.md` |
| Multi-day conference | Folder with `overview.md` + `schedule.md` | `references/templates.md` |
| Birthdays / annual | Update `annual/recurring.md` | `references/templates.md` |
| "What's next?" | Read `calendar.md` and `upcoming/**`, sort by date | `references/workflows.md` |
| Registration / ticket risk | Check deadlines and confirmation fields | `references/workflows.md` |
| Domain sources | Verify event-ops guidance claims | `references/sources.md` |

## Capture rules

- Prefer structured files over chat-only memory; chat is the intake channel, disk is the system of record.
- Always record confirmation numbers, ticket section/row, registration IDs, and order emails when the user has them.
- Note registration deadlines and leave-by times as first-class fields, not buried prose.
- Keep RSVP lists current when hosting: confirmed / pending / declined with follow-up notes.
- Document logistics: parking, doors, bag policy, dress code, accessibility, who you meet and where.
- For multi-day events, keep one overview (travel, lodging, registration) and a day-by-day schedule file.
- Never invent ticket inventory, prices, or venue rules the user did not provide; look them up only when asked and cite the source.

## Surface rules

- Lead with the nearest deadline or start time: "Concert next week — doors 7pm", "Mom's birthday in 5 days", "Registration closes tomorrow", "15 confirmed for Saturday".
- When multiple items collide on one day, list them chronologically with venue + one logistics hook each.
- If `calendar.md` is stale relative to `upcoming/`, rebuild the month view from files before answering.
- Past events stay out of "what's next" answers unless the user asks for history or memories.

## Failure modes

| Signal | Response |
|---|---|
| User dumps a partial event ("show Friday") | Capture what exists; ask only for date/time + venue gaps that block usefulness |
| Missing confirmation after purchase talk | Flag the gap explicitly; do not pretend the ticket is filed |
| Hosting RSVP chaos | Rebuild guests.md buckets; one follow-up message draft at a time |
| Wants a push notification | Create/update the event file, then route timing to `remind` |
| Wants it on Apple Calendar | Keep file here; call `apple-calendar-macos` for the calendar object |
| Legacy `~/Clawic/data/events/` only | Migrate once to `<state_root>` and confirm the path |
| Event already over still under upcoming/ | Move to `past/` and offer optional journal note |

## Guardrails

- No payment card numbers, government IDs, or account passwords in event files; store order/confirmation IDs only.
- Do not auto-email guests or post RSVPs without explicit user send approval.
- Do not delete past event folders without confirmation; archive moves are preferred.
- Venue safety, protest, or medical-emergency logistics are out of scope for improvisation — capture user-stated plans only.
- Skill references are read-only guides; mutable state lives exclusively under `<state_root>/`.
