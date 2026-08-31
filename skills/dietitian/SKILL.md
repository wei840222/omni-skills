---
name: dietitian
description: Plan meals, calculate calorie targets and macros, schedule meal timing, and advise on goal-specific diet protocols. Use this when the user needs structured diet advice, meal plans, or macro calculations.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🥗"}'
  related-skills: '{"fitness":"Can create complementary workouts and manage overall health."}'
---

## State location

This skill is stateless and does not store local configuration or persistent user state.

## Core Operations

To provide diet advice, read the following references when needed:

| Topic | When to load | File |
|---|---|---|
| **Calculating Calories and Macros** | When setting calorie targets, BMR, deficits/surpluses, or macronutrient splits | `references/calculating-macros.md` |
| **Meal Structure and Planning** | When creating meal plans, timing protocols, food swaps, or meal prep advice | `references/meal-structure.md` |
| **Diet Protocols** | When discussing specific diets like Keto, Low-carb, Mediterranean, or IIFYM | `references/diet-protocols.md` |
| **Tracking and Adjusting** | When answering questions about tracking methods, food scales, or making adjustments over time | `references/tracking-adjustments.md` |
| **Evidence Sources** | When verifying calorie/macro guidance against authoritative references | `references/sources.md` |
