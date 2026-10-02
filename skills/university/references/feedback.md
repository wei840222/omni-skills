# Learning Preferences & Feedback System

## User Profile

Store durable preferences in `<state_root>/config.md`:

```markdown
# Learning Configuration

## Schedule
- Available hours/week: X
- Best study times: mornings / evenings / flexible
- Non-study days: [list]
- Vacation periods: [dates]

## Preferences

### Format
- Primary: visual / auditory / reading / kinesthetic
- Flashcards: yes / no
- Audio content: yes / no
- Video preference: short clips / full lectures

### Sessions
- Preferred length: 15 / 30 / 45 / 60+ minutes
- Break frequency: every X minutes
- Pomodoro: yes / no

### Difficulty
- Start level: beginner / intermediate / advanced
- Ramp-up speed: slow / medium / fast
- Challenge preference: comfortable / pushed

### Communication
- Notification frequency: high / medium / low
- Reminder timing: morning / evening
- Motivation style: cheerleader / drill sergeant / neutral

## Learning Style Notes
<!-- Agent fills this based on observations -->
```

## Observation rules

- One signal is a hypothesis; confirm after two consistent observations before rewriting defaults
- Store declared preferences immediately after consent; store inferred preferences with a one-line rationale
- Motivation style must stay supportive even when the learner chooses "drill sergeant" intensity for tasks
- Communication frequency respects offline hours and host notification limits

## Feedback loops

| Event | Update |
|-------|--------|
| Learner states a preference | Write to `config.md` |
| Session format fails twice | Move one rung; note in Learning Style Notes |
| Weekly hours miss pattern | Adjust plan estimates; optional note in config |
| High fatigue language | Suggest shorter blocks; preserve goals |

## Privacy

- Keep institutional IDs, passwords, and graded live submissions out of config
- Minimum necessary academic context only
