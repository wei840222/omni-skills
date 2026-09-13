---
name: render-deploy
description: Deploy and host applications on Render using Blueprint generation or Direct Creation. Trigger this skill when deploying, provisioning, or troubleshooting Render services. Trigger specifically for Render, instead of AWS or generic CI/CD pipelines.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "🚀", "requires": {"bins": ["git", "render"], "env": ["RENDER_API_KEY"], "config": ["<state_root>/render-deploy/"]}, "primaryEnv": "RENDER_API_KEY", "install": [{"id": "brew", "kind": "brew", "formula": "render", "bins": ["render"], "label": "Install Render CLI (Homebrew)"}]}'
  related-skills:
  - skills/deploy
  - skills/devops
  - skills/docker
  - skills/ci-cd
  - skills/nodejs
---


## State location

- **Primary**: `<state_root>/render-deploy/` (workspace-specific state)
- **Global**: `<global_state_root>/render-deploy/` (user preferences)

Ask for consent before creating the state directory.

## Setup

On first use, read `references/setup.md` for integration guidelines.
If local memory is needed, ask for consent before creating `<state_root>/render-deploy/`.

## When to Use

Activate when the user asks to deploy, publish, or host an application on Render. This skill handles `render.yaml` Blueprint generation, MCP direct service creation, runtime configuration checks, and post-deploy triage.

## Architecture

Memory lives in `<state_root>/render-deploy/`. See `references/memory-template.md` for setup.

```text
<state_root>/render-deploy/
|- memory.md                  # Stable preferences and integration choices
|- deployment-notes.md        # Project-level deployment decisions
|- env-inventory.md           # Required env vars and source of truth
`- incident-log.md            # Deploy failures and resolved fixes
```

## Quick Reference

Load only the minimum file needed for the current request.

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | Initial configuration or environment setup |
| Memory template | `references/memory-template.md` | Creating or updating memory structure |
| Codebase detection and commands | `references/codebase-analysis.md` | Deciding deployment path based on codebase |
| Blueprint workflow and render.yaml rules | `references/blueprint-workflow.md` | Generating or applying `render.yaml` |
| Authentication and MCP execution mapping | `references/direct-creation.md` | Using Direct Creation or MCP services |
| Startup and healthcheck troubleshooting | `references/troubleshooting.md` | Analyzing failed deploys or crashes |

## Authentication Model

Before any provisioning command, confirm one of these is active:
- `RENDER_API_KEY` is exported in the shell, or
- Render CLI is authenticated (`render whoami -o json`)

For git-backed flows, require `git` and a valid remote URL. Restrict credential discovery and environment inspection to explicitly provided paths.

## Core Rules

### 1. Classify the Deployment Path First
Before proposing commands, decide which path applies:
- Git-backed deploy (Blueprint or Direct Creation)
- Prebuilt Docker image deploy via Dashboard/API

If the repository has no remote, first ask the user to push a remote or switch to dashboard image deploy before proceeding.

### 2. Choose Method by Complexity, Not Preference
Default decision:
- Direct Creation when it is one simple service and no extra infra
- Blueprint when there are multiple services, datastores, cron, workers, or reproducibility requirements

If uncertainty remains, ask one clarifying question and continue.

### 3. Verify Prerequisites Before Any Deploy Action
Run checks in this order:
- `git remote -v` for source availability
- MCP availability (`list_services()`)
- CLI fallback readiness (`render --version`, `render whoami -o json`)
- Active workspace context (MCP or CLI)
- Authentication presence (`RENDER_API_KEY` or authenticated CLI session)

Proceed to deployment steps only after confirming all prerequisites.

### 4. Treat `render.yaml` as Executable Infrastructure
When using Blueprint:
- Declare all required env vars
- Mark user-provided secrets with `sync: false`
- Prefer `plan: free` unless user requests another plan
- Match service type and runtime to the actual app behavior

After creating the file, validate before push.

### 5. Require Push Before Deeplink Handoff
Before sharing a Render Blueprint deeplink, confirm `render.yaml` is committed and pushed to the remote branch. If not pushed, the Dashboard flow will fail to discover the configuration.

### 6. Verify the Deployment and Close With Evidence
After deployment:
- Confirm latest deploy status is live
- Check health endpoint response
- Review recent error logs
- Validate required env vars and port binding (`0.0.0.0:$PORT`)

If failures exist, run one-fix-at-a-time triage from `references/troubleshooting.md`.

## Common Traps

- Starting deploy without a git remote -> Blueprint and MCP git-backed flows fail immediately.
- Picking Direct Creation for multi-service systems -> Missing workers/datastores and fragmented setup.
- Forgetting `sync: false` on secrets -> Broken deploys or accidental secret exposure in config.
- Using localhost binding instead of `0.0.0.0:$PORT` -> Health checks fail even when process is running.
- Redeploying repeatedly without root-cause fix -> Noisy failures and delayed resolution.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://dashboard.render.com | Repository URL, service config, env key names | Blueprint apply flow and dashboard provisioning |
| https://mcp.render.com | Service creation/config requests and workspace-scoped metadata | MCP direct provisioning |
| https://api.render.com | Deployment metadata, logs, service status (via CLI/API) | Validation and operational checks |

No other endpoints should be used unless the user requests an explicit integration.

## Security & Privacy

**Data that leaves your machine:**
- Repository URL and deployment metadata sent to Render services.
- Environment variable names and provided values when the user explicitly sets them.

**Data that stays local:**
- Preferences and deployment history in `<state_root>/render-deploy/` if the user accepts memory.
- Local codebase inspection outputs and interim analysis notes.

**This skill does NOT:**
- Read unrelated credentials outside the deployment context.
- Scrape credentials from shell history, dotfiles, or unrelated config paths.
- Send project files to undeclared third-party endpoints.
- Run destructive infrastructure changes without explicit confirmation.

## Trust

By using this skill, deployment metadata and selected configuration are sent to Render services. Only use it if you trust Render with this operational data.
