## Authentication

- Token in URL query (`wss://host/ws?token=xxx`) is simple, but tokens appear in access logs; prefer short-lived tokens if used.
- First-message auth (connect → send token → wait for ack) keeps credentials out of URLs at the cost of an extra round trip.
- Cookie auth works for same-origin browser sessions; WebSocket handshakes cannot set arbitrary custom headers from the browser API.
- Require a fresh authentication handshake after every reconnect; previous sessions are not assumed valid.
