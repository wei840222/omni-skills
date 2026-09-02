# Primary sources for Sui operational claims

Use these sources to verify time-sensitive network behavior, package interfaces, or security guidance before making a transaction decision.

| Topic | Source | Applied guidance |
| --- | --- | --- |
| Object ownership | [Sui: Types of Object Ownership](https://docs.sui.io/develop/objects/object-ownership) | Ownership controls transaction access and versioning; shared objects require explicit Move-layer authorization. |
| Gas | [Sui: Gas in Sui](https://docs.sui.io/develop/transaction-payment/gas-in-sui) | Query current gas information rather than embedding fixed operational fees or a reference price. |
| Tokenomics and staking | [Sui: Tokenomics on Sui](https://docs.sui.io/develop/sui-architecture/tokenomics-overview) | SUI is used for gas and delegated staking; stake changes occur at epoch boundaries. |
| Move packages | [Sui: Writing Move Packages](https://docs.sui.io/develop/write-move) | Confirm the current package-development workflow and interfaces before package operations. |
| Security | [Sui: Security Best Practices](https://docs.sui.io/develop/security/best-practices) | Validate authorization and transaction effects before irreversible operations. |
