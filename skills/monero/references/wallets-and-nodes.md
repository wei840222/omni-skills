# Wallets and nodes

Load when choosing a wallet UI or deciding whether to run `monerod`.

## Wallet orientation

| Option | Fit |
|---|---|
| Official Monero GUI | Full desktop path with bundled node/wallet tooling and a PDF guide in the download tree |
| Official Monero CLI (`monero-wallet-cli`) | Scripting, power-user transfers, integrated-address helpers, proofs |
| Feather Wallet | Lightweight open-source desktop wallet for Linux/Tails/Windows/macOS; beginner-friendly with advanced features and threat-model toggles |
| Cake Wallet | Mobile-first non-custodial multi-asset wallet with first-class Monero support; verify current app store / release channel before install advice |
| Hardware wallets | Support matrices change; confirm the live official hardware guide before promising a device path |

Official docs separate **node logic** (`monerod`) from **wallet logic** (GUI, CLI, wallet RPC). After unpacking a GUI release you typically see `monerod`, `monero-wallet-gui`, and extras such as `monero-wallet-cli` / `monero-wallet-rpc`.

## Own node vs remote node

- **Own node** — maximum query privacy; you do not leak wallet block-scan patterns to a third party. Initial sync can take hours to days depending on hardware and whether the chain is pruned.
- **Remote node** — convenient, but the remote operator can observe your IP and which outputs your wallet queries. Prefer Tor/I2P when a remote node is unavoidable.
- **Pruned nodes** — reduce disk use while remaining useful for many wallet and P2Pool setups; confirm prune flags against current `monerod` docs.

Official running-node docs cover config files, systemd service units, and Tor/I2P. Point users there rather than inventing flag sets from memory when exact CLI syntax matters.

## Operational hygiene

1. Download from the official Downloads page and verify published hashes.
2. Decide whether the wallet will talk to a local `monerod`, a trusted remote node, or an anonymity network fronted remote.
3. Create receives with subaddresses when the counterparty workflow allows it.
4. Keep seed / spend material offline; use view-only wallets only with the audit limits described in `domain.md`.
