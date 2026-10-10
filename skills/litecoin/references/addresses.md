# Litecoin address formats

Use this when validating a deposit address, diagnosing “unsupported address”, or explaining fee differences across script types.

## Mainnet prefixes (from Litecoin Core `chainparams`)

| Type | Core field | Version / HRP | Typical prefix | Notes |
| --- | --- | --- | --- | --- |
| Legacy P2PKH | `PUBKEY_ADDRESS` | base58 version `48` | `L…` | Oldest widely supported format |
| P2SH | `SCRIPT_ADDRESS` | base58 version `5` | `3…` | Same version byte family as Bitcoin P2SH |
| P2SH (Litecoin alternate) | `SCRIPT_ADDRESS2` | base58 version `50` | `M…` | Common nested-SegWit / P2SH style on Litecoin |
| Native SegWit (bech32) | `bech32_hrp` | `ltc` | `ltc1…` | BIP173; usually lowest fees when both sides support SegWit |
| MWEB stealth | `mweb_hrp` | `ltcmweb` | `ltcmweb1…` | Extension-block privacy path only |

Testnet uses different HRPs (`tltc`, `tmweb`) and base58 versions — do not treat testnet strings as mainnet deposits.

## Practical checks

1. Read the **first characters** before any send or exchange whitelist.
2. Confirm the venue’s deposit network is **Litecoin mainnet**, not a wrapped LTC token on another chain.
3. Prefer `ltc1…` when the counterparty and wallet both support native SegWit.
4. Treat `ltcmweb1…` as **MWEB-only**. If the exchange UI shows a normal LTC deposit address (`L` / `M` / `3` / `ltc1`), keep funds on the main chain.
5. Address strings are case-sensitive for base58; bech32 is lowercase canonical.

## Wallet import zero-balance order

1. Ask which wallet created the seed and which receive address type it showed (do not collect the seed).
2. Match the receive address prefix to the table above.
3. Rescan or enable the matching script type / derivation account in a trusted local or hardware wallet.
4. Prefer watch-only / xpub flows over re-entering seeds into new software.

## Exchange deposit pitfalls

- Venues may accept only a subset of main-chain formats; follow the address **they** generated.
- Sending main-chain LTC to an MWEB address (or the reverse) is the wrong layer — recoverability is not guaranteed.
- No memo/destination tag is required for plain LTC (unlike some other networks). If a venue shows an extra memo field for “LTC”, re-read the asset network label before sending.
