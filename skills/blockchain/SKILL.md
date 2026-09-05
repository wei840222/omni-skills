---
name: blockchain
description: Evaluate whether blockchain fits a problem, explain distributed-ledger fundamentals, and safely read or write EVM smart contracts with viem. Use for blockchain architecture decisions, wallet and transaction safety, or EVM contract interactions; do not use for trading advice or price analysis.
metadata:
  openclaw: '{"emoji":"⛓️"}'
  related-skills: '{"solidity":"Covers Solidity development and common smart-contract security pitfalls beyond this skill’s viem interaction guidance."}'
---

This skill is stateless and does not store local configuration or persistent user state.

## What this covers

Blockchain fundamentals and practical EVM interaction—the technology, not speculation.

**In scope:** distributed ledgers, consensus, transactions, contract interaction, wallets, and token standards.

**Out of scope:** trading strategies, price analysis, specific DeFi protocols, and Solidity development (use the `solidity` skill).

## Developer quick reference

```typescript
import { createPublicClient, createWalletClient, http } from 'viem'
import { mainnet } from 'viem/chains'

const client = createPublicClient({ chain: mainnet, transport: http() })
const balance = await client.getBalance({ address: '0x...' })
const hash = await walletClient.writeContract({ address, abi, functionName, args })
const receipt = await client.waitForTransactionReceipt({ hash })
```

Before sending a transaction, verify the chain, recipient, token decimals, allowance, simulation result, and wallet prompt. A submitted transaction may be irreversible; never request or handle a seed phrase or private key.

## When blockchain fits

Use blockchain when independent parties need shared truth without a trusted operator, immutability materially matters, or reconciliation costs dominate. Avoid it when one organization controls the data, deletion is required, or a conventional database with audit logs solves the need.

> **Database test:** Would PostgreSQL with appropriate access controls and audit logs solve the problem? If yes, use the database.

## Reference files

Use the concise entry point above first; then load exactly one or more references only when their trigger applies:

| Resource | When to load |
| --- | --- |
| `references/concepts.md` | Explaining core concepts, consensus, or Layer 2 architectures. |
| `references/dev.md` | Reading or writing contracts, selecting libraries, or checking gas and transaction patterns. |
| `references/evaluation.md` | Deciding whether a workload needs blockchain rather than conventional infrastructure. |
| `references/security.md` | Reviewing wallet, seed phrase, approval, phishing, or smart-contract safety. |
