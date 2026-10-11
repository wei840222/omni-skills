# Command Reference — Polymarket CLI

## Installation

```bash
# Homebrew (macOS/Linux) — recommended
brew tap Polymarket/polymarket-cli https://github.com/Polymarket/polymarket-cli
brew install polymarket

# From source
git clone https://github.com/Polymarket/polymarket-cli
cd polymarket-cli && cargo install --path .
```

Installation requires user consent. The official tap must be added before `brew
install`; absence from an untapped Homebrew registry is not proof of an absent tap.
The observed crates.io probe found no `polymarket-cli` crate, so use the upstream
source-build route instead of a registry install. Review and pin the source/release
before building; the upstream install script is another user-approved option,
not a reason to pipe an uninspected network script into a shell.

## Version and protocol preflight

Run `polymarket --version` and the installed subcommand's `--help`. Official
current docs and pinned upstream source describe pUSD (six-decimal ERC-20 collateral
on Polygon, backed by USDC). The verified 0.1.5 release binary still advertises
USDC collateral in CTF help and its old collateral address. That is a real version
split: a public-query success does not certify old trading/CTF contracts. Keep
mutations pending until version, current collateral/spender addresses and wallet
signature model agree. Confirm any upgrade separately; changing only a ticker or
forcing a new collateral address into an old CLI is not a migration procedure.

POL is the current Polygon PoS native gas asset. Upstream README still says MATIC;
the current Polygon RPC docs and official migration announcement supersede that
label. Collateral and gas are different assets. Actual fee rates, supported order
types, approvals and transaction counts come from current metadata/source/help,
not fixed historical numbers. Source URLs are in `references/sources.md`.

## Output Modes

```bash
polymarket -o table ...  # Human-readable (default)
polymarket -o json ...   # Machine-readable
```

Errors: table prints to stderr, JSON prints `{"error": "..."}` to stdout.

---

## Markets (No Wallet Needed)

```bash
# List markets
polymarket markets list --limit 10
polymarket markets list --active true --closed false --limit 10

# Get specific market
polymarket markets get SLUG_OR_ID
polymarket markets get MARKET_SLUG_OR_ID

# Search
polymarket markets search "bitcoin" --limit 5

# Tags
polymarket markets tags MARKET_ID
```

Flags include `--limit`, `--offset`, `--order`, `--ascending`, `--active`, `--closed`;
check the installed help. `--tag` is on `events list`, not `markets list`.
The API rejected `--order volume_num` with 422 during the checked 0.1.5 invocation
even though CLI help/README suggests it. Retry without sorting and rank returned
results by a clearly named metric locally; a limited page is not a global top-N.
For politics, discover tagged events, then select their active, nonclosed markets.
For "trending", define a metric (such as 24-hour volume) and disclose coverage;
event volume is not a market's individual volume.

## Events (No Wallet Needed)

```bash
polymarket events list --limit 10
polymarket events list --tag politics --active true
polymarket events get EVENT_ID
polymarket events tags EVENT_ID
```

## Other Read-Only

```bash
# Tags
polymarket tags list
polymarket tags get politics
polymarket tags related politics

# Series
polymarket series list --limit 10
polymarket series get SERIES_ID

# Comments
polymarket comments list --entity-type event --entity-id 500
polymarket comments by-user 0xADDRESS

# Profiles
polymarket profiles get 0xADDRESS

# Sports
polymarket sports list
polymarket sports teams --league NFL --limit 32
```

---

## CLOB Queries (No Wallet Needed)

```bash
# Health
polymarket clob ok

# Prices
polymarket clob price TOKEN_ID --side buy
polymarket clob midpoint TOKEN_ID
polymarket clob spread TOKEN_ID

# Batch queries
polymarket clob batch-prices "TOKEN1,TOKEN2" --side buy
polymarket clob midpoints "TOKEN1,TOKEN2"
polymarket clob spreads "TOKEN1,TOKEN2"

# Order book
polymarket clob book TOKEN_ID
polymarket clob books "TOKEN1,TOKEN2"

# Last trade
polymarket clob last-trade TOKEN_ID

# Market info
polymarket clob market CONDITION_ID
polymarket clob markets

# Price history
polymarket clob price-history TOKEN_ID --interval 1d --fidelity 30
# Intervals: 1m, 1h, 6h, 1d, 1w, max

# Metadata
polymarket clob tick-size TOKEN_ID
polymarket clob fee-rate TOKEN_ID
polymarket clob neg-risk TOKEN_ID
polymarket clob time
polymarket clob geoblock
```

---

## Trading (Wallet Required)

### Orders

```bash
# Limit order
polymarket clob create-order \
  --token TOKEN_ID \
  --side buy --price 0.50 --size 10

# Market order
polymarket clob market-order \
  --token TOKEN_ID \
  --side buy --amount 5

# Batch orders
polymarket clob post-orders \
  --tokens "TOKEN1,TOKEN2" \
  --side buy \
  --prices "0.40,0.60" \
  --sizes "10,10"

# Cancel
polymarket clob cancel ORDER_ID
polymarket clob cancel-orders "ORDER1,ORDER2"
polymarket clob cancel-market --market CONDITION_ID
polymarket clob cancel-all
```

Order types: GTC (default), FOK, GTD, FAK. Add `--post-only` for limit orders.

### View Orders and Trades

```bash
polymarket clob orders
polymarket clob orders --market CONDITION_ID
polymarket clob order ORDER_ID
polymarket clob trades
```

### Balances

```bash
polymarket clob balance --asset-type collateral
polymarket clob balance --asset-type conditional --token TOKEN_ID
polymarket clob update-balance --asset-type collateral
```

