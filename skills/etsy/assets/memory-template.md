# Memory Template - Etsy

File shapes for durable state under `<state_root>/`. Create a file only when that data is needed.

## `<state_root>/memory.md`

```markdown
# Etsy Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Shop Context
- Core products:
- Ideal buyer profile:
- Main markets and shipping constraints:
- Target price bands:

## Goals and Constraints
- Primary objective right now:
- Margin constraints:
- Capacity constraints:
- Compliance sensitivities:

## Active Experiments
- Name:
  hypothesis:
  variable_changed:
  start_date:
  success_metrics:
  status: planned | running | completed | paused

## Notes
- Durable observations worth reusing

---
*Updated: YYYY-MM-DD*
```

## `<state_root>/listing-experiments.md`

```markdown
# Listing Experiments

## YYYY-MM-DD - [Experiment Name]
listing_scope:
baseline:
change_applied:
window:
results:
decision: keep | revert | iterate
```

## `<state_root>/launch-checklists.md`

```markdown
# Launch Checklists

## Pre-Launch
- Listing title clarity verified
- Photos show product use context
- Price and shipping checks completed (fee-aware margin noted)
- Tags mapped to buyer intent clusters
- Policy/IP risk scan completed

## Post-Launch
- Initial metrics captured at 24h and 7d
- Customer questions reviewed for messaging gaps
- Next iteration hypothesis documented
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Default state | Keep learning stable shop context |
| `complete` | Context is stable | Reuse defaults unless user changes direction |
| `paused` | User wants lower overhead | Save only critical updates |
| `never_ask` | User opted out of persistence | Operate statelessly |
