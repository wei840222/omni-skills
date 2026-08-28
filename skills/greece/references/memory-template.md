# Memory Template - Greece

Create `<state_root>/memory.md` with this structure:

```markdown
# Greece Trip Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | skip_setup

## Trip Snapshot
- Dates:
- Duration:
- Arrival and departure airports:
- Travelers:
- Kids:
- Mobility notes:

## Route Direction
- Main cluster: [Athens-Attica / Cyclades / Crete / Ionian / Peloponnese / North]
- Confirmed bases:
- Open route questions:
- Ferry tolerance: [low / medium / high]
- Driving comfort: [none / local only / road-trip ready]

## Preferences
- Trip style:
- Budget:
- Pace:
- Food priorities:
- Beach priorities:
- Archaeology priorities:
- Nightlife priorities:

## Conditions
- Heat tolerance:
- Wind or sea sensitivity:
- Swim confidence:
- Must-see places:
- Must-skip:

## Bookings and Deadlines
| Item | Needed by | Status | Notes |
|------|-----------|--------|-------|
| Entry docs | | | |
| Ferries | | | |
| Flights | | | |
| Hotels | | | |
| Car rental | | | |
| Site tickets | | | |

## Working Plan
- Current route draft:
- Backup plan:
- Last-night protection:

## Notes
- Durable observations only.
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | still learning trip shape | ask only high-impact follow-ups |
| `complete` | core context is stable | act quickly from saved defaults |
| `paused` | memory use paused | expand only when requested |
| `skip_setup` | no setup prompts wanted | proceed without setup questions |

## Key Principles

- Save route logic and constraints, not casual travel chatter.
- Keep changing details in the bookings table, not scattered notes.
- Replace stale guesses once dates, ferries, or hotels become fixed.
- Preserve transport tolerance because it determines almost every Greece itinerary choice.
