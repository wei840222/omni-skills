"""Frozen offline task graders. No actual baseline/challenger outputs are bundled."""
import ast
import copy
import csv
import io
import json
import os
from pathlib import Path
import re
import resource
import shlex
import signal
import sqlite3
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "experiments/fixtures/harness_task_checks.json"
PYTHON = ROOT / "experiments/.venv/bin/python"
NODE, BASH = "/usr/bin/node", "/usr/bin/bash"
TSC = "/home/wei/.openclaw/extensions/skill-harness/node_modules/typescript/bin/tsc"
LIMITS = {"timeout_seconds": 4, "vm_timeout_ms": 200, "artifact_bytes": 12000,
          "output_bytes": 131072, "hard_os_sandbox": False,
          "scope": "Reviewed pure-task subset; syntax/API guards are not adversarial OS isolation."}


def _task(task_id):
    for task in json.loads(SPEC.read_text())["tasks"]:
        if task["id"] == task_id:
            return task
    raise ValueError("Unknown frozen task id")


def public_task_input(task_id):
    return {"id": task_id, **copy.deepcopy(_task(task_id)["public"])}


def _caps(executable):
    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (131072, 131072))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    if executable in {str(PYTHON), BASH}:
        memory = 1073741824 if executable == str(PYTHON) else 268435456
        resource.setrlimit(resource.RLIMIT_AS, (memory, memory))


def _invoke(command, folder, payload=b"", arguments=()):
    environment = {"PATH": "", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "TMPDIR": str(folder),
                   "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1",
                   "GOMAXPROCS": "1", "GOMEMLIMIT": "128MiB", "NODE_NO_WARNINGS": "1"}
    with (folder / "stdout.bin").open("wb") as out, (folder / "stderr.bin").open("wb") as err:
        process = subprocess.Popen([*command, *arguments], cwd=folder, env=environment, stdin=subprocess.PIPE,
                                   stdout=out, stderr=err, start_new_session=True, preexec_fn=lambda: _caps(command[0]))
        try:
            process.communicate(payload, timeout=4)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            raise ValueError("runtime-timeout") from None
    if process.returncode != 0:
        raise ValueError("runtime-rejected")
    return (folder / "stdout.bin").read_bytes()


def _python_guard(source):
    allowed_attributes = {"reader", "writer", "StringIO", "writerows", "writerow", "getvalue", "DataFrame",
                          "fillna", "astype", "groupby", "sum", "agg", "reset_index", "sort_values", "to_dict",
                          "copy", "rename", "get", "items", "keys", "values", "append", "extend", "add",
                          "loads", "JSONDecodeError", "splitlines", "strip", "replace", "join", "sort"}
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.ClassDef, ast.Global, ast.Nonlocal)):
            raise ValueError("source-policy")
        if isinstance(node, ast.Name) and (node.id.startswith("__") or node.id in {"open", "eval", "exec", "compile", "getattr", "setattr", "globals", "locals", "vars", "input", "breakpoint"}):
            raise ValueError("source-policy")
        if isinstance(node, ast.Attribute) and node.attr not in allowed_attributes:
            raise ValueError("source-policy")
    return tree


