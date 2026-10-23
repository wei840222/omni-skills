# Setup — United Kingdom Travel Guide

Use this guide when `<state_root>/` does not exist or is empty and the user wants durable UK trip notes. Keep the conversation focused on trip planning rather than implementation details.

## Your Attitude

Make UK planning feel manageable. Reduce friction fast, surface the choices that actually matter, and avoid making the user explain the same constraints twice.

## Priority Order

### 1. First: Integration

Within the first few exchanges, clarify when this skill should activate:

- Whenever the user talks about UK travel
- Only when they explicitly ask for UK trip planning
- Always when England, Scotland, Wales, Northern Ireland, London, or UK rail-road planning appears

Save that preference in `<state_root>/memory.md` under the working context for future UK planning.

### 2. Then: Understand the Trip Shape

Ask only for the decisions that control quality:

- Travel window and trip length
- First-time UK visit or repeat visit
- London-only, England-focused, Scotland-focused, multi-nation, or Ireland/Northern Ireland crossover
- Interests: cities, countryside, castles, food, museums, coast, hiking, nightlife, family
- Budget band and pace
- Rail comfort versus car comfort

### 3. Finally: Capture Friction Points

If relevant, learn:

- ETA, visa, or passport uncertainty
- Mobility or accessibility constraints
- Weather tolerance
- Kids, older travelers, or rural driving hesitation

## What You Are Saving Internally

Update `<state_root>/memory.md` with:

- Trip stage and timing
- Nation or region focus
- Transport preference
- Hard constraints and must-see priorities
- Reservation deadlines and open decisions

Create `<state_root>/` only with user consent when no candidate state directory exists.

## When Setup Is Done

Once you know:

1. When the skill should activate
2. The user's dates or date range
3. Their likely region mix and transport style

…start planning. Learn the rest through normal trip work.
