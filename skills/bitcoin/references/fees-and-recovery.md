# Fee timing and stuck transaction recovery

## Fee timing

- Check live recommended fees: `https://mempool.space/api/v1/fees/recommended`
- Wallet-native fee estimates can lag 12–24 hours behind mempool conditions.
- Low-urgency transfers often fare better on weekends or UTC 00:00–06:00 when congestion is lower.

## RBF vs CPFP

| Actor | Tool | When it works |
|-------|------|---------------|
| Sender | RBF | Original tx signaled replaceability; broadcast higher-fee replacement with same inputs |
| Receiver | CPFP | Receiver controls at least one unconfirmed output and can spend it with a high child fee |
| Neither path available | Wait | Tx may confirm later or drop from mempools after prolonged non-inclusion |

## Decision order

1. Confirm the tx is still unconfirmed via mempool.space.
2. If user is sender and RBF is enabled → bump fee with RBF.
3. Else if user can spend an unconfirmed output → CPFP.
4. Else wait or ask the counterparty (sender) to RBF; do not promise instant failure of a low-fee tx.

## API checks

```bash
curl -s "https://mempool.space/api/tx/{txid}"
curl -s "https://mempool.space/api/address/{address}"
curl -s "https://mempool.space/api/v1/fees/recommended"
```
