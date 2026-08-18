# Execution Reference

## Core Rules
- Keep the primary conversation available by delegating substantial drafting work when delegation is available.
- Apply each workspace-content change with `scripts/edit.sh <state_root> <piece-id> <new-content-file>` so it receives a version snapshot.
- Complete the agreed draft without an unnecessary continuation check.

## Draft Workflow

1. **Sub-agent receives task:**
   - Piece ID
   - Brief (audience, tone, length)
   - Research notes (if any)

2. **Sub-agent writes to temp file:**
   ```bash
   # Write draft to /tmp/{piece-id}-draft.md
   ```

3. **Sub-agent calls edit script:**
   ```bash
   ./scripts/edit.sh <state_root> <piece-id> /tmp/<piece-id>-draft.md
   ```

4. **Sub-agent reports completion**

## Anti-Patterns

- Writing directly to content.md (bypasses versioning)
- Stopping after intro to ask "want more?"
- Starting with "Great question!"
- Using AI smell words: delve, leverage, utilize, foster

## AI Smell Words — Avoid

```
delve, leverage, utilize, facilitate, foster,
ensure, seamless, robust, innovative, cutting-edge,
it's important to note, one might argue
```

## Length Defaults

| Type | Default |
|------|---------|
| Tweet | < 280 chars |
| Email | < 150 words |
| Article section | 100-200 words |
| Full article | Per brief |
| Book chapter | 2000-5000 words |

## For Long Pieces

1. Create outline first
2. Write section by section
3. Each section = sub-agent task
4. Compile sections
5. Audit full piece
6. Revise as needed
