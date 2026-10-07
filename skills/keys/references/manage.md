# Key management

Guide the user through local keychain commands. Prefer prompts that accept the secret on a local TTY. Do not ask the user to paste API keys into chat, tickets, or git.

Service names must match broker keys: lowercase letters, digits, `_`, `-` only. Keychain account attribute on macOS is `$USER`; service attribute is `keys:<service>` (example: `keys:openai`).

## Add a key

### macOS

Interactive-friendly pattern (user runs locally):

```bash
security add-generic-password -s "keys:SERVICE" -a "$USER" -w
# if the installed security(1) requires the password inline, the user supplies -w ONLY in their own terminal:
# security add-generic-password -s "keys:SERVICE" -a "$USER" -w 'paste-locally-not-in-chat'
```

### Linux (libsecret / secret-tool)

```bash
secret-tool store --label="SERVICE API Key" service keys:SERVICE
# secret-tool prompts on the TTY for the secret value
```

## Update (rotate) a key

### macOS

```bash
security delete-generic-password -s "keys:SERVICE" -a "$USER"
security add-generic-password -s "keys:SERVICE" -a "$USER" -w
```

### Linux

```bash
secret-tool clear service keys:SERVICE
secret-tool store --label="SERVICE API Key" service keys:SERVICE
```

## Remove a key

### macOS

```bash
security delete-generic-password -s "keys:SERVICE" -a "$USER"
```

### Linux

```bash
secret-tool clear service keys:SERVICE
```

## Verify a key exists (user terminal only)

These commands print the secret. Run them only in the user's local terminal when diagnosing "Key not found"; do not capture stdout into agent context.

```bash
# macOS
security find-generic-password -s "keys:SERVICE" -a "$USER" -w >/dev/null && echo "present"

# Linux — prefer a non-printing check when possible; lookup still returns the secret
secret-tool lookup service keys:SERVICE >/dev/null && echo "present"
```

After rotation, confirm with a low-risk broker call (for example `keys-broker ping` cannot see keys; use a documented read-only API endpoint for that service).

## Extend the broker allowlist

1. Edit `scripts/keys-broker.sh` and add one regex under `ALLOWED_URLS`:

```bash
declare -A ALLOWED_URLS=(
    ["openai"]="^https://api\.openai\.com/"
    ["anthropic"]="^https://api\.anthropic\.com/"
    ["stripe"]="^https://api\.stripe\.com/"
    ["github"]="^https://api\.github\.com/"
    ["myservice"]="^https://api\.myservice\.com/"
)
```

2. Reinstall onto PATH (`install -m 0755 scripts/keys-broker.sh ~/.local/bin/keys-broker`).
3. Store `keys:myservice` in the keychain.
4. Call only HTTPS URLs that match the new prefix.

Allowlist entries are security controls: keep them as tight prefixes, require HTTPS, and obtain user consent before adding a destination that can receive the bearer token.

## Default services and where users create keys

| Service | Typical key prefix (informational) | Console |
|---------|------------------------------------|---------|
| openai | `sk-…` | https://platform.openai.com/api-keys |
| anthropic | `sk-ant-…` | https://console.anthropic.com/settings/keys |
| stripe | `sk_test_…` / `sk_live_…` | https://dashboard.stripe.com/apikeys |
| github | `ghp_…` fine-grained / classic PAT | https://github.com/settings/tokens |

Prefixes change over time; trust the provider console over this table. Prefer least-privilege tokens and revoke on rotation.

## Example authenticated calls

```bash
# OpenAI chat completions
keys-broker call '{"action":"call","service":"openai","url":"https://api.openai.com/v1/chat/completions","method":"POST","body":{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}}'

# Stripe list customers (read-only style probe after storing keys:stripe)
keys-broker call '{"action":"call","service":"stripe","url":"https://api.stripe.com/v1/customers?limit=1","method":"GET","body":null}'

# GitHub current user
keys-broker call '{"action":"call","service":"github","url":"https://api.github.com/user","method":"GET","body":null}'
```

Replace models and paths with current provider docs when the upstream API drifts.

## Upstream API docs (verify before path changes)

- OpenAI Auth / API reference: https://platform.openai.com/docs/api-reference/authentication
- Anthropic API keys: https://docs.anthropic.com/en/api/getting-started
- Stripe authentication: https://docs.stripe.com/api/authentication
- GitHub REST authentication: https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api
