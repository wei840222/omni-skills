# Hyperliquid trading features (verified)

Facts below are grounded in official Hyperliquid docs retrieved during this refactor. Prefer live docs or the app when values may have changed.

## Onboarding and deposits

### Account routes

- Users can trade with a normal DeFi wallet or by logging in with email on supported interfaces (including `app.hyperliquid.xyz`).
- DeFi wallet path: connect an EVM wallet → Enable Trading (gas-less signature) → deposit.
- Email path: connect with email code → deposit to the shown address/QR.

### Collateral and deposit methods

Official onboarding distinguishes methods by route:

**Email login deposit window**

- Send USDC on Arbitrum, Ethereum, Base, or Polygon to the deposit address (or QR). Deposit arrives as USDC on HyperCore.
- Also supported: BTC on Bitcoin; ETH/ENA on Ethereum; SOL and listed Solana assets; MON on Monad; XPL on Plasma; AVAX on Avalanche; ZEC on Zcash (spot assets may need conversion to the quote asset used for the market).

**DeFi wallet deposit**

- USDC on Arbitrum is the common USDC path (enter amount → Deposit → confirm in wallet).
- Same Unit-protocol style spot assets as above can be sent to the destination address shown; sell/convert to USDC (or the relevant quote) before trading perps when required.

**Additional funding notes**

- Many CEXs and bridges support Hyperliquid via HyperCore or HyperEVM.
- USDC can move from other chains via CCTP; source chain needs USDC plus native gas. Trading on Hyperliquid itself is gas-free.
- Arbitrum is a common intermediate when a CEX does not support Hyperliquid directly.
- Do **not** state that deposits are exclusively via Arbitrum or that Ethereum/mainnet deposits are categorically impossible. Route, asset, and UI method decide availability.

### Withdrawals

- From the app, use Withdraw and follow the chain/method prompts. Small gas may apply depending on withdrawal chain and method.

## Account and margin model

- **Cross margin (default):** shared collateral across cross positions for capital efficiency. Unrealized PnL can support new cross initial margin.
- **Isolated margin:** collateral constrained to that asset; liquidations do not cascade to other isolated or cross books the same way.
- **Strict isolated:** isolated plus margin cannot be removed; margin leaves proportionally as the position closes.
- HIP-3 / multi-DEX accounts may change how cross margin is shared (unified/portfolio vs standard abstraction). Load official account-abstraction docs when the user has multi-DEX positions.
- Account value includes deposits and unrealized PnL (mark-to-market).

### Leverage and initial margin

- User leverage is any integer from 1 to the asset's **max leverage**.
- Max leverage is **asset- and tier-specific**, not a fixed global 50x.
  - Example mainnet tiers (notional USDC): BTC 40x then 20x above 150M; ETH 25x then 15x above 100M; many alts 10x/5x. Confirm live `meta` / margin tables for the asset in question.
- Initial margin to open ≈ `position_size * mark_price / leverage`.
- Cross initial margin stays reserved; isolated can add/remove margin (except strict isolated).
- Leverage may be increased on an open position; leverage is checked at open. After open, the user monitors usage to avoid liquidation.
- Transferring margin out (withdraw, spot transfer, isolated margin removal) requires remaining margin ≥ max(initial margin required, 10% of total open notional).

## Perpetuals trading basics

- Perps use USDC collateral to long/short without holding the spot asset.
- Position size ≈ leverage × collateral (UI slider/entry).
- Order types commonly include limit, market, and TP/SL family orders; prefer reduce-only when the intent is only to close.
- Prefer mark price for liquidation monitoring; mark blends external CEX prices with book state.

## Funding

- Funding is peer-to-peer; the protocol does not take a cut of funding payments.
- Paid **every hour** (8-hour formula components paid at 1/8 per hour).
- Interest component is aligned with CEX conventions (docs: 0.01% per 8h interest component → 0.00125% per hour toward shorts in the clamp model).
- Premium follows impact prices vs oracle; positive funding → longs pay shorts; negative → shorts pay longs.
- High funding is a carrying-cost signal, not free yield.

## Liquidations

Maintenance margin is half of initial margin at max leverage for the asset (about 1.25%–16.7% depending on 40x–3x max leverage classes).

Process (official order):

