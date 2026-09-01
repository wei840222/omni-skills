# Alerting

- Alert evaluates on server — not browser, query must work without variables
- Alert rules run without dashboard variables; express scope with fixed labels or alert rule labels.
- Multiple conditions: AND is default — configure for OR if needed
- Alert state "Pending" before "Firing" — for duration, prevents flapping
- Configure a contact point and notification policy; without a matching policy, a firing alert has no notification delivery.

## Current Grafana Alerting

Grafana Alerting evaluates rules on the server. Dashboard template variables are unavailable to alert rule queries, so express alert scope with fixed labels or rule labels. Test the rule query in the alert rule editor with the same evaluation context before enabling notifications.

For alert delivery, configure a contact point and a notification policy that routes the alert labels to it. When debugging a silent firing alert, check the alert state, matching notification policy, contact point configuration, and notification log in that order.

Source: [Grafana Alerting documentation](https://grafana.com/docs/grafana/latest/alerting/).
