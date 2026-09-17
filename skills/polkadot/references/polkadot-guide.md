## Network Architecture
- Relay Chain is the main chain — coordinates shared security and consensus
- Parachains are application-specific chains — lease Relay Chain security
- DOT is the native token — staking, governance, fees, and parachain bonds
- Kusama is the canary network — real economic value, faster upgrade cadence

## Address Format (SS58)
- Same seed yields different displayed addresses per network
- Polkadot mainnet addresses commonly start with `1`
- Kusama addresses commonly start with a capital letter
- SS58 is Substrate encoding — not Ethereum hex (`0x…`)
- One seed can derive many Substrate chains — always verify the network prefix before sending

## DOT Token Economics
- 2020 redenomination: old 1 DOT = new 100 DOT — ignore pre-redenomination balances in docs
- 10 decimal places (Planck is the smallest unit) — not Ethereum's 18 decimals
- Existential deposit (ED): accounts below the network ED are reaped (deleted)
- Locked DOT can still participate in governance — staking lock ≠ lost voting power

## Staking (Direct Nomination)
- Nominate up to 16 validators — stake backs their validation set
- Minimum active stake is dynamic — competition sets the floor; check a live staking dashboard
- Unbonding period is 28 days on Polkadot — funds locked and not transferable while unbonding
- Slashing risk exists — misbehaving validators can penalize nominators
- Rewards may be claimed manually or auto-compounded — wallet / nomination setup dependent

## Nomination Pools
- Lower entry barrier than direct nomination — pools accept small DOT amounts (commonly from 1 DOT)
- Pool operator selects validators — less control, simpler UX
- Rewards are distributed by the pool after commission
- Same 28-day unbonding period applies when leaving a pool

## Governance (OpenGov)
- OpenGov tracks handle proposals, referenda, and voting
- Conviction voting: longer lock → higher vote weight
- Any DOT holder can participate within track rules
- Treasury spends are community-controlled via referenda

## Parachains and Crowdloans
- Parachain slots are won via auctions — projects lock DOT for lease duration
- Crowdloans let users contribute DOT for the lease (historically multi-year leases)
- Contributed DOT is returned after the lease — project tokens may be granted as reward
- System chains hold permanent slots — Asset Hub (formerly Statemint), Bridge Hub, and related system parachains

## Cross-Consensus Messaging (XCM)
- XCM moves assets and instructions across consensus systems
- Teleport vs reserve-backed transfer — different trust and reserve models
- Not every parachain supports every asset — verify route and asset registry first
- Fees may be paid in DOT or the parachain fee asset — depends on the hop

## Wallets
- Polkadot.js — full-featured power-user extension / apps
- Nova Wallet, Talisman — stronger day-to-day UX for many users
- Ledger via compatible wallets — prefer hardware for large balances
- SubWallet — solid mobile option
- Never paste a seed phrase into a chat, website form, or agent session

## Transaction Characteristics
- Block time is on the order of ~6 seconds with deterministic finality after a few blocks (~12s class UX)
- Fees are paid in DOT from transferable (unlocked) balance
- Nonce-ordered extrinsics — stuck nonce blocks later transactions
- Optional tips can bump priority — rarely required for normal use

## Common Issues
- Existential deposit error — transfer would drop free balance below ED; add funds or use transfer-all / allow-death flow
- Staking not earning — below the dynamic minimum active bond, or nominated validators not elected
- Cannot transfer while fully bonded — keep unlocked DOT for fees
- Wrong network address — Kusama / other SS58 prefixes will not credit Polkadot mainnet
- Still unbonding — wait the full 28 days before the balance becomes transferable
- XCM failed mid-route — check asset support, weight/fees, and destination parachain status

## Security
- One Substrate seed can control many networks — treat it as multi-chain root access
- Verify full address and network label before every send
- Prefer hardware wallets for treasury-size balances
- Revoke unused dApp extensions and review proxy/multisig permissions regularly
- Phishing targets Polkadot.js and wallet connect flows — type known-good URLs yourself
