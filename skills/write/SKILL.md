---
name: write
description: Plan, draft, revise, and audit written content in a versioned workspace. Use when authoring or editing an article, email, post, report, guide, or other long-form piece that benefits from a brief, tracked revisions, research, or a quality check.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✍️","os":["linux","darwin"]}'
---

## State location

- Resolve `<state_root>` to a user-approved local writing workspace, such as `./workspace`; keep pieces, version snapshots, audits, research, `config.json`, and `index.json` there rather than in the skill package.
- If `<state_root>/index.json` already exists, load the workspace. Otherwise initialize it with `./scripts/init-workspace.sh <state_root>`; the initializer preserves existing `config.json` and `index.json` files.
- Supply the same `<state_root>` to every script. Treat the workspace as the source of truth for drafts and version history.

## Workflow

1. **Plan:** For a piece over 300 words or with multiple arguments, load `references/brief.md` and establish audience, purpose, tone, length, and platform. For a quick reply under 100 words, draft directly.
2. **Initialize or locate:** Resolve `<state_root>` as above. Create it only when absent, then make a piece with `./scripts/new-piece.sh <state_root> <type> "<title>"`.
3. **Research when warranted:** Load `references/research.md` for unfamiliar, thorough, or 1,000+ word work; complete research notes before drafting.
4. **Draft and revise:** Load `references/execution.md`, write the proposed content to a temporary file, and apply it with `./scripts/edit.sh <state_root> <piece-id> <new-content-file>` so each replacement is versioned.
5. **Audit before delivery:** Load `references/audit.md` and `references/verification.md`. Run `./scripts/audit.sh <state_root> <piece-id>` for work over 300 words, important publishing/sending, requested review, or `auto_audit: true`. Address every Must Fix item through another versioned edit; deliver once the audit is at least 8/10 with no blockers.
6. **Recover or clean up:** Load `references/versioning.md` to restore a prior version. When the user confirms the piece is final, use `./scripts/cleanup.sh <state_root> <piece-id> [keep-count]` to retain recent backups.

For writing-process rationale, version-control benefits, and audit principles, load `references/domain_knowledge.md`.

## Configuration

Set these options in `<state_root>/config.json`:
- `depth`: "quick" | "standard" | "thorough" — controls research and revision passes
- `auto_audit`: true/false — run audits automatically after drafts

## Scripts (Enforced)

| Script | Purpose |
|--------|---------|
| `init-workspace.sh` | Create project structure |
| `new-piece.sh` | Start new writing piece with ID |
| `edit.sh` | Edit with automatic version backup |
| `audit.sh` | Run quality audit, generate report |
| `list.sh` | Show all pieces and versions |
| `restore.sh` | Restore previous version |
| `cleanup.sh` | Remove old versions (with confirmation) |

## References

Load these only for the stated branch:
- **Planning:** `references/brief.md` — define the brief and decide whether to outline.
- **Drafting:** `references/execution.md` — prepare a temporary draft and apply it through the versioning script.
- **Quality checks:** `references/verification.md` — perform the final self-check and platform fit check.
- **Tracking:** `references/state.md` — identify pieces, workspace layout, or interruption recovery.
- **Research:** `references/research.md` — gather and record sources for unfamiliar or thorough work.
- **Version rules:** `references/versioning.md` — create, edit, restore, or safely clean up a piece.
- **Audit dimensions:** `references/audit.md` — score a draft and route required revisions.
- **Preferences:** `references/criteria.md` — decide whether a stable user preference belongs below.

---

### Preferences
<!-- User's writing preferences -->

### Never
<!-- Things that don't work for this user -->

---
*Empty sections = observe and fill.*
