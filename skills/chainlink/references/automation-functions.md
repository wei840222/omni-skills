# Automation and Functions

## Chainlink Automation

Use Automation when contracts need reliable, decentralized triggers (time-based, custom logic, log triggers, etc.) without running your own keeper fleet.

Guidance:

1. Define the exact trigger condition and the onchain function that should run.
2. Register/upkeep through official Automation docs for the target network.
3. Fund the upkeep; monitor perform gas and failure logs.
4. Keep perform logic bounded — unbounded loops risk gas failures.

## Chainlink Functions

Functions let smart contracts request **custom offchain computation** against APIs, with DON execution and onchain fulfillment.

Guidance:

1. Write the minimal source request; avoid shipping secrets in plaintext source.
2. Use supported secrets mechanisms from official Functions docs.
3. Fund the subscription; handle callback failures and response size limits.
4. Treat external API data as untrusted until validated in the consumer contract.

## Routing

- Pure price reads without custom offchain logic → `data-feeds.md` or `data-streams.md`
- Cross-chain send → `ccip.md`
- Randomness → `vrf.md`