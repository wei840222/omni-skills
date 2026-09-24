# BNB Chain Network & Tokens

## Network Clarity (Critical)
- "BNB Chain" is the main smart contract chain (formerly Binance Smart Chain / BSC).
- "BNB Beacon Chain" was for staking — deprecated, merged into BNB Chain.
- BEP-20 tokens on BNB Chain are equivalent to ERC-20, EVM compatible.
- The address format is identical to Ethereum — 0x... addresses work on both.
- **CRITICAL**: Sending funds to the wrong network (e.g. sending ETH directly to BNB Chain without a bridge) results in lost funds.

## BNB Token & Gas
- Native gas token for BNB Chain — required for all transactions.
- EVM-compatible gas model, but gas prices are typically 3-5 gwei.
- Standard transfer costs ~21,000 gas.
- Fast block time (3 seconds).

## BEP-20 Tokens
- Same interface as ERC-20 — all ERC-20 tooling works.
- Uses the standard Approve + Transfer pattern.
- Verify contract addresses on bscscan.com to ensure authenticity.
- Popular tokens: USDT, USDC, CAKE, and various meme tokens (Note: BUSD is deprecated).

## Cross-Chain Transfers
- The easiest method to move funds is withdrawing directly from the Binance exchange to the BNB Chain.
- Bridges (e.g. cBridge, Multichain, Stargate) are required to move assets between BNB Chain and Ethereum.
- opBNB is an L2 on BNB Chain with lower fees and a different RPC.
