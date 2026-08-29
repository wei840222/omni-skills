---
name: ansible
description: "Identify and fix Ansible playbook mistakes: YAML quoting traps, variable precedence, non-idempotent command/shell tasks, handler timing, become placement, conditionals, loops, and facts. Use when reviewing or debugging Ansible YAML, playbooks, roles, inventory vars, handlers, or privilege escalation. Not for generic YAML syntax alone (yaml) or Linux host ops without Ansible (linux)."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✨"}'
  related-skills: '{"yaml":"Parser-level YAML quoting, booleans, and indentation traps under Ansible files.","linux":"Host-side sudo, permissions, and service behavior when become or package tasks fail.","bash":"Shell/command module scripts that need idempotence wrappers or creates/removes."}'
---

## State location

This skill is stateless and does not store local configuration or persistent user state.

## When to Use

- Reviewing or writing Ansible playbooks, roles, tasks, handlers, or inventory variables
- Debugging unexpected `changed`, failed conditionals, missing facts, or privilege-escalation failures
- Cleaning up non-idempotent `command`/`shell` usage and handler notify patterns

Redirect pure YAML parser questions to `yaml`. Redirect host troubleshooting that is not about Ansible play semantics to `linux` or `bash`.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Core operating rules | `references/core-rules.md` | Start of playbook review or rewrite |
| Common traps | `references/common-traps.md` | During review or when a task misbehaves |
| Domain knowledge and sources | `references/domain-knowledge.md` | Before asserting Ansible semantics or citing docs |

## Operating Rules

1. Prefer idempotent modules (`apt`, `yum`, `dnf`, `copy`, `template`, `file`, `service`) over raw `command`/`shell`.
2. Quote Jinja2 expressions in YAML values; never put Jinja2 braces inside `when:`.
3. Treat handlers as end-of-play, change-gated, and deduplicated unless `meta: flush_handlers` or `--force-handlers` is intentional.
4. Verify `become` at the task that needs escalation; play-level `become` is not always enough.
5. Name the layer before fixing: YAML parse, variable precedence, module semantics, facts, or privilege escalation.
