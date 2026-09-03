## Heartbeats

- Prefer application-level ping/pong; browsers do not expose protocol ping frames to page scripts.
- Send a ping about every 30s and expect a pong within about 10s; missing pong means reconnect.
- Have the server ping as well so dead clients are detected and cleaned up.
- Keep the heartbeat interval shorter than typical proxy idle timeouts (often 60–120s).
- Rely on application heartbeats rather than TCP keepalive, which is too infrequent through proxies.
