---
name: flask
description: >
  Audit Flask apps for context errors, circular imports, secure session cookies,
  debug exposure, blueprints, Flask-SQLAlchemy session pitfalls, and production
  WSGI deployment. Use when fixing "working outside application/request context",
  factory import cycles, session cookie flags, debug=True risks, or replacing
  flask run with Gunicorn/uWSGI. Not for Django, FastAPI, or plain Python.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✨","displayName":"Flask","requires":{"bins":["python3"]}}'
  related-skills: '{"django":"Full Django stack, ORM, admin, and migrations beyond Flask.","fastapi":"Async-first FastAPI services instead of Flask.","py":"Plain Python packaging, typing, and pytest outside Flask.","http":"Protocol-level HTTP status, headers, and caching independent of Flask.","rest-api":"Framework-independent API contracts and error shapes."}'
---

## When to load

- Flask app init, blueprints, extensions, or factory pattern (`create_app`)
- RuntimeError: working outside application/request context
- Circular imports between models, blueprints, and the app object
- Session cookie security (`SECRET_KEY`, Secure/HttpOnly/SameSite)
- `debug=True` / development server in a production path
- Flask-SQLAlchemy commit/rollback, detached instance, or background-task sessions
- Deploying behind Gunicorn/uWSGI + reverse proxy instead of `flask run`

Load deeper notes only when needed:

| Topic | File |
|-------|------|
| Application & request context | `references/context.md` |
| Factory pattern & circular imports | `references/architecture.md` |
| Sessions & cookie security | `references/security.md` |
| Debug mode & production WSGI | `references/deployment.md` |
| Blueprints | `references/blueprints.md` |
| Flask-SQLAlchemy pitfalls | `references/sqlalchemy.md` |
| Common request/response mistakes | `references/common-mistakes.md` |
| Research sources | `references/sources.md` |

## Core rules

1. **Need app or request context before touching proxies.** `current_app`, `g`, `request`, and `session` only work inside a request or an explicit `with app.app_context():` / test client. Background jobs and CLI commands must push context or receive plain data—never bare proxies.
2. **Prefer `create_app()` and import `current_app`, not a module-level `app`.** Factory + late imports break most circular-import cycles between models and blueprints.
3. **Bind extensions with `init_app(app)`.** Construct extensions without an app, then bind inside the factory so imports stay order-independent.
4. **Set a strong `SECRET_KEY` and harden session cookies in production.** Unsigned cookies let anyone forge session data. Use `SESSION_COOKIE_SECURE=True`, `SESSION_COOKIE_HTTPONLY=True`, and an explicit `SESSION_COOKIE_SAMESITE`.
5. **Ship production with debug disabled and a WSGI server.** Debug mode enables a remote code-execution console; use `FLASK_DEBUG` only in development and serve with Gunicorn/uWSGI behind a reverse proxy—not `flask run` / `app.run`.
6. **Commit and roll back SQLAlchemy sessions explicitly.** Autocommit is off by default; leave a failed session dirty and the next request inherits the bad state. Background work needs its own session, not the request-scoped one.
7. **Prefer `url_for` and `jsonify`.** Hard-coded paths break on blueprint prefixes; raw `json.dumps` skips the correct content type and app JSON provider.

## Quick checks

| Symptom | First move |
|---------|------------|
| `working outside of application context` | Wrap with `app.app_context()` or move work into a request/CLI that already has context (`references/context.md`) |
| `working outside of request context` | Use test client, `test_request_context()`, or pass values instead of reading `request`/`session` |
| Import cycle on `from app import app` | Switch to factory + `current_app`; register blueprints inside the factory (`references/architecture.md`) |
| Session data forged / cookies on HTTP | Rotate `SECRET_KEY`; set Secure + HttpOnly (+ SameSite) (`references/security.md`) |
| Production process exposes interactive debugger | Force `debug=False` / unset `FLASK_DEBUG`; replace `app.run` with WSGI server (`references/deployment.md`) |
| DetachedInstanceError / stale session after error | `db.session.rollback()`; refetch or merge; open a fresh session off-request (`references/sqlalchemy.md`) |

## Output gates

Before calling a Flask change done:

- Context boundaries named (request vs app vs background) and no proxy used outside them
- Factory/`init_app` used when modules import each other
- Production path has no `debug=True` and no built-in server as the serving process
- Session cookie flags and `SECRET_KEY` source documented
- DB writes commit/rollback on the correct session scope
