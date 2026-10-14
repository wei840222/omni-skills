---
name: beszel
description: >
  Deploy, secure, and troubleshoot Beszel monitoring with hub/agent topology,
  Docker or binary agents, alert calibration, and upgrade-safe operations for
  self-hosted servers. Use when planning Beszel coverage, onboarding agents,
  tuning noisy alerts, diagnosing disconnects, or rolling out hub/agent upgrades.
  Prefer `monitoring` for vendor-neutral observability strategy, `server` for
  host-level service diagnosis, `self-host` for whole-stack hardening,
  `docker`/`docker-compose` for container runtime mechanics, and `home-server`
  for broader homelab design beyond Beszel itself.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊","requires":{"anyBins":["docker","podman"]},"configPaths":["<state_root>/"]}'
  related-skills: '{"monitoring":"Vendor-neutral observability strategy when Beszel is only one tool among several.","server":"Host service diagnosis when the issue is not Beszel-specific.","self-host":"Whole-service self-host hardening beyond Beszel hub/agent ops.","docker":"Container runtime and image debugging for hub/agent containers.","docker-compose":"Compose wiring for multi-service hub/agent stacks.","home-server":"Homelab architecture when Beszel is one service in a larger household stack."}'
---

## Setup

On first use, explain planned local storage in `<state_root>/` and ask for confirmation before creating or updating files. Resolve `<state_root>` from an explicit host/user path when present; otherwise prefer `<workspace>/beszel/`, then `<workspace>/memory/beszel/`, then `~/beszel/`.

## When to Use

Load this skill when the user needs help planning, deploying, or maintaining Beszel for infrastructure monitoring: hub/agent topology, secure agent onboarding, alert calibration, disconnect triage, or upgrade-safe rollouts.

Prefer more specific skills when the ask is narrow:

- `monitoring` — cross-tool observability architecture
- `server` — host service diagnosis outside Beszel
- `self-host` — broader self-host stack hardening
- `docker` / `docker-compose` — container runtime or Compose debugging
- `home-server` — household/homelab design beyond one monitoring product

## Architecture

Beszel has two runtime components: a **hub** (PocketBase-based dashboard) and an **agent** on each monitored system. Skill memory lives in `<state_root>/`. See `assets/data-templates.md` for templates and `references/sources.md` for official docs.

```text
<state_root>/
├── memory.md                  # Current environment, goals, and priorities
├── nodes.md                   # Agent inventory and ownership
├── alerts.md                  # Alert thresholds and escalation targets
└── incidents.md               # Incident timeline and recovery notes
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup behavior | `references/setup.md` |
| Memory structure | `assets/data-templates.md` |
| Deployment topologies | `references/deployment-patterns.md` |
| Alert calibration workflow | `references/alert-tuning.md` |
| Diagnostics and recovery | `references/diagnostics-playbook.md` |
| Core rules & security | `references/domain.md` |
| Official sources | `references/sources.md` |

## Data Storage

All skill state files are stored in `<state_root>/`.
Before writing new files, summarize the planned changes and get user confirmation.

## Operating Guidelines

Read `references/domain.md` for core rules, common traps, and security boundaries. Keep product facts anchored to `references/sources.md` rather than inventing version-specific claims.
