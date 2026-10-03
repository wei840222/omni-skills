# Memory Template — Las Vegas

Create `<state_root>/memory.md` with this structure:

```markdown
# Las Vegas Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## User Context
<!-- What you know about their relationship with Vegas -->

Type: visitor | potential_mover | resident | remote_worker
Timeline: (trip dates or move timeline if known)
Location: (where they're coming from if known)

## Interests
<!-- What aspects of Vegas they care about -->

- Entertainment: (shows, clubs, sports, etc.)
- Food: (preferences, budget)
- Outdoors: (hiking interest, heat tolerance)
- Neighborhoods: (areas they're interested in)
- Budget level: luxury | moderate | budget

## Work/Life Context
<!-- If relevant to their questions -->

Work: (remote, hospitality, tech, etc.)
Family: (solo, couple, family with kids)

## Trip Notes
<!-- For visitors - specific trip context -->

Dates:
Hotel:
Purpose: (vacation, bachelor party, convention, etc.)
Party size:

## Move Notes
<!-- For potential movers - relocation context -->

Reason:
Target timeline:
Budget range:
Must-haves:
Deal-breakers:

## Preferences Learned
<!-- Things you've learned from conversation -->

- (Add observations as you learn them)

## Notes
<!-- Internal observations, things to remember -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Gather context opportunistically |
| `complete` | Have enough context | Work normally |
| `paused` | User said "not now" | Work strictly with existing context |
| `skip_prompts` | User declined prompts | Proceed without requesting further context |

## Key Principles

- **No config keys visible** — use natural language, not "budget: moderate"
- **Learn from conversation** — observe and confirm preferences organically
- **Most users stay `ongoing`** — always learning, that's fine
- Update `last` on each use
