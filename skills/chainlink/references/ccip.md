# CCIP (Cross-Chain Interoperability Protocol)

CCIP sends **tokens, arbitrary messages, or programmable token transfers** across supported blockchains with Chainlink security assumptions.

## Before any send

1. Confirm **lane support** (source ↔ destination) in the CCIP directory / docs — not all pairs exist.
2. Estimate **fees** (LINK or native fee token) and ensure balances cover execution.
3. Understand **finality / execution latency** for both chains; do not promise instant settlement.
4. For token transfers, confirm pool mechanism (burn/mint vs lock/mint), decimals, and **rate limits**.
5. Prefer official tutorials/SDKs/CLI; disclose third-party messenger risk if the user proposes an alternate bridge.

## Message lifecycle (operator mindset)

- Track message status via official explorer/API/SDK after send.
- Know manual-execution / defensive patterns when destination execution fails.
- CCT (cross-chain token) registration and pool config are issuer workflows — separate from app messaging.

## Common failures

- Unsupported lane or wrong router address
- Underpaid fees
- Rate-limit hits on token pools
- Assuming source finality equals destination execution

Re-check `sources.md` for directory, fee, and CCIP 2.0 announcements before stating current network coverage.