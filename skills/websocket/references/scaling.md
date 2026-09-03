## Scaling Challenges

- WebSocket connections are stateful—can't round-robin between servers
- Sticky sessions: route by client ID to same server—or use Redis pub/sub for broadcast
- Each connection holds memory—thousands of connections = significant RAM
- Graceful shutdown: send close frame, wait for clients to reconnect elsewhere
