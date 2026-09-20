# Memory Template - Bulgaria

Create `<state_root>/data/bulgaria/memory.md` with this structure:

```markdown
# Bulgaria Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Trip stage:
- Dates or season:
- Cities or regions:
- Group:
- Pace and budget:

## Preferences
- Likes:
- Dislikes:
- Food notes:
- Mobility or hiking notes:

## Plans and Bookings
- Confirmed:
- Considering:

## Notes
- Specific recommendations already given
- Follow-up questions for next time

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Keep collecting context naturally |
| `complete` | Enough context exists | Recommend directly and update quietly |
| `paused` | User does not want more setup right now | Help with what is known |
| `never_ask` | User prefers direct answers | Proceed without asking for more setup context |

## Principles

- Keep observations in natural language
- Update `last` whenever the skill is used
- Store only information that improves future Bulgaria recommendations
- Keep memory focused on actionable travel constraints
