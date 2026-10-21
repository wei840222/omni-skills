---
name: hype
description: >
  Assist with Hyperliquid perpetuals, deposits, withdrawals, cross/isolated margin,
  liquidations, funding rates, HLP vaults, and HYPE staking. Trigger when the user
  asks about Hyperliquid onboarding, margin modes, liquidation risk, vault deposits,
  or HYPE delegation. Out of scope: unrelated CEX APIs (binance) and generic portfolio
  allocation (invest).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🟢"}'
  related-skills: '{"binance":"Binance Spot REST/WebSocket and CEX account flows instead of Hyperliquid L1 perps.","ethereum":"Ethereum gas, approvals, and L2 bridges when the path is EVM deposit plumbing rather than Hyperliquid trading.","bitcoin":"Bitcoin UTXO and fee recovery when Unit BTC deposit paths need chain-native diagnosis.","aave":"Aave lending Health Factor risk rather than Hyperliquid perp liquidations.","invest":"General portfolio education after Hyperliquid mechanics are settled.","crypto-tools":"Market data and multi-venue tooling once Hyperliquid-specific account rules are clear."}'
---

This skill is stateless knowledge guidance. It does not store local configuration or persistent user state. The wallet owner retains signing and fund control.

## Safety posture

- Treat every rate, max leverage, deposit route, and fee tier as time-sensitive; verify against current official docs or the live app/API before irreversible actions.
- Prefer read-only diagnosis first. For deposits, withdrawals, orders, approvals, vault transfers, or staking moves, state the exact action and wait for explicit user authorization before guiding a signed step.
- Prefer official URLs and the app deposit UI over third-party bridges or unsolicited wallet connections.

## Workflow

1. Identify the user goal: onboard/deposit, withdraw, open or size a perp, diagnose margin/liquidation, funding, HLP vault, or HYPE staking/governance.
2. Confirm account route (email login vs DeFi wallet), margin mode (cross vs isolated), asset, and whether the question is mainnet or testnet.
3. Load only the matching reference section (tracer bullets for the asked mechanic), then answer with current official constraints and recovery steps.
4. For any fund movement or position change, restate the action, required network/asset, and risk boundary; proceed only after the user confirms.

## Load references

| Reference | Load when |
|---|---|
| `references/trading-features.md` | Deposits/withdrawals, margin, leverage tiers, liquidations, funding, order notes, HLP, HYPE staking, common failures, or security checks. |
| `references/sources.md` | Need primary-source URLs, claim freshness notes, or research provenance for PR/review. |

## Route adjacent asks

- Binance Spot API keys / signed REST → `binance`
- ETH gas or ERC-20 approve debugging without Hyperliquid deposit context → `ethereum`
- Portfolio allocation education without Hyperliquid mechanics → `invest`
- Aave Health Factor / supply-borrow → `aave`

## Quick checks

- **Deposit path depends on login route.** Email onboarding can accept USDC on Arbitrum/Ethereum/Base/Polygon and several Unit-protocol spot assets; DeFi-wallet USDC deposit commonly starts from Arbitrum. State the verified networks for the active login method rather than a single-chain default.
- **Max leverage is per asset and tier**, not a global 50x. BTC can reach 40x in the lowest tier; other assets are lower.
- **Liquidation** first sends book market orders; positions above the partial-liquidation notional threshold may liquidate 20% first with a short cooldown; backstop liquidation via the liquidator vault applies if equity falls below 2/3 maintenance margin.
- **Fees** go to HLP, the assistance fund (burns HYPE), and deployers. Staking HYPE unlocks **fee discounts** by tier plus separate staking rewards from emissions—distinct from a trading-fee revenue share.
- **Funding** is peer-to-peer and paid hourly.
