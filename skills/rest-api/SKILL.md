---
name: rest-api
description: Design and implement secure, contract-driven REST APIs. Triggers for
  endpoint design, security, persistence, or API deployment tasks.
metadata:
  openclaw: '{"emoji": "🌐", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "REST API"}'
  related-skills:
  - skills/backend
  - skills/auth
  - skills/http
  - skills/api
---
## Setup

On first use, read `references/setup.md` for integration behavior and memory initialization.

## When to load

Load this skill when tasked with designing, implementing, securing, testing, or shipping a REST API.

This skill covers contract-first design, endpoint conventions, authentication and authorization, persistence strategy, test plans, observability, and release checklists.

## State location
Working memory lives in `<state_root>/`. Read `references/architecture.md` for memory structure.

## Quick Reference

Load only what is needed for the current API task.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory schema | `assets/memory-template.md` |
| Contract-first design | `references/api-contract.md` |
| Endpoint conventions and errors | `references/endpoint-design.md` |
| Auth and API security controls | `references/auth-and-security.md` |
| Data model and migrations | `references/persistence-and-migrations.md` |
| Test strategy and telemetry | `references/testing-and-observability.md` |
| Pre-release readiness gate | `references/deployment-checklist.md` |

## Core Rules and Traps
Read `references/core-rules.md` for API design rules, security standards, testing strategies, and common pitfalls.

## Security & Privacy
Read `references/security-and-privacy.md` for data boundary rules and infrastructure safety constraints.
