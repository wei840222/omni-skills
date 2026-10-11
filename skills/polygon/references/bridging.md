# Bridging with Polygon Portal

## Official bridge

- **UI:** [Polygon Portal](https://portal.polygon.technology) — official trustless two-way bridge between Ethereum and Polygon Chain.
- **Docs overview:** lock-on-L1 / mint-on-L2 for deposits; burn-on-L2 / unlock-on-L1 for withdrawals (pegged 1:1 circulating supply across the bridge path).
- The historical hostname `bridge.polygon.technology` is **not** a reliable entry point; send users to Portal.

## Deposit (Ethereum → Polygon Chain)

1. Connect a wallet that holds the asset on **Ethereum**.
2. In Portal, select the token and destination Polygon Chain.
3. Confirm the lock transaction on Ethereum; wait for inclusion.
4. Receive the pegged token on Polygon Chain after state sync / mint completes (often on the order of tens of minutes; do not invent exact SLAs).
5. Ensure the destination wallet already holds **POL** for later PoS gas, or bridge a small POL/MATIC amount first when the destination is empty.

## Withdraw (Polygon Chain → Ethereum)

1. Initiate burn/withdraw on Polygon Chain via Portal (or mapped token flow).
2. Wait for a **checkpoint** to land on Ethereum. Docs describe checkpoints submitted on the order of ~30 minutes; actual wait varies—verify with Portal / explorer status rather than a fixed clock.
3. Complete the **exit / claim** step on Ethereum (second transaction, pays Ethereum gas in ETH).
4. Historic PoS exits could stretch much longer under load or if the user never claims; "pending forever" is often an unclaimed exit, not a lost burn.

## Third-party bridges

Hop, Across, Stargate, and similar routes can be faster but add smart-contract and liquidity risk. Prefer Portal when the user wants the official trust model. Never present a random bridge URL from chat as "official."

## Safety rules

- Verify token contract addresses on both chains (scam tokens reuse tickers).
- Confirm network + token before signing; wrong-network sends are usually irreversible.
- After deposit, if the UI shows tokens but the wallet does not, add the token contract or refresh the Polygon network view—do not re-bridge as the first fix.
- Custom token mappings may require a mapping request; widely used tokens are already listed in Portal.
