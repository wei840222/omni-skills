# Staking and Stake Pool Selection

## Staking Mechanics

Cardano staking is non-custodial and permissionless:
- ADA stays in your wallet at all times — fully liquid
- No minimum delegation amount
- No lockup period
- Rewards distributed every epoch (5 days)
- First rewards appear 15-20 days after delegation (3-4 epochs)

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
  --tx-in YOUR_UTXO \
  --tx-out "YOUR_ADDRESS+2000000" \
  --change-address YOUR_ADDRESS \
  --certificate-file stake.cert \
  --certificate-file deleg.cert \
  --out-file deleg.tx
```

## Stake Pool Evaluation

### Decision workflow

Evaluate pools in this order. Eliminate at each step:

1. **Check saturation** — Pools above saturation threshold give diminishing rewards
   ```bash
   # Query pool metrics
   cardano-cli query pool-params --stake-pool-id POOL_ID_HEX
   ```
   - Saturation < 100%: proceed
   - Saturation ≥ 100%: skip (rewards reduced)
   - Target: 50-80% saturation for optimal rewards

2. **Check block production** — Missed blocks = missed rewards
   - Query last 30 epochs of block production
   - Expected blocks = (pool stake / total stake) × blocks per epoch
   - Actual/Expected ratio < 0.8: skip
   - Actual/Expected ratio ≥ 0.8: proceed

3. **Evaluate cost structure**
   - Fixed cost: minimum 340 ADA/epoch (protocol parameter)
   - Margin: operator's percentage of rewards after fixed cost
   - For small delegators (<10k ADA): fixed cost dominates — prefer lower fixed cost
   - For large delegators (>100k ADA): margin matters more — prefer lower margin

4. **Check pledge**
   - Higher pledge signals operator commitment
   - Pledge ratio = pledge / pool stake
   - Pledge ratio < 1%: caution
   - Pledge ratio > 5%: strong signal

5. **Verify reliability**
   - Uptime > 99%
   - Consistent block production over 3+ months
   - Active operator presence (check pool homepage/social)

### Pool selection anti-patterns

- **Chasing lowest margin alone** — a 0% margin pool with poor uptime earns nothing
- **Ignoring fixed cost for small stakes** — 340 ADA fixed cost on 100 ADA delegation is devastating
- **Delegating to friends/family pools without analysis** — sentiment ≠ returns
- **Splitting delegation across many pools** — reduces effectiveness, increases complexity
- **Ignoring saturation** — oversaturated pools give reduced rewards to all delegators

### Reward calculation

Approximate annual return:
```
Annual reward ≈ (delegated ADA / total staked ADA) × total rewards per year
```

Current approximate APY: 3-5% (varies with total staked ratio and pool performance)

### Epoch timing

- 1 epoch = 5 days
- Delegation takes effect at next epoch boundary
- Rewards for epoch N appear in epoch N+2
- First reward: ~15-20 days after initial delegation

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
