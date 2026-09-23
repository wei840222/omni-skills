---
name: ux-researcher
description: Generate personas, pain points, journey maps, heuristic evaluations, and UX recommendations from product context without interviews. Use when the user asks for UX research, persona generation, journey mapping, pain-point analysis, competitive UX comparison, or heuristic evaluation.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji": "🔬"}'
  related-skills: '{"product":"Product strategy, validation, and launch framing once research outputs must drive roadmap or listing decisions.","cpo":"Executive product leadership and org-level bets that consume research evidence.","design":"Visual and interaction design execution that turns research findings into concrete UI decisions."}'
---

## State location

UX research state may exist under several candidate roots. Before the first state operation, resolve one `<state_root>`:

1. Use an explicitly configured state root when the user or host supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/ux-researcher/`, `<workspace>/memory/ux-researcher/`, then `~/ux-researcher/`.
3. If none exists and durable research data must be created, ask once and default to `<workspace>/ux-researcher/`.

Keep the selected root for the whole invocation. When more than one candidate exists, use only the highest-precedence directory and tell the user; do not merge or synchronize copies.

### Research state tree

```text
<state_root>/
├── memory.md           # Products researched, preferences, cross-project patterns
└── research/
    └── {product}/
        ├── personas.md
        ├── pain-points.md
        ├── journey-map.md
        └── recommendations.md
```

See `references/memory-template.md` for bootstrap structure. Create child files only when the corresponding research output is produced.

## When to load

Trigger when the user requests UX research, persona generation, journey mapping, pain-point analysis, competitive UX comparison, or heuristic evaluation. Load `references/setup.md` on first use or when `<state_root>/` is empty so integration and context questions run before deep deliverables.

## Core Rules

### 1. Understand the Product First
Before generating any research output:
- What does the product do?
- Who is the target audience?
- What problem does it solve?
- What's the competitive landscape?

Ask clarifying questions until you have enough context.

### 2. Ground Insights in Reality
Base insights on:
- Known patterns in the industry/domain
- Public data (app reviews, forum discussions, competitor analysis)
- Established UX heuristics (Nielsen, etc.)
- Common user behaviors for this type of product

When uncertain, state assumptions explicitly.

### 3. Create Actionable Personas
Personas must drive decisions. Include:
- Goals (what they want to achieve)
- Frustrations (what blocks them)
- Behaviors (how they currently solve the problem)
- Context (when/where they use the product)

Focus strictly on factors that change design decisions rather than demographic fluff.

### 4. Map the Full Journey
Journey maps should cover:
- Discovery: How do they find out about this?
- Evaluation: How do they decide to try it?
- First use: What's the onboarding experience?
- Regular use: What does habitual use look like?
- Edge cases: What breaks or frustrates?

Identify emotional highs and lows at each stage.

### 5. Prioritize Pain Points by Impact
Not all pain points matter equally:
- Frequency: How often does this happen?
- Severity: How bad is it when it happens?
- Alternatives: Can users work around it?

Focus recommendations on high-frequency, high-severity issues.

### 6. Recommendations Must Be Specific
Bad: "Improve the onboarding"
Good: "Add a 3-step progress indicator during signup. Users in this category expect to know how long forms will take — without it, 40%+ abandon mid-flow (industry benchmark)."

Every recommendation needs: What to do + Why it works + Evidence/reasoning.

### 7. Acknowledge Limitations
Synthetic research has limits. Be explicit:
- "This is based on industry patterns, not user interviews"
- "Validate with real users before major decisions"
- "These personas represent archetypes, individual users vary"

Always clearly state that synthetic research is distinct from real user data.

## Capabilities

### Persona Generation
Given a product and target market, generate 2-4 user personas:
- Primary persona (main user)
- Secondary personas (other important segments)
- Anti-persona (who this is NOT for)

### Pain Point Analysis
Identify likely pain points based on:
- Product category patterns
- Competitor weaknesses (from reviews)
- Common UX anti-patterns
- Industry-specific friction points

### Journey Mapping
Create end-to-end journey maps:
- Stages from awareness to advocacy
- Actions, thoughts, emotions at each stage
- Opportunities and pain points
- Moments of truth

### Heuristic Evaluation
Analyze a product/concept against:
- Nielsen's 10 usability heuristics
- Mobile-specific patterns (if applicable)
- Accessibility considerations
- Industry-specific best practices

### Competitive UX Analysis
Compare UX patterns across competitors:
- What do they all do? (table stakes)
- What do leaders do differently?
- What gaps exist in the market?
- What can be learned from their reviews?

### Recommendation Generation
Provide prioritized UX recommendations:
- Quick wins (low effort, high impact)
- Strategic improvements (higher effort, high impact)
- Nice-to-haves (lower priority)

## Output Formats

### Persona Template
```markdown
# Persona: [Name]

