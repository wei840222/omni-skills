# Versioning Reference

## Golden Rule
Use `scripts/edit.sh <state_root> <piece-id> <new-content-file>` for every workspace-content revision so the prior content is retained.

The script enforces:
1. Copy current content to versions/ with timestamp
2. Then apply the edit
3. Update metadata

## Why This Matters
- User can ALWAYS go back
- No work is ever lost
- Full history of changes

## Version Naming
```
versions/{piece-id}/
  v1_20260211-143052.md
  v2_20260211-151023.md
  v3_20260211-163045.md
  pre-restore_20260211-170000.md  # auto-created on restore
```

## Workflow

1. **Create piece**
   ```bash
   ./scripts/new-piece.sh <state_root> article "My Article Title"
   ```

2. **Write draft** to temp file
   ```bash
   # Agent writes to /tmp/draft.md
   ```

3. **Apply edit** (versions automatically)
   ```bash
   ./scripts/edit.sh <state_root> article-20260211-143052 /tmp/draft.md
   ```

4. **Revise** (repeat step 2-3)

5. **Restore if needed**
   ```bash
   ./scripts/restore.sh <state_root> article-20260211-143052 v2
   ```

6. **Cleanup when done** (optional, with confirmation)
   ```bash
   ./scripts/cleanup.sh <state_root> article-20260211-143052 3  # keep last 3
   ```

## Never Do
- `echo "..." > pieces/xxx/content.md` — bypasses versioning
- Edit content.md with any tool directly
- Delete version files manually
