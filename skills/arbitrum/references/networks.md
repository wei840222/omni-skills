# Networks, tokens, and wallet setup

## Public chains (mainnet)

| Network | Chain ID | Role | Canonical public RPC (example) | Explorer |
|---|---|---|---|---|
| Arbitrum One | `42161` | Optimistic Rollup (Nitro), settles to Ethereum | `https://arb1.arbitrum.io/rpc` | [arbiscan.io](https://arbiscan.io) |
| Arbitrum Nova | `42170` | AnyTrust (Nitro), lower fees, extra DA trust assumptions | `https://nova.arbitrum.io/rpc` | Nova explorers (e.g. Blockscout / Nova Arbiscan) |
| Arbitrum Sepolia | `421614` | Testnet rollup | `https://sepolia-rollup.arbitrum.io/rpc` | Sepolia explorers per docs |

Official chain tables: [Public chains overview](https://docs.arbitrum.io/build-decentralized-apps/public-chains), [Chain info](https://docs.arbitrum.io/for-devs/dev-tools-and-resources/chain-info). Prefer a maintained provider RPC for production traffic; public endpoints are convenience defaults.

## One vs Nova

- **One**: trust-minimized Optimistic Rollup path; default choice for general DeFi and high-value activity.
- **Nova**: AnyTrust data-availability committee model—cheaper, different trust assumptions; common for gaming/social style workloads.
- Different chain IDs, sequencers, bridges, and balances. An address string can look identical across Ethereum/One/Nova while balances and contracts do not.

## Gas and ARB

- **Gas token on One and Nova: ETH** (native). ERC-20 balances cannot pay gas.
- **ARB**: governance token for Arbitrum DAO voting—not a gas token on One/Nova.
- “I have ARB but cannot deploy” almost always means missing ETH for gas.

## Wallet configuration checklist

1. Add the correct network name, chain ID, RPC, and explorer (MetaMask “Add network” or chainlist-style helpers).
2. Verify chain ID matches the intended network before first send.
3. Keep a separate mental model for Ethereum L1 vs One vs Nova balances.
4. For large transfers, send a dust test, then the full amount.

## Ecosystem pointers (non-exhaustive)

- DeFi and perps venues rotate; verify contract addresses on the explorer for the **same chain ID**.
- TVL and venue rankings change continuously—point users to current dashboards (e.g. L2Beat project pages) instead of hard-coding stale dollar figures.
- Governance and Security Council actions can change operational policy (upgrades, Stylus activation pauses); confirm against live docs when advising deployments.
