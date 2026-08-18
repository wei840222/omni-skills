# Reverse proxy and TLS termination

Load this reference when deciding where public traffic terminates and how the proxy hands requests to the application.

- A reverse proxy accepts client traffic and forwards it to an internal application. Keep the application listener private unless it deliberately serves public traffic.
- TLS termination decrypts traffic at the proxy or edge. Record the chosen boundary and ensure the application receives and validates the forwarding headers it needs.
- Verify the full request path after a change: client → proxy → app → dependency. A proxy error often reports an adjacent-hop failure rather than a proxy defect.

Sources:
- https://nginx.org/en/docs/http/ngx_http_proxy_module.html
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling
