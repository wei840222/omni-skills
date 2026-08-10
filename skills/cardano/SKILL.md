---
name: cardano
description: "Guide Cardano operations: inspect and prepare transactions, explain stake-pool and DRep delegation, mint native assets, work with Plutus, and review governance actions. Use when the request explicitly mentions Cardano, ADA, Plutus, a Cardano stake pool, DRep, CIP-25/CIP-68, or a Cardano `addr1` address."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"₳"}'
  related-skills: '{"bitcoin":"Cardano uses UTxO like Bitcoin; understanding Bitcoin''s model helps explain Cardano''s design.","blockchain":"Provides foundational blockchain concepts underlying Cardano.","crypto-tools":"Real-time Cardano price data, portfolio tracking, and transaction monitoring.","ethereum":"Contrasts Cardano''s UTxO model with Ethereum''s account model and EVM.","polkadot":"Another proof-of-stake blockchain with cross-chain capabilities; compares governance and staking models.","trading":"ADA trading analysis, technical patterns, and risk management for Cardano positions."}'
---

# Cardano Operations Guide

Operational guide for Cardano blockchain tasks. This knowledge skill has no persistent state. It assumes a compatible `cardano-cli`, current node connection configuration, and an explicitly selected user network.

## Safety boundary

Use this skill to explain, inspect, and prepare transactions. Before a command can sign, submit, mint, delegate, or register a governance credential, present the complete transaction details (network, inputs, outputs, fee, certificates, policy ID, and validity interval) and obtain the user's explicit approval. Use testnet for first execution of a new policy or validator. Keep signing keys outside the skill package and use paths supplied by the user.

## Gotchas

**UTxO model is not accounts** — You cannot spend "part" of a UTxO. Transactions consume entire UTxOs and create change outputs automatically. This is fundamentally different from Ethereum's account model.

**Fees and minimum output ADA are protocol parameters** — Query current protocol parameters and calculate the minimum required ADA for each actual output. Values depend on the active network, transaction, and output shape.

**Minimum UTxO value** — Every output must contain the current minimum ADA required for its serialized shape. Outputs below that value are rejected.

**Staking rewards delay** — Delegation and reward timing span multiple epochs; confirm the current schedule before promising an arrival date.

**Pool saturation** — Evaluate saturation and recent performance with current explorer or pool data before delegating; protocol parameters and pool metrics change.

**Policy ID is the token identifier** — Token names can be faked. Always verify by policy ID, not name.

**Time-locked policies are irreversible** — Once a time-lock expires, tokens cannot be minted or burned. Verify slot numbers carefully.

**Smart contracts require collateral** — Plutus interactions need an ADA-only collateral UTxO sized for the current protocol parameters. Collateral is consumed only when the script transaction is invalid on-chain.

**Governance delegation is separate from staking** — Same ADA, two independent signals: stake pool delegation earns rewards, DRep delegation assigns voting power.

## Decision Tree: What Are You Doing?

### 1. Building a Transaction

**Check first:**
- [ ] Have enough ADA for outputs + fees + minimum UTxO values
- [ ] Current protocol parameters and minimum-output calculation are available
- [ ] The target network is explicit (`--mainnet` or its testnet equivalent)

**Workflow:**
```bash
# 1. Query UTxOs and current parameters on the intended network.
cardano-cli query utxo --address "$ADDRESS" --mainnet
cardano-cli query protocol-parameters --mainnet --out-file protocol.json

# 2. Build an unsigned draft. LOVELACE_AMOUNT is an integer in lovelace.
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --tx-out "$RECIPIENT+$LOVELACE_AMOUNT" \
  --change-address "$ADDRESS" \
  --mainnet \
  --out-file tx.draft

# 3. After the user approves the inspected draft, sign and submit.
cardano-cli transaction sign --tx-body-file tx.draft --signing-key-file "$SIGNING_KEY_FILE" --mainnet --out-file tx.signed
cardano-cli transaction submit --tx-file tx.signed --mainnet
```

**If transaction fails:**
- "Insufficient funds for fee" → Add more UTxOs or reduce output
- "Minimum UTxO not met" → Recalculate the required ADA for that exact output and increase it accordingly
- "UTxO too fragmented" → Consolidate with self-transfer first
- "Transaction too large" → Split into multiple transactions

🔴 **CHECKPOINT: Before signing** — Present the complete draft for explicit user approval: recipient address, lovelace and asset quantities, fee, certificates, validity interval, and exact network.

