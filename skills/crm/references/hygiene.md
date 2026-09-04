# Data Hygiene

Order of operations for a dirty CRM: **identity key → merge → decay**. Enrichment and automation come after.

## Identity key

1. Primary key: lowercased email.
2. Fallback when email is missing: `name + company domain`, flagged for human confirm.
3. Preserve provider-significant local-parts:
   - Strip dots only for known Gmail domains (`gmail.com`, `googlemail.com`).
   - Strip `+tags` only when the base address already exists.
4. Never invent a second person row for a near-duplicate spelling; merge or ask.

## Merge order

When two rows collide on the identity key:

1. Keep the **richest** record as the survivor (most filled durable fields), not the newest.
2. For provenance fields (`created`, original source), oldest wins.
3. For commercial state (stage, value, next step), keep the more advanced live deal and log the discarded one.
4. Rewrite every foreign key that pointed at the loser before deleting it.
5. Append one interaction line: what merged, which id survived, which fields moved.

## Decay sweep

On the review day (default Monday):

| Signal | Action |
|---|---|
| Bounce / invalid email | Mark suppressed for outreach; keep the row until a human confirms delete |
| No interaction beyond `stale_days` (default 90) and no open deal | Move to tier C or archive outside the active pipeline |
| Field fill rate &lt; ~70% after 30 days | Delete the field or make it required |
| Duplicate orgs on the same domain | Merge on domain; keep the richer firmographics |

## Before automation

Run bounce sweep and merge pass before any enrichment, mail sync, or sequenced follow-up. Automating stale or duplicated data advertises the rot to the recipient.
