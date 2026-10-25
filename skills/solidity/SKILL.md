---
name: solidity
description: >
  Avoid common Solidity pitfalls—reentrancy, ether-send patterns, overflow/
  unchecked math, upgradeable storage collisions, and tx.origin auth mistakes.
  Use when writing or reviewing Solidity contracts, choosing Checks-Effects-
  Interactions vs ReentrancyGuard, or explaining proxy/EIP-1967 layout. Prefer
  `ethereum` for L1 gas/approvals/MEV, `blockchain` for viem interaction and
  ledger-fit decisions, and `arbitrum` for L2 ops.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⟠"}'
---

This skill is stateless and does not store local configuration or persistent user state.

## When to use

Load this skill for Solidity **language and contract-authoring** pitfalls: reentrancy, ether handling, integer/unchecked math, visibility, storage vs memory, upgradeable proxies, and common compiler/EVM footguns.

Hand off when the ask is mainly:

- L1 fees, approvals, MEV, or generic bridging → `ethereum`
- Architecture fit or viem read/write workflows → `blockchain`
- Arbitrum deposits/exits or chain parameters → `arbitrum`
- Generic secure-code review outside Solidity → `security-best-practices`

## Workflow

1. Identify the failure mode (reentrancy, send/transfer vs call, overflow/unchecked, auth with `tx.origin`, upgrade storage, loop gas, randomness).
2. Prefer the official Solidity Security Considerations wording; load only the matching reference below.
3. Give a minimal safe pattern (Checks-Effects-Interactions, withdraw pattern, `msg.sender` auth, append-only upgrade storage) before optional library helpers such as OpenZeppelin `ReentrancyGuard`.
4. Do not invent gas costs, stipend values, or hard-fork behavior from memory—re-check `references/sources.md` when precision matters.

## Load the relevant reference

| Reference | Load when |
|---|---|
| `references/security-pitfalls.md` | Reentrancy, ether send/receive, loops/gas, `tx.origin`, overflow/unchecked, visibility, storage/memory, upgradeable proxies. |
| `references/sources.md` | Verifying any numeric, hard-fork, EIP, or library claim before giving irreversible advice. |

## Critical rules

- Treat every external call and Ether transfer as handing control to the callee; finish Checks → Effects before Interactions.
- Prefer a withdraw pattern over push-payments when recipients can revert or reenter.
- Authorize with `msg.sender`, never `tx.origin`.
- Solidity 0.8+ checked arithmetic still reverts on overflow; `unchecked {}` opts into wrapping—do not treat checked mode as a substitute for input bounds.
- On upgradeable contracts: no constructor side effects (use `initializer`), keep implementation storage append-only / EIP-1967-aware, and do not rely on `selfdestruct` of an implementation.
- Everything on-chain is observable; `private` is not confidentiality, and block data is a weak randomness source.
