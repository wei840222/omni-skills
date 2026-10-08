# Domain Defaults — Food Classification

Load for allergen conflict checks, label reading defaults, and non-medical boundaries.

## Restriction priority

1. Treat stated allergies and medical exclusions as hard stops for suggestions.
2. Store them under Preferences with type (`allergy`, `intolerance`, `choice`).
3. When a logged meal or recipe likely conflicts (e.g. pad thai + peanut allergy), flag the risk, ask for confirmation, and do not normalize the conflict away.
4. "May contain" / cross-contact uncertainty stays uncertain—ask rather than clear the dish.

## Major allergen awareness (US labeling baseline)

US packaged-food labeling highlights major allergens (including milk, eggs, fish, shellfish, tree nuts, peanuts, wheat, soybeans, and sesame). Use official labeling pages when advising on packaged products; restaurant and homemade food lack the same guarantee.

Sources (full URLs belong in the PR Research Sources section):

- FDA — Food Allergies: What You Need to Know
- FDA — Food Allergies overview under nutrition/critical foods
- FDA — How to Understand and Use the Nutrition Facts Label

## Nutrition estimate hygiene

- Estimates are ranges, not single false-precision numbers.
- Label values are per stated serving; confirm servings eaten before totaling.
- Restaurant and homemade dishes vary widely; prefer ranges and assumptions stated aloud.
- This skill classifies and organizes; deep macro coaching belongs to `calories`.
- Never present outputs as medical diagnosis, allergy testing, or prescribed therapy.

## Failure recovery

| Situation | Recovery |
|-----------|----------|
| Photo unreadable | Ask for a clearer photo or a short text list of items |
| Label serving ambiguous | Ask servings eaten before storing product calories |
| Conflicting state roots | Keep highest-precedence root only; report the conflict |
| Empty memory on insight request | Say no history yet; offer to log the first meal |
| User wants clinical plan | Hand off to `dietitian` without inventing protocols |
