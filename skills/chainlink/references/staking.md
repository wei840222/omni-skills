# Chainlink Staking (v0.2)

Staking lets LINK holders and node operators back oracle services with staked LINK for rewards and cryptoeconomic security. Details below are **orientation only** — caps, eligibility, and pool fill state change; verify on the official staking/economics pages before any stake or unstake.

## v0.2 orientation (from official economics materials)

- v0.2 (Nov 2023 upgrade path from v0.1) introduced a modular platform, unbonding for unstake, slashing for **node operator** stake tied to in-scope services, and a path to dynamic rewards.
- Community stakers: documented per-address min/max (historically min 1 LINK, max on the order of 15,000 LINK) subject to **protocol capacity**.
- Node operator stakers: higher min/max band (historically 1,000–75,000 LINK) with slashing exposure for misbehavior on secured services.
- When the community pool is full, new stake waits until existing stake unbonds and frees capacity.
- Unbonding means withdrawals are not instant after unstake initiation.

## Safety

- Confirm you are on the official staking UI / contracts.
- Distinguish **community** vs **node operator** roles — slashing scope is not identical.
- Do not invent APR figures; read the live rewards UI and docs.
- If pool state or caps matter to the user decision, re-open live official pages in `sources.md` rather than quoting this file’s historical launch numbers as current truth.