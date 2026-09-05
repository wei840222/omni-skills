# Setup - Binance API

Read this when `<state_root>/` is missing or empty.
Keep setup practical, safe, and non-blocking.

## Operating Priorities

- Answer the immediate user question first.
- Confirm integration behavior in the first exchanges.
- Default to testnet until the user explicitly asks for production.

## First Activation Flow

1. Confirm integration preference early:
- Should Binance workflows activate whenever user mentions Binance, Spot orders, or crypto execution?
- Should the agent act proactively with warnings on risky order payloads, or only when asked?

2. Confirm operating mode:
- Testnet-only
- Mixed mode (testnet first, then production)
- Production support with explicit pre-trade confirmations

3. Confirm workflow scope:
- Market data only
- Trading and account endpoints
- Streams and reconciliation tracking

4. After resolving `<state_root>` and receiving approval to persist operational notes, initialize only the needed state paths:
```bash
mkdir -p <state_root>/snapshots
touch <state_root>/{memory.md,runbooks.md,incidents.md}
chmod 700 <state_root> <state_root>/snapshots
chmod 600 <state_root>/{memory.md,runbooks.md,incidents.md}
```

5. If `<state_root>/memory.md` is empty, initialize it from `references/memory-template.md`.

## Integration Defaults

- Use Spot testnet first for every new order shape.
- Always verify filters from `exchangeInfo` before signed order calls.
- Require explicit user confirmation before any production order placement.
- Require final order-state reconciliation for timeout or uncertain responses.

## What to Save

- Preferred mode (testnet-only, mixed, or production-enabled)
- Approved symbols, intervals, and trading constraints
- Known errors and proven fixes for the user environment
- Stream and reconnection behavior that worked reliably

## Guardrails

- Never ask the user to paste secrets into chat.
- Never execute production trading flows without explicit confirmation.
- Never present uncertain order status as final without reconciliation.
