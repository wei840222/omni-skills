# Flask-SQLAlchemy pitfalls

## Session lifecycle

- Request-scoped session is normal with Flask-SQLAlchemy; it tears down after the request.
- Call `db.session.commit()` explicitly—autocommit is not the default.
- On error: `db.session.rollback()` or the session stays unusable for the rest of the request.

## Detached instances

- Accessing lazy attributes after the session closed raises `DetachedInstanceError`.
- Fix: keep work inside the session scope, eager-load what the response needs, or `db.session.merge(obj)` / refetch by primary key.

## Background tasks

- Do not reuse the request session on another thread.
- Open a new app context and let Flask-SQLAlchemy create a fresh session, or manage an explicit sessionmaker bound to the app's engine.

## Transactions

- Group multi-step writes in one commit; partial commits leave inconsistent domain state.
- After rollback, discard in-memory objects that were part of the failed unit of work.
