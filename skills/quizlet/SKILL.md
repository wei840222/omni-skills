---
name: quizlet
description: "Trigger this skill to manage Quizlet study workflows, including designing high-yield card sets, selecting optimal study modes (Learn, Test), diagnosing poor retention, and analyzing weak cards. Trigger strictly for Quizlet workflows; route Anki or general knowledge tasks elsewhere."
metadata:
  related-skills: '{"flashcards": "Core flashcard writing rules and question quality patterns", "study": "Structured study planning and session management workflows", "exam": "Exam-specific preparation, prioritization, and review strategy"}'
  openclaw: '{"requires": {"config": ["<state_root>/quizlet/"]}}'
---

## Setup

On first use, read `references/setup.md` for activation boundaries and context capture priorities.

## When to Use

Use this skill when the user is studying with Quizlet and needs better set design, mode selection, session planning, or recovery from weak retention.

## State location

State is persisted to the local workspace.

Lookup order and creation logic:
1. `<state_root>/quizlet/` (Primary)
2. If not found, create `<state_root>/quizlet/` upon first study setup.

Structure:
```text
<state_root>/quizlet/
|-- memory.md           # Status, activation boundaries, and learning context
|-- set-playbooks.md    # Reusable set patterns by subject and goal
|-- weak-cards.md       # Rewritten cards and recurring failure patterns
`-- session-plans.md    # Time-boxed study plans and exam countdown strategy
```
See `references/memory-template.md` for structure and status fields.

## Quick Reference

Use the smallest relevant file for faster and more accurate recommendations.

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When initializing the skill or changing context |
| Memory template | `references/memory-template.md` | When creating or updating the memory file |
| Building high-yield sets | `references/set-design.md` | When helping the user create new study sets |
| Choosing study modes | `references/study-modes.md` | When deciding which Quizlet study mode to use |
| Diagnosing poor retention | `references/diagnostics.md` | When the user struggles to recall cards |
| Import and cleanup workflows | `references/imports.md` | When importing notes or external sets into Quizlet |
| Core rules and guidelines | `references/core-rules.md` | Always, provides core guidelines for set creation and workflows |
| Common pitfalls and mistakes | `references/common-traps.md` | Always, to learn correct study strategies and correct common errors |
| Domain Knowledge and Features | `references/research.md` | When you need information on Quizlet's features like Learn mode, Test mode, or Q-Chat |
