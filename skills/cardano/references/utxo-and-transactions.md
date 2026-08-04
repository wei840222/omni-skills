# UTxO Model and Transactions

## UTxO Fundamentals

Cardano uses the Extended UTxO (EUTxO) model, fundamentally different from account-based chains like Ethereum.

**Key concepts:**
- Each transaction consumes existing UTxOs and creates new ones
- Wallet balance = sum of all UTxOs, not a single account balance
- Transaction fees depend on transaction size (bytes), not gas
- Change outputs are created automatically when consuming full UTxOs
- Minimum UTxO value required (~1 ADA) to prevent dust accumulation

**Implications for transaction building:**
- You cannot spend "part" of a UTxO — you must consume the entire output and create change
- More inputs/outputs = larger transaction = higher fee
- UTxO fragmentation (many small UTxOs) increases fees and can exceed transaction size limits
- Consolidation via self-transfer reduces fragmentation

## Transaction Construction

### Fee calculation

Transaction fees are deterministic and calculated before submission:

```bash
# Calculate fee (example)
cardano-cli transaction calculate-min-fee \
  --tx-body-file tx.draft \
  --tx-in-count 2 \
  --tx-out-count 2 \
  --witness-count 1 \
  --byron-witness-count 0 \
  --protocol-params-file protocol.json
```

Current fee structure (as of Conway era):
- Base fee: 155381 lovelace
- Per-byte fee: 44 lovelace
- Per-word fee: 0 lovelace (deprecated)

### Minimum UTxO value

Every output must contain at least the minimum ADA value to cover the cost of storing the UTxO on-chain. Calculate with:

```bash
cardano-cli transaction calculate-min-required-utxo \
  --tx-out "addr1...+1000000+policyid.assetname" \
  --protocol-params-file protocol.json
```

Typical minimums:
- ADA-only output: ~1 ADA
- Output with native tokens: ~1.2-1.5 ADA (depends on token count)

### Transaction size limits

Maximum transaction size: 16384 bytes. When transactions exceed this:
- Split into multiple transactions
- Consolidate UTxOs first to reduce input count
- Reduce output count if possible

## Common Transaction Failures

### "Insufficient funds for fee"

**Cause:** Total inputs < total outputs + fee

**Diagnosis:**
1. Calculate total input value
2. Calculate total output value
3. Calculate fee
4. Verify: inputs ≥ outputs + fee

**Fix:** Add more UTxOs as inputs, or reduce output value

### "Minimum UTxO not met"

**Cause:** Output value below minimum required

**Diagnosis:**
```bash
cardano-cli transaction calculate-min-required-utxo \
  --tx-out "ADDRESS+VALUE+ASSETS" \
  --protocol-params-file protocol.json
```

**Fix:** Increase output value to meet minimum

### "UTxO too fragmented"

**Symptoms:**
- High transaction fees
- "Transaction too large" errors
- Slow transaction building

**Diagnosis:** Count UTxOs in wallet
```bash
cardano-cli query utxo --address addr1... --out-file utxos.json
cat utxos.json | jq 'length'
```

**Fix:** Consolidate with self-transfer
```bash
# Send all UTxOs back to yourself in one transaction
cardano-cli transaction build \
  --tx-in $(cardano-cli query utxo --address addr1... | awk 'NR>2 {print $1"#"$2}' | tr '\n' ' ') \
  --tx-out "addr1...+TOTAL_VALUE" \
  --change-address addr1... \
  --out-file consolidate.tx
```

### "Collateral required"

**Cause:** Smart contract interaction requires collateral UTxO

**Fix:** Designate a collateral UTxO (typically 5 ADA)
```bash
cardano-cli transaction build \
  --tx-in-collateral COLLATERAL_UTXO \
  ...
```

Collateral is only consumed if the transaction fails on-chain (which shouldn't happen with proper off-chain validation).

### "Transaction too large"

**Cause:** Transaction exceeds 16384 bytes

**Fix:**
- Reduce input count (consolidate UTxOs first)
- Reduce output count (split into multiple transactions)
- Remove unnecessary metadata

## Metadata

Transactions can include up to 16KB of arbitrary metadata:

```bash
# Create metadata file
cat << EOF > metadata.json
{
  "674": {
    "msg": ["Transaction message"]
  }
}
EOF

# Include in transaction
cardano-cli transaction build \
  --metadata-json-file metadata.json \
  ...
```

Common metadata standards:
- CIP-20: Transaction metadata
- CIP-25: NFT metadata
- CIP-67: Fungible token metadata
- CIP-68: Token metadata with references

## References

- [Cardano documentation: UTxO model](https://docs.cardano.org/explore-cardano/cardano-monetary-policy/)
- [CIP-1: Cardano Improvement Proposals](https://github.com/cardano-foundation/CIPs)
- [EUTxO handbook](https://ucarecdn.com/3da33f2f-73ac-4c9b-844b-f215dcce0628/EUTXOhandbook_for_EC.pdf)
