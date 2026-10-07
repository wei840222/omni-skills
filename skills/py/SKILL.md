---
name: py
description: >
  Writes, debugs, and reviews Python code — runtime traps, packaging, typing, async,
  tests, performance. Use when Python raises or misbehaves: ModuleNotFoundError,
  circular imports, AttributeError on None, UnboundLocalError, UnicodeDecodeError,
  mutable default arguments, `is` vs `==`, float rounding, naive vs aware datetimes,
  or a wrong answer with no exception; when pip, uv, poetry, venv, pyproject or a
  lockfile fight over dependencies, or a package installs but will not import; when
  threads, asyncio, multiprocessing or the GIL hang, deadlock, or leak memory; when
  pytest passes but should not, mocks patch the wrong module, or async tests never
  run; when mypy or pyright errors need clearing; when a script is slow, eats RAM,
  or gets OOM-killed; when subprocess calls hang or logs fail to appear; or when upgrading
  Python breaks the build. Not for library-specific problems — pandas, numpy, django,
  fastapi and flask have their own skills.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐍","requires":{"bins":["python3"]},"os":["linux","darwin","win32"],"displayName":"Python"}'
  related-skills: '{"pandas":"DataFrame-specific traps and idioms beyond core Python.","numpy":"Array and numerical work beyond plain Python lists.","fastapi":"Async web APIs in Python.","django":"Django ORM and framework patterns.","flask":"Flask apps, Werkzeug debugger, and WSGI patterns.","docker":"Container base images and pin strategy for Python runtimes.","regex":"Deeper regular-expression craft beyond stdlib re.","code":"Language-agnostic implementation planning when the task is not Python-specific.","git":"Repository workflow around the Python change being committed."}'
---

## State location

Python preferences may exist in `<workspace>/py/`, `<workspace>/memory/py/`, or `~/py/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/py/`, `<workspace>/memory/py/`, `~/py/`.
3. If none exists and state must be created, default to `<workspace>/py/` only with user consent.
4. If multiple candidates exist, use only the first, report the conflict, and leave the others untouched.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/py/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use `<state_root>/config.yaml` for user preferences (see Configuration in `references/core-rules.md`). Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy paths `~/Clawic/data/py/` and `~/clawic/py/` are migration sources only — outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration. Say in one line if a migration was performed and from where.

## When to use

- Writing or reviewing Python — scan Core Rules and Output Gates before committing
- Debugging wrong results without exceptions: state leaking across calls, aliased mutations, silent coercion
- Any traceback whose cause is not obvious in ten seconds, plus hangs, memory growth, and segfaults
- Environment and dependency work: venvs, lockfiles, editable installs, publishing, version upgrades
- Choosing a concurrency model, a data model, or a typing strategy, and living with the consequences
- Hardening a script into a tool: arguments, exit codes, logging, timeouts, retries, untrusted input
- Not for library-specific issues — hand off to `pandas`, `numpy`, `django`, `fastapi`, or `flask`

## Quick reference

Read `SKILL.md` by default. Open exactly one guide when the situation matches.

| Situation | Play |
|-----------|------|
| Core rules, configuration, traps, expert disagreements | `references/core-rules.md` |
| Wrong value, no exception | `repr()` at input, midpoint, output; first wrong value is the bug → `references/debugging.md` |
| A traceback you have not seen before | Message → cause table, then matching chain → `references/debugging.md` |
| Installed it, still `ModuleNotFoundError` | Check `sys.executable`, then `python -m pip` → `references/packaging.md` |
| venvs, lockfiles, uv vs pip vs poetry, publishing | Apps pin with hashes; libraries declare ranges → `references/packaging.md` |
| `cannot import name X from partially initialized module` | Circular import; `import a` + `a.f()` first → `references/imports.md` |
| `is` vs `==`, float rounding, money, NaN, string surgery | `is` only for `None`/`True`/`False`/sentinels; `Decimal` from strings → `references/types.md` |
| Aliasing, copies, ordering, membership cost | `[[]]*3` shares one list; `x in list` is O(n) → `references/collections.md` |
| State leaks across calls: defaults, closures, decorators, generators | Defaults evaluate once at `def` time → `references/functions.md` |
| Class design: shared attributes, hashability, MRO, `__slots__` | `__eq__` without `__hash__` makes instances unhashable → `references/classes.md` |
| dict vs dataclass vs NamedTuple vs pydantic; validating input | Validate once at the boundary → `references/data-modeling.md` |
| Slow, hanging, or racy: GIL, threads, asyncio, multiprocessing | Pure-Python CPU → processes; I/O → threads or asyncio → `references/concurrency.md` |
| Too slow, or too much memory | Profile first, then fix the top line → `references/performance.md` |
| Tests pass but should not; mock patches nothing; async tests skipped | Patch where the name is USED; `autospec=True` → `references/testing.md` |
| mypy or pyright errors, annotating a legacy codebase | Freeze a baseline, ratchet one package at a time → `references/type-checking.md` |
| Formatting, import order, lint rules, pre-commit | One formatter owns layout; `ruff check` for bugs → `references/linting.md` |
| `UnicodeDecodeError`, CSV/JSON traps, atomic writes, temp files | `encoding="utf-8"`; temp then `os.replace` → `references/files.md` |
| Timezones, DST, parsing dates, measuring elapsed time | Aware datetimes; `time.monotonic()` for durations → `references/datetime.md` |
| Calling git/ffmpeg/anything external, hanging or failing silently | `run([...], check=True, timeout=…)`, never `shell=True` with interpolation → `references/subprocess.md` |
| Writing a script or CLI: arguments, exit codes, pipes, signals | `sys.exit(main())`; stdout for data, stderr for logs → `references/cli.md` |
| Nothing appears in the logs, or deciding what to log | Four gates: basicConfig, logger, handler, propagation → `references/logging.md` |
| Exception design, chaining, retries, timeouts | `raise X from exc`; exponential backoff with jitter → `references/errors.md` |
| Calling an HTTP API: sessions, status codes, redirects, streaming | One client per process; `raise_for_status()` before `.json()` → `references/http.md` |
| A local database, cache, or queue in a file; `database is locked` | WAL + busy timeout; one connection per thread → `references/sqlite.md` |
| Untrusted input: pickle, eval, SQL, paths, archives, secrets | Unpickling executes code; parameterize SQL; contain paths → `references/security.md` |
| "Is there something in the stdlib for this?" | Counter, deque, bisect, itertools, pathlib, secrets, sqlite3 → `references/stdlib.md` |
| Notebook works for you and nobody else; results change between runs | Restart and run all; `%pip` not `!pip` → `references/notebooks.md` |
| Upgrading Python, choosing a version, a module that vanished | Run suite with `-W error::DeprecationWarning` on OLD version first → `references/versions.md` |
| Official sources for PEPs, packaging, typing, security | `references/sources.md` |
| Anything else | Core rules, then `python -I -c '<five suspect lines>'` and re-add one thing at a time |

