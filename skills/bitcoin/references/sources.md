# Research sources (Gate 6)

Verified public references used for fee, path, Lightning, and explorer guidance.

## Fee and mempool

- mempool.space recommended fees API — live sat/vB guidance via https://mempool.space/api/v1/fees/recommended
- mempool.space transaction API — confirmation and fee inspection via https://mempool.space/api/tx/{txid}
- mempool.space address API — funded/spent totals via https://mempool.space/api/address/{address}
- mempool.space docs / explorer UI — operator-facing fee and confirmation concepts via https://mempool.space/docs/api/rest

## Wallet standards

- BIP44 multi-account hierarchy — legacy path convention via https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki
- BIP84 native segwit derivation — `bc1q` path convention via https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki
- BIP86 taproot derivation — `bc1p` path convention via https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki
- BIP125 opt-in full replace-by-fee — RBF signaling rules via https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki

## Lightning

- BOLT #11 invoice format / expiry behavior overview via https://github.com/lightning/bolts/blob/master/11-payment-encoding.md
- Lightning inbound liquidity conceptual guidance (operator docs vary by implementation; keep advice implementation-agnostic)

## Security

- Prefer hardware-wallet on-device address verification and never request seed phrases in chat.
- Treat unsolicited "recovery" or "support" DMs that request seeds as theft attempts.
