# Research sources (Gate 6)

Retrieval window for this refactor: **2026-10-11**. Re-open these pages before restating version-sensitive Core, address, or MWEB claims.

## Agent Skills package format

- **Agent Skills specification** — frontmatter and resource layout via https://agentskills.io/specification
- **Document index** — https://agentskills.io/llms.txt
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Litecoin Core and parameters

- **Litecoin Core repository** — integration tree and docs via https://github.com/litecoin-project/litecoin
- **Project README** — overview and https://litecoin.org pointer via https://raw.githubusercontent.com/litecoin-project/litecoin/master/README.md
- **Official site** — binaries and project entry via https://litecoin.org/
- **chainparams.cpp** — block spacing, halving interval, base58 versions, `bech32_hrp`, `mweb_hrp`, MWEB deployments via https://raw.githubusercontent.com/litecoin-project/litecoin/master/src/chainparams.cpp
- **amount.h** — `COIN` and `MAX_MONEY` (84 million LTC) via https://raw.githubusercontent.com/litecoin-project/litecoin/master/src/amount.h
- **descriptors.md** — bech32 `ltc1…` / `tltc1…` notes via https://raw.githubusercontent.com/litecoin-project/litecoin/master/doc/descriptors.md
- **bips.md** — implemented BIPs plus LIP-0002/0003/0004 MWEB references via https://raw.githubusercontent.com/litecoin-project/litecoin/master/doc/bips.md
- **release-notes-litecoin.md** — current Core maintenance focus including MWEB validation/relay via https://raw.githubusercontent.com/litecoin-project/litecoin/master/doc/release-notes-litecoin.md

## MWEB / LIPs

- **LIP-0002** — extension blocks mechanism via https://github.com/litecoin-project/lips/blob/master/lip-0002.mediawiki
- **LIP-0003** — opt-in MimbleWimble via extension blocks (peg-in/out model) via https://github.com/litecoin-project/lips/blob/master/lip-0003.mediawiki
- **LIP-0004** — one-sided MW transactions via https://github.com/litecoin-project/lips/blob/master/lip-0004.mediawiki
- **MWEB stealth addresses** — DKSAP receive path via https://raw.githubusercontent.com/litecoin-project/litecoin/master/doc/mweb/stealth-addresses.md
- **MWEB consensus notes** — kernels/outputs orientation via https://raw.githubusercontent.com/litecoin-project/litecoin/master/doc/mweb/consensus.md
- **MWEB doc directory** — additional mining/light-client notes via https://github.com/litecoin-project/litecoin/tree/master/doc/mweb

## Shared Bitcoin standards used by Litecoin tooling

- **BIP173** — bech32 address format via https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
- **BIP125** — opt-in full replace-by-fee via https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki
- **BIP141/143/144** — segregated witness family (see Core `bips.md` for Litecoin activation notes)

## Fragile claims

- Do not quote live USD fee levels; fees are weight-driven and mempool-dependent.
- Do not claim all exchanges support MWEB or every address type.
- Do not treat MWEB as default privacy or as Lightning-compatible Script.
- Do not invent address prefixes; re-check `chainparams` version bytes and HRPs.
- Base58 version `50` → `M…` is Litecoin-specific alternate P2SH (`SCRIPT_ADDRESS2`); do not assume Bitcoin-only `3…` P2SH pedagogy covers Litecoin deposits.
