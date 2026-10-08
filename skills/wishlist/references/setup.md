# Setup

Use this file only when `<state_root>` is missing required bootstrap files or the user is activating wishlist tracking for the first time.

## First-run steps

1. Explain that wishlist data stays local under the resolved `<state_root>`.
2. Confirm the user wants durable storage before creating directories or files.
3. Create only what is needed for the current request:
   - `settings.md` — check frequency, alert rules, preferred stores
   - `items/` — individual want files
   - `by-priority/` — must-have / want / someday indexes
   - `by-category/` — optional browsing indexes
   - `price-alerts.md` — active and triggered alerts
   - `purchased.md` — completed buys and simple hit-rate stats
4. Name every path created in the reply.

## Default settings template

```markdown
# settings.md

## Price Check Frequency
Weekly on Sundays (adjust with the user)

## Alert Preferences
Notify when:
- Price drops below target
- Price drops more than 15% from last checked price
- A configured store marks the item on sale

## Preferred Stores
- User-named retailers only; do not invent a store list

## Review Cadence
Monthly relevance review of must-have and want items
```

## Consent and migration

- Ask before creating `<state_root>` when none of the candidate paths exist.
- If `~/Clawic/data/wishlist/` exists, treat it as a migration source: propose copy → validate item counts → cut over → keep rollback copy. Delete the legacy tree only after explicit user approval.
- If duplicate candidate roots exist, keep operating on the highest-precedence root only and report the others.
