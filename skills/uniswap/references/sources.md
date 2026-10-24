# Research Sources — Uniswap Protocol Operations

Primary documentation and technical references for Uniswap V2/V3/V4 operations, swap routing, and MEV protection.

## Protocol Documentation

- **Uniswap V3 Core & Periphery** — https://docs.uniswap.org/contracts/v3/overview
  - Concentrated liquidity math, tick spacing, pool fee tiers (0.01%, 0.05%, 0.3%, 1.0%), and `SwapRouter` contract interfaces.
- **Uniswap QuoterV2** — https://docs.uniswap.org/contracts/v3/reference/periphery/lens/QuoterV2
  - Simulating swap outputs off-chain with exact gas estimation and slippage bound checks before sending transactions.
- **UniswapX Protocol** — https://docs.uniswap.org/contracts/uniswapx/overview
  - Dutch auction order routing, off-chain signed orders (`Permit2`), and gasless cancellation semantics.

## Security & MEV Protection

- **MEV Blocker** — https://mevblocker.io
  - Private RPC endpoints preventing frontrunning, sandwich attacks, and backrun rebates.
- **Flashbots Protect** — https://docs.flashbots.net/flashbots-protect/overview
  - Private mempool submission and bundle inclusion.
- **Revoke.cash** — https://revoke.cash
  - Managing and revoking ERC-20 allowances across EVM networks.
