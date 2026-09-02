---
name: sui-network
description: Diagnose Sui transactions, object ownership, staking, and Move smart-contract questions. Use when handling SUI coins, object IDs, gas, validators, programmable transactions, or Sui wallet safety.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"💧","os":["linux","darwin","win32"]}'
---

This skill is stateless and does not store local configuration or persistent user state.

## Workflow

1. Identify the network, wallet role, object or transaction digest, package ID, and the intended operation or exact error.
2. Load `references/sui-network.md` for the domain model and operational guidance.
3. Use current RPC results, wallet simulation, and official Sui documentation as the source of truth for a transaction decision.
4. Verify the resulting digest and expected object state before reporting completion.

## Load the relevant reference

| Reference | Load when |
| --- | --- |
| `references/sui-network.md` | Handling SUI coins, object ownership, transactions, staking, Move, DeFi, NFTs, bridges, or wallet safety. |
| `references/sources.md` | Verifying a time-sensitive protocol value, network behavior, package interface, or security requirement against primary documentation. |
