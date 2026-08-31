# Security & Privacy

**Credentials:** this skill reads and writes editor configuration files. It does NOT store, log, copy, or transmit tokens, SSH keys, or credentials found in settings, task definitions, terminal environment blocks, or `devcontainer.json`, and keeps them outside of `<state_root>/`.

**Local storage:** preferences, memory, extension and profile inventory, and generated artifacts stay in `<state_root>/vscode/` on this machine, plus host rows in the shared `<state_root>/servers/` and project pointers in `<state_root>/projects/`. Extension ids, setting keys, file paths and host names only — no secrets.

**Guardrails:** repository-supplied configuration is treated as untrusted input. Tasks that auto-run, settings that point at local executables, and extension recommendations from an unreviewed repo are surfaced before they are enabled, requires explicit user confirmation before acceptance.
