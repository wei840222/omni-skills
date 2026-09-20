---
name: bulgaria
description: Plan travel to Bulgaria by offering local context on cities, coastal
  and mountain regions, food, and navigating practical travel logistics.
metadata:
  related-skills:
  - travel
  - food
  - bulgarian
  openclaw: '{"emoji": "🇧🇬", "requires": {"bins": [], "config": ["<state_root>/data/bulgaria/"]},
    "os": ["linux", "darwin", "win32"], "displayName": "Bulgaria"}'
---

## Setup

If `<state_root>/data/bulgaria/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to load

Load this skill when the user is planning a trip to Bulgaria or needs local context on cities, beaches, mountain routes, food, transport, winter resorts, or practical travel logistics. Use progressive disclosure to load specific `references/` guides as needed.

## Architecture

Memory lives in `<state_root>/data/bulgaria/`. If `<state_root>/data/bulgaria/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```
<state_root>/data/bulgaria/
└── memory.md     # Trip context and learned preferences
```

## Quick Reference

| Topic | File |
|