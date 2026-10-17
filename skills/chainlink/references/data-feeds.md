# Data Feeds

## What they are

Decentralized oracle networks publish aggregated onchain answers (prices, reserves/NAV/SmartData, rates/volatility, L2 sequencer uptime, tokenized equity, and related feed types). Lending markets and other protocols read them for collateral valuation and settlement.

## Consumer checklist

1. Resolve the **proxy/feed address** for the exact network + pair from official docs or `data.chain.link` — never hardcode from memory.
2. Prefer `latestRoundData()` (or current AggregatorV3 / MVR APIs) over a bare latest answer so you get round id, startedAt, updatedAt, and answeredInRound.
3. **Stale-data gate**: reject answers when `updatedAt` is too old for your risk policy, when the round is incomplete, or when an L2 sequencer uptime feed shows downtime.
4. Add **circuit breakers** for extreme moves; critical systems should not rely on a single oracle path alone.
5. Watch **deprecation** notices — Chainlink announces feeds being retired; migrate before shutdown.

## Feed families (routing)

| Family | Typical use |
|---|---|
| Price Feeds | Collateral / derivatives mark prices |
| SmartData / PoR / NAV / MVR | RWA reserves, fund NAV, multi-variable bundles |
| Rate & Volatility | Rate curves, staking APR, realized vol benchmarks |
| L2 Sequencer Uptime | Pause sensitive actions while a sequencer is down |
| Tokenized Equity / extended-hours | Equity-linked onchain data with market-hours nuance |

## Common mistakes

- Hardcoding feed addresses across networks
- Ignoring heartbeat / deviation update semantics (feeds are not every-block ticks)
- Skipping sequencer-uptime checks on L2
- Treating off-docs address lists as authoritative

Re-open `sources.md` before quoting a specific address, heartbeat, or deprecation date.