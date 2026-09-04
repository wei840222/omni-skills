---
name: ethereum
description: Assist with Ethereum transactions, optimize gas, audit token approvals, troubleshoot reverts, and navigate L2 bridges. Use when a user asks about ETH transactions, gas tracking, MEV, or L2 bridging.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⟠"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Workflow

1. Identify the chain (L1 vs L2), wallet role, nonce/gas symptom, approval target, or bridge direction.
2. Load only the reference that matches that branch, then verify with an explorer, RPC, or simulation before advising irreversible actions.
3. Prefer exact-amount approvals, private/MEV-aware submission for sensitive swaps, and explicit wait/fee trade-offs for L2 exits.

## Load the relevant reference

| Reference | Load when |
|---|---|
| `references/transactions.md` | Handling stuck transactions or nonce gaps. |
| `references/gas.md` | Explaining EIP-1559, maxFeePerGas, baseFee, or fee optimization. |
| `references/security.md` | Auditing ERC-20 approvals, Permit/Permit2, or revoke flows. |
| `references/troubleshooting.md` | Diagnosing reverted or failed transactions. |
| `references/l2-bridges.md` | Assisting with L2 rollups, bridges, or withdrawal delays. |
| `references/mev.md` | Protecting swaps or transactions against frontrunning and MEV. |
| `references/addresses.md` | Verifying addresses, checksums, or ENS domains. |
| `references/sources.md` | Verifying fee-market, approval, L2, or MEV claims against primary docs. |
