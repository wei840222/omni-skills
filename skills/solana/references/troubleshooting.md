# Troubleshooting transaction errors

| Symptom | First action | Recovery path |
| --- | --- | --- |
| Insufficient funds or rent-related error | Inspect the fee payer and required account balances. | Fund the required account or reduce the operation, then rebuild and sign a new transaction. |
| Account not found | Confirm the exact public key, cluster, token mint, and expected token-account address. | Create the required account or correct the instruction account list; use program logs to confirm the missing account. |
| Blockhash not found or expired transaction | Check the current signature status before retrying. | Fetch a fresh blockhash, rebuild, re-sign, and resubmit; do not reuse an expired signed transaction. |
| Program failed to complete | Retrieve simulation output or on-chain logs for the signature. | Resolve the program-specific error, then simulate the corrected transaction before submission. |
