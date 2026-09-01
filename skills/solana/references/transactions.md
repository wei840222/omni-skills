# Transactions, fees, and finality

## Fees and compute budget

- The base transaction fee is charged per required signature. Obtain current fee details from the cluster or RPC response instead of embedding a fixed cost in an operational decision.
- During congestion, a Compute Budget `SetComputeUnitPrice` instruction can add a prioritization fee. Pair it with an appropriate `SetComputeUnitLimit` only after estimating the program's compute requirements.
- Transactions that exceed their compute-unit limit fail. Set the limit from simulation or program guidance rather than assuming a per-instruction default.

## Lifecycle and confirmation

- A transaction uses a recent blockhash with a limited validity window. If the blockhash expires, fetch a new blockhash, rebuild the transaction, re-sign it, and submit it again.
- A dropped or expired transaction was not confirmed on-chain; a failed transaction was processed and returned an error. Use the signature status and logs to distinguish them.
- For high-value or irreversible operations, wait for the commitment level your application requires and confirm the expected account state after execution.
- Run preflight simulation by default. Disable it only when an application-specific recovery path explains why simulation is unsuitable.
