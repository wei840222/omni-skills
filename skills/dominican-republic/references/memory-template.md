# Memory Template - Dominican Republic

Use this file only after resolving `<state_root>` via `SKILL.md`. Create
`<state_root>/memory.md` with this structure when durable trip context must
persist.

```markdown
# Dominican Republic Trip Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Trip Snapshot
- Dates:
- Duration:
- Arrival and departure airports:
- Travelers:
- Kids:
- Mobility notes:

## Route Direction
- Main base or coast:
- Backup base:
- Open region questions:
- Resort or independent bias:
- Transfer tolerance: [low / medium / high]
- Driving comfort: [none / daylight only / comfortable]

## Preferences
- Trip style:
- Budget:
- Pace:
- Water priorities:
- Food priorities:
- Nightlife priorities:
- Nature or adventure priorities:

## Conditions
- Must-see places:
- Exclude preferences:
- Heat tolerance:
- Rain tolerance:
- Hurricane-season flexibility:
- Surf or rough-water comfort:

## Bookings and Deadlines
| Item | Needed by | Status | Notes |
|------|-----------|--------|-------|
| Entry steps | | | |
| Flights | | | |
| Hotels or resorts | | | |
| Airport transfers | | | |
| Car rental | | | |
| Tours or boat days | | | |

## Working Plan
- Current route draft:
- Weather backup:
- High-risk links:

## Notes
- Durable observations only.
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | still learning trip shape | ask only high-impact follow-ups |
| `complete` | core context is stable | act quickly from saved defaults |
| `paused` | memory use paused | keep responses concise and skip memory expansion |
| `never_ask` | no setup prompts wanted | bypass future setup questions |

## Key Principles

- Save coast choice, water fit, and transfer tolerance because they decide most Dominican Republic plans.
- Preserve airport, resort, and driving decisions because they create the biggest downstream friction.
- Replace guesses once flights, hotels, and transport become fixed.
- Avoid storing credentials, full passport numbers, payment card data, or third-party private contact details.
