---
name: dogecoin
description: >
  Diagnose Dogecoin (DOGE) address formats, fees, confirmations, unconfirmed
  sends without RBF, wallet sync, and Scrypt merged-mining context with Litecoin.
  Use for D-prefix deposits, stuck txs, exchange compatibility, or scam checks.
  Not for Bitcoin UTXO/Lightning (`bitcoin`), Litecoin/MWEB (`litecoin`), XRPL
  tags (`xrp`), or portfolio/market tooling (`crypto-tools`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐕"}'
  related-skills: '{"bitcoin":"Bitcoin UTXO, fees, RBF/CPFP, and Lightning outside Dogecoin.","litecoin":"Litecoin address/MWEB flows and Scrypt merged-mining peer of Dogecoin.","xrp":"XRPL reserves and destination tags instead of Dogecoin simple addresses.","blockchain":"General ledger fundamentals beyond Dogecoin-specific payment guidance.","crypto-tools":"Market data and exchange tooling once Dogecoin transaction mechanics are settled."}'
---

# Dogecoin (DOGE)

Stateless domain skill for **Dogecoin payments, address checks, fees, stuck-tx triage, exchange deposits, and merged-mining context**. It does not store keys, seeds, or transaction history in the package.

## When to load

- Send/receive DOGE; verify mainnet addresses that start with `D`
- Unconfirmed or slow payments when the user expects Bitcoin-style RBF
- Exchange deposit compatibility and confirmation policy
- Wallet sync / dust / fee-by-size questions on Dogecoin Core or light wallets
- Scrypt merged-mining context with Litecoin when it affects security narrative

## Core defaults

Keep always-on rules here; load at most one deep `references/` file per step (progressive disclosure).

1. **Classify first** — address check, fee/stuck tx, exchange deposit, wallet sync, or security/scam.
2. **Match the `D` prefix before blaming missing funds** — wrong network or mistyped address is the usual root cause.
3. **Never request seeds or private keys in chat** — guide local wallet UI or hardware on-device verification.
4. **Use wait/explorer recovery for stuck sends** — Dogecoin Core does not expose Bitcoin BIP125 Replace-By-Fee as a user recovery path; wait or ask the sender/venue for policy.
5. **Re-open `references/sources.md`** before restating version-sensitive Core, subsidy, or AuxPoW claims.

## Ordered workflow

1. **Classify** — address, fee/stuck tx, exchange deposit, wallet sync, merged mining, or scam.
2. **Context** — mainnet vs testnet, amount/urgency, wallet type, whether the user is sender or receiver.
3. **Apply minimum viable rules** below; load only the matching reference.
4. **Verify** on a public explorer or venue docs when confirmation status or deposit support is disputed.
5. **Bound** — irreversible sends and seed-phishing attempts get hard stops.

## Minimum viable rules

| Topic | Rule |
| --- | --- |
| Block time | Target ~1 minute (`consensus.nPowTargetSpacing = 60` in Core `chainparams.cpp`) |
| Address (P2PKH) | Mainnet `PUBKEY_ADDRESS` version `30` → addresses typically start with `D` |
| Address (P2SH) | Mainnet `SCRIPT_ADDRESS` version `22` → less common; still verify full string |
| Confirmations | ~1 block ≈ 1 minute; high-value / exchange flows often wait ~6+ blocks—venue policy overrides |
| Fees | Size (bytes/weight) driven, not DOGE amount; most wallets auto-select a relayable fee |
| RBF | Not a Dogecoin user recovery tool like Bitcoin BIP125; stuck sends usually wait |
| Memo/tag | Plain DOGE deposits do **not** use XRPL-style destination tags |
| Merged mining | Scrypt AuxPoW with Litecoin at miner/pool layer—no end-user config to send payments |
| State | Stateless knowledge skill; wallet owner retains signing and custody |

## Failure branches

| Signal | Action |
| --- | --- |
| Address does not start with expected mainnet prefix | Stop send; open `references/addresses.md`; never invent formats |
| Unconfirmed send, user expects RBF | Use explorer + wait path; see `references/fees-and-recovery.md` |
| Exchange no-credit after send | Confirmations + correct asset/network + full `D…` string; ask venue policy |
| Wallet shows zero / slow sync | Full-node sync or light-wallet scan; no seed in chat |
| “Double your DOGE” / fake Elon giveaway / support wants seed | Refuse key requests; verify only with public txid/address |
| Fee, subsidy, or AuxPoW claim is version-sensitive | Re-open Core docs in `references/sources.md` |

## Routing

| Need | Load |
| --- | --- |
| Address prefixes, deposit checks | `references/addresses.md` |
| Fees, confirmations, stuck recovery | `references/fees-and-recovery.md` |
| Network defaults, wallets, merged mining, scams | `references/domain.md` |
| Official sources before restating Core facts | `references/sources.md` |
