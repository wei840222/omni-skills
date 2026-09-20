---
name: coding
description: Manage and apply user-specific coding style preferences, stack decisions,
  and architectural patterns. Trigger when explicitly corrected by the user or when
  generating code that requires style alignment.
metadata:
  openclaw: '{"emoji": "💻", "os": ["linux", "darwin", "win32"], "displayName": "Coding"}'
  related-skills: null
---

## When to load

Load `references/dimensions.md` to review the categories of coding preferences you can track.
Load `references/criteria.md` when deciding whether to add a new preference.
Load `assets/memory-template.md` to view the required format for memory files.

## State location

```text
<workspace>/coding/
<workspace>/memory/coding/
~/coding/
```

- **Lookup order**: Highest precedence first.
- **Creation**: If none exist, `<workspace>/coding/` is created on first write.
- **Storage**: Write state exclusively to external locations, keeping the skill package read-only. All paths below use `<state_root>` to indicate the resolved location.

## Architecture

Memory lives in `<state_root>/` with tiered structure. See `assets/memory-template.md` for setup.

```
<state_root>/
├── memory.md      # Active preferences (≤100 lines)
└── history.md     # Archived old preferences
```

## Data Storage

All data stored in `<state_root>/`. Create on first use:
```bash
mkdir -p <state_root>
```

## Scope

This skill ONLY:
- Learns from explicit user corrections ("I prefer X over Y")
- Stores preferences in local files (`<state_root>/`)
- Applies stored preferences to code output

This skill is RESTRICTED to explicitly requested actions. You must skip:
- Reads project files to infer preferences
- Observes coding patterns without consent
- Makes network requests
- Reads files outside `<state_root>/`
- Modifies its own SKILL.md

## Core Rules

### 1. Learn from Explicit Feedback Only
- User corrects output → ask: "Should I remember this preference?"
- User confirms → add to `<state_root>/memory.md`
- Infer intent only from explicit instruction, ignoring silence or observation

### 2. Confirmation Required
No preference is stored without explicit user confirmation:
- "Actually, I prefer X" → "Should I remember: prefer X?"
- User says yes → store
- User says no → discard the preference and proceed without asking again

### 3. Ultra-Compact Format
Keep each entry 5 words max:
- `python: prefer 3.11+`
- `naming: snake_case for files`
- `tests: colocated, not separate folder`

### 4. Category Organization
Group by type (see `references/dimensions.md`):
- **Stack** — frameworks, databases, tools
- **Style** — naming, formatting, comments
- **Structure** — folders, tests, configs
- **Rejected** — explicitly rejected patterns

### 5. Memory Limits
- memory.md ≤100 lines
- When full → archive old patterns to history.md
- Merge similar entries: "no Prettier" + "no ESLint" → "minimal tooling"

### 6. On Session Start
1. Load `<state_root>/memory.md` if exists
2. Apply stored preferences to responses
3. If no file exists, start with no assumptions

### 7. Query Support
User can ask:
- "Show my coding preferences" → display memory.md
- "Forget X" → remove from memory
- "What do you know about my Python style?" → show relevant entries

## Common Traps

- Adding preferences without confirmation → user loses trust
- Inferring from project structure → privacy violation
- Exceeding 100 lines → context bloat
- Vague entries ("good code") → useless, be specific

## Security & Privacy

**Data that stays local:**
- All preferences stored in `<state_root>/`
- No telemetry or analytics

**This skill does NOT:**
- Send data externally
- Access files outside `<state_root>/`
- Observe without explicit user input