## Overview
**Role:** [Job/life role]
**Goal:** [Primary objective with this product]
**Frustration:** [Main pain point]

## Context
- When do they use this? [Situation]
- Where? [Environment]
- How often? [Frequency]
- What device? [Platform]

## Current Behavior
How they solve this problem today (before/without your product)

## Needs
1. [Primary need]
2. [Secondary need]
3. [Tertiary need]

## Frustrations
1. [Main frustration] — [Impact]
2. [Secondary frustration] — [Impact]

## Quote
"[A sentence that captures their mindset]"

## Design Implications
- [What this means for product decisions]
```

### Pain Points Template
```markdown
# Pain Points Analysis: [Product]

## Critical (High frequency + High severity)
### [Pain point 1]
- **What:** [Description]
- **Why it hurts:** [Impact on user]
- **Evidence:** [Industry pattern / competitive gap / etc.]
- **Recommendation:** [How to address]

## Significant (Medium priority)
### [Pain point 2]
...

## Minor (Lower priority)
### [Pain point 3]
...
```

### Journey Map Template
```markdown
# User Journey: [Product]

## Stage 1: Awareness
**User goal:** [What they're trying to achieve]
**Actions:** [What they do]
**Thoughts:** [What they're thinking]
**Emotions:** [How they feel] — 😊/😐/😟
**Opportunities:** [How to improve this stage]

## Stage 2: Consideration
...

## Stage 3: First Use
...

## Stage 4: Regular Use
...

## Stage 5: Advocacy/Churn
...

---
## Key Insights
- Moment of truth: [Critical point]
- Biggest drop-off risk: [Where users leave]
- Delight opportunity: [Where to exceed expectations]
```

### Heuristic Evaluation Template
```markdown
# Heuristic Evaluation: [Product]

| Heuristic | Score | Issue | Recommendation |
|-----------|-------|-------|----------------|
| Visibility of system status | 🟢/🟡/🔴 | [Issue if any] | [Fix] |
| Match with real world | 🟢/🟡/🔴 | ... | ... |
| User control and freedom | 🟢/🟡/🔴 | ... | ... |
| Consistency and standards | 🟢/🟡/🔴 | ... | ... |
| Error prevention | 🟢/🟡/🔴 | ... | ... |
| Recognition over recall | 🟢/🟡/🔴 | ... | ... |
| Flexibility and efficiency | 🟢/🟡/🔴 | ... | ... |
| Aesthetic and minimal design | 🟢/🟡/🔴 | ... | ... |
| Help users with errors | 🟢/🟡/🔴 | ... | ... |
| Help and documentation | 🟢/🟡/🔴 | ... | ... |

## Top 3 Issues
1. [Most critical]
2. [Second]
3. [Third]
```

## Common Traps

- Ground every insight in a known industry pattern, public signal, or explicit assumption the user can challenge
- Build personas around goals, frustrations, behaviors, and design implications rather than demographic filler
- Keep the set to 2–4 personas so each one still changes a decision
- Treat the emotional arc as a first-class journey-map output, not an optional flourish
- Attach evidence or reasoning to every recommendation (what + why + source of confidence)
- Label synthetic research as synthetic and call out what still needs real-user validation
- Define the anti-persona so the product boundary is as clear as the target audience

## Security & Privacy

**Data that stays local:**
- Research outputs stored under the resolved `<state_root>/`
- All research artifacts remain local to the machine

**Boundaries:**
- Read and write only under the selected `<state_root>/`
- Keep full offline operation for skill-owned state
- Do not store credentials, tokens, or third-party account secrets in research files
- If the user pastes private research notes, keep them inside `<state_root>/` and do not publish them
