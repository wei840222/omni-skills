# Avalanche Primary Network architecture

## Three built-in chains

Avalanche's Primary Network exposes three chains that share AVAX but serve different jobs:

| Chain | Role | Typical tools |
| --- | --- | --- |
| **C-Chain** (Contract Chain) | EVM execution for most DeFi, tokens, and smart contracts | MetaMask, Core, EVM RPCs, Snowtrace / Avalanche Explorer |
| **X-Chain** | UTXO-style asset transfers and exchange-oriented flows | Core / Avalanche wallet surfaces that speak X-Chain |
| **P-Chain** | Platform operations: validators, staking, subnet/L1 metadata | Core / Avalanche wallet; not MetaMask |

Same seed can control addresses on all three chains, but balances do **not** auto-move. An asset sitting on X or P is invisible to a C-Chain-only wallet until it is exported/imported correctly.

## Avalanche L1s (historical "subnets")

Custom blockchains validated by a subset of Primary Network validators are commonly called Avalanche L1s (older docs say subnets). Each L1 can define its own VM, gas token, and bridging path. Do not assume AVAX gas or C-Chain tooling works unchanged on an L1; confirm the L1's own network parameters and official bridge.

## Safety defaults

- Name the source chain, destination chain, and asset before any transfer advice.
- One private key can unlock C/X/P; protect the seed as a multi-chain credential.
- Prefer official docs and Core for multi-chain operations over third-party "bridge everything" UIs when the user only needs Primary Network atomic transfers.
