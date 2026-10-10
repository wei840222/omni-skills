# MWEB (MimbleWimble Extension Block)

MWEB is Litecoin’s **optional** privacy path: MimbleWimble transactions inside extension blocks that run alongside canonical blocks (LIP-0002 / LIP-0003 / LIP-0004). It is not the default wallet send path and is not a drop-in Lightning substitute.

## Mental model

1. **Main chain** — ordinary transparent LTC UTXOs and addresses (`L` / `M` / `3` / `ltc1`).
2. **Extension block (EB)** — MW transaction graph with cut-through; amounts and counterparties are confidential inside MWEB.
3. **Peg-in** — move value from main chain into the EB (integrating / HogEx path).
4. **Peg-out** — move value from the EB back to a main-chain address.
5. **Stealth addresses** — MWEB receives via dual-key stealth addresses (HRP `ltcmweb` on mainnet).

Old nodes that do not understand MWEB still see peg-in coins locked in the integrating anyone-can-spend construct; they do not validate the EB MW graph.

## Address and deposit rules

- Mainnet MWEB HRP: **`ltcmweb`** (Core `mweb_hrp`). Receiving addresses appear as `ltcmweb1…`.
- Before any exchange deposit: confirm the venue **explicitly** supports MWEB deposits.
- If support is missing or unclear → **peg-out to main chain first**, then deposit to the venue’s normal LTC address.
- Sending MWEB value to a main-chain-only deposit address (or the reverse) is a common loss path.

## What MWEB does and does not do

| Does | Does not |
| --- | --- |
| Optional confidential amounts and MW-style cut-through inside the EB | Make every LTC payment private by default |
| Peg-in / peg-out bridges to canonical LTC | Replace main-chain SegWit address best practices |
| Stealth-address receive path on MWEB | Provide Bitcoin-style Script / Lightning BOLT compatibility inside MW |
| Soft-fork style deployment via extension blocks | Guarantee exchange, custodian, or tax-tool support |

## User guidance checklist

1. Ask whether funds are currently **main-chain or MWEB**.
2. Ask whether the destination is a **self-custody wallet** or a **custodial deposit**.
3. For custodial deposits without documented MWEB support → require peg-out first.
4. For self-custody MWEB receives → use a wallet that implements current Litecoin Core MWEB stealth-address rules.
5. Re-open LIP-0003 and Core `doc/mweb/` notes before asserting kernel, weight, or light-client details.

## Security notes

- Privacy is **opt-in**. Transparent main-chain history remains linkable with ordinary chain analysis.
- Peg paths and integrating transactions are consensus-critical; prefer current Litecoin Core releases for MWEB validation fixes (see recent Core release notes).
- Never request scan/spend keys or seeds. Stealth-address scan keys are as sensitive as account credentials.
