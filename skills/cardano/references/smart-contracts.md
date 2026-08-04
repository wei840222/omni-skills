# Smart Contracts (Plutus)

## EUTxO Model for Smart Contracts

Cardano smart contracts differ fundamentally from Ethereum's EVM:

- **EUTxO model** — validators guard UTxOs locked at script addresses
- **Off-chain construction** — transactions are built off-chain, then submitted
- **Deterministic validation** — success depends only on the transaction and its inputs
- **No re-entrancy** — scripts cannot call other scripts during validation
- **Off-chain verifiable** — transaction validity can be checked before submission

## Development Languages

| Language | Type | Notes |
|----------|------|-------|
| Aiken | Purpose-built for Cardano | Most popular in 2025 developer survey |
| Plutus (Haskell) | Original smart contract language | Full-featured, steep learning curve |
| OpShin | Python-based | Lower barrier for Python developers |
| Helios | TypeScript-like | Familiar syntax for web developers |

## Key Concepts

### Validator scripts

Validators decide whether a transaction can consume a UTxO:

```
validator(redeemer, datum, context) -> bool
```

- **Datum** — data attached to the UTxO (state)
- **Redeemer** — input provided by the transaction spending the UTxO
- **Context** — the transaction being validated

### Minting policies

Control token minting/burning:

```
minting_policy(redeemer, context) -> bool
```

### Reference scripts

Scripts stored on-chain and referenced by transactions (use reference scripts to reduce transaction size):

```bash
# Attach script as reference to a UTxO
cardano-cli transaction build \
  --tx-out "ADDRESS+VALUE+1 POLICY_ID.ASSET_NAME" \
  --tx-out-reference-script-file script.plutus \
  ...

# Reference in spending transaction
cardano-cli transaction build \
  --tx-in "UTXO#0" \
  --tx-in-script-file script.plutus \
  --tx-in-reference-script \
  ...
```

## Transaction Building for Plutus

### Collateral

Smart contract interactions require collateral (typically 5 ADA):

```bash
cardano-cli transaction build \
  --tx-in-collateral COLLATERAL_UTXO \
  --tx-in SCRIPT_UTXO \
  --tx-in-script-file validator.plutus \
  --tx-in-redeemer-value '{"constructor": 0, "fields": []}' \
  --tx-in-datum-value '{"constructor": 0, "fields": []}' \
  ...
```

Collateral is consumed only if the script fails on-chain. With proper off-chain validation, this should not happen.

### Execution units

Scripts consume execution units (CPU steps and memory). Fees depend on units consumed:

```bash
# Check execution units for a script
cardano-cli transaction build \
  --tx-in SCRIPT_UTXO \
  --tx-in-script-file validator.plutus \
  --tx-in-execution-units "(EX_CPU, EX_MEM)" \
  ...
```

Optimize scripts to reduce execution units and lower fees.

## Common Plutus Issues

### "Non-optimistic script evaluation"

**Cause:** Script fails during off-chain evaluation

**Diagnosis:**
- Check datum and redeemer format
- Verify all required inputs are present
- Check script version compatibility

### "Insufficient collateral"

**Cause:** Collateral UTxO too small or missing

**Fix:** Provide adequate collateral (default: 5 ADA)

### "Script execution failed on-chain"

**Cause:** Script returned false during validation

**Diagnosis:**
- Verify datum matches expected format
- Check redeemer matches validator expectations
- Ensure all context requirements are met

### "Script size too large"

**Cause:** Serialized script exceeds limits

**Fix:**
- Use reference scripts to reduce transaction size
- Optimize script code
- Split logic across multiple validators when script size exceeds 4KB serialized

## PlutusV3 Features (Conway era)

- BLS12-381 primitives for zero-knowledge proofs
- Keccak-256 hash function (Ethereum compatibility)
- Blake2b-224 hash function
- Sums of products (SOPs) for efficient data encoding
- Bitwise primitives for low-level manipulation

## References

- [Plutus documentation](https://docs.cardano.org/developer-resources/smart-contracts/plutus)
- [Aiken language](https://aiken-lang.org/)
- [Plutus pioneer program](https://github.com/input-output-hk/plutus-pioneer-program)
- [Cardano developer portal](https://developers.cardano.org/)
- [OpShin documentation](https://github.com/OpShin)
