# Food Input Processing

Load when classifying a new food input or choosing a pipeline.

## Auto-Classification

| Input | Type | Action |
|-------|------|--------|
| Photo + "ate/had/just" | meal | log + offer analysis |
| Photo with barcode/label | product | extract nutrition, store |
| Photo of raw ingredients | inventory | list items |
| Photo of menu | restaurant | extract options, suggest |
| Photo with recipe/steps | recipe | extract and save |
| "I ate X" | meal | log, infer context |
| "allergic/exclude/avoid X" | preference | store permanently |
| "find restaurant" | restaurant | suggest from Places + context |
| "what can I cook" | recipe | suggest from inventory + Recipes |
| "plan my week" | plan | hand off structure to `meal-planner` after reading preferences |

## Meal Photo Pipeline

1. Identify food items and portions against plate/utensil cues when visible.
2. Detect context: home / restaurant / takeout (plate style, packaging, setting).
3. Tag: `#meal` `#[context]` `#[meal_type]`.
4. Prompt once: "Want a nutrition estimate?"
5. If yes and macros are the goal, hand off details to `calories`; otherwise store a light estimate range.
6. Store with timestamp under Patterns-relevant notes only when the user wants continuity.

## Label Photo Pipeline

1. OCR: brand, product name, serving size, calories/macros when present, ingredients.
2. Normalize units (g, ml, per serving vs per package).
3. Tag: `#product` `#[brand]`.
4. Store under Products for quick-log reuse (`had [product]`).
5. Confirm serving size before treating label calories as a single meal total.

## Recipe Photo/Text Pipeline

1. Extract title, ingredients, and steps.
2. Parse ingredient quantities when present; mark missing amounts explicitly.
3. Tag: `#recipe` `#[cuisine]`.
4. Link to inventory items when the user tracks stock.
5. Approximate nutrition per serving only when ingredients and yields are complete enough; otherwise state the gap.

## Text Input Pipeline

1. Classify intent: log / query / plan / edit preference.
2. Route to the matching handler above.
3. Confirm the action taken in one short line.

## Tagging System

- `#meal` — something eaten
- `#product` — packaged food with nutrition
- `#recipe` — how to make something
- `#restaurant` — place to eat
- `#inventory` — what is in stock
- `#preference` — likes, dislikes, restrictions

## Context Inference

Use as soft defaults, then confirm when ambiguous:

- 06:00–10:00 → breakfast
- 12:00–14:00 → lunch
- 19:00–22:00 → dinner
- wording "ordered/takeout/delivery" → restaurant/takeout
- wording "cooked/made/homemade" → home

## Weekly Insights (computed from stored entries)

- Variety score: unique foods / total entries
- Frequent foods: top 5 in the window
- Meal timing: average times per meal type
- Eating-out ratio: restaurant-tagged / total meals
- Nutrition trends: only when the user enabled estimates or `calories` linkage

If the memory file is empty, say so and offer to start logging instead of inventing patterns.
