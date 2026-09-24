# BNB Ecosystem & Security

## DeFi Ecosystem
- PancakeSwap is the largest DEX on the chain (similar to Uniswap).
- Venus is used for lending and borrowing (similar to Aave).
- Higher rug pull risk exists due to a less rigorous auditing culture; verify contracts on bscscan before interacting.

## Wallet Configuration
- MetaMask works natively by adding the BNB Chain network.
- Chain ID: 56
- RPC: `https://bsc-dataseed.binance.org`
- Block Explorer: `https://bscscan.com`
- Trust Wallet has native support. Hardware wallets work via MetaMask.

## Staking
- Stake BNB with validators to earn rewards.
- Unbonding period is 7 days.
- Slashing risks exist; choose reliable validators.
- Liquid staking options like stkBNB and ankrBNB are available.

## Common Issues & Security
- **"Insufficient funds for gas"**: Ensure you have native BNB for gas, not just BEP-20 tokens.
- **Wrong network**: Sending tokens to the same address on a different chain.
- Revoke unused approvals using bscscan.com token approval checker.
- Verify all contract addresses against official sources.

## Common Scams
- Honeypot tokens — can buy but not sell
- Fake PancakeSwap sites — always verify URL
- Airdropped tokens you didn't request — often scam triggers
- "Validators" asking for private keys — never share

## Additional Security
- Same security model as Ethereum — private key = full access
- Use hardware wallet for large amounts — same setup as Ethereum
- Maintain distance from unknown airdropped tokens — can contain malicious contracts
