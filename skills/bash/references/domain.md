# Bash Domain Knowledge

## Quoting

- `"$var"`, `"$(cmd)"`, `"${arr[@]}"` — always. `$(cmd)` strips ALL trailing newlines, not just one.
- Single quotes are literal; `$'...'` interprets escapes: `$'\t'`, `$'\r'`, `$'\0'`.
- Filenames from variables get `--` or `./`: `rm -- "$f"` survives a file named `-rf`.
- `echo "$var"` breaks when var is `-n`, `-e`, or has backslashes — `printf '%s\n' "$var"` functions reliably.
- Arguments to `ssh`/`su -c`/`bash -c` are re-parsed by the receiving shell — build them with `printf '%q '` (`references/quoting.md`).
- `${arr[*]}` joins with the first char of IFS into one word; `"${arr[@]}"` preserves elements. Joining is the only reason to write `[*]`.

## Version Floors

| Feature | Needs |
|---------|-------|
| `printf -v var`, `+=` append | bash >=3.1 |
| `declare -A`, `mapfile`, `${var^^}`/`${var,,}`, `globstar`, `;&` fallthrough, `\|&` | bash >=4.0 |
| `[[ -v var ]]`, `shopt -s lastpipe`, `declare -g` | bash >=4.2 |
| `${arr[-1]}`, `declare -n` namerefs, `wait -n` | bash >=4.3 |
| `inherit_errexit`, `${var@Q}`, `mapfile -d`, empty `"${arr[@]}"` safe under `set -u` | bash >=4.4 |
| `EPOCHSECONDS`/`EPOCHREALTIME`, `SRANDOM` (5.1) | bash >=5.0 |

macOS `/bin/bash` stays at 3.2. `#!/usr/bin/env bash` finds a Homebrew bash on PATH; `#!/bin/bash` will fail to do so. Check at runtime with `BASH_VERSINFO`, not by parsing `bash --version`.

## Exit Codes

Formula: a code above 128 means killed by signal `code − 128`. Codes are mod 256 — `exit 256` reports 0, `exit -1` reports 255.

| Code | Meaning | First move |
|------|---------|-----------|
| 1 | Generic failure — also `(( expr ))` evaluating to 0 | Read the last command, then the `((` traps below |
| 2 | Shell syntax or builtin usage error | `bash -n script` locates it; conventionally also "wrong CLI usage" (`references/arguments.md`) |
| 126 | Found but not executable | `chmod +x`, or the shebang interpreter is not executable |
| 127 | Command not found | PATH (the cron classic), typo, or a missing shebang interpreter ("bad interpreter") |
| 130 | SIGINT (128+2) | User pressed Ctrl-C — propagate it, propagate it |
| 137 | SIGKILL (128+9) | OOM killer or `kill -9`; no trap ever ran, so cleanup did not happen |
| 141 | SIGPIPE (128+13) | A consumer (`head`, `grep -q`) closed the pipe early — usually success misread as failure |
| 143 | SIGTERM (128+15) | Orderly external stop (systemd, CI timeout) — trap it to clean up |
| 124 | GNU `timeout` expired (125 = timeout itself failed) | Raise the timeout or fix the hang (`references/processes.md`) |
| 255 | `ssh` transport error, and any `exit` with a negative or >255 value wrapped | Distinguish ssh's own failure from the remote command's |

## Subshells and State

- Every pipe segment runs in a subshell: `cmd | while read -r x; do ((n++)); done` loses `n`. Fix: `done < <(cmd)`, or `shopt -s lastpipe` (bash >=4.2, scripts only).
- `( )` is a subshell, `{ ...; }` is the current shell — `exit` inside `( )` or `$( )` exits only that subshell.
- Background jobs: `cmd & pid=$!` then `wait "$pid"` — `wait` returns the job's exit code, your only way to check it.
- `cd` inside `( )` to visit a directory without having to `cd` back.

## Robust Iteration

