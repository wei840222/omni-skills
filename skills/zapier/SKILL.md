---
name: zapier
description: >
  Design and operate Zapier Zaps, Tables, Interfaces, Catch Hooks, and REST/AI
  Actions. Use when connecting apps, debugging polling delays, mapping fields,
  choosing Paths/Filters, or calling Zapier APIs; prefer `webhook` for generic
  receiver design and `api` for non-Zapier REST clients.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚡","requires":{"env":["ZAPIER_API_KEY","ZAPIER_TABLES_TOKEN"],"config":["<state_root>/"]},"primaryEnv":"ZAPIER_API_KEY","os":["linux","darwin","win32"],"displayName":"Zapier"}'
  related-skills: '{"api": "Generic REST/GraphQL client patterns outside Zapier-hosted APIs.", "saas": "Subscription and plan-economics framing when Zapier billing or task usage is the ask.", "webhook": "Provider-agnostic webhook receiver/sender design when Zapier is not the platform."}'
---


# Zapier

Operate **Zapier** workflows and related product surfaces: Zaps, Tables,
Interfaces, Catch Hooks, and documented Zapier APIs. Keep account preferences
under a resolved `<state_root>`; never commit API keys into the skill package.

## State location

Zapier preferences may exist in `<workspace>/zapier/`,
`<workspace>/memory/zapier/`, or `~/zapier/`. Before reading or writing state,
resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/zapier/`, `<workspace>/memory/zapier/`, `~/zapier/`.
3. If more than one candidate exists, use only the highest-precedence directory
   and report the duplicates; do not merge them.
4. If none exists and the user confirms saving preferences, create
   `<workspace>/zapier/`. If `<workspace>` is unavailable, ask for a state root
   instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation. Never write the literal string
   `<state_root>` to disk.

```text
<state_root>/
|-- memory.md   # Account context, common Zaps, plan/polling notes (no secrets)
`-- zaps/       # Optional documented Zap configurations
```

If older notes exist under a legacy Clawic Zapier data directory, migrate them
into the resolved `<state_root>/` on first write and say in one line that you
moved them and from where. Seed new memory from `references/memory-template.md`.

## Quick Start

```bash
# Test a configured Zapier API credential (endpoint family depends on product)
curl -H "Authorization: Bearer $ZAPIER_API_KEY" \
  https://actions.zapier.com/api/v1/exposed/
```

On first use, read `references/setup.md`. Preferences live in
`<state_root>/memory.md`.

## When to Use

- Create or edit Zaps across 6000+ apps (Sheets → Slack, CRM → email, etc.)
- Explain polling vs instant triggers and plan-dependent update intervals
- Configure Catch Hooks, Paths/Filters/Formatters, Tables, or Interfaces
- Call Zapier-hosted APIs / AI Actions with env-stored credentials
- Triage task burn, duplicate runs, webhook timeouts, or field-mapping bugs

Prefer other skills when the ask is mainly:

- generic webhook receiver/sender design → `webhook`
- non-Zapier REST/GraphQL client work → `api`
- SaaS billing math unrelated to Zapier task/plan limits → `saas`

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup & memory | `references/setup.md`, `references/memory-template.md` | First use or preference bootstrap |
| REST / AI Actions API notes | `references/api.md` | Calling Zapier-hosted HTTP APIs |
| Triggers | `references/triggers.md` | Choosing polling vs instant triggers |
| Actions | `references/actions.md` | Mapping action steps and search actions |
| Filters, Paths, Formatters | `references/logic.md` | Branching or field transforms |
| Webhooks | `references/webhooks.md` | Catch Hook / outbound webhook steps |
| Tables | `references/tables.md` | Zapier Tables as a no-code datastore |
| Interfaces | `references/interfaces.md` | Forms, pages, chatbots |
| Popular integrations | `references/integrations.md` | Common app pairings |
| Patterns & recipes | `references/patterns.md` | Multi-Zap recipes and anti-patterns |

## Core Rules

1. **Test mode first** — exercise with sample data before enabling a Zap.
2. **Triggers define scope** — a Zap runs only when its trigger fires.
3. **Field mapping is explicit** — verify each mapped field before publish.
4. **Filters before actions** — reduce unnecessary task usage.
5. **Idempotency via Dedup** — protect critical flows from duplicate processing.
6. **Prefer instant triggers** — polling intervals are plan-dependent.

## Authentication

Environment variables:

- `ZAPIER_API_KEY` — Zapier API / AI Actions credential (primary)
- `ZAPIER_TABLES_TOKEN` — Tables API token when Tables HTTP access is required

Store secrets in the host secret manager or env; keep only pointers in
`<state_root>/memory.md`.

## Zapier Product Suite

| Product | Purpose | File |
|---------|---------|------|
| **Zaps** | Automated workflows | `references/triggers.md`, `references/actions.md` |
| **Tables** | No-code database | `references/tables.md` |
| **Interfaces** | Forms, pages, chatbots | `references/interfaces.md` |
| **Chatbots** | AI-assisted Interfaces | `references/interfaces.md` |
| **Canvas** | Visual planning | Web UI only |

## Common Traps

- **Amount format mismatch** → Zapier often passes strings; convert with Formatter
- **Missing idempotency** → Dedup / unique keys prevent duplicate side effects
- **Webhook timeout** → Return HTTP 200 within ~30 seconds for Catch Hook receivers
- **Task burn** → One Zap run can consume 1+ tasks; filters that stop a run early still matter for design
- **Polling delay** → Free: 15 min; Professional: 2 min; Team/Enterprise: 1 min; instant/webhook triggers bypass polling

## External Endpoints

| Endpoint | Purpose | Notes |
|----------|---------|-------|
| `https://actions.zapier.com/api/v1/*` | AI Actions / exposed actions | Common LLM integration surface |
| `https://hooks.zapier.com/hooks/catch/*` | Incoming Catch Hook URLs | Instant inbound events |
| `https://tables.zapier.com/api/v1/*` | Tables API | Requires Tables token/plan access |
| `https://api.zapier.com/v1/*` | Legacy/account automation APIs | Availability varies by product/auth; verify against current Zapier docs before relying on a path |

Connected third-party apps receive only fields the Zap explicitly maps.

## Security & Privacy

**Environment variables used:** `ZAPIER_API_KEY`, optional `ZAPIER_TABLES_TOKEN`

**Sent to Zapier:** workflow configuration and mapped run data
**Sent to connected apps:** only explicitly mapped fields
**Stays local:** `<state_root>/` preferences and secret pointers
**Instead:** protect API keys, verify webhook authenticity where the receiver supports it, and never log raw tokens

## Trust

This skill sends data to Zapier (`zapier.com` and related Zapier hostnames) and
to any apps connected through Zaps.
