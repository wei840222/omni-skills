---
name: windows
description: Diagnose silent Windows failures, manage credentials safely, and navigate
  PowerShell, WinRM, Defender, service-account, and file-lock traps. Use when scripting
  or troubleshooting on Windows hosts, scheduled tasks, remoting, or ops automation.
  Not for PowerShell language syntax depth (`powershell`) or broad defensive security
  programs (`cybersecurity`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🪟","os":["win32"]}'
  related-skills: '{"cybersecurity": "Broader defensive security triage, detection, and program work beyond Windows ops traps.", "powershell": "PowerShell language, pipelines, arrays, operators, and cross-version syntax beyond Windows host traps.", "security-best-practices": "Secure-by-default code review and remediation rather than Windows host operations."}'
---

## When to Use

- Windows scripts or automation fail silently or intermittently
- Credentials, scheduled tasks, WinRM, Defender, or service accounts are involved
- Choosing safe defaults for PowerShell ops, file locks, temp files, or event logging on Windows
- Not for deep PowerShell language craft (`powershell`) or org-wide security program design (`cybersecurity`)

This skill is stateless and does not store local configuration or persistent user state.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Credentials, silent failures, symlinks, signing, safety | `references/windows-operations.md` | Default ops and troubleshooting |
| WinRM, event log, file locks, temp files, service accounts | `references/windows-operations.md` | Remoting and long-running automation |
| Official sources | `references/sources.md` | Verify current Microsoft guidance |

## Core Rules

1. Prefer explicit errors over quiet failure: avoid `-ErrorAction SilentlyContinue` for control-flow paths; use `Stop` and handle.
2. Never hardcode passwords. Use Windows Credential Manager, `Get-Credential` + `Export-Clixml`, or a secrets store scoped to the run identity.
3. Assume Defender, GPO, AV, and execution policy can change observed behavior without a loud error — verify the effective policy before blaming the script.
4. Service/scheduled-task identity is not the interactive user: no mapped drives, different `$env:USERPROFILE`, machine credentials for network access.
5. Destructive ops start with `-WhatIf` / canary; file writes check locks; temp files clean up in `try/finally`.
6. For PowerShell language details (streams, arrays, operators, `pwsh` vs Windows PowerShell), load `powershell` instead of expanding this skill.

## Operations

For credential management, silent failures, scripting safety, WinRM, logging, file locking, temp files, and service accounts, load [Windows Operational Details](references/windows-operations.md).
