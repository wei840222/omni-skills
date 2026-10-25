---
name: bnb
description: "Assist with BNB Chain transactions, BEP-20 token transfers, wallet/RPC setup, and DeFi tasks on PancakeSwap or similar apps. Use when handling BNB gas fees, bridging assets, verifying contracts on bscscan, or managing BEP-20 tokens."
metadata:
  openclaw: '{"emoji": "🔶"}'
---

## When to load

Load this skill for BNB Chain (formerly BSC) network setup, BNB gas, BEP-20 transfers, cross-chain bridging caveats, PancakeSwap/DeFi interactions, staking basics, and scam/contract verification on bscscan.

## Critical Safety Rule

- Verify all BEP-20 contract addresses on `https://bscscan.com` and confirm the target network before any transfer or approval to prevent irreversible loss of funds.
- BNB Chain and Ethereum share `0x` address format but are different networks; never treat a same-looking address as a same-chain destination.

## Progressive disclosure

- **When to load `references/network-and-tokens.md`**: BNB Chain identity, BEP-20 behavior, gas rules, and cross-chain bridging.
- **When to load `references/ecosystem-and-security.md`**: PancakeSwap/Venus DeFi, wallet RPC/Chain ID setup, staking, common issues, and scam patterns.
