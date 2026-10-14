# Dashboard Domain Rules

## Architecture

```text
[User cron/manual] → [fetch.sh] → [data.json] → [index.html]
                           ↓
                 Uses env credentials only
```

The agent generates scripts and HTML. The user runs collectors.

## Fetch script template

Resolve `$STATE_ROOT` before writing the script. Example Stripe balance snapshot
(useful for treasury/cash views; **not** MRR):

```bash
#!/usr/bin/env bash
set -euo pipefail
# Requires: STRIPE_API_KEY or STRIPE_SECRET_KEY in the environment
# STATE_ROOT must be the resolved dashboard state root (absolute path)
: "${STATE_ROOT:?STATE_ROOT is required}"
KEY="${STRIPE_API_KEY:-${STRIPE_SECRET_KEY:-}}"
: "${KEY:?Set STRIPE_API_KEY or STRIPE_SECRET_KEY}"
mkdir -p "$STATE_ROOT/dashboard/stripe"
curl -sS -u "${KEY}:" \
  https://api.stripe.com/v1/balance \
  | jq '.' > "$STATE_ROOT/dashboard/stripe/data.json"
```

For subscription revenue dashboards, prefer Stripe Billing/Subscriptions or
Reporting APIs (or exported metrics) rather than `/v1/balance`. Confirm the
endpoint against current Stripe docs before hard-coding field names.

Docker CPU example shape:

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${STATE_ROOT:?STATE_ROOT is required}"
mkdir -p "$STATE_ROOT/dashboard/docker"
docker stats --no-stream --format '{{json .}}' \
  | jq -s '.' > "$STATE_ROOT/dashboard/docker/data.json"
```

## Design defaults

| Element | Value |
|---------|-------|
| Background | `#0f172a` (dark) / `#f8fafc` (light) |
| Text | `#e2e8f0` (dark) / `#1e293b` (light) |
| Spacing | 16px, 24px, 32px |
| Corners | 8px |
| KPI | 48–72px number, 14px label |

## Security

- Credentials via env vars or secret-store pointers; keep secrets out of files
- Serve on `127.0.0.1` by default
- No raw PII in displayed tables without explicit user request and minimization
- User owns auth if exposing beyond localhost
- Generated scripts should use `set -euo pipefail` and fail if required env is missing
