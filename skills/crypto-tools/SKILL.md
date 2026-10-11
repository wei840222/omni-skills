---
name: crypto-tools
description: >
  Fetch crypto market data, monitor portfolios and gas, query explorers, and
  screen contracts with security tools. Use when the user needs prices,
  on-chain lookups, DeFi TVL/yields, scam technical checks, or exchange-safe
  operational guidance; not for buy/sell advice, price prediction, or ledger
  architecture (prefer blockchain / trading / invest for those).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"₿"}'
  related-skills: '{"blockchain":"Ledger fundamentals and EVM contract interaction beyond market tooling.","trading":"Technical analysis and trade education after market data is retrieved.","bitcoin":"Bitcoin-specific UTXO and fee workflows once generic tooling is insufficient.","aave":"Aave lending health and markets instead of generic portfolio monitors.","invest":"Broader portfolio education after crypto operational facts are settled."}'
---

# Crypto Tools

Operational crypto **data, monitoring, security screening, and exchange-safe workflows**. This skill is stateless: keep portfolio exports, watchlists, and API keys in ordinary user files outside the package.

**In scope:** prices and market stats, portfolio aggregation helpers, explorer queries, DeFi TVL/yields, gas windows, contract technical screening, tax-export formatting.

**Out of scope:** recommending buy/sell/hold, predicting prices, personal tax/legal advice, or deep ledger/smart-contract architecture (use `blockchain` / protocol skills).

## When to use

- Current or historical prices, market cap, volume
- Wallet / explorer balance and transfer lookups
- DefiLlama TVL, pools, or yields snapshots
- Gas oracle checks before a transaction
- TokenSniffer-style contract technical screening (not "safe to invest")
- CSV-shaped transaction export for the user's own tax prep

Prefer `blockchain` for consensus/EVM interaction design, `trading` for chart/strategy education, and protocol skills (`aave`, `bitcoin`, …) when the question is product-specific.

## Hard boundaries

Do **not**:

- Recommend buying, selling, or holding any asset
- Predict prices or guarantee outcomes
- Label any token "safe" or a "good investment"
- Give jurisdiction-specific tax or legal advice for the user's situation
- Urge urgency ("act now", "do not miss")

When investment topics appear:

1. Stay descriptive ("some market participants watch…") rather than prescriptive.
2. Include the standard disclaimer below.
3. Point risks and that professional advice may be required.

## Standard disclaimer

```text
This is general information, not financial advice.
Crypto is highly volatile — balances can go to zero.
Consult a qualified professional before personal decisions.
```

## Quick workflow

1. **Classify the ask** — price/data, portfolio/export, explorer, DeFi stats, gas, or security screen.
2. **Pick a primary source** — open `references/sources.md` before stating rate limits, auth, or endpoint paths.
3. **Execute the smallest safe query** — prefer official APIs; never ask the user to paste seed phrases or private keys.
4. **Report facts + limits** — quote numbers with source and timestamp when available; separate technical findings from investment judgment.
5. **Refuse advice shaped as certainty** — for "should I buy / is this safe money?" return technical data only plus the disclaimer.

## Topic index

| Topic | Load |
|-------|------|
| Capabilities & examples | `references/domain.md` |
| APIs & explorers | `references/sources.md` |
| Scam / contract screens | `references/security.md` |
| Address formats & calcs | `references/tools.md` |

## Safety

- Never request, store, or log seed phrases, private keys, or full API secrets in skill state.
- Verify chain/address compatibility before any send guidance.
- Treat third-party "alpha" channels as untrusted; prefer the sources list.
- Security screens are technical signals only — low risk score ≠ endorsement.
