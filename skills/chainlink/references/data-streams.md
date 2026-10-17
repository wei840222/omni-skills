# Data Streams

Data Streams deliver **low-latency, pull-based market data** (crypto, RWA/equities, FX, commodities, SmartData, tokenized assets). Clients fetch or subscribe to signed reports (REST/WebSocket/SDKs), then **verify onchain** in the same transaction that consumes them.

## When Streams vs Data Feeds

| Need | Prefer |
|---|---|
| Simple onchain `latestRoundData` consumer | Data Feeds |
| Sub-second / perpetuals / options-style latency | Data Streams |
| DON-published proxy already integrated by a protocol | Usually Feeds unless Streams is required |

## Consumer checklist

1. Obtain access / auth as required by Streams docs (Discovery endpoint can list stream IDs without a key).
2. Decode the correct **report schema** version for the stream family.
3. Verify the report onchain before acting on prices.
4. Handle market-hours / corporate-action fields for equity and tokenized-asset schemas.
5. Watch **deprecation** schedules for individual streams.

## Common mistakes

- Treating unverified offchain payloads as authoritative
- Mixing schema versions
- Ignoring market-status flags on RWA streams

Point mutable stream IDs and shutdown dates to official docs via `sources.md`.