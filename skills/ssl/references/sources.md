# Primary sources (Gate 6)

Use these canonical pages when refreshing facts. Prefer the live document over memorized limits.

## Agent Skills / packaging

- [Agent Skills specification](https://agentskills.io/specification) — frontmatter, progressive disclosure, file references
- [skills-ref validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) — `uvx --from skills-ref agentskills validate`

## Certificate authorities and ACME

- [Let's Encrypt FAQ](https://letsencrypt.org/docs/faq/) — DV-only CA; default cert lifetime **90 days**; renew ~day 60; six-day short-lived option
- [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/) — per-registered-domain and failed-validation budgets; renewals designed to avoid ordinary limits
- [Let's Encrypt Staging](https://letsencrypt.org/docs/staging-environment/) — non-trusted certs for client development
- [Certbot User Guide](https://eff-certbot.readthedocs.io/en/stable/using.html) — `certonly`, `renew`, plugins, dry-run

## TLS configuration baselines

- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/) and [guidelines 5.7 JSON](https://ssl-config.mozilla.org/guidelines/5.7.json) — modern vs intermediate profiles, HSTS `max-age=63072000`, recommended lifespan 90 days

## Server docs

- [Nginx configuring HTTPS servers](https://nginx.org/en/docs/http/configuring_https_servers.html)
- [Nginx ngx_http_v2_module](https://nginx.org/en/docs/http/ngx_http_v2_module.html) — `http2 on;` (separate from `listen ... ssl`)
- [Apache 2.4 SSL how-to](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html)
- [Caddy Automatic HTTPS](https://caddyserver.com/docs/automatic-https)
- [Traefik ACME / Let's Encrypt](https://doc.traefik.io/traefik/https/acme/)
