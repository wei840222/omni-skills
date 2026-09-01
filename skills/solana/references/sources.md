# Sources for Solana operational claims

Use these primary sources when validating a time-sensitive cluster value or SDK-specific behavior.

| Topic | Source | Applied guidance |
| --- | --- | --- |
| Transaction fees and prioritization | [Solana: Transaction Fees](https://solana.com/docs/core/fees) | Fees and prioritization depend on the transaction and current cluster conditions; compute-budget instructions control prioritization fees. |
| Transaction lifecycle | [Solana: Transactions](https://solana.com/docs/core/transactions) | Transactions use recent blockhashes and are signed messages submitted to the cluster. |
| Confirmation and expiry | [Solana: Transaction Confirmation & Expiration](https://solana.com/docs/advanced/confirmation) | A recent blockhash has a limited validity window; expired transactions require reconstruction with a fresh blockhash. |
| Token accounts | [Solana: Create a Token Account](https://solana.com/docs/tokens/basics/create-token-account) | Token balances reside in token accounts; an ATA is the standard account derived for an owner and mint. |
| Rent-exemption query | [Solana RPC: getMinimumBalanceForRentExemption](https://solana.com/docs/rpc/http/getminimumbalanceforrentexemption) | Query the cluster for the lamports required by a specific account size instead of treating a fixed SOL value as universal. |
| Priority-fee samples | [Solana RPC: getRecentPrioritizationFees](https://solana.com/docs/rpc/http/getrecentprioritizationfees) | Retrieve recent prioritization-fee samples from the RPC before setting an application-specific fee policy. |
