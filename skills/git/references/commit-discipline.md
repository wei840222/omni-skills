# Commit Discipline

- One reviewable change per commit; `git add -p` splits mixed work. `git commit --fixup <sha>` + `git rebase -i --autosquash` batches corrections without "fix typo" noise.
- Match the repo's existing message style before imposing one — check `git log --oneline -20`, or follow `commit_style` and `message_language` when the user set them. Conventional commits (`type(scope): description`) only where the log or release tooling already uses them.
- `git pull --rebase --autostash` before push: no surprise merge commits, works with a dirty tree.
- First push: `git push -u origin HEAD`, or set `push.autoSetupRemote` (git >=2.37) once and never type `-u` again.
