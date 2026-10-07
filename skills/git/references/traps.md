# Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| `git stash` before a risky operation, expecting untracked files saved | Plain stash skips untracked files | `git stash -u` |
| Assuming `stash pop` dropped the stash after a conflict | Pop only drops on clean apply; on conflict the entry stays | Resolve, then `git stash drop` |
| `git clean -fdx` to "clean build artifacts" | `-x` also deletes ignored files: `.env`, IDE config, local secrets | `git clean -fd`, always preview with `-n` |
| Renaming `Foo.js` → `foo.js` works locally, breaks CI | macOS/Windows filesystems are case-insensitive, Linux is not | `git mv Foo.js tmp && git mv tmp foo.js` |
| `git branch -d` refuses to delete after squash-merge | Squashed commits are unreachable from main, so Git thinks the branch is unmerged | Verify the PR merged, then `-D` |
| Committing a large binary "just this once" | GitHub warns >50 MB, blocks >100 MB — and history keeps the blob forever | Git LFS before first commit; after the fact, `git filter-repo` (`references/secrets.md`) |
| "Sharing" hooks via `.git/hooks` | `.git/hooks` is never versioned | Commit a hooks dir + `git config core.hooksPath` (`references/hooks.md`) |
| Cloned repo has empty submodule directories | Submodules need explicit initialization | `git clone --recurse-submodules`, or `git submodule update --init` |
| Adding a path to `.gitignore` to stop tracking it | Ignore rules do not apply to already-tracked files — the file keeps showing up in every diff | `git rm --cached <path>`, commit the removal, then ignore it |
| `git reset --hard` when the intent was "unstage this" | `--hard` also throws away the working tree; unstaging needs no destructive flag | `git restore --staged <path>` (index only) |
| Marking a config file `--assume-unchanged` so local edits stop appearing | Git now lies in `status`, and any incoming change to that file breaks pull with a confusing error | Commit a `.example` template, gitignore the real file (`references/config.md`) |
