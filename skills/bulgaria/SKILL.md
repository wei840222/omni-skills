---
name: bulgaria
description: "Plan travel to Bulgaria. Use when exploring Sofia, Plovdiv, Black Sea coast or mountain destinations, navigating public transit, calculating travel budgets, or understanding local customs."
metadata:
  openclaw: '{"emoji": "🇧🇬", "requires": {"bins": [], "config": ["<state_root>/data/bulgaria/"]}, "os": ["linux", "darwin", "win32"], "displayName": "Bulgaria"}'
---

## Setup

If `<state_root>/data/bulgaria/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to load

Load this skill when the user is planning a trip to Bulgaria or needs local context on cities, beaches, mountain routes, food, transport, winter resorts, or practical travel logistics. Use progressive disclosure to load specific `references/` guides as needed.

## State location

Bulgaria state may exist in `<workspace>/bulgaria/`, `<workspace>/memory/bulgaria/`, or `~/bulgaria/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bulgaria/`, `<workspace>/memory/bulgaria/`, `~/bulgaria/`.
3. If none exists and state must be created, default to `<workspace>/bulgaria/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/data/bulgaria/`. If `<state_root>/data/bulgaria/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```
<state_root>/data/bulgaria/
└── memory.md     # Trip context and learned preferences
```

## Quick Reference

| Topic | File |
|-------|------|
| Sofia, Plovdiv, Varna, Bansko | `references/sofia.md`, `references/plovdiv.md`, `references/varna.md`, `references/bansko.md` |
| Itineraries & trip planning | `references/itineraries.md`, `references/accommodation.md` |
| Food, wine & culture | `references/food-guide.md`, `references/wine.md`, `references/culture.md` |
| Transport & telecom | `references/transport.md`, `references/telecoms.md`, `references/apps.md` |
| Official government & consular sources | `references/sources.md` |
