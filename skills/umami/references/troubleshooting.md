# Troubleshooting — Umami

## Zero pageviews

1. Browser **Network** tab: confirm the tracker script loads (no 404) and a collect/send request reaches your Umami host.
2. Confirm `data-website-id` matches the website in the dashboard.
3. Ad blockers / privacy extensions — proxy or rename script + collect path (Bypass ad blockers).
4. Mixed content or wrong `data-host-url` when script and API hosts differ.
5. Dev vs prod sharing one website ID — separates noise; use `data-domains` or separate websites.

## Script or collect failures

- **404 on script** — wrong public URL, reverse-proxy path, or `TRACKER_SCRIPT_NAME` mismatch.
- **CORS** — cross-origin collect without proper proxy; prefer first-party proxy.
- **Console errors on `umami`** — script blocked or loaded after code that assumes it exists.

## SPA “missing” route hits

Default tracker already records client-side navigations. If routes are missing:

- Check whether `data-auto-track` or `data-auto-pageview` was set to `false`.
- Confirm the framework actually changes History API URLs.
- Only then add manual `umami.track()` pageviews.

## Dashboard / ops

- Slow dashboard — inspect PostgreSQL load, vacuum/indexes, and host resources (DB usually dominates).
- Expect a short delay before UI refresh; not always instantaneous.
- After fresh install, change default `admin` / `umami` credentials immediately.
- Exclude own traffic with `localStorage.setItem('umami.disabled', 1)` per tracked origin when needed.

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Citing `HASH_SALT` | Use `APP_SECRET` |
| Claiming MySQL is fine on v3 | PostgreSQL only; migrate on v2 first |
| Requiring manual SPA `umami.track()` always | Auto History tracking is default |
| Recommending `@umami/next` | Use script / `next/script` / layout |
| Putting tracker only in late body and assuming head is wrong | Official collect-data uses `<head>` |
| Same website ID for local and production | Separate websites or `data-domains` |
