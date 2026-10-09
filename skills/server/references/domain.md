# Domain Knowledge

## Workflow

Use this ordered path for every service incident, deployment, or exposure change.

1. Map the request path: client → proxy → app → dependency. Identify the hop that reports the symptom and the adjacent hop most likely to own it.
2. Gather read-only evidence first: listener addresses, supervisor state, logs, and the effective proxy/application configuration.
3. Choose one smallest reversible change. Validate configuration syntax before a graceful reload; present restarts, stop/halt commands, firewall changes, and destructive cleanup with impact plus an explicit confirmation step.
4. Verify from the affected path, then record durable service, incident, release, and capacity facts under `<state_root>`.

Read `references/reverse-proxy.md` when deciding how a reverse proxy or TLS termination should divide responsibility between the public edge and the application. Read `references/sources.md` before asserting version-sensitive defaults.

## Core Rules

1. **Name the hops before touching a config.** Client → proxy → app process → dependency. Every fault in this domain lives between two adjacent hops, and the layer that emits the error is rarely the layer that owns it: a 502 is the proxy reporting the app's behavior; a 499 is the client giving up first. Write the chain down, then edit exactly one hop and reload it.
2. **Require supervision.** Anything expected to be running after a reboot is a systemd unit (or a container with a restart policy), with `Restart=on-failure`, an explicit user, and `WantedBy=multi-user.target` so it actually starts at boot. `nohup`, `screen`, and a terminal left open are not deployments — the box reboots for a kernel update at 4am and the service is gone until someone notices.
3. **The timeout ladder runs shortest on the inside.** Each hop's timeout must be strictly shorter than the hop outside it, so a slow request fails as an application error you can read instead of a proxy 504 you cannot. Working ladder: DB statement 5s < app request 15s < proxy read 30s < client/LB idle 60s. Inverting any pair means the outer layer kills a request the inner one was about to answer, and the log that would explain it gets skipped.
4. **Keepalive runs the other way: longest on the inside.** The upstream's idle timeout must exceed the proxy's, or the proxy reuses a connection the app is closing in the same millisecond and the user gets a 502 that no log explains. Node's default `keepAliveTimeout` is 5s against nginx's 75s default `keepalive_timeout` — set the app to proxy keepalive + 5s (Node also needs `headersTimeout` above that). This is a common intermittent 502 in production.
5. **Concurrency is the smaller of two numbers, never the CPU count alone.** For blocking workers: `min(2 × cores + 1, (usable_RAM × 0.75) ÷ RSS_per_worker)`. Four cores, 2 GB usable, 400 MB per worker → CPU says 9, memory says 3, you run 3. Then check the ceiling the database imposes: `processes × pool_size` must stay below `max_connections` minus reserve (Postgres defaults: `max_connections=100`, `superuser_reserved_connections=3`), counting *every* app that shares that database.
6. **Reload, do not restart, anything serving traffic.** `nginx -s reload`, `systemctl reload`, `pm2 reload` drain and hand over; `restart` drops every in-flight request. Validate before applying — `nginx -t`, `caddy validate`, `systemd-analyze verify` — because a reload with a syntax error leaves the old process running while you believe the new config is live, and the next unrelated restart takes the site down with a config nobody edited that day.
7. **Bind to loopback unless the port must be public.** An app on `0.0.0.0:8080` behind a proxy is also reachable directly on 8080, bypassing TLS, auth headers and rate limits. Bind `127.0.0.1` (or a Unix socket) and let the proxy be the only public listener. Where Docker publishes ports, publish as `127.0.0.1:8080:8080` — a bare `-p 8080:8080` writes its own firewall rules ahead of ufw and the port is open to the internet whatever ufw reports.
8. **One release is one directory, and rollback is an artifact, not a rebuild.** Deploy into `releases/<timestamp-or-sha>/`, flip a `current` symlink, reload. Rolling back is flipping the symlink to the previous directory — seconds, no network, no build. "Roll back by redeploying the old commit" is a build you have not tested, run by someone at 3am.
9. **Health checks answer two different questions.** Liveness says "this process is wedged, kill it"; readiness says "do not send me traffic yet". A liveness check that queries the database restarts every app instance during a database blip and turns a 30-second dependency hiccup into a full outage. Liveness: process-local only. Readiness: dependencies included.

## Defaults That Decide Behavior

Unchosen numbers are still numbers you are running. These are the defaults that most often turn out to be the answer. Confirm against `references/sources.md` when the claim is version-sensitive.

