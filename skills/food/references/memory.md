# Memory Storage Format

Load before creating or updating `<state_root>/memory.md`.

All user data for this skill persists in `<state_root>/memory.md` after opt-in. Use the following Markdown structure and keep section headings stable so later reads stay parseable.

```markdown
### Preferences
<!-- Food preferences and restrictions. Format: "item: type" -->
<!-- Examples: nuts: allergy, gluten: intolerance, vegetarian: choice -->

### Products
<!-- Scanned/saved products for quick-log. Format: "product: cal/serving" -->
<!-- Examples: Hacendado yogurt: 120/170g, Oatly oat milk: 45/100ml -->

### Patterns
<!-- Detected eating patterns. Format: "pattern" -->
<!-- Examples: breakfast ~8am, snacks after 10pm, eats out Fridays -->

### Places
<!-- Restaurants and spots. Format: "place: notes" -->
<!-- Examples: Noma: loved fermented plum, Local Thai: go-to takeout -->

### Recipes
<!-- Saved recipes. Format: "dish: key info" -->
<!-- Examples: quick hummus: chickpeas+tahini+lemon 5min, Sunday roast: 2h -->
```

## Write rules

1. Resolve `<state_root>` from `SKILL.md` before any write.
2. Create `<state_root>/memory.md` only after the user opts into continuity.
3. Prefer append/update of the matching section; do not delete other sections.
4. Empty sections mean "no data yet"—leave the heading in place.
5. Preference changes (allergy, exclusion, diet choice) update Preferences immediately and take priority over meal suggestions.
6. Do not store credentials, full medical records, or unrelated private data in this file.
