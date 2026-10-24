---
name: restaurants
description: Track restaurants to try, log dining experiences, and surface personalized recommendations from saved places. Use when the user mentions a restaurant, asks where to eat, or wants to record a meal.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "🍽️"}'
---

## Core Behavior
- User mentions restaurant → offer to save with notes
- User asks for recommendation → check their saved places first
- User returns from meal → help document experience
- Create `<state_root>/restaurants/` as workspace

## State location

Restaurants state may exist in `<workspace>/restaurants/`, `<workspace>/memory/restaurants/`, or `~/restaurants/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/restaurants/`, `<workspace>/memory/restaurants/`, `~/restaurants/`.
3. If none exists and state must be created, default to `<workspace>/restaurants/`.

Use the selected `<state_root>` for every state operation in this skill.

This skill stores state at `<state_root>/restaurants/`. Use this path for storing restaurant entries. Examples: `~/.local/state/restaurants/`, `C:\Users\User\AppData\Local\restaurants\`.

## File Structure
```
<state_root>/restaurants/
├── to-try/
├── favorites/
├── visited/
│   └── 2024/
├── by-cuisine/
└── by-occasion/
```

## To-Try Entry
```markdown
# sushi-nakazawa.md
## Location
West Village, NYC

## Cuisine
Omakase sushi

## Source
Friend recommendation

## Price Range
$$$$

## Notes
Need reservation weeks ahead
```

## Visited Entry
```markdown
# la-mercerie-2024-03.md
## Date
March 15, 2024

## Occasion
Anniversary dinner

## What We Ordered
- Burrata (excellent)
- Duck breast (slightly dry)
- Chocolate soufflé (must order)

## Verdict
★★★★☆ — Would return for brunch
```

## Favorites
```markdown
# joes-pizza.md
## Go-To Order
Plain slice, extra crispy

## Best For
Quick lunch, late night

## Notes
Cash only, expect line
```

## By-Cuisine and By-Occasion
Simple lists linking to favorites:
```markdown
# date-night.md
- La Mercerie — beautiful space
- Via Carota — classic Village
- Carbone — always reliable
```

## What To Track
- Location and neighborhood
- Cuisine type
- Price range: $ to $$$$
- Reservation: needed? how far ahead?
- Standout dishes
- Rating after visit

## Surfacing Recommendations
When user asks "where should we eat":
- Ask occasion and cuisine preference
- Check THEIR saved places first
- Suggest from their data before general knowledge

## What To Surface
- "You haven't tried that sushi place on your list"
- "Last Italian you loved was L'Artusi"
- "For date night you rated La Mercerie highest"

## Progressive Enhancement
- Start: add 5 places to try
- After meals: quick entry with verdict
- Build cuisine and occasion lists over time

## Important Constraints
- Prioritize user's saved places before suggesting new external options
- Always account for the user's documented dietary restrictions
- Maintain a lightweight structure; simple notes are preferred over heavy categorization