NODE_DRIVER = r'''
const fs=require('node:fs'),vm=require('node:vm'),strip=require('node:module').stripTypeScriptTypes;
const p=JSON.parse(fs.readFileSync(0,'utf8'));
let source=p.source;
if(p.kind==='ts') source=strip(source).replace(/\bexport\s+(?=function)/g,'');
const inputs={kind:p.kind,mode:p.grader.mode,pattern:p.pattern,flags:p.flags,
 cases:p.grader.cases.map(c=>p.kind==='regex'?{text:c.text}:{args:c.args})};
const ctx=vm.createContext({dataJSON:JSON.stringify(inputs)}, {codeGeneration:{strings:false,wasm:false}});
new vm.Script('Object.freeze(JSON);Object.freeze(Object.prototype);Object.freeze(Array.prototype);').runInContext(ctx,{timeout:200});
new vm.Script(source).runInContext(ctx,{timeout:200});
const results=new vm.Script(`
(()=>{const p=JSON.parse(dataJSON);return p.cases.map(c=>{
 if(p.kind==='regex')return {value:Array.from(c.text.matchAll(new RegExp(p.pattern,p.flags)),m=>m[0]),unchanged:true};
 const args=c.args, before=JSON.stringify(args); const fn=${p.kind==='regex' ? 'null' : p.grader.function};
 const result=fn(...args), unchanged=JSON.stringify(args)===before;
 if(p.mode==='readers'){for(let i=0;i<args[0].length;i++)args[0][i]='changed';return {value:result.map(f=>f()),unchanged};}
 return {value:result,unchanged};
});})()`).runInContext(ctx,{timeout:200});
process.stdout.write(JSON.stringify(results));
'''


def _sql_connection():
    db = sqlite3.connect(":memory:", isolation_level=None)
    db.setlimit(sqlite3.SQLITE_LIMIT_LENGTH, 65536)
    db.setlimit(sqlite3.SQLITE_LIMIT_SQL_LENGTH, 12000)
    db.execute("PRAGMA foreign_keys=ON")
    return db


def _sql_guard(db, writable=False):
    ticks = [0]
    def progress():
        ticks[0] += 1
        return int(ticks[0] > 50)
    def authorize(action, first, second, *_):
        allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_RECURSIVE}
        if action == sqlite3.SQLITE_FUNCTION:
            return sqlite3.SQLITE_OK if second in {"sum", "total", "count", "max", "min", "avg", "row_number", "rank", "coalesce", "ifnull"} else sqlite3.SQLITE_DENY
        if writable and action in {sqlite3.SQLITE_TRANSACTION, sqlite3.SQLITE_SAVEPOINT}:
            return sqlite3.SQLITE_OK
        if writable and action in {sqlite3.SQLITE_UPDATE, sqlite3.SQLITE_INSERT} and first in {"accounts", "ledger"}:
            return sqlite3.SQLITE_OK
        return sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY
    db.set_authorizer(authorize)
    db.set_progress_handler(progress, 1000)


def _sql_results(payload):
    source, grader, kind = payload["source"], payload["grader"], payload["kind"]
    checks = []
    for index, fixture in enumerate(grader["cases"]):
        # Reversing insertion order is a semantic stability check, not a second solution.
        permutations = [fixture, list(reversed(fixture))] if kind == "sql" else [fixture]
        for order, item in enumerate(permutations):
            with _sql_connection() as db:
                if kind == "sql":
                    db.execute("CREATE TABLE events(event_id INTEGER PRIMARY KEY,customer TEXT,occurred_at INTEGER,amount INTEGER)")
                    db.executemany("INSERT INTO events VALUES(?,?,?,?)", item)
                    _sql_guard(db)
                    cursor = db.execute(source)
                    got = cursor.fetchall()
                    groups = {}
                    for event_id, customer, occurred_at, amount in fixture:
                        group = groups.setdefault(customer, [])
                        group.append((occurred_at, event_id, amount))
                    expected = [(customer, max(events)[1], sum(row[2] for row in events)) for customer, events in sorted(groups.items())]
                    passed = [col[0] for col in cursor.description] == ["customer", "event_id", "total"] and got == expected
                else:
                    db.executescript(grader["schema"])
                    db.executemany("INSERT INTO accounts VALUES(?,?)", fixture["accounts"])
                    db.execute("INSERT INTO request VALUES(?,?,?)", fixture["request"])
                    _sql_guard(db, writable=True)
                    failed = False
                    try:
                        db.executescript(source)
                    except sqlite3.IntegrityError:
                        failed = True
                        db.rollback()
                    sender, recipient, amount = fixture["request"]
                    expected = dict(fixture["accounts"])
                    if fixture["valid"]:
                        expected[sender] -= amount
                        expected[recipient] += amount
                    passed = (failed != fixture["valid"] and not db.in_transaction
                              and dict(db.execute("SELECT id,balance FROM accounts")) == expected
                              and db.execute("SELECT sender,recipient,amount FROM ledger").fetchall() == ([tuple(fixture["request"])] if fixture["valid"] else []))
                checks.append({"name": f"semantic-{index + 1}-order-{order}", "passed": passed})
    return checks


