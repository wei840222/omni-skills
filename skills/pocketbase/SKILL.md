---
name: pocketbase
description: Build and maintain PocketBase backends with collections, authentication, API rules, realtime subscriptions, file uploads, and JavaScript event hooks. Use when implementing or troubleshooting a PocketBase application with its JavaScript SDK or server runtime.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📦","requires":{"bins":["pocketbase"]}}'
---

# PocketBase

## Workflow

1. Identify the running PocketBase version, the target collection name, and whether the task affects client SDK code, API rules, or server hooks.
2. Inspect the application's collection schema and current rules before changing authentication, access, or data behavior. Collection names are application-defined; `users` below is only an example.
3. Apply the smallest change in the relevant layer, then verify it against a local development instance and the current official documentation for that PocketBase version.
4. Keep runtime data outside this skill package. PocketBase creates `pb_data/` beside its executable; treat it as application data and keep it out of source control. Version JavaScript migrations in `pb_migrations/` when the application uses them.

## Choose the Relevant Guide

| Task | Read first |
| --- | --- |
| JavaScript SDK queries, auth-store use, realtime subscriptions, or file uploads | `references/sdk-usage.md` |
| Password or OAuth2 login, superusers, or API-rule semantics | `references/auth-and-rules.md` |
| Server-side JavaScript event hooks | `references/hooks.md` |

## Safe Change Boundary

- Keep superuser credentials and client secrets out of browser code, logs, and repositories.
- Confirm the intended collection and rule outcome before changing access rules, deleting records, or applying migrations.
- If a proposed API or hook call is not documented for the installed version, stop and verify it in that version's official documentation before implementing it.

## Sources

- PocketBase documentation: https://pocketbase.io/docs/
- PocketBase JavaScript SDK: https://github.com/pocketbase/js-sdk
