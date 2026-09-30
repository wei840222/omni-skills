---
name: scrape
description: >
  Scrape public web pages legally with robots.txt checks, polite rate limits,
  session reuse, and GDPR/CCPA-aware data handling. Use when writing or reviewing
  scraping scripts for public factual data (prices, listings, docs). Prefer an
  official API when one exists. Not for browser automation of JS-heavy sites
  (`playwright` / `puppeteer`), pure HTTP protocol debugging (`http`), SEO ranking
  work (`seo`), or full website builds (`web`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🕷️"}'
  related-skills: '{"http":"Protocol-level methods, status codes, caching, and headers beyond scrape fetch loops.","playwright":"JS-rendered pages, locators, and browser automation when plain HTTP is insufficient.","puppeteer":"Chromium-only headless flows, screenshots, and PDF capture.","legal":"Jurisdiction-first IRAC analysis when scrape ToS/CFAA risk needs structured legal framing.","web":"Site architecture and launch work rather than extraction scripts.","seo":"Ranking and Search Console work beyond robots.txt compliance for crawlers."}'
---

## When to load

Load this skill when the user wants **polite, public-web extraction** with compliance checks:

- robots.txt and ToS gate before any fetch loop
- rate-limited HTTP sessions with contactable User-Agent
- PII minimization and audit logging for scrape jobs
- refusing login-walled or personal-data scrapes without authorization

Route away when the task is mainly:

- browser automation / JS rendering → `playwright` or `puppeteer`
- HTTP semantics only → `http`
- ranking strategy → `seo`
- building or hardening a site → `web`
- multi-issue legal IRAC → `legal`

## State location

Optional scrape job notes (targets allowed by robots, rate preferences, audit paths) may live under `<workspace>/scrape/`, `<workspace>/memory/scrape/`, or `~/scrape/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/scrape/`, `<workspace>/memory/scrape/`, `~/scrape/`.
3. If none exists and persistent state must be created, default to `<workspace>/scrape/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.

Use only the selected `<state_root>` for every state operation in this skill. Never invent `<workspace>` from the shell cwd. Keep credentials, cookies for authenticated areas, and raw PII **out of the skill package and out of git**.

```text
<state_root>/
|-- jobs.md          # Dated job notes and allow/deny decisions
|-- audit.log        # Optional fetch audit trail (url, status, time)
`-- preferences.md   # User-approved delay and User-Agent contact email
```

One-off scripts may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Routing

| Need | Load |
|------|------|
| Pre-scrape compliance and legal boundaries | `references/guidelines.md` |
| robots.txt parser, session, rate-limited fetch | `references/code.md` |
| Spec + case/source map | `references/sources.md` |

## Core rules

1. **Gate before fetch.** Check robots.txt for the target path; if disallowed, stop and report. Prefer an official API when one exists.
2. **Public data only by default.** Login-walled content and bulk personal data need explicit authorization; refuse otherwise and cite CFAA / GDPR / CCPA risk.
3. **Be polite.** Minimum 2–3 s between requests (or slower if the site signals), real browser User-Agent plus contact email, honor `429` / `Retry-After`, reuse sessions.
4. **Minimize and log.** Strip unnecessary PII at collection time; keep an audit trail of what/when/where; store only what the job needs under `<state_root>/` after consent.
5. **Escalate tools honestly.** JS-heavy pages go to `playwright`/`puppeteer`; protocol-only questions go to `http`.

## Operating loop

1. Confirm target URL(s), data type (public factual vs personal), and whether an API exists.
2. Load `references/guidelines.md` and run the compliance checklist.
3. Load `references/code.md` when writing or reviewing fetch code.
4. Cite live sources from `references/sources.md` for legal or standards claims; do not invent case holdings from memory.
5. Deliver script or review notes with rate limits, UA, robots gate, and refusal paths explicit.

## Completion check

- robots.txt decision recorded (allow / deny / missing-treated-as-allow with note)
- rate limit and contactable UA present in any generated fetcher
- login-wall and PII paths refused or gated with authorization language
- no secrets or raw PII committed; optional state only under resolved `<state_root>/`
