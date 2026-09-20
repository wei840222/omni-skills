# Cosmos Network Guide

## Ecosystem Overview
- Cosmos is a network of sovereign blockchains — not a single chain
- Cosmos Hub is the main Hub chain — where ATOM lives for staking and Hub governance
- IBC (Inter-Blockchain Communication) connects participating Cosmos SDK chains
- Each chain is sovereign — own validators, own fee token, own governance
- One seed can derive many chain addresses — prefixes and paths differ per chain

## ATOM Token
- Native token of Cosmos Hub — staking, governance, and Hub fees
- Secures the Hub — not other app chains by default
- Inflation funds staking rewards on the Hub
- Other chains use their own gas tokens (for example OSMO on Osmosis)

## IBC Transfers (Critical)
- IBC moves assets between participating chains over named channels/paths
- Recipient address differs per chain even from the same mnemonic
- Channel/path matters — the same asset may exist on multiple routes
- Tokens may appear wrapped or denom-traced on the destination (ATOM on Osmosis is IBC ATOM)
- Verify the channel is active before retrying a stuck transfer
- Prefer waiting for relayer progress before opening a second parallel transfer on the same sequence

## Address Format
- Bech32 format — human-readable prefix + data
- `cosmos1…` for Cosmos Hub; other chains use their own prefixes (`osmo1…`, `juno1…`, …)
- Same mnemonic yields different addresses per chain derivation path
- Verify the prefix matches the destination chain before signing

## Staking
- Delegate ATOM to Hub validators to earn staking rewards
- Unbonding period on Cosmos Hub is 21 days — funds are locked while unbonding
- Slashing risk exists — validator downtime or double-sign can penalize delegators
- Redelegation can move stake between validators without waiting out unbonding (subject to redelegation rules and locks)
- Liquid staking products (for example stATOM-style derivatives) trade liquidity for smart-contract and issuer risk

## Validators
- Compare commission, uptime, and slashing history before delegating
- Prefer decentralization — select reliable validators outside the most concentrated top set when practical
- Validators may vote on governance by default — override by voting with your own stake
- Prefer community operators over exchange validators when airdrop eligibility matters

## Governance
- On-chain proposals move through deposit, voting, and execution windows
- Staked ATOM provides voting power
- Options typically include Yes, No, NoWithVeto, and Abstain — veto can kill a proposal under quorum rules
- Active participation affects chain parameters and treasury decisions

## Wallets
- Keplr — widely used browser extension and mobile wallet for Cosmos chains
- Leap — alternative multi-chain Cosmos wallet
- Cosmostation — mobile and web option
- Ledger via compatible wallet apps for larger balances
- One seed can cover many Cosmos chains inside a supported wallet — never paste a seed into chat, a website form, or an agent session

## Gas and Fees
- Fees are paid in the chain’s native fee token — ATOM on Hub, OSMO on Osmosis, and so on
- Fees are often low relative to Ethereum L1, but still chain- and congestion-dependent
- Wallets usually estimate gas; under-gassed transactions fail and need a higher-gas retry
- Failed simulations should be fixed before rebroadcasting

## DeFi on Cosmos (High Level)
- Osmosis — major Cosmos DEX / AMM venue
- Liquid staking and lending venues exist across the ecosystem and change over time
- Always confirm the live app URL, channel, and asset denom before signing
- Treat third-party dApp approvals as revocable permissions to audit periodically

## Airdrops
- Ecosystem airdrops have historically rewarded Hub stakers and early users
- Staking with non-exchange validators is a common eligibility pattern — verify each campaign’s rules
- Claiming windows expire — check deadlines and required actions before moving stake
- Past examples (OSMO, JUNO, STARS eras) are historical context, not a guarantee of future drops

## Common Issues
- **Account not found** — address is valid but has never received funds / has no on-chain account yet
- **IBC transfer pending or stuck** — often relayer delay; wait, then verify channel status before retrying a different path
- **Sequence mismatch** — a prior transaction is still pending or was broadcast twice; wait for inclusion or reset sequence carefully in the wallet
- **Unbonding pending** — 21-day Hub unbonding is expected, not a stuck transfer
- **Wrong chain address** — a `cosmos1…` address is not valid as an Osmosis destination (`osmo1…`)

## Security
- The same seed unlocks many chains — protect it as high-value credential material
- Verify wallet connection origins — phishing sites mimic Keplr/Leap connect flows
- IBC itself does not remove user-error risk — wrong channel, wrong prefix, or malicious dApp still loses funds
- Prefer Ledger for large balances when the wallet path supports it
- Revoke unused dApp permissions after campaigns or one-off approvals
