# Staking and delegation (P-Chain)

Primary Network validation and delegation happen on the **P-Chain**. MetaMask cannot manage validators.

## Mainnet floors (verify live before quoting as immutable law)

From Avalanche primary docs (How to Stake / Validate vs Delegate):

| Role | Minimum stake (Mainnet) | Notes |
| --- | --- | --- |
| Validator | **2,000 AVAX** | Must run a validating node and meet uptime to earn rewards |
| Delegator | **25 AVAX** | Stakes to an existing validator; no node required |

Validation period guidance in current node docs is commonly **14–365 days** (also described as about two weeks minimum through one year maximum). Always re-check `references/sources.md` links before giving a user a hard number that gates funds.

## Operational rules

- Staked AVAX is locked for the chosen duration; plan liquidity before bonding.
- Rewards depend on validator uptime, fee/commission, and stake parameters—compare validators rather than promising a fixed APY.
- Avalanche Primary Network staking is documented as **no slashing** of principal for downtime; underperformance mainly reduces or eliminates rewards. Still treat key compromise and incorrect address entry as total-loss risks.
- Fuji testnet uses much smaller stake floors; never mix testnet numbers into mainnet instructions.

## Liquid staking

Protocols such as sAVAX / ggAVAX wrap staked exposure into a liquid token. Treat them as third-party DeFi: verify the protocol docs, smart contracts, and unlock/redemption path separately from native P-Chain delegation.

## Workflow

1. Confirm mainnet vs Fuji and validator vs delegator intent.
2. Confirm the user can fund the **P-Chain** (atomic transfer from C/X if needed).
3. Use Core or another P-Chain-capable wallet; never invent CLI key commands from chat.
4. Record end time, node id / validator choice, and expected reward address before submitting.
