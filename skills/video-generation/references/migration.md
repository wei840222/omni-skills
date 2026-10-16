# Migration Guide - AI Video Generation

Read this guide when upgrading from older published versions or Clawic-era memory paths.

## Breaking Changes in v1.0.2

### 1) Portable `<state_root>` replaces hard-coded Clawic paths

**Before:** `~/Clawic/data/video-generation/memory.md` was the default pattern

**Now:** resolve `<state_root>` once per invocation (`<workspace>/video-generation/`, `<workspace>/memory/video-generation/`, or `~/video-generation/`), then use `<state_root>/memory.md`

**Migration steps:**

1. Resolve `<state_root>` using `SKILL.md` State location rules.
2. If legacy memory exists, create a backup and copy only after confirmation:
   ```bash
   cp ~/Clawic/data/video-generation/memory.md <state_root>/memory.md.bak 2>/dev/null || true
   cp ~/Clawic/data/video-generation/memory.md <state_root>/memory.md
   ```
3. Add missing sections from `../assets/data-templates.md`.
4. Keep the legacy file until the user confirms cleanup.

### 2) Provider routing shifted to current model stacks

**Before:** older references (for example early Kling, SVD-only fallback)

**Now:** prioritized routing includes Sora 2, Veo 3.x, Runway Gen-4, Seedance, Vidu, and Hailuo paths

**Migration steps:**

1. Map old provider notes into the current files listed in Quick Reference.
2. Keep old prompts as baseline, then rerun with current model IDs from `sources.md`.
3. Preserve previous output archives for side-by-side quality checks.

### 3) API guidance now assumes async-first execution

**Before:** polling/retry logic was partial

**Now:** `api-patterns.md` defines unified async handling, backoff, URL expiry, and fallback rules

**Migration steps:**

1. Add idempotency keys for create requests where supported.
2. Standardize status polling and timeout handling.
3. Download outputs immediately after completion.

## Post-Migration Verification

- [ ] `<state_root>/memory.md` exists and keeps prior preferences
- [ ] Legacy provider notes map to current provider files
- [ ] Async job handling is implemented consistently
- [ ] User assets stay intact until explicit confirmation

## Cleanup Policy

- Preserve backups until the user confirms removal.
- Prefer copy-first migration, then optional cleanup.
