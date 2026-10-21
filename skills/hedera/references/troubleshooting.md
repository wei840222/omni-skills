# Common Hedera failures

| Symptom / status | Likely cause | Recovery |
| --- | --- | --- |
| `INVALID_ACCOUNT_ID` | Account ID unknown or not yet created | Confirm network + ID formatting (`0.0.x`). Create/fund the account or use a documented auto-create alias path. |
| `TOKEN_NOT_ASSOCIATED_TO_ACCOUNT` / association errors | Receiver has not associated the token | Have the receiver associate (or raise max automatic associations), then retry the transfer. |
| `INSUFFICIENT_PAYER_BALANCE` | Payer lacks HBAR for the fee (and any transfer amount) | Fund the payer with enough HBAR on the correct network; re-estimate fee with extras. |
| `INSUFFICIENT_TX_FEE` | `maxTransactionFee` too low for actual characteristics | Raise the max fee using the fee estimator; include signature/memo/size extras. |
| `ACCOUNT_FROZEN_FOR_TOKEN` | Token freeze key froze the account | Contact token operator or use a different token; holders cannot unilaterally unfreeze. |
| `TOKEN_WAS_DELETED` / `ACCOUNT_DELETED` | Entity no longer transferable | Stop retries; migrate to a live account/token. |
| Contract call runs out of gas | EVM gas limit too low | Resimulate with higher gas; remember failed calls can still consume paid gas. |

## Transfer checklist

1. Correct network and account ID (not an ETH hex address unless using a verified alias/EVM path).
2. Receiver exists or auto-create conditions are satisfied.
3. For custom tokens: association present.
4. Memo matches exchange instructions and contains no secrets.
5. Payer can cover amount + fee; collect the transaction ID / mirror-node receipt before declaring success.
