# Memory Template — NumPy

Create `<state_root>/memory.md` with this structure only after the user wants
persistent preferences. Resolve `<state_root>` per `SKILL.md` before writing.

```markdown
# NumPy Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Context
<!-- experience: beginner | intermediate | advanced -->
<!-- use_cases: data science, scientific computing, ML, general -->

## Preferences
<!-- default_dtype: float32 | float64 -->
<!-- memory_priority: speed | memory | balanced -->

## Common Patterns
<!-- Patterns the user explicitly asks to save -->

## Notes
<!-- Workflow remarks the user volunteered -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning preferences | Ask when relevant |
| `complete` | Preferences known | Work normally |
| `paused` | User said “not now” | Keep quiet; use what exists |
| `never_ask` | User said stop | No further preference prompts |

## Principles

- Update `last` on each significant preference change
- Save only information the user explicitly shares
- Optional snippets go under `<state_root>/snippets/`
- Never write runtime state into the skill package directory
