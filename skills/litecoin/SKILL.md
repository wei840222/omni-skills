---
name: litecoin
description: >
  Diagnose Litecoin (LTC) address formats, fees, confirmations, RBF recovery,
  and optional MWEB privacy (peg-in/peg-out, stealth addresses). Use for
  Legacy/P2SH/bech32/MWEB deposit checks, stuck txs, exchange compatibility,
  or merged-mining context with Dogecoin. Not for Bitcoin UTXO/Lightning
  (`bitcoin`), Dogecoin-only flows (`dogecoin`), EVM chains (`ethereum`), or
  portfolio/market tooling (`crypto-tools`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"Ł"}'
  related-skills: '{"bitcoin":"Bitcoin UTXO, fees, RBF/CPFP, and Lightning outside Litecoin.","dogecoin":"Dogecoin-only txs and Scrypt merged-mining peer of Litecoin.","ethereum":"EVM gas, approvals, and L2 bridges outside Litecoin.","blockchain":"General ledger fundamentals beyond Litecoin-specific address and MWEB guidance.","crypto-tools":"Market data and exchange tooling once Litecoin transaction mechanics are settled."}'
---

# Litecoin (LTC)

Stateless domain skill for **Litecoin payments, address formats, fees, stuck-tx recovery, exchange deposit checks, and optional MWEB privacy**. It does not store keys, seeds, or transaction history in the package.

## When to load

- Send/receive LTC; verify Legacy (`L`), P2SH (`M`/`3`), native SegWit (`ltc1…`), or MWEB (`ltcmweb1…`) deposit addresses
- Stuck or slow confirmations; RBF eligibility; fee sizing by vbytes
- Exchange deposit compatibility, especially MWEB vs main-chain only
- MWEB peg-in / peg-out and stealth-address orientation
- Merged-mining context with Dogecoin (Scrypt) when it affects security narrative

## Core defaults

Keep always-on rules here; load at most one deep `references/` file per step (progressive disclosure).

1. **Classify the layer first** — main-chain UTXO vs optional MWEB extension block. Do not treat MWEB as the default send path.
2. **Match address prefix before blaming missing funds** — wrong script type or wrong network HRP is the usual root cause.
3. **Never request seeds or private keys in chat** — guide local wallet UI or hardware on-device verification.
4. **Verify exchange deposit rules** — many venues accept main-chain LTC only; MWEB deposits can be unrecoverable if unsupported.
5. **Re-open `references/sources.md`** before restating version-sensitive Core, LIP, or MWEB claims.

## Ordered workflow

1. **Classify** — address format check, fee/stuck tx, exchange deposit, MWEB privacy, wallet sync, or security/scam.
2. **Context** — network (mainnet), amount/urgency, wallet type, whether funds are main-chain or MWEB, and whether the user is sender or receiver.
3. **Apply minimum viable rules** below; load only the matching reference.
4. **Verify** on a public explorer or venue docs when confirmation status or deposit support is disputed.
5. **Bound** — irreversible sends, unsupported MWEB deposits, and seed-phishing attempts get hard stops.

## Minimum viable rules

| Topic | Rule |
| --- | --- |
| Block time | Target ~2.5 minutes (`nPowTargetSpacing = 2.5 * 60` in Core chainparams) |
| Supply | Consensus `MAX_MONEY = 84_000_000 * COIN`; subsidy halving interval 840000 blocks |
| Legacy P2PKH | Base58 version `48` → addresses typically start with `L` |
| Nested SegWit / P2SH | Version `5` → `3…`; Litecoin also uses version `50` → `M…` (SCRIPT_ADDRESS2) |
| Native SegWit | Bech32 HRP `ltc` → `ltc1…` (BIP173); preferred for lower fees when supported |
| MWEB addresses | HRP `ltcmweb` → `ltcmweb1…` stealth addresses (DKSAP); opt-in only |
| Confirmations | ~1 block ≈ 2.5m; high-value often waits ~6 blocks (~15m)—venue policy overrides |
| Fees | Size (vbytes/weight) driven, not amount sent; prefer SegWit inputs/outputs when both sides support them |
| RBF | Opt-in BIP125-style replace-by-fee when the original tx signaled replaceability |
| MWEB path | Peg-in main → extension block; peg-out extension → main; do not deposit MWEB to unsupported exchanges |
| Merged mining | Scrypt PoW; Dogecoin merge-mining shares work—no user action required |

## Failure branches

| Signal | Action |
| --- | --- |
| Address prefix unknown / mixed networks | Stop send; match prefix table in `references/addresses.md`; never invent formats |
| Exchange gave `L`/`M`/`3`/`ltc1` and wallet is SegWit-capable | Main-chain send is fine; fee savings may be lower when paying a legacy output |
| User holds MWEB and venue is main-chain only | Peg-out to a standard main-chain address first; do not send `ltcmweb1…` blindly |
| Unconfirmed send, user is sender, RBF enabled | Broadcast higher-fee replacement with same inputs |
| Unconfirmed send, user is receiver only | Cannot RBF; wait or ask sender to bump; CPFP only if an unconfirmed output is spendable |
| Wallet shows zero after seed import | Check address type / derivation scan order before assuming loss; no seed in chat |
| Unsolicited “support” wants seed / “MWEB sync” | Treat as theft; refuse; verify on explorer with public txid/address only |
| Fee or MWEB claim is version-sensitive | Re-open Core docs / LIPs in `references/sources.md` |

## Routing

| Need | Load |
| --- | --- |
| Address prefixes, script types, deposit checks | `references/addresses.md` |
| Fees, confirmations, RBF/stuck recovery | `references/fees-and-recovery.md` |
| MWEB model, peg-in/out, stealth addresses, exchange caution | `references/mweb.md` |
| Network parameters, wallets, merged mining, security defaults | `references/domain.md` |
| Verified primary sources for Gate 6 facts | `references/sources.md` |

Load at most one deep reference beyond the active step unless the user asks for a second topic.

## Safety defaults

- Operational guidance only: no custodial login, no broadcasting transactions for the user, no holding keys.
- Never paste or request seed phrases, private keys, or full wallet dumps in chat.
- Prefer hardware on-device address verification; compare first/last characters across devices against clipboard malware.
- Do not promise fixed USD fees, guaranteed confirmation times, or exchange support without checking current venue docs.
- MWEB is optional privacy, not a default layer and not Lightning-compatible MW scripting.
