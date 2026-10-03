# Memory Template - Orlando

Create `<state_root>/memory.md` with this structure:

```markdown
# Orlando Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Context
<!-- What you know about their Orlando situation -->
<!-- Visitor, conference traveler, resident, relocator, remote worker, family -->
<!-- Trip dates, move timeline, budget, and anchors such as parks, airport, or Downtown -->

## Place Fit
<!-- Hotel zones, neighborhoods, school districts, or commute corridors they care about -->
<!-- Car tolerance, toll tolerance, and airport frequency if relevant -->

## Notes
<!-- Preferences learned from conversation -->
<!-- Open questions, risks, and next actions to remember -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Gather context opportunistically |
| `complete` | Has enough context | Work normally |
| `paused` | User said "not now" | Wait for user to resume |
| `never_ask` | User said pause | Honor user request to cease inquiry |

## Key Principles

- **No config keys visible** - use natural language observations, not robotic settings
- **Learn from behavior** - notice patterns across trips or move decisions, gather context naturally
- **Most stay `ongoing`** - Orlando needs shift over time, that is normal
- Update `last` on each use
