# Setup — Self-Direction

Read this when `<state_root>/self-direction/` does not exist or is empty.

## Attitude

Learn how this person thinks, decides, and prioritizes. Capture the WHY behind
decisions. Stay curious; do not turn the first session into an interrogation.

## First session

Start in real work. Invite optional upfront direction, then capture signals as
they appear.

Good opening:

> I'd like to learn how you think about priorities and decisions so I can work
> more autonomously over time. As we work, I'll pick up preferences. If you want
> to tell me anything upfront about what matters to you, I'm listening.

## What to capture

### Explicit signals (high value)

- "I always want…" → value / criterion
- "Never do X without…" → boundary
- "Because…" → reasoning
- "That's not right; it should be…" → correction

### Implicit signals (build over time)

- Choosing A over B → criteria
- Spending time on X but not Y → resource priorities
- Strong positive / negative reactions → values
- Rejected suggestions → boundaries

## Learning loop

After each significant interaction:

1. Did I learn anything about their direction?
2. Should I capture it to the model?
3. What confidence level?
4. Does it conflict with earlier captures?

## Validation moments

Periodically (not every session):

- Share 3–5 key elements of the current model
- Ask whether they are accurate
- Update confidence

## When to ask directly

Ask only when:

- A high-stakes decision is imminent
- The model contains a conflict
- A gap blocks useful help
- The user asked to establish something explicitly

Ask as a collaborator:

- "For this decision, would you prioritize X or Y?"
- "I see both A and B in past choices. What distinguishes them?"

## Creating the initial model

After the first useful signals, create
`<state_root>/self-direction/direction.md` from `assets/memory-template.md`:

- A shallow model is better than none
- Mark new entries low-confidence
- Note gaps explicitly

## File structure

```text
<state_root>/self-direction/
├── direction.md
├── evidence.md
├── confidence.md
├── conflicts.md
└── transmission.md
```

Legacy `~/Clawic/data/self-direction/` is a migration source only. When the user
asks, move it into the resolved `<state_root>/self-direction/` and report the
move in one line.

## Goal

Enough faithful direction that the agent can decide, explain, and brief
sub-agents as the user would — without inventing priorities the model does not
support.
