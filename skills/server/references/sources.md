# Primary sources (Gate 6)

Use these canonical pages when refreshing facts. Prefer the live document over memorized limits.

## Agent Skills / packaging

- [Agent Skills specification](https://agentskills.io/specification) — frontmatter, progressive disclosure, file references
- [skills-ref validator](https://github.com/agentskills/agentskills/tree/main/skills-ref) — `uvx --from skills-ref agentskills validate`

## Reverse proxy and HTTP edge

- [nginx ngx_http_core_module](https://nginx.org/en/docs/http/ngx_http_core_module.html) — `client_max_body_size` default `1m`; `keepalive_timeout` default `75s`
- [nginx ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) — `proxy_read_timeout` default `60s`; upstream `keepalive`
- [MDN: Proxy servers and tunneling](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling)
- [Caddy reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [Traefik Docker provider](https://doc.traefik.io/traefik/providers/docker/)
- [HAProxy documentation](https://www.haproxy.org/#docs)

## Process supervision and Node/Python runtimes

- [systemd.service(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — `Type=`, restart behavior, stop timeouts
- [systemd-analyze](https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html) — `verify` before enabling units
- [Node.js http.Server](https://nodejs.org/api/http.html) — `keepAliveTimeout` (default 5000 ms), `headersTimeout`
- [Gunicorn settings](https://docs.gunicorn.org/en/stable/settings.html) — workers, timeout, worker class
- [PHP-FPM configuration](https://www.php.net/manual/en/install.fpm.configuration.php) — `pm.max_children`

## Databases and TCP limits that cap concurrency

- [PostgreSQL connection settings](https://www.postgresql.org/docs/current/runtime-config-connection.html) — `max_connections` default 100; `superuser_reserved_connections` default 3
- [Linux `ip(7)` / ephemeral ports](https://man7.org/linux/man-pages/man7/ip.7.html) — outbound connection budget context

## TLS lifetime (edge renewal expectations)

- [Let's Encrypt FAQ](https://letsencrypt.org/docs/faq/) — default certificate lifetime 90 days
- [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/) — duplicate-certificate and failed-validation budgets

## Containers on a single host

- [Docker networking publish](https://docs.docker.com/engine/network/) — published ports and host firewall interaction
- [Compose networking](https://docs.docker.com/compose/networking/) — per-app stacks and external proxy networks
