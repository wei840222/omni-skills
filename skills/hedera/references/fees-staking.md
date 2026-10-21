# Fees and staking

## Fee model

- Hedera publishes USD-denominated base fees that are paid in HBAR at the current exchange rate. The same fee tables apply on mainnet and testnet; only the HBAR (real vs test) differs.
- Typical simple transfers are on the order of ~`$0.0001`, but extras (extra signatures, memos, larger payloads, high-volume multipliers, contract gas) increase the charge. Use the official fee tables / Fee Estimator before quoting a hard number.
- Network fees are not an Ethereum-style priority-gas auction. For smart contracts, gas still meters EVM work and is charged in HBAR-denominated units; insufficient gas fails the call while consumed gas may still be charged.

## Staking

- Accounts can stake HBAR to a node or to another account. Docs state there is no lock-up: the staked balance remains liquid for transfers while staked.
- An account stakes to at most one node or one account at a time. Rewards and pending-reward fields are visible via account info / mirror node; users can decline rewards.
- Prefer current staking FAQ / account-property docs over memorized APY figures.

## Memos

- Account and transaction memos are public network data. Never place private keys, seed phrases, passwords, or government IDs in a memo.
- Exchange deposits often require a specific memo / destination-tag style string. Verify the exchange's current deposit instructions before sending.
- Keep memos short; transaction memo capacity is network-limited (`transaction.maxMemoUtf8Bytes` and related account memo limits). Prefer the live limit over a remembered constant when size matters.
