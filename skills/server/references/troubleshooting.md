# Troubleshooting and Configuration

## Failure Signatures

Decode rule: the error names the hop that *noticed*, not the hop at fault. Refused means something answered with a rejection; timed out means nothing answered at all.

| Signature | Most likely cause | First move |
|---|---|---|
| `Connection refused` from outside, works on the box | Listening on `127.0.0.1`, not the public interface — or the proxy is stopped | `ss -tlnp` and read the *Local Address* column: `127.0.0.1:8080` and `0.0.0.0:8080` are different diagnoses |
| `Connection timed out` from outside | Packets dropped: host firewall, cloud security group, or the wrong host entirely | Refused = reached and rejected; timed out = failed to arrive. Diagnose each signal from its distinct network path |
| `Address already in use` on start | Old process still holds the port, or two units define it | Find the holder (`ss -tlnp` / `lsof -i :PORT`), stop the *supervisor*, not the process — a supervised process comes back in seconds |
| 502 immediately, every request | Upstream stopped, wrong port, or wrong socket path/permissions | Curl the upstream from the box itself; if that works, it is the proxy's address, not the app |
| 502 intermittently, worse under load | Upstream keepalive shorter than the proxy's (Rule 4), or upstream worker recycling mid-request | Raise the app's idle timeout above the proxy's; check `max_requests`-style worker recycling |
| 504 at a suspiciously round number of seconds | A timeout, and the number names the layer that owns it (30s, 60s, 75s are defaults, not coincidences) | Grep every hop's config for that number before touching application code |
| 499 in nginx logs, no error in the app | The client hung up first; the app is slower than the caller's patience | Fix latency, or move the work to a job — raising proxy timeouts changes nothing |
| 413 on upload | Body limit at some hop: proxy, app framework, or CDN | Raise it at *every* hop in the path; the smallest one wins |
| Redirect loop between http and https | App misses `X-Forwarded-Proto`, or distrusts it, so it redirects an already-secure request | Send the header at the proxy and enable the framework's proxy trust for the proxy's IP only |
| Service ran fine, then stopped and fails to start | systemd start-limit hit — the unit is now in `failed` and stays there | `systemctl reset-failed` after fixing the cause; raise `RestartSec` so a crash loop is throttled, not banned |
| Works on reboot for weeks, then fails | Unit not enabled, only started; or ordered before a mount/network it needs | `systemctl is-enabled`, then `After=`/`Requires=` on the real dependency |
| Certificate valid in `openssl s_client`, stale in the browser | The serving process never reloaded after renewal | Renewal hook that reloads the proxy, then verify the served expiry, not the file on disk |
| `Too many open files` under load | fd limit is per-process and services do not inherit your shell's `ulimit` | Raise `LimitNOFILE` in the unit and `worker_rlimit_nofile` in the proxy (≥ 2 × worker_connections) |
| Uploads or downloads truncate at a size, not a time | Buffering to a temp dir that is full or read-only | Check the proxy's temp path and disk, then decide buffering vs streaming |
| WebSocket connects then drops at ~60s | Proxy idle timeout closing an idle tunnel | Raise the read timeout on that route only, and send application-level pings |
| Anything else | Reproduce at the hop closest to the app, then walk outward one hop at a time | Trace the request path |

## Output Gates

Before delivering a config, a unit, a deploy plan, or a diagnosis:

- Did I name the hop that owns the behavior, and give the exact file plus the reload that applies it?
- Does the timeout ladder still run shortest on the inside (Rule 3), and keepalive longest on the inside (Rule 4)?
- Is anything binding to `0.0.0.0` that only the proxy needs to reach (Rule 7)?
- Does this survive a reboot — unit enabled, or restart policy set — and is there a named rollback artifact?
- Is the command I am about to give service-affecting (`restart`, `down`, `stop`/`halt`, `rm`, `prune`, `-v`)? Then it ships with the reload alternative and an explicit confirmation step, clearly separated from read-only commands.
- Did this session change what runs where, produce a measured number, or resolve an outage? Then record the service state, baseline, or incident under `<state_root>` before finishing.

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

- **Tooling** — proxy and supervisor flavor already covered above, plus the release mechanism (rsync, `git pull`, image pull) and the container runtime (Docker, Podman, none)
- **Conventions** — service naming, port allocation ranges, socket paths, vhost file layout, release directory format, log filenames
- **Platform** — architecture, memory and core count of the target box, whether a CDN or load balancer sits in front, IPv6 posture
- **Safety posture** — appetite for in-place edits on a live box, whether destructive commands are emitted at all, mandatory dry runs, backup-before-change
- **Observability** — access-log format and destination, whether request ids are propagated, uptime checker in use, alert routing
- **Delivery** — deploy style (symlink releases, containers, platform push), migration-before-or-after policy, canary appetite
- **Constraints** — no-root requirements, no-Docker boxes, air-gapped hosts, compliance regimes, distro versions frozen by policy

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
| Backups that lack restore drills | Restores fail on the parts nobody wrote down: ownership, secrets, database roles, upload paths | Timed restore drill into a scratch location, quarterly, recorded |
| One `docker-compose.yml` for every service on the box | One unrelated change or a bad image blocks everything; `down` takes the whole machine offline | One stack per app, one shared external proxy network |
| Adding a second box because the first "feels slow" | Doubles the cost and the failure modes while the bottleneck is a missing index or 1 worker | Find the saturated resource first; most single-box limits are configuration, not hardware |
