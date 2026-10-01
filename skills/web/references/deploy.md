# Deployment patterns

Load for platform choice, DNS/SSL, env wiring, CORS, and production checklists. Host-specific deep runbooks may still hand off to `deploy` / `netlify-deploy` / `render-deploy`.

## Platform comparison

| Platform | Best for | Gotchas |
|----------|----------|---------|
| Vercel | Next.js, serverless | Function duration limits vary by plan; cold starts on low traffic |
| Netlify | Static + functions | Function timeouts differ by plan; check current docs before promising limits |
| Cloudflare Pages | Static + Workers | Workers are not full Node; enable node compatibility only when required |
| VPS (Docker) | Long-running, full control | You own SSL, patches, backups, scaling |
| Railway / Render | Container apps | Free/low tiers may sleep; cold starts after idle |

Timeouts and plan limits change — verify the vendor page before quoting exact seconds.

## Common deploy issues

- **Works locally, fails in CI/host** — pin Node via `.nvmrc` / `engines`; match package manager lockfile.
- **Missing env vars** — dashboards do not auto-sync from `.env`; set values in the host UI/CLI and **redeploy**.
- **Static export drops API routes** — pure static export has no server handlers; use a platform with functions or a custom server.
- **Trailing slash drift** — pick one policy (`/about` vs `/about/`) to avoid duplicate content and broken assets.
- **Wrong output directory** — `out`, `dist`, `.next`, `build` differ by tool; align host “publish directory” with the bundler.

## DNS and TLS

1. Point apex (`@`) with the records the host documents (A/ALIAS/ANAME) or use their nameservers.
2. Point `www` with CNAME to the host target when required.
3. Wait for propagation (`dig` / DoH); often minutes, occasionally longer.
4. Let the platform provision certificates after DNS resolves; confirm HTTPS before cutting traffic.

## CORS and HTTPS

- **CORS is enforced by browsers** against server responses. Fix `Access-Control-Allow-Origin` (and methods/headers) on the API, or proxy through the same origin. “Disable CORS” browser extensions are not a product fix.
- **Mixed content** — HTTPS pages cannot load active HTTP scripts; upgrade asset URLs.
- Prefer HTTPS redirects at the edge.

## Deployment checklist

- [ ] Env vars set in the host for the target environment (preview vs production)
- [ ] Build command is `build`, not `start` (unless the host expects a long-running process)
- [ ] Publish/output directory matches the framework
- [ ] Node version aligned with local and CI
- [ ] DNS propagated; certificate valid
- [ ] Custom 404 (and critical redirects for migrations)
- [ ] Smoke-test the production URL (HTML shell, one API path, one asset)

## Common requests

- **"Deploy to production"** → Confirm platform, build cmd, output dir, env, DNS, HTTPS, smoke test.
- **"Fix CORS error"** → Inspect response headers on the failing origin; adjust server or same-origin proxy.
