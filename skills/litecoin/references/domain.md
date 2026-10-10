# Litecoin domain defaults

## Network parameters (consensus-oriented)

| Parameter | Value | Source anchor |
| --- | --- | --- |
| Block target spacing | 2.5 minutes | `nPowTargetSpacing = 2.5 * 60` in Core `chainparams.cpp` |
| Subsidy halving interval | 840000 blocks | `nSubsidyHalvingInterval` |
| Absolute money range | 84 million LTC | `MAX_MONEY = 84000000 * COIN` in `amount.h` |
| Proof of work | Scrypt | Project documentation / mining ecosystem |
| Bech32 HRP | `ltc` | `bech32_hrp` |
| MWEB HRP | `ltcmweb` | `mweb_hrp` |

Genesis and branding often describe Litecoin as a faster peer of Bitcoin for payments; treat marketing slogans as non-normative.

## Wallet orientation (non-exhaustive)

Prefer software the user already trusts and can verify:

- **Litecoin Core** — full node; strongest validation including MWEB components when running current releases.
- **Hardware wallets** (vendor LTC apps) — on-device address verification for main-chain sends.
- **Light / multi-asset wallets** — faster UX; confirm which address types and whether MWEB is actually implemented before relying on privacy features.

Always download from vendor-official channels; never from unsolicited DM links.

## Merged mining with Dogecoin

- Dogecoin is commonly merge-mined with Litecoin on Scrypt, sharing miner work.
- This is a **miner/pool** concern; end users do not configure merged mining to send payments.
- Security narratives may reference combined work, but users still verify payments on the Litecoin chain they actually use.

## Security defaults

- Seed / xprv never in chat; never in skill state files (this skill is stateless).
- Verify full destination strings on device screens; clipboard malware swaps middle characters.
- Reject “send LTC get 2× back”, cold-DM “support”, and “MWEB recovery portals” that request keys.
- Dust unsolicited receipts: avoid consolidating with primary UTXOs without a privacy plan.
- Irreversible sends: triple-check network + address prefix + venue name before broadcast.

## Common issue → first response

| Issue | First response |
| --- | --- |
| Unconfirmed payment | Explorer check → RBF/CPFP eligibility → wait policy (`fees-and-recovery.md`) |
| Exchange no-credit | Confirmations + correct asset/network + whether MWEB was used |
| Zero balance after import | Address type / scan path (`addresses.md`); no seed collection |
| Want privacy | Explain optional MWEB + peg rules; do not promise default anonymity on main chain |
| “Is LTC the same as BTC?” | Shared UTXO ancestry and tooling patterns, different ports, prefixes, PoW, supply, and MWEB |
