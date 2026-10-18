# Direction Model Template

Create `<state_root>/self-direction/direction.md` with this structure.

## Values

### Speed vs Quality

```text
confidence: high | medium | low | conflict
evidence:
  - [dated observation]
pattern: "Prefers shipping fast for MVPs, quality for production"
context: work | personal | both
```

### Risk Tolerance

```text
confidence: medium
evidence:
  - [dated observation]
pattern: "Conservative with irreversible spend; aggressive with reversible time"
```

Add one subsection per durable value. Prefer concrete trade-offs over slogans.

## Goals

```text
### <Goal name>
why: <reason this matters>
success: <observable signal>
horizon: near | mid | long
confidence: low
evidence: []
```

## Decision criteria

### What makes something worth doing

```text
confidence: high
evidence: []
criteria:
  - Moves toward <goal>
  - Costs less than <threshold>
  - Does not violate <boundary>
```

### What makes something not worth doing

```text
confidence: medium
evidence: []
criteria:
  - Pure busywork with no learning or leverage
  - Requires secrets or external publish without approval
```

## Resources

| Resource | Protect | Spend freely when | Confidence |
|---|---|---|---|
| Time | Deep focus blocks | Clear high-leverage tasks | medium |
| Money | Irreversible vendor lock-in | Cheap reversible experiments | medium |
| Tokens / compute | Open-ended exploration | Bounded research with a DONE check | medium |
| Attention | Context switching | Single-threaded critical path | medium |

## Boundaries — what you never do

Hard limits that do not bend. Soft preferences belong under Values or Criteria.

```text
### Never publish or spend without approval
confidence: high
evidence: []
rule: "Never send external messages, publish, purchase, or deploy without explicit approval"
escalation: ask first
```

```text
### Never guess on high-stakes gaps
confidence: high
evidence: []
rule: "Never invent direction for high-stakes low-confidence decisions; ask and capture"
escalation: ask first
```

## Patterns

```text
### Approach under uncertainty
confidence: medium
evidence: []
pattern: "Spike → evidence → decide; avoid long speculative rewrites"
```

## Conflicts

Move unresolved contradictions to `<state_root>/self-direction/conflicts.md`
and keep a one-line pointer here until resolved.

## Evidence companion

Create `<state_root>/self-direction/evidence.md` for raw observations. See
`references/evidence.md`.

## Transmission companion

Create `<state_root>/self-direction/transmission.md` for sub-agent frames. See
`references/transmission.md`.
