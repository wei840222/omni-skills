---
name: hedera
description: >
  Assist with Hedera HBAR transfers, account creation, Hedera Token Service
  (HTS) association, staking, and consensus or file service lookups. Use when
  the user asks about Hedera account IDs (0.0.x), HBAR fees, token association
  failures, mirror-node queries, or Hashgraph finality. Prefer `ethereum` for
  EVM L1/L2 gas and approvals, `solana` for SPL/ATA issues, and `crypto-tools`
  for cross-chain market or explorer tooling.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"ℏ"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Workflow

1. Identify the network (`mainnet` / `testnet` / `previewnet`), account ID or alias, token ID, transaction ID/status, and whether the ask is native HTS or EVM/smart-contract.
2. Load only the reference that covers that branch. Prefer current fee tables, mirror-node receipts, or explorer data over memorized prices.
3. Before irreversible advice, verify the recipient account exists (or is a valid auto-create path), required token associations, keys/signatures, and the exact error code.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/accounts.md` | Creating, funding, deleting, or explaining Hedera account IDs, aliases, hollow accounts, or keys. |
| `references/tokens.md` | Creating or transferring HTS fungible/NFT tokens, association requirements, or admin-key risk. |
| `references/fees-staking.md` | Estimating fees, explaining USD-denominated pricing paid in HBAR, or staking/liquidity. |
| `references/services.md` | Consensus (HCS), File (HFS), smart-contract/EVM, or mirror-node query guidance. |
| `references/troubleshooting.md` | Interpreting a concrete Hedera status code or failed transfer. |
| `references/sources.md` | Re-checking mutable fee, association, staking, or network claims against primary docs. |

## Critical rules

1. **Advise only** — draft SDK steps or wallet actions; do not request private keys or operate someone else's account.
2. **Network first** — mainnet uses real HBAR; testnet/previewnet use valueless test HBAR and may reset.
3. **Association before custom tokens** — HTS receivers usually must associate (or use a documented auto-association path) before a transfer succeeds.
4. **Public memos** — treat account and transaction memos as public; never put secrets there.
5. **Verify with live sources** — fee USD amounts and network parameters change; open `references/sources.md` or the live fee estimator before quoting exact costs.
