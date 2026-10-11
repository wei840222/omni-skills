# Setup — United States Travel Guide

## First-Time Setup

When user mentions U.S. travel for the first time:

### 1. Create Memory Structure
```bash
mkdir -p <state_root>
```

### 2. Initialize Memory File
Create `<state_root>/memory.md` using `assets/data-templates.md`.

### 3. Gather Trip Context Naturally
Ask in conversational flow:
- Entry pathway: ESTA/visa status already solved or still pending?
- Travel window and flexibility: exact dates or month range?
- Scope preference: one region deep or multi-region highlights?
- Priorities: cities, parks, beaches, food, road trip, family, nightlife, shopping.
- Constraints: budget, mobility, dietary, driving comfort, weather tolerance.
- Pace: relaxed, moderate, or fast-moving itinerary.

### 4. Save to Memory
Update `<state_root>/memory.md` with the current intent, constraints, and decision status.

## Returning Users

If `<state_root>/memory.md` exists:
1. Read it silently
2. Reuse known constraints and preferences
3. Ask only what changed (dates, region focus, budget, mobility)
4. Update memory with deltas

## Quick Start Responses

**"I want to visit New York"**
→ Ask: nights, first-time vs repeat, budget band, core interests.
→ Then use: `references/new-york-city.md`, `references/accommodation.md`, `references/transport-domestic.md`.

**"I want national parks"**
→ Ask: month, hiking level, car comfort, crowd tolerance.
→ Then use: `references/national-parks.md`, `references/southwest-and-rockies.md`, `references/weather-and-seasonality.md`.

**"I need a full U.S. itinerary"**
→ Ask: total days and whether user accepts flights between regions.
→ Then use: `references/regions.md`, `references/itineraries.md`, `references/budget-and-costs.md`.

## Important Notes

- Entry/admin risk can block otherwise perfect itineraries.
- U.S. travel quality depends heavily on regional focus and season fit.
- Big cost deltas often come from transport and hidden fees, rather than hotel headline prices.
- Always include a weather-aware fallback plan.
