# VRF v2.5

Chainlink VRF provides **provably fair onchain randomness**: each fulfillment includes a cryptographic proof verified onchain before consumers may use the value.

## Request methods

| Method | When it fits | Funding note |
|---|---|---|
| **Subscription** | Regular requests; multiple consumers | Fund a subscription with LINK or native; costs settle after fulfillment |
| **Direct funding** | Infrequent one-offs | Consumer pays at request time; estimate costs carefully |

Migrate remaining v1/v2 integrations to **v2.5** using the official migration guide. v2.5 adds easier future upgrades and the option to pay in LINK or native tokens.

## Operational rules

- Randomness is **async**: request → wait for fulfillment callback; do not assume synchronous returns.
- Underfunded subscription/direct balance causes failed or stuck requests — monitor balances.
- If the **consumer callback reverts**, randomness for that request can be lost; harden callbacks and keep gas limits realistic.
- More confirmation blocks improve safety against certain reorg/bias scenarios but add latency.
- Coordinator addresses, gas lane keys, and max gas limits are **network-specific** — verify on Supported Networks docs.

## Security framing

Results cannot be manipulated by a single oracle operator, developer, user, or builder under normal assumptions. Extreme edge cases (compromised VRF key **and** block-building power) are documented in official security considerations — point users there rather than inventing threat models.

Prefer `sources.md` links for billing formulas and network config tables.