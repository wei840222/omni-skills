# Memory template — cooking

Use only after a session produces something durable. All paths are under the selected `<state_root>`.

## Files

### `<state_root>/cooking/config.yaml`
User preferences from the Configuration table (`units`, `salt_type`, `heat_source`, `diet`, …). Create on first stated preference; update in place.

### `<state_root>/cooking/memory.md`
Observed kitchen facts and repertoire. Suggested headings:

```markdown
## Boxes
- artifacts/dinner-YYYY-MM-DD.md — when a full run-sheet is worth keeping

## Kitchen
- oven_offset_c: …
- salt_in_jar: diamond-kosher

## Repertoire
- YYYY-MM-DD | dish | change tried | outcome

## Due
- | item | next_date | note |
```

### `<state_root>/cooking/artifacts/`
Optional recipes-as-cooked, brine formulas, dinner run-sheets. One file per artifact; link from `## Boxes`.

### Shared boxes
- `<state_root>/health/profile.md` — allergies / intolerances / diet-relevant conditions only (identity = condition name; include severity).
- `<state_root>/contacts/contacts.md` — people you cook for; food constraint in `Context`; identity = `Key`.
- `<state_root>/profile.yaml` — shared universals (units/locale) read after `config.yaml`.

## Write rules
1. Read health profile before naming ingredients.
2. Update only rows this skill owns in shared boxes; preserve foreign rows.
3. No credentials under `<state_root>/` — store pointers (`keychain:…`, `env:…`, `1password:…`, `file:…`).
4. Record the single variable changed (Core Rule 8) when logging repertoire experiments.
