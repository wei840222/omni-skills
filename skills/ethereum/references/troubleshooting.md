# Failed Transactions

- A reverted transaction is mined and consumes gas — you pay even though nothing happened
- Common causes: slippage exceeded, deadline passed, insufficient token balance, contract paused
- "Transaction failed" in explorer means it executed but reverted — completely different from "pending" (not yet mined)
- Simulating transactions before sending (via Tenderly or wallet preview) catches most revert conditions
