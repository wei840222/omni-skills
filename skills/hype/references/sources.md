# Research sources (Gate 6)

Retrieved 2026-10-03 during repair of Jules session `14121828639315505087`. Prefer re-fetching `.md` docs before asserting live numeric tiers.

## Onboarding / deposits / withdrawals

- **How to start trading** — email vs DeFi wallet routes; USDC on Arbitrum/Ethereum/Base/Polygon for email deposits; Unit-protocol spot assets; CCTP; Arbitrum as common intermediate; withdraw UI.
  https://hyperliquid.gitbook.io/hyperliquid-docs/onboarding/how-to-start-trading.md
  Local snapshot SHA256: `11f3c200e4d50edbca9c2961128460b4be8f168064b4a6bb4db26829c2889bda`

## Margin and leverage

- **Margining** — cross vs isolated vs strict isolated; initial margin formula; transfer margin floor (max initial, 10% notional); maintenance = half initial at max leverage.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining.md
  Local snapshot SHA256: `95891a47102caca3171f406873178efc0d456ecda5636ed89fd5dc797f6c90a7`
- **Margin tiers** — per-asset max leverage tiers (e.g. BTC 40x/20x, ETH 25x/15x); maintenance rate = half initial at tier max leverage.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margin-tiers.md
  Local snapshot SHA256: `f6e6f5ec37b26359e128983b9c94bc3ab4b1736b471da9234620834f6546bbaf`

## Liquidations and ADL

- **Liquidations** — book-first liquidation; partial 20% above 100k USDC with 30s cooldown; backstop below 2/3 maintenance via liquidator vault; mark price.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations.md
  Local snapshot SHA256: `162afe17f94665546d4e4169591368921a06a94d3f7f48c8fbec6b1ee9394a57`
- **Auto-deleveraging** — underwater account closed against profitable opposite side; no socialization onto flat users.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/auto-deleveraging.md
  Local snapshot SHA256: `a064a9f32008f244e263687d7972efd5512d5c992714439dcd650ac739a27e27`

## Funding

- **Funding** — hourly payment; 8h formula components; premium vs oracle; peer-to-peer.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding.md
  Local snapshot SHA256: `126d1a0489517bad351787542d555a0de25339c69fd544a0d8d283ae172d234c`

## Fees and fee destinations

- **Fees** — volume tiers; staking fee discounts; maker rebates; fees to HLP, assistance fund (burn HYPE), deployers.
  https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees.md
  Local snapshot SHA256: `75e55504b1b887a89e1668a9544d09b013242747bcc29f8648a5410142a71258`

## Staking

- **Staking (HyperCore)** — spot↔staking transfers; 7-day unstake queue; 1-day delegation lock; validator self-delegation; rewards.
  https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking.md
  Local snapshot SHA256: `d773e914f7bdd609845356dca3b2cb63e3be7cc81ffa09cae569068fe23b1bef`

## Index

- **Docs llms.txt index** — discovery of canonical paths.
  https://hyperliquid.gitbook.io/hyperliquid-docs/llms.txt

## Obsolete claims corrected

| Old claim | Correction | Source |
|---|---|---|
| Deposits only via Arbitrum; no Ethereum/mainnet deposits | Route-dependent; email USDC accepts Arbitrum/Ethereum/Base/Polygon; other Unit assets supported | how-to-start-trading |
| Partial liquidations always happen first | Conditional on >100k USDC (10k testnet); else full book liquidation; backstop at <2/3 MM | liquidations |
| Global up to 50x leverage | Per-asset tiered max (BTC 40x tier-0 example; many alts lower) | margin-tiers / margining |
| Trading fees partially go to HYPE stakers as revenue share | Fees → HLP, assistance fund burn, deployers; stakers get fee **discounts** + separate staking rewards | fees / staking |
| Cancellations are instant (absolute) | Softened to observed/API-specific; no unverifiable guarantee | execution notes |
