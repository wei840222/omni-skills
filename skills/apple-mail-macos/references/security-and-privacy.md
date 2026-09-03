# Security & Privacy


**Data that stays local:**
- Operational context and defaults in `<state_root>/`.
- Message metadata needed to execute the requested task.

**Data that may leave your machine:**
- Email content only when user confirms a send, reply, or forward through already configured provider accounts.

**This skill does NOT:**
- Send mail without explicit user confirmation.
- Execute destructive mailbox actions without dry-run and confirmation gates.
- Request undeclared API keys or call undeclared third-party APIs.
