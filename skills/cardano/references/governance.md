# Governance Participation

## Overview

Cardano governance operates through CIP-1694 (Conway era, September 2024). Three groups vote on governance actions:

1. **DReps (Delegated Representatives)** — vote on behalf of delegating ada holders
2. **SPOs (Stake Pool Operators)** — vote on hard forks, security parameters, no-confidence motions
3. **Constitutional Committee** — ensures proposals align with the Cardano constitution

## Governance Actions

Seven types of governance actions exist:

| Type | Description | Approval threshold |
|------|-------------|-------------------|
| Motion of no-confidence | Remove constitutional committee | 50%+1 of voting stake |
| New constitutional committee | Elect committee members | 50%+1 of voting stake |
| Constitution update | Modify the constitution | 50%+1 of voting stake |
| Hard-fork initiation | Trigger protocol upgrade | 50%+1 of voting stake |
| Protocol parameter changes | Adjust protocol parameters | 50%+1 of voting stake |
| Treasury withdrawals | Fund projects from treasury | 50%+1 of voting stake |
| Info actions | Non-binding signals | 50%+1 of voting stake |

## DRep Delegation

### Decision workflow

1. **Do you want to vote directly?**
   - Yes → Register as a DRep yourself
   - No → Delegate voting power to a DRep

2. **Choosing a DRep:**
   - Check their voting history on governance tools (GovTools, DRepTalk)
   - Review their stated positions and manifesto
   - Verify they are actively participating (voted in recent epochs)
   - Prefer DReps with < 1M ADA delegated — your vote carries more weight

### Delegate to a DRep

```bash
# Create DRep delegation certificate
cardano-cli governance vote-delegation-certificate \
  --staking-verification-key-file stake.vkey \
  --drep-verification-key-file drep.vkey \
  --out-file drep-deleg.cert

# Submit in transaction
cardano-cli transaction build \
  --tx-in YOUR_UTXO \
  --tx-out "YOUR_ADDRESS+5000000" \
  --change-address YOUR_ADDRESS \
  --certificate-file drep-deleg.cert \
  --out-file drep-deleg.tx
```

**Important:** DRep delegation is independent from stake pool delegation. Same ADA, two separate signals:
- Stake pool delegation → earns staking rewards
- DRep delegation → assigns voting power

## Registering as a DRep

```bash
# Create DRep registration certificate
cardano-cli governance drep-registration-certificate \
  --drep-verification-key-file drep.vkey \
  --key-registration-metadata-file drep-metadata.json \
  --out-file drep-reg.cert

# Deposit required (configurable protocol parameter, currently 500 ADA)
# Submit in transaction with certificate
```

DRep responsibilities:
- Vote on governance actions each epoch
- Maintain transparency about voting rationale
- Engage with delegators
- Stay informed on technical proposals

## Governance Tools

- **GovTools** — governance dashboard for proposals and voting
- **DRepTalk** — delegate, register, discuss governance
- **Chang Watch** — vote distribution and DRep analytics
- **Cardano Governance Tool** — delegate and vote on proposals

## Verification checkpoints

Before participating in governance:
- [ ] Staking key is registered
- [ ] You understand the governance action being voted on
- [ ] DRep delegation is active (if delegating)
- [ ] You have reviewed the proposal details and community discussion

## References

- [CIP-1694: A new on-chain governance system](https://github.com/cardano-foundation/CIPs/tree/master/CIP-1694)
- [Cardano governance overview](https://cardano.org/governance/)
- [Chang hard fork documentation](https://docs.cardano.org/about-cardano/evolution/upgrades/chang)
- [Intersect MBO governance resources](https://www.intersectmbo.org/)
