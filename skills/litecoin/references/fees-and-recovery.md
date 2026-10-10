# Fees, confirmations, and stuck-transaction recovery

## Network timing

- Litecoin targets **2.5 minute** block intervals (`consensus.nPowTargetSpacing = 2.5 * 60` in Core).
- Rough guidance: 1 confirmation ≈ one block; many high-value or exchange flows wait on the order of **6 confirmations (~15 minutes)**. Always defer to the venue’s published policy.
- Faster blocks than Bitcoin do **not** remove fee markets under congestion; size still matters.

## Fee model

- Fees track **transaction weight/size**, not the LTC amount sent.
- SegWit inputs/outputs generally reduce weight versus legacy-only constructions — prefer `ltc1` when supported end-to-end.
- Paying a legacy (`L`) or older P2SH output from a SegWit wallet still works on main chain, but you may not capture the full fee reduction of SegWit-to-SegWit transfers.
- Dust-sized UTXOs can cost more to spend than they are worth; avoid consolidating dust into valuable inputs carelessly.

## RBF and recovery order

Litecoin Core implements **opt-in full replace-by-fee** behavior aligned with BIP125-style signaling (see Core BIP list).

| Actor | Tool | When it works |
| --- | --- | --- |
| Sender | RBF | Original transaction signaled replaceability; broadcast a higher-fee replacement spending the same inputs |
| Receiver | Child-pays-for-parent style bump | Only if the receiver can spend an unconfirmed output they control with a high-fee child |
| Neither | Wait | Tx may confirm when congestion falls, or drop from mempools after prolonged non-inclusion |

### Decision order

1. Confirm the tx is still **unconfirmed** on a public explorer the user trusts.
2. If the user is the **sender** and RBF was enabled → fee-bump via replacement.
3. Else if the user can spend an unconfirmed output → high-fee child spend.
4. Else wait or ask the sender to RBF. Do not claim a low-fee tx has “failed forever” after a few hours.

## Confirmation language

- **Unconfirmed** = in mempool / not in a block yet.
- **N confirmations** = included in a block plus N−1 descendants.
- Exchange credit policies differ; never invent a universal confirmation count for withdrawals or deposits.
