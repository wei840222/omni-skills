# UTxO Model and Transactions

Before using an artifact-producing command, define this preflight and call it with every new output path:

```bash
require_new_outputs() {
  for output_path in "$@"; do
    [ -n "$output_path" ] || { printf '%s\n' 'Set every output path before continuing.' >&2; return 2; }
    [ ! -e "$output_path" ] || { printf 'Refusing to overwrite: %s\n' "$output_path" >&2; return 1; }
  done
}
```

## UTxO Fundamentals

Cardano uses the Extended UTxO (EUTxO) model, fundamentally different from account-based chains like Ethereum.

**Key concepts:**
- Each transaction consumes existing UTxOs and creates new ones
- Wallet balance = sum of all UTxOs, not a single account balance
- Transaction fees depend on transaction size (bytes), not gas
- Change outputs are created automatically when consuming full UTxOs
- Minimum ADA value is required for each output to prevent dust accumulation; calculate it from current protocol parameters and the exact output shape

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
  --tx-body-file "$TX_DRAFT_FILE" \
  --tx-in-count 2 \
  --tx-out-count 2 \
  --witness-count 1 \
  --byron-witness-count 0 \
  --protocol-params-file "$PROTOCOL_PARAMS_FILE"
```

Fetch protocol parameters for the intended network before building. The current fee coefficients and output-cost parameter are network configuration, not constants for this skill.

### Minimum UTxO value

Every output must contain at least the minimum ADA value to cover the cost of storing the UTxO on-chain. Calculate with:

```bash
cardano-cli transaction calculate-min-required-utxo \
  --tx-out "addr1...+1000000+policyid.assetname" \
  --protocol-params-file "$PROTOCOL_PARAMS_FILE"
```

The result depends on the actual address, datum, reference script, and asset bundle. Use the command result for the output you will include in the draft rather than a rule-of-thumb ADA amount.

### Transaction size limits

The maximum transaction size is a current protocol parameter. When a draft exceeds the active limit:
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
  --protocol-params-file "$PROTOCOL_PARAMS_FILE"
```

**Fix:** Increase output value to meet minimum

### "UTxO too fragmented"

**Symptoms:**
- High transaction fees
- "Transaction too large" errors
- Slow transaction building

**Diagnosis:** Count UTxOs in wallet
```bash
require_new_outputs "$UTXO_REPORT_FILE" || exit $?
cardano-cli query utxo --address addr1... --out-file "$UTXO_REPORT_FILE"
cat "$UTXO_REPORT_FILE" | jq 'length'
```

**Fix:** Consolidate with self-transfer
```bash
# Build a self-transfer from explicitly selected inputs.
# First inspect every input and present the draft for user approval.
require_new_outputs "$CONSOLIDATION_DRAFT_FILE" || exit $?
cardano-cli transaction build \
  --tx-in "$SELECTED_TX_IN" \
  --change-address "$ADDRESS" \
  --mainnet \
  --out-file "$CONSOLIDATION_DRAFT_FILE"
```

### "Collateral required"

**Cause:** Smart contract interaction requires collateral UTxO

**Fix:** Designate an ADA-only collateral UTxO sized for the active protocol parameters and draft transaction
```bash
cardano-cli transaction build \
  --tx-in-collateral COLLATERAL_UTXO \
  ...
```

Collateral is only consumed if the transaction fails on-chain (which shouldn't happen with proper off-chain validation).

### "Transaction too large"

**Cause:** Transaction exceeds the current maximum transaction size

**Fix:**
- Reduce input count (consolidate UTxOs first)
- Reduce output count (split into multiple transactions)
- Remove unnecessary metadata

## Metadata

Transaction metadata limits are protocol parameters. Check the current limit before preparing metadata:

```bash
# Create metadata at a new, user-selected path.
require_new_outputs "$METADATA_FILE" || exit $?
cat << EOF > "$METADATA_FILE"
{
  "674": {
    "msg": ["Transaction message"]
  }
}
EOF

# Include in transaction
cardano-cli transaction build \
  --metadata-json-file "$METADATA_FILE" \
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
