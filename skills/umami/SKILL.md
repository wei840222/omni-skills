---
name: umami
description: >
  Integrate, configure, and troubleshoot Umami analytics for pageviews, custom
  events, SPA route tracking, self-hosting, and ad-blocker bypass. Use when the
  user deploys Umami, embeds the tracker, wires React/Next.js/Vue apps, or debugs
  missing data. Prefer plausible or matomo for those products; use pg for
  PostgreSQL operations beyond Umami's DATABASE_URL.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"pg":"PostgreSQL operations beyond Umami DATABASE_URL setup.","nextjs":"Next.js app structure when embedding the Umami tracker.","react":"React SPA patterns when placing the tracker or custom events.","vue":"Vue/Nuxt head config when embedding the tracker.","plausible":"Plausible Analytics instead of Umami.","matomo":"Matomo Analytics instead of Umami.","analytics":"General analytics patterns across products."}'
---

# Umami

Privacy-first **web and product analytics** (Umami v3 docs). Cloud or self-hosted.
No cookies in the tracker by default. This skill is **knowledge-only** and keeps
no local runtime state tree.

## When to use

- Install or harden a self-hosted Umami instance (Node 18.18+, PostgreSQL)
- Embed the tracker script and verify pageviews appear
- Wire SPA/Next.js/React/Vue apps or custom events
- Debug zero traffic, ad blockers, wrong website ID, or slow dashboards
- Plan MySQL→PostgreSQL migration before a v3 upgrade

Prefer `plausible` or `matomo` when the product is not Umami. Hand deep Postgres
work to `pg`.

## Progressive disclosure

| Need | Load |
|------|------|
| Tracker embed, SPA, events, Next.js | `references/integration.md` |
| Env vars, DB, hosting, multi-site, secrets | `references/configuration.md` |
| Zero data, blockers, CORS, common mistakes | `references/troubleshooting.md` |
| Official doc anchors for fact checks | `references/sources.md` |

## Core rules

1. **PostgreSQL on current docs** — Install with PostgreSQL ≥ 12.14. For legacy MySQL on v2, finish MySQL→PostgreSQL migration before v3.
2. **`APP_SECRET`** — Set a unique value (`openssl rand -hex 32`) for auth tokens. Current docs use `APP_SECRET` rather than legacy `HASH_SALT`.
3. **Tracker in `<head>`** — Copy the site Tracking code into `<head>` (or Next.js `Script` / root layout) per collect-data guidance.
4. **SPA pageviews are automatic** — The tracker watches History API / `popstate`. Use manual `umami.track()` pageviews only when auto pageviews are disabled or a custom payload is required.
5. **Official Next.js embed** — Use the script tag, `next/script`, or root layout from the SPA guide; do not invent an `@umami/next` dependency.
6. **Match `data-website-id`** — Wrong ID yields silent zero data. Keep dev and prod IDs separate.
7. **Secrets stay out of the package** — `DATABASE_URL`, `APP_SECRET`, and API keys live in env/host secret stores only.

## Workflow

1. Confirm product (Umami vs Plausible/Matomo) and cloud vs self-hosted.
2. For self-host: verify Node, PostgreSQL UTC, `DATABASE_URL`, unique `APP_SECRET`, reverse proxy to port 3000, change default `admin` / `umami` password.
3. Add website → copy tracking code → place in `<head>` → load `references/integration.md` for SPA/events.
4. Verify Network requests to the Umami collect endpoint; if blocked, load bypass guidance from `references/troubleshooting.md`.
5. For facts that may drift (env names, DB support, package names), re-open URLs in `references/sources.md` rather than relying on memory.
