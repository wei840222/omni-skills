# Fees, confirmations, and stuck-transaction recovery

## Network timing

- Dogecoin targets **1 minute** block intervals (`consensus.nPowTargetSpacing = 60` in Core `chainparams.cpp`).
- Rough guidance: 1 confirmation ≈ one block; many high-value or exchange flows wait on the order of **6+ confirmations**. Always defer to the venue’s published policy.
- Faster blocks than Bitcoin do **not** remove fee sizing by transaction weight/size.

## Fee model

- Fees track **transaction size**, not the DOGE amount sent.
- Consolidating many small (“dust”) UTXOs produces a larger transaction and a higher absolute fee.
- Most wallets select a relayable fee automatically; manual fee edits are uncommon for normal payments.
- Transactions below a node’s minimum relay fee are rejected rather than “pending forever at zero fee”.

## Stuck / unconfirmed recovery

| Actor | Tool | When it works |
| --- | --- | --- |
| Sender or receiver | Wait + explorer check | Default path; ~1 minute blocks usually clear ordinary fees quickly |
| Sender | Higher-fee **new** spend of the same coins | Only if the wallet/UI supports creating a replacement; **not** Bitcoin BIP125 RBF as a documented Dogecoin user workflow |
| Receiver-only | Wait / ask sender | Receiver cannot accelerate a payment they cannot spend |

### Decision order

1. Confirm the tx is still unconfirmed on a public Dogecoin explorer.
2. If the user expected Bitcoin-style RBF: explain Dogecoin does not offer that recovery path for ordinary users.
3. If fee was below relay or congestion is unusual: wait or recreate from a wallet that can rebuild the spend correctly—do not invent RBF steps.
4. If the user is only the receiver: wait or ask the sender/venue; do not promise CPFP unless they demonstrably control an unconfirmed output in a wallet that supports it.

## Dust and consolidation

- Very small UTXOs may cost more in fees than their value when spent.
- Avoid consolidating dust with primary UTXOs without a deliberate privacy/fee plan.
