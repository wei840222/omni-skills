# Network services and environments

## Environments

| Network | Use |
| --- | --- |
| Mainnet | Production value, real HBAR, real finality. |
| Testnet | Development with free test HBAR from the portal/faucet; fees mirror mainnet economically but tokens are worthless. |
| Previewnet | Early-access features; expect instability and possible state loss on upgrades. |

## Consensus and history

- Hashgraph consensus provides fast finality; public docs commonly describe absolute finality in about 3–5 seconds for typical transactions.
- Mirror nodes store historical records and offer REST APIs for transactions, balances, and token data. Query mirror nodes for history instead of overloading consensus nodes.
- Example public mainnet mirror base: `https://mainnet.mirrornode.hedera.com/` (testnet/previewnet have matching hosts).

## Other services

- **Hedera Consensus Service (HCS)** — ordered, timestamped message logging for applications that need consensus timestamps without embedding business state in HBAR transfers.
- **Hedera File Service (HFS)** — network file storage often used for contract bytecode and configuration blobs; large contract deploys may need chunked file upload before create.
- **Smart contracts** — EVM-compatible contracts with Hedera-specific account/key and HTS system-contract behaviors. Rent / expiry semantics can apply to contract state; check current smart-contract docs before long-lived storage assumptions.
