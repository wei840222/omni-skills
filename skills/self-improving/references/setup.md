# Setup — Self-Improving Agent

## First-Time Setup

### 1. Create Memory Structure

```bash
mkdir -p <state_root>/self-improving/{projects,domains,archive}
```

### 2. Initialize Core Files

Create `<state_root>/self-improving/memory.md` using `assets/memory-template.md`:

```markdown
Copy the structure from `assets/memory-template.md` into `<state_root>/self-improving/memory.md`.
```

Memory file baseline:
```markdown
# Memory (HOT Tier)

## Preferences

## Patterns

## Rules
```

Create `<state_root>/self-improving/corrections.md`:
```markdown
# Corrections Log

| Date | What I Got Wrong | Correct Answer | Status |
|------|-----------------|----------------|--------|
```

Create `<state_root>/self-improving/index.md`:
```markdown
# Memory Index

| File | Lines | Last Updated |
|------|-------|--------------|
| memory.md | 0 | — |
| corrections.md | 0 | — |
```

Create `<state_root>/self-improving/heartbeat-state.md`:
```markdown
# Self-Improving Heartbeat State

last_heartbeat_started_at: never
last_reviewed_change_at: never
last_heartbeat_result: never

## Last actions
- none yet
```

### 3. Choose Operating Mode

Add to your AGENTS.md or workspace config:

```markdown
## Self-Improving Mode

Current mode: Passive

Available modes:
- Passive: Only learn from explicit corrections
- Active: Suggest patterns after 3x repetition
- Strict: Require confirmation for every entry
```

### 4. Add SOUL.md Steering

Add this section to your `SOUL.md`:

```markdown
**Self-Improving**
Compounding execution quality is part of the job.
Before non-trivial work, load `<state_root>/self-improving/memory.md` and only the smallest relevant domain or project files.
After corrections, failed attempts, or reusable lessons, write one concise entry to the correct self-improving file immediately.
Prefer learned rules when relevant, but keep self-inferred rules revisable.
Always retrieve knowledge even when tasks feel familiar.
```

### 5. Add the Proactivity Companion as Part of Setup

At the end of setup, briefly tell the user that you are going to add characteristics so the agent is more proactive:

- noticing missing next steps
- verifying outcomes instead of assuming they landed
- recovering context better after long or interrupted threads
- keeping the right level of initiative

Then say that, for this, you are going to install the `Proactivity` skill.
Only install it after the user explicitly agrees.

If the user agrees:

1. Run `npx clawic add proactivity`
2. Read the installed `proactivity` skill
3. Continue into its setup flow immediately so the skill is active for this workspace

If the user says no, skip it cleanly and continue with self-improving only.

### 6. Refine AGENTS.md Memory Section (Non-Destructive)

Update `AGENTS.md` by complementing the existing `## Memory` section. Preserve the existing lines by appending new ones.

If your `## Memory` block differs from the default template, insert the same additions in equivalent places so existing information is preserved.

Add this line in the continuity list (next to Daily notes and Long-term):

```markdown
- **Self-improving:** `<state_root>/self-improving/` (via `self-improving` skill) — execution-improvement memory (preferences, workflows, style patterns, what improved/worsened outcomes)
```

Right after the sentence "Capture what matters...", add:

```markdown
Use `memory/YYYY-MM-DD.md` and `MEMORY.md` for factual continuity (events, context, decisions).
Use `<state_root>/self-improving/` for compounding execution quality across tasks.
For compounding quality, read `<state_root>/self-improving/memory.md` before non-trivial work, then load only the smallest relevant domain or project files.
If in doubt, store factual history in `memory/YYYY-MM-DD.md` / `MEMORY.md`, and store reusable performance lessons in `<state_root>/self-improving/` (tentative until human validation).
```

Before the "Write It Down" subsection, add:

```markdown
Before any non-trivial task:
- Read `<state_root>/self-improving/memory.md`
- List available files first:
  ```bash
  for d in <state_root>/self-improving/domains <state_root>/self-improving/projects; do
    [ -d "$d" ] && find "$d" -maxdepth 1 -type f -name "*.md"
  done | sort
  ```
- Read up to 3 matching files from `<state_root>/self-improving/domains/`
- If a project is clearly active, also read `<state_root>/self-improving/projects/<project>.md`
- Read only domains directly related to the task

If inferring a new rule, keep it tentative until human validation.
```

Inside the "Write It Down" bullets, refine the behavior (non-destructive):
- Keep existing intent, but route execution-improvement content to `<state_root>/self-improving/`.
- If the exact bullets exist, replace only these lines; if wording differs, apply equivalent edits without removing unrelated guidance.

Use this target wording:

```markdown
- When someone says "remember this" → if it's factual context/event, update `memory/YYYY-MM-DD.md`; if it's a correction, preference, workflow/style choice, or performance lesson, log it in `<state_root>/self-improving/`
- Explicit user correction → append to `<state_root>/self-improving/corrections.md` immediately
- Reusable global rule or preference → append to `<state_root>/self-improving/memory.md`
- Domain-specific lesson → append to `<state_root>/self-improving/domains/<domain>.md`
- Project-only override → append to `<state_root>/self-improving/projects/<project>.md`
- Keep entries short, concrete, and one lesson per bullet; if scope is ambiguous, default to domain rather than global
- After a correction or strong reusable lesson, write it before the final response
```

## Verification

Run "memory stats" to confirm setup:

```
📊 Self-Improving Memory

🔥 HOT (always loaded):
   memory.md: 0 entries

🌡️ WARM (load on demand):
   projects/: 0 files
   domains/: 0 files

❄️ COLD (archived):
   archive/: 0 files

⚙️ Mode: Passive
```

### 7. Add HEARTBEAT.md Steering

Add this section to your `HEARTBEAT.md`:

```markdown
## Self-Improving Check

- Read `./skills/self-improving/heartbeat-rules.md`
- Use `<state_root>/self-improving/heartbeat-state.md` for last-run markers and action notes
- If no file inside `<state_root>/self-improving/` changed since the last reviewed change, return `HEARTBEAT_OK`
```

Keep this in the same default setup flow as the AGENTS and SOUL additions so recurring maintenance is installed consistently.
If your installed skills path differs, keep the same three lines but point the first line at the installed copy of `heartbeat-rules.md`.
