# Memory Template - Consultant

Create `<state_root>/consultant/memory.md` with this structure:

```markdown
# Consultant Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Primary role or business context:
- Current top priorities:
- Known constraints (budget, team, time, compliance):
- Decision horizon and urgency:

## Preferences
- Preferred output format:
- Preferred depth:
- Communication style:

## Stakeholders
- Key decision owner(s):
- Influencers/blockers:
- Approval path:

## Active Engagements
- [name]: objective, phase, next milestone, review date

## Notes
- Durable observations that improve future recommendations

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep learning from each task |
| `complete` | Core context is stable | Execute with minimal clarification |
| `paused` | User deferred setup questions | Pause setup prompts, focus on task work |
| `bypass_setup` | User declined setup prompts | Bypass setup prompts unless requested |

## Memory Rules

- Keep entries factual, reusable, and concise
- Replace outdated assumptions instead of stacking contradictions
- Store only consulting-relevant context
- Store only public or task-relevant consulting context
- Update `last` on each meaningful interaction
