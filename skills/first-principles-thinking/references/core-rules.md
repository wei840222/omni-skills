# Core rules — first principles thinking

Load this file when running the full protocol, writing the structured output, or checking common traps.

## Three-step protocol

### 1. Decompose

Break the problem into fundamental components:

- Absolute physical or logical constraints
- What is actually true versus assumed true
- Conventions, traditions, and analogies stripped out of the claim set

### 2. Verify

Challenge each remaining component:

- “Why do we believe this?” — trace origin
- “Is this a law of nature or a human convention?”
- “What evidence shows this is fundamental?”
- “What would falsify it?”

### 3. Rebuild

Construct a solution from verified fundamentals only:

- Build up from proven truths
- Use “how others do it” only when that path is independently optimal
- Keep every layer connected to a verified fundamental
- Filter out options that violate physics or named hard constraints

## Constraint test

For each constraint, classify and act:

| Type | Action |
| --- | --- |
| Law of physics | Respect |
| Logical necessity | Respect |
| Regulation / contract | Changeable with process, cost, or jurisdiction |
| Convention | Challenge; keep only if still optimal |
| Untested assumption | Verify before treating as binding |

## When first principles is the wrong tool

First principles is expensive. Prefer analogical reasoning when:

- The problem is well-understood with proven solutions
- Time pressure rules out deep analysis
- Marginal improvement is enough
- The domain is stable and innovation value is low

Rule of thumb: first principles for novel or failed-conventional problems; analogy for routine optimization.

## Socratic depth (example pattern)

```text
Claim: "Electric cars are too expensive"
Why expensive? → Batteries dominate cost
Why batteries expensive? → Materials + manufacturing
Why those materials? → Current chemistry needs them
Is chemistry fundamental? → No; energy storage is the function

Fundamental need: energy storage density/cost under safety limits
Not fundamental: a specific cobalt-bearing cell chemistry
```

Stop only at physics, logic, math, or an explicit regulation that truly binds the decision.

## Blank-slate test

Ask: if we started today with current knowledge and tools, and no legacy solution existed, how would we solve this?

Use this to bypass sunk-cost and “we already built X” lock-in.

## Output format

```markdown
## Problem Statement
[One-sentence outcome that matters]

## Assumed Constraints (to verify)
- Constraint A — [source class: historical / authority / analogical / social / resource / technical / market]
- Constraint B — [source class]

## Fundamental Truths
- Truth 1 (physics / logic / math / named regulation)
- Truth 2

## Decomposition
[Functions and components; implementations marked non-fundamental]

## Rebuilt Solution
[Option built only from verified fundamentals; implementation notes]

## Assumptions Challenged
- [Claim that looked fundamental and was not]
```

## Common traps (positive recovery)

| Trap | Do instead |
| --- | --- |
| Stopping at “materials are expensive” | Keep asking until mass, energy, or process limits appear |
| Treating difficulty as impossibility | Separate engineering hardness from physics impossibility |
| Rejecting all analogy | Keep analogy as a fast heuristic; switch to first principles when it fails |
| Analysis paralysis | Time-box decomposition; ship a better-grounded option, not a perfect ontology |
| Ignoring buildability | Attach materials, labor, regulation, and ops constraints to the rebuild |
| Solo unchallenged reasoning | Invite a second perspective on the assumption list when stakes are high |

## Domain prompt starters

| Domain | First question |
| --- | --- |
| Business | What does the customer fundamentally need (not merely want)? |
| Engineering | What do physics and materials actually allow? |
| Product | What job is being done at the most basic level? |
| Cost | What are the raw inputs and minimum required labor? |
| Process | Which steps are logically necessary versus historically accumulated? |

## Security and privacy

- All reasoning stays in the conversation context; no skill-local persistent state.
- No network calls and no package-local file writes during normal use.
- Load `references/sources.md` only when citing external definitions or method history.
