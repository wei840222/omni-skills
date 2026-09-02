# Sui network operations

## Object model and ownership

Sui uses objects rather than an account-centric state model. Objects have unique IDs and ownership determines how a transaction accesses and versions them.

- **Address-owned objects** belong to one address and use the fast path; they are suitable for a user's coins, NFTs, and capabilities.
- **Shared objects** can be referenced by any address and use consensus ordering. Move code must perform explicit authorization checks; shared-object access alone does not authorize the caller.
- **Immutable objects** are readable by anyone and cannot be mutated, transferred, or deleted.
- **Wrapped objects** are available only through their parent object.

For shared-object workloads, reduce simultaneous writes to the same object because contention can reduce throughput.

## Transactions and gas

- SUI is the native token used to pay transaction gas. `1 SUI = 10^9 MIST`.
- Inspect the transaction's current gas budget, price, payment coin, and simulation or dry-run result instead of assuming a fixed fee or reference gas price.
- Sui transactions are atomic: a failed transaction does not apply only part of its intended state transition. Inspect the effects and error details before rebuilding a transaction.
- A sponsored transaction uses a separate gas owner. Confirm the sender, gas owner, transaction kind, and all requested object changes before signing.

### Common transaction failures

| Symptom | First action | Recovery |
| --- | --- | --- |
| Insufficient gas or balance | Inspect the selected gas coin, gas budget, and SUI balance. | Fund or select an adequate gas coin, then rebuild and re-sign the transaction. |
| Object not found, version mismatch, or object already used | Confirm the network, object ID, object version, and whether another transaction consumed or transferred it. | Fetch current object data; rebuild the transaction against the current object state. |
| Move abort or permission error | Retrieve the dry-run or execution error and identify the package, module, and function. | Correct the arguments or authorization condition, then dry-run the updated transaction before submission. |
| Fragmented SUI coins | Inspect owned coin objects and wallet behavior. | Merge or split coins only when the intended transaction needs a particular coin layout; verify the resulting coin objects. |

## Staking

Sui uses delegated proof of stake. SUI holders may delegate to validators, and stake changes take effect at epoch boundaries.

- Check the validator's current commission, performance, and the wallet's current staking flow before delegating.
- Treat unstaking or redelegation as an epoch-bound operation; confirm the wallet's stated activation or withdrawal epoch.
- Query current network or wallet data for epoch duration, reward rate, minimum stake, and validator availability; treat those values as mutable rather than permanent protocol constants.

## Move and packages

Sui smart contracts use Move and model assets as resources and objects. Before publishing, upgrading, or calling a package:

1. Confirm the active network, package ID, module, function, type arguments, and object IDs.
2. Dry-run or simulate the transaction when the tool supports it.
3. Review every changed, received, or deleted object and every transfer recipient.
4. Publish or sign only after the expected effects match the request.

Package upgrade behavior and compatibility policy are package-specific. Read the current package and network documentation before an upgrade rather than assuming an earlier package remains callable in the same way.

## Wallet, DeFi, NFT, and bridge safety

- Verify the connected network, package ID, recipient, token type, amount, and transaction effects in the wallet confirmation.
- A wallet confirmation authorizes a request but does not establish that it is safe. Keep recovery phrases and private keys offline; enter secrets only through the wallet or key-management flow you have independently verified.
- Treat DEX, NFT marketplace, bridge, and wrapped-asset package IDs as network-specific. Obtain them from the project's official documentation and inspect the transaction before signing.
- A bridge transfer creates or handles representations governed by the bridge; verify the official bridge, source and destination network, asset type, and recipient before proceeding.

For time-sensitive protocol behavior, load `references/sources.md` and use the linked primary documentation.
