# Cron Basics and Domain Knowledge

Cron is a time-based job scheduler. A scheduled task is commonly called a "cron job". The classic UNIX crontab uses five fields: minute, hour, day of month, month, and day of week.

## Field order

```text
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, Sunday=0 or 7)
│ │ │ │ │
* * * * *
```

Common expressions:

- `* * * * *` — every minute
- `0 * * * *` — every hour at minute 0
- `0 0 * * *` — every day at midnight
- `0 9 * * 1-5` — every weekday at 09:00

## Timezones and DST

- Cron expressions are meaningless without an explicit timezone. Persist the user's IANA zone (for example `Asia/Taipei`) with every job.
- During spring-forward, local times in the skipped hour may never fire; during fall-back, times in the repeated hour may fire twice unless the runtime de-duplicates.
- Prefer asking for wall-clock confirmation ("Tuesday 09:00 Asia/Taipei") over relative phrases such as "tomorrow morning".

## Sources

- crontab(5) man page — field semantics and special strings via https://man7.org/linux/man-pages/man5/crontab.5.html
- IANA Time Zone Database — canonical zone names via https://www.iana.org/time-zones
- IETF RFC 5545 §3.3.10 — recurrence concepts useful when mapping human schedules via https://www.rfc-editor.org/rfc/rfc5545#section-3.3.10
- Wikipedia Cron overview — historical context only via https://en.wikipedia.org/wiki/Cron
