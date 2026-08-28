---
name: auth
description: Build secure authentication with sessions, JWT, OAuth, passwordless, MFA, and SSO for web and mobile apps.
metadata:
  version: "1.3.0"
  openclaw: '{"emoji": "🔐", "requires": null, "os": ["linux", "darwin", "win32"], "displayName": "Auth"}'
---


## Documentation-Only Skill

This skill is a **reference guide**. It contains code examples that demonstrate authentication patterns.

**Important:** The code examples in this skill:
- Are templates for developers to adapt
- Show placeholder values (SECRET, API_KEY, etc.)
- Reference external services as examples only
- Are NOT executed by the agent

The agent provides guidance. The developer implements in their own project.


## State location

This skill is completely stateless and does not store any local configuration or data.

## When to Use

User needs guidance on implementing authentication. Agent explains patterns for login flows, token strategies, password security, OAuth integration, MFA, and session management.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Session vs JWT strategies | `references/strategies.md` | Load when comparing authentication patterns or deciding between stateless tokens and stateful sessions. |
| Password handling | `references/passwords.md` | Load when implementing password hashing, validation, or storage. |
| MFA implementation | `references/mfa.md` | Load when adding multi-factor authentication. |
| OAuth and social login | `references/oauth.md` | Load when integrating third-party login providers. |
| Framework middleware | `references/middleware.md` | Load when protecting routes or verifying tokens in application middleware. |
| Core rules | `references/core-rules.md` | Load when starting a new authentication implementation to review fundamental security principles. |
| Common traps | `references/common-traps.md` | Load during code review or finalization to ensure known security pitfalls are avoided. |
| Domain knowledge | `references/domain-knowledge.md` | Load to understand standard authentication concepts like JWT, MFA, and OAuth. |

## Scope

This skill ONLY:
- Explains authentication concepts
- Shows code patterns as examples
- Provides best practice guidance

Restricted actions:
- Code execution
- Making network requests
- Accessing credentials
- Storing data
- Reading environment variables

## Note on Code Examples

Code examples in auxiliary files show:
- Environment variables like `process.env.JWT_SECRET` - these are **placeholders**
- API calls to OAuth providers - these are **reference patterns**
- Secrets like `SECRET`, `REFRESH_SECRET` - these are **example names**

The agent does not have access to these values. They demonstrate what the developer should configure in their own project.
