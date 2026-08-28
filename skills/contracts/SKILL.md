---
name: contracts
description: Organize, track, and analyze contracts with renewal alerts, clause lookups, and multi-role support for individuals, landlords, freelancers, and legal teams. Use when managing a contract register, extracting key terms from NDAs/leases/subscriptions, setting renewal or notice reminders, or comparing obligations across counterparties.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📑"}'
  related-skills: '{"lawyer":"Counsel-style redlines and negotiation when the user needs markup, not a register","legal":"Issue-spotting drills when the task is legal analysis rather than contract filing","documents":"Personal document vault when the file is an ID/certificate rather than an executable contract","extract-pdf-text":"Local PDF text extraction before contract metadata filing","calendar-planner":"Multi-calendar planning when renewal alerts must land on a real calendar"}'
---


## Role

Manage all contracts in one place. Track dates, extract key terms, flag expiring items. Scale from personal subscriptions to enterprise contract libraries.

---

## State location

Candidate locations (workspace-first):
1. `contracts/`
2. `Documents/contracts/`
3. `~/.local/share/contracts/`

When a new contract is managed, create the directory structure in the first valid candidate location if it doesn't exist, and treat it as `<state_root>`.

```
<state_root>/
├── index.md                    # Master list with quick stats
├── by-type/                    # NDAs, leases, subscriptions, etc.
├── by-party/                   # Organized by counterparty
├── {contract-name}/
│   ├── executed.pdf            # Final fully-signed version
│   ├── meta.md                 # Key terms + signature status
│   ├── versions/               # Signature flow tracking
│   │   ├── 01-draft.pdf        # Initial version sent
│   │   ├── 02-signed-them.pdf  # Signed by counterparty
│   │   └── 03-signed-us.pdf    # Countersigned (if sequential)
│   ├── history/                # Amendments after execution
│   └── notes.md                # User notes, flags
```

**Signature states:** `draft` → `pending-them` → `pending-us` → `executed`

---

## Quick Reference

| Context | When to load | Load |
|---------|--------------|------|
| Role-specific workflows | When analyzing contracts based on a specific user persona (e.g. landlord, freelancer) | `references/roles.md` |
| Contract analysis patterns | When extracting key terms, clauses, or identifying red flags from a contract | `references/analysis.md` |
| Alert and deadline tracking | When setting reminders, priority levels, or detecting renewal traps | `references/alerts.md` |
| Security and boundaries | When handling sensitive information, ensuring privacy, or setting boundaries | `references/security.md` |
| Domain knowledge for concepts | When explaining contract lifecycle management principles and terms | `references/domain-knowledge.md` |

---

## Core Capabilities

1. **Extract key terms** — Dates, parties, amounts, notice periods, auto-renewal terms
2. **Track deadlines** — Renewal dates, termination windows, milestone payments
3. **Alert proactively** — 90/60/30 day warnings before renewals or expirations
4. **Quick clause lookup** — "What's my cancellation notice period for X?"
5. **Cross-contract search** — "Find all contracts expiring this quarter"
6. **Version tracking** — Link amendments to parent contracts
7. **Cost aggregation** — Total spend across subscriptions/vendors

---

## On Upload

When user shares a new contract:
1. Create folder in <state_root>/{name}/
2. Save as current.pdf
3. Extract to meta.md: parties, effective date, term, value, renewal terms, notice period
4. Add to index.md
5. Set calendar alerts per `references/alerts.md`

---

## Boundaries

- **Provide factual extraction only** — Present contract clauses as written, and refer users to legal counsel for interpretation, risk assessment, or recommended actions.
- **Maintain local storage** — Keep all contracts securely stored on the local filesystem. Require explicit user authorization to move or share files.
- **Protect confidentiality** — Ensure contract text remains within the designated storage locations and is not exposed through messaging channels.
- "Is this clause good?" → "I can show you the clause, but consult a lawyer for interpretation"

---

### Active Contracts
<!-- Count and categories from <state_root>/index.md -->

### Expiring Soon
<!-- Next 90 days from meta.md dates -->
