# Sonoff Access and Authentication

Use this guide to keep auth handling and control mode coherent.

## Credentials

- Cloud mode uses `EWELINK_API_TOKEN` from the environment for agent-side automation, or a documented OAuth/client credential flow when building against CoolKit open-platform materials.
- LAN and DIY local mode may not require a cloud token but still require device eligibility and reachability checks.
- iHost local API uses a short-lived local access token flow against the iHost Open API base URL.

## Auth Rules

1. Load secrets from environment or a secret store; guide setup steps instead of accepting pasted production tokens in chat.
2. Keep raw token values out of `<state_root>/` files; record only presence, scope, and rotation notes.
3. Use least-privilege account scope and rotate tokens when possible.
4. Re-authenticate after repeated unauthorized responses; do not blind-retry writes through a failing credential.

## iHost Token Pattern

Typical local sequence:

1. Request a bridge access token from the local iHost Open API endpoint.
2. Execute REST calls with that token against the same iHost instance.
3. Subscribe to the SSE stream when event confirmation is required.
4. Refresh the token when unauthorized or expired responses appear; replay read-only checks before writes.

## Practical Safeguards

- Verify target device identity before every write.
- Keep cloud id, LAN id, and iHost id mapping in one table.
- Halt rollout on repeated auth or permission drift.
- Treat region, appid, and redirect/OAuth settings as integration-specific; follow current CoolKit docs rather than copying stale hostnames from memory.
