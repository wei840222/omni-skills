# Dogecoin domain defaults

## Network parameters (consensus-oriented)

| Parameter | Value | Source anchor |
| --- | --- | --- |
| Block target spacing | 1 minute | `consensus.nPowTargetSpacing = 60` in Core `chainparams.cpp` |
| Coinbase maturity | 30 blocks | `consensus.nCoinbaseMaturity = 30` |
| Proof of work | Scrypt | Project documentation / mining ecosystem |
| AuxPoW / merge-mining | Supported (Litecoin ecosystem) | Core AuxPoW parameters (`nAuxpowChainId`, etc.) |
| Mainnet P2PKH version | `30` → `D…` | `base58Prefixes[PUBKEY_ADDRESS]` |
| Default P2P port | `22556` | Core `chainparams.cpp` |

Supply continues without a hard end-user “cap” narrative for ordinary payments; treat marketing slogans as non-normative and re-check Foundation/Core docs before quoting issuance figures.

## Wallet orientation (non-exhaustive)

Prefer software the user already trusts and can verify:

- **Dogecoin Core** — full node; strongest validation; large initial sync.
- **Hardware wallets** with official DOGE apps — on-device address verification.
- **Light / multi-asset wallets** — faster UX; confirm which address types are actually implemented before relying on them.
- Prefer local or hardware custody over leaving large balances on exchanges or web wallets.

Always download from vendor-official channels; never from unsolicited DM links.

## Merged mining with Litecoin

- Dogecoin is commonly merge-mined with Litecoin on Scrypt, sharing miner work (AuxPoW).
- This is a **miner/pool** concern; end users do not configure merged mining to send payments.
- Security narratives may reference combined work, but users still verify payments on the Dogecoin chain they actually use.

## Security defaults

- Seed / xprv never in chat; never in skill state files (this skill is stateless).
- Verify full destination strings on device screens; clipboard malware swaps middle characters.
- Reject “double your DOGE”, cold-DM “support”, and fake celebrity giveaways that request keys.
- Dust unsolicited receipts: avoid consolidating with primary UTXOs without a privacy plan.
- Irreversible sends: triple-check network + address prefix + venue name before broadcast.

## Common issue → first response

| Issue | First response |
| --- | --- |
| Unconfirmed payment | Explorer check → no RBF expectation → wait policy (`fees-and-recovery.md`) |
| Exchange no-credit | Confirmations + correct asset/network + full `D…` address |
| Zero balance after import | Address type / sync (`addresses.md`); no seed collection |
| “Can I RBF like Bitcoin?” | No Dogecoin BIP125 user path; wait or rebuild carefully |
| “Is DOGE the same as LTC?” | Shared Scrypt/merge-mining ancestry; different ports, prefixes, spacing, and product scope |
