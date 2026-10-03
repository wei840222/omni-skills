# Common Avalanche failures

| Symptom | Likely cause | Recovery direction |
| --- | --- | --- |
| "Insufficient funds" while token balances look large | C-Chain gas must be **AVAX**; tokens cannot pay gas | Keep a AVAX gas buffer on C-Chain |
| Balance missing after bridge | Wrong destination chain, wrapped token, or incomplete import | Switch wallet network; check bridge status; verify token contract |
| MetaMask cannot move to X/P or stake | Wallet is C-Chain-only | Use Core / Avalanche wallet for X-Chain, P-Chain, validators |
| Tokens "on Avalanche" but not in MetaMask | Asset on X/P or an L1, or custom token not added | Identify chain first; add correct network/token; complete import if atomic tx pending |
| Slow bridge to Ethereum | Bridge finality / third-party path delay | Track the bridge's status UI; do not re-send blindly |
| Subnet/L1 token not showing | Wallet missing that network | Add the L1 RPC/chain id from official L1 docs |
| Approval / spender risk on C-Chain | Unlimited ERC-20 allowances | Review and revoke via explorer allowance tools after confirming the spender |

## Debug checklist

1. Which chain holds the asset right now?
2. Which wallet software can see that chain?
3. Is the next action a C-Chain EVM tx, an atomic export/import, a P-Chain stake, or an external bridge?
4. What primary doc or explorer evidence confirms the current state?

Refuse to "just retry" a bridge or atomic transfer without identifying whether the first leg already succeeded.
