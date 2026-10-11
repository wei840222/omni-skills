---
name: polygon
description: >
  Assist with Polygon Chain (PoS) wallets, POL/MATIC gas, RPC setup, official
  Portal bridging, and stuck-tx recovery. Use when a user adds chain 137/Amoy,
  migrates MATIC→POL, bridges via portal.polygon.technology, or confuses PoS
  with deprecated Polygon zkEVM / other EVMs. Prefer ethereum for generic L1
  gas/approvals, blockchain for ledger fundamentals, crypto-tools for market
  data once mechanics are settled.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🟣"}'
  related-skills: '{"ethereum":"Generic EVM gas, approvals, and L1/L2 patterns outside Polygon Chain specifics.","blockchain":"Ledger fundamentals and contract interaction beyond Polygon operations.","crypto-tools":"Prices, explorers, and portfolio tooling after Polygon tx mechanics are clear."}'
---

# Polygon Chain

Stateless guidance for **Polygon Chain (PoS) network setup, POL gas, MATIC→POL
migration, official Portal bridging, and transaction troubleshooting**. Do not
store keys, seeds, or wallet exports in this package.

## When to load

- Add Polygon mainnet (chain ID `137`) or Amoy testnet (`80002`) to a wallet
- Pay gas with **POL** (formerly MATIC) or fix "insufficient MATIC/POL" errors
- Migrate remaining MATIC on Ethereum to POL, or fix wallet symbol still showing MATIC
- Bridge tokens with the official **Polygon Portal** (lock/mint, checkpoint exits)
- Clarify deprecated **Polygon zkEVM** vs current Polygon Chain / CDK guidance

## Hard defaults

1. **Name the network before the asset** — Polygon Chain ≠ Ethereum ≠ deprecated zkEVM. Same address format, different balances and gas tokens.
2. **Gas on Polygon Chain is POL** — bridged ETH/USDC/etc. do not pay PoS gas. Keep a POL reserve after every bridge-in.
3. **Official bridge UI is Portal** — `https://portal.polygon.technology` (not the retired `bridge.polygon.technology` hostname).
4. **zkEVM is deprecated for new work** — do not recommend new zkEVM integrations; prefer Polygon Chain or Polygon CDK / Agglayer paths.
5. **Re-open `references/sources.md`** before restating chain IDs, RPC hosts, withdrawal timing, or migration steps.

## Ordered workflow

1. **Classify** — wallet/RPC setup, gas/POL, MATIC migration, Portal bridge in/out, stuck tx, or zkEVM legacy question.
2. **Load one reference** that matches the branch (table below).
3. **Verify on-chain** with the matching explorer or Portal status before irreversible advice (send, approve, bridge exit).
4. **Hand off** to `ethereum` for generic EIP-1559/approvals, `blockchain` for contract design, `crypto-tools` for prices/TVL.

## Progressive disclosure

| Need | Load |
|------|------|
| Networks, chain IDs, RPC, POL gas, wallet symbol | `references/network.md` |
| Portal bridge deposit/withdraw, checkpoints, third-party risk | `references/bridging.md` |
| MATIC→POL migration paths (Ethereum / PoS / legacy zkEVM) | `references/migration.md` |
| Tokens, DeFi orientation, staking notes | `references/ecosystem.md` |
| Deprecated zkEVM boundary and safe redirects | `references/zkevm.md` |
| Stuck txs, missing tokens, security checklist | `references/troubleshooting.md` |
| Official docs and citation anchors | `references/sources.md` |
