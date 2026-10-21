# Hedera accounts and keys

## Account model

- A Hedera account is a ledger entity that can hold HBAR and HTS tokens. Account IDs look like `0.0.12345`, not Ethereum-style hashes.
- Network balances and many APIs report tinybars (`tℏ`); `100_000_000 tℏ = 1 ℏ (HBAR)`.
- New accounts are normally created with an `AccountCreateTransaction` paid by an existing funded account. Wallets and exchanges often create the account for the user on first funding/withdrawal.
- Auto Account Creation / hollow accounts can create an account when value is first sent to an alias or EVM address derived from a public key. A hollow account can receive funds but cannot send or change properties until the matching key completes the account.

## Keys

- Supported key types include Ed25519 and ECDSA (`secp256k1`). Current docs recommend ECDSA for new accounts that need EVM compatibility.
- For EVM-friendly accounts, set an EVM address alias derived from the ECDSA public key at creation (`setECDSAKeyWithAlias` / equivalent). That alias is bound to the original key material.
- Accounts can use threshold / multi-key setups. Rotate keys with an account update signed by the current key; do not assume lost keys are recoverable without a seed phrase the user already controls.

## Delete and migration

- `AccountDeleteTransaction` transfers remaining HBAR to a beneficiary account. The account being deleted must sign; custom tokens and associations must be cleared first per current delete rules.
- When migrating, move or dissolve token associations, then delete the old account to sweep remaining HBAR to the new beneficiary.
