# MATIC → POL migration

Official migration is **1:1**. POL is the native gas and staking token on Polygon Chain.

## Where the tokens live

| Location | Action |
|----------|--------|
| **Polygon Chain (PoS)** | Automatic 1:1 conversion to native POL. No Portal migrate click required. Update wallet currency symbol to `POL` if the UI still shows `MATIC`. |
| **Ethereum** | Manual upgrade via [Portal POL upgrade](https://portal.polygon.technology/pol-upgrade): switch wallet to Ethereum → approve → confirm migration tx → receive POL. |
| **Stakers / delegators** | Docs state stakers and delegators do **not** need a separate migrate action for the stake path; follow current Portal/staking UI if a tool still shows MATIC labels. |
| **Legacy Polygon zkEVM balances** | Bridge MATIC out to Ethereum via Portal, then run the Ethereum migration steps. Do not treat zkEVM as the long-term home for new funds. |

## Wallet symbol still says MATIC

On MetaMask (docs walkthrough): Expand view → Settings → Networks → Polygon Mainnet → set **Currency symbol** to `POL` → Save. Other wallets differ; change the network native symbol, not an ERC-20 watch-asset entry, when the balance is native gas.

## What not to claim

- Do not invent a deadline that "burns" unmigrated MATIC without a cited governance/source update.
- Do not tell users to send MATIC to a random burn address.
- Do not equate ERC-20 MATIC on Ethereum with native POL on Polygon Chain until migration/bridge completes.
- Re-open `https://docs.polygon.technology/pos/concepts/tokens/matic-to-pol` and the POL token page before restating emission or governance numbers.
