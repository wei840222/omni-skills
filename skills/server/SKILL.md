---
name: server
description: 'Manages web and application services, process supervision, ports, and restart loops. Handles reverse proxy configurations, TLS termination, worker sizing, deployments, and troubleshooting for services running on a host.'
metadata:
  openclaw: '{"emoji":"🖥️"}'
  related-skills: '{"nginx": "directive-level nginx configuration and debugging", "ssl": "certificate issuance, renewal, and chain problems", "linux": "the host underneath: boot, disks, permissions, cron, OOM", "docker": "building images and container runtime internals", "vps": "provisioning, SSH hardening, and firewalling the machine itself"}'
---
## State location

- `<workspace>/server/` (Highest priority, created by default if none exist)
- `<workspace>/memory/server/`
- `~/server/`

This skill follows the workspace-first state convention. Resolve `<state_root>` once per session by checking the candidate locations in order. Use the first one that exists. If none exist, create and use `<workspace>/server/`. All runtime data must be stored under `<state_root>`.


**Data.** At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, and it is a dynamically generated list based on active conditions. What the user declared wins: an observation always preserves existing `config.yaml` values unless explicit user override is provided. Read `<workspace>/servers/servers.md` before any deploy, sizing, capacity or "what is running where" question, and `<workspace>/domains/domains.md` before touching a hostname, vhost, or certificate. If none of it exists, work from defaults and say nothing about it. If you have data at an old location (`~/.clawic/server/` or `~/server/`), move it to `<state_root>/`, and say in one line that you moved it and from where. Everything this skill reads or writes is a plain local note under `<state_root>` — nothing leaves the machine and ensure all credentials use safe pointer references (e.g. env:KEY). In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, is strictly read-only and must be preserved, and every write and deletion is named in one line as it happens.

