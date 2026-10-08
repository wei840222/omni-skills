---
name: stellar
description: >
  Handle Stellar (XLM) operations: memo requirements for exchange deposits,
  account base reserves and trustlines, path payments, SDEX order books and
  protocol AMMs/liquidity pools, anchors/USDC corridors, and Soroban contract
  basics. Use when sending or receiving XLM or issued assets, diagnosing
  missing-memo or reserve errors, validating trustlines, routing cross-border
  payments, or deploying/debugging Soroban contracts on Stellar. Not for
  Ethereum/EVM chains (`ethereum`), Bitcoin UTXO flows (`bitcoin`), or generic
  multi-chain portfolio tracking without a Stellar network question.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚀"}'
  related-skills: '{"aave":"EVM lending markets when the question leaves Stellar.","bitcoin":"Bitcoin UTXO and L1 flows outside Stellar.","ethereum":"EVM account model, gas, and contracts outside Stellar.","payments":"Generic payment rails when the network is not Stellar-specific."}'
---

# Stellar (XLM)

Stateless domain skill for **Stellar network payments, reserves, trustlines, SDEX/AMM liquidity, anchors, and Soroban basics**. It does not store keys, account credentials, or transaction history in the package.

## Core instructions

When working with the Stellar network, load `references/stellar-details.md` and verify:

1. **Memo fields** — exchange deposits require the exact memo the venue provides; omitting it can permanently lose funds.
2. **Account minimums** — an account needs two base reserves (currently 1 XLM) to exist; each ordinary trustline adds one base reserve (0.5 XLM); pool-share trustlines add two.
3. **Trustlines** — non-XLM assets need an established trustline before receive (claimable balances are the exception path).
4. **DEX liquidity** — SDEX supports classic order books **and** protocol liquidity pools (constant-product AMMs).

## When to load

- send/receive XLM or issued assets; exchange deposit with memo/ID/hash
- "destination account does not exist", insufficient reserve, or unestablished trustline
- path payments, cross-border/remittance corridors, anchors, native USDC
- SDEX offers vs liquidity-pool swaps; pool-share reserves
- Soroban (Rust smart contracts) orientation on Stellar mainnet

## Routing

| Need | Load |
| --- | --- |
| Memos, reserves, trustlines, addresses, fees, common errors | `references/stellar-details.md` |
| DEX order book + AMM/liquidity pools, path payments | `references/stellar-details.md` (DEX and Cross-Border sections) |
| Soroban contract platform notes | `references/stellar-details.md` (Soroban section) |