**Load for details:** [references/utxo-and-transactions.md](references/utxo-and-transactions.md) — fee calculation, minimum UTxO, metadata standards, and advanced transaction building.

### 2. Delegating Stake

**Check first:**
- [ ] Staking key is registered
- [ ] Current pool saturation and performance data are available
- [ ] The user has selected the pool after reviewing its current metrics
- [ ] Pool cost structure matches your delegation size

**Workflow:**
```bash
# 1. Register staking key (one-time)
cardano-cli stake-address registration-certificate \
  --staking-verification-key-file stake.vkey \
  --out-file stake.cert

# 2. Build delegation certificate
cardano-cli stake-address delegation-certificate \
  --staking-verification-key-file stake.vkey \
  --stake-pool-id POOL_ID \
  --out-file deleg.cert

# 3. Submit transaction with certificates
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --change-address "$ADDRESS" \
  --certificate-file stake.cert \
  --certificate-file deleg.cert \
  --mainnet \
  --out-file tx.draft
```

**Pool selection criteria (in priority order):**
1. Current saturation relative to the network target
2. Recent block-production history and operator reliability
3. Cost structure appropriate for the user's stake size
4. Operator pledge and published operational information
5. Pool's current status from an independent explorer or the operator

🔴 **CHECKPOINT: Before delegating** — Present the selected pool ID, current metrics, certificate contents, transaction fee, and network for explicit user approval. Explain that delegation and rewards take effect over future epochs, not immediately.

**Load for details:** [references/staking.md](references/staking.md) — pool evaluation workflow, reward calculation, epoch timing, and verification checkpoints.

### 3. Minting Native Tokens

**Check first:**
- [ ] Policy script is correctly configured (time-lock, signatures)
- [ ] Metadata follows the applicable standard: CIP-25 for NFT transaction metadata, CIP-67 for asset-name labels, or CIP-68 for datum metadata/reference-NFT patterns
- [ ] Asset name is hex-encoded
- [ ] Minimum UTxO value calculated for token output

**Workflow:**
```bash
# 1. Create policy script
cat > policy.script << EOF
{
  "type": "all",
  "scripts": [
    {"type": "before", "slot": EXPIRY_SLOT},
    {"type": "sig", "keyHash": "YOUR_KEY_HASH"}
  ]
}
EOF

# 2. Get policy ID
cardano-cli transaction policyid --script-file policy.script > policy.id

# 3. Build minting transaction
cardano-cli transaction build \
  --mint "1 $POLICY_ID.$ASSET_NAME_HEX" \
  --minting-script-file policy.script \
  --metadata-json-file metadata.json \
  --tx-in "$TX_IN" \
  --tx-out "$RECIPIENT+$MIN_OUTPUT_LOVELACE+1 $POLICY_ID.$ASSET_NAME_HEX" \
  --change-address "$ADDRESS" \
  --invalid-hereafter EXPIRY_SLOT \
  --mainnet \
  --out-file tx.draft
```

**Token safety:**
- Always verify policy ID, not just token name
- Check IPFS pinning is permanent before buying NFTs
- Time-locked policies cannot mint/burn after expiry

🔴 **CHECKPOINT: Before minting** — First exercise the policy on testnet. Then present the policy ID, asset name, mint/burn quantity, metadata, validity interval, fee, and mainnet transaction details for explicit user approval.

**Load for details:** [references/tokens-and-nfts.md](references/tokens-and-nfts.md) — policy script types, CIP standards, minting/burning workflows, and marketplace verification.

### 4. Interacting with Smart Contracts

**Check first:**
- [ ] ADA-only collateral UTxO sized for the current protocol parameters is available
- [ ] Datum and redeemer formats match validator expectations
- [ ] Script version is compatible with current era
- [ ] Execution units are estimated

**Workflow:**
```bash
# 1. Prepare collateral
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --tx-out "$ADDRESS+$COLLATERAL_LOVELACE" \
  --change-address "$ADDRESS" \
  --mainnet \
  --out-file collateral.draft

# 2. Build script transaction
cardano-cli transaction build \
  --tx-in-collateral COLLATERAL_TXHASH#IX \
  --tx-in SCRIPT_UTXO \
  --tx-in-script-file validator.plutus \
  --tx-in-redeemer-value '{"constructor": 0, "fields": []}' \
  --tx-in-datum-value '{"constructor": 0, "fields": []}' \
  --tx-out "$RECIPIENT+$LOVELACE_AMOUNT" \
  --change-address "$ADDRESS" \
  --mainnet \
  --out-file tx.draft
```

