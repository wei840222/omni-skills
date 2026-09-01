# Accounts and token accounts

## Rent and account creation

- A newly created Solana account needs enough lamports for its allocated data size. Query the cluster's current rent-exemption minimum instead of relying on a fixed SOL amount.
- A token account is a separate on-chain account. Creating it requires funding for account creation; closing an eligible token account returns its remaining lamports to its designated recipient.

## SPL token accounts

- A wallet address does not itself hold each SPL token balance. Standard user token balances are held in token accounts, commonly the Associated Token Account (ATA) for the wallet and mint.
- For a first transfer to a wallet, create or confirm the recipient's ATA using the current token-program and transfer flow. An account-not-found error can mean that the expected token account is absent, but inspect the instruction logs before assuming this cause.
- Programs can use non-associated token accounts. Treat the ATA as the standard convention, not as the only valid token-account address.