## Core rules (summary)

Full text, configuration table, traps, and expert disagreements: `references/core-rules.md`.

1. No mutable defaults: `def f(xs=None)` then `if xs is None: xs = []`. Never `xs = xs or []`.
2. `is` only for `None`, `True`, `False`, and sentinels; `==` for everything else.
3. Never mutate the collection you iterate — iterate a copy or apply changes after.
4. Match concurrency to workload: pure-Python CPU → `multiprocessing`; I/O → threads or asyncio.
5. `except Exception:`, never bare `except:`. Re-raise with bare `raise`.
6. Files, locks, sockets, connections: always `with`.
7. Money and exact decimals: `decimal.Decimal('1.10')` from strings — never `Decimal(1.1)`.
8. Declare `encoding='utf-8'` at every I/O boundary.
9. Guard entry points with `if __name__ == "__main__":`.

## Version floors

Syntax and stdlib floors that shape everyday code. Support windows and upgrade procedure: `references/versions.md`. Inline floors stay next to the instruction they gate in each guide.

| Feature | Needs |
|---|---|
| Guaranteed dict insertion order, dataclasses, `breakpoint()`, `from __future__ import annotations`, `sys.stdout.reconfigure` | python >=3.7 |
| Walrus `:=`, positional-only `/`, `functools.cached_property`, `TypedDict`/`Protocol`/`Literal`/`Final`, `basicConfig(force=)`, self-documenting `f"{value=}"` | python >=3.8 |
| Builtin generics `list[int]`, `d1 \| d2` (dict merge), `zoneinfo`, `removeprefix`/`removesuffix`, `functools.cache`, `asyncio.to_thread`, `importlib.resources.files`, `Path.is_relative_to`, `graphlib`, `argparse.BooleanOptionalAction`, `executor.shutdown(cancel_futures=)` | python >=3.9 |
| `X \| Y` unions, `match`, `zip(strict=True)`, dataclass `slots=`/`kw_only=`, `itertools.pairwise`, `ParamSpec`, `EncodingWarning` and `-X warn_default_encoding` | python >=3.10 |
| `ExceptionGroup`/`except*`, `asyncio.TaskGroup`, `tomllib`, `Self`, `StrEnum`, `exc.add_note()`, `contextlib.chdir`, full-ISO `fromisoformat`, `NotRequired` | python >=3.11 |
| PEP 695 generics (`def f[T]()`), `@override`, `itertools.batched`, `tarfile(filter="data")` | python >=3.12 |
| Experimental free-threaded build; PEP 594 module removals (`cgi`, `telnetlib`, …) | python >=3.13 |
| `forkserver` as the Linux multiprocessing default, lazy annotations (PEP 649) | python >=3.14 |
| UTF-8 as the default text encoding everywhere (PEP 686), retiring the locale default | python >=3.15 |

## Output gates

Before delivering Python code, check:

- No mutable default argument, and no `xs or []` where an empty argument is meaningful
- Every text `open`, `subprocess`, and decode boundary declares `encoding="utf-8"`; every file, lock, socket, and connection is acquired in a `with`
- Every network, subprocess, lock, and queue call has a timeout
- Exceptions: narrowest class caught, chained with `from`, nothing swallowed without a log line or a written reason
- Logging through a module logger with lazy `%s` arguments and no secrets
- Syntax and stdlib stay within `min_python`; annotations match `type_strictness`
- Nothing user-supplied reaches `eval`, `pickle`, a shell string, an SQL string, or a path join without containment
- The new test was seen failing without the fix in place — `change_workflow` decides when that run happens, never whether it happened
