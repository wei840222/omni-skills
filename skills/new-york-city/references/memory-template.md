# New York City Memory

Create `<state_root>/memory.md` with this structure only if the user wants continuity across sessions:

```markdown
# New York City Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Current Situation
- Mode: visitor / moving / resident / work-study
- Main borough:
- Neighborhood or base:
- Airport / station / commute anchor if known:

## Constraints
- Timeline:
- Budget pressure:
- Housing or hotel constraints:
- Commute, walking, and transit realities:
- Family, safety, or accessibility needs:

## Open Loops
- Task:
- Waiting on:
- Next deadline:

## Notes
- Natural-language observations that improve future NYC advice

---
Updated: YYYY-MM-DD
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning context | Keep gathering high-signal details naturally |
| `complete` | Enough stable context exists | Reuse what is already known before asking |
| `paused` | User prefers no further setup right now | Help with the current task and keep intake limited to an explicit request |
| `never_ask` | User does not want this tracked | Stop collecting new background unless asked |

## Key Principles

- Keep notes in natural language, not config-style keys.
- Borough, neighborhood, and commute anchor matter more than a generic "NYC" label.
- Save only details that will materially improve the next New York City answer.
- Keep the default memory coarse. Record full building details or sensitive identifiers only when the user explicitly requests that continuity level.
- Update `last` on each meaningful use.
