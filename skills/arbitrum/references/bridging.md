# Bridging and withdrawals

## Official bridge

- Primary UI: [Arbitrum bridge](https://bridge.arbitrum.io) (see also [Bridge quickstart](https://docs.arbitrum.io/arbitrum-bridge/quickstart)).
- Use cases: move ETH or ERC-20 between a **parent chain** (usually Ethereum) and a **child chain** (Arbitrum One or Nova).
- Always bridge a small amount of **ETH** first when the destination wallet has none—tokens without gas cannot pay fees.

## Parent → child (deposit)

- After the parent-chain transaction confirms, funds become available on the child chain on the order of minutes (wait for parent confirmation, then child execution/retryable redemption as applicable).
- Deposits use inbox / retryable-ticket mechanics under the hood; failed retryables may need manual redeem via official tooling.
- Confirm the destination is the intended child (One vs Nova) before signing.

## Child → parent (native withdrawal)

1. Initiate the withdrawal on the child chain (burn/lock + outgoing message).
2. Wait for the **dispute / challenge window**. Official bridge UX describes a **seven-day** period for One and Nova; chain parameters document a dispute window of **45818 blocks (~6.4 days)** on those networks. Treat “about a week” as the user-facing expectation.
3. After the window, **claim** on the parent chain (bridge UI Transactions tab, or programmatic Outbox execute). The claim is a separate L1 transaction and needs L1 ETH for gas.
4. A dispute can delay **confirmation of L2→L1 messages**; ordinary L2 transactions continue. Native exits cannot be “sped up” inside the official bridge without changing security assumptions.

## Fast exits (third party)

- Liquidity bridges (e.g. Across, Hop, Stargate and similar) can return funds faster by taking inventory risk and fees.
- Extra trust surface: bridge contracts, solvers/LPs, and correct asset mapping.
- Prefer official bridge when value is large or the user can wait the dispute window.

## Status and recovery

- Track deposit/withdrawal hashes in the bridge transaction history; claim when the UI shows ready.
- “Pending for days” on a native exit during the window is expected behavior, not loss of funds.
- Wrong-network sends (same address on Ethereum vs Arbitrum) are a recovery problem—do not tell users the funds are permanently gone without checking both chains and any recover paths.
- For programmatic monitoring, see [Monitor withdrawals](https://docs.arbitrum.io/arbitrum-bridge/withdrawal-monitoring) and child-to-parent messaging docs.
