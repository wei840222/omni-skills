# Networks, RPC, and POL gas

Retrieval window: **2026-10-11**. Re-check `references/sources.md` before quoting live RPC hosts or faucet URLs.

## Polygon Chain mainnet

| Field | Value |
|-------|-------|
| Network name | Polygon (Polygon Chain / PoS) |
| Parent chain | Ethereum |
| Chain ID | `137` |
| Gas token | **POL** |
| Public RPC examples | `https://polygon-rpc.com`, `https://polygon.drpc.org` |
| Block explorer | `https://polygonscan.com/` |
| Gas station | `https://gasstation.polygon.technology/pos` |

Official docs also list additional public RPCs (Tenderly, Allnodes, 1RPC, QuickNode, OnFinality, …). Prefer a maintained provider when public endpoints rate-limit.

## Amoy testnet

| Field | Value |
|-------|-------|
| Network name | Amoy |
| Parent chain | Sepolia |
| Chain ID | `80002` |
| Gas token | POL |
| Public RPC example | `https://polygon-amoy.drpc.org` |
| Block explorer | `https://amoy.polygonscan.com/` |
| Gas station | `https://gasstation.polygon.technology/amoy` |
| Faucet | `https://faucet.polygon.technology/` |

Mumbai is retired; do not give Mumbai chain IDs for new setups.

## Add network to MetaMask

Official order of preference (docs):

1. **ChainList** — `https://chainlist.org/chain/137` (mainnet) or `https://chainlist.org/chain/80002` (Amoy) → Add to MetaMask → Approve → Switch network.
2. **Polygonscan** — open the explorer for the target network and use the page footer "Add … Network" control.
3. **Manual entry** — Network name, RPC URL, chain ID `137` or `80002`, currency symbol **POL**, explorer URL from the tables above.

After MATIC→POL, wallets may still display currency symbol `MATIC`. Update the network **Currency symbol** to `POL` in wallet settings (MetaMask: Settings → Networks → Polygon Mainnet).

## POL as gas

- POL is the native gas and staking token on Polygon Chain (PIP-17/19 lineage; 1:1 with historical MATIC supply at migration).
- On Polygon Chain, former native MATIC balances were auto-converted to POL; Ethereum-held MATIC needs a manual Portal upgrade (see `migration.md`).
- "Insufficient MATIC for gas" after migration usually means the wallet still labels POL as MATIC, or the account truly has zero native POL.
- Do not quote live gwei or USD fee levels; use Gas Station / explorer estimates at send time.
- Failed or replaced transactions still consume gas when included.

## Critical confusion traps

- **Same hex address on Ethereum and Polygon does not share balances.** Always confirm the active network before sending.
- **Bridged / wrapped ETH on Polygon is not native ETH on Ethereum** and is not PoS gas.
- **Polygon Chain ≠ deprecated Polygon zkEVM** — different chain IDs, explorers, and gas models; see `zkevm.md`.
- EVM tooling (Foundry, Hardhat, Remix, ethers, web3) works when pointed at the correct RPC and chain ID; no Solidity dialect change is required for ordinary contracts.
