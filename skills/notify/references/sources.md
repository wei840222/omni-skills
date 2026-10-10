# Sources

Verified while refactoring `notify` (2026-10-10). Prefer these over memory when tightening channel, fatigue, or escalation guidance.

## Agent skill format

- [Agent Skills specification](https://agentskills.io/specification) — frontmatter, progressive disclosure, package layout

## Notification UX and fatigue

- [NN/g: Indicators, Validations, and Notifications](https://www.nngroup.com/articles/indicators-validations-notifications/) — distinguish status indicators from interruptive notifications
- [Atlassian: Alert fatigue](https://www.atlassian.com/incident-management/on-call/alert-fatigue) — noise, prioritization, and on-call load

## Platform delivery constraints

- [Apple: Change notification settings on iPhone](https://support.apple.com/guide/iphone/change-notification-settings-iph3e2e428d/ios) — user-controlled quieting and focus behavior
- [Android developers: Notifications overview](https://developer.android.com/develop/ui/views/notifications) — channels, importance, and user control
- [GitHub: Configuring notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) — subscription and delivery preference patterns
- [GitHub Actions: Notifications for workflow runs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/notifications-for-workflow-runs) — completion-oriented CI notify defaults

## Operations / on-call

- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — interrupt budget and sustainable paging