| Layer | Default that bites |
|---|---|
| nginx | `client_max_body_size 1m` → 413 on any real upload · `proxy_read_timeout 60s` · `keepalive_timeout 75s` · no `keepalive` to upstreams unless declared, so every proxied request opens a new TCP connection |
| systemd | start-limit burst can leave the unit permanently `failed` · `TimeoutStopSec` 90s before SIGKILL · service `LimitNOFILE` soft often 1024 regardless of your shell · `Type=simple` reports "started" before the app can serve, so ordered units start too early |
| Node.js | `keepAliveTimeout` 5s (Rule 4) · single-threaded: one process serves one CPU |
| Gunicorn | 1 worker · 30s worker timeout · sync worker class serves exactly one request at a time |
| php-fpm | `pm.max_children` caps concurrency; when it is hit the log says so plainly and requests queue in the proxy as 502/504 |
| Postgres | `max_connections` 100 with `superuser_reserved_connections` 3 — the real ceiling on `processes × pool_size` across every app on that database |
| Linux TCP | ephemeral range ~32768-60999 (~28k outbound connections per destination) · `TIME_WAIT` 60s, fixed · listen backlog `somaxconn` 128 on kernels before 5.4, 4096 after |
| Ports | below 1024 needs root or `AmbientCapabilities=CAP_NET_BIND_SERVICE` — keep apps unprivileged on high ports or sockets |
| journald | keeps up to 10% of the filesystem, capped at 4 GB, and is not rotated by logrotate — a chatty service silently owns gigabytes |
| Let's Encrypt | 90-day certificates, renewal around 30 days remaining; duplicate-certificate rate limits punish retry loops |

## Stack Defaults

One default per need, with the condition that overrides it.

| Need | Default | Switch when |
|---|---|---|
| Terminate HTTPS for 1-20 sites | Caddy | Existing nginx expertise, or a directive Caddy does not expose |
| Route to many containers that come and go | Traefik with the Docker provider | The set of services is static — labels add moving parts for nothing (→ Caddy/nginx) |
| Very high connection counts, TCP/UDP balancing | HAProxy | Not needed below the point where one box saturates (→ keep the proxy you have) |
| Supervise a long-running app on a VM | systemd unit | The whole box already runs Compose (→ container restart policy) |
| Node process management | systemd, one process per core via the app | The team already lives in PM2 tooling (→ PM2 in cluster mode) |
| Python WSGI/ASGI | Gunicorn with uvicorn workers behind the proxy | Pure-async app with no WSGI need (→ uvicorn directly, still behind a proxy) |
| Serve static files | The proxy, directly from disk | Global audience or heavy egress (→ CDN in front, same headers) |
| App-to-proxy transport | Unix socket on the same host | Proxy and app on different hosts (→ TCP on a private interface) |
| Multiple apps on one box | Compose stack per app + one shared proxy network | Only one app exists (→ do not add Docker for a single process) |

## Where Experts Disagree

- **Containers vs packages on a single box.** Containers give a reproducible runtime and painless rollback; a systemd unit with the distro's runtime gives fewer layers to debug at 3am and no image registry to depend on. The frontier is the number of services: past three or four with conflicting runtimes, containers win; for one Go binary they are pure overhead.
- **Where TLS terminates.** Terminating at a CDN or load balancer is simpler and gets you a cert requiring zero local handling; terminating on the box keeps traffic encrypted end to end and keeps you working when the provider's edge has an incident. Regulated data pushes to end-to-end; everything else does fine terminating at the edge with an internal hop over a private network.
- **Reverse proxy on the host or in a container.** Host-installed proxies survive a container-daemon restart and see the real client IP without extra work; containerized proxies deploy with the rest of the stack. Teams that already do everything with Compose should keep the proxy inside Compose as well.
- **Zero-downtime on one machine.** One camp says a symlink flip and a graceful reload is enough; the other says anything that matters needs two instances behind a proxy. Both are right at different sizes — the honest question is whether losing ~200ms of connections during a deploy costs anything measurable to your users.

## Security & Privacy

**Credentials:** this skill configures services that need secrets (database URLs, API tokens, TLS private keys). It does not store, copy, or transmit them: secrets stay in the environment, the OS keychain, or the secret manager the user already runs, and only pointers such as `env:DATABASE_URL` or `file:/etc/myapp/env` are recorded under `<state_root>/`.

**Local storage:** service inventory, baselines, releases, incidents and runbooks stay in `<state_root>/` on this machine; hosts and domains in the shared boxes. Hostnames, ports and unit names only — no keys, no passwords.

**Guardrails:** diagnostic commands are read-only by default. Service-affecting operations (restart, stop/halt, down, prune, volume removal, firewall changes) are presented with their impact and require explicit confirmation before running.
