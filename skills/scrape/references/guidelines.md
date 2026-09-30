# Scraping Guidelines

## Pre-Scrape Compliance Checklist

Before writing any scraping code:

1. **robots.txt** — Fetch `{scheme}://{host}/robots.txt`, parse with a robots parser, and check whether the target path is allowed for your User-Agent. If disallowed, halt and report the restriction.
2. **Terms of Service** — Check `/terms`, `/tos`, `/legal` when material. Explicit scraping prohibition means obtain permission or stop.
3. **Data type** — Public factual data (prices, listings, public docs) is lower risk. Personal data triggers GDPR/CCPA-style duties.
4. **Authentication** — Content behind login is off-limits without authorization. Keep scrapers on public content unless the user has explicit rights.
5. **API available?** — If the site offers an official API that covers the need, use it. Scraping when an API exists often violates ToS and is fragile.

## Legal Boundaries (orientation, not advice)

- **Public data, no login** — Often treated as lower risk in US civil scrape disputes (see hiQ v. LinkedIn orientation in `sources.md`); still honor robots/ToS and local law.
- **Bypassing access barriers** — Elevated CFAA-style risk when circumventing authentication or other barriers (see Van Buren orientation in `sources.md`).
- **Ignoring robots.txt** — Often a ToS breach and strong evidence of bad faith even when civil outcomes vary.
- **Personal data without a lawful basis** — GDPR/CCPA exposure; refuse bulk email/phone harvests without authorization.
- **Republishing copyrighted content** — Copyright risk; extract facts, do not mirror protected expression wholesale.

Cite live URLs from `references/sources.md` when making standards or case claims. Escalate multi-issue legal framing to the `legal` skill.

## Request Discipline

- **Rate limit**: Default minimum **2–3 seconds** between requests to the same host; slow further when the site is small or signals strain.
- **User-Agent**: Real browser-like string **plus a contact email** the operator monitors.
- **Respect 429**: Honor `Retry-After` (seconds or HTTP-date). Ignoring repeated 429s is hostile behavior.
- **Session reuse**: Keep-alive / session reuse reduces handshake load.
- **Proactive headers**: Watch `X-RateLimit-Remaining` when present and slow down early.

## Data Handling

- **Strip PII early** — Collect names, emails, or phones only with a clear lawful basis and user authorization.
- **No fingerprinting** — Avoid combining public crumbs solely to re-identify individuals.
- **Minimize storage** — Cache only what the job needs; discard excess; optional notes under resolved `<state_root>/` after consent.
- **Audit trail** — Log what URL, when, and status code as evidence of good-faith politeness.

## Failure and recovery

| Signal | Response |
|--------|----------|
| robots disallow | Stop; report path and user-agent used |
| 401/403 on public URL | Stop; do not rotate credentials or bypass |
| 429 / low remaining | Back off per Retry-After or exponential delay |
| 5xx | Limited retries with exponential backoff + jitter; then fail closed |
| Login wall discovered | Refuse scrape; ask for authorized API or export path |
