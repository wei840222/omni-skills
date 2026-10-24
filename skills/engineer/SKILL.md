---
name: engineer
description: Trigger when evaluating system requirements, comparing designs via trade-offs, planning execution steps, or troubleshooting complex process failures. Use `software-engineer` for standard code implementation.
metadata:
  openclaw: '{"emoji":"🛠️"}'
  related-skills: '{"analytics": "Measurement and evidence framing once verification criteria exist.", "architecture": "System structure and boundary decisions beyond single-process engineering judgment.", "cto": "Org-level tech strategy when the decision exceeds local system design.", "product-manager": "Product scope and prioritization adjacent to engineering trade-offs.", "software-engineer": "Implementation and code debugging once the engineering plan is set."}'
---
## When to Use

Trigger this skill when transitioning vague ideas into system requirements, constraints, interfaces, and acceptance criteria. It is designed to aid in evaluating designs, comparing trade-offs, defining failure modes, and establishing execution or troubleshooting sequences.

**Scope Limitations:**
Route requests for direct code implementation, debugging scripts, or pure business strategy to specialized skills like `software-engineer` or `cto`.

## State location

Engineer state may exist in `<workspace>/engineer/`, `<workspace>/memory/engineer/`, or `~/engineer/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/engineer/`, `<workspace>/memory/engineer/`, `~/engineer/`.
3. If none exists and state must be created, default to `<workspace>/engineer/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/engineer/`. See `references/setup.md` for initialization and `references/memory-template.md` for schema details.
Persistence is optional; session-only execution is the default.

```text
<state_root>/engineer/
├── memory.md         # Optional activation preferences and output defaults
├── decisions/        # Optional decision records and option comparisons
├── assumptions/      # Optional assumption ledgers and open questions
├── verification/     # Optional test plans, readiness checks, and evidence logs
└── archive/          # Optional retired decisions and closed investigations
```

## Quick Reference

Load the specific file corresponding to the current engineering task to maintain context:

| Category | Description | File to Load |
|----------|-------------|--------------|
| **Core** | Setup, defaults, and activation behavior | `references/setup.md` |
| **Data** | Optional local memory schema | `references/memory-template.md` |
| **Design** | Constraint framing and design envelope | `references/constraints-first.md` |
| **Architecture** | System boundaries and handoff logic | `references/interface-map.md` |
| **Risk** | Failure analysis and containment | `references/failure-modes-first.md` |
| **Decisions** | Option comparison and trade-off scoring | `references/trade-off-matrix.md` |
| **Testing** | Validation depth and evidence planning | `references/verification-ladder.md` |
| **Execution** | Rollout, changeover, and execution planning | `references/execution-planning.md` |
| **Operations** | Troubleshooting unstable systems | `references/troubleshooting.md` |
| **Pitfalls** | Common traps and better alternatives | `references/common-traps.md` |

## Engineering Output Pack

For substantial tasks, deliver recommendations using the following structure:
- Problem statement and success criteria
- System boundary and interfaces
- Constraints ledger
- Option comparison
- Failure modes and containment
- Verification ladder
- Execution sequence with owners and hold points

## Security & Privacy

**Data that leaves your machine:**
- None by default.

**Data stored locally:**
- Optional configurations in `<state_root>/engineer/`.

**Operational Boundaries:**
- Route production code writing to `software-engineer`.
- Maintain offline execution.
- Request explicit authorization before storing credentials or proprietary data.

## Trust

Provides structured engineering reasoning without relying on third-party services or requiring credentials.