def _python_results(payload):
    import builtins
    safe_names = ["abs", "all", "any", "bool", "dict", "enumerate", "float", "int", "isinstance", "len", "list", "max", "min", "range", "set", "sorted", "str", "sum", "tuple", "type", "zip", "ValueError", "Exception"]
    namespace = {"__builtins__": {name: getattr(builtins, name) for name in safe_names}, "csv": csv, "io": io, "json": json}
    if payload["kind"] == "pandas":
        import pandas as pd
        namespace["pd"] = pd
    exec(compile(_python_guard(payload["source"]), "reviewed-task-artifact", "exec"), namespace)
    grader, checks = payload["grader"], []
    for index, fixture in enumerate(grader["cases"]):
        value = fixture["text"] if grader["mode"] == "ndjson" else fixture
        value = copy.deepcopy(value)
        original = copy.deepcopy(value)
        try:
            got = namespace[grader["function"]](value)
            if grader["mode"] == "csv":
                expected = list(csv.reader(io.StringIO(fixture), delimiter=";"))
                passed = isinstance(got, str) and list(csv.reader(io.StringIO(got))) == expected and _crlf_records(got)
            elif grader["mode"] == "ndjson":
                expected = [json.loads(line) for line in fixture["text"].splitlines() if line.strip()] if fixture["valid"] else None
                passed = fixture["valid"] and got == expected
            else:
                totals = {}
                for row in fixture:
                    totals[row["sku"]] = totals.get(row["sku"], 0) + (row["units"] or 0)
                expected = [{"sku": sku, "units": units} for sku, units in sorted(totals.items())]
                passed = got == expected and all(type(row["units"]) is int for row in got)
        except ValueError:
            passed = grader["mode"] == "ndjson" and fixture["valid"] is False
        checks.append({"name": f"semantic-{index + 1}", "passed": bool(passed and value == original)})
    return checks


def _crlf_records(text):
    """Check record separators outside quoted fields; embedded newlines survive."""
    quoted, index = False, 0
    while index < len(text):
        char = text[index]
        if char == '"':
            if quoted and text[index:index + 2] == '""':
                index += 2
                continue
            quoted = not quoted
        if not quoted and ((char == "\n" and (index == 0 or text[index - 1] != "\r"))
                           or (char == "\r" and text[index:index + 2] != "\r\n")):
            return False
        index += 1
    return not quoted


def _source_guard(source, kind):
    if kind in {"python", "pandas"}:
        _python_guard(source)
    elif kind in {"ts", "js"}:
        if re.search(r"\b(import|require|process|fetch|eval|Function|constructor|prototype|__proto__|globalThis|module|Buffer)\b", source):
            raise ValueError("source-policy")
        if kind == "ts" and (re.search(r"\b(any|as)\b|@ts-|///|\breturn\s*<|=\s*<", source)):
            raise ValueError("source-policy")
    elif kind == "bash":
        if re.search(r"[`<>]|\$\(|\\\n|\b(?:PATH|HOME|BASH_ENV|ENV)\b", source):
            raise ValueError("source-policy")
        tokens = shlex.split(source, comments=True)
        if any(token in {"eval", "exec", "source", ".", "command", "builtin", "enable", "trap", "cd", "export", "declare", "typeset", "unset", "kill", "alias", "unalias", "set", "shopt", "ulimit", "umask", "-v"} for token in tokens):
            raise ValueError("source-policy")


