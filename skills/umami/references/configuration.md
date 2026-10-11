# Configuration — Umami

Self-host and multi-site setup. Re-check `sources.md` when env names or DB support may have changed.

## Database

- **Current install path:** PostgreSQL only (minimum v12.14). Prefer UTC on the database.
- **Required env:** `DATABASE_URL=postgresql://user:***@host:5432/dbname`
- **SQLite:** not supported.
- **MySQL:** supported historically on Umami v2; **removed as a supported option in v3**. Before upgrading to v3, migrate MySQL → PostgreSQL on a v2.19.0-compatible schema (see official Migrate MySQL to PostgreSQL guide).
- All tracking data, users, and config live in the database — backup strategy = database backup.

## Secrets and runtime env

| Variable | Role |
|----------|------|
| `DATABASE_URL` | Required connection string |
| `APP_SECRET` | Random string securing auth tokens; unique per install (`openssl rand -hex 32`) |
| `COLLECT_API_ENDPOINT` | Optional alternate collect path to reduce ad-block hits |
| `CLIENT_IP_HEADER` | When behind a proxy with non-standard client IP headers |
| `DISABLE_TELEMETRY` | Opt out of anonymous product telemetry |
| `TRACKER_SCRIPT_NAME` | Custom tracker filename (no automatic `.js` suffix) |

Do **not** instruct users to set `HASH_SALT` — current docs use `APP_SECRET`.

Default first login after fresh DB setup: username `admin`, password `umami`. Change immediately.

## Process and hosting

- App listens on `http://localhost:3000` by default; put HTTPS termination and reverse proxy in front (Nginx, Caddy, platform proxy, etc.).
- Node.js **18.18+**; install paths include source (`pnpm`), Docker Compose, prebuilt image, or third-party Helm.
- PostgreSQL often needs more RAM/CPU planning than the Node process itself; small sites can run Umami on modest RAM, but size the DB honestly.
- Managed Postgres and app hosts are listed in the official Hosting guide (Vercel/Netlify/Railway/etc. still need a Postgres somewhere).

## Multi-site

- One Umami instance can serve many websites (Dashboard → Settings/Websites).
- Each site has its own tracking snippet / `data-website-id`.
- Share URL is per-website and opt-in; metrics stay private until a Share URL is created.
