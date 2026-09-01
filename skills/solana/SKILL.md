---
name: solana
description: Troubleshoot Solana transactions, token accounts, priority fees, and wallet safety. Use when handling Solana transfers, SPL token accounts, transaction failures, compute budgets, RPCs, or wallet configuration.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"◎"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Workflow

1. Identify the cluster, wallet role, token mint, transaction signature, and exact error or intended operation.
2. Load the reference that covers that branch, then use RPC data, simulation output, or program logs as the current source of truth.
3. Verify the resulting signature status and expected account state before reporting completion.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/accounts.md` | Handling wallet addresses, SOL balances, token accounts, or account-creation requirements. |
| `references/transactions.md` | Diagnosing transaction lifecycle, blockhash expiry, priority fees, or compute budgets. |
| `references/troubleshooting.md` | Interpreting a concrete transaction or program error. |
| `references/ecosystem.md` | Selecting RPCs, using an explorer, or reviewing wallet-security practices. |
| `references/sources.md` | Verifying current protocol or RPC behavior against Solana primary documentation. |
