# Staking and Stake Pool Selection

## Staking Mechanics

Cardano staking is non-custodial and permissionless:
- ADA stays in your wallet at all times — fully liquid
- No minimum delegation amount
- No lockup period
- Rewards are distributed by epoch under the active network schedule
- Initial delegation and rewards take multiple epochs; confirm the current schedule before giving a date

## Delegation Process

```bash
# 1. Register staking key (one-time)
cardano-cli stake-address registration-certificate \
  --staking-verification-key-file stake.vkey \
  --out-file stake.cert

# 2. Build delegation certificate
cardano-cli stake-address delegation-certificate \
  --staking-verification-key-file stake.vkey \
  --stake-pool-id POOL_ID_HEX \
  --out-file deleg.cert

# 3. Submit transaction with certificates
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --change-address "$ADDRESS" \
  --certificate-file stake.cert \
  --certificate-file deleg.cert \
  --mainnet \
  --out-file deleg.tx
```

## Stake Pool Evaluation

### Decision workflow

Evaluate pools in this order. Eliminate at each step:

1. **Check current saturation** — compare the pool's current saturation against the network target
   ```bash
   # Query pool metrics
   cardano-cli query pool-params --stake-pool-id POOL_ID_HEX
   ```
   - Record the source and observation time; explorer-derived metrics are time-sensitive

2. **Check block production** — Missed blocks = missed rewards
   - Review a meaningful recent period and compare actual production with the explorer's expected-production metric

3. **Evaluate cost structure**
   - Check the current fixed cost and margin from current pool data
   - Explain that relative impact depends on the user's stake and describe rewards as variable

4. **Check pledge**
   - Higher pledge signals operator commitment
   - Pledge ratio = pledge / pool stake
   - Treat pledge as one current signal, not a return guarantee

5. **Verify reliability**
   - Seek consistent recent block production and an operator status channel
   - Active operator presence (check pool homepage/social)

### Pool selection anti-patterns

- **Chasing lowest margin alone** — a 0% margin pool with poor uptime earns nothing
- **Ignoring fixed cost for small stakes** — compare the current fixed cost and margin with the stake size
- **Delegating to friends/family pools without analysis** — sentiment ≠ returns
- **Splitting delegation across many pools** — reduces effectiveness, increases complexity
- **Ignoring saturation** — oversaturated pools give reduced rewards to all delegators

### Reward calculation

Approximate annual return:
```
Annual reward ≈ (delegated ADA / total staked ADA) × total rewards per year
```

Rewards are variable and are not a promised yield. Use current network and pool data only to illustrate the calculation.

### Epoch timing

- Confirm the current epoch schedule from a current network source
- Delegation and rewards take effect in subsequent epochs rather than immediately

## Verification checkpoints

Before delegating, verify:
- [ ] Pool is not oversaturated
- [ ] Pool has produced blocks in recent epochs
- [ ] Pool's cost structure matches your delegation size
- [ ] Pool operator has reasonable pledge
- [ ] Your staking key is registered

## References

- [Cardano staking documentation](https://docs.cardano.org/explore-cardano/cardano-staking/)
- [Pool selection guide](https://cardano.org/staking/)
- [Cardano epoch and reward schedule](https://docs.cardano.org/explore-cardano/cardano-fee-structure/)
