---
name: six-thinking-hats
description: Use this skill when the user needs to analyze a decision, evaluate options from multiple perspectives, or solve a complex problem. Applies De Bono's Six Thinking Hats parallel thinking method to explore facts (White), emotions (Red), risks (Black), benefits (Yellow), alternatives (Green), and process (Blue) in structured sequences. Use when the user mentions six thinking hats, parallel thinking, multi-perspective analysis, decision analysis, or wants to evaluate options systematically — even if they don't explicitly name the method.
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
- Announce hat changes explicitly: "Switching to Black hat now"

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
All participants think in the same direction at the same time. This replaces adversarial debate (where one side argues for and another argues against) with collaborative exploration where everyone examines each perspective together.

### 4. Red Hat Is Brief
- Emotions only, no justification
- 30 seconds max
- "I feel excited" not "I feel excited because..."

### 5. Black Hat Is Constructive
- Critical thinking to identify risks
- Identifies risks to ADDRESS, paired with Yellow for balance
- Research shows dedicated "Black hat" evaluation leads to higher-quality ideas in design thinking by surfacing assumptions early

### 6. Green Hat Forces Output
- Generate at least 3 alternatives
- No judgment during Green
- Quantity over quality first
- Connects to de Bono's lateral thinking: dig a new hole, not the same hole deeper

### 7. Blue Hat Owns the Process
- Opens and closes the session
- Summarizes each hat's findings
- Makes the meta-decisions about which hat comes next

## Choosing the Right Sequence

| Context | Sequence | Why |
|---------|----------|-----|
| Strategic decision | Blue → White → Green → Yellow → Black → Red → Blue | Full analysis covers all angles |
| Quick operational choice | Blue → White + Yellow + Black → Red → Blue | Rapid assessment when time is limited |
| Creative challenge | Blue → Green → Yellow → Black → White → Blue | Generate first, evaluate later |
| Problem diagnosis | Blue → White → Black → Green → Yellow → Blue | Understand causes before solutions |
| Conflict resolution | Blue → Red → White → Green → Yellow → Black → Blue | Surface emotions early, then find common ground |

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

## Gotchas

- **Black hat dominance**: Humans naturally default to critical thinking. Enforce equal time for Yellow hat to balance risk identification with benefit exploration.
- **Red hat skipping**: Teams often skip emotions because it feels unprofessional. Surface feelings early to prevent them from derailing logical analysis later.
- **Mixed hats**: When someone argues benefits while another raises risks, the analysis becomes confused. Return to Blue hat, restate the current hat, and restart that section.
- **No Blue closure**: Analysis without a Blue hat conclusion lacks actionable next steps. Always close with a summary and decision.
- **Green hat premature judgment**: Evaluating ideas during Green hat kills creativity. Generate at least 3 alternatives before any criticism.

## AI-Specific Guidance

When applying Six Thinking Hats as an AI agent:

1. **Explicit hat announcements**: State "Now switching to [color] hat" before each perspective change. This improves output quality by signaling clear context shifts.
2. **Separate passes**: Run each hat as a distinct section rather than blending perspectives. Parallel thinking works best when each direction gets dedicated attention.
3. **Black hat as provocateur**: Use Black hat to challenge assumptions and surface hidden risks. Research shows critical-evaluator roles produce higher-quality ideas.
4. **Red hat framing**: When expressing Red hat perspective, use "This feels [exciting/concerning/risky] because..." — the user wants the AI's assessment, not genuine emotion.
5. **Blue hat synthesis**: Always close with Blue hat. Summarize findings across all hats and provide a clear recommendation with next steps.

## Recovery Actions

When a trap occurs, apply the matching recovery:

| Trap | Recovery |
|------|----------|
| Mixing hats | Blue hat → restate current hat → restart that section |
| Skipping Red | Add Red hat after Black/Yellow evaluation |
| Black without Yellow | Immediately follow with Yellow hat at equal depth |
| Green without constraints | Follow Green with Black hat to evaluate feasibility |
| No Blue at end | Close with Blue hat summary, recommendation, and next steps |

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
