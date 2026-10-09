# Bash State Configuration

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/bash/config.yaml`. Record a preference automatically — record a preference the moment it is stated.

| Variable | Type | Default | Effect |
|---|---|---|---|
| bash_floor | 3.2 \| 4.4 \| 5.x | 4.4 | Gates which Version Floors features may be used unguarded; `3.2` bans `mapfile`, `declare -A`, namerefs and emits the portable fallbacks instead |
| target_os | linux \| macos \| both | both | Picks GNU or BSD flag forms in every emitted command (`sed -i`, `date`, `stat`, `readlink`); `both` restricts to the intersection (`references/portability.md`) |
| strict_mode | set-euo \| explicit-checks | set-euo | Chooses the Script Skeleton and which school reviews enforce (Where Experts Disagree) |
| lint_gate | error \| warning \| style \| none | warning | Severity at or above which shellcheck findings block delivery (`shellcheck -S <value>`); Output Gates use it |
| rewrite_threshold | number (lines) | 100 | Length at which Core Rule 9 recommends another language |
| indent_style | 2-spaces \| 4-spaces \| tabs | 2-spaces | Formatting of emitted scripts and the `shfmt -i` value |
| destructive_confirm | bool | true | Emitted scripts guard deletes, overwrites, and remote pushes behind `--yes` or a dry-run pass |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Tooling**: shellcheck/shfmt/bats availability, GNU coreutils on macOS (`gsed`, `gdate`), jq vs python for JSON — affects `testing.md` gates and every parsing example
- **Conventions**: function and variable naming, usage/help layout, log line format, script header content — affects `functions.md` and `arguments.md` output
- **Platform**: bash floor and OS mix, POSIX-sh-only targets, alpine images where `/bin/sh` is ash and bash may be absent — affects `portability.md` guidance
- **Safety posture**: whether scripts may `sudo`, dry-run first, banned constructs (`eval`, `curl | sh`, `rm -rf` on a variable) — affects `security.md` and destructive workflows
- **Runtime home**: where the script actually runs unattended — cron, systemd timer, launchd, CI runner, container entrypoint — affects `cron.md` and `ci.md` advice
- **Output**: verbosity, color only when the output is a TTY, timestamps, quiet or machine-readable logging — affects `interactive.md` and logging helpers
