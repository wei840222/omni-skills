---
name: bash
description: >
  Write, debug, and harden Bash shell scripts — quoting, arrays, strict mode,
  traps, argument parsing, and macOS/Linux portability. Use when writing or
  reviewing any script, one-liner, cron job, deploy script, container entrypoint,
  or CI step; when a script breaks on spaces in filenames, exits silently, ignores
  set -e, hangs, or returns the wrong exit code; when quoting, IFS, globs, arrays,
  heredocs, process substitution, trap, getopts, or mapfile misbehave; when shellcheck
  flags SC2086 and friends; when unbound variable, bad substitution, command not found,
  ambiguous redirect, or unexpected end of file show up; when a script works by hand
  but fails under cron, systemd, sudo, or a CI runner; or when porting between macOS
  bash 3.2, GNU/Linux, WSL, and POSIX sh. Not for interactive zsh or fish configuration,
  not for PowerShell, and not for host-level cron, systemd, or permission failures
  (`linux`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🖥️","requires":{"bins":["bash"]}}'
  related-skills: '{"linux":"Host permissions, systemd, cron installation, and OS-level failures outside the script text.","docker":"Container entrypoints and image shells that still need Bash quoting and PID 1 hygiene.","devops":"CI/CD orchestration around scripts this skill authors or reviews.","server":"Server administration for the machine where scripts run unattended."}'
---

# Bash

Write and harden **Bash scripts** with concrete quoting, exit-code, portability,
and recovery rules. Prefer the smallest change that names the failing subsystem:
expansion, pipeline, trap, PATH, or version floor.

## State location

Optional Bash preferences may exist in `<workspace>/bash/`,
`<workspace>/memory/bash/`, or `~/bash/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bash/`, `<workspace>/memory/bash/`, `~/bash/`.
3. If none exists and durable preferences must be created, default to
   `<workspace>/bash/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/bash/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Preferences live in `<state_root>/config.yaml` when the user wants
defaults kept across sessions (see `references/state.md`). This skill is
primarily routing knowledge; durable notes are optional. Do not invent a script
inventory unless the user asks to keep state.

**Legacy paths.** Historical notes under `~/Clawic/data/bash/`, `~/clawic/bash/`,
or other non-candidate roots are **not** in active lookup order and must **not**
be moved, merged, or deleted during ordinary sessions. Migration is a separate
user decision.

## When to load

- Writing or reviewing any Bash beyond a one-liner: CI steps, deploy scripts, cron tasks, entrypoints, glue code
- Debugging scripts that break on spaces in filenames, fail silently, hang, or exit with the wrong code
- Hardening an existing script: strict mode, cleanup traps, argument parsing, re-runnability, portability
- Porting a script between macOS and Linux, or down to POSIX sh
- Deciding whether the task belongs in Bash at all (Core Rule 9)
- Not for POSIX-sh-only targets (dash, busybox, alpine `/bin/sh`) — most patterns here are bashisms; `references/portability.md` covers the downgrade

## Routing

Load supporting resources only on demand:

| Need | File |
| --- | --- |
| Domain traps, version floors, exit codes | `references/domain.md` |
| Preference variables and defaults | `references/state.md` |
| Quoting and hostile filenames | `references/quoting.md` |
| `set -e` holes and cleanup traps | `references/errors.md` |
| `bash -x` symptom chains | `references/debugging.md` |
| `[` vs `[[` and arithmetic tests | `references/conditionals.md` |
| Cron PATH / `%` / timers | `references/cron.md` |
| CI runners and secret hygiene | `references/ci.md` |
| Fork cost and batching | `references/performance.md` |
| macOS 3.2 vs GNU/BSD flags | `references/portability.md` |
| `getopts` and usage exits | `references/arguments.md` |
| Redirection, heredocs, locking | `references/redirection.md` |
| Paths, globs, temp files | `references/files.md` |
| awk/sed/jq text jobs | `references/text-processing.md` |
| Jobs, signals, timeouts | `references/processes.md` |
| Expansions and string surgery | `references/expansion.md` |
| Arrays and maps | `references/arrays.md` |
| Functions and libraries | `references/functions.md` |
| TTY prompts and color | `references/interactive.md` |
| curl HTTP status handling | `references/http.md` |
| Untrusted input and secrets | `references/security.md` |
| shellcheck / bats gates | `references/testing.md` |
| Gate 6 research URLs | `references/sources.md` |

## Quick Reference

| Situation | Play |
|-----------|------|
| Breaks on spaces or hostile filenames | Quote every expansion, iterate with `find -print0` + `while IFS= read -r -d ''` → `references/quoting.md` |
| `set -e` missed a failure, cleanup failed to run | The five blind spots (conditions, `\|\|`/`&&`, `$( )`, `! cmd`, `exit` in a subshell) → `references/errors.md` |
| Pipeline "fails" but each command worked | Exit code 141 = SIGPIPE from an early-exit consumer; `PIPESTATUS` names the segment → `references/errors.md` |
| Wrong output and you cannot see why | `PS4='+ ${BASH_SOURCE##*/}:${LINENO}: ' bash -x script` → `references/debugging.md` |
| Command built from variables misfires | Build it as an array (`cmd=(rsync -a); cmd+=(--dry-run); "${cmd[@]}"`), avoid strings for lists → `references/quoting.md` |
| Comparison wrong: `[` vs `[[`, numeric vs lexical | `[[ 10 < 9 ]]` is TRUE (lexical); numbers belong in `(( ))` or `-lt` → `references/conditionals.md` |
| Runs fine by hand, fails from cron | Cron has no login shell: minimal PATH, no profile, `$HOME` as cwd, `%` means newline → `references/cron.md` |
| Works locally, fails in the CI runner | Each step is a fresh non-interactive shell; strict mode does not carry over → `references/ci.md` |
| Script takes minutes on a large file | Count forks: one external command per line is the cost — batch into awk/sort → `references/performance.md` |
| `unbound variable` / `bad substitution` / `ambiguous redirect` | Symptom→cause chains → `references/debugging.md` |
| Must run on macOS stock bash or an old server | Version Floors below, then GNU-vs-BSD flags → `references/portability.md` |
| Flags, `--help`, subcommands, usage exit codes | `getopts` with a silent optstring, then `shift $((OPTIND-1))` → `references/arguments.md` |
| Redirection order, heredocs, one-instance locking | Redirections apply left to right before the command runs → `references/redirection.md` |
| Paths, globs, temp files, deletes that must be safe | Resolve once with `cd … && pwd -P`; write temp + `mv` → `references/files.md` |
| Parsing CSV/JSON/logs, choosing awk vs sed vs jq | Per-line and stateless → one `awk` pass; use jq for JSON instead of grep → `references/text-processing.md` |
| Background jobs, signals, timeouts, N in parallel | `pid=$!` then `wait "$pid"`; `xargs -P` for fan-out → `references/processes.md` |
| String surgery: defaults, trim, replace, basename | Builtin expansions, no forks → `references/expansion.md` |
| Lists, dictionaries, sets, counters | `mapfile -t` to load, `declare -A` for maps → `references/arrays.md` |
| Splitting into functions or a sourced library | `main "$@"` behind a `BASH_SOURCE` guard; scope is dynamic → `references/functions.md` |
| Prompts, confirmations, color, progress | Gate every one of them on `[[ -t 1 ]]` → `references/interactive.md` |
| Calling an API, webhook, or health check | curl exits 0 on a 500 — capture `%{http_code}` and branch → `references/http.md` |
| Untrusted input, secrets, temp-file races, sudo | Keep values as data, always as data → `references/security.md` |
| Adding tests, stubbing commands, lint in CI | `bash -n`, shellcheck, then bats with PATH stubs → `references/testing.md` |
| Anything else | Core Rules below, then reproduce with `bash -x` on the smallest input that still fails |

## Core Rules

1. Open every script with `#!/usr/bin/env bash` and `set -euo pipefail`, then learn the `-e` holes (`references/errors.md`) instead of dropping strict mode — the holes are enumerable; silent failures are not.
2. Quote every expansion: `"$var"`, `"$(cmd)"`, `"${arr[@]}"`. An unquoted expansion is a deliberate act that carries a comment saying why. Word splitting plus globbing is Bash's #1 bug class (shellcheck SC2086).
3. Build commands as arrays, not as strings. `opts="--exclude '*.log'"; rsync $opts src dst` passes the quotes as literal characters; `opts=(--exclude '*.log'); rsync "${opts[@]}" src dst` passes `--exclude` and `*.log` as two clean arguments. Conditional flags append: `[[ $dry == 1 ]] && opts+=(--dry-run)`.
4. Run shellcheck before shipping, blocking at `lint_gate` severity. Suppress only with the code and a reason on the same line: `# shellcheck disable=SC2086 -- flags must split`.
5. Know your floor: macOS `/bin/bash` is 3.2 forever (GPLv3 freeze). If the script uses any `bash >=4.0` feature (Version Floors), state the floor in a header comment and enforce it: `((BASH_VERSINFO[0] >= 4)) || { echo "needs bash 4+" >&2; exit 1; }`.
6. Prefer globs or `find -print0` over parsing `ls`: filenames may contain newlines, so NUL is the only delimiter a filename cannot contain.
7. Test the failure path before delivering: swap one command for `false`, confirm the script stops, the trap fires, and the exit code is nonzero. A cleanup you have untested is a cleanup you do not have.
8. Untrusted input must be blocked from reaching `eval`, arithmetic, or array subscripts: `(( $userinput ))` executes commands via `arr[$(cmd)]` subscripts. Gate with a regex first: `[[ $n =~ ^[0-9]+$ ]] || die "not a number: $n"`.
9. Past `rewrite_threshold` lines (default 100, the Google Shell Style Guide cutoff) or once you need nested data structures, rewrite in Python or similar. Bash orchestrates processes; it does not model data.

## Script Skeleton

```bash
#!/usr/bin/env bash
# Requires bash >= 4.4 (inherit_errexit). Run: script.sh [-n] <target>
set -euo pipefail
shopt -s inherit_errexit 2>/dev/null || true   # bash >=4.4: $(cmd) failures propagate

die() { printf '%s\n' "$*" >&2; exit 1; }

tmp=$(mktemp) || die "mktemp failed"
trap 'rm -f "$tmp"' EXIT   # single-quoted: expands when it FIRES, not now
                           # fires on error and normal exit; kill -9 bypasses all traps
```

## Detailed References

- Read `references/domain.md` for Variables and Expansions, Quoting, Version Floors, Exit Codes, Subshells, Robust Iteration, Traps, and Where Experts Disagree.
- Read `references/state.md` for Configuration variables and user preferences.
