# Memory Template — Anki

Create `<state_root>/memory.md` with this structure:

```markdown
# Anki Memory

## Status
status: ongoing
last: YYYY-MM-DD

## Collection
<!-- Subject and level, deck names and structure, tag scheme, note types in use -->
<!-- Client they study on; add-ons allowed or not -->

## Numbers Observed
<!-- reviews_per_card, seconds_per_review, current new/day and review cap -->
<!-- Measured from stats they shared, with the date — these drive every workload estimate -->

## Dates
<!-- Exam or deadline dates that trigger the capacity math -->

## Pain Points
<!-- Backlogs, leech clusters, sync incidents, imports that went wrong -->

## Preferences
<!-- Cutting aggressiveness, confirmation before destructive operations -->
<!-- Explanation depth, output format quirks not covered by config.yaml -->

---
*Updated: YYYY-MM-DD*
```

Config vs memory: `<state_root>/config.yaml` holds what the user declares (the Configuration table of `SKILL.md`); this file holds observations. An observation never overwrites a declared preference without user confirmation.

## Status Values

| Value | Meaning |
|-------|---------|
| `ongoing` | Still learning their collection and workload |
| `complete` | Structure, numbers, and deadlines known |
