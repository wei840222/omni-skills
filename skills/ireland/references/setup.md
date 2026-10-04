# Setup — Ireland Travel Guide

## First-time setup

When the user mentions Ireland travel for the first time and wants context kept:

### 1. Resolve and create state root

Follow the `<state_root>` resolver in `SKILL.md`. Prefer creating `<workspace>/ireland/` when workspace is available; otherwise ask before writing outside an existing allowed root.

```bash
mkdir -p <state_root>
```

### 2. Initialize memory file

Create `<state_root>/memory.md` using the template from `assets/memory-template.md` only after the user wants persistence.

### 3. Gather trip context

Ask naturally (not as a form):

- Which month are you going? (weather and daylight matter)
- How long is the trip?
- City-break, road-trip, or mixed plan?
- Mostly food/pubs, culture, or coastal nature?
- Comfortable driving on the left on narrow roads?
- Any dietary, mobility, or budget constraints?

### 4. Save to memory

Update `<state_root>/memory.md` with their answers when persistence is requested.

## Returning users

If `<state_root>/memory.md` exists:

1. Read it silently
2. Reuse known preferences
3. Ask what changed since last plan
4. Update memory with new priorities and constraints

## Quick start responses

**"I am going to Dublin"**
→ Ask: nights, neighborhood preference, budget
→ Then: use `dublin.md` + `accommodation.md`

**"I want a road trip"**
→ Ask: days, driving comfort, must-see coast sections
→ Then: use `wild-atlantic-way.md` + `transport.md` + `itineraries.md` + `operating-rules.md`

**"Planning Ireland trip"**
→ Ask: first-time vs repeat visit, city vs coast split
→ Then: use `regions.md` to narrow scope before a final itinerary

## Important notes

- Distances look moderate, but average speeds drop on scenic rural roads.
- Peak season in coastal areas needs early booking.
- Shoulder months are often better for value and crowd control.
- Weather can change quickly, so every outdoor day needs a backup.