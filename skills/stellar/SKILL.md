---
name: stellar
description: Use this to handle Stellar (XLM) operations, verify transaction and memo
  requirements, or troubleshoot cross-border payments on the Stellar network.
metadata:
  openclaw: '{"emoji": "🚀", "os": ["linux", "darwin", "win32"], "displayName": "Stellar"}'
---
## Core Instructions
When working with the Stellar network, you MUST verify the following rules by reading `references/stellar-details.md`:
1. **Memo Fields**: Confirm memo requirements for exchange deposits to prevent loss of funds.
2. **Account Minimums**: Ensure the 1 XLM base reserve requirements are met before transacting.
3. **Trustlines**: Validate that trustlines exist prior to interacting with non-XLM assets.

To execute a transaction, troubleshoot a cross-border payment, or deploy Soroban contracts, load and follow `references/stellar-details.md`.
