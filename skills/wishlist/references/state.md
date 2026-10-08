# State Management

All paths below are relative to the resolved `<state_root>`.

## Tree

```text
<state_root>/
├── items/
│   └── sony-headphones.md
├── by-priority/
│   ├── must-have.md
│   ├── want.md
│   └── someday.md
├── by-category/
│   ├── tech.md
│   ├── home.md
│   └── clothing.md
├── purchased.md
├── price-alerts.md
└── settings.md
```

Create a subdirectory only when the first file inside it is needed.

## Item file (`items/{slug}.md`)

Slug: lowercase hyphenated product nickname derived from the user wording (example: `sony-headphones`).

```markdown
# sony-headphones.md
## Item
Sony WH-1000XM5 Headphones

## Why I Want It
Best noise cancelling for cafe work

## Priority
Must-have

## Category
Tech

## Price Tracking
- Target price: 300 USD
- Current best: 349 USD (Amazon) — observed, not guessed
- Currency: USD
- Last checked: 2026-10-01

## Links
- Amazon: https://example.invalid/sony
- Best Buy: https://example.invalid/bb

## Price History
- 2026-09-01: 379 USD
- 2026-10-01: 349 USD

## Notes
Prefer sale windows; consider refurbished with warranty

## Added
2026-01-15

## Status
open
```

Rules:

- Record currency with every price.
- Mark unknown fields as `unknown` rather than inventing values.
- Keep payment credentials out of notes.
- When status becomes `purchased`, leave a stub or archive note in the item file and append the buy to `purchased.md`.

## Priority indexes

Maintain short bullet indexes; the item file remains the source of truth.

```markdown
# by-priority/must-have.md
- Sony WH-1000XM5 — waiting for < 300 USD
- Standing desk — researching options

# by-priority/want.md
- Kindle Paperwhite
- AirTag 4-pack

# by-priority/someday.md
- Espresso machine
- Drone
```

Priority meanings:

| Level | Meaning |
|-------|---------|
| Must-have | Actively planning to buy when price/need align |
| Want | Would buy on a clear good deal |
| Someday | Nice to have; no active timeline |

## Category indexes

Optional browsing lists (`tech`, `home`, `clothing`, `hobby`, `gifts-for-self`, user-defined). Keep one line per item pointing back to the item slug.

## Price alerts (`price-alerts.md`)

```markdown
## Active Alerts
- Sony WH-1000XM5: alert if < 300 USD
- Kindle Paperwhite: alert if < 100 USD

## Triggered
- 2026-10-01: Sony at 349 USD (still above target)
```

Update `Last checked` on the item file whenever an alert evaluation runs.

## Purchased log (`purchased.md`)

```markdown
## 2026
- Sony WH-1000XM5: 299 USD (2026-02-20) — hit target
- Standing desk: 450 USD (2026-01-15) — slightly over target

## Stats
- Items bought at/under target: count when data exists
- Average wait time: compute from Added → purchase date when both exist
- Total saved vs first observed price: only with recorded history
```

Recompute stats from logged rows; do not hard-code marketing percentages.

## Path safety

- Write only under the resolved `<state_root>`.
- Write only the resolved filesystem path; the placeholder name `<state_root>` stays documentation-only.
- Shared host memory such as workspace `MEMORY.md` is outside this tree; mention wishlist facts there only when the user asks for a cross-skill summary.
