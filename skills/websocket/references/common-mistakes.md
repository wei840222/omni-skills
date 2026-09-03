## Common Mistakes

- Missing heartbeats leave half-open connections that accept no traffic; add application ping/pong.
- Immediate reconnect loops can hammer a recovering server; use exponential backoff with jitter.
- Keeping critical session state only in the socket loses it on reconnect; persist externally and rehydrate.
- Sending huge messages on the event loop stalls the client; chunk or stream large payloads.
- Ignoring `bufferedAmount` lets memory grow when the peer is slower than the sender; pause when backpressure rises.