**Write before the session ends** whenever the session produced something durable: a service deployed, moved, renamed or retired; a host discovered or decommissioned; a hostname or certificate wired; a release or a rollback; an outage and what actually caused it; a measured number (worker count, RSS per worker, requests per second, p95); or something the user will want to read again — a runbook, a unit file or vhost that finally worked, a topology decision, a load-test report. `memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**Hosts go to the shared inventory `<workspace>/servers/servers.md`** and **domains to `<workspace>/domains/domains.md`**, not here: those files are shared with every other infrastructure skill, so "what do I have" answers itself whoever wrote the row. What belongs to this skill is the *service* layer — which process runs where, on which port, under which supervisor. A person or a project that turns up in this work has its own shared box as well (`<workspace>/contacts/`, `<workspace>/projects/`): the record lives there, only the name stays here.

**Credentials are never written to persistent notes.** — not in the files named here, not in a file you create, not in text the user pastes in to be saved. Replace the value with its pointer before writing: `env:DATABASE_URL`, `keychain:deploy-key`, `file:/etc/myapp/env`, `1password:Infra/prod-db`.

A server is not interesting; the request path through it is. Before configuring anything, name the hops a request takes — client → proxy → app process → dependency — because every symptom in this domain is a mismatch between two adjacent hops (a timeout, a header, a keepalive, a limit). Give the exact file to edit and the reload command that applies it, then say what breaks if it is wrong. Work from defaults immediately: always work from defaults and wait for the user to provide their stack details. Precedence for any value: `config.yaml` → `<workspace>/profile.yaml` (shared universals) → the Configuration table default.



## When To Use

- Getting a web or application service running on a machine and surviving reboots, logouts, and crashes: unit files, process managers, sockets, users, ports
- The service runs but nobody can reach it, or the proxy answers instead of the app: refused connections, wrong interface, 502/504/413/499, redirect loops, broken WebSockets or uploads
- Sizing and tuning what is already live: workers, threads, connection pools, keepalive, timeouts, file descriptors, static-file and compression settings
- Shipping a new version onto a box and being able to undo it: release layout, migration order, health-gated restart, rollback
- Running other people's software on your own hardware: Compose stacks, self-hosted apps, media and game servers
- Keeping it alive: hardening, log rotation, disk, certificate reloads, health checks, backups and restores
- Not for nginx directive-level tuning (`nginx`), Caddyfile syntax (`caddy`), issuing or renewing certificates (`ssl`), host OS failures such as boot, cron, disk or permissions (`linux`), building images (`docker`), Kubernetes (`k8s`), or provisioning and firewalling the machine (`vps`) — this covers the service that sits on top of all of them

## Workflow

Use this ordered path for every service incident, deployment, or exposure change.

1. Map the request path: client → proxy → app → dependency. Identify the hop that reports the symptom and the adjacent hop most likely to own it.
2. Gather read-only evidence first: listener addresses, supervisor state, logs, and the effective proxy/application configuration.
3. Choose one smallest reversible change. Validate configuration syntax before a graceful reload; present restarts, stop commands, firewall changes, and destructive cleanup with impact plus an explicit confirmation step.
4. Verify from the affected path, then record durable service, incident, release, and capacity facts under `<state_root>`.

Read `references/reverse-proxy.md` when deciding how a reverse proxy or TLS termination should divide responsibility between the public edge and the application.

## Core Rules

1. **Name the hops before touching a config.** Client → proxy → app process → dependency. Every fault in this domain lives between two adjacent hops, and the layer that emits the error is rarely the layer that owns it: a 502 is the proxy reporting the app's behavior, a 499 is the client giving up first. Write the chain down, then edit exactly one hop and reload it.
2. **Supervised or it does not exist.** Anything expected to be running after a reboot is a systemd unit (or a container with a restart policy), with `Restart=on-failure`, an explicit user, and `WantedBy=multi-user.target` so it actually starts at boot. `nohup`, `screen`, and a terminal left open are not deployments — the box reboots for a kernel update at 4am and the service is gone until someone notices.
3. **The timeout ladder runs shortest on the inside.** Each hop's timeout must be strictly shorter than the hop outside it, so a slow request fails as an application error you can read instead of a proxy 504 you cannot. Working ladder: DB statement 5s < app request 15s < proxy read 30s < client/LB idle 60s. Inverting any pair means the outer layer kills a request the inner one was about to answer, and the log that would explain it gets skipped.
4. **Keepalive runs the other way: longest on the inside.** The upstream's idle timeout must exceed the proxy's, or the proxy reuses a connection the app is closing in the same millisecond and the user gets a 502 that no log explains. Node's default `keepAliveTimeout` is 5s against nginx's 75s default keepalive — set the app to proxy keepalive + 5s (Node also needs `headersTimeout` above that). This is the single most common intermittent 502 in production.
5. **Concurrency is the smaller of two numbers, never the CPU one alone.** For blocking workers: `min( 2 × cores + 1 , (usable_RAM × 0.75) ÷ RSS_per_worker )`. Four cores, 2 GB usable, 400 MB per worker → CPU says 9, memory says 3, you run 3. Then check the ceiling the database imposes: `processes × pool_size` must stay below `max_connections` minus reserve (Postgres defaults: 100 and 3), counting *every* app that shares that database.
6. **Reload, do not restart, anything serving traffic.** `nginx -s reload`, `systemctl reload`, `pm2 reload` drain and hand over; `restart` drops every in-flight request. Validate before applying — `nginx -t`, `caddy validate`, `systemd-analyze verify` — because a reload with a syntax error leaves the old process running while you believe the new config is live, and the next unrelated restart takes the site down with a config nobody edited that day.
7. **Bind to loopback unless the port must be public.** An app on `0.0.0.0:8080` behind a proxy is also reachable directly on 8080, bypassing TLS, auth headers and rate limits. Bind `127.0.0.1` (or a Unix socket) and let the proxy be the only public listener. Where Docker publishes ports, publish as `127.0.0.1:8080:8080` — a bare `-p 8080:8080` writes its own firewall rules ahead of ufw and the port is open to the internet whatever ufw reports.
8. **One release is one directory, and rollback is an artifact, not a rebuild.** Deploy into `releases/<timestamp-or-sha>/`, flip a `current` symlink, reload. Rolling back is flipping the symlink to the previous directory — seconds, no network, no build. "Roll back by redeploying the old commit" is a build you have not tested, run by someone at 3am.
9. **Health checks answer two different questions.** Liveness says "this process is wedged, kill it"; readiness says "do not send me traffic yet". A liveness check that queries the database restarts every app instance during a database blip and turns a 30-second dependency hiccup into a full outage. Liveness: process-local only. Readiness: dependencies included.

## Failure Signatures

Decode rule: the error names the hop that *noticed*, not the hop at fault. Refused means something answered with a rejection; timed out means nothing answered at all.

| Signature | Most likely cause | First move |
|---|---|---|
| `Connection refused` from outside, works on the box | Listening on `127.0.0.1`, not on the public interface — or the proxy is not running | `ss -tlnp` and read the *Local Address* column: `127.0.0.1:8080` and `0.0.0.0:8080` are different diagnoses |
| `Connection timed out` from outside | Packets dropped: host firewall, cloud security group, or the wrong host entirely | Refused = reached and rejected; timed out = did not arrive. Never debug both the same way |
| `Address already in use` on start | Old process still holds the port, or two units define it | Find the holder (`ss -tlnp` / `lsof -i :PORT`), stop the *supervisor*, not the process — a supervised process comes back in seconds |
| 502 immediately, every request | Upstream not running, wrong port, or wrong socket path/permissions | Curl the upstream from the box itself; if that works, it is the proxy's address, not the app |
| 502 intermittently, worse under load | Upstream keepalive shorter than the proxy's (Rule 4), or upstream worker recycling mid-request | Raise the app's idle timeout above the proxy's; check `max_requests`-style worker recycling |
| 504 at a suspiciously round number of seconds | A timeout, and the number names the layer that owns it (30s, 60s, 75s are defaults, not coincidences) | Grep every hop's config for that number before touching application code |
| 499 in nginx logs, no error in the app | The client hung up first; the app is slower than the caller's patience | Fix latency, or move the work to a job — raising proxy timeouts changes nothing |
| 413 on upload | Body limit at some hop: proxy, app framework, or CDN | Raise it at *every* hop in the path; the smallest one wins |
| Redirect loop between http and https | App does not see `X-Forwarded-Proto`, or does not trust it, so it redirects an already-secure request | Send the header at the proxy and enable the framework's proxy trust for the proxy's IP only |
| Service ran fine, then stopped and will not start | systemd start-limit hit (5 starts in 10s by default) — the unit is now in `failed` and stays there | `systemctl reset-failed` after fixing the cause; raise `RestartSec` so a crash loop is throttled, not banned |
| Works on reboot for weeks, then not | Unit not enabled, only started; or ordered before a mount/network it needs | `systemctl is-enabled`, then `After=`/`Requires=` on the real dependency |
| Certificate valid in `openssl s_client`, stale in the browser | The serving process never reloaded after renewal | Renewal hook that reloads the proxy, then verify the served expiry, not the file on disk |
| `Too many open files` under load | fd limit is per-process and services do not inherit your shell's `ulimit` | Raise `LimitNOFILE` in the unit and `worker_rlimit_nofile` in the proxy (≥ 2 × worker_connections) |
| Uploads or downloads truncate at a size, not a time | Buffering to a temp dir that is full or read-only | Check the proxy's temp path and disk, then decide buffering vs streaming |
| WebSocket connects then drops at ~60s | Proxy idle timeout closing an idle tunnel | Raise the read timeout on that route only, and send application-level pings |
| Anything else | Reproduce at the hop closest to the app, then walk outward one hop at a time | `debug.md` |

## Defaults That Decide Behavior

Numbers you did not choose are still numbers you are running. These are the defaults that most often turn out to be the answer.

| Layer | Default that bites |
|---|---|
| nginx | `client_max_body_size 1m` → 413 on any real upload · `proxy_read_timeout 60s` · `keepalive_timeout 75s` · no `keepalive` to upstreams unless declared, so every proxied request opens a new TCP connection |
| systemd | 5 starts per 10s then permanent `failed` · `TimeoutStopSec` 90s before SIGKILL · `LimitNOFILE` soft 1024 for the service regardless of your shell · `Type=simple` reports "started" before the app can serve, so ordered units start too early |
| Node.js | `keepAliveTimeout` 5s (Rule 4) · single-threaded: one process serves one CPU, no matter the machine |
| Gunicorn | 1 worker · 30s worker timeout · sync worker class serves exactly one request at a time, so one slow client blocks a whole worker |
| php-fpm | `pm.max_children` caps concurrency; when it is hit the log says so plainly and requests queue in the proxy as 502/504 |
| Postgres | `max_connections` 100 with 3 reserved — the real ceiling on `processes × pool_size` across every app on that database |
| Linux TCP | ephemeral range ~32768-60999 (~28k outbound connections per destination) · `TIME_WAIT` 60s, fixed · listen backlog `somaxconn` 128 on kernels before 5.4, 4096 after |
| Ports | below 1024 needs root or `AmbientCapabilities=CAP_NET_BIND_SERVICE` — ensure apps run unprivileged to get port 80 |
| journald | keeps up to 10% of the filesystem, capped at 4 GB, and is not rotated by logrotate — a chatty service silently owns gigabytes |
| Let's Encrypt | 90-day certificates, renewal at 30 days remaining; duplicate-certificate rate limits punish retry loops |

## Stack Defaults

One default per need, with the condition that overrides it. Selection logic and break-evens: `stack.md`.

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

## Output Gates

Before delivering a config, a unit, a deploy plan, or a diagnosis:

- Did I name the hop that owns the behavior, and give the exact file plus the reload that applies it?
- Does the timeout ladder still run shortest on the inside (Rule 3), and keepalive longest on the inside (Rule 4)?
- Is anything binding to `0.0.0.0` that only the proxy needs to reach (Rule 7)?
- Does this survive a reboot — unit enabled, or restart policy set — and is there a named rollback artifact?
- Is the command I am about to give service-affecting (`restart`, `down`, `stop`, `rm`, `prune`, `-v`)? Then it ships with the reload alternative and an explicit confirmation step, must be clearly separated from read-only commands.
- Did this session change what runs where, produce a measured number, or resolve an outage? Then the service row, the baseline, or the incident is written before I finish — `## Services`, `## Baselines`, `incidents/<year>.md`.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| proxy | nginx \| caddy \| traefik \| haproxy \| none | caddy | Dialect of every vhost, route, and reload example, and the default in Stack Defaults |
| process_manager | systemd \| pm2 \| supervisor \| compose | systemd | Whether supervision examples are units, ecosystem files, or restart policies |
| os_family | debian \| rhel \| alpine \| other | debian | Package names, service paths, log locations, and firewall tool in every command |
| app_root | path | /srv | Where release directories, sockets, and app configs are placed in generated examples |
| tls_issuer | certbot \| acme.sh \| caddy-auto \| proxy-terminated \| cloudflare | certbot | How renewal and its reload hook are wired, and who owns expiry monitoring |
| confirm_restarts | bool | true | When true, any service-affecting command is emitted with a confirmation step and the reload alternative first |
| maintenance_window | text | none | Window quoted for restarts, upgrades and migrations; unset means state the impact and act now |
| health_path | text | /healthz | Path used in generated health checks, proxy upstream checks, and deploy gates (Rule 9) |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — proxy and supervisor flavor already covered above, plus the release mechanism (rsync, `git pull`, image pull) and the container runtime (Docker, Podman, none) — affects `deployment.md` and `containers.md`
- **Conventions** — service naming, port allocation ranges, socket paths, vhost file layout, release directory format, log filenames — affects every generated unit and vhost
- **Platform** — architecture, memory and core count of the target box, whether a CDN or load balancer sits in front, IPv6 posture — affects the concurrency math and where TLS terminates
- **Safety posture** — appetite for in-place edits on a live box, whether destructive commands are emitted at all, mandatory dry runs, backup-before-change — affects Output Gates and `maintenance.md`
- **Observability** — access-log format and destination, whether request ids are propagated, uptime checker in use, alert routing — affects `logs.md`
- **Delivery** — deploy style (symlink releases, containers, platform push), migration-before-or-after policy, canary appetite — affects `deployment.md`
- **Constraints** — no-root requirements, no-Docker boxes, air-gapped hosts, compliance regimes, distro versions frozen by policy — affects stack selection and hardening defaults

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Raising the proxy timeout to fix a 504 | Moves the failure later and hides the slow query that caused it; the user waits 120s for the same error | Fix the inner hop; the ladder (Rule 3) exists so the app fails first, with a log line |
| Running the app as root to bind port 80 | Every RCE in a dependency is now a root shell on the box | Proxy owns 80/443; app runs unprivileged on a high port or a socket (Rule 7) |
| `systemctl restart` as the standard way to apply a change | Drops in-flight requests, and on a bad config leaves nothing running | Validate, then reload (Rule 6) |
| Editing config directly on the live box | The next deploy overwrites it and the fix is gone; nobody can say what is actually running | Change in the repo, deploy it; if an emergency edit happens, write it into `artifacts/` the same turn |
| `docker run -p 8080:8080` on a box with ufw | Docker's rules run ahead of ufw's, so the port is public while ufw claims it is blocked | Publish as `127.0.0.1:8080:8080` and let the proxy be the only public listener |
| Killing the process that holds the port | The supervisor restarts it within `RestartSec` and the port is taken again | Stop the unit or the container, then confirm the port is free |
| `copytruncate` in logrotate | Lines written between copy and truncate are lost, and the "rotated" file can reappear at its old size | Rotate with `create` plus a `postrotate` signal to reopen the log |
| Tuning workers by intuition before measuring | Every tuning guide's number was written for a different box and a different app | Measure the saturation point first, change one variable, measure again |
| Trusting `X-Forwarded-For` from anywhere | Any client can forge it — rate limits and audit logs become fiction | Trust it only from the proxy's address, via the real-ip mechanism of your proxy |
| Certificate renewal without a reload hook | The file on disk is new, the process still serves the old one, and it expires in production | Deploy hook that reloads the serving process, plus an expiry check in `## Due` |
| Backups that have never been restored | Restores fail on the parts nobody wrote down: ownership, secrets, database roles, upload paths | Timed restore drill into a scratch location, quarterly, recorded |
| One `docker-compose.yml` for every service on the box | One unrelated change or a bad image blocks everything; `down` takes the whole machine offline | One stack per app, one shared external proxy network |
| Adding a second box because the first "feels slow" | Doubles the cost and the failure modes while the bottleneck is a missing index or 1 worker | Find the saturated resource first; most single-box limits are configuration, not hardware |

