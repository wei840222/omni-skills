# L2 Bridges and Withdrawals

- Optimistic rollups (Optimism, Arbitrum, Base) have 7-day withdrawal period to mainnet — this is not a bug, it's the security model
- ZK rollups (zkSync, Starknet) have faster finality but bridging back still takes 1-24 hours depending on liquidity
- Third-party bridges (Hop, Across) offer faster exits but charge fees and have smart contract risk
- Ensure you have sufficient liquidity to wait 7 days before bridging natively, or use a fast bridge and accept the fee if faster access is required

- Dencun Upgrade (EIP-4844): Introduced "blobs" (Proto-Danksharding) which significantly reduces L2 transaction fees by providing cheaper data availability.
