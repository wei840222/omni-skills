# Monero domain guide

Use this file for privacy primitives, address handling, keys, and payment
proofs. Re-check mutable vendor or fee claims via `sources.md`.

## Privacy by default

Monero hides **sender, receiver, and amount** on every transaction. Official
project materials contrast this with transparent chains (Bitcoin/Ethereum) and
with selectively transparent designs: Monero keeps privacy on by default through
three core technologies:

- **Ring signatures** — the true spend is mixed among decoy outputs pulled from
  the chain, so an outside observer cannot tell which ring member signed.
- **Stealth addresses** — the sender creates a one-time destination on behalf of
  the recipient; on-chain outputs do not reuse the published address as a simple
  linkable receive identifier.
- **RingCT (Ring Confidential Transactions)** — amounts are confidential; RingCT
  became mandatory for all network transactions after September 2017
  (activated earlier at block 1220516 in January 2017).

Because every spend carries plausible deniability, Monero treats fungibility as
a protocol property rather than an optional privacy mode.

## Keys and addresses

Creating an account yields a private **view key**, a private **spend key**, and
a public address built from the public counterparts of those keys.

| Key / artifact | Role |
|---|---|
| Spend key | Authorizes outgoing spends |
| View key | Reveals incoming transactions to that account |
| Public address | What counterparties use to pay you |

Official Moneropedia notes that a raw Monero address is **95 characters** and
starts with `4` or `8`. Integrated addresses (address + encrypted compact
payment ID) are **106 characters**.

Practical routing:

- Prefer generating a **fresh subaddress** (commonly presented as an `8…`
  receive address in wallets) per counterparty or invoice when the wallet
  supports it.
- Keep the primary `4…` address for cases that explicitly need it (some mining
  setups still document primary-address requirements).
- **OpenAlias** names (for example `donate.getmonero.org`) can resolve to a
  Monero address for human-friendly receives.

### Payment IDs

Long standalone payment IDs (64 hex chars) were **phased out** because reuse can
link payments, users forget them, and services cannot batch them cleanly. The
2019 project notice told services to move to **integrated addresses or, better,
subaddresses**, and noted integrated addresses might also be phased later.
For new guidance, prefer **subaddresses**.

Compact payment IDs still appear inside integrated addresses; wallets that still
expose `integrated_address` do so for compatibility, not as the preferred modern
merchant pattern.

## View-key audits

Sharing a private view key lets another party see **incoming** transactions for
that address. Official Moneropedia still warns that **outgoing** transactions
cannot be reliably reconstructed from a view key alone, so a balance inferred
only from a view key must not be treated as authoritative settlement evidence.

Use view keys for accounting or limited audits when the user understands that
limitation. Prefer transaction proofs for payment disputes.

## Payment proofs

To prove a payment without handing over spend authority, Monero wallets can
produce a proof from:

1. transaction ID (tx ID)
2. transaction key (tx key / tx secret key)
3. recipient address

The recipient (or an agreed auditor) can verify the proof without receiving the
sender's seed. Public explorers cannot substitute for this proof on a private
chain. See the official prove-payment user guide in `sources.md`.

## Default spendability vs custom unlock_time

Two different "unlock" ideas appear in Monero docs:

1. **Ordinary received outputs** must mature before they can be spent again.
   Wallets commonly surface this as a short post-receive wait measured in
   blocks; treat the wallet's displayed unlock/pending state as source of truth
   rather than inventing a USD timeline.
2. **Custom `unlock_time`** on a transfer can lock outputs until an absolute
   block height or (via non-CLI paths) timestamp. The value is public, rarely
   used, harms privacy when clustered, and official Moneropedia marks the
   feature as deprecated toward FCMP++. Do not design critical product flows on
   custom unlock times; warn users to check `show_transfers` (or equivalent) for
   unexpected locks on received funds.

## Security defaults

- Download official binaries from getmonero.org and **verify hashes** before
  install; corrupted archives can lose funds.
- Prefer an own node, or a remote node over Tor/I2P, when query privacy matters.
- Keep seed phrases offline and never paste them into chat.
- For large balances, confirm any hardware-wallet path against current official
  docs before promising device support.
- Exchange listing status and fiat fee tables change; verify live before advising
  a specific venue or USD cost.