**If script fails:**
- "Non-optimistic script evaluation" → Check datum/redeemer format
- "Insufficient collateral" → Provide adequate collateral
- "Script execution failed on-chain" → Verify context requirements

🔴 **CHECKPOINT: Before submitting a Plutus transaction** — Present the collateral input and size, datum/redeemer, script version, evaluated execution units, fee, validity interval, outputs, and network for explicit user approval.

**Load for details:** [references/smart-contracts.md](references/smart-contracts.md) — EUTxO model, development languages, validator scripts, execution units, and PlutusV3 features.

### 5. Participating in Governance

**Check first:**
- [ ] Staking key is registered
- [ ] You understand the governance action being voted on
- [ ] DRep delegation is active (if delegating voting power)

**Workflow:**
```bash
# Delegate voting power to DRep
cardano-cli stake-address vote-delegation-certificate \
  --stake-verification-key-file stake.vkey \
  --drep-verification-key-file drep.vkey \
  --out-file drep-deleg.cert

# Submit in transaction
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --change-address "$ADDRESS" \
  --certificate-file drep-deleg.cert \
  --mainnet \
  --out-file tx.draft
```

**Governance actions:** Action type, required voting bodies, and thresholds vary. Review the action's current on-chain details and protocol parameters rather than applying a fixed percentage.

**Load for details:** [references/governance.md](references/governance.md) — CIP-1694, DRep delegation, registration, governance tools, and verification checkpoints.

## Common Anti-Patterns

**Transaction building:**
- ❌ Spending "part" of a UTxO → ✅ Consume entire UTxO, create change
- ❌ Ignoring UTxO fragmentation → ✅ Consolidate before large transactions
- ❌ Hardcoding fees → ✅ Calculate fees dynamically from protocol parameters

**Staking:**
- ❌ Choosing pools by lowest margin alone → ✅ Evaluate saturation, block production, costs
- ❌ Delegating to friends without analysis → ✅ Verify pool performance metrics
- ❌ Splitting delegation across many pools → ✅ Delegate to one well-performing pool

**Tokens:**
- ❌ Trusting token name → ✅ Verify policy ID
- ❌ Minting without time-lock → ✅ Use time-locked policies for limited supply
- ❌ Using `any` instead of `all` in scripts → ✅ Use `all` for stronger constraints

**Smart contracts:**
- ❌ Assuming Ethereum patterns work → ✅ Use EUTxO model (off-chain construction)
- ❌ Skipping collateral → ✅ Always provide collateral for script transactions
- ❌ Hardcoding execution units → ✅ Estimate units from script evaluation

## Tool Selection

**cardano-cli** — Official command-line tool
- Full transaction building, signing, submission
- Query UTxOs, protocol parameters, stake pools
- Certificate generation and submission

**Block explorers** — Verification and monitoring
- Cardanoscan (cardanoscan.io) — Transaction lookup, pool stats
- Pool.pm — UTxO visualization, asset tracking
- CExplorer (cexplorer.io) — Pool analytics, governance tracking

**Wallets** — Daily operations
- Daedalus — Full node, most secure, slow sync
- Yoroi — Light wallet, fast, browser extension
- Eternl — Advanced features, multi-wallet support

**Development** — Smart contracts
- Aiken — purpose-built for Cardano
- Plutus (Haskell) — Original, full-featured
- OpShin — Python-based, lower barrier

## Current protocol values

Do not copy fixed values for fees, minimum output ADA, transaction-size limits, collateral, deposits, or reward expectations. Query current parameters for the intended network and calculate against the actual draft transaction.

## Security Checklist

Before any transaction:
- [ ] Verify recipient address (check first/last characters)
- [ ] Confirm transaction amount and fee
- [ ] Check network (mainnet vs testnet)
- [ ] Verify policy IDs for token transactions
- [ ] Ensure sufficient UTxOs for outputs + fees

Before delegating:
- [ ] Verify pool is not oversaturated
- [ ] Check pool block production history
- [ ] Confirm operator pledge and cost structure

Before minting:
- [ ] Test policy script on testnet first
- [ ] Verify metadata format and IPFS links
- [ ] Confirm the validity interval and policy time-lock match the intended network

## References

- [Cardano documentation](https://docs.cardano.org/)
- [Cardano Improvement Proposals (CIPs)](https://github.com/cardano-foundation/CIPs)
- [Developer portal](https://developers.cardano.org/)
- [Intersect MBO](https://www.intersectmbo.org/) — Cardano's member-based organization
