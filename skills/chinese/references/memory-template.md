# Memory Template — State Storage Reference

Use this reference only after the user explicitly asks to save a Chinese-language preference. State lives under `<state_root>/`; do not write outside that resolved directory.

---

## File Layout

```
<state_root>/
├── config.yaml       ← user-declared defaults
└── memory.md         ← approved, durable language decisions
```

## memory.md Structure

```markdown
# Chinese preferences

## Decisions

| scope | decision | evidence | recorded |
|-------|----------|----------|----------|
| Taiwan product page | Use 軟體, 檔案, 影片 | User-approved publication style | 2026-08-08 |

## Recipients

| key | address_form | register | evidence |
|-----|--------------|----------|----------|
| recipient-1 | 您 | 正式 | User confirmed this preference |
```

---

## What to save

- A user-approved default belongs in `<state_root>/config.yaml`.
- A durable term, variant, register, or recipient-address decision belongs in `<state_root>/memory.md`.
- Record the decision, its scope, and user-provided evidence. Use a stable pseudonymous key when a recipient must be distinguished; omit names and contact details.
- Keep drafts, project records, conversations, accounts, credentials, and third-party data in their owning system rather than this skill's state.

---

## Write boundary

Before writing, name the exact file and the preference being saved. Keep the edit limited to `<state_root>/config.yaml` or `<state_root>/memory.md`; all package resources remain read-only. If the user has not asked to save a preference, finish the writing task without creating state.
