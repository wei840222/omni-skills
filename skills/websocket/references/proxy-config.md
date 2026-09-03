## Nginx/Proxy Config

```
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";
proxy_read_timeout 3600s;
```
- Include the Upgrade and Connection headers so the handshake completes.
- Set `proxy_read_timeout` above the heartbeat interval; the Nginx default of 60s is usually too short.
- Point load-balancer health checks at a separate HTTP endpoint, not the WebSocket path.
