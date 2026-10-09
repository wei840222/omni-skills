# Bash research sources (Gate 6)

Verified 2026-10-09 against public documentation. Prefer these over memory for version floors and style cutoffs.

## Official / primary

- **GNU Bash manual** — expansions, `set -e` behavior, job control, exit status — https://www.gnu.org/software/bash/manual/
- **Bash man page (Debian)** — portable summary of builtins and options — https://manpages.debian.org/bookworm/bash/bash.1.en.html
- **POSIX shell command language** — when downgrading to `sh` — https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html

## Style and lint

- **Google Shell Style Guide** — ~100-line rewrite threshold and readability norms — https://google.github.io/styleguide/shellguide.html
- **ShellCheck wiki** — SC2086 and related quoting diagnostics — https://www.shellcheck.net/wiki/

## Platform notes

- **Apple platform bash** — system `/bin/bash` remains 3.2-era on macOS; use `#!/usr/bin/env bash` when a newer bash is installed — confirm on target with `BASH_VERSINFO` rather than parsing `--version`.
