# Memory setup — Meditate

## Initial setup

On first authorized write, ensure the resolved state tree exists:

```bash
mkdir -p <state_root>/archive
```

Replace `<state_root>` with the absolute directory selected by the State location rules. Do not create the literal folder name `<state_root>`.

## profile.md template

Copy to `<state_root>/profile.md`:

```markdown
# User Profile

## Detected Type
<!-- entrepreneur | developer | creative | personal | system | unknown -->
Type: unknown
Confidence: low
Last updated: none

## Rhythm Preferences
Frequency: conservative
Last meditation: none
Feedback rate: 0%

## Focus Areas
<!-- Topics user has confirmed interest in -->

## Excluded Topics
<!-- Topics user requested to exclude -->

---
*Updated from feedback signals*
```

## topics.md template

Copy to `<state_root>/topics.md`:

```markdown
# Active Meditation Topics

## High Priority
<!-- Topics with positive feedback -->

## Normal Priority
<!-- Default topics based on profile -->

## Low Priority
<!-- Topics with no feedback yet -->

## Excluded
<!-- User explicitly said no -->

---
*Priorities shift based on user feedback*
```

## insights.md template

Copy to `<state_root>/insights.md`:

```markdown
# Pending Insights

<!-- Maximum 3 pending at any time -->
<!-- Format:
## [YYYY-MM-DD] Topic
**Observation:** ...
**Question:** ...
**Context:** ...
Generated: HH:MM
-->

---
*Present oldest first*
```

## feedback.md template

Copy to `<state_root>/feedback.md`:

```markdown
# Feedback Log

<!-- Format:
## YYYY-MM-DD
- Topic: [topic]
- Insight: [summary]
- Response: [positive|neutral|negative|silence]
- Action: [continue|demote|exclude|prioritize]
-->

## Stats
Total: 0
Positive: 0
Neutral: 0
Negative: 0
Silence: 0

---
*Stats update when feedback is recorded*
```

## Legacy migration

If meditation files are found only under a legacy vendor path outside the candidate roots, copy them once into the resolved `<state_root>/` with user consent, report what moved in one line, and leave the skill package free of marketplace homepage links.
