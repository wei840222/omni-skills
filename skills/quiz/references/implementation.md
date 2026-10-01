# Quiz implementation

Use this when building flows, choosing tools, or reviewing UX—not when the only task is writing stems.

## Platforms and tools (orientation)

### No-code builders

- Typeform-style flows: polished UX; strong for lead-gen and personality
- Interact-style marketing quiz builders: outcome-oriented marketing quizzes
- Google Forms: free/basic internal assessments
- Jotform-style builders: flexible templates
- Quizlet: flashcard/learn modes — route product-specific work to the `quizlet` skill

### LMS-integrated

- Canvas / Moodle / Blackboard built-in quizzes for courses
- Articulate/Storyline-style e-learning with branching
- WordPress LMS plugins for course quizzes

### Custom development

Build custom when you need proprietary scoring, deep branching, system integration, custom gamification, or strict data ownership.

Treat vendor feature and pricing claims as time-sensitive; verify on current vendor docs before asserting them as facts (`sources.md`).

## Data model (logical)

```text
Quiz
├── id, title, description, settings
├── Questions[]
│   ├── id, text, type, order
│   ├── Options[]
│   │   ├── id, text, isCorrect?, points?
│   │   └── outcomeMapping? (personality)
│   └── explanation? (learning feedback)
├── Outcomes[] (personality / assessment bands)
│   ├── id, title, description, media?
│   └── score range or trait mapping
└── Results[] (runtime; not skill-package state)
    ├── quizId, respondentId?, timestamp
    ├── answers[], score, duration
    └── outcomeId?
```

Persist respondent PII and raw answers outside the skill git tree. Optional author drafts may use `<state_root>/drafts/`.

## UX patterns

### Progress

- Progress bar and/or “3 of 10”
- Optional time remaining for timed exams
- Uncertainty without progress increases abandonment (see Baymard progress-indicator research in `sources.md`)

### Navigation

- Linear (forced order) vs free navigation
- Review-before-submit for low-stakes learning
- Mark-for-review on longer assessments

### Feedback timing

| Mode | When | Best for |
|------|------|----------|
| Immediate | After each item | Learning / practice |
| End of quiz | After submit | Assessment purity |
| Delayed | After deadline | Timed exams / certifications |

### Mobile

- Large tap targets (aim for WCAG 2.2 target-size minimum guidance; see `sources.md`)
- Readable text without zoom
- Vertical scrolling only for options
- No hover-only interactions
- Autosave progress on flaky connections when quizzes are long

## Gamification (optional)

| Element | Purpose | Caution |
|---------|---------|---------|
| Streaks | Momentum | Can punish interruption |
| Points | Feedback | Vanity points without meaning |
| Leaderboards | Social competition | Privacy / demotivation risk |
| Badges | Milestone marking | Easy to feel hollow |

Use gamification only when it serves the stated goal.

## Accessibility quick pass

- Labels on every control; do not rely on color alone for correct/incorrect
- Keyboard reachability for custom widgets
- Sufficient contrast on selected/disabled states
- Announce progress and errors to assistive tech when building custom UI

## Implementation checklist

- [ ] Scoring rules written before UI polish
- [ ] Outcome mapping covered for every personality path
- [ ] Progress indicator present for multi-step flows
- [ ] Feedback timing matches stakes
- [ ] Mobile tap targets and layout checked
- [ ] No secrets or real respondent exports committed to the skill package