- Globs: `shopt -s nullglob` first — otherwise `for f in *.txt` in an empty dir runs once with the literal string `*.txt`.
- Hostile filenames or recursion: `while IFS= read -r -d '' f; do ...; done < <(find . -name '*.log' -print0)`.
- Lines of a file: `while IFS= read -r line; do ...; done < file` — `IFS=` keeps leading whitespace, `-r` keeps backslashes. A final line without a trailing newline is still skipped: append `|| [[ -n $line ]]` to the read.
- Any command inside the loop that reads stdin (`ssh`, `ffmpeg`, `mysql`) eats the rest of the input and the loop ends after one pass — pass `ssh -n` or redirect `< /dev/null`.
- Split a string: `IFS=, read -ra fields <<< "$csv"`. Join: `(IFS=,; echo "${arr[*]}")` — the subshell keeps the IFS change local.

## Output Gates

Before delivering any script, check:

- Every expansion quoted, or the unquoted one carries a comment saying why
- Commands with variable flags built as arrays, not concatenated strings
- shellcheck clean at `lint_gate`, or each disable names its SC code and reason
- Failure path exercised: injected `false`, watched the trap fire and the exit code go nonzero
- Bash floor stated in a header comment and matching `bash_floor` if any `bash >=4.0` feature is used
- No `eval`; no unvalidated input inside `(( ))` or array subscripts
- Re-runnable: a run that dies halfway leaves nothing half-written — temp file plus `mv`, `mkdir -p`, `rm -f`
- Destructive steps gated per `destructive_confirm`; no secret can appear in `set -x` output or `ps`

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| `local out=$(cmd)` | `local` returns 0, masking cmd's failure — `set -e` remains untriggered | `local out; out=$(cmd)` |
| `((count++))` when count is 0 | expression evaluates to 0 → exit status 1 → `set -e` kills the script | `count=$((count+1))` |
| `grep -q` downstream under pipefail | early exit sends SIGPIPE upstream; producer dies with 141 (128+13) and the pipeline "fails" on success | capture first: `out=$(cmd)`, then grep the variable |
| `rm -rf "$dir/"` | empty/unset `dir` → `rm -rf /` | `rm -rf "${dir:?}/"` aborts if empty |
| `trap "rm -rf $tmp" EXIT` (double quotes) | the body expands NOW, when `tmp` may still be empty — you registered `rm -rf` | single quotes: `trap 'rm -rf "$tmp"' EXIT` |
| Checking `$?` after a log line | the `echo` overwrote it | `rc=$?` on the very next line |
| `which cmd` to test existence | external, output format varies (SC2230) | `command -v cmd >/dev/null` |
| `cd "$dir"` without a check | without `-e`, everything after runs in the wrong directory | `cd "$dir" \|\| exit 1` — habit survives scripts that lack `-e` |
| `sudo cmd > /root/out` | the redirection is performed by YOUR shell before sudo runs — permission denied | `cmd \| sudo tee /root/out >/dev/null` |
| `set -euo pipefail` in a sourced library | it mutates the caller's shell and breaks their error handling | set options in executables only; libraries return codes (`references/functions.md`) |

## Where Experts Disagree

- `set -e`: the strict-mode school makes it mandatory; the Google Shell Style Guide school argues its exceptions (conditions, `||`, command substitution) make it false comfort and prefers explicit `|| die`. Boundary: short glue scripts → strict mode; sourced libraries and functions whose return codes callers inspect → explicit handling. Maintain a single philosophy in one file.
- Bash vs POSIX sh: write sh only when the target set actually contains dash/busybox/alpine. "Portable by default" costs arrays, `[[ ]]`, and `set -o pipefail` for hosts you may never meet.
- Returning values from functions: print to stdout and capture (composable, costs a fork per call) vs write through a nameref or a documented global (no fork, couples caller and callee). Boundary: hot loops and large payloads → nameref (`bash >=4.3`); everything else → stdout.
- Long options: GNU `getopt(1)` parses them but does not exist usably on macOS (BSD getopt has no long options); a hand-rolled `while`/`case` loop is portable and you own the error messages. Boundary: Linux-only tooling → `getopt`; anything shipped to laptops → hand-rolled (`references/arguments.md`).
