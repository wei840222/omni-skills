# Research sources (Gate 6)

Verified public references used for Dogecoin address, timing, AuxPoW, and custody guidance.

## Core and consensus

- Dogecoin Core repository — primary implementation via https://github.com/dogecoin/dogecoin
- Dogecoin Core `chainparams.cpp` (raw) — `nPowTargetSpacing = 60`, `PUBKEY_ADDRESS` version `30`, AuxPoW parameters via https://raw.githubusercontent.com/dogecoin/dogecoin/master/src/chainparams.cpp
- Dogecoin Core `doc/README.md` — developer documentation index via https://raw.githubusercontent.com/dogecoin/dogecoin/master/doc/README.md
- Agent Skills specification — package format rules via https://agentskills.io/specification

## Project / foundation orientation

- Dogecoin project site — community and wallet orientation via https://dogecoin.com/
- Dogecoin Foundation — stewardship and trailmap context via https://foundation.dogecoin.com/
- Dogecoin Foundation about — organizational context via https://foundation.dogecoin.com/about/

## Related-chain contrast (routing only)

- Litecoin skill in this repo — Scrypt merged-mining peer guidance via `skills/litecoin/SKILL.md`
- Bitcoin skill in this repo — BIP125 RBF contrast via `skills/bitcoin/SKILL.md`
- XRP skill in this repo — destination-tag contrast via `skills/xrp/SKILL.md`

## Security posture

- Prefer hardware-wallet on-device address verification and never request seed phrases in chat.
- Treat unsolicited “recovery”, “support”, or “double your DOGE” DMs that request seeds as theft attempts.
