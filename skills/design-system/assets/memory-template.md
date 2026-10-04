# Memory Template — Design System

Create `<state_root>/memory.md` with this structure after first-write consent:

```markdown
# Design System Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
<!-- Stack and platforms -->
<!-- Existing patterns to preserve -->
<!-- Team size and workflow -->

## Decisions
<!-- Key decisions and why -->
<!-- Token naming conventions -->
<!-- Component API patterns -->

## Notes
<!-- Preferences to keep consistent -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning their system | Gather context, suggest patterns |
| `complete` | System is established | Maintain consistency, extend carefully |
| `paused` | User said not now | Work with what you have |
| `never_ask` | User said stop | Do not solicit more context |

## Principles

- Use plain language in Context and Notes
- Update `last` on meaningful use
- Keep all learned data under the resolved `<state_root>/`
- Never write the literal string `<state_root>` to disk
