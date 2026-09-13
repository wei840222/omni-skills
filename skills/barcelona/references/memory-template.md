# Memory Template — Barcelona

Create `<state_root>/barcelona/memory.md` with this structure after resolving `<state_root>` per `SKILL.md`:

```markdown
# Barcelona Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Context
<!-- What you know about their Barcelona situation -->
<!-- Role: visitor, resident, tech worker, student, founder -->
<!-- Nationality: visa implications -->
<!-- Timeline: when visiting, when moving, how long there -->
<!-- Language: Spanish / Catalan / English comfort -->

## Neighborhoods
<!-- Areas they're interested in or considering -->
<!-- Budget constraints if any -->

## Notes
<!-- Preferences learned from conversations -->
<!-- Things to remember for future interactions -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Gather context opportunistically |
| `complete` | Has enough context | Work normally |
| `paused` | User said "not now" | Proceed using existing context without asking |
| `skip_asking` | User requested to discontinue | Proceed without requesting more context |
