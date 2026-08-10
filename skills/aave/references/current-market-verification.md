# Current Aave Market Verification

Load this reference when a request needs a current Aave market, position, contract-address, GHO, E-Mode, liquidation, permit, or Umbrella fact. It records the live facts to resolve from official sources; use a market name or interface screenshot as a discovery input, then resolve the exact deployment.

**Verified:** 2026-08-08. Aave deployment, governance, liquidity, rate, and risk settings can change after this date.

## Claim inventory and treatment

| Claim or question | Freshness | Resolve it from | Apply it this way |
| --- | --- | --- | --- |
| Market, reserve, user position, availability, caps, pause/freeze state, and E-Mode membership | Platform-specific | Aave Markets data and operations docs [16][7] | Identify `chainId`, market address, reserve, and user before interpreting displayed data. Retrieve user-specific fields with the user address. |
| Contract address and deployment version | Platform-specific | Aave Address Book API [19][20] | Read the current manifest for the selected chain and product, then pin a versioned module for reproducible analysis. |
| Health Factor (HF) | Stable protocol concept; version-specific implementation | Aave liquidation help and current `GenericLogic.sol` [13][21] | Aave describes HF as total collateral value times weighted average liquidation threshold divided by total borrow value. Recalculate from current market data; prices, debt accrual, collateral flags, E-Mode, and risk parameters all affect it. |
| Liquidation eligibility and amount | Platform- and version-specific | Aave liquidation help and `LiquidationLogic.sol` [13][22] | `HF < 1` makes a position eligible. Resolve the market-specific close-factor, incentive, dust, and grace-period conditions. |
| Borrow-rate mode | Version-sensitive | Current V3 Pool documentation [3] | For V3, use the documented variable mode (`2`) for `borrow` and `repay`. Identify a different protocol version and its source before naming an alternate mode. |
| E-Mode | Platform-specific | Aave E-Mode help [4] | Inspect the selected category: it supplies its own LTV, liquidation threshold, bonus, permitted assets, and may have liquid-category membership. |
| GHO | Platform-specific | Aave GHO documentation and `gho-origin` [5][12] | In the Aave V3 Ethereum Pool, a facilitator mints GHO for the position. Verify collateralization and the facilitator's live capacity, rate, and discount configuration. |
| AAVE protocol-risk staking | Platform-specific | Aave Umbrella documentation and source repository [6][18] | Umbrella is replacing the legacy Safety Module. Treat coverage, reward, cooldown, and slashing terms as asset- and network-specific configuration. |
| Permit signature | Standard- and token-specific | EIP-2612 and Aave market operations [17][7] | Choose a permit flow when the selected token and execution plan support it; read its exact spender, amount, deadline, chain, and verifying contract. |

## Live review sequence

1. Resolve the user's chain, Aave market address, protocol version, wallet address (when supplied), and exact token contracts.
2. Retrieve the market and user state. Confirm reserve pause/freeze state, user supply and borrow eligibility, collateral status, available liquidity, caps, rates, E-Mode, and HF before drawing a conclusion.[16][7]
3. For addresses, use the Aave Address Book manifest. Use a versioned release for repeatable analysis; the `latest` manifest supports live discovery.[19][20]
4. For a proposed supply, borrow, repay, withdrawal, collateral toggle, or liquidation, model its user-specific effect. A withdrawal is limited by both available liquidity and the HF remaining after the withdrawal.[3][7]
5. Describe the transaction plan and its assumptions. Let the wallet owner examine and authorize the actual signature or transaction.

## Source synthesis and reconciliation

- The liquidation help page and `GenericLogic.sol` agree that HF uses collateral value, weighted liquidation thresholds, and debt value; both identify `HF < 1` as liquidation eligibility.[13][21]
- The broad Pool page says its close factor is `0.5`, while the current `LiquidationLogic.sol` and liquidation help page describe conditions that permit partial or full liquidation. Use the detailed help page and current logic for V3 analysis; value-free wording in `SKILL.md` keeps a future release accurately represented.[3][13][22]
- The GHO documentation and the official `gho-origin` repository agree on the facilitator-and-cap model. The documentation adds the Aave V3 Ethereum Pool context and current cross-chain mechanism, while the repository is the contract source of record.[5][12]
- The Umbrella documentation and official source both describe a stake-token system that covers deficits through slashing. The documentation establishes the current transition from the legacy Safety Module; the repository supplies implementation detail.[6][18]

## Official source guide

### Market discovery, live status, and addresses

- [16] Aave Market Data — market/reserve/user fields, including pause, freeze, caps, available liquidity, and E-Mode data.
- [7] Aave Market Operations — user-specific eligibility checks, operation plans, permit capability, and HF previews.
- [19] Aave Address Book API — current manifest and immutable versioned address-book releases.
- [20] Current Address Book Manifest — live discovery pointer for distinct V3 and V4 modules.

### Health Factor, liquidations, and V3 mechanics

- [13] Health Factor & Liquidations — HF formula, liquidation threshold, and current partial/full-liquidation rules.
- [3] Aave V3 Pool — supported Pool operations, variable-rate mode, collateral operations, and simplified liquidation interface information.
- [21] Aave V3 `GenericLogic.sol` — HF calculation inputs and oracle-priced user account data.
- [22] Aave V3 `LiquidationLogic.sol` — close-factor, collateral, incentive, and dust logic.

### E-Mode, GHO, and protocol-risk staking

- [4] Efficiency Mode (E-Mode) — category-specific risk values, asset permissions, and liquid E-Mode membership.
- [5] GHO — facilitator caps, V3 Ethereum minting, repayment, and official CCIP-based cross-chain context.
- [12] `gho-origin` — official GHO contract source and facilitator model.
- [6] Umbrella — current replacement of the legacy Safety Module, asset/network isolation, slashing, and cooldown behaviour.
- [18] `aave-umbrella` — official Umbrella contract source.

### Permit security

- [17] ERC-2612 — permit domain, spender, amount, nonce, deadline, and replay-protection semantics.

## Sources

[3] https://aave.com/docs/developers/smart-contracts/pool
[4] https://aave.com/help/borrowing/e-mode
[5] https://aave.com/docs/ecosystem/gho
[6] https://aave.com/docs/aave-v3/umbrella
[7] https://aave.com/docs/aave-v3/markets/operations
[12] https://github.com/aave-dao/gho-origin
[13] https://aave.com/help/borrowing/liquidations
[16] https://aave.com/docs/aave-v3/markets/data
[17] https://eips.ethereum.org/EIPS/eip-2612
[18] https://github.com/aave-dao/aave-umbrella
[19] https://github.com/aave-dao/aave-address-book
[20] https://assets.aave.com/address-book/releases/latest/manifest.json
[21] https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/logic/GenericLogic.sol
[22] https://github.com/aave-dao/aave-v3-origin/blob/main/src/contracts/protocol/libraries/logic/LiquidationLogic.sol