def run_task_check(task_id, artifact_dir):
    task = _task(task_id)
    artifact_dir = Path(artifact_dir).resolve()
    if not artifact_dir.is_relative_to(ROOT / "experiments/datasets"):
        raise ValueError("Task artifacts must be inside workspace experiments/datasets")
    artifact = artifact_dir / task["public"]["artifact_contract"]["filename"]
    checks = []
    try:
        if artifact.is_symlink() or not artifact.is_file() or artifact.stat().st_size > 12000:
            raise ValueError("artifact-policy")
        source = artifact.read_text()
        grader, kind = task["grader"], task["grader"]["kind"]
        _source_guard(source, kind)
        parent = ROOT / "experiments/datasets/task-check-test-fixtures"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as temporary:
            folder = Path(temporary)
            (folder / artifact.name).write_text(source)
            payload = {"kind": kind, "source": source, "grader": grader}
            if kind == "ts":
                (folder / "harness.ts").write_text(grader["ts_harness"])
                (folder / "tsconfig.json").write_text(json.dumps({"files": [artifact.name, "harness.ts"], "compilerOptions": {"strict": True, "noEmit": True, "target": "ES2023", "module": "ESNext", "moduleResolution": "bundler", "types": [], "skipLibCheck": True}}))
                _invoke([NODE, TSC, "--project", "tsconfig.json", "--pretty", "false"], folder)
                checks.append({"name": "strict-type-contract", "passed": True})
            if kind in {"ts", "js", "regex"}:
                if kind == "regex":
                    pattern = json.loads(source)
                    if set(pattern) != {"pattern", "flags"} or pattern["flags"] not in {"g", "gu"} or len(pattern["pattern"]) > 256:
                        raise ValueError("pattern-contract")
                    payload.update(pattern)
                    payload["source"] = ""
                observed = json.loads(_invoke([NODE, "--max-old-space-size=64", "-e", NODE_DRIVER], folder, json.dumps(payload).encode()))
                for index, (got, fixture) in enumerate(zip(observed, grader["cases"])):
                    expected = fixture["expected"]
                    checks.append({"name": f"semantic-{index + 1}", "passed": got["value"] == expected and got["unchanged"]})
                if len(observed) != len(grader["cases"]):
                    raise ValueError("result-count")
            elif kind == "bash":
                (folder / "driver.sh").write_text(source + "\n" + grader["function"] + ' "$@"\n')
                for index, values in enumerate(grader["cases"]):
                    data = b"" if task_id == "t09" else b"".join(value.encode() + b"\0" for value in values)
                    observed = _invoke([BASH, "--noprofile", "--norc", "--restricted", "driver.sh"], folder, data, values if task_id == "t09" else ())
                    expected = b"".join((value if task_id == "t09" else value.rsplit("/", 1)[-1]).encode() + b"\0" for value in values)
                    checks.append({"name": f"argv-or-record-{index + 1}", "passed": observed == expected})
            else:
                checks.extend(json.loads(_invoke([str(PYTHON), "-I", "-B", str(Path(__file__).resolve()), "--worker"], folder, json.dumps(payload).encode())))
    except (ValueError, OSError, SyntaxError, sqlite3.Error, KeyError, TypeError, StopIteration):
        checks.append({"name": "bounded-execution-or-contract", "passed": False})
    failures = [check["name"] for check in checks if not check["passed"]]
    return {"passed": bool(checks) and not failures, "checks": checks, "failures": failures, "limits": dict(LIMITS)}


if __name__ == "__main__" and sys.argv[1:] == ["--worker"]:
    try:
        payload = json.load(sys.stdin)
        result = _sql_results(payload) if payload["kind"] in {"sql", "transaction"} else _python_results(payload)
        print(json.dumps(result))
    except Exception:
        sys.exit(1)
