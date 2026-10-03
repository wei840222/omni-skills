# Memory Template — Help Center

Create `<state_root>/memory.md` from this structure after the user consents to the real resolved path:

```markdown
# Help Center Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
<!-- Company support model, audience, channel mix, and constraints -->

## Current Stack
<!-- Existing provider/tools and key integration dependencies -->

## Decisions
<!-- Approved choices with rationale and date -->

## Rejected Options
<!-- Options declined and why -->

## Risks
<!-- Open risks, blockers, and mitigation owners -->

## Next Milestones
<!-- Next steps with target dates -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
| --- | --- | --- |
| `ongoing` | Context still evolving | Keep collecting constraints and decisions |
| `complete` | Initial operating model defined | Focus on execution and iteration |
| `paused` | User deferred planning | Keep context; answer only when asked |
| `skip_setup` | User opted out of setup prompts | Execute only direct requests; skip durable prompts |

## Storage rules

- Write only user-approved decisions and explicit constraints.
- Update `last` on each durable skill use.
- Keep entries concise and action-oriented.
- Optional files (`provider-score.md`, `content-inventory.md`, `rollout-log.md`) are created only when that work actually starts.
