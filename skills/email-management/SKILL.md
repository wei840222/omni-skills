---
name: email-management
description: "Triage inbox email, draft replies, and track follow-ups. Trigger when user requests inbox processing, response drafting, or managing pending threads."
metadata:
  related-skills: '{"mail":"generic mail workflow support", "email-marketing":"campaign and newsletter execution workflows", "crm":"customer relationship process management", "productivity":"execution and prioritization frameworks", "assistant":"general assistant orchestration patterns"}'
  clawdbot:
    emoji: 📬
    requires:
      config:
      - "<state_root>"
    os:
    - linux
    - darwin
    - win32
    configPaths:
    - <state_root>/
    displayName: Email Management
  openclaw: '{"requires":{"config":["<state_root>"]}}'
---

## State Location
- Primary: `<state_root>/`
- Fallback: Workspace-first state location.
- Creation: Agent must create the directory if it does not exist during setup.

## Setup
On first use, read `references/setup.md` for integration guidelines and memory initialization.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup | `references/setup.md` | On first activation |
| Memory template | `references/memory-template.md` | When initializing or updating state |
| Domain knowledge | `references/domain-knowledge.md` | For Inbox Zero concepts |
| Triage | `references/triage.md` | When sorting new emails |
| Tracking | `references/tracking.md` | When an email contains a commitment |
| Templates | `references/templates.md` | When drafting recurring replies |
| Profiles | `references/profiles.md` | When determining tone and focus |
| Automation | `references/automation.md` | To verify safety boundaries |
| Feedback | `references/feedback.md` | When reviewing output quality |
| Rules & Privacy | `references/rules.md` | When ensuring safety, privacy, and process adherence |
