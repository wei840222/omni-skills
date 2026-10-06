# Decomposition techniques — first principles

Load this file for Five Whys depth, component maps, cost stacks, constraint maps, and rebuild synthesis.

## Enhanced Five Whys

Ordinary 5 Whys often stops at operational symptoms. First-principles depth continues:

```text
Levels 1–3: surface / operational causes
Levels 4–5: systemic / organizational causes
Level 6+:   physics, logic, or economics fundamentals
```

Example:

1. Why is shipping slow? → Warehouse is far
2. Why far? → Land was cheap there
3. Why prioritize cheap land? → Minimize fixed costs
4. Why minimize fixed costs that way? → Assumed variable costs scale better
5. Why that assumption? → Historical model when labor was cheap
6. **Fundamental trade-off:** fixed cost (location) versus variable cost (distance shipping). Neither side is a law of nature.

## Component mapping

Break the system into components, then classify each:

| Component | Function | Fundamental need? | Alternative implementations |
| --- | --- | --- | --- |
| Battery | Store energy | Energy storage | Capacitors, hydrogen, flywheel, grid buffer |
| Wheels | Transfer motion | Motion transfer | Tracks, legs, maglev |
| Steel frame | Structure | Load-bearing structure | Aluminum, composites |

Insight: **functions** are closer to fundamentals; **implementations** are negotiable.

## Cost decomposition

For any “too expensive” claim:

```text
Total cost ≈ Σ (material_i × quantity_i) + labor + overhead + margin + compliance

For each line:
├── Is this material required by the function?
├── Is this quantity required by physics/quality limits?
├── Is this labor required by the process, or by habit?
├── Is this margin a business choice?
└── Is this compliance a real legal constraint?
```

Use public, dated sources when quoting market prices. Do not invent $/kWh or commodity figures from memory.

## Constraint mapping

| Constraint | Type | Changeable? | How |
| --- | --- | --- | --- |
| Speed of light | Physics | No | — |
| Minimum viable feature set | Logic / product definition | Partially | Redefine “viable” with user evidence |
| Regulatory approval | Legal | Sometimes | Redesign, reclassify, relocate, petition |
| “Industry standard” practice | Convention | Yes | Prove a better path |
| Team capacity | Resource | Yes | Hire, automate, narrow scope |

Spend energy on changeable constraints. Physics is not negotiable; conventions are.

## Function analysis

```text
Product: electric car
├── Stated function: personal transportation
├── Deeper function: move a person from A to B on demand
└── Fundamental need: mobility / access

Alternative paths to mobility:
├── Better transit (no personal vehicle)
├── Remote work (no commute)
├── Relocate (shorter distance)
└── Shared autonomous fleet (access without ownership)
```

Moving up the function ladder expands the solution space.

## Physics checklist

Before accepting a rebuilt option:

- [ ] Conservation of energy respected?
- [ ] Thermodynamic limits acknowledged?
- [ ] Material properties realistic for the environment?
- [ ] Information or bandwidth limits considered when relevant?
- [ ] Scale effects (for example square-cube) accounted for?

A design that violates physics is not a candidate solution.

## Synthesis from fundamentals

1. List verified fundamentals (physics, logic, math, binding rules)
2. Define the minimum viable function
3. Generate options per function without filtering on convention
4. Evaluate options against fundamentals only
5. Combine the best feasible options
6. Validate against the original problem and build constraints

Build **up** from fundamentals. Avoid merely trimming a legacy design downward.
