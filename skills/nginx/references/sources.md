# Official Sources & Module Specifications

This document records the official documentation and security standards for the Nginx web server and reverse proxy.

## Official Documentation & Directives

- **Nginx Documentation Home**: [https://nginx.org/en/docs/](https://nginx.org/en/docs/)
  - Core architecture, event processing mechanisms (epoll/kqueue), and master-worker process models.
- **Nginx HTTP Core Module**: [https://nginx.org/en/docs/http/ngx_http_core_module.html](https://nginx.org/en/docs/http/ngx_http_core_module.html)
  - Directive specifications for `server`, `location` matching precedence, `root`, `alias`, and client buffers.
- **Nginx HTTP/3 (QUIC) Module**: [https://nginx.org/en/docs/http/ngx_http_v3_module.html](https://nginx.org/en/docs/http/ngx_http_v3_module.html)
  - HTTP/3 over QUIC listener configuration (`listen 8443 quic reuseport`), 0-RTT support, and Alt-Svc headers.

## Security Standards & TLS Profiles

- **Mozilla SSL Configuration Generator**: [https://ssl-config.mozilla.org/](https://ssl-config.mozilla.org/)
  - Modern, intermediate, and backward-compatible cipher suites, TLS 1.2/1.3 configurations, and OCSP Stapling baselines.
