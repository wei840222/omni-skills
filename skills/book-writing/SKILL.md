---
name: book-writing
description: Plan, draft, and revise long-form books and manuscripts with a structural blueprint, chapter outcomes, voice continuity, and staged revision passes.
metadata:
  openclaw: '{"emoji":"📚"}'
  related-skills: '{"writing": "voice adaptation and writing preference memory", "writer": "anti-robotic writing patterns and rhythm control", "write": "general-purpose drafting support for fast composition", "article": "long-form article structuring and editorial flow", "content-marketing": "audience-driven messaging and conversion framing"}'
---

## State location

Book-writing state may exist in `<workspace>/book-writing/`, `<workspace>/memory/book-writing/`, or `~/book-writing/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state path when one exists.
2. Otherwise, use the first existing directory in this order: `<workspace>/book-writing/`, `<workspace>/memory/book-writing/`, then `~/book-writing/`.
3. If more than one directory exists, use only the highest-precedence directory and tell the user that multiple copies were found; do not merge or synchronize them.
4. If none exists and the user opts into saved project state, create `<workspace>/book-writing/`; if `<workspace>` is unavailable, ask for a state root rather than guessing from the current directory.

Use the same resolved `<state_root>` for the entire invocation. See `references/memory-template.md` for the state schema.

## Setup

On first use, read `references/setup.md` to initialize local memory and capture activation preferences.

## When to Use

Use this skill when the user is writing a nonfiction or fiction book and needs structure, drafting support, revisions, or progress control across many chapters.

```
<state_root>/
├── memory.md          # HOT: status, voice, manuscript state, next actions
├── chapters/          # WARM: chapter-level notes and draft checkpoints
├── revisions/         # WARM: pass-by-pass revision logs
└── archive/           # COLD: retired directions and superseded outlines
```

## Quick Reference

Load these references only when performing the specific phase:

| Phase | Action | Load |
|-------|--------|------|
| **Setup** | Initialize project state | `references/setup.md` |
| **Planning** | Define structure and promises | `references/blueprint.md` |
| **Drafting** | Write new chapters | `references/chapter-loop.md` |
| **Revising** | Polish and structural checks | `references/revision-rubric.md` |
| **Context** | Check project memory | `references/memory-template.md` |
| **Theory** | Review domain principles | `references/knowledge-sources.md` |

## Core Rules

### 1. Lock the Book Promise Before Drafting
Define audience, core promise, transformation, and scope before generating large text blocks. If these are unclear, pause drafting and clarify first.

### 2. Keep a Living Book Blueprint
Use `references/blueprint.md` to maintain title candidates, one-sentence premise, chapter map, and evidence or story assets. Update this blueprint whenever the direction changes.

### 3. Write by Chapter Outcomes, Not Word Count
Each chapter must deliver one concrete outcome for the reader. Start with chapter intent, then draft only material that serves that intent.

### 4. Preserve Voice and POV Consistency
Track voice profile in memory and enforce consistent point of view, tense, reading level, and sentence rhythm across chapters.

### 5. Run Structured Revision Passes
Revise in separate passes: structure, argument or narrative continuity, clarity, and line polish. Run each revision pass sequentially, completing one before starting the next.

### 6. Surface Risks Early
Flag weak logic, redundant chapters, unresolved promises, and pacing holes as soon as they appear. Propose fixes with concrete rewrite options.

### 7. Always End With the Next Smallest Action
After each interaction, leave a precise next step the user can execute immediately, such as chapter brief approval, scene rewrite, or revision pass target.

## Common Traps

- Drafting before scope is defined -> bloated manuscript and major rewrites.
- Treating every chapter the same -> flat pacing and repetitive structure.
- Line editing too early -> local polish over global coherence.
- Changing voice mid-book -> reader trust drops quickly.
- Ignoring chapter outcomes -> chapters feel busy but non-essential.

## Security & Privacy

**Data that stays local:**
- Project memory in `<state_root>/`.
- Chapter and revision notes created during sessions.

**Data that leaves your machine:**
- None by default.

**This skill does NOT:**
- Send manuscript data to external APIs.
- Access files outside `<state_root>/` for memory storage.
- Delete user writing without explicit confirmation.
