# Meal planning domain knowledge

Load when drafting weekly plans, shopping lists, leftovers strategy, batch-cook prep, ratings, or meal-database entries.

## Meal database

Build a personal collection over time:

- Meals you actually make (realistic everyday meals, not aspirational)
- Prep time and cook time
- Servings
- Dietary tags: vegetarian, gluten-free, dairy-free, and user-specific
- Difficulty: quick weeknight vs weekend project
- Optional rating: make-again yes / no / maybe

Suggested file: `<state_root>/meals/{slug}.md`.

## Weekly plan format

Simple list is enough:

- Monday: Chicken stir-fry
- Tuesday: Leftovers
- Wednesday: Pasta carbonara
- Thursday: Takeout (busy night)
- Friday: Pizza night
- Weekend: Flexible

Store under `<state_root>/plans/` with an ISO week name when practical (example `2026-W41.md`).

## Shopping list generation

- Aggregate ingredients from planned meals only (plus explicit extras the user adds)
- Combine quantities (`2 onions + 1 onion = 3 onions`)
- Group by store section: produce, dairy, meat/seafood, pantry, frozen, other
- Exclude pantry staples listed in preferences unless the user says they are out
- Write the list under `<state_root>/shopping/` tied to the plan id

## Pantry staples

Track what the household usually has (salt, oil, garlic, rice, pasta, common spices). Subtract automatically from shopping lists. When the user reports running out, update preferences the same turn.

## Meal preferences

- Restrictions: allergies, intolerances, ethical choices
- Dislikes and hard vetoes
- Favorites and go-to weeknight meals
- Cuisine cadence (optional themes)

Never invent an allergy. If unknown, ask once.

## Progressive enhancement

- Week 1: plan a few dinners; make one shopping list
- Week 2: save meals that worked to the database
- Month 2: reuse past meals to speed planning
- Month 3: surface patterns (repeats, gaps, ratings)

## Quick weeknight filters

Tag meals by time/effort:

- Under 30 minutes
- One-pot / sheet pan
- No-cook
- Make-ahead
- Freezer-friendly

## Batch cooking support

- Sunday prep suggestions when the user wants them
- Meals that share ingredients across the week
- Components that work multiple ways
- Proteins: cook once, use twice (with leftovers rules below)

## What to surface

- "Last week you made tacos Tuesday — repeat or vary?"
- "Chicken appears twice — intentional?"
- "Salmon has not appeared in three weeks"
- "That pasta was rated make-again last time"

## Leftovers planning

- Big batch → planned leftover lunch or dinner
- Transform leftovers deliberately (roast chicken → chicken salad)
- Note which meals keep well
- Freeze portions only when the user wants future lazy nights

Keep guidance high-level; defer precise temperature/time limits to official FSIS/CDC pages listed in `sources.md` when the user asks for safety detail.

## Meal ratings

After cooking (when the user reports back):

- Make again? yes / no / maybe
- What to adjust next time
- Household feedback
- Feed future suggestions from this data

## Dietary tracking (optional, non-clinical)

- Focus on composition and balance across the week (vegetables, protein variety, cuisine variety)
- Special emphases the user names (iron-rich, higher-protein days) — do not invent medical targets
- Calorie counting belongs in `calories`, not here

## Priorities when stuck

- Simple planning before complex meal prep
- Quick low-effort options on busy nights
- Repeating favorites is success, not failure
- One clarifying question at a time

## Integration points

- `cooking`: technique once the meal is chosen
- `shopping`: non-meal errands or store workflow beyond ingredient aggregation
- `daily-planner` / calendar notes: guests and cook-night timing
- Recipe files the user already keeps: link paths; do not scrape paywalled content

## Seasonal awareness

- Warm weather: grilling, salads, no-cook
- Cold weather: soups, stews, comfort food
- Seasonal produce: prefer what the user says is good/local now
- Holidays: plan around known events without overfilling weeknights

## Plate-balance pattern (non-prescriptive)

When the user wants "healthy" without a clinical diet, prefer a plate pattern roughly half vegetables/fruit, one-quarter whole grains or starch, one-quarter protein, plus water as the default drink. Cite `references/sources.md` rather than inventing micronutrient RDAs.