1. When account equity < maintenance margin, the engine first tries to close via **market orders on the book** (full size; may fill fully or partially). If maintenance is restored, remaining collateral stays with the trader.
2. **Partial liquidations:** for liquidatable positions larger than **100k USDC** notional (10k on testnet), only **20%** is sent as a market liquidation order. After any partial liquidation in a block, a **30s cooldown** applies; during cooldown, liquidation orders for that user are for the **entire** position.
3. If equity falls below **2/3 of maintenance margin** without successful book liquidation, **backstop liquidation** runs through the liquidator vault (HLP component):
   - Cross backstop: cross positions and cross margin transfer to the liquidator; with no isolated positions, equity can go to zero.
   - Isolated backstop: only that isolated position and margin transfer; cross book untouched.
   - Maintenance margin is not returned on backstop (buffer for liquidator profitability).
4. Liquidations use **mark price**.

Do **not** claim “partial liquidation always happens first.” Partial size reduction is conditional on notional threshold and cooldown rules; small positions liquidate in full via the book path first.

### Auto-deleveraging (ADL)

- If account or isolated value goes negative, opposite-side users are ranked by profitable leverage usage and closed at prior mark against the underwater account so the platform stays solvent.
- Users with no open positions do not socialize platform losses under the documented invariant.

## Order execution notes

- On-chain order book; trading has no gas fee (trading fees still apply).
- Prefer stating cancellation and fill behavior as exchange/API observed facts; avoid absolute “always instant cancel” guarantees without a current API citation for the specific client path.
- REST and WebSocket APIs exist for programmatic trading; respect rate limits. Testnet is available for practice.

## Fees and where they go

- Fee tiers use rolling 14-day weighted volume (spot volume counts double toward tier). Staking tiers grant **trading fee discounts** (e.g. Wood >10 HYPE staked → 5% discount, up through Diamond).
- Maker rebates can apply at high maker-volume share tiers.
- Docs state fees are directed to the community via **HLP**, the **assistance fund**, and **deployers**. The assistance fund converts trading fees to HYPE and burns them.
- Spot/HIP-3 deployers may keep a configured share of fees on deployed markets.
- Correct framing: HYPE stakers can receive **fee discounts** (and separate staking rewards from emissions). Do **not** claim that trading fees are paid out as direct revenue share to all HYPE stakers.

## HLP vaults

- HLP (Hyperliquidity Provider) is the community vault complex; liquidator vault PnL is a component strategy of HLP.
- Depositing USDC to vaults earns vault performance (can be negative in stress). Treat vault risk separately from personal perp positions.

## HYPE staking (HyperCore)

- Transfer HYPE spot → staking account (instant). Staking account → spot has a **7-day** unstaking queue (max 5 pending withdrawals per address).
- Delegate (stake) to validators; lockup **1 day** per validator delegation before undelegate; undelegate returns to staking account instantly after lockup.
- Validators need 10k HYPE self-delegation to activate (locked one year). Commission cannot be raised above small thresholds except limited cases (≤1% new commission rule in docs).
- Rewards accrue frequently and compound by redelegation; rate formula scales with total stake (docs example ~2.37% at 400M HYPE staked—verify live).
- Staking-link feature can attribute stake to a trading account for fee discounts; linking is permanent and security-sensitive (staking user can lock trading user funds)—only link addresses the same person controls.

## Common issues and recovery

| Symptom | First checks |
|---|---|
| Insufficient margin | Add USDC, reduce size, or lower leverage; confirm perps vs spot balance. |
| Order would trigger liquidation | Size/leverage vs free margin; deposit or reduce; check cross vs isolated. |
| Deposit not visible | Confirm route (email vs wallet), source chain/asset, and whether funds landed in spot vs perps USDC. |
| Withdrawal slow / re-deposit | Check method-specific gas and FAQ for the chosen chain; avoid repeat withdraw loops. |
| Rate limited | Back off API calls; separate IP vs account limits. |
| Position missing | Refresh UI; check sub-accounts and isolated panels. |

## Security checklist

- Prefer non-custodial wallet control; keep seed phrases and private keys offline and out of chat—guide UI steps without requesting secrets.
- Verify `app.hyperliquid.xyz` (or the chosen official interface) before connecting.
- Enable trading only via the official signature prompt; revoke unused wallet connections when done.
- Geo and interface restrictions may apply; this skill does not bypass them.
- No skill content should request credentials, API secrets, or seed material.
