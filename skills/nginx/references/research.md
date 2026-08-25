# Nginx Domain Knowledge and Fact Verification

## Core Fact Sources
- Nginx Official Documentation: http://nginx.org/en/docs/
- Nginx Admin Guide: https://docs.nginx.com/nginx/admin-guide/
- Mozilla SSL Configuration Generator: https://ssl-config.mozilla.org/

## Verified Facts and Directives
- **worker_processes**: Auto is generally recommended, but inside constrained containers (without CPU quotas set appropriately), explicitly setting to the allocated cores might be safer to avoid over-spawning.
- **keepalive connections**: When proxying via HTTP, `keepalive` requires setting `proxy_http_version 1.1;` and clearing the `Connection` header (`proxy_set_header Connection "";`) to prevent connections from being closed after the first request.
- **try_files**: The directive executes its parameters in order, and the final parameter acts as a fallback or internal redirect.
- **SSL**: Nginx configuration of `ssl_certificate` requires the full chain of certificates (leaf + intermediates).

*All references are validated against the standard Nginx behavior.*
