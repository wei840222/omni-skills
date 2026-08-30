---
name: uniswap
description: Execute swaps, provide liquidity, and assess risks on Uniswap. Use when the user requests token swaps, Uniswap V3 position management, or evaluates DeFi execution safety and MEV protection.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🦄"}'
  related-skills: '{"crypto-tools": "Use for broader crypto management beyond trading on Uniswap.", "ethereum": "Provides deep context for Ethereum transactions and token standard specifics."}'
---

## State location

This skill is stateless and does not store local configuration or persistent user state.

## Core Workflows

Load the corresponding reference file immediately when a task matches its trigger condition:

| Reference File | When to load |
|---|---|
| `references/swap-execution.md` | When executing a swap, configuring slippage, optimizing gas, handling failed swaps, or using limit orders/UniswapX. |
| `references/security.md` | When evaluating risks, handling token approvals, protecting against MEV/frontrunning, verifying tokens, or checking safety before a large swap. |
| `references/liquidity.md` | When adding/removing liquidity, managing Uniswap V3 positions, or evaluating impermanent loss. |
