# Sources for Hedera operational claims

Use these primary sources when validating account, token, fee, staking, or network claims. Prefer the live page over memorized constants.

| Topic | Source | Applied guidance |
| --- | --- | --- |
| Account model | [Accounts](https://docs.hedera.com/learn/core-concepts/accounts) | Accounts hold HBAR/HTS balances; creation is a paid network transaction unless using documented auto-create paths. |
| Account creation SDK | [Create an account](https://docs.hedera.com/native/accounts/create) | `AccountCreateTransaction` must be paid/signed by an existing account; ECDSA + EVM alias helpers exist. |
| Account properties / staking fields | [Account properties](https://docs.hedera.com/learn/core-concepts/accounts/account-properties) | Memos are public; staking targets, decline-reward, and pending reward fields are first-class account properties. |
| Account delete | [Delete an account](https://docs.hedera.com/native/accounts/delete) | Deleting transfers remaining HBAR to a beneficiary; the deleted account must sign. |
| Keys | [Keys and signatures](https://docs.hedera.com/learn/core-concepts/keys) | ECDSA recommended for new EVM-compatible accounts; aliases bind to key material. |
| Tokenization models | [Tokenization on Hedera](https://docs.hedera.com/learn/core-concepts/tokens) | HTS native, ERC/EVM, and hybrid models; fees are USD-denominated and paid in HBAR. |
| Token association | [Associate tokens](https://docs.hedera.com/native/tokens/associate) | Accounts must associate before receiving custom HTS tokens; documents concrete association error codes. |
| Network fees | [Fees](https://docs.hedera.com/networks/fees) | Base fee + extras; same schedule shape on mainnet/testnet; use Fee Estimator for live HBAR amounts. |
| Staking overview | [Staking](https://docs.hedera.com/learn/core-concepts/staking) | Proof-of-stake influence; FAQ text states no lock-up and liquid balances while staked. |
| Networks | [Networks](https://docs.hedera.com/networks) | Mainnet / testnet / localnet (and portal docs for previewnet) environment split. |
| Getting started / previewnet | [Getting started FAQ](https://docs.hedera.com/support/faq/getting-started) | Portal creates testnet/previewnet accounts; previewnet can lose state on upgrades. |
| Hashgraph consensus | [Hashgraph](https://docs.hedera.com/learn/core-concepts/hashgraph) | Fast certainty of ordering versus probabilistic chain tips. |
| Product overview / finality | [What is Hedera](https://docs.hedera.com/learn/getting-started/what-is-hedera) | Public PoS hashgraph ledger; docs cite ~3–5s finality and ~$0.0001 average fee order-of-magnitude. |
| Smart contracts | [Smart contracts](https://docs.hedera.com/learn/core-concepts/services/smart-contracts) | EVM differences, HTS system contracts, rent topics. |
| Gas and fees | [Gas and fees](https://docs.hedera.com/evm/development/gas-fees) | Intrinsic + opcode + system-contract gas; fees paid in HBAR denominations. |
| Mirror Node REST | [Mirror Node REST API](https://docs.hedera.com/reference/rest-api) | Historical queries via mainnet/testnet/previewnet mirror hosts. |
