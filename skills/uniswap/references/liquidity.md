## Liquidity Provision
- Impermanent loss is real and permanent when you withdraw — LPs lose vs just holding when prices diverge
- V3 concentrated liquidity amplifies both gains and losses — narrow range means more fees but higher IL risk
- Out-of-range positions earn zero fees — price moves outside your range, you hold 100% of the depreciating asset
- V2 is simpler: full range, less management, but less capital efficient — consider for volatile pairs you want to forget

## V3 Position Management
- Narrower range = more fees per dollar but more rebalancing — only worth it if you actively manage
- Gas costs to adjust positions add up — each add/remove liquidity is a transaction
- "Collect fees" is separate from "remove liquidity" — uncollected fees stay in the position
- NFT represents your V3 position — losing the NFT means losing access to the liquidity
