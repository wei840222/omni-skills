---
name: bnb
description: >
  Assist with BNB Chain transactions, BEP-20 token transfers, wallet/RPC setup,
  and DeFi tasks on PancakeSwap or similar apps. Load when handling BNB gas fees,
  bridging assets, verifying contracts on bscscan, or managing BEP-20 tokens.
metadata:
  openclaw: '{"emoji": "🔶"}'
  related-skills: '{"ethereum":"Handle Ethereum/L2 gas, approvals, and bridges instead of BNB Chain BEP-20 flows.","blockchain":"Cover general ledger and EVM fundamentals beyond BNB-specific network and token mechanics.","crypto-tools":"Fetch market data and exchange tooling once BNB Chain transaction mechanics are settled.","binance":"Handle Binance exchange account/API workflows rather than on-chain BNB Chain operations.","aave":"Analyze multi-chain Aave positions when the request leaves BNB-native DeFi mechanics."}'
---

## When to load

Load this skill for BNB Chain (formerly BSC) network setup, BNB gas, BEP-20 transfers, cross-chain bridging caveats, PancakeSwap/DeFi interactions, staking basics, and scam/contract verification on bscscan.

## Critical Safety Rule

- Verify all BEP-20 contract addresses on `https://bscscan.com` and confirm the target network before any transfer or approval to prevent irreversible loss of funds.
- BNB Chain and Ethereum share `0x` address format but are different networks; never treat a same-looking address as a same-chain destination.

## Progressive disclosure

- **When to load `references/network-and-tokens.md`**: BNB Chain identity, BEP-20 behavior, gas rules, and cross-chain bridging.
- **When to load `references/ecosystem-and-security.md`**: PancakeSwap/Venus DeFi, wallet RPC/Chain ID setup, staking, common issues, and scam patterns.
