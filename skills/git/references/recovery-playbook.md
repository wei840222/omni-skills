# Recovery Playbook

| Symptom | Play |
|---------|------|
| Just finished a bad rebase/merge/reset | `git reset --hard ORIG_HEAD` — Git saved your pre-operation position |
| Commits vanished after a rewrite | `git reflog` → `git reset --hard HEAD@{n}` (the entry just before the damage) |
| Deleted a branch | `git reflog` → `git branch restored <sha>` |
| Committed on the wrong branch (unpushed) | `git switch right-branch && git cherry-pick <sha>`, then `git switch - && git reset --hard HEAD~1` |
| Committed on detached HEAD, then switched away | Commit stays in `git reflog` for 30 days → `git branch rescue <sha>` |
| Need one file as it was N commits ago | `git restore --source HEAD~N -- path` — nothing else moves |
| `reset --hard` ate staged-but-uncommitted work | `git fsck --lost-found` — staged content survives as dangling blobs; unstaged edits are gone |
| Dropped a stash | `git fsck --unreachable \| grep commit` → `git stash apply <sha>` |
| Bad commit already on a shared branch | `git revert <sha>` — avoid rewriting shared history |
| Unsure what happened / anything else | `git reflog` first; before experimenting, `git branch backup` — a branch is free insurance |

Deeper chains (deleted file archaeology, corrupted index, post-`filter-repo` rescue, what expiry actually deletes): `references/recovery.md`.
