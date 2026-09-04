# Gas (EIP-1559)

- `maxFeePerGas` = max total you'll pay per gas unit. `maxPriorityFeePerGas` = tip to validator. `baseFee` = burned, set by protocol
- Actual cost: `min(baseFee + priorityFee, maxFee) × gasUsed` — unused gas is refunded, but failed txs still consume gas
- Gas limit is separate from gas price — setting limit too low causes "out of gas" revert, but you still pay for gas used up to that point
- Check current base fee at etherscan.io/gastracker or via `eth_gasPrice` RPC — wallets often overestimate by 20-50%
