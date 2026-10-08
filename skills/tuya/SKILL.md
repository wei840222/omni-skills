---
name: tuya
description: >
  Control and automate Tuya Smart devices with official cloud APIs, secure
  request signing, region-aware routing, and safe command execution. Use when
  the user needs Tuya/Smart Life cloud auth, device discovery, DPS commands,
  account linking, or multi-device orchestration rather than generic IoT advice.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔌","requires":{"bins":["curl","jq","openssl"],"env":["TUYA_ACCESS_ID","TUYA_ACCESS_SECRET"]},"displayName":"Tuya Smart"}'
  related-skills: '{"iot":"Broader IoT patterns outside Tuya-specific cloud control.","smart-home":"Home automation context that may include non-Tuya devices.","api":"Generic HTTP API request craft when Tuya signing is not the focus.","mqtt":"Local/broker messaging paths adjacent to cloud control.","zigbee":"Local radio fabrics that may coexist with Tuya cloud devices."}'
compatibility: '*'
license: MIT
---

## State location

Tuya operational notes may exist in `<workspace>/tuya/`, `<workspace>/memory/tuya/`, or `~/tuya/`.
Resolve `<state_root>` before the first state read or write:

1. Use an explicit user/host-configured path if supplied; resolve it to an actual absolute directory.
2. Otherwise select the first existing directory in this order:
   `<workspace>/tuya/`, `<workspace>/memory/tuya/`, `~/tuya/`.
3. If multiple candidates exist, use only the highest-precedence directory, report the conflict, and leave the others unchanged.
4. If none exists and the user authorizes persistence, create `<workspace>/tuya/` by default.

Use the selected `<state_root>` for every state path in this skill. Do not write the literal string `<state_root>` to disk.

## Setup

On first use, read `references/setup.md` and align activation boundaries, cloud region context, and write-safety defaults before sending Tuya commands.

## When to Use

Use this skill when the user needs practical execution across the Tuya ecosystem: cloud API authentication, device discovery, DPS-based command control, account linking, or automation orchestration.
Use this instead of generic IoT advice when outcomes depend on Tuya Smart API behavior, regional endpoints, request signing, and command validation.

## Quick Reference

Use the smallest file needed for the current task.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory and workspace templates | `references/memory-template.md` |
| Cloud auth and signing reference | `references/auth-signing.md` |
| User account and home/device linking | `references/account-linking.md` |
| Device commands and state workflows | `references/device-operations.md` |
| Multi-device rollout patterns | `references/orchestration-playbooks.md` |
| Diagnostics and recovery | `references/troubleshooting.md` |
| Architecture and domain traps | `references/domain.md` |
| State path conventions | `references/state.md` |

## Requirements

- Tuya IoT Platform project credentials: Access ID and Access Secret
- Environment variables: `TUYA_ACCESS_ID` and `TUYA_ACCESS_SECRET`
- Correct regional OpenAPI endpoint for the project data center
- Device permissions enabled in the project (Cloud Authorization and required API groups)
- For account-based device binding: configured user permission package and app account flow

Ask users to set credentials via local environment variables instead of pasting production secrets into chat logs. Prefer redacted examples.

## Domain Knowledge

Read `references/domain.md` for architecture, core rules, common traps, external endpoints, security and privacy, and trust details.

## State Management

Read `references/state.md` after `<state_root>` is resolved for the files kept under that directory.
