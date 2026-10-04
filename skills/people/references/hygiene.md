# Hygiene

## Merge order

1. Match on `Key` (email/handle/stable disambiguator), never name alone.
2. Prefer the record with richer dated interactions.
3. Preserve suppression entries over convenience merges.
4. Keep a one-line merge note with date.

## Imports

Phone / vCard / LinkedIn exports arrive as **candidates**, not live roster.
Promote on first real interaction. Never bulk-promote hundreds of rows.

## Decay

- Bounce / dead address: mark channel invalid; keep person unless user deletes
- Drift without conflict: move to `dormant` instead of delete
- Quarterly (or `roster_review`) pass: bounces, untiered bloat, duplicate keys
