# Blueprints

## Registration

- Set `url_prefix` at registration: `app.register_blueprint(bp, url_prefix="/api")`.
- Routes on the blueprint are relative to that prefix: `@bp.route("/users")` → `/api/users`.
- Name endpoints as `blueprint_name.endpoint` for `url_for`.

## Hooks

- `bp.before_request` / `after_request` / `teardown_request` apply only to that blueprint.
- `app.before_request` runs for every request—use for global auth/logging, not feature-specific logic.

## Layout

- Keep blueprint modules free of a concrete `app` import.
- Export `bp` and register it from the factory so tests can register a subset of blueprints.
