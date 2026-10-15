# Memory Template — Mixpanel

Create `<state_root>/memory.md` with this structure:

```markdown
# Mixpanel Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Project
<!-- Product context learned from conversations -->

## Key Events
<!-- Events and cohort ids the user tracks -->

## Saved Queries
<!-- Frequently reused selectors / report ids -->

## Insights
<!-- Notable findings from analysis -->

---
*Updated: YYYY-MM-DD*
```

Optional saved-query notes live at `<state_root>/queries/<name>.md` and should
record endpoint, params, and interpretation — never credentials.

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning their setup | Gather context from queries |
| `complete` | Know their product well | Focus on analysis |
| `paused` | User declined right now | Work with what you have |

## Principles

- Learn events from actual queries instead of asking for exhaustive lists
- Save useful insights for later sessions
- Keep credentials exclusively in environment variables
