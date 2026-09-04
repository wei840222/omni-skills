# Token Approvals (Critical Security)

- ERC-20 `approve()` grants a contract permission to spend your tokens — many dApps request unlimited (type(uint256).max) approval
- If that contract gets hacked, attacker can drain all approved tokens even years later — audit approvals at revoke.cash
- Recommend users approve only the exact amount needed, or revoke after each use
- Approvals persist forever until explicitly revoked — changing wallets doesn't help if the old address still has tokens
- EIP-2612 (Permit) and Permit2 allow gasless approvals via off-chain signatures. Be extremely careful when signing messages that look like approvals, as they can drain tokens just like on-chain approvals.
