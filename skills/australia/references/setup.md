# Setup — Australia Travel Guide

## First-time setup

When the user mentions Australia travel for the first time and wants context kept:

### 1. Resolve and create state root

Follow the `<state_root>` resolver in `SKILL.md`. Prefer creating `<workspace>/australia/` when workspace is available; otherwise ask before writing outside an existing allowed root.

```bash
mkdir -p <state_root>
```

### 2. Initialize memory file

Create `<state_root>/memory.md` using the template from `assets/memory-template.md` only after the user wants persistence.

### 3. Gather trip context

Ask naturally (not as a form):

- Which month are you going? (season strongly affects region quality)
- How long is the trip?
- City-and-coast mix, nature-first, or outback-first?
- How comfortable are you with long drives and domestic flights?
- Any mobility, dietary, heat/humidity, or budget constraints?
- Must-see items that would force multi-base routing?

### 4. Save to memory

Update `<state_root>/memory.md` with their answers when persistence is requested.

## Returning users

If `<state_root>/memory.md` exists:

1. Read it silently
2. Reuse known preferences
3. Ask what changed since last plan
4. Update memory with new priorities and constraints

## Quick start responses

**"I am going to Sydney"**
→ Ask: nights, neighborhood style, city vs beach balance
→ Then: use `sydney.md` + `accommodation.md` (handoff to `sydney` skill for deep resident/neighborhood work)

**"I want coast and reef"**
→ Ask: tropical north tolerance and weather window
→ Then: use `cairns-reef.md` + `beaches.md` + `seasonality.md` + `sources.md`

**"Planning Australia trip"**
→ Ask: one-region depth vs multi-region route, trip length, month
→ Then: use `regions.md` and `transport.md` before a final itinerary

## Important notes

- Australia route quality is mostly a distance and pacing decision.
- Fewer anchors usually outperform checklist-heavy plans.
- Seasonal timing matters more than many travelers assume.
- Remote, reef, and outdoor days need explicit safety buffers.
