---
name: monero
description: >
  Explain Monero (XMR) privacy defaults, addresses, wallets, nodes, payment
  proofs, mining/P2Pool choices, and common sync or unlock failures. Use for
  RingCT/ring-signature/stealth-address questions, subaddress vs integrated
  address routing, view-key audit limits, remote-node privacy trade-offs, or
  download verification. Prefer `bitcoin` for UTXO/Lightning fee recovery,
  `ethereum` for EVM gas/approvals/L2 bridges, `crypto-tools` for market/explorer
  lookups, `payments` for fiat PSP checkout, and `cybersecurity` for broader
  incident response beyond Monero wallet ops.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔒"}'
  related-skills: '{"bitcoin":"Bitcoin UTXO, fee, RBF/CPFP, and Lightning recovery instead of Monero privacy defaults.","ethereum":"EVM gas, approvals, and L2 bridges instead of Monero ring/stealth flows.","crypto-tools":"Market data, explorers, and generic crypto tooling once Monero mechanics are settled.","payments":"Fiat PSP checkout and webhook-first commerce rather than XMR wallet privacy.","cybersecurity":"Broader defensive incident response when the ask is not Monero-specific."}'
---

# Monero

Assist with **Monero-native privacy and wallet operations**: default-private
transactions, address types, wallet/node choices, payment proofs, mining path
selection, and sync/unlock troubleshooting. This skill is **stateless** and does
not store local configuration, seed phrases, view keys, or payment proofs.

## When to load

Load for Monero / XMR questions such as:

- why sender, receiver, and amount stay hidden by default
- standard vs subaddress vs integrated address choice
- GUI / CLI / Feather / Cake / hardware-wallet selection
- own-node vs remote-node privacy trade-offs
- proving a payment without exposing a seed
- solo / pool / P2Pool mining orientation
- "wallet not synced", zero balance while scanning, or unexpected unlock waits

Route away when another skill owns the job:

| Job | Skill |
|-----|-------|
| Bitcoin fees, RBF/CPFP, Lightning | `bitcoin` |
| EVM gas, approvals, L2 bridges | `ethereum` |
| Prices, generic explorers, market screens | `crypto-tools` |
| Fiat PSP checkout / webhooks | `payments` |
| Non-Monero incident response | `cybersecurity` |

## Operating path

1. Identify the ask branch: privacy model, address/payment ID, wallet/node,
   proof, mining, or troubleshooting.
2. Load only the matching reference below; keep seed phrases, spend keys, and
   live payment proofs out of chat logs whenever a safer local path exists.
3. For mutable claims (exchange listings, exact USD fees, software versions,
   hardware-wallet matrix), open `references/sources.md` and re-check the live
   official page before stating them as current.
4. Prefer official downloads from getmonero.org (and documented companion
   wallets); verify archive hashes before install advice becomes actionable.

## Progressive disclosure

Keep `SKILL.md` as the entry point; open only the reference that matches the active branch.

| Reference | Load when |
|---|---|
| `references/domain.md` | Privacy primitives, address types, view/spend keys, payment proofs, safety defaults |
| `references/wallets-and-nodes.md` | GUI/CLI/Feather/Cake choice, own-node vs remote node, Tor/I2P notes |
| `references/mining.md` | RandomX orientation, solo vs pool vs P2Pool |
| `references/troubleshooting.md` | Sync, scanning, unlock, daemon, and stuck-tx recovery order |
| `references/sources.md` | Official URLs for live verification |

## Hard boundaries

- Keep seed phrases, spend keys, and unrestricted wallet passwords on local
  secure channels; chat stays limited to non-secret operational guidance.
- Treat shared view keys as incoming-audit capability only; outgoing history and
  balances from a view key alone are not reliable settlement evidence.
- Prefer subaddresses for services and new integrations; long standalone payment
  IDs are deprecated legacy paths.
- Design around ordinary wallet maturity displays; custom transaction
  `unlock_time` is rare, public on-chain, and headed toward deprecation.
