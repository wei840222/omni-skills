# Notify Domain Knowledge

## Notification types and routing

| Type | Channel | Timing | Group |
|------|---------|--------|-------|
| System down, security alert | Push + primary chat | Immediate, 24/7 | Never merge across incidents |
| Deadline <2h, needs action | Primary chat | Immediate | By project |
| Task completed | Primary chat | Batch 5–15 min when related | Yes |
| Daily/weekly summary | Email or chat | Scheduled outside quiet hours | Everything in the window |
| Debug / internal status | Log only | Never user-notify | N/A |

Severity ladder (operational):

1. Debug — logs only
2. Info — digest / batch
3. Action needed soon — primary chat, respect quiet hours unless deadline <2h
4. User-blocking failure — primary chat immediately; quiet hours only if non-critical recovery can wait until 08:00 local
5. Security / system down — push + primary chat, break quiet hours; optional SMS only if configured as critical channel

## Essential constraints

### Empty notifications

```text
BAD:  "Task completed"
GOOD: "Deploy v2.3.1 done. Preview: https://dev.example.com"

BAD:  "Error occurred"
GOOD: "Build failed: missing env var STRIPE_KEY in production"
```

### Notification spam

- Send only for actionable events or final completions
- Batch multiple subtask updates into one summary
- Queue non-critical items instead of sending during quiet hours
- Do not send heartbeat "still running" or "everything OK" pings

### Wrong channel urgency

```text
BAD:  Critical alert via email only
GOOD: Critical alert via push + primary chat (SMS only if configured)

BAD:  Weekly summary via SMS at 23:30 local
GOOD: Weekly summary via email Monday 09:00 local
```

## Formatting rules

### By channel

- **Telegram / Discord / Slack chat**: no markdown tables; short bullets; keep under a readable screenful
- **Email**: full formatting OK; actionable subject line with outcome first
- **SMS**: under 160 characters; most critical fact first
- **Push**: title ≤50 chars; body ≤100 chars

### Universal rules

- Lead with outcome, not process
- Include one clear action when action is required
- Timestamp in the user's timezone
- Context = what + impact + suggested action
- Prefer links over pasted JSON or log walls

## Timing and batching

### Quiet hours

- Default: 23:00–08:00 in the user's timezone when unset
- Severity 5 may break quiet hours
- Queue non-critical items and deliver at 08:00 local (or the user's configured quiet-hours end)

### Batching logic

```text
If 3+ notifications within 5 minutes for the same project:
  → combine into one summary

If notification is informational (severity 1–2):
  → queue for next digest (morning or evening)
```

When batching, preserve distinct failures; never hide a severity ≥4 item inside a soft digest.

## Confirmation format

When scheduling a future or recurring notification, confirm:

```text
Scheduled: "Weekly metrics report"
Every Monday 09:00 (Europe/Madrid)
Via: Email
Respects quiet hours: Yes
```

## Escalation

If the user does not respond to a **critical** alert:

1. Wait 2 hours
2. Send one reminder on the same channel
3. If still no response after 4 hours total, try the configured secondary/critical channel once
4. Contact only the primary user unless explicit permission names others
5. After three attempts, log the failure and stop escalation

## User preferences checklist

Before the first non-critical send, know:

- [ ] Primary channel (chat / email / push target)
- [ ] Timezone
- [ ] Quiet hours (or default 23:00–08:00)
- [ ] Critical alert channel (same or SMS/push)

Store answers under `<state_root>/preferences.md` after consent.

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| "Notification sent" after every action | Trust erosion | Notify on completion or error only |
| Same message to three channels | Redundant noise | One appropriate channel |
| JSON dumps in chat | Unreadable | Format or link to full log |
| "Reminder: X" daily until done | Harassment | Max three reminders, then ask if still relevant |
| Notify on no-change | Pointless | Notify only when state changes or action is needed |
| Breaking quiet hours for info digests | Fatigue | Queue until quiet hours end |

## Recovery framing

When a send is deferred, say what was queued, when it will release, and how the user can override quiet hours for true emergencies.
