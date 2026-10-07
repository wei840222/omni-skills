# Python Core Rules and Constraints

## Core Rules

Do this first; the traps table below is the failure mode mirror.

1. No mutable defaults: `def f(xs=None)` then `if xs is None: xs = []`. Replace `xs = xs or []` — a caller passing an empty list to be filled gets a fresh list instead; their reference stays empty.
2. `is` only for `None`, `True`, `False`, and sentinel objects; `==` for everything else. Interning makes `is` on ints and strings pass in tests and fail in production (`references/types.md`).
3. Iterate copies instead of mutating the collection you iterate — dicts raise `RuntimeError`, lists silently skip elements. Iterate a copy (`for x in list(xs)`) or collect changes and apply after.
4. Match concurrency to workload: pure-Python CPU → `multiprocessing`; I/O → threads or asyncio; threads fail to speed up pure-Python CPU work, because the GIL serializes bytecode (`references/concurrency.md`).
5. `except Exception:`, skipping bare `except:` — bare also catches `KeyboardInterrupt` and `SystemExit`, making the process unkillable. Re-raise with bare `raise`, keeping the original traceback (`references/errors.md`).
6. Files, locks, sockets, connections: always `with`. CPython's refcounting closes leaked handles by accident; exceptions and other interpreters (PyPy) expose the leak.
7. Money and exact decimals: `decimal.Decimal('1.10')` from strings — `Decimal(1.1)` imports the float error it was meant to avoid. Float comparisons via `math.isclose` (`references/types.md`).
8. Declare `encoding='utf-8'` at every I/O boundary — the default follows the platform locale until UTF-8 becomes the default (PEP 686, `python >=3.15`), so the code breaks first on Windows and in lean containers (`references/files.md`).
9. Guard entry points with `if __name__ == "__main__":` — top-level code runs on every import and again in every `multiprocessing` spawn child (`references/imports.md`).

## Output Gates

Before delivering Python code, check:

