---
name: cardano
description: Cardano blockchain operations — build and submit transactions, delegate staking to stake pools, mint and manage native tokens and NFTs, interact with Plutus smart contracts, and participate in on-chain governance. Use when the user mentions ADA, Cardano transactions, staking delegation, stake pool selection, token minting, NFT creation, Plutus validators, or governance voting — even if they don't explicitly say "Cardano" (e.g., "delegate my ADA", "mint a token on the blockchain", "which stake pool should I choose").
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"₳"}'
  related-skills: '{"bitcoin":"Cardano uses UTxO like Bitcoin; understanding Bitcoin''s model helps explain Cardano''s design.","ethereum":"Contrasts Cardano''s UTxO model with Ethereum''s account model and EVM.","blockchain":"Provides foundational blockchain concepts underlying Cardano.","polkadot":"Another proof-of-stake blockchain with cross-chain capabilities; compares governance and staking models.","crypto-tools":"Real-time Cardano price data, portfolio tracking, and transaction monitoring.","trading":"ADA trading analysis, technical patterns, and risk management for Cardano positions."}'
---

# Cardano Operations Guide

Operational guide for Cardano blockchain tasks. This skill assumes you have `cardano-cli` installed and configured.

## Gotchas

**UTxO model is not accounts** — You cannot spend "part" of a UTxO. Transactions consume entire UTxOs and create change outputs automatically. This is fundamentally different from Ethereum's account model.

**Fees are deterministic** — Calculate fees before building transactions. Fees depend on transaction size (bytes), not gas or complexity.

**Minimum UTxO value** — Every output must contain at least ~1 ADA (varies with token count). Outputs below this threshold are rejected.

**Staking rewards delay** — First rewards appear 15-20 days after delegation (3-4 epochs), not immediately.

**Pool saturation** — Pools above saturation threshold give diminishing rewards. Always check saturation before delegating.

**Policy ID is the token identifier** — Token names can be faked. Always verify by policy ID, not name.

**Time-locked policies are irreversible** — Once a time-lock expires, tokens cannot be minted or burned. Verify slot numbers carefully.

**Smart contracts require collateral** — Plutus interactions need a collateral UTxO (typically 5 ADA) that is consumed only if the script fails on-chain.

**Governance delegation is separate from staking** — Same ADA, two independent signals: stake pool delegation earns rewards, DRep delegation assigns voting power.

## Decision Tree: What Are You Doing?

### 1. Building a Transaction

**Check first:**
- [ ] Have enough ADA for outputs + fees + minimum UTxO values
- [ ] UTxOs are not overly fragmented (< 50 UTxOs ideal)
- [ ] Network parameters are current (`cardano-cli query protocol-parameters`)

**Workflow:**
```bash
# 1. Query UTxOs
cardano-cli query utxo --address $ADDR --mainnet

# 2. Calculate fee
cardano-cli transaction calculate-min-fee \
  --tx-body-file tx.draft \
  --tx-in-count 2 \
  --tx-out-count 2 \
  --witness-count 1 \
  --protocol-params-file protocol.json

# 3. Build transaction
cardano-cli transaction build \
  --tx-in TXHASH#IX \
  --tx-out "RECIPIENT+AMOUNT" \
  --change-address $ADDR \
  --out-file tx.draft

# 4. Sign and submit
cardano-cli transaction sign --tx-body-file tx.draft --signing-key-file $ADDR.skey --out-file tx.signed
cardano-cli transaction submit --tx-file tx.signed --mainnet
```

**If transaction fails:**
- "Insufficient funds for fee" → Add more UTxOs or reduce output
- "Minimum UTxO not met" → Increase output to ≥ 1 ADA
- "UTxO too fragmented" → Consolidate with self-transfer first
- "Transaction too large" → Split into multiple transactions

🔴 **CHECKPOINT: Before signing** — Verify recipient address (first/last 4 chars), confirm amount + fee, ensure correct network (mainnet vs testnet).

**Load for details:** [references/utxo-and-transactions.md](references/utxo-and-transactions.md) — fee calculation, minimum UTxO, metadata standards, and advanced transaction building.

### 2. Delegating Stake

**Check first:**
- [ ] Staking key is registered
- [ ] Pool is not oversaturated (< 100% saturation)
- [ ] Pool has produced blocks in last 30 epochs
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
  --tx-in TXHASH#IX \
  --tx-out "$ADDR+5000000" \
  --change-address $ADDR \
  --certificate-file stake.cert \
  --certificate-file deleg.cert \
  --out-file tx.draft
