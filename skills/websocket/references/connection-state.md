## Connection State

- `readyState`: 0=CONNECTING, 1=OPEN, 2=CLOSING, 3=CLOSED—check before sending
- Buffer messages while CONNECTING—send after OPEN
- `bufferedAmount` shows queued bytes—pause sending if backpressure building
- Multiple tabs = multiple connections—coordinate via BroadcastChannel or SharedWorker
