# Official Sources — Binance Spot

Use these primary sources to verify time-sensitive API behavior before changing an operational workflow.

## REST API and limits

- **Spot REST API** — https://developers.binance.com/docs/binance-spot-api-docs/rest-api
  - Endpoint parameters, response headers, request-weight handling, and error semantics.
- **Error codes** — https://developers.binance.com/docs/binance-spot-api-docs/errors
  - Interpret API error codes before retrying an order whose execution state is uncertain.

## Signing and WebSocket behavior

- **WebSocket API request security** — https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-security
  - Signature payload construction, API-key security types, timestamps, and `recvWindow`.
- **WebSocket streams** — https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
  - Connection lifecycle, ping/pong, stream limits, and reconnect considerations.

## Test environment

- **Spot Testnet** — https://developers.binance.com/docs/binance-spot-api-docs/testnet
  - Supported test-environment endpoints and limitations.

Treat an uncertain placement response as an order-state reconciliation task: query the order and user-data events before considering another submission.
