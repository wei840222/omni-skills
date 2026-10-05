# Memory Template - Discover

Create `<state_root>/memory.md` with this structure:

```markdown
# Discover Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- What the user tends to explore and why those topics matter
- When discovery should activate automatically and when it should stay quiet

## Discovery Preferences
- Preferred mix of opportunities, warnings, comparisons, operators, or contrarian angles
- Preferred autonomy level: on request, suggestive, or heartbeat-backed
- Sources to prefer, if explicit

## Notes
- Stable observations that improve future discovery work
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Discovery is active | Keep reading memory on activation |
| `paused` | Bypass discovery | Only use when user asks directly |
| `complete` | Setup is stable | Use normal workflow |
| `never_ask` | Bypass setup-style questions | Infer from active work only |
