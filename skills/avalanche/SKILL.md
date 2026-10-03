---
name: avalanche
description: >
  Assist with Avalanche Primary Network operations across C-Chain, X-Chain, and
  P-Chain: AVAX transfers, C-Chain gas, atomic cross-chain moves, staking or
  delegation, Avalanche L1/subnet context, and bridging. Use when the user asks
  about Avalanche, AVAX, Core wallet multi-chain flows, C-Chain RPC/chain id
  43114, P-Chain validators, or moving assets to or from Avalanche. Not for
  generic Ethereum L1-only work unless the user is bridging to Avalanche.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔺"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Workflow

1. Identify the chain role (C / X / P), wallet capability, asset location, and the exact operation (transfer, gas, stake/delegate, bridge, L1/subnet, or failure).
2. Load only the reference that matches that branch, then verify with an explorer, RPC, Core wallet status, or primary docs before advising irreversible moves.
3. Prefer official Core / Avalanche tooling for multi-chain and P-Chain work; treat MetaMask-class wallets as C-Chain-only unless the user already added another network.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/architecture.md` | Explaining Primary Network roles, C/X/P separation, or Avalanche L1/subnet context. |
| `references/c-chain.md` | Handling C-Chain transactions, gas paid in AVAX, RPC/chain id, explorers, or EVM wallet setup. |
| `references/cross-chain.md` | Moving AVAX between C/X/P, atomic export/import, or bridging from other networks. |
| `references/staking.md` | Validator vs delegator stakes, lock periods, rewards, or liquid-staking handoffs. |
| `references/troubleshooting.md` | Diagnosing insufficient gas, wrong-chain balances, missing tokens, or wallet limits. |
| `references/sources.md` | Verifying stake floors, chain roles, RPC, bridge, or wallet claims against primary docs. |
