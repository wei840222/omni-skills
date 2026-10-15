# Sources — Monero skill

Last bulk-checked: 2026-10-15 (handoff). Re-open live pages before restating
software versions, exchange listings, USD fee ranges, or hardware-wallet matrices.

## Project overview and privacy primitives

- What is Monero — https://www.getmonero.org/get-started/what-is-monero/
- About Monero — https://www.getmonero.org/resources/about/
- Moneropedia index — https://www.getmonero.org/resources/moneropedia/
- Ring signatures — https://www.getmonero.org/resources/moneropedia/ringsignatures.html
- Stealth addresses — https://www.getmonero.org/resources/moneropedia/stealthaddress.html
- RingCT — https://www.getmonero.org/resources/moneropedia/ringCT.html
- View key — https://www.getmonero.org/resources/moneropedia/viewkey.html
- Address — https://www.getmonero.org/resources/moneropedia/address.html
- Payment ID — https://www.getmonero.org/resources/moneropedia/paymentid.html
- Unlock time (deprecated trajectory) — https://www.getmonero.org/resources/moneropedia/unlocktime.html
- RingCT paper (Shen Noether) — https://eprint.iacr.org/2015/1098

## Downloads, docs, and node ops

- Official downloads — https://www.getmonero.org/downloads/
- Monero Docs home — https://docs.getmonero.org/
- Interacting overview — https://docs.getmonero.org/interacting/overview/
- Running a node — https://docs.getmonero.org/running-node/
- User guides index — https://www.getmonero.org/resources/user-guides/
- Prove payment — https://www.getmonero.org/resources/user-guides/prove-payment.html
- Remote node GUI guide — https://www.getmonero.org/resources/user-guides/remote_node_gui.html
- monero-wallet-rpc reference — https://docs.getmonero.org/interacting/monero-wallet-rpc-reference/
- Monero GitHub — https://github.com/monero-project/monero

## Payment ID / unlock policy notes

- Long Payment ID deprecation notice — https://www.getmonero.org/2019/06/04/Long-Payment-ID-Deprecation.html
- Deprecating custom unlock time (FCMP++ trajectory) — https://getmonero.org/2026/05/10/deprecating-unlock-time.html

## Wallets and mining companions

- Feather Wallet — https://featherwallet.org/
- Feather docs — https://docs.featherwallet.org/
- Cake Wallet — https://cakewallet.com/
- Mining get-started — https://www.getmonero.org/get-started/mining/
- P2Pool site — https://p2pool.io/
- P2Pool release announcement — https://www.getmonero.org/2021/10/05/p2pool-released.html
- P2Pool GitHub — https://github.com/SChernykh/p2pool
- Mining pool stats (informational) — https://miningpoolstats.stream/monero

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Best practices — https://agentskills.io/skill-creation/best-practices
- Optimizing descriptions — https://agentskills.io/skill-creation/optimizing-descriptions
- llms.txt — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Claim handling

| Claim class | Handling |
|---|---|
| Ring signature / stealth / RingCT mechanics | Stable domain from Moneropedia; cite pages above |
| Address lengths / prefixes | Stable from Address Moneropedia; still verify wallet UI labels |
| Long payment IDs | Deprecated — steer to subaddresses |
| Custom unlock_time | Rare + deprecated trajectory — do not design on it |
| Feather/Cake/P2Pool version floors | Time-sensitive — re-open vendor pages |
| Exchange listings / USD fees | Time-sensitive — never freeze in skill prose |
| Hardware-wallet support | Version-sensitive — confirm official guide live |
