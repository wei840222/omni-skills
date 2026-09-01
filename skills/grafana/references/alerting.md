# Alerting

- Alert evaluates on server — not browser, query must work without variables
- Variables not supported in alerts — hardcode values or use templates
- Multiple conditions: AND is default — configure for OR if needed
- Alert state "Pending" before "Firing" — for duration, prevents flapping
- Notification channel must be configured — alert without channel = no notification