---

## Rewards and API Keys (Wallet Required)

```bash
polymarket clob rewards --date 2024-06-15
polymarket clob earnings --date 2024-06-15
polymarket clob earnings-markets --date 2024-06-15
polymarket clob reward-percentages
polymarket clob current-rewards
polymarket clob market-reward CONDITION_ID

# Order scoring
polymarket clob order-scoring ORDER_ID
polymarket clob orders-scoring "ORDER1,ORDER2"

# API keys
polymarket clob api-keys
polymarket clob create-api-key
polymarket clob delete-api-key

# Account
polymarket clob account-status
polymarket clob notifications
polymarket clob delete-notifications "NOTIF1,NOTIF2"
```

---

## Public Data (No Wallet Needed)

```bash
# Portfolio
polymarket data positions 0xWALLET
polymarket data closed-positions 0xWALLET
polymarket data value 0xWALLET
polymarket data traded 0xWALLET

# Trade history
polymarket data trades 0xWALLET --limit 50

# Activity
polymarket data activity 0xWALLET

# Market data
polymarket data holders CONDITION_ID
polymarket data open-interest CONDITION_ID
polymarket data volume EVENT_ID

# Leaderboards
polymarket data leaderboard --period month --order-by pnl --limit 10
polymarket data builder-leaderboard --period week
polymarket data builder-volume --period month
```

---

## Approvals (Wallet Required, On-Chain)

```bash
# Check approvals
polymarket approve check
polymarket approve check 0xADDRESS

# Approve configured contracts (state-dependent transactions; POL gas)
polymarket approve set
```

## Conditional Tokens (Wallet Required, On-Chain)

```bash
# Split current collateral into YES/NO tokens (verify version/contract first)
polymarket ctf split --condition CONDITION_ID --amount 10

# Merge outcome tokens back to current collateral
polymarket ctf merge --condition CONDITION_ID --amount 10

# Redeem after resolution
polymarket ctf redeem --condition CONDITION_ID
polymarket ctf redeem-neg-risk --condition CONDITION_ID --amounts "10,5"

# Calculate IDs (read-only)
polymarket ctf condition-id --oracle 0x... --question 0x... --outcomes 2
polymarket ctf collection-id --condition 0x... --index-set 1
polymarket ctf position-id --collection 0x...
```

Current upstream CTF `--amount` is expressed in pUSD units; 0.1.5 help still says
USDC. Preserve that version distinction and verify before any mutation. Direct
Polygon transactions use POL for gas. Market-order amount is collateral spend
for buys and shares for sells, not a universal dollar amount.

## Bridge

```bash
# Deposit addresses
polymarket bridge deposit 0xWALLET

# Supported assets
polymarket bridge supported-assets

# Check status
polymarket bridge status 0xDEPOSIT_ADDRESS
```

---

## Wallet Management (USER-ONLY — agent must not run these)

These commands handle private keys. The user must run them directly:

```bash
polymarket wallet create          # Generate new
polymarket wallet create --force  # Overwrite existing
polymarket wallet import PRIVATE_KEY_USER_ONLY    # Import existing
polymarket wallet address         # Print address
polymarket wallet show            # Full info (may reveal sensitive data)
polymarket wallet reset           # Delete config (prompts)
polymarket wallet reset --force   # Delete without prompt
```

Wallet commands and the setup wizard are user-only. Explain the boundary and hand execution to the user's own terminal; secret entry is outside chat/agent scope.

## Interactive Shell

```bash
polymarket shell
# polymarket> markets list --limit 3
# polymarket> clob book TOKEN_ID
# polymarket> exit
```

## Utility

```bash
polymarket status     # API health
polymarket setup      # USER-ONLY: first-time wallet wizard
polymarket upgrade    # Separate user-confirmed installation mutation
polymarket --version
polymarket --help
```


## Execution boundaries

Use SKILL.md for per-action confirmation, wallet/config restrictions and the
pre-trade report. Command examples here are syntax references, not authorization.
Use array arguments for untrusted slugs/IDs rather than interpolated shell code.
Authenticated orders/trades/balances and credential management require account
access consent; API-key create/delete and notification deletion are mutations.
`bridge deposit` may create deposit addresses despite its query-like name; seek
confirmation. Public `data` calls expose the queried wallet address to the provider.
CTF ID calculation is read-only but requires real contract identifiers; placeholders
are not runnable inputs. Keep secret flags and user-managed wallet commands out of
automated command batches and interactive shell sessions.

## Failure recovery

- Unknown flag: inspect that exact installed subcommand's help; remove only the
  unsupported filter and disclose any narrowed intent (politics uses tagged events).
- Market slug 404: report the exact unavailable slug, then search the intended topic.
  Present candidates and obtain the user's selection; a similarly named market is
  not an equivalent substitute. If none matches, give no current price.
- No orderbook for a token: verify outcome mapping and market closure. Report price
  unavailable; a historical settled outcome value is not a fresh executable quote.
- Malformed/empty JSON or API error: inspect exit status/error and retry one public
  read only when transient. Preserve the last verified timestamp; report persistent failure.
- 422 sorting error: retry the same query without `--order`, then explain ranking
  coverage rather than manufacturing a top market list.
- Network/429 failure: back off and retry once, then return the diagnostic and the
  missing evidence; trade execution waits for a successful fresh preflight.
- Auth/allowance failure: report the failing boundary and user-managed setup or
  separately confirmed allowance next step. Credentials and fund transfers remain
  outside the repair action; an uncertain submitted order is checked before any retry.
- Unsupported collateral/contracts: leave the mutation pending; compare installed
  help and pinned current source/docs, then perform a separately approved migration.
