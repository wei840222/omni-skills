# Sync — Webhooks and Polling

Keep an external system aligned with Notion without full re-scans every time.

**Contents:** [Prefer webhooks when available](#prefer-webhooks-when-available) · [Polling](#polling) · [Conflict rules](#conflict-rules) · [Version note](#version-note)

## Prefer webhooks when available

Subscribe to workspace events for page/database/data-source changes. Verify signatures on the receiver (`webhook` skill for generic receiver craft). Persist delivery cursors / processed event ids under `<state_root>/` so retries stay idempotent.

## Polling

When webhooks are unavailable:

1. Query the data source sorted by `last_edited_time`.
2. Store the high-water mark.
3. Pace under `rate_limit_rps`; paginate fully.

Search is index-lagged — do not use Search as a sync cursor.

## Conflict rules

- Decide authority per field (Notion-wins / external-wins / latest-timestamp).
- Writes remain per-object; never assume multi-page transactions.
- On ambiguous 503 after write, retrieve before repeating (see `references/bulk.md`).

## Version note

Webhook payload parent shapes change across API versions (including `2025-09-03` data sources). Pin subscription/API versions together and record them in `<state_root>/memory.md`.

Official sources: Webhooks API reference; Upgrade guide webhook section.
