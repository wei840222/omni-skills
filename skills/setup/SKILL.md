---
name: setup
description: Configure OpenClaw installations — channels, security hardening,
  gateway/Tailscale exposure, tools/exec policy, automation, and production
  recommendations. Trigger for first-time setup, dmPolicy/allowlist changes,
  remote gateway auth, or openclaw doctor/onboard follow-up.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "\u2699\ufe0f"}'
---
This skill guides host OpenClaw configuration under `~/.openclaw/`. It is
stateless and does not store local skill state or persistent user notes.

## Resource Loading

Load these references as needed for specific configuration tasks:

| Task | Load |
|------|------|
| Messaging channels (Telegram, WhatsApp, Discord, etc.) | `references/channels.md` |
| Agent settings, models, workspaces | `references/agents.md` |
| Security, auth, DM policies, allowlists | `references/security.md` |
| Tools: exec, browser, web, media | `references/tools.md` |
| Cron, hooks, heartbeats, automation | `references/automation.md` |
| Recommendations by use case | `references/recommendations.md` |
| Memory search, embeddings, QMD | `references/memory.md` |
| Gateway: port, TLS, Tailscale, remote | `references/gateway.md` |

---

## First Setup Checklist

Before any config, run:
```bash
openclaw onboard --install-daemon  # Full wizard
openclaw doctor                    # Check issues
```

**Minimum viable config:**
- [ ] At least one channel connected (Telegram recommended for testing)
- [ ] Model configured (Anthropic Claude or OpenAI)
- [ ] Workspace path set (`agents.defaults.workspace`)
- [ ] Owner allowlist configured (your user ID in `channels.*.allowFrom`)

---

## Config Locations

| File | Purpose |
|------|---------|
| `~/.openclaw/openclaw.json` | Main config |
| `~/.openclaw/.env` | Environment variables |
| `~/.openclaw/workspace/` | Default workspace |
| `~/.openclaw/sessions/` | Session storage |

**Hot reload:** Most settings apply instantly. Gateway settings (port, TLS) require restart.

---

## Common Configuration Issues

1. **Open DM policy without allowlist** → Anyone can message your bot
2. **No auth token on remote gateway** → Exposed to internet
3. **Model without fallbacks** → Single point of failure
4. **Heartbeat without delivery target** → Lost proactive messages
5. **exec.security: "full" in groups** → Dangerous command access

---

## When You're Done

```bash
openclaw doctor       # Verify config
openclaw status       # Check runtime
openclaw health       # Gateway health
```
