# Dogecoin address formats

Use this when validating a deposit address, diagnosing “unsupported address”, or explaining why funds did not appear after a send.

## Mainnet prefixes (from Dogecoin Core `chainparams`)

| Type | Core field | Version | Typical prefix | Notes |
| --- | --- | --- | --- | --- |
| Legacy P2PKH | `PUBKEY_ADDRESS` | base58 version `30` | `D…` | Dominant mainnet receive format |
| P2SH | `SCRIPT_ADDRESS` | base58 version `22` | less common | Still verify the full string before send |

Testnet uses different base58 versions — do not treat testnet strings as mainnet deposits.

## Practical checks

1. Read the **first character** before any send or exchange whitelist (`D` for typical mainnet P2PKH).
2. Confirm the venue’s deposit network is **Dogecoin mainnet**, not a wrapped DOGE token on another chain.
3. Address strings are case-sensitive for base58; copy/paste errors mid-string lose funds permanently.
4. Dogecoin does **not** require an XRPL-style destination tag/memo for plain DOGE. If a venue shows an extra memo field for “DOGE”, re-read the asset network label before sending.
5. Prefer hardware or local wallet on-device confirmation of the full destination string.

## Wallet import zero-balance order

1. Ask which wallet created the seed and which receive address it showed (do not collect the seed).
2. Match the receive address prefix to the table above.
3. Rescan or finish sync in a trusted local or hardware wallet.
4. Prefer watch-only / xpub flows over re-entering seeds into new software.

## Exchange deposit pitfalls

- Venues may require a minimum confirmation count (often on the order of 6–20 blocks)—follow **their** published policy.
- Sending DOGE to a Bitcoin/Litecoin/EVM address (or the reverse) is the wrong network — recoverability is not guaranteed.
- No memo/destination tag is required for plain DOGE. Extra tag fields usually mean the UI is for another asset.
