---
name: fishing
description: Track fishing trips, log catches, save spot patterns, and get personalized gear recommendations. Use when planning fishing trips, recording catches, or asking for tackle advice.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎣"}'
---


## State location

Fishing state may exist in `<workspace>/fishing/`, `<workspace>/memory/fishing/`, or `~/fishing/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/fishing/`, `<workspace>/memory/fishing/`, `~/fishing/`.
3. If none exists and state must be created, default to `<workspace>/fishing/`.

Use the selected `<state_root>` for every state operation in this skill.

## When to Use

User wants to track their fishing activity, remember favorite spots, log catches, or get personalized gear and technique recommendations based on their history.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for setup.

```
<state_root>/
├── memory.md          # HOT: preferences, gear, active spots
├── catches.md         # WARM: catch log with dates, species, conditions
├── spots.md           # WARM: saved locations with notes
└── archive/           # COLD: past seasons
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Memory setup | `assets/memory-template.md` | When setting up or resetting user fishing preferences and inventory. |
| Species guide | `references/species.md` | When user needs information on fish habitats, baits, or seasonal behavior. |
| Tackle reference | `references/tackle.md` | When advising on rods, lines, hooks, presentations, or seasonal patterns. |

## Core Rules

### 1. Check Memory First
Before any recommendation, read `<state_root>/memory.md` for:
- User's gear inventory
- Preferred species
- Skill level
- Local regulations they've noted

### 2. Log Catches Proactively
After user reports a catch, update `<state_root>/catches.md`:

| Date | Species | Weight | Spot | Conditions | Technique |
|------|---------|--------|------|------------|-----------|
| YYYY-MM-DD | Bass | 3.5 lb | Lake X | Cloudy, 65F | Texas rig |

### 3. Learn Spot Patterns
Track what works at each location in `<state_root>/spots.md`:
- Best times (dawn, dusk, tide)
- Productive techniques
- Seasonal notes

### 4. Personalize Recommendations
Use catch history to suggest:
- "Last 3 bass at Lake X were on cloudy mornings with plastics"
- "You haven't tried spot Y since spring—spawning season now"

### 5. Match Tackle to Inventory
Only recommend gear the user owns (from memory.md). If suggesting new gear, mark it clearly as a purchase suggestion.

## Required protections

- **Verify inventory:** Always check the user's gear in `<state_root>/memory.md` before recommending tackle. If they lack it, suggest a purchase clearly.
- **Contextualize advice:** Reference past catches when providing recommendations to ensure relevance.
- **Seasonal awareness:** Review `<state_root>/catches.md` by month to identify seasonal patterns.
- **Maintain records:** Update `<state_root>/spots.md` proactively after discussions to ensure future recommendations remain fresh.

## Failure modes

| Failure | What to do |
|---------|------------|
| Missing `<state_root>` files | Create from `assets/memory-template.md`; do not invent past catches. |
| Empty gear inventory | Give general technique advice; mark any new-gear idea as a purchase suggestion. |
| Regulation questions | Do not guess limits; point to the current local wildlife agency source and ask which water/jurisdiction. |
| Conflicting spot notes | Prefer newest dated catch/spot entries; ask before overwriting older notes. |
| Unsafe handling advice | Prefer wet hands, minimal air time, and supported landing; never recommend illegal methods. |

## Anti-patterns

- Do not hardcode `~/Clawic/...` or any single-user absolute path.
- Do not recommend tackle the user does not own without labeling it as a purchase.
- Do not claim legal bag limits, seasons, or license status without a current local source.
- Do not skip reading `<state_root>/memory.md` before personalized gear advice.
