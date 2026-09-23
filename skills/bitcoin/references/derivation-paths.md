# Bitcoin derivation paths and address prefixes

Use this when a seed import shows zero balance or the user is unsure which address type their wallet used.

## Common paths

| Address style | Typical path | Address prefix examples |
|---------------|--------------|-------------------------|
| Legacy P2PKH | BIP44 `m/44'/0'/0'` | starts with `1` |
| Nested SegWit P2SH-P2WPKH | BIP49 `m/49'/0'/0'` | starts with `3` |
| Native SegWit P2WPKH | BIP84 `m/84'/0'/0'` | starts with `bc1q` |
| Taproot P2TR | BIP86 `m/86'/0'/0'` | starts with `bc1p` |

## Troubleshooting order

1. Ask which wallet originally created the seed and which address type it displayed.
2. Match the receiving address prefix before declaring funds missing.
3. Prefer watch-only / xpub import over re-entering the seed into untrusted software.
4. If an exchange rejects `bc1p`, request a `bc1q` or legacy deposit address from the exchange docs.

## Notes

- The same mnemonic can control multiple script types; scanning only one path hides the others.
- Do not ask the user to paste a seed into chat. Guide local wallet UI or hardware verification instead.
