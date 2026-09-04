# Sources for Ethereum operational claims

Use these primary sources when validating fee markets, L2 withdrawals, approvals, or MEV protection behavior.

| Topic | Source | Applied guidance |
| --- | --- | --- |
| EIP-1559 fee market | [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) | `baseFee` is burned; users set `maxFeePerGas` and `maxPriorityFeePerGas`; unused gas is refunded. |
| Blob data availability (Dencun) | [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844) | Blob-carrying transactions reduce L2 data-availability cost versus calldata. |
| ERC-20 approvals | [EIP-20](https://eips.ethereum.org/EIPS/eip-20) | `approve` grants spend allowance; unlimited approvals remain until revoked or spent down. |
| Gasless approvals | [EIP-2612](https://eips.ethereum.org/EIPS/eip-2612) | Permit signatures authorize allowances off-chain; treat approval-like signatures as high risk. |
| Optimism withdrawal delay | [OP Stack: Withdrawals](https://docs.optimism.io/stack/transactions/withdrawal) | Native Optimistic Rollup withdrawals include a challenge/fraud-proof window before finalization on L1. |
| Arbitrum withdrawals | [Arbitrum: Withdrawing](https://docs.arbitrum.io/for-users/how-tos/withdraw-to-l1) | Native withdrawals follow the rollup challenge period; fast bridges are third-party alternatives. |
| Flashbots Protect | [Flashbots Protect](https://docs.flashbots.net/flashbots-protect/overview) | Private RPC submission hides txs from the public mempool until inclusion. |
| Address checksum | [EIP-55](https://eips.ethereum.org/EIPS/eip-55) | Mixed-case checksum encoding helps catch typed address errors. |
