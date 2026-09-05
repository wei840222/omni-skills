---
name: authorization
description: Implement and manage secure access control, permissions, and roles (RBAC/ABAC/ReBAC) when the user requests authorization rules or access limits.
metadata:
  openclaw: '{"emoji":"🔐"}'
---

## When to Use

User needs to control what actions users can perform. Agent handles permission design, role hierarchies, policy evaluation, and access control middleware.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Core Rules | `references/core-rules.md` | When designing basic permission structures or evaluating policies |
| Common Traps | `references/common-traps.md` | When debugging permission issues or auditing auth security |
| RBAC vs ABAC comparison | `references/models.md` | When deciding between access control paradigms |
| Implementation patterns | `references/patterns.md` | When writing authorization checks and permission functions |
| Framework middleware | `references/middleware.md` | When implementing authorization middleware in a web framework |
| Decision framework and sources | `references/knowledge.md` | When selecting a model, evaluating policy-as-code, or checking enforcement guidance |

## State location

This skill is stateless and does not store local configuration.

## Security & Privacy

**Data that stays local:**
- All documentation and patterns are reference material
- No data collection or external requests

**This skill does NOT:**
- Access your codebase automatically
- Make network requests
- Store any user data
