# Setup — Odoo

Read this when `<state_root>/` does not exist or is empty. Start with the user's
Odoo problem and keep the tone practical, business-aware, and safety-first.

## Your Attitude

You are stepping into a live business system. Be calm, decisive, and aware that
small mistakes in Odoo can ripple into finance, stock, procurement, and customer
operations.

Help first, then learn the smallest reusable context that will make the next
Odoo task faster and safer. Do not lead with file names, paths, or
implementation details unless the user explicitly asks.

## Priority Order

### 1. First: Integration

Within the first few exchanges, learn when this skill should activate in the
future:

- Should it kick in whenever the user mentions Odoo, ERP, invoices, sales
  orders, stock, purchasing, or reconciliation?
- Should it activate proactively for risky Odoo writes, or only when the user
  asks?
- Are there environments where this skill should stay read-only unless the user
  explicitly escalates?

Store that activation preference in the resolved `<state_root>/memory.md` so
future sessions know when to load this skill.

### 2. Then: Understand the Odoo Surface

Learn only the details that change the answer:

- company and environment
- core modules in scope
- version if relevant
- whether the task is report, write, import, automation, or repair
- whether custom modules or Studio fields are likely involved

Infer what you can from the conversation. Ask only for the missing piece that
changes risk or execution.

### 3. Finally: Capture Stable Operating Defaults

When the user reveals durable patterns, keep them for next time:

- preferred modules and objects they work with most
- approval boundaries for writes, imports, and accounting changes
- known custom fields, integrations, warehouses, journals, or fiscal rules
- preferred output style for KPIs, exports, or executive summaries

Do not turn setup into a form. Keep solving the live task while collecting
durable context.

## What You're Saving

In `<state_root>/memory.md`, keep only stable notes:

- instances, companies, and operating environments
- active modules and customizations worth remembering
- read vs write boundaries
- recurring reporting scopes and output preferences
- incidents that changed the safe default

Never store passwords, API keys, cookies, personal data exports, or raw
accounting dumps in memory.

Use `assets/data-templates.md` when creating the first memory file.

## Optional companion files

- `<state_root>/instances.md` for per-instance URLs, auth lanes, and owners
- `<state_root>/modules.md` for custom fields and model overrides
- `<state_root>/incidents.md` for failed imports, broken automations, or
  audit-sensitive corrections

## Key Principles

- Store stable operating facts, not temporary tickets
- Prefer natural language notes over config-like keys outside the status block
- Never store credentials, exports, invoices, payroll data, or copied ledgers
- Update `last` every time the skill is used
- Keep the memory useful for the next real Odoo task, not exhaustive
