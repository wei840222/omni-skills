## Memo Field (Critical)
- Exchanges require a memo for deposits — sending without the venue memo can permanently lose funds
- Memo can be text, ID, or hash — use exactly what the exchange provides
- Memos are mandatory for centralized exchange deposits — differentiate from self-custody wallets that usually need none
- Personal wallets typically function without memos — reserve memos for centralized services and some anchors
- Verify memo type matches — text memo vs ID memo are different encodings

## Account Requirements
- Minimum balance to exist: **two base reserves** (currently **1 XLM**) — required to activate a `G…` account
- One base reserve is currently **0.5 XLM** (validators can change this rarely)
- Each ordinary trustline, offer, extra signer, or data entry adds **one** base reserve (0.5 XLM) — locked for reserves, not freely spendable
- Pool-share trustlines cost **two** base reserves (currently 1 XLM) and consume two of the 1,000 subentry slots
- Available balance ≈ balance − minimum balance − selling liabilities
- Sending to a new account must fund at least the create/minimum (typically 1+ XLM) unless sponsored
- Merging an account recovers reserve — remove trustlines/offers/data first
- Sources: https://developers.stellar.org/docs/learn/fundamentals/lumens#minimum-balance · https://developers.stellar.org/docs/learn/fundamentals/stellar-data-structures/accounts

## XLM Token
- Native asset of the Stellar network — used for fees, rent (Soroban), and reserves
- Network minimum inclusion fee is currently **100 stroops per operation** (0.00001 XLM) when not in surge pricing; effective fee can rise under load
- Stroop = 0.0000001 XLM (one ten-millionth of a lumen)
- Fast finality — on the order of a few seconds via Stellar Consensus Protocol (SCP)
- No proof-of-work mining — SCP validator agreement
- Source: https://developers.stellar.org/docs/learn/fundamentals/fees-resource-limits-metering

## Trustlines
- Must trust an issuer before receiving their tokens — explicit opt-in (`change_trust`)
- Trustline costs one base reserve — locked until removed (pool shares: two)
- Remove trustlines to recover reserve — balance must be zero first
- XLM needs no trustline; claimable balances can stage assets until the recipient opens a trustline
- Trustlines also track buying/selling liabilities against open offers

## Anchors and Assets
- Anchors issue fiat-backed or on/off-ramp tokens — verify issuer reputation before trusting
- Stellar has native USDC issued by Circle on the network — still requires the USDC trustline
- Path payments convert automatically along SDEX books and liquidity pools — send one asset, receive another
- Always confirm asset code **and** issuer account, not ticker alone

## Addresses
- Public keys start with **G** — 56 characters (Stellar accounts)
- Contract accounts use **C…** addresses (Soroban) — different from classic G accounts
- Secret keys start with **S** — keep strictly confidential; never paste into chat logs or skill state
- Federated addresses: `user*domain.com` — human-readable, resolves to a G address
- Muxed addresses encode account + memo — **M** prefix, useful when a venue needs memo semantics in the address

## Transaction Features
- Multiple operations per transaction — batch related actions
- Sequence number is required and must advance — similar role to a nonce
- Time bounds optional — transactions can expire
- Fee bumping available — wrap/increase fee on a pending transaction
- Inclusion fee is per-operation; surge pricing can raise the paid inclusion fee above the network minimum

## DEX and Trading
- Built-in decentralized exchange (SDEX) — native to the protocol
- **Order books** — classic limit offers
- **Liquidity pools / AMMs** — constant-product automated market makers held in-protocol (not only external DEXes)
- Path payments (`PathPaymentStrictSend` / `PathPaymentStrictReceive`) can route across books **and** pools
- Pool participants deposit reserves, hold non-transferable pool shares, and earn pool swap fees (protocol pool fee is 30 bps / 0.30%, separate from network fees)
- Pool-share trustlines require prior authorized trustlines for both reserves (unless a reserve is XLM)
- Swap UIs exist in ecosystem wallets (e.g. Lobstr, StellarTerm) — still verify asset issuers
- Source: https://developers.stellar.org/docs/learn/fundamentals/liquidity-on-stellar-sdex-liquidity-pools

## Wallets
- Lobstr — popular mobile/web wallet
- StellarTerm — web trading UI
- Solar Wallet — desktop
- Ledger — hardware via compatible apps
- Freighter — browser extension for dApps / Soroban

## Common Issues
- "Destination account does not exist" — account uninitialized; fund with enough XLM to meet minimum (or use sponsorship)
- "Missing memo" / wrong memo — exchange deposit at risk of loss; stop and match venue instructions
- "Insufficient balance" — must keep minimum reserve + liabilities above spend
- "Trustline is unestablished" — add trustline before receiving the asset
- Transaction stuck — classic payments usually finalize quickly; re-check sequence, time bounds, and fee under surge

## Cross-Border Payments
- Designed for remittances — fast and low network fees relative to correspondent banking
- Anchor network for fiat on/off ramps — availability varies by corridor and provider
- MoneyGram partnership historically used for cash pickup in supported markets — confirm live corridor status with the provider
- USDC corridors — stablecoin transfers between countries on Stellar rails

## Soroban (Smart Contracts)
- Smart contract platform on Stellar — Rust-oriented contracts, separate from classic payment ops
- Contract accounts use C addresses; classic G accounts still hold XLM for fees/reserves
- Contract data uses rent / state archival rather than classic base-reserve subentries
- Mainnet is live — DeFi and other contract apps continue to expand
- Prefer official Stellar docs and audited examples before mainnet deploys

## Security
- Seed phrase / secret key custody is critical — treat as high-value secrets
- Multisig available on classic accounts — require multiple signatures
- SEP-10 web authentication is a common standard for service login
- Decode and verify transaction XDR before signing
- Prefer hardware wallets or well-reviewed software; never reuse secrets across chat or automation logs
