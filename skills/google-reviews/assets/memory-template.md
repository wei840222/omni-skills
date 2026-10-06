# Memory Template — Google Reviews

Create `<state_root>/memory.md` from this template when the user wants persistence.

```markdown
# Google Reviews Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | done | declined

## Monitoring Context
- Frequently analyzed companies and ownership context
- Source mapping by brand (Business Profile, Places, Shopping/merchant, manual)
- Priority markets or languages to monitor

## Research Patterns
- Typical user questions for one-off company analysis
- Preferred comparison style (single company vs competitor set)
- Evidence depth preference (quick signal vs deep thematic pass)

## Cadence and Alerts
- Heartbeat interval and deep-report cadence
- Alert thresholds for rating drops and negative-review spikes
- Cooldown rules to avoid duplicate alerts

## Reporting Preferences
- Audience: operator, manager, or executive
- Default template: snapshot | heartbeat digest | daily | weekly
- Delivery channel (ask-first if external)

## Connector Notes
- Active access modes per brand
- Known degraded sources and last errors
```
