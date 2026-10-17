# Bulk — Imports, Exports, Backfills

Writes are per-object and never transactional. A job that dies halfway leaves half the pages.

**Contents:** [Rate math](#rate-math) · [Checkpointing](#checkpointing) · [Idempotency](#idempotency) · [Pilot then scale](#pilot-then-scale) · [Exports](#exports)

## Rate math

Official request limits (live-checked 2026-10-17):

- Per-connection average: **~3 req/s** on non-Business plans (**180/min**); **~10 req/s** on Business/Enterprise (**600/min**).
- Burst inside the 60s window is allowed; exceeding returns HTTP **429** with `Retry-After` (seconds) and `code: rate_limited`.
- A separate **per-workspace** budget is shared across connections; you can be limited even when one connection looks quiet.
- Honour `Retry-After`; add jitter; centralize pacing. Default skill config `rate_limit_rps: 3` remains the safe default until the workspace plan is known.

Time estimate ≈ `total_requests / rate_limit_rps` before retries. 5,000 page creates at 3/s ≈ 28 minutes.

## Checkpointing

Every bulk write must:

1. Persist a cursor / offset after each successful batch.
2. Append id mappings as it goes (`<state_root>/mappings/…`).
3. Resume from the checkpoint on rerun — never restart from zero blindly.

## Idempotency

Store an external id in a Notion property. Before create, filter on that property. Timeouts after a write may have succeeded; retrieve/filter before retrying creates. For 503 on writes, read Notion `additional_data.retry_guidance` — some 503s mean the write already committed.

## Pilot then scale

Run ~10 rows, verify in the UI (property shapes, relations, files), then run the rest with pacing + checkpoints.

## Exports

Paginate every list (`has_more` / `next_cursor`). Stream to disk; do not accumulate unbounded arrays. Prefer data-source queries over Search for known containers.

Official source: Request limits reference.
