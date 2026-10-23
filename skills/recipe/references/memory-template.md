# Memory template — recipe

Use only after a session produces something durable. All paths are under the selected `<state_root>`.

## Files

### `<state_root>/recipe/config.yaml`
User preferences from the Configuration table. Create on first stated preference; update in place.

### `<state_root>/recipe/memory.md`
Observed kitchen/collection facts. Suggested headings:

```markdown
## Boxes
- recipes/<kebab>.md — when a new recipe file is created
- made/YYYY.md — when a cook is logged

## Kitchen
- oven_offset_c: …
- salt_in_jar: diamond-kosher
- pan_sizes: …

## Sources
- YYYY-MM-DD | url-or-book | note

## Due
- | item | next_date | note |
```

### `<state_root>/recipe/index.md`
Canonical collection index. One row per recipe; retired recipes move under `## Retired` with a reason.

### `<state_root>/recipe/recipes/<kebab-title>.md`
One recipe, one file. See `format.md`.

### `<state_root>/recipe/made/<year>.md`
Make log rows: date, recipe, rating, change tried, outcome.

### Shared boxes
- `<state_root>/health/profile.md` — allergies / intolerances / diet-relevant conditions
- `<state_root>/contacts/contacts.md` — people you cook for; dietary note in `Context`
- `<state_root>/projects/<project>.md` — cookbook / supper-club / catering status line
- `<state_root>/profile.yaml` — shared universals (units/locale/currency)

## Write rules
1. Read health profile before proposing or adapting recipes.
2. Update only rows this skill owns in shared boxes; preserve foreign rows.
3. No credentials under `<state_root>/` — store pointers (`keychain:…`, `env:…`, `1password:…`, `file:…`).
4. Index and recipe file are written in the same turn as capture.
