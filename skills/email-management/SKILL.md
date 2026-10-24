---
name: email-management
description: "Triage inbox email, draft replies, and track follow-ups. Use when user requests inbox processing, response drafting, or managing pending threads."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📬","requires":{"config":["<state_root>"]},"configPaths":["<state_root>/"]}'
  related-skills: '{"assistant": "general assistant orchestration patterns", "crm": "customer relationship process management", "email-marketing": "campaign and newsletter execution workflows", "mail": "generic mail workflow support", "productivity": "execution and prioritization frameworks"}'
---

## State location

Email Management state may exist in `<workspace>/email-management/`, `<workspace>/memory/email-management/`, or `~/email-management/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/email-management/`, `<workspace>/memory/email-management/`, `~/email-management/`.
3. If none exists and state must be created, default to `<workspace>/email-management/`.

Use the selected `<state_root>` for every state operation in this skill.

- Fallback: Workspace-first state location.
- Creation: Agent must create the directory if it does not exist during setup.

## When to Use

User needs help processing inbox load, preparing replies, or keeping response commitments on track.
Agent triages messages by urgency, drafts context-aware responses, and tracks pending follow-ups until closure.

This skill is workflow-focused and local by default. It analyzes email text provided by the user in chat or by a separate mail integration skill.

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
