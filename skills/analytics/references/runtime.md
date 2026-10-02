# Runtime setup and safety

## Environment split

- **Always** use a separate Umami website / Plausible site / PostHog project for local and staging traffic.
- Production pollution (test pageviews, QA emails as persons) is difficult to reverse and skews funnels.

## Tracking domains and hosts

- Drive script hosts and API bases from **environment variables** (for example `NEXT_PUBLIC_UMAMI_URL`, `PLAUSIBLE_DOMAIN`, `POSTHOG_HOST`).
- Switch localhost vs production by env, not by editing hard-coded domains in multiple files.
- Umami: `data-host-url` overrides where the tracker sends data; `data-domains` limits which hostnames run the tracker.
- PostHog: pick US/EU/self-hosted ingest hosts explicitly.

## Script load checks

Before calling vendor helpers:

1. Confirm the script tag is present and not blocked (ad blockers commonly drop analytics hosts).
2. Check globals when applicable: `window.umami`, `window.plausible`, `window.posthog`.
3. For SPA routers, fire manual pageviews on client-side route changes when auto pageview only runs on first load.

## Bots and internal traffic

- Enable vendor bot filtering in project settings when available — privacy-first tools often have weaker bot detection than Google Analytics defaults.
- Exclude staff IPs / internal QA in vendor allow/block lists (Plausible documents IP exclusion; verify IPv4 and IPv6).

## Failure recovery

| Symptom | Check |
|---------|--------|
| Zero pageviews | website/site id mismatch; ad blocker; script in late layout; wrong env host |
| 401/403 on API | wrong key type (stats vs site), missing Bearer, wrong cloud base URL |
| 429 | backoff; reduce Stats API polling; batch PostHog captures where appropriate |
| Skewed persons | PII in properties; shared `distinct_id`; dev traffic in prod project |
