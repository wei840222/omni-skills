# Nonce and Stuck Transactions

- Every Ethereum account has a nonce that increments with each transaction — if tx with nonce 5 is pending, nonces 6+ are blocked until 5 confirms
- To unstick: send a new tx with the SAME nonce and higher gas — this replaces the pending tx (even a 0 ETH self-transfer works)
- MetaMask "Speed up" and "Cancel" buttons do exactly this — they resubmit with same nonce and higher priority fee
- Nonce gaps cause permanent stuck state — if nonce 3 was omitted but 4 was broadcast, 4 will remain pending indefinitely until 3 is sent
