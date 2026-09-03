## Reconnection

- Treat missing heartbeats as connection loss; do not wait only for `onclose`, because TCP FIN can fail to arrive.
- Use exponential backoff: 1s, 2s, 4s, 8s… capped at 30s, to avoid a reconnect storm after outages.
- Add jitter with `delay * (0.5 + Math.random())` so clients do not reconnect in lockstep.
- Track reconnect state, queue outbound messages while offline, and replay them after `OPEN`.
- After the maximum retry count, surface a clear error to the user and stop silent retries.
