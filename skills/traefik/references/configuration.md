# Traefik configuration reference

Use this reference after the routing intent is known and you need label-level detail or diagnosis.

## Docker labels

Attach labels to the container. A minimal HTTPS service looks like:

```yaml
services:
  app:
    labels:
      - traefik.enable=true
      - traefik.http.routers.app.rule=Host(`example.com`)
      - traefik.http.routers.app.entrypoints=websecure
      - traefik.http.routers.app.tls=true
      - traefik.http.routers.app.tls.certresolver=letsencrypt
      - traefik.http.services.app.loadbalancer.server.port=8080
```

For multiple routers or service ports on one container, explicitly bind each router with `traefik.http.routers.<router>.service=<service>`.

## ACME certificates

Configure `certificatesResolvers.<name>.acme.email` and durable ACME storage. Use the staging CA while testing to avoid production rate limits. HTTP-01 needs reachable port 80; select DNS-01 for wildcard certificates or when port 80 cannot be reached.

## Middleware and file provider

A router accepts a comma-separated middleware chain, such as `auth,compress`. Apply `stripPrefix` before forwarding a public path prefix to an upstream that does not expect it. Use the file provider for dynamic routers, services, and middlewares outside Docker labels; `watch=true` reloads file changes.

## Troubleshooting sequence

1. Confirm the router's rule, entrypoint, and selected service in the dashboard.
2. Confirm Docker provider visibility and `traefik.docker.network` when multiple networks exist.
3. Confirm the upstream port; a 502 commonly means Traefik selected the wrong exposed port.
4. Confirm TLS resolver configuration, challenge reachability, and persisted ACME storage.
5. Check debug logs for rule matching and middleware execution.

## Sources

- Traefik Docker routing: https://doc.traefik.io/traefik/reference/routing-configuration/other-providers/docker/
- Traefik ACME certificate resolvers: https://doc.traefik.io/traefik/reference/install-configuration/tls/certificate-resolvers/acme/
- Traefik routers and priority: https://doc.traefik.io/traefik/routing/routers/
