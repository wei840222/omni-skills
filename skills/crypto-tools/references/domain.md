# Crypto Tools Domain Knowledge

## Core capabilities

| Task | How |
|------|-----|
| **Price data** | CoinGecko / CoinMarketCap APIs — spot and historical |
| **Portfolio tracking** | Aggregate exchange/wallet positions; compute performance offline |
| **On-chain queries** | Etherscan-family explorers, Solscan — balances, txs, contracts |
| **DeFi data** | DefiLlama (TVL/yields), Dune, The Graph |
| **Scam screening** | TokenSniffer, RugDoc, CertiK — verified source, locks, honeypot signals |
| **Gas monitoring** | Explorer gas oracles; suggest lower-fee windows without urgency hype |
| **Alerts** | User-defined price or whale thresholds (host automation owns delivery) |
| **Tax prep support** | Export user-owned history to CSV-shaped rows (dates, amounts, prices) |

## Example interactions

- **Good:** "What's the current ETH price?" → CoinGecko simple/price + 24h change, cite source.
- **Good:** "Screen contract 0x…" → TokenSniffer/explorer technical findings; state no token is risk-free.
- **Good:** "Export my tx history for taxes" → CSV columns from explorer data the user controls.
- **Refuse-as-advice:** "Should I buy ETH now?" → decline recommendation; offer price/trend facts + disclaimer.

## Failure branches

- API 429 / auth required → report limit, suggest backoff or keyed tier; do not invent prices.
- Ambiguous chain for an address → ask chain or detect from context before querying.
- "Is this safe to invest?" → technical screen only + disclaimer; never binary safety claims.
