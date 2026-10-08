# Operations — Paperclip CLI and API

Replace placeholders. Never commit real tokens. Prefer env vars over inline secrets.

## Setup layer (local config / process)

```bash
paperclipai onboard --yes
paperclipai doctor
paperclipai configure
paperclipai run
paperclipai run --data-dir ./tmp/paperclip-dev
paperclipai allowed-hostname host.docker.internal
```

`run` with **no** subcommand starts the server. `run <subcommand>` inspects heartbeat runs via API.

## Auth / context

```bash
paperclipai connect
paperclipai auth login
paperclipai context show
paperclipai context set --api-base http://localhost:3100 --company-id <company-id>
paperclipai context set --api-key-env-var-name PAPERCLIP_API_KEY
export PAPERCLIP_API_KEY=...   # value stays in env; profile stores the *name*
```

Board token vs agent key:

| Persona | Credential | Scope |
|---------|------------|-------|
| Board | `token board create` | Instance/board operations |
| Agent | `token agent create` / `agent local-cli` | One company + one agent |

`local_trusted` loopback can imply board access without browser login.

## Control-plane CLI essentials

```bash
paperclipai company list
paperclipai issue list --status todo,in_progress
paperclipai issue create --title "Define CTO hiring plan" --status todo --priority high
paperclipai approval list --status pending
paperclipai heartbeat run --agent-id <agent-id>
paperclipai agent local-cli <agent-id> -C <company-id>
```

Add `--json` for scripts. Company-scoped commands take `--company-id` / `-C` as documented upstream.

## API identity check

```bash
curl -sS "$PAPERCLIP_API_URL/api/health"

curl -sS "$PAPERCLIP_API_URL/api/agents/me" \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY"
```

## Create a company

```bash
curl -sS -X POST "$PAPERCLIP_API_URL/api/companies" \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"Acme AI","description":"Autonomous product studio"}'
```

On `local_trusted` loopback, board auth may be implicit—still avoid pasting secrets into logs.

## Create and update work

```bash
curl -sS -X POST "$PAPERCLIP_API_URL/api/companies/$PAPERCLIP_COMPANY_ID/issues" \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title":"Draft onboarding system","status":"todo","priority":"high"}'

curl -sS -X PATCH "$PAPERCLIP_API_URL/api/issues/$ISSUE_ID" \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID" \
  -H "Content-Type: application/json" \
  -d '{"status":"done","comment":"Completed and documented the workflow."}'
```

## Operating principle

- CLI setup commands repair local instances; control-plane commands never run the model themselves—they wake adapters server-side.
- Use UI for exploratory board work; use CLI/API for automation and CI.
- If a client “cannot connect,” read the resolved API URL in the error and hit `/api/health` before deeper debugging.