```

**Pool selection criteria (in priority order):**
1. Saturation < 100% (select pools with saturation below 100%)
2. Block production ratio ≥ 0.8 (actual/expected blocks)
3. Cost structure appropriate for your stake size
4. Operator pledge > 1% of pool stake
5. Uptime > 99%

🔴 **CHECKPOINT: Before delegating** — Verify pool is not oversaturated, has produced blocks in last 30 epochs, and cost structure matches your delegation size. Delegation takes effect at next epoch boundary; rewards appear 15-20 days later.

**Load for details:** [references/staking.md](references/staking.md) — pool evaluation workflow, reward calculation, epoch timing, and verification checkpoints.

### 3. Minting Native Tokens

**Check first:**
- [ ] Policy script is correctly configured (time-lock, signatures)
- [ ] Metadata follows CIP-25 (NFT) or CIP-68 (fungible) standard
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
  --mint "1 POLICY_ID.ASSET_NAME" \
  --minting-script-file policy.script \
  --metadata-json-file metadata.json \
  --tx-in TXHASH#IX \
  --tx-out "RECIPIENT+2000000+1 POLICY_ID.ASSET_NAME" \
  --change-address $ADDR \
  --invalid-hereafter EXPIRY_SLOT \
  --out-file tx.draft
```

**Token safety:**
- Always verify policy ID, not just token name
- Check IPFS pinning is permanent before buying NFTs
- Time-locked policies cannot mint/burn after expiry

🔴 **CHECKPOINT: Before minting** — Test policy script on testnet first, verify metadata format matches CIP standard, confirm time-lock slot is in the future (calculate current slot: `cardano-cli query tip --mainnet | jq .slot`). Once minted, policy ID is permanent.

**Load for details:** [references/tokens-and-nfts.md](references/tokens-and-nfts.md) — policy script types, CIP standards, minting/burning workflows, and marketplace verification.

### 4. Interacting with Smart Contracts

**Check first:**
- [ ] Collateral UTxO available (typically 5 ADA)
- [ ] Datum and redeemer formats match validator expectations
- [ ] Script version is compatible with current era
- [ ] Execution units are estimated

**Workflow:**
```bash
# 1. Prepare collateral
cardano-cli transaction build \
  --tx-in TXHASH#IX \
  --tx-out "$ADDR+5000000" \
  --change-address $ADDR \
  --out-file collateral.draft

# 2. Build script transaction
cardano-cli transaction build \
  --tx-in-collateral COLLATERAL_TXHASH#IX \
  --tx-in SCRIPT_UTXO \
  --tx-in-script-file validator.plutus \
  --tx-in-redeemer-value '{"constructor": 0, "fields": []}' \
  --tx-in-datum-value '{"constructor": 0, "fields": []}' \
  --tx-out "RECIPIENT+AMOUNT" \
  --change-address $ADDR \
  --out-file tx.draft
```

**If script fails:**
- "Non-optimistic script evaluation" → Check datum/redeemer format
- "Insufficient collateral" → Provide adequate collateral
- "Script execution failed on-chain" → Verify context requirements

🔴 **CHECKPOINT: Before submitting Plutus transaction** — Verify collateral UTxO is available (5 ADA), datum/redeemer JSON matches validator expectations, and execution units are estimated. Collateral is consumed only if script fails on-chain.

**Load for details:** [references/smart-contracts.md](references/smart-contracts.md) — EUTxO model, development languages, validator scripts, execution units, and PlutusV3 features.

### 5. Participating in Governance

**Check first:**
- [ ] Staking key is registered
- [ ] You understand the governance action being voted on
- [ ] DRep delegation is active (if delegating voting power)

**Workflow:**
```bash
# Delegate voting power to DRep
cardano-cli governance vote-delegation-certificate \
  --stake-verification-key-file stake.vkey \
  --drep-verification-key-file drep.vkey \
  --out-file drep-deleg.cert

# Submit in transaction
cardano-cli transaction build \
  --tx-in TXHASH#IX \
  --tx-out "$ADDR+5000000" \
  --change-address $ADDR \
  --certificate-file drep-deleg.cert \
  --out-file tx.draft
```

**Governance actions:**
- Motion of no-confidence
- Constitutional committee election
- Constitution updates
- Hard-fork initiation
- Protocol parameter changes
- Treasury withdrawals
- Info actions

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
- Aiken — Most popular in 2025, purpose-built for Cardano
- Plutus (Haskell) — Original, full-featured
- OpShin — Python-based, lower barrier

## Network Parameters

**Epoch:** 5 days
**Slot time:** 1 second
**Block time:** ~20 seconds average
**Minimum UTxO:** ~1 ADA (varies with token count)
**Transaction fee:** Base 155381 lovelace + 44 lovelace per byte
**Max transaction size:** 16384 bytes
**Staking rewards:** ~3-5% APY (varies with total staked ratio)

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
- [ ] Confirm time-lock slot is in the future

## References

- [Cardano documentation](https://docs.cardano.org/)
- [Cardano Improvement Proposals (CIPs)](https://github.com/cardano-foundation/CIPs)
- [Developer portal](https://developers.cardano.org/)
- [Intersect MBO](https://www.intersectmbo.org/) — Cardano's member-based organization
