---
name: infrastructure
description: Guide architecture decisions and generate infrastructure provisioning commands for the user to execute.
metadata:
  openclaw: '{"emoji": "\ud83c\udfd7\ufe0f"}'
  related-skills:
    server: skills/server
    docker: skills/docker
---

## Scope

This skill:
- ✅ Guides architecture decisions
- ✅ Provides provisioning commands for user to run
- ✅ Documents infrastructure patterns

**User-driven model:**
- User provides cloud credentials when needed
- User runs provisioning commands
- Skill guides decisions and generates commands

**Safety and Execution:**
- ✅ Treat cloud credentials as ephemeral environment variables provided by the user.
- ✅ Output provisioning commands strictly for the user to copy and execute.
- ✅ Require explicit user confirmation before suggesting any infrastructure modifications.

**For implementation:** User runs commands skill provides, or uses `server` skill for execution.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Architecture patterns | `references/patterns.md` | When designing or scaling application architecture |
| Provider commands | `references/providers.md` | When generating commands for specific cloud providers (AWS, Hetzner, DO) |
| Backup strategies | `references/backups.md` | When setting up or verifying backups |
| Cloud architecture principles | `references/cloud-architecture.md` | When evaluating high-level design, security, and scalability |


## State location

This skill is stateless and does not store local configuration or state.

## Core Rules

### 1. User Runs Commands
Skill generates commands, user executes:
```
Agent: "To create the server, run:
        hcloud server create --name web1 --type cx21 --image ubuntu-24.04
        
        This requires HCLOUD_TOKEN in your environment."
User: [runs command]
```

### 2. Required Tools (User Installs)
| Provider | Tool | Install |
|----------|------|---------|
| Hetzner | `hcloud` | brew install hcloud |
| AWS | `aws` | brew install awscli |
| DigitalOcean | `doctl` | brew install doctl |
| Docker | `docker` | Docker Desktop |

### 3. Credential Handling
- User sets credentials in their environment
- Ensure credential values remain in the user's secure environment space
- Commands reference env vars: `$HCLOUD_TOKEN`, `$AWS_ACCESS_KEY_ID`

### 4. Architecture Guidance

| Stage | Recommended |
|-------|-------------|
| MVP | Single VPS + Docker Compose |
| Growth | Dedicated DB + load balancer |
| Scale | Multi-region + CDN |

### 5. Decision Framework
| Question | Answer |
|----------|--------|
| How to structure infra? | ✅ This skill |
| Should I add another server? | ✅ This skill |
| How to configure nginx? | Use `server` skill |
| How to write Dockerfile? | Use `docker` skill |

### 6. Backup Strategy
| Data | Method | Frequency |
|------|--------|-----------|
| Database | pg_dump → S3/B2 | Daily |
| Volumes | Snapshots | Weekly |
| Config | Git | Every change |
