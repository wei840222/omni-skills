## Scaling Challenges

- WebSocket connections are stateful; prefer sticky sessions by client ID or Redis pub/sub for cross-instance broadcast.
- Budget memory for concurrent sockets—thousands of connections consume significant RAM.
- On graceful shutdown, send a close frame and give clients time to reconnect elsewhere.
