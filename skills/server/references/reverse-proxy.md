# Reverse proxy and TLS termination

Load this reference when deciding where public traffic terminates and how the proxy hands requests to the application.

- A reverse proxy accepts client traffic and forwards it to an internal application. Keep the application listener private unless it deliberately serves public traffic.
- TLS termination decrypts traffic at the proxy or edge. Record the chosen boundary and ensure the application receives and validates the forwarding headers it needs (`X-Forwarded-Proto`, `X-Forwarded-For` / real-ip, Host).
- Trust forwarding headers only from the proxy's address. Blind trust lets any client forge client IP and scheme.
- Prefer Unix sockets or loopback TCP between proxy and app on the same host; use a private interface when they sit on different hosts.
- After a change, verify the full request path: client → proxy → app → dependency. A proxy error often reports an adjacent-hop failure rather than a proxy defect.
- When TLS renews, reload the process that actually serves the certificate; a fresh file on disk with a stale process still expires in production.

Sources:

- https://nginx.org/en/docs/http/ngx_http_proxy_module.html
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling
- https://caddyserver.com/docs/caddyfile/directives/reverse_proxy
