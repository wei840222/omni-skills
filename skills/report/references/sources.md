# Report sources and domain notes

Use this file when citing external guidance or refreshing scheduling/format knowledge. Prefer primary docs over secondary blogs. Re-verify versioned APIs before quoting exact flags.

## Scheduling and cron

- **crontab(5) man page (Linux man-pages project)** — field order and special strings for recurring jobs via https://man7.org/linux/man-pages/man5/crontab.5.html
- **OpenClaw automation / cron patterns** — isolated agent-turn jobs for report generation; follow the host's current automation skill or CLI docs rather than inventing job schemas

## Report formats and delivery

- **HTML to PDF via print CSS** — use the host browser PDF action or a maintained HTML-to-PDF tool; keep print CSS page-break rules explicit (see `formats.md`)
- **Telegram / channel delivery** — send only after the user configures destination IDs; never guess chat IDs
- **Webhook delivery** — POST JSON only to user-provided HTTPS endpoints; do not log response bodies that may contain PII

## Security and credentials

- **Environment-variable secrets** — store names in config; values stay in the process environment. Do not commit `.env` files into the skill package.
- **Least privilege** — request only the API scopes needed for the declared metrics

## Obsolete knowledge corrected

- Replaced host-specific `~/Clawic/data/report/` paths with portable `<state_root>/report/` resolution
- Removed Clawic homepage / `_meta.json` promotional packaging from the skill entrypoint
- Treat optional API keys as user-supplied env names, not skill-bundled secrets
