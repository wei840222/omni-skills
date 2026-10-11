# Troubleshooting and security

## Common failures

| Symptom | Likely cause | First checks |
|---------|--------------|--------------|
| Insufficient MATIC/POL for gas | No native POL, or symbol still labeled MATIC | Confirm chain ID 137/80002; check native balance on polygonscan; migrate/bridge POL |
| Tx stuck pending | Fee too low or RPC lag | Compare Gas Station suggestion; speed up/cancel in wallet; try another RPC |
| Tokens missing after bridge | Wrong network view, missing token contract, or bridge not finished | Confirm Portal status; add token contract on the **destination** chain; wait for mint/claim |
| "Network not supported" in dApp | dApp allowlist | Switch to Polygon Chain 137; if dApp only lists deprecated zkEVM, prefer another venue or contact the dApp |
| Sent to "same address" but empty | Funds on the other chain | Explorer on both Ethereum and Polygon; never re-send hoping it merges |
| Withdraw "done" on L2 but no L1 funds | Exit/claim not completed | Complete Portal claim on Ethereum after checkpoint |
| Wallet shows MATIC after upgrade | Display symbol only | Update network currency symbol to POL |

## Security checklist

- Private key / seed controls every EVM network for that address—phishing on one chain drains all.
- Review and revoke stale ERC-20 approvals (explorer token approval tools); prefer exact allowances over unlimited when teaching users.
- Verify contract addresses from official docs or reputable explorers—ticker collisions are common.
- Prefer Portal for official bridge trust assumptions; third-party bridges need explicit risk acceptance.
- Keep a POL dust reserve so tokens are not stranded without gas.
- Never request seed phrases, private keys, or "support recovery" forms in chat.

## Recovery order for stuck value

1. Identify **exact network** (chain ID) and **tx hash**.
2. Open the matching explorer and Portal status—not a random support DM.
3. If bridge-in incomplete: wait/sync; do not double-bridge.
4. If bridge-out burned but unclaimed: perform L1 exit/claim with ETH for gas.
5. If wrong-network external transfer to an exchange deposit: contact the venue with tx hash; success is not guaranteed.
