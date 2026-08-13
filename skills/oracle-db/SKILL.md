---
name: oracle-db
description: "Write and optimize Oracle SQL and PL/SQL queries. Trigger when interacting with an Oracle database, generating PL/SQL blocks, or optimizing Oracle-specific SQL queries (pagination, hints, dates, modern 23ai features)."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔴","requires":{"anyBins":["sqlplus","sql"]}}'
---

# Oracle DB

## State Location

This skill is completely stateless and does not require persistent state storage.

## Execution Workflow

1.  **Understand Database Target**: Identify the target Oracle Database version (e.g., 12c, 19c, 23ai).
2.  **Formulate Query or Script**: Write the SQL or PL/SQL utilizing modern Oracle syntax (e.g., `FETCH FIRST`, `BOOLEAN` in 23c).
3.  **User Confirmation**: Stop and present the generated SQL or PL/SQL to the user for confirmation before execution, especially for DDL or destructive operations.
4.  **Execute**: Run the script only after user approval.

## Failure Modes

-   **Unsupported Version**: If the user asks for a feature not in their version (e.g., `FETCH FIRST` on Oracle 11g), fall back to older syntax (e.g., `ROWNUM` subqueries) and notify the user.
-   **Execution Errors**: If execution fails with an ORA- error, analyze the error message and provide a corrected script.

## Anti-patterns (Blacklist)

-   Do not use `VARCHAR`; use `VARCHAR2` exclusively.
-   Do not use `CONCAT()`; use `||` for string concatenation.
-   Do not treat the empty string `''` as non-NULL; treat it as `NULL` to match Oracle behavior.
-   Do not omit exception handling; always include `EXCEPTION WHEN OTHERS` in PL/SQL blocks.

## Syntax and performance patterns

### Syntax differences

- Use `ROWNUM` for limiting rows (`WHERE ROWNUM <= 10`); Oracle 12c+ also supports `FETCH FIRST 10 ROWS ONLY`.
- Use `DUAL` for expressions, for example `SELECT SYSDATE FROM dual`.
- Use `VARCHAR2`, not `VARCHAR`; use `||` to concatenate multiple values.
- Treat an empty string as `NULL`; this differs from many other databases.

### Pagination and NULL handling

- `ROWNUM` is assigned before `ORDER BY`; order in a subquery before applying it.
- For pre-12c offsets, use nested `ROWNUM` queries. Prefer `OFFSET … FETCH NEXT …` on 12c+.
- Use `NVL(col, default)` for two-argument null replacement, `NVL2(col, if_not_null, if_null)` for conditional values, and `NULLIF(a, b)` to avoid division by zero.

### Dates, sequences, and hierarchy

- `SYSDATE` has no parentheses. Use `TO_DATE(value, format)` and `TO_CHAR(date, format)` with explicit formats; date arithmetic is in days.
- Get a sequence value with `seq_name.NEXTVAL`; `CURRVAL` is available only after `NEXTVAL` in the same session. Consider identity columns on 12c+.
- Use `CONNECT BY PRIOR child = parent` with `START WITH` for hierarchies. `LEVEL` provides depth and `SYS_CONNECT_BY_PATH` builds a path.

### SQL, PL/SQL, and transactions

- Use bind variables (`:variable_name` in PL/SQL) to avoid hard parsing and shared-pool contention.
- Put hints after `SELECT`, for example `/*+ INDEX(table idx_name) */`, `/*+ FULL(table) */`, or `/*+ PARALLEL(table, 4) */`; verify a plan rather than assuming a hint helps.
- Run anonymous PL/SQL blocks as `BEGIN … END;` followed by `/`, enable `SERVEROUTPUT` before using `DBMS_OUTPUT.PUT_LINE`, and handle or log exceptions.
- Oracle does not auto-commit ordinary DML; commit explicitly. DDL auto-commits. Use `SAVEPOINT` / `ROLLBACK TO` for partial rollback and bounded `SELECT FOR UPDATE WAIT n` rather than an indefinite lock wait.

### Performance and common traps

- Inspect plans with `EXPLAIN PLAN FOR …` and `DBMS_XPLAN.DISPLAY`; use `V$SQL` and `V$SESSION` only when the account has the required privileges.
- Avoid `SELECT *`, especially where LOBs are present. Do not rely on `ROWID` across transactions.
- Oracle uses `MINUS`, not `EXCEPT`. Prefer `CASE` over Oracle-only `DECODE` when portability matters, and avoid implicit type conversion such as comparing a numeric column with a string literal.

### Modern features

- Oracle 23ai adds JSON Relational Duality and AI Vector Search; Oracle 23c adds the SQL `BOOLEAN` type and `IF EXISTS` / `IF NOT EXISTS` DDL forms.
- Oracle 21c+ supports Multilingual Engine JavaScript. Confirm database edition and version before selecting these features.