## Where Experts Disagree

- **Containers vs packages on a single box.** Containers give a reproducible runtime and painless rollback; a systemd unit with the distro's runtime gives fewer layers to debug at 3am and no image registry to depend on. The frontier is the number of services: past three or four with conflicting runtimes, containers win; for one Go binary they are pure overhead.
- **Where TLS terminates.** Terminating at a CDN or load balancer is simpler and gets you a cert you never touch; terminating on the box keeps traffic encrypted end to end and keeps you working when the provider's edge has an incident. Regulated data pushes to end-to-end; everything else does fine terminating at the edge with an internal hop over a private network.
- **Reverse proxy on the host or in a container.** Host-installed proxies survive a container-daemon restart and see the real client IP without extra work; containerized proxies deploy with the rest of the stack. Teams that already do everything with Compose should not make the proxy the one exception.
- **Zero-downtime on one machine.** One camp says a symlink flip and a graceful reload is genuinely enough; the other says anything that matters needs two instances behind a proxy. Both are right at different sizes — the honest question is whether losing 200ms of connections during a deploy costs anything measurable to your users.

## Security & Privacy

**Credentials:** this skill configures services that need secrets (database URLs, API tokens, TLS private keys). It does NOT store, copy, or transmit them: secrets stay in the environment, the OS keychain, or the secret manager the user already runs, and only pointers such as `env:DATABASE_URL` or `file:/etc/myapp/env` are recorded under `<state_root>/.

**Local storage:** service inventory, baselines, releases, incidents and runbooks stay in `<state_root>/` on this machine; hosts and domains in the shared boxes. Hostnames, ports and unit names only — no keys, no passwords.

**Guardrails:** diagnostic commands are read-only by default. Service-affecting operations (restart, stop, down, prune, volume removal, firewall changes) are presented with their impact and require explicit confirmation before running.
