---
name: aave
description: Use when analyzing or planning an Aave supply, borrow, withdrawal, liquidation, E-Mode, GHO, or market-specific risk position, including a Health Factor question where Aave is implicit.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"👻"}'
---

## State location

Aave is a stateless knowledge skill. Analyze user-provided information and facts read from the intended public market; the wallet owner retains transaction signing and wallet control.

## Operating principle

Treat every market configuration, displayed rate, and position value as time-sensitive. Identify the exact chain, Aave market, supplied and borrowed assets, collateral setting, and user goal before interpreting a position or suggesting a next step.

Load [current-market-verification.md](references/current-market-verification.md) when the request needs a live market, contract address, protocol-version detail, GHO, E-Mode, liquidation, permit, or Umbrella fact.

## Evidence foundation

- **Deployment identity:** resolve a chain ID, market address, and token contract for every position; tickers and interface labels are secondary identifiers.
- **Live position:** gather current collateral flags, debt, and eligibility data; a dashboard starts discovery, while a current position snapshot supports risk characterization.
- **Reproducible addresses:** pin a versioned Aave Address Book release when the analysis needs stable addresses; use its `latest` manifest for live discovery.
- **Authorizations:** check permit support on the selected reserve and execution plan before presenting an approval and operation as one wallet flow.

## Decision gates

- **Known deployment and position:** continue with quantified analysis after resolving the chain ID, market address and version, token addresses, and relevant user position state. When a required input is unavailable, open with the exact evidence request and keep the result qualitative.
- **Position-changing plan:** before comparing a withdrawal, borrow, repay, collateral, swap, or cross-chain option, obtain its current simulation or preview and the reserve status. When a simulation is unavailable, name that analysis boundary and present conditional options.
- **Liquidation exposure:** when the live Health Factor is near or below `1`, organize the response around current position data and modelled repayment, added-collateral, or reduced-exposure paths before discussing a withdrawal or transfer.

## Core concepts

- **Supply:** deposit a supported asset and receive an interest-bearing position token.
- **Collateral:** enable an eligible supplied asset before borrowing against it; eligibility is configured per reserve and market.
- **Borrow:** debt accrues interest under the selected market's current rate model.
- **Health Factor (HF):** the protocol's current measure of liquidation exposure; `HF < 1` signals liquidation eligibility.
- **Market configuration:** loan-to-value, liquidation threshold, liquidation bonus, borrow modes, caps, and available reserves vary by market and may change through governance.

## Position review workflow

1. Identify the network and exact Aave market. Keep bridged and native asset variants distinct.
2. Collect the current `chainId`, market address, supplied assets, collateral-enabled flags, debt assets, HF, reserve state, and user-specific supply/borrow/withdraw eligibility from the intended market.
3. Validate the collected values against the selected market and state which missing input prevents a conclusion.
4. Report the result in this order: scope and evidence, current HF, material price/rate dependencies, withdrawal constraints, liquidation consequence, and user-controlled options with their assumptions.
5. Leave execution to the user's wallet after they review the current transaction details.

## Health Factor and liquidations

- HF changes with collateral and debt values, accrued interest, reserve parameters, and oracle prices.
- A position with `HF < 1` becomes eligible for permissionless liquidation according to the current market's close-factor and liquidation-bonus rules. The outcome can be partial or complete, depending on the version, position, and protocol conditions.
- A liquidation repays eligible debt and transfers collateral under the market's configured incentive; the amount is market- and position-specific.
- For a position near its threshold, use current values and show how each proposed action changes the relevant exposure.

## Supplying and borrowing

- Confirm the reserve is active, unfrozen, and unpaused; check user-specific supply, borrow, and withdrawal eligibility before modeling a borrow or withdrawal.
- A supplied asset can remain non-collateral by choice; clarify that distinction before explaining borrowing capacity.
- Review the current rate data and implementation for the chosen reserve. Rate availability and pricing vary by market and protocol version.
- Model approvals, supply, borrow, repay, withdrawal, and collateral toggles as distinct actions. When a reserve supports a verified permit flow, inspect the permit's spender, amount, deadline, chain, and verifying contract before treating it as a bundled action.

## Market-specific features

- **E-Mode:** use the active market's category membership and risk parameters. An asset can belong to more than one category, and the selected category sets its own asset permissions, LTV, liquidation threshold, and liquidation bonus.
- **GHO:** verify whether the selected market supports GHO, its current facilitator capacity, borrowing configuration, and applicable discount conditions. In the Aave V3 Ethereum Pool, a facilitator mints GHO for the position.
- **AAVE and protocol-risk staking:** distinguish governance-token holdings from protocol positions. Aave currently documents Umbrella as replacing the legacy Safety Module; resolve its asset-, network-, reward-, cooldown-, and slashing-specific terms from current official sources.
- **Cross-market activity:** treat each network and market as separate. GHO's official CCIP transfer path moves the token; analyze the source-market collateral position and debt as separate changes.

## Risk framing

- Set a buffer from the user's own volatility and repayment assumptions, then compare it with the displayed borrowing capacity.
- Explain concentration risk when collateral and debt values move together or when a bridged asset has different liquidity or oracle behavior.
- Treat automated deleveraging, swap, and flash-loan flows as advanced actions: inspect their current permissions, fees, slippage constraints, and failure behavior before use.

## Transaction and gas considerations

- Read the wallet's exact chain, token contract, spender, allowance, transaction simulation, and gas estimate before authorizing an action.
- Distinguish token approvals from supply, borrow, repay, withdrawal, and collateral-setting transactions.
- Use the intended market's interface and current network fees; fee levels and interface capabilities differ across networks.
