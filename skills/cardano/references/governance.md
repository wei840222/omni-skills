# Governance Participation

## Overview

Cardano governance operates through CIP-1694 (Conway era, September 2024). Three groups vote on governance actions:

1. **DReps (Delegated Representatives)** — vote on behalf of delegating ada holders
2. **SPOs (Stake Pool Operators)** — vote on hard forks, security parameters, no-confidence motions
3. **Constitutional Committee** — ensures proposals align with the Cardano constitution

## Governance Actions

Governance-action types, required voting bodies, and ratification thresholds are defined by the current protocol and can differ by action. Derive guidance from the current on-chain action and its governance metadata rather than a fixed percentage.

## DRep Delegation

Before using an artifact-producing command, define this preflight and call it with every new output path:

```bash
require_new_outputs() {
  for output_path in "$@"; do
    [ -n "$output_path" ] || { printf '%s\n' 'Set every output path before continuing.' >&2; return 2; }
    [ ! -e "$output_path" ] || { printf 'Refusing to overwrite: %s\n' "$output_path" >&2; return 1; }
  done
}
```

### Decision workflow

1. **Do you want to vote directly?**
   - Yes → Register as a DRep yourself
   - No → Delegate voting power to a DRep

2. **Choosing a DRep:**
   - Check their voting history on governance tools (GovTools, DRepTalk)
   - Review their stated positions and manifesto
   - Verify they are actively participating (voted in recent epochs)
   - Choose based on the DRep's published rationale, voting history, and current participation; delegation size does not make an individual delegator's vote intrinsically more influential

### Delegate to a DRep

```bash
require_new_outputs "$DREP_DELEG_CERT_FILE" "$DREP_DELEG_TX_DRAFT_FILE" || exit $?
# Create DRep delegation certificate
cardano-cli stake-address vote-delegation-certificate \
  --staking-verification-key-file stake.vkey \
  --drep-verification-key-file drep.vkey \
  --out-file "$DREP_DELEG_CERT_FILE"

# Submit in transaction
cardano-cli transaction build \
  --tx-in "$TX_IN" \
  --change-address "$ADDRESS" \
  --certificate-file "$DREP_DELEG_CERT_FILE" \
  --mainnet \
  --out-file "$DREP_DELEG_TX_DRAFT_FILE"
```

**Important:** DRep delegation is independent from stake pool delegation. Same ADA, two separate signals:
- Stake pool delegation → earns staking rewards
- DRep delegation → assigns voting power

## Registering as a DRep

```bash
require_new_outputs "$DREP_REG_CERT_FILE" || exit $?
# Create DRep registration certificate
cardano-cli governance drep-registration-certificate \
  --drep-verification-key-file drep.vkey \
  --key-registration-metadata-file drep-metadata.json \
  --out-file "$DREP_REG_CERT_FILE"

# Query the current DRep deposit parameter and submit in an explicitly approved transaction.
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
