---
name: bitcoin
description: >
  Diagnose Bitcoin transactions, wallet derivation mismatches, fee strategies,
  Lightning gotchas, and on-chain security risks. Load when troubleshooting
  stuck txs, zero-balance imports, RBF/CPFP recovery, Lightning liquidity, or
  scam patterns. Not for custodial account recovery that requires seed phrases.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "₿"}'
  related-skills: '{"ethereum":"Handle EVM gas, approvals, and L2 bridges instead of Bitcoin UTXO/Lightning flows.","xrp":"Handle XRPL reserves, destination tags, and native DEX instead of Bitcoin fees/UTXOs.","blockchain":"Cover general ledger fundamentals beyond Bitcoin-specific wallet and fee recovery.","crypto-tools":"Fetch market data and exchange tooling once Bitcoin transaction mechanics are settled."}'
---

## When to load

Load this skill when the user needs help with Bitcoin transaction diagnosis, wallet compatibility, fee timing, stuck-tx recovery (RBF/CPFP), Lightning Network limits, privacy pitfalls, scam recognition, or mempool.space verification APIs.

## Wallet Compatibility Traps

- Same seed phrase in different wallets can show zero balance — derivation paths differ (BIP44 for legacy, BIP84 for native segwit, BIP86 for taproot). Ask which wallet created the seed before troubleshooting "missing funds".
- Importing a seed into a watch-only wallet fails to show funds if the wallet defaults to a different address type than the original.
- Some exchanges still reject `bc1p` (taproot) addresses for withdrawals — verify before giving the user a taproot address.
- See `references/derivation-paths.md` for path and address-prefix quick checks.

## Fee Timing

- Bitcoin fees follow predictable patterns: weekends and UTC night hours (00:00–06:00) are typically 50–80% cheaper than weekday peaks.
- `https://mempool.space/api/v1/fees/recommended` gives current sat/vB rates — wallet built-in estimates are often 12–24 hours stale.
- A transaction at 1 sat/vB during high congestion can stay unconfirmed for 2+ weeks, but will eventually drop from mempools (not fail, just disappear).
- See `references/fees-and-recovery.md` for RBF/CPFP decision order.

## Stuck Transaction Recovery

- **RBF (Replace-By-Fee):** sender broadcasts a new tx with higher fee — only works if the original was flagged replaceable (most modern wallets do this by default).
- **CPFP (Child-Pays-For-Parent):** receiver creates a high-fee tx spending the unconfirmed output, incentivizing miners to confirm both — useful when the sender did not enable RBF.
- If the user is the receiver and the stuck tx has no change/output they control, CPFP is impossible — they must wait or ask the sender to RBF.

## Lightning Network Gotchas

- Lightning invoices expire (default ~1 hour on many wallets) — an expired invoice cannot receive payment even if the payer retries.
- Inbound liquidity limits how much a user can receive — a fresh channel can send but not receive until the balance shifts.
- Closing a channel during high on-chain fees can cost more than the channel balance — warn users before force-closing small channels.
- Lightning payments are not automatically retried — if a route fails, the user must manually retry or the payment fails permanently.

## Privacy and Security Patterns

- Dust attacks: tiny amounts sent to addresses to link them when the user spends — advise not to consolidate dust with main UTXOs.
- Address reuse lets anyone see the full transaction history of that address — each receive should use a fresh address.
- Clipboard malware silently replaces copied addresses — always verify the first and last 6 characters match on both devices before confirming send.
- Hardware wallet "verify on device" is critical — if malware changed the address, only the device screen shows the real destination.

## Scam Recognition

- "Send X BTC, receive 2X back" is always a scam — no exceptions, even if the account looks official.
- "Recovery services" that ask for a seed phrase will steal everything — legitimate recovery only requires public information or a watch-only setup.
- Fake wallet apps in app stores with slight name variations — verify publisher and download count before recommending.
- "Support" DMing users on social media asking to "validate wallet" or "sync" — real support only responds to user-initiated requests.

## Verification APIs

- mempool.space is the current standard block explorer — blockchain.info is outdated and less reliable for fee data.
- Confirmed = included in a block. 1 confirmation is minimum, 6 is standard for high-value; some exchanges require 3.
- Raw tx: `curl -s "https://mempool.space/api/tx/{txid}"` — fee, size, confirmation status.
- Address balance: `curl -s "https://mempool.space/api/address/{address}"` — funded/spent totals.
- Source notes: `references/sources.md`.
