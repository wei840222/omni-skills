## WebSocket Domain Knowledge

- **Standard**: WebSocket is defined by RFC 6455 and maintained by WHATWG as a living standard. Primary references: https://www.rfc-editor.org/rfc/rfc6455.html and https://websockets.spec.whatwg.org/
- **Protocol**: Provides a bidirectional, full-duplex communication channel over a single TCP connection after an HTTP Upgrade handshake.
- **Port Usage**: Typically uses port 443 (`wss://`) or port 80 (`ws://`), remaining firewall-friendly with existing HTTP infrastructure.
- **Handshake**: The client starts with an HTTP request that includes `Upgrade: websocket` and `Connection: Upgrade`, then switches protocols once the server accepts.
- **Advantages over Polling**: Lower overhead than repeated HTTP polling because the server can push frames continuously without repeating request headers.
- **Message Framing**: Unlike raw TCP byte streams, WebSocket frames discrete messages; libraries reassemble fragmented frames for the application.
- **Close semantics**: Normal closures use status `1000`; abnormal closures without a close frame surface as `1006`. See https://www.rfc-editor.org/rfc/rfc6455.html#section-7.4
- **Browser API notes**: Browser clients expose the WHATWG/MDN WebSocket API rather than raw protocol ping frames; application-level heartbeats remain necessary. See https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
