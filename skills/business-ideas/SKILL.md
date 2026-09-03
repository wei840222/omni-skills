---
name: business-ideas
description: "Use when the user wants to brainstorm new business ideas, apply startup frameworks, or validate the market viability of side projects."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💡"}'
  related-skills: '{"business":"Strategy and planning for generated ideas.","indie-hacker":"Bootstrap and grow side projects solo.","startup":"Launch and scale the validated business concept."}'
---

## When to Use

User wants new business ideas, startup concepts, or side project inspiration. Agent generates ideas using proven frameworks, filters by constraints, and validates viability.

## State location

Business ideas state may exist in `<workspace>/business-ideas/`, `<workspace>/memory/business-ideas/`, or `~/business-ideas/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/business-ideas/`, `<workspace>/memory/business-ideas/`, `~/business-ideas/`.
3. If none exists and state must be created, default to `<workspace>/business-ideas/`.

Use the selected `<state_root>` for every state operation in this skill.

```text
<state_root>/
├── ideas.md           # HOT: generated ideas with scores
├── favorites.md       # WARM: ideas user marked for exploration
├── filters.md         # User's default filters and preferences
└── archive/           # COLD: rejected or explored ideas
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| State structure | `references/memory.md` | When initializing state or determining the schema for saving ideas. |
| Idea frameworks | `references/frameworks.md` | When generating new business ideas or brainstorming concepts. |
| Validation rules | `references/validation.md` | When the user asks how to test, validate, or verify an idea's viability. |
| Research sources | `references/tech.md` | When citing Gate 6 validation / discovery sources or refreshing domain notes. |

## Core Rules

### 1. Generate Unique Ideas
Before generating, scan `<state_root>/ideas.md` for existing concepts. Ensure each new idea is meaningfully differentiated from previous generations.

### 2. Apply Filters
Ask for or use stored filters before generating:

| Filter | Options |
|--------|---------|
| Industry | Tech, Health, Finance, Education, Consumer, B2B, Creator |
| Model | SaaS, Marketplace, Agency, Product, Content, Service |
| Investment | Bootstrap ($0-1K), Seed ($1K-50K), Funded ($50K+) |
| Time | Side project (5h/week), Part-time, Full-time |
| Skills | Technical, Non-technical, Hybrid |

### 3. Score Every Idea
Rate each idea on 5 dimensions (1-10):

| Dimension | Question |
|-----------|----------|
| Market | Is there proven demand? |
| Timing | Why now? What changed? |
| Moat | Can this be defended? |
| Founder-fit | Does user have unfair advantage? |
| Simplicity | Can MVP ship in 30 days? |

**Viability = average score.** Flag ideas scoring 7+ as high-potential.

### 4. Use Frameworks Systematically
Rotate through frameworks to ensure variety. See `references/frameworks.md` for complete list:
- Pain Point Mining
- Trend Riding  
- Existing Business Remix
- Audience First
- Technology Arbitrage

### 5. Batch Generation Mode
When user asks for "ideas" (plural) or "brainstorm":
- Generate 5-10 ideas minimum
- Use multiple frameworks
- Include mix of safe bets and moonshots
- Present as ranked table

### 6. Deep Dive on Request
When user picks an idea to explore:
1. Expand business model canvas
2. Identify 3 biggest risks
3. Suggest validation experiments
4. Estimate time-to-revenue
5. Save to favorites

### 7. Update Memory Proactively

| Event | Action |
|-------|--------|
| Ideas generated | Append to ideas.md with date |
| User likes idea | Move to favorites |
| User rejects idea | Note rejection reason |
| User sets preference | Update filters.md |

## Required Quality Standards

- **Specificity**: Define a clear target customer and unique angle for every idea.
- **Feasibility**: Provide bootstrappable alternatives for ideas that require massive scale.
- **Monetization**: Define a concrete revenue model from day one for pure tech plays.
- **Differentiation**: Require a "10x better" or "10x cheaper" angle when adapting existing solutions.
- **Constraint alignment**: Verify and apply user filters before generation.
