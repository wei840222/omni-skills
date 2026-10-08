# Alert Configuration

## Alert Configuration

For `<state_root>/config.json`, use the `config` entry in `assets/alert-examples.json` listed directly in SKILL.md.

## Alert Logic

### When to Alert
- Status change: ok→fail or fail→ok
- After N consecutive failures (failure_threshold)
- Recovery: include duration of outage

### Alert Payload
Use the `failure_payload` entry in `assets/alert-examples.json` listed directly in SKILL.md.

### Recovery Alert
Use the `recovery_payload` entry in `assets/alert-examples.json` listed directly in SKILL.md.

## Channel Implementation

### Pushover
```bash
curl -s -X POST https://api.pushover.net/1/messages.json \
  -d "token=$PUSHOVER_TOKEN" \
  -d "user=$PUSHOVER_USER" \
  -d "message=$MESSAGE"
```

### Webhook
```bash
curl -s -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d "$ALERT_JSON"
```

## Trap: Spam Prevention
- Track last alert per monitor in `<state_root>/alerts/state.json`
- Only alert on STATUS CHANGE, not repeated failures
- Use failure_threshold to avoid flapping alerts
