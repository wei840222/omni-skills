---
name: zendesk
description: Manage Zendesk tickets, users, and support workflows. Authenticate via environment variables or local memory, execute REST API operations, and handle common ticket lifecycles. Use when creating or updating tickets, searching support history, checking user details, or automating Zendesk Support API workflows. Not for Zendesk Sell CRM or Help Center content authoring alone.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎫","requires":{"env":["ZENDESK_SUBDOMAIN","ZENDESK_EMAIL","ZENDESK_TOKEN"]},"primaryEnv":"ZENDESK_TOKEN","os":["linux","darwin","win32"],"displayName":"Zendesk"}'
---

## Setup

On first use, read `references/setup.md` for API credentials and workspace integration.

## When to Use

User needs to interact with Zendesk: create or update tickets, search support history, check user details, or automate support workflows. Agent handles API operations, ticket management, and reporting.

## State location

Zendesk state may exist in `<workspace>/zendesk/`, `<workspace>/memory/zendesk/`, or `~/zendesk/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/zendesk/`, `<workspace>/memory/zendesk/`, `~/zendesk/`.
3. If none exists and state must be created, default to `<workspace>/zendesk/`.

Use the selected `<state_root>` for every state operation in this skill.

Resolve `<state_root>` as:

```
<state_root>/
├── memory.md    # credentials prefs + views + recent context
└── exports/     # optional local ticket/report exports
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When initializing credentials for the first time |
| Memory template | `references/memory-template.md` | When structuring or reading local memory |
| API operations | `references/api-reference.md` | When making specific Zendesk API calls |
| Common issues | `references/troubleshooting.md` | When API calls fail or return unexpected results |
| Core Rules | `references/core-rules.md` | Before performing any state-changing API operations |
| Common Operations | `references/common-operations.md` | When needing examples of standard ticket and user operations |
| Ticket Statuses | `references/ticket-statuses.md` | When interpreting or updating ticket states |
| Priorities | `references/priorities.md` | When assigning or interpreting ticket urgency |
| Common Traps | `references/common-traps.md` | When encountering errors or designing a robust automation |
| Domain Knowledge | `references/zendesk-knowledge.md` | When needing a conceptual understanding of Zendesk entities |
| Official sources & API specifications | `references/sources.md` | When verifying official Support REST API endpoints, ticket schemas, or rate limits. |

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `https://{subdomain}.zendesk.com/api/v2/*` | Ticket/user data | All operations |

Data transmission is strictly limited to the listed Zendesk endpoints.

## Security & Privacy

**Data that leaves your machine:**
- Ticket content sent to Zendesk API
- Search queries sent to Zendesk

**Data that stays local:**
- API credentials in <state_root>/memory.md
- Exported reports in <state_root>/exports/

**This skill does NOT:**
- Store credentials in plain text outside <state_root>/
- Send data to any service other than Zendesk
- Access tickets without explicit user request

## Trust

By using this skill, ticket and user data is sent to Zendesk's API.
Only install if you have authorized Zendesk API access.
