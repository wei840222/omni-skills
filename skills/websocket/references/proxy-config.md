## Nginx/Proxy Config

```
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
proxy_read_timeout 3600s;
```
- Without these headers, upgrade fails—connection closes immediately
- `proxy_read_timeout` must exceed your ping interval—default 60s too short
- Load balancer health checks: separate HTTP endpoint, not WebSocket
