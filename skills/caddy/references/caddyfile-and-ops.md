# Caddyfile, reverse_proxy, and operations

Patterns retained from the pre-refactor skill body and checked against current Caddy docs. Prefer live directive pages in `sources.md` when flag defaults matter.

## Caddyfile shape

- Site address first, then directives inside the block.
- Indentation defines structure; put a space before `{` (`example.com {` not `example.com{`).
- Global options go in a top-level block:

```caddyfile
{
	debug
	# email <OPS_EMAIL>
	# acme_ca https://acme-staging-v02.api.letsencrypt.org/directory
}

example.com {
	reverse_proxy 127.0.0.1:3000
}
```

- `caddy fmt --overwrite <file>` normalizes formatting.
- `caddy validate --config <file>` is stronger than adapt alone — adapt can succeed while provision/validation still fails (missing cert files, bad modules, etc.).
- `caddy adapt --config <file> --pretty` shows native JSON for inspection; add `--validate` when checking provision errors.

## reverse_proxy essentials

```caddyfile
app.example.com {
	reverse_proxy backend:8080 backend2:8080 {
		lb_policy random
		# health_uri /healthz
		# header_up Host {host}
	}
}
```

- Default LB policy is **random** when multiple upstreams are listed; set `lb_policy` deliberately (`first`, `round_robin`, `least_conn`, hash variants, etc.).
- Passive health checks can mark upstreams unhealthy after failures (`fail_duration`, `max_fails`, status/latency gates). Active checks need explicit health_* configuration and stable upstream lists.
- Upstream forms: `host:port`, `http://` / `https://` shorthand, `h2c://`, `unix//path/to.sock`, port ranges where supported.
- Do not put paths/query strings in the upstream address expecting rewrite-while-proxy — use `rewrite` / handle blocks with defined behavior instead.
- Caddy sets forwarded headers for the upstream by default. Add `header_up` only for intentional overrides (for example forcing `Host` to match upstream SNI on `https://` upstreams).
- WebSocket upgrades work through `reverse_proxy` without a special module; long-lived streams may need buffer/flush tuning (`flush_interval`, buffer sizes) if an app stalls.

## Docker and Compose

- Prefer **Compose service names** as upstream hostnames on a shared user-defined network (`reverse_proxy api:3000`).
- Default bridge alone does not give reliable DNS between arbitrary containers — put Caddy and backends on the same Compose network.
- Publish or forward host 80/443 to the Caddy container; backends can stay internal.
- Mount persistent volumes for `/data` and `/config` (image conventions) so certificates survive recreate.
- After backend IP changes, Caddy still dials the name you configured; combine with health checks / retries when rolling deploys briefly empty the pool.

## Config lifecycle

| Goal | Prefer |
| --- | --- |
| Syntax / provision check | `caddy validate --config ...` |
| Pretty JSON view | `caddy adapt --config ... --pretty` |
| Apply new config without dropping process | `caddy reload --config ...` |
| Foreground run | `caddy run --config ...` |
| Format Caddyfile | `caddy fmt --overwrite ...` |

Reload replaces config atomically from Caddy's perspective: if the new config fails validation/load, the previous config remains active. Prefer reload over restart for config-only changes on a live edge.

Admin API / `caddy reverse-proxy` one-liners are fine for labs; production edges usually pin an explicit Caddyfile path and unit/service manager.

## Headers, TLS edge, performance

- Automatic HTTPS handles certs and HTTP→HTTPS redirect; it does **not** invent a full security-header suite. Add `header` directives for `X-Frame-Options`, `X-Content-Type-Options`, CSP, etc., when the app does not.
- HSTS is commonly enabled as part of modern HTTPS defaults when serving HTTPS — still verify app/CDN behavior before forcing long `max-age` on a first rollout.
- Enable HTTP/3 explicitly when required via server protocols configuration (global/servers options); ensure UDP 443 is allowed on the path.
- Compression for common text types is available through encode directives; turn it on intentionally rather than assuming every build ships the same defaults.

## Debugging order

1. `caddy validate` the exact file the service uses.
2. Confirm DNS and 80/443 path from an external vantage (or DNS-01 credentials).
3. Enable `debug` in global options temporarily; watch ACME and TLS handshake logs.
4. Inspect certificate material under the data directory (container: often `/data/caddy/...`) without deleting production keys.
5. `curl -vI https://example.com` and hit the upstream directly to separate edge vs app failures.
6. For WebSockets: verify the client upgrade, then the Caddy `reverse_proxy` hop, then app-level protocol (`websocket` skill) last.
