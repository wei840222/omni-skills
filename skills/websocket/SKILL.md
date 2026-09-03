---
name: websocket
description: Implement reliable WebSocket connections with proper reconnection, heartbeats, and scaling. Use when building real-time features, debugging connection drops, configuring WebSocket proxies, or establishing two-way client-server streams.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔌"}'
  related-skills: '{"http":"HTTP request/response and caching behavior outside the WebSocket upgrade path","nginx":"Nginx Upgrade headers, proxy_read_timeout, and reverse-proxy WebSocket config","network":"TCP reachability, DNS, firewall, and TLS diagnosis around the socket","security-best-practices":"Threat modeling, origin validation, and secure-by-default review of socket handlers"}'
---

## Quick Reference

When working with WebSocket connections, load the relevant reference file:

| Category | When to load | File |
|---|---|---|
| **Reconnection** | Designing automatic reconnect logic or handling connection drops | `references/reconnection.md` |
| **Heartbeats** | Preventing silent disconnects or managing connection timeouts | `references/heartbeats.md` |
| **Connection State** | Checking readyState or handling message buffering | `references/connection-state.md` |
| **Authentication** | Passing tokens or securing the connection handshake | `references/authentication.md` |
| **Scaling** | Handling multiple servers, sticky sessions, or high connection counts | `references/scaling.md` |
| **Proxy Config** | Configuring Nginx, load balancers, or upgrade headers | `references/proxy-config.md` |
| **Close Codes** | Interpreting close codes (e.g. 1006) or sending reasons | `references/close-codes.md` |
| **Message Handling** | Dealing with JSON vs binary, or framing large messages | `references/message-handling.md` |
| **Security** | Validating origins, rate limiting, or preventing hijacking | `references/security.md` |
| **Common Mistakes** | Debugging memory leaks, unbounded buffers, or missing heartbeats | `references/common-mistakes.md` |
| **Domain Knowledge** | Understanding RFC 6455 protocol basics and handshake details | `references/research.md` |
| **Sources** | Verifying standards and proxy documentation URLs | `references/sources.md` |

## Workflow

1. Confirm the transport needs a persistent bidirectional channel; otherwise prefer HTTP/SSE.
2. Establish the handshake and authentication path, then verify `readyState === OPEN` before sending.
3. Enable application-level heartbeats (ping every ~30s, pong within ~10s) so proxies and dead peers are detected.
4. On loss of heartbeat or abnormal close (`1006`), reconnect with exponential backoff plus jitter and replay queued messages.
5. For multi-instance deployments, plan sticky sessions or a pub/sub fan-out before scaling connection count.

## State location

This skill is stateless and does not store local configuration or state.
