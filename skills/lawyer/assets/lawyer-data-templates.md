# Lawyer data templates

Copy into the resolved `<state_root>` only after the user authorizes the named write. Replace placeholders. Never store passwords, full account numbers, national IDs, or raw data-room contents — use pointers.

## `config.yaml`

```yaml
home_jurisdiction: ""  # e.g. "US-DE" or "England and Wales"
default_side: either     # vendor | customer | employer | employee | either
risk_posture: balanced   # conservative | balanced | commercial
entity_type: none
liability_cap_basis: fees-12mo
signature_authority_usd: 25000
notice_lead_days: 45
compliance_regimes: []
counsel_relationship: none
document_format: markdown
```

## `memory.md`

```markdown
# Lawyer memory

## Status
- Home jurisdiction assumption:
- Default side:
- Open pressure this week:

## Boxes
<!-- path — condition -->
- contracts.md — when tracking more than one agreement
- matters/ — when a matter needs its own file

## Due
| Item | Next date | Unit | Owner | Status |
|------|-----------|------|-------|--------|
| | | | | |

## Positions
<!-- issue | ask | landed | date -->

## Open items
-
```

## `contracts.md` (optional register)

```markdown
# Agreement register

| Name | Counterparty | Type | Effective | Renewal / notice alarm | Cap summary | Path |
|------|--------------|------|-----------|------------------------|-------------|------|
| | | | | | | file:... |
```

## Matter file `matters/{name}.md`

```markdown
# Matter: {name}

- Opened:
- Jurisdiction:
- Side:
- Counterparty (name only):
- Counsel:
- Status:
- Budget:

## Facts
-

## Deadlines
|

## Documents
- file:...

## Notes
-
```

## Artifact `artifacts/clause-{topic}.md`

```markdown
# Clause: {topic}

- Agreement context:
- Side:
- Accepted language:
- Rejected alternatives:
- Why it landed:
- Date:
```
