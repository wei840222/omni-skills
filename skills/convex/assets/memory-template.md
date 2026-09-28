# Memory Template - Convex

After resolving `<state_root>` and obtaining persistence consent, create the optional concise summary `<state_root>/memory.md` with this structure. Keep detailed schema, rollout, and permission decisions in their corresponding topic notes.

```markdown
# Convex Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Project Context
<!-- Repos and environments using Convex -->
<!-- Product domain and lifecycle stage -->

## Data Model Decisions
<!-- Concise summary; detailed table/index rationale in <state_root>/schema-notes.md -->

## Index Strategy
<!-- Summary of critical access paths; details in <state_root>/schema-notes.md -->

## Auth and Permissions
<!-- Summary of identity and tenant boundaries; details in <state_root>/auth-notes.md -->

## Rollout and Incidents
<!-- Summary of current rollout risk; details in <state_root>/rollout-notes.md -->

## Notes
<!-- Durable, high-signal implementation lessons -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Default learning state | Keep collecting technical context |
| `complete` | Stable context available | Use memory as primary defaults |
| `paused` | User wants fewer prompts | Ask only when critical data is missing |
| `never_ask` | User rejected setup prompts | Stop prompting and operate with existing context |

## Integration Values

| Value | Meaning |
|-------|---------|
| `pending` | Activation preference not confirmed |
| `done` | Activation preference confirmed |
| `declined` | User wants manual activation only |

## Key Principles

- Store decisions that improve future Convex work, not raw chat logs.
- Keep memory concise and implementation-focused.
- Redact secrets and sensitive identifiers before saving notes.
- Update `last` whenever memory is edited.
