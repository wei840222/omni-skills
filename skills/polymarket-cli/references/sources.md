# Primary sources and version boundaries

Checked 2026-10-12. Re-open mutable sources before installation, trading or on-chain
operations. Public-query compatibility is separate from write-path compatibility.

## CLI installation, syntax and source

- Official CLI README — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/README.md
  Homebrew tap, source build and release install script are documented. Upstream
  calls the CLI experimental. A checked registry probe found no crates.io
  polymarket-cli crate; the source build uses `cargo install --path .`.
- Current CLI command constants — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/src/commands/mod.rs
  pUSD symbol, six decimals, current collateral and spender constants.
- Current CLI CTF implementation — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/src/commands/ctf.rs
  pUSD-unit amount conversion and collateral defaults.
- Current CLI approval implementation — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/src/commands/approve.rs
  Target-dependent ERC-20/CTF approval operations; broad ERC-20 allowance can be used.
- Current CLI CLOB implementation — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/src/commands/clob.rs
  U256 token parsing; buy amounts in pUSD and sell amounts in shares.
- Current CLI auth/provider defaults — https://github.com/Polymarket/polymarket-cli/blob/9b18b5faf5493b945c48ca22efaf9645f0c69ab8/src/auth.rs
  CLOB host and RPC are environment-overridable; current RPC default is polygon.drpc.org.
- Official 0.1.5 release — https://github.com/Polymarket/polymarket-cli/releases/tag/v0.1.5
  The digest-verified 0.1.5 binary was used for public read-only probes. Installed
  CTF help still advertises USDC and an older collateral contract. Trading/CTF
  migration compatibility was not inferred or tested by sending transactions.

## Market IDs, data endpoints and collateral

- Official docs index — https://docs.polymarket.com/llms.txt
- API overview — https://docs.polymarket.com/getting-started/api.md
  Gamma, CLOB, Data and relay endpoints are distinct; the endpoint list is not
  exhausted by CLOB/Gamma/Polygon RPC alone.
- Positions and tokens — https://docs.polymarket.com/concepts/positions-tokens.md
  Distinguishes positions/outcomes and token identifiers.
- Market-data overview — https://docs.polymarket.com/market-data/overview.md
  Discovery/details and public analytical data have separate query roles.
- pUSD — https://docs.polymarket.com/concepts/pusd.md
  Current trading collateral is a six-decimal Polygon ERC-20 backed by USDC.
  pUSD versus USDC/USDC.e is a protocol/version distinction, not just a display label.
- Wallets/authentication — https://docs.polymarket.com/trading/wallets-auth.md
  Current authentication/account models need version-aware integration; wallet
  setup remains user-managed under this skill's stricter security boundary.
- First order — https://docs.polymarket.com/trading/quickstart.md
- Fees — https://docs.polymarket.com/trading/fees.md
  Fees and order eligibility are mutable; fetch current market metadata before trading.

## Polygon gas

- Polygon RPC network details — https://docs.polygon.technology/pos/reference/rpc-endpoints
  Polygon mainnet chain ID 137 and native gas token POL.
- Official MATIC-to-POL migration announcement — https://polygon.technology/blog/save-the-date-matic-pol-migration-coming-september-4th-everything-you-need-to-know
  POL replaced MATIC as Polygon PoS native gas; the CLI README's old MATIC wording
  is a stale label. Direct CLI on-chain writes still need native gas; a relayed
  account path must be evaluated separately rather than generalized to every command.

## Observed live drift

The 0.1.5 command surface accepts `events list --tag politics`, not `markets list
--tag politics`. The old Trump-2024 documentation slug returned 404, and a resolved
Bitcoin token had no orderbook. The API rejected markets sorting by volume_num
with 422 although upstream help suggested it. Inspect live help/error and apply
explicit recovery; documentation examples and market data are not stable fixtures.
