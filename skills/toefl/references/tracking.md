# Progress Tracking System

## File structure in `<state_root>/toefl/`

### profile.md

```markdown
# TOEFL Profile

## Basic Info
- Name: [Name]
- Test Date: YYYY-MM-DD
- Days Remaining: N
- Delivery mode: test center | Home Edition

## Target Scores
- Overall goal (1–6): X.X
- Overall goal (0–120, if school still uses it): NNN
- Section floors (if any): R / L / S / W
- MyBest accepted by targets?: yes / no / mixed / unknown

## Target Schools / Pathways
| Organization | Program or visa | Required overall | Section minima | MyBest? | Source URL |
|--------------|-----------------|------------------|----------------|---------|------------|
| MIT | MS CS | … | … | no | https://… |

## Current Status
- Latest practice / official: date
- Section breakdown (1–6 and/or 0–30): R… L… S… W…
- Overall (1–6 / 0–120 comparable): …
- MyBest potential: …

## User Type
- [ ] Student (university application)
- [ ] Professional (immigration / employer)
- [ ] Tutor (managing students)
- [ ] Retaker (improving previous score)
```

### sections/{section}.md

```markdown
# Reading Progress

## Current Status
- Latest score: …
- Mastery: …
- Trend: ↑ / → / ↓

## Weak Task Types (sorted by frequency)
| Type | Accuracy | Priority |
|------|----------|----------|
| Complete the Words | 60% | ★★★★★ |
| Read an Academic Passage — inference | 65% | ★★★★ |

## Strong Areas
- Daily-life main idea: 95%

## Error Log (last 10)
| Date | Task type | Error reason |
|------|-----------|--------------|
| 02-13 | Academic Passage | Missed qualifier |

## Time Analysis
- Average pace vs section budget
- Items rushed or abandoned
```

Use the same template for `listening.md`, `speaking.md`, and `writing.md`, swapping task-type names from `exam-config.md`.

### sessions/{date}.md

```markdown
# Study Session: YYYY-MM-DD

## Focus Areas
- Speaking Listen and Repeat: 20 min
- Writing Academic Discussion: 25 min
- Vocabulary: 15 min

## Practice Results
- Attempts / estimated scores
- Key issue in one line

## Total Time
## Energy Level
## Key Win
```

### practice/{date}-{label}.md

```markdown
# Practice Set: YYYY-MM-DD label

## Scores
| Section | Score (1–6 or 0–30) | vs Last | vs Target |
|---------|---------------------|---------|-----------|
| Reading | | | |
| Listening | | | |
| Speaking | | | |
| Writing | | | |
| **Overall** | | | |

## Error Analysis
### Speaking
- …

### Writing
- …

## Action Items
1. …
```

### vocabulary/

Optional word lists or spaced-review notes. Keep paths under `<state_root>/toefl/vocabulary/`.

### feedback.md

See `feedback.md` for the preferred structure of effective/ineffective tactics and correction logs.

## Update triggers

| Event | Action |
|-------|--------|
| Study session ends | Write `sessions/{date}.md` |
| Practice set finished | Write `practice/{date}-….md`, update `sections/*` |
| Section improved | Update mastery in section file |
| Weekly review | Summarize progress, adjust plan |
| Official score received | Update profile; recalculate readiness and MyBest potential |

## Metrics to track

### Daily
- Minutes per section
- Items completed
- Error count and type
- Vocabulary reviewed

### Weekly
- Total hours vs plan
- Section score trends
- Weak tasks addressed
- Full or sectional mocks completed

### Monthly
- Trajectory vs target sitting date
- School/visa requirement re-check
- Ready / postpone decision with evidence