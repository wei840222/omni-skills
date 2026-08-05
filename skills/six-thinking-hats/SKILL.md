---
name: six-thinking-hats
description: Analyze decisions, problems, or ideas using De Bono's Six Thinking Hats parallel thinking method. Use when the user needs structured multi-perspective analysis, wants to evaluate options from different angles, or mentions six thinking hats, parallel thinking, or decision analysis.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎩"}'
  related-skills: '{"brainstorm":"Generates creative ideas before or after structured hat analysis.","decide":"Applies decision frameworks to evaluate options produced by hat analysis.","first-principles-thinking":"Breaks problems to foundational truths, complementing hat-based perspective exploration."}'
---

## State location

Six Thinking Hats state may exist in `<workspace>/six-thinking-hats/`, `<workspace>/memory/six-thinking-hats/`, or `~/six-thinking-hats/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/six-thinking-hats/`, `<workspace>/memory/six-thinking-hats/`, `~/six-thinking-hats/`.
3. If none exists and state must be created, default to `<workspace>/six-thinking-hats/`.

Use the selected `<state_root>` for every state operation in this skill.

## The Six Hats

| Hat | Focus | Key Question |
|-----|-------|--------------|
| White | Facts, data | What do we know? What data is missing? |
| Red | Emotions, intuition | How do I feel about this? Gut reaction? |
| Black | Risks, problems | What could go wrong? Why might this fail? |
| Yellow | Benefits, value | What are the advantages? Best case? |
| Green | Creativity, alternatives | What else is possible? New ideas? |
| Blue | Process, control | What's the next step? Summary? |

For detailed guidance on each hat, read `references/hats.md`.

## Core Rules

### 1. One Hat at a Time
- Wear only ONE hat at each moment
- Complete that perspective before switching
- Announce hat changes explicitly

### 2. Sequence Matters
Standard sequence for decisions:
1. **Blue** — Define the problem
2. **White** — Gather facts
3. **Green** — Generate options
4. **Yellow** — Evaluate benefits (per option)
5. **Black** — Evaluate risks (per option)
6. **Red** — Gut check
7. **Blue** — Conclude and decide

### 3. Keep It Parallel
- Everyone thinks in the same direction
- Each hat gets its full moment

### 4. Red Hat Is Brief
- Emotions only, no justification
- 30 seconds max
- "I feel excited" not "I feel excited because..."

### 5. Black Hat Is Constructive
- Critical thinking to identify risks
- Identifies risks to ADDRESS, paired with Yellow for balance

### 6. Green Hat Forces Output
- Generate at least 3 alternatives
- No judgment during Green
- Quantity over quality first

### 7. Blue Hat Owns the Process
- Opens and closes the session
- Summarizes each hat's findings
- Makes the meta-decisions

## Output Format

When analyzing a decision, structure output as:

```markdown
## Analysis: [Topic]

### Blue Hat: Framing
[Problem statement, scope, goal]

### White Hat: Facts
[Known data, missing information, sources]

### Green Hat: Options
1. [Option A]
2. [Option B]
3. [Option C]

### Yellow Hat: Benefits
| Option | Benefits |
|--------|----------|
| A | [benefits] |
| B | [benefits] |
| C | [benefits] |

### Black Hat: Risks
| Option | Risks |
|--------|-------|
| A | [risks] |
| B | [risks] |
| C | [risks] |

### Red Hat: Gut Check
[Brief emotional response to each option]

### Blue Hat: Conclusion
[Summary, recommendation, next steps]
```

## Alternative Sequences

For different contexts, use these sequences:

**New Ideas:**
1. Blue (frame) → Green (generate) → Yellow (find value) → Black (find risks) → White (check facts) → Blue (decide)

**Problem Solving:**
1. Blue (define problem) → White (gather data) → Black (identify causes) → Green (solutions) → Yellow (evaluate) → Blue (conclude)

**Quick Decisions:**
1. Blue (frame) → White + Yellow + Black (rapid assessment) → Red (gut check) → Blue (decide)

## Common Traps and How to Handle Them

| Trap | Consequence | Recovery |
|------|-------------|----------|
| Mixing hats | Analysis becomes confused, key perspectives missed | Return to Blue hat, restate current hat, restart that section |
| Skipping Red | Intuition that might catch what logic misses is ignored | Add Red hat after Black/Yellow evaluation |
| Black without Yellow | Decisions feel negative, good options get rejected | Always pair Black with Yellow for balance |
| Green without constraints | Impractical ideas waste time | Follow Green with Black to evaluate feasibility |
| No Blue at end | Analysis without actionable conclusion | Always close with Blue hat summary and next steps |

## Persistent State

When the user wants to save analyses or track preferences, create `<state_root>/memory.md` with this structure:

```markdown
# Six Thinking Hats Memory

## Status
setup: ongoing | complete | paused | never_ask
version: 1.0.0
last_interaction: YYYY-MM-DD

## Preferences
output_format: full | abbreviated
archive_analyses: yes | no
favorite_sequence: standard | custom
emphasis_hats: [list of hats to spend more time on]

## Custom Sequences
<!-- If user prefers different hat orders for different contexts -->

## Recent Analyses
<!-- Last 3-5 analyses with dates and outcomes -->
```

Save incrementally — capture preferences as they emerge. Archive completed analyses if the user wants history.
