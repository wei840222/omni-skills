---
name: open-router
description: Configure OpenRouter model routing, provider preferences, fallbacks, and cost controls. Use when a user asks to route LLM requests through OpenRouter, choose models or providers, recover from routing failures, or control inference spend.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛣️","requires":{"bins":["curl","jq"],"env":["OPENROUTER_API_KEY"]}}'
  related-skills: '{"api":"Designs and validates API requests used with OpenRouter.","auth":"Handles credential and authentication troubleshooting for OpenRouter clients.","models":"Helps compare and select models for routing policies.","monitoring":"Tracks runtime health and incidents for routing operations."}'
---

## State location

Before reading or writing routing state, resolve `<state_root>` once for this invocation:

1. Use an explicitly configured state path when the user or host provides one.
2. Otherwise use the first existing directory in this order: `<workspace>/open-router/`, `<workspace>/memory/open-router/`, then `~/.open-router/`.
3. If none exists and the user authorizes persistent routing state, create `<workspace>/open-router/` and use it as `<state_root>`.

Use only the selected `<state_root>` for this invocation. When more than one candidate exists, choose the first, report the conflict, and leave the other copies unchanged until the user selects a migration path.

## Setup

On first use, load `references/setup.md` before changing routing configuration. Load only the reference that matches the current routing, provider, cost, authentication, or reliability question.

| Topic | Reference | Load when |
|---|---|---|
| State template | `references/memory-template.md` | Initializing or updating persistent routing state. |
| Authentication and provider wiring | `references/auth-and-provider.md` | Configuring credentials, headers, or an API client. |
| Workload routing | `references/routing-playbooks.md` | Selecting models or providers by workload. |
| Fallback recovery | `references/fallback-reliability.md` | Handling rate limits, timeouts, outages, or quality regressions. |
| Cost controls | `references/cost-guardrails.md` | Setting budgets or reviewing inference spend. |
| Core operating rules | `references/core-rules.md` | Reviewing a routing policy before rollout. |
| API concepts | `references/openrouter-api-concepts.md` | Clarifying OpenRouter request, provider-routing, or fallback behavior. |

## State layout

State remains outside this skill package:

```text
<state_root>/
├── memory.md          # Active routing profile and constraints
├── providers.md       # Confirmed provider and authentication choices
├── routing-rules.md   # Task-to-model and fallback policy
├── incidents.md       # Outages, rate limits, and recovery notes
└── budgets.md         # Spend guardrails and review actions
```

## External endpoints

Use these endpoints only for an explicit user task:

| Endpoint | Data sent | Purpose |
|---|---|---|
| `https://openrouter.ai/api/v1/models` | Authentication header when supplied | Discover available model metadata. |
| `https://openrouter.ai/api/v1/chat/completions` | Prompt content and selected routing parameters | Execute an inference request. |

## Security and privacy

- Read `OPENROUTER_API_KEY` from the local environment; do not request, log, or store its value.
- Send prompt content to OpenRouter only when the user requests inference or configuration verification requiring a live request.
- Store routing notes and verification outcomes under `<state_root>/`; do not modify state outside that root for this skill.
- Before a routing change, identify the workload, primary route, fallback trigger, and budget boundary. Verify the change with a representative request before broad rollout.
