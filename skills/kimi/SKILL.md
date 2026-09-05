---
name: kimi
description: Build and debug Moonshot AI Kimi API workflows for chat, coding, reasoning, long-context research, and structured output. Use when the user needs live model discovery, safe request routing, retries, or OpenAI-compatible migration.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌙","requires":{"bins":["curl","jq"],"env":["MOONSHOT_API_KEY"],"config":["<state_root>/kimi/"]}}'
  related-skills: '{"api":"Debug API authentication, payloads, retries, and OpenAI-compatible request shapes.","models":"Compare model families and cost tiers before production selection.","coding":"Harden coding-agent behavior after the Kimi route is stable.","backend":"Connect Kimi workflows to services, jobs, and API boundaries.","fastapi":"Expose Kimi-backed endpoints with request validation and safer deployment defaults."}'
---

## When to Use

User needs Kimi to work reliably for chat, coding, long-context research, structured outputs, or agent workflows. Agent handles live model verification, request shaping, migration from other OpenAI-compatible providers, and failure recovery before the workflow is trusted.

## Architecture

## State location

Memory lives in `<state_root>/kimi/`. Look for configuration in the workspace first, falling back to the global state root. If `<state_root>/kimi/` does not exist, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/kimi/
├── memory.md         # Status, activation rules, and stable defaults
├── routes.md         # Preferred route per workload
├── approvals.md      # Sensitive-send boundaries and redaction preferences
├── experiments.md    # Prompt, parser, and fallback notes
└── logs/             # Optional sanitized repro payloads
```

## Quick Reference

Use the smallest file that resolves the blocker.

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | Load when the state directory does not exist or initialization is needed. |
| Memory template | `references/memory-template.md` | Load when reading or writing to `memory.md` to ensure correct formatting. |
| Minimal request patterns | `references/api-patterns.md` | Load when crafting API payloads for Kimi chat or tool usage. |
| Workload routing choices | `references/routing-matrix.md` | Load when deciding which model size or feature set to use for a specific task. |
| OpenAI-compatible migration | `references/migration-playbook.md` | Load when transitioning existing OpenAI-style code to Moonshot's endpoints. |
| Trust and redaction workflows | `references/safety-workflows.md` | Load when dealing with sensitive data that requires user approval or redaction. |
| Fast diagnosis and recovery | `references/troubleshooting.md` | Load when Kimi API requests fail or produce unexpected results. |
| Core rules | `references/core-rules.md` | Load before choosing a route, sending sensitive data, or persisting state. |
| Common traps | `references/common-traps.md` | Load when troubleshooting a repeated or ambiguous failure. |
| Official endpoints | `references/external-endpoints.md` | Load before making a live API request or confirming external data flow. |

## Requirements

- `curl` and `jq` for minimal endpoint checks
- `MOONSHOT_API_KEY` kept in environment variables only
- Kimi access through the official Moonshot API base URL
- User approval before persisting local notes or sanitized logs

See `references/core-rules.md`.

See `references/common-traps.md`.

See `references/external-endpoints.md`.

## Security & Privacy

**Data that leaves your machine:**
- Prompt content sent to the Moonshot API when the user asks for Kimi inference
- Optional sanitized excerpts of code, logs, or documents sent for analysis after approval

**Data that stays local:**
- Activation preferences, route defaults, and approval boundaries in `<state_root>/kimi/` after user approval
- Optional sanitized repro payloads and troubleshooting notes saved for recurring workflows

**This skill does NOT:**
- Store `MOONSHOT_API_KEY` in markdown or project files
- Send data to undeclared endpoints
- Persist raw secrets or sensitive prompts without explicit user approval
- Modify its own skill files

## Scope

This skill ONLY:
- designs and debugs Kimi API workflows
- routes Kimi usage across coding, reasoning, research, and deterministic-output jobs
- hardens retries, validation, and migration from other OpenAI-compatible providers
- stores lightweight local notes only after user approval

Required protections for every workflow:
- verify live model availability by checking the API endpoint first
- keep secrets out of `<state_root>/kimi/`
- validate output before executing any downstream automation
- enforce cost-sensitive and sensitive-send boundaries explicitly

## Trust

Using this skill sends prompt data to Moonshot's Kimi API.
Only install if you trust Moonshot with that data, or keep sensitive preprocessing local and sanitized.
