---
name: binance
description: Use safe Binance Spot REST and WebSocket workflows for market data, signed requests, order reconciliation, and testnet-first validation; do not use for unrelated exchanges or autonomous production trading.
metadata:
  version: "1.0.0"
  related-skills: '{"api": "Build and debug robust HTTP API request workflows", "auth": "Handle API auth models, signatures, and credential safety", "bash": "Automate shell workflows with safer command composition", "bitcoin": "Add BTC domain context when analyzing crypto execution"}'
  openclaw: '{"emoji": "📈", "requires": {"bins": ["curl", "openssl", "jq"], "env": ["BINANCE_API_KEY", "BINANCE_API_SECRET"]}}'
---


# Binance Spot API Operations


## State location

Before any state operation, use an explicitly configured state root when one exists. Otherwise choose the first existing directory in this order: `<workspace>/binance/`, `<workspace>/memory/binance/`, then `~/binance/`. If more than one exists, use only the highest-precedence directory and tell the user that separate copies exist; never merge or synchronize them automatically. If none exists and persistent state is needed with authorization, create `<workspace>/binance/`.

Use the selected `<state_root>` consistently for the entire invocation. The host supplies `<workspace>`; do not substitute the shell working directory.

## Setup

On first use, read `references/setup.md` for integration preferences and safe environment defaults.

## When to Use

User needs to read Binance market data, place or manage Spot orders, or troubleshoot signed API calls from terminal workflows. Agent handles request signing, filter validation, rate-limit safety, and WebSocket reconciliation.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md            # API mode, symbols, and execution preferences
├── runbooks.md          # Repeatable workflows that worked in production
├── incidents.md         # Failures, response codes, and fixes
└── snapshots/           # Symbol filters and pre-trade validation captures
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup behavior | `references/setup.md` | When starting the skill for the first time |
| Memory template | `references/memory-template.md` | When interpreting or modifying the state format |
| Fast start commands | `references/quickstart.md` | When the user asks for initial command examples |
| Auth and signatures | `references/auth-signing.md` | Before making any signed API calls |
| Market data patterns | `references/market-data.md` | When retrieving spot pricing or order book data |
| Streams and WS API | `references/websocket.md` | When subscribing to real-time streams |
| SDK and CLI options | `references/sdk-cli.md` | When standard REST tools are insufficient |
| Limits and error handling | `references/errors-limits.md` | When troubleshooting rate limits or API errors |
| Spot testnet operations | `references/testnet.md` | When executing trades safely in the testnet |
| Incident recovery | `references/troubleshooting.md` | When resolving an issue or tracking down failures |
| Official API sources | `references/official-sources.md` | Before relying on time-sensitive endpoint, signing, limit, or testnet behavior |

## Requirements

- `curl`
- `openssl`
- `jq`
- `BINANCE_API_KEY` and `BINANCE_API_SECRET` for signed Spot requests
- Optional: `BINANCE_BASE_URL`, `BINANCE_WS_BASE`, and `BINANCE_TESTNET=1`

Store API keys and secrets securely outside of repository files.

## Data Storage

- `<state_root>/memory.md` for preferences and environment mode
- `<state_root>/runbooks.md` for proven workflows
- `<state_root>/incidents.md` for outage and error history
- `<state_root>/snapshots/` for `exchangeInfo` and filter captures

## Core Rules

### 1. Start in Spot Testnet by Default
- Use production only after explicit confirmation in the current conversation.
- Run the same flow in testnet first for every new order or account workflow.

### 2. Enforce Timestamp and Signature Correctness
- Sync server time before signed calls and keep `recvWindow` realistic.
- Sort params before signing and include every signed field in the canonical string.

### 3. Validate Symbol Filters Before Creating Orders
- Read symbol filters from `exchangeInfo` and enforce `PRICE_FILTER`, `LOT_SIZE`, and `MIN_NOTIONAL`.
- Reject order payloads locally before sending requests that will fail.

### 4. Use Test Order Before Real Order
- For every new payload shape, call `POST /api/v3/order/test` first.
- Promote to `POST /api/v3/order` only when payload and filters are confirmed.

### 5. Reconcile Every Order Through User Events
- Treat placement response as provisional when network quality is poor.
- Confirm final state through `executionReport` events and REST queries.

### 6. Respect Rate Limits and Back Off Fast
- Parse `rateLimits` in responses and throttle proactively.
- On `429` or `418`, pause, back off exponentially, and avoid hammering retries.

### 7. Keep Scope Tight and Transparent
- Use only declared Binance endpoints and symbols requested by the user.
- Modify only user-authorized state paths and preserve the skill package as read-only operational guidance.

## Execution Heuristics

- For `-1021`, use Binance server time before rebuilding the signed request.
- For `-1022`, rebuild the canonical payload after every parameter change and sign that exact payload.
- Align quantity to the `LOT_SIZE` `stepSize` before sending an order.
- Treat the placement response as provisional; reconcile partial fills and cancels through REST and user-data events.
- Rotate market-data sockets before their documented connection lifetime and reconnect with jitter.
- Reduce request rate after `429` and follow the documented ban-recovery path after `418`.

## External Endpoints

Only official Binance API surfaces below are used by this skill.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `https://api.binance.com` and `https://api-gcp.binance.com` | Signed trade/account params, market query params | Spot REST production |
| `https://api1.binance.com` to `https://api4.binance.com` | Same as Spot REST | Alternative production REST hosts |
| `https://data-api.binance.vision` | Public market data params only | Spot public market data |
| `wss://stream.binance.com:9443` and `wss://stream.binance.com:443` | Stream subscribe payloads and listenKey stream data | Spot market/user streams |
| `wss://data-stream.binance.vision` | Market stream subscriptions only | Public market streams |
| `wss://ws-api.binance.com:443/ws-api/v3` | WS API signed and unsigned request payloads | Spot WebSocket API |
| `https://testnet.binance.vision`, `wss://stream.testnet.binance.vision`, `wss://ws-api.testnet.binance.vision/ws-api/v3` | Test order/account payloads | Spot testnet validation |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- API key identifier and signed params for account and trading endpoints
- Requested symbols, intervals, and market stream subscriptions

**Data that stays local:**
- Operational memory and incident logs in `<state_root>/`
- Local helper scripts and runbooks created during sessions

**Operating boundary:**
- Send request data only to the declared Binance endpoints.
- Place a production order only after explicit confirmation in the current conversation.
- Keep API secrets in the host credential store rather than repository files.
- Preserve this skill definition as read-only guidance during Binance operations.

## Trust

By using this skill, request data is sent to Binance infrastructure.
Only install if you trust Binance with your operational trading metadata.
