# Memory Template - Bali

Create `<state_root>/memory.md` with this structure:

```markdown
# Bali Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Context
- Why the user cares about Bali right now
- Current timeline (trip, move, scouting)
- Primary neighborhood candidates

## Planning Profile
- Profile: visitor | resident | remote-worker | student | founder | family | mixed
- Budget tier: low | mid | high
- Risk tolerance: conservative | balanced | aggressive
- Mobility: transit-first | ride-hailing | scooter | driver | car

## Active Constraints
- Visa or legal constraints
- Health or insurance constraints
- Family or school constraints
- Work and time-zone constraints
- Climate / Nyepi / peak-season constraints

## Next Decisions
- Decision currently blocked
- Information needed to unblock
- Date-sensitive steps

## Notes
- Durable preferences observed from behavior
- Lessons from prior recommendations

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep collecting context naturally |
| `complete` | Core context is stable | Focus on execution details |
| `paused` | User paused setup | Stop setup prompts, continue task support |
| `never_ask` | User does not want setup questions | Do not ask activation/setup questions unless requested |

## Key Principles

- Keep memory short, concrete, and useful in future turns.
- Prefer observed behavior over speculative assumptions.
- Update `last` whenever constraints or priorities change.
