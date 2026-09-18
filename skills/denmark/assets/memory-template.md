# Memory Template - Denmark

Create `<state_root>/denmark/memory.md` with this structure:

```markdown
# Denmark Trip Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | silent_mode

## Trip Snapshot
- Dates:
- Duration:
- Arrival and departure gateway:
- Travelers:
- Kids:
- Mobility notes:

## Route Direction
- Main corridor: [Copenhagen-only / capital-region-plus-Zealand / Funen / Aarhus-east-Jutland / north-Jutland / southwest-Jutland / Bornholm / mixed]
- Confirmed bases:
- Open route questions:
- Rail preference: [low / medium / high]
- Driving comfort: [none / occasional / comfortable]
- Ferry tolerance: [low / medium / high]

## Preferences
- Trip style:
- Budget:
- Pace:
- Food priorities:
- Museum or design priorities:
- Cycling priorities:
- Coast or beach priorities:

## Conditions
- Cold tolerance:
- Rain and wind tolerance:
- Must-see places:
- Omit:
- Urban vs nature balance:

## Bookings and Deadlines
| Item | Needed by | Status | Notes |
|------|-----------|--------|-------|
| Entry docs | | | |
| Flights or rail arrival | | | |
| Ferries or bridges | | | |
| Hotels | | | |
| Car rental or bike rental | | | |
| Attractions or museum passes | | | |

## Working Plan
- Current route draft:
- Backup plan:
- High-risk links:

## Notes
- Durable observations only.
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | still learning trip shape | ask only high-impact follow-ups |
| `complete` | core context is stable | act quickly from saved defaults |
| `paused` | memory use paused | keep focused on current tasks |
| `silent_mode` | user requested skipping setup prompts | skip future setup questions |

## Key Principles

- Save route logic and logistics constraints, not casual travel chatter.
- Preserve season, corridor, and transport model because they determine almost every Denmark plan.
- Keep changing details in the bookings table, not scattered notes.
- Replace old guesses once dates, bases, or ferry and car choices become fixed.