- No mutable default argument, and no `xs or []` where an empty argument is meaningful
- Every text `open`, `subprocess`, and decode boundary declares `encoding="utf-8"`; every file, lock, socket, and connection is acquired in a `with`
- Every network, subprocess, lock, and queue call has a timeout
- Exceptions: narrowest class caught, chained with `from`, nothing swallowed without a log line or a written reason
- Logging through a module logger with lazy `%s` arguments and no secrets
- Syntax and stdlib stay within `min_python`; annotations match `type_strictness`
- Nothing user-supplied reaches `eval`, `pickle`, a shell string, an SQL string, or a path join without containment
- The new test was seen failing without the fix in place — `change_workflow` decides when that run happens, rather than whether it happened

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`. Accept user preferences directly — record a preference the moment it is stated.

| Variable | Type | Default | Effect |
|---|---|---|---|
| min_python | 3.9 \| 3.10 \| 3.11 \| 3.12 \| 3.13 \| 3.14 | 3.11 | Gates which Version Floors features may be emitted unguarded, and which fallback appears instead |
| package_manager | pip \| uv \| poetry \| pdm \| conda | pip | Chooses the install, lock, and venv commands in every example (`references/packaging.md`) |
| type_strictness | none \| gradual \| strict | gradual | How far annotations go: none skips hints, gradual annotates public boundaries, strict turns on `disallow_untyped_defs` (`references/type-checking.md`) |
| test_runner | pytest \| unittest | pytest | Shape of emitted tests, fixtures, and mocking guidance (`references/testing.md`) |
| target_os | linux \| macos \| windows \| cross | cross | Path, encoding, and multiprocessing start-method assumptions; `cross` flags all three |
| src_layout | src \| flat | src | Project scaffolding, editable-install and import advice (`references/packaging.md`) |
| line_length | number (79-120) | 88 | Formatting of emitted code and the `ruff`/`black` config value (`references/linting.md`) |
| change_workflow | test-first \| fix-first | test-first | Order of the work: test-first writes the failing test before the fix, fix-first patches first and backfills the test against the reverted change (`references/testing.md`) |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Tooling**: formatter and linter (ruff vs black+flake8), checker (mypy vs pyright), task runner, notebook vs module workflow — affects every emitted config block (`references/linting.md`)
- **Conventions**: docstring style (Google/NumPy/reST), naming, module granularity, error-message phrasing — affects generated code and review comments
- **Platform**: deployment target (container, serverless, desktop, embedded), CPU architecture, private package index, CI provider — affects `references/packaging.md` and `references/versions.md` guidance
- **Safety posture**: how aggressively to flag `pickle`, `eval`, `shell=True`, missing timeouts and unpinned dependencies — affects `references/security.md` and `references/cli.md`
- **Dependencies**: stdlib-only constraints, banned or mandated libraries (requests vs httpx, pydantic vs dataclasses), tolerance for new transitive dependencies — affects every recommendation
- **Output format**: whole file vs minimal diff, how much explanation, whether tests accompany every change — affects the shape of the answer, leaving correctness rules intact
- **Work order**: which gates run before a change is proposed rather than after — checker and suite green first, a plan approved before editing, a `--dry-run` pass on destructive scripts, a profile before any optimization — affects the sequence of every task, leaving correctness rules intact

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Bare `pip install` | Installs into whatever interpreter is first on PATH — the "installed it, still ModuleNotFoundError" loop | `python -m pip install` inside an activated venv (`references/packaging.md`) |
| `except Exception: pass` | Turns a crash into a wrong answer three layers away | Log with `logger.exception`, or write down why this failure is expected (`references/errors.md`) |
| `assert user.is_admin` as a check | `python -O` removes every assert, including that one | Raise explicitly (`references/security.md`) |
| `time.time()` to measure a duration | NTP can step the clock backwards mid-measurement and produce negative elapsed time | `time.monotonic()` (`references/datetime.md`) |
| `datetime.utcnow()` | Returns a NAIVE datetime holding UTC: compares wrong against aware values, deprecated in `python >=3.12` | `datetime.now(timezone.utc)` (`references/datetime.md`) |
| f-strings inside logging calls | Formats even when the level is disabled, and every line becomes a unique string to the aggregator | `log.info("user %s", uid)` (`references/logging.md`) |
| `sys.path.append(...)` to fix an import | Works from one entry point, breaks under pytest, packaging, and any other cwd | Editable install with a `src/` layout (`references/imports.md`) |
| `shell=True` with an interpolated value | Command injection — and `/bin/sh` is not bash | Argument list; `shlex.quote` if a shell is unavoidable (`references/subprocess.md`) |
| `verify=False` to silence an SSL error | Disables peer authentication for every request in the process | Install the CA bundle (`references/security.md`) |
| `pickle` across a process, user, or network boundary | Unpickling executes attacker-controlled code before you can inspect it | JSON/msgpack, or an HMAC-signed payload (`references/security.md`) |
| `raise e` when re-raising | Appends the current line and hides where the exception really came from | Bare `raise` (`references/errors.md`) |
| Type hints treated as validation | Unenforced at runtime: `def f(x: int)` happily takes a string | Checker in CI plus runtime validation at the boundary (`references/type-checking.md`) |
| `x in list` or `list.pop(0)` inside a loop | O(n) per operation makes the loop O(n²) | `set` for membership, `deque` for both ends (`references/collections.md`) |

## Where Experts Disagree

- **asyncio vs threads.** asyncio is not "faster Python": for moderate I/O concurrency, `ThreadPoolExecutor` matches it with far less ceremony. Boundary: high connection counts AND an async-native stack end to end → asyncio; one blocking driver anywhere in the chain forfeits the benefit (`references/concurrency.md`).
- **How much typing.** The strict school annotates everything and treats `Any` as a defect; the pragmatic school types boundaries and lets internals be inferred. Boundary: libraries and cross-team APIs → annotate fully; single-owner scripts and glue → boundaries only. Either way, one checker in CI (`references/type-checking.md`).
- **Packaging tooling.** `venv` + `pip` exists on every machine and surprises nobody; `uv`/`poetry`/`hatch` are faster and manage more. Boundary: a project with a real dependency problem, many contributors, or several interpreters justifies the tool; one that installs three libraries does not (`references/packaging.md`).
- **EAFP vs LBYL.** Python's culture prefers `try/except` over pre-checking, and it is genuinely more correct under concurrency — the file can disappear between `exists()` and `open()`. Boundary: LBYL when the operation is expensive or irreversible, EAFP when the failure is cheap and the race is real.
