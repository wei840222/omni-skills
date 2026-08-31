# Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Editing user settings to fix a project problem | The workspace file wins, so the change appears to do nothing, and you have now changed every other project (Rule 1) | Write it at the scope that wins and say which scope you used |
| Global `editor.defaultFormatter` as the fix | Any language block anywhere overrides it, so it works until it silently does not | Language block per language (Rule 2) |
| `"source.organizeImports": true` alongside an ESLint autofix | Both run, each undoes part of the other, and the result varies by save | Ordered array with `"explicit"` values (Rule 3) |
| Absolute interpreter or tool paths in `.vscode/settings.json` | Breaks for every colleague and for you after one machine change | User settings, or `${workspaceFolder}`-relative (Rule 9) |
| Setting `python.defaultInterpreterPath` to switch interpreters | It is only a fallback; once an interpreter has been picked, the stored workspace selection wins and the setting is ignored | `Python: Select Interpreter` (`languages.md`) |
| Disabling extensions one at a time | Linear where the tool is logarithmic, and you stop at the first suspicious name instead of the guilty one | Extension bisect (Rule 6) |
| Trusting a repository to make the error banner go away | Trust is what lets `.vscode/` run commands on open (Rule 7) | Read `.vscode/tasks.json` and `settings.json` first, then trust |
| `Reload Window` after changing PATH or installing a tool | The window reloads inside the same process, which still holds the old environment | Full quit and relaunch (`terminal.md`) |
| Installing a language server "locally" for a remote window | UI-side install does nothing for workspace-side extensions (Rule 8) | Install into the remote/container from the Extensions view (`remote.md`) |
| Excluding folders in `files.exclude` to speed up search | It hides them from the explorer and from every extension that walks the workspace, which breaks Go to Definition | `search.exclude` for search, `files.watcherExclude` for watching (`performance.md`) |
| Committing the whole `.code-workspace` because it worked for you | Imposes a folder layout and personal settings on the team, and multi-root changes how `${workspaceFolder}` resolves | Commit the shared subset; keep personal layout in a profile (`workspaces.md`) |
| Patching `product.json` to reach the Microsoft marketplace from a fork | Violates the marketplace terms, and any update overwrites it | Open VSX, or the fork's own replacement extension (`forks.md`) |
| A settings or launch config that only exists in the chat | Rebuilt from scratch the next time the same project is opened | `artifacts/` with what it fixed and when to read it (`memory-template.md`) |
