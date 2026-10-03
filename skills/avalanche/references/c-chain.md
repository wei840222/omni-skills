# C-Chain operations

## Network parameters

- C-Chain is an EVM implementation (Coreth) on Avalanche.
- Mainnet chain id **43114**.
- Public HTTP RPC commonly documented as `https://api.avax.network/ext/bc/C/rpc` (confirm current provider docs if a vendor endpoint is required).
- Gas is paid in **AVAX only**. ERC-20 / DEX balances do not pay C-Chain gas.
- Fee market follows EIP-1559-style base fee + priority fee semantics; unused gas is not a reason to ignore failed-tx cost—reverted transactions still consume gas.

## Wallet fit

- **Core**: official multi-chain wallet for C/X/P and many L1 flows.
- **MetaMask (and most browser EVM wallets)**: C-Chain only unless the user manually adds another EVM network. They cannot natively export/import to X-Chain or manage P-Chain validators.
- Hardware wallets are typically used through Core or an EVM wallet connector for C-Chain.

## Tokens and DeFi on C-Chain

- Native gas/value asset: AVAX.
- Wrapped AVAX (WAVAX) appears in AMM / lending flows that need an ERC-20 form of AVAX.
- Verify token contracts on an Avalanche explorer before swapping; scam tokens reuse tickers.
- Bridged assets from other networks are usually wrapped representations (for example `*.e` style naming from the Avalanche Bridge era)—treat the bridge receipt and token contract as the source of truth.

## Before sending a C-Chain transaction

1. Confirm the wallet is on Avalanche C-Chain (chain id 43114), not Ethereum mainnet or an L1 EVM.
2. Confirm spendable **AVAX** covers value + max fee.
3. For token transfers, confirm the token contract and decimals on an explorer.
4. After broadcast, verify the tx hash status on an explorer before declaring success.
