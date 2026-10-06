# Review Schema — Google Reviews

Normalize all inputs into this canonical shape before comparison or monitoring.

## Required fields

| Field | Type | Notes |
| --- | --- | --- |
| source | string | `gbp`, `places`, `shopping`, `merchant`, `manual` |
| brand | string | Stable brand key |
| entity_id | string | Location, place, product, or merchant ID |
| review_id | string | Source-native review ID when available; otherwise stable hash of source+entity+time+author |
| rating | number | 1–5 normalized when the source uses stars |
| review_time | string | ISO-8601 timestamp of the review or last edit |
| text | string | Raw review text when available |
| language | string | ISO language code when known |
| author_label | string | Public display label if provided |

## Derived fields

| Field | Type | Purpose |
| --- | --- | --- |
| sentiment | string | `positive`, `neutral`, `negative`, `mixed` |
| themes | array | Complaint/praise categories |
| urgency | string | `low`, `medium`, `high` based on policy |
| is_new | boolean | New since previous snapshot |
| is_edited | boolean | Text or rating changed since last snapshot |
| access_mode | string | `api`, `export`, `page-check` |

## Dedup key

Primary: (`source`, `entity_id`, `review_id`)

If `review_id` is missing, fall back to (`source`, `entity_id`, `review_time`, `author_label`, normalized `text` prefix).

## Snapshot guidance

- Append-only JSONL under `<state_root>/snapshots/{brand}/{source}.jsonl`
- One normalized object per line
- Preserve raw source payload references out-of-band when needed; do not store secrets
