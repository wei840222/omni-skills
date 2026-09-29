---
name: invoice
description: Create, calculate, generate, send, and track professional invoices and
  credit notes for clients you bill. Use when issuing outbound invoices, credit notes,
  tax totals, PDF generation, or payment tracking; not for filing supplier invoices received.
metadata:
  version: 1.0.0
  openclaw: '{"emoji":"🧾","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["<state_root>/billing/"],"displayName":"Invoice"}'
  related-skills: '{"billing":"Product or subscription billing systems when the work is software billing rather than a single client invoice.","clients":"Client CRM records and follow-up when invoice work needs durable client context beyond billing state.","email-management":"Outbound send and mailbox workflows after the PDF is finalized.","expenses":"Day-to-day spend logs that are not client-facing invoices.","invoices":"Filing and auditing invoices the user received from suppliers, the opposite document direction.","money":"Cashflow and payment-status views once invoices are sent.","pdf-generator":"Generic PDF rendering helpers when the invoice HTML template needs a shared converter."}'
---

## When to load

Load this skill when the user asks to create, modify, finalize, send, or track an **outbound** invoice or credit note to their own client.
Prefer this skill over generic PDF or email helpers when correlative numbering, tax lines, legal invoice types, or payment tracking change the workflow.
Do not load for supplier invoices the user received (`invoices`), personal expense logs (`expenses`), or building billing product software (`billing`) as the primary task.

## State location

Invoice state may exist in `<workspace>/invoice/`, `<workspace>/memory/invoice/`, or `~/invoice/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/invoice/`, `<workspace>/memory/invoice/`, `~/invoice/`.
3. If none exists and state must be created, default to `<workspace>/invoice/` after the user approves persistence.

Use the selected `<state_root>` for every state operation in this skill. Keep the root fixed for the rest of the invocation.
If multiple candidates exist, use the highest-precedence path only; tell the user duplicates were detected and do not merge automatically.
Never write the literal string `<state_root>` to disk.

Domain layout under the resolved root (preserve this architecture):

```text
<state_root>/billing/
├── drafts/                   # Work in progress
│   └── {client-name}/
│       ├── current.md        # Latest version
│       └── versions/         # v001.md, v002.md
├── sent/                     # Finalized invoices
│   └── 2026/
│       └── F-2026-001.pdf
├── clients/                  # Client database
│   └── index.json
├── config.json               # User's business data, templates
└── series.json               # Numbering per series
```

## Security and data boundaries

- Never store private keys, mailbox passwords, bank login secrets, or API tokens inside skill files or invoice Markdown.
- Keep credentials in the host secret store or env; invoice state may hold only non-secret pointers.
- Treat client tax IDs and bank details as sensitive local data; do not exfiltrate them to third parties without explicit user authorization.
- Do not reuse, skip, or invent correlative invoice numbers to “fix” a draft.

## When to load references

| Requirement | Load this reference |
|-------------|---------------------|
| Draft → review → finalize → send → track workflow | `references/phases.md` |
| Client database schema and lookup | `references/clients.md` |
| HTML templates and PDF generation | `references/templates.md` |
| Country legal/tax field requirements | `references/legal.md` |
| Full vs simplified vs credit-note rules | `references/types.md` |
| Verified primary sources for legal/tax claims | `references/sources.md` |

## Core rules

- **Numbering integrity**: Use strictly correlative numbering without gaps (for example `F-2026-001`, `F-2026-002`). To cancel or correct, issue a credit note that references the original; never reuse the original number.
- **Tax calculation**: Always show base, rate, tax amount, and total as separate lines. Do not hide tax inside a single opaque total.
- **Data validation**: Before finalize, B2B invoices need company name, tax ID, and address. Collect missing required fields instead of guessing.
- **Draft vs final**: Assign the next number when drafting for preview, but persist the counter only when the invoice is finalized.
- **Send boundary**: Final PDF generation and optional email send happen only after user review of the draft totals.

## Initialization

Before the first invoice, ensure `<state_root>/billing/config.json` contains:

- Business name, tax ID, address
- Bank details (IBAN) for payment instructions
- Default tax rate
- Invoice series format (for example `F-2026-`)
- Optional send-from email identity (non-secret)

If config is missing, collect only the fields required for the current draft and write them after the user confirms persistence.
