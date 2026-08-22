---
name: traefik
description: Configure and troubleshoot Traefik HTTP routing, TLS certificates, Docker labels, entrypoints, middlewares, services, and file-provider rules. Use when creating a Traefik-enabled Docker Compose deployment or diagnosing routes, redirects, certificates, dashboard exposure, or upstream-port errors.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔀"}'
---

# Traefik Configuration

## Configure a route

1. Define the router rule and its target service; a router needs both.
2. Bind the router to explicit entrypoints such as `web` and `websecure`.
3. Set the service's `loadbalancer.server.port` whenever the container exposes more than one port.
4. Apply TLS deliberately: enable `tls=true`, select a `certresolver` when automatic certificates are needed, and test ACME against staging before production.
5. Verify the router, service, middleware chain, and certificate in the dashboard or debug logs before treating the route as ready.

## Router and Docker labels

- Router priority defaults to rule length; set an explicit `priority` when overlapping rules need a deterministic winner.
- `Host()` matching is case-insensitive. Combine hosts with `Host(\`a.example\`) || Host(\`b.example\`)`.
- Put Docker labels on the container service. In Docker Swarm, use `deploy.labels`.
- Use backticks in `Host()` rules within Compose labels, and set `traefik.enable=true` when `exposedByDefault=false`.
- Set `traefik.docker.network` if a container has multiple networks so Traefik selects the intended one.

## TLS and entrypoints

- Define entrypoints in static configuration, for example `--entrypoints.web.address=:80` and `--entrypoints.websecure.address=:443`.
- Redirect HTTP to HTTPS at the entrypoint layer when every route should be secure.
- `websecure` requires a TLS-enabled router. Configure `certificatesResolvers.<name>.acme.email` for ACME registration.
- Keep port 80 reachable for an HTTP challenge; use a DNS challenge for wildcard certificates or environments where port 80 is unavailable.
- Persist ACME storage to retain certificates and avoid rate-limit pressure.

## Middlewares and services

- Middleware order is significant: the first middleware wraps those that follow. Reuse named chains across routers where the behavior is shared.
- Common middlewares include `stripPrefix`, `redirectScheme`, `basicAuth`, `rateLimit`, and `compress`.
- BasicAuth labels use `htpasswd` values; write `$` as `$$` in `docker-compose.yml`.
- Use `stripPrefix` with `PathPrefix` when the upstream expects a path without the public prefix.
- Configure service health checks to remove unhealthy upstreams, and sticky cookies only for stateful workloads.

## Detailed configuration

Read `references/configuration.md` when you need a Compose-label example, ACME setup details, file-provider configuration, or a diagnosis sequence.

## File provider and troubleshooting

- Enable `watch=true` in the file provider for hot reload. Docker and file providers can operate together.
- Raise the log level with `--log.level=DEBUG` to trace router matching and provider configuration.
- Review dashboard exposure as a protected administrative endpoint; `api.insecure=true` is suitable only for isolated local development.
- When a request fails, verify in order: router rule and entrypoint, TLS/ACME prerequisites, selected Docker network, middleware order, then the upstream port and health check.
