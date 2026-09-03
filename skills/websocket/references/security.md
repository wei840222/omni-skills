## Security

- Validate the Origin header during the handshake to block cross-site WebSocket hijacking.
- Assume any page may attempt a connection; same-origin policy does not protect WebSocket servers by itself.
- Rate-limit messages per connection so one client cannot flood the server.
- Validate every message payload and close with an application-defined code (4000–4999) on policy violations.
