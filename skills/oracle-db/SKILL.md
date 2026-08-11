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

## Resources

When interacting with an Oracle Database or when the user needs Oracle-specific SQL syntax, pagination, hints, or performance tuning, load the following reference:

- **Syntax & Patterns**: Load `references/syntax.md` for Oracle-specific syntax differences, pagination rules, NULL handling, date formatting, PL/SQL block structures, hints, and common performance traps.

## Execution Workflow

1.  **Understand Database Target**: Identify the target Oracle Database version (e.g., 12c, 19c, 23ai).
2.  **Formulate Query or Script**: Write the SQL or PL/SQL utilizing modern Oracle syntax (e.g., `FETCH FIRST`, `BOOLEAN` in 23c).
3.  **User Confirmation**: Stop and present the generated SQL or PL/SQL to the user for confirmation before execution, especially for DDL or destructive operations.
4.  **Execute**: Run the script only after user approval.

## Failure Modes

-   **Unsupported Version**: If the user asks for a feature not in their version (e.g., `FETCH FIRST` on Oracle 11g), fall back to older syntax (e.g., `ROWNUM` subqueries) and notify the user.
-   **Execution Errors**: If execution fails with an ORA- error, analyze the error message and provide a corrected script.

## Anti-patterns (Blacklist)

-   Use `VARCHAR2` exclusively instead of `VARCHAR`.
-   Use `||` for string concatenation instead of `CONCAT()`.
-   Treat the empty string `''` as `NULL` rather than a length-0 string, matching Oracle behavior.
-   Ensure `EXCEPTION WHEN OTHERS` is handled in PL/SQL blocks.
