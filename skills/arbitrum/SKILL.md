---
name: arbitrum
description: >
  Operate Arbitrum One and Nova: official bridging and ~7-day exits, ETH gas vs ARB
  governance, chain IDs/RPCs, Stylus status, sequencer force-inclusion, and BoLD
  dispute context. Use for Arbitrum deposits, withdrawals, wallet setup, L2 gas,
  or One-vs-Nova confusion. Not for general Ethereum L1 fee markets alone
  (`ethereum`), multi-chain architecture choice (`blockchain`), or Solidity authoring
  (`solidity`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔵"}'
  related-skills: '{"blockchain":"Broader ledger and EVM interaction decisions when the problem is not Arbitrum-specific.","ethereum":"L1 gas, approvals, MEV, and cross-L2 bridge framing once Arbitrum-specific steps are clear.","solidity":"Contract authoring and audit patterns when the task moves from chain ops into Solidity code."}'
---

This skill is stateless and does not store local configuration or persistent user state.

# Arbitrum

Arbitrum-specific guidance for **Arbitrum One** (Optimistic Rollup) and **Arbitrum Nova** (AnyTrust): bridging, gas token rules, network parameters, Stylus, sequencer behavior, and dispute-window exits secured on Ethereum.

## When to load

Load this skill when the request is **Arbitrum-specific**, for example:

- depositing or withdrawing via the official bridge (`bridge.arbitrum.io`)
- clarifying ETH (gas) vs ARB (governance)
- adding One (`42161`) or Nova (`42170`) to a wallet
- explaining the native exit delay, claim step, or third-party fast bridges
- Stylus contract status, sequencer downtime, or force-inclusion

Prefer sibling skills when the problem is already broader: `ethereum` for L1 fee markets and generic L2 framing, `blockchain` for fit/architecture, `solidity` for writing contracts.

## Quick workflow

1. **Name the chain** — Arbitrum One vs Nova vs Sepolia; confirm chain ID before any send or bridge.
2. **Name the direction** — parent→child deposit vs child→parent withdrawal vs same-chain tx.
3. **Load one reference** — bridging, networks, technical, or sources; do not load all by default.
4. **Verify before irreversible steps** — explorer/RPC, official bridge UI history, and enough **ETH** for gas on the destination.
5. **Separate soft vs hard finality** — sequencer inclusion is fast; native L2→L1 finality waits out the dispute window, then a claim on L1.

## Load the relevant reference

| Reference | Load when |
|---|---|
| `references/bridging.md` | Deposits, native withdrawals, claim step, third-party fast exits, stuck bridge txs. |
| `references/networks.md` | Chain IDs, RPCs, explorers, One vs Nova (Rollup vs AnyTrust), gas token, ARB role. |
| `references/technical.md` | Fees (L2 + L1 data), Stylus status, sequencer/force-inclusion, BoLD dispute window, common failures. |
| `references/sources.md` | Re-check time-sensitive protocol claims against primary docs. |

## Non-negotiable operating rules

- Treat **ETH** as the gas token on Arbitrum One and Nova; **ARB** is governance, not gas.
- Treat official bridge **child→parent** exits as a multi-day dispute window (docs and UI describe about **seven days**; chain params list ~**6.4 days** / 45818 blocks on One/Nova), then an L1 **claim**—not a stuck transfer.
- Prefer the **official bridge** for large value; third-party bridges trade speed for extra smart-contract and liquidity risk.
- Never mix **One** and **Nova** chain IDs, RPCs, or bridges in the same instruction.
- For new **Stylus** work, confirm current activation policy on One/Nova before telling users to deploy (activations have been paused by Security Council notice while existing activated contracts can keep running until expiry).
