---
name: chainlink
description: >
  Assist with Chainlink LINK tokens, Data Feeds, VRF v2.5, Automation, Functions,
  CCIP, Data Streams, and staking. Use when the user asks about oracle price feeds,
  stale-data checks, verifiable randomness, keepers/Automation, cross-chain CCIP
  messaging, Data Streams reports, LINK funding, or Chainlink staking. Prefer
  `ethereum` for generic EVM gas/approvals/bridges, `blockchain` for ledger
  fundamentals, `solidity` for contract-security pitfalls, `crypto-tools` for
  market data once oracle mechanics are settled, and `avalanche`/`polygon` for
  chain-native ops outside Chainlink products.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⬡"}'
  related-skills: '{"ethereum":"Generic EVM gas, approvals, nonce, and L2 bridge mechanics outside Chainlink product guidance.","blockchain":"Ledger fundamentals and viem contract interaction beyond oracle integration.","solidity":"Solidity security pitfalls (reentrancy, visibility) when writing consumer contracts.","crypto-tools":"Prices, explorers, and portfolio tooling after Chainlink product rules are clear.","avalanche":"Avalanche C/X/P-Chain operations when the ask is network-native rather than Chainlink feeds/CCIP.","polygon":"Polygon Chain PoS wallet/gas/Portal bridging outside Chainlink product flows."}'
---

# Chainlink

Stateless guidance for **Chainlink oracle products, LINK usage, and staking**.
Do not store keys, subscription IDs, or funded wallet exports in this package.

## When to load

- Read or integrate **Data Feeds** / SmartData / L2 sequencer uptime feeds
- Request **VRF v2.5** randomness (subscription or direct funding)
- Schedule **Automation** jobs or connect off-chain APIs via **Functions**
- Send tokens/messages with **CCIP**, or pull high-frequency **Data Streams**
- Fund subscriptions with LINK, verify feed addresses, or explain **staking v0.2**

## Hard defaults

1. **Verify addresses on official docs** — feed, VRF coordinator, Automation registry, and CCIP router addresses differ per network; never hardcode from memory.
2. **Treat feed answers as time-sensitive** — check `updatedAt` / round completeness; add circuit breakers for stale or extreme moves.
3. **Prefer official docs and `data.chain.link`** over third-party address lists.
4. **Re-open `references/sources.md`** before restating billing, staking caps, unbonding, lane availability, or feed deprecation claims.
5. **No trading advice** — explain oracle mechanics only; portfolio allocation belongs in `invest` / `trading` / `crypto-tools` as appropriate.

## Ordered workflow

1. **Classify** — LINK/token basics, Data Feeds, VRF, Automation/Functions, CCIP, Data Streams, staking, or security/stale-data incident.
2. **Load one matching reference** from the table below (plus `sources.md` when quoting mutable facts).
3. **Verify live** — docs.chain.link address pages, `data.chain.link`, explorer, or subscription UI — before irreversible funding, staking, or cross-chain sends.
4. **Near-miss routing** — pure EVM gas/approvals → `ethereum`; Solidity pitfalls → `solidity`; prices/TVL tooling → `crypto-tools`.

## Load the relevant reference

| Reference | Load when |
|---|---|
| `references/link-and-networks.md` | LINK ERC-20 basics, multi-chain addresses, bridging via CCIP, network trade-offs. |
| `references/data-feeds.md` | Price/SmartData/sequencer feeds, `latestRoundData`, stale checks, deprecation. |
| `references/vrf.md` | VRF v2.5 subscription vs direct funding, billing, callback failure modes. |
| `references/automation-functions.md` | Chainlink Automation triggers and Functions API connectivity. |
| `references/ccip.md` | Cross-chain token/message transfers, fees, finality, rate limits. |
| `references/data-streams.md` | Pull-based Streams reports, verification, latency-sensitive markets. |
| `references/staking.md` | Community/node-operator staking v0.2 caps, unbonding, slashing scope. |
| `references/sources.md` | Primary URLs for any mutable address, billing, staking, or deprecation claim. |

## Safety posture

- Prefer read-only diagnosis first. For subscription funding, staking, CCIP sends, or consumer deploys, state the exact action and wait for explicit user authorization.
- Never request seed phrases or private keys.
- Multi-oracle / circuit-breaker patterns for critical collateral paths; do not treat a single feed as infallible.