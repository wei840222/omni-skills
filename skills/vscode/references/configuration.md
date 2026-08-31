# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/vscode/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| vscode_build | code \| code-insiders \| vscodium \| cursor \| windsurf \| code-server | code | Which marketplace, which license-gated extensions exist, and which settings are fork-specific (`forks.md`) |
| os_family | macos \| linux \| windows \| wsl \| none | none | Modifier keys, config-directory paths, and shell defaults. While `none`, give shortcuts in both `Cmd` and `Ctrl` form instead of asking (`keybindings.md`) |
| remote_mode | local \| ssh \| devcontainer \| wsl \| tunnel \| codespaces | local | Which side an extension is installed on, where settings live, and which paths the debugger must map (`remote.md`, Rule 8) |
| settings_scope_default | user \| workspace \| folder \| profile | workspace | Where a proposed setting gets written when the user does not say (Rule 1) |
| vscode_dir_policy | commit-shared \| commit-all \| gitignore | commit-shared | Which of the four `.vscode/` files generated configs are written into, and what the `.gitignore` advice is (Rule 9) |
| extension_marketplace | microsoft \| openvsx | microsoft | Install source, extension ids used in recommendations, and whether first-party extensions are reachable (`forks.md`) |
| formatter_stack | prettier \| eslint \| biome \| language-native | prettier | Which formatter is wired as `defaultFormatter` and which save actions are generated (`formatting.md`, Rule 2) |
| trust_posture | restricted-default \| trust-on-open | restricted-default | Whether generated tasks may auto-run, and how aggressively `security.md` flags an unreviewed repo (Rule 7) |
| config_output | diff \| full-file | diff | Whether answers emit only the keys to add or the complete file |
| banned_extensions | list (extension ids) | empty | Never recommended, never installed, and flagged if already present (`extensions.md`) |
| startup_budget_ms | number (ms, 500-10000) | 2000 | The window-load time above which `performance.md` treats startup as a problem worth profiling |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — profiles vs one settings file, Settings Sync on or off, the Insiders channel, GUI vs `code` CLI, which test and Git extensions are canonical — affects `settings.md` and `extensions.md`
- **Conventions** — indentation and EOL policy, `.editorconfig` as the source of truth, file nesting and explorer layout, naming for launch and task labels, per-language formatter map — affects generated `.vscode/` files
- **Language stack** — which languages get first-class setup, the linter and type-checker per language, the test framework — affects `languages.md`, `formatting.md`, `testing.md`
- **Platform** — keyboard layout and any remapped modifiers, terminal shell, monorepo layout, huge-repo exclusions — affects `keybindings.md`, `terminal.md`, `performance.md`
- **Safety posture** — trust defaults, whether to install extensions unprompted, appetite for auto-run tasks and auto-fetch, telemetry level — affects Output Gates and `security.md`
- **Output register** — diff vs whole file, JSON with comments or without, how much reasoning to keep alongside a config — affects every answer's shape
- **Cadence** — extension audit, remote-server cleanup, profile export, keybinding review — every accepted cadence becomes a row in the `## Due` table of `memory.md`
