---
name: django
description: "Build, debug, and harden Django web applications. Use for Django models, ORM query problems, migrations, views, templates, forms, admin, DRF, deployment, async work, or tests; not for plain Python, FastAPI/Flask, or database-engine tuning."
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"🌿","requires":{"bins":["python3"]}}'
  related-skills: '{"auth":"Use for protocol-level OAuth, SAML, OIDC, MFA, and passwordless identity flows beyond Django session integration.","fastapi":"Use for async-first services that do not need Django’s ORM, admin, or templates.","pg":"Use for PostgreSQL execution plans, index design, vacuum, locks, and connection-pooling questions below Django’s ORM.","py":"Use for plain Python semantics, packaging, typing, asyncio internals, and pytest mechanics outside Django-specific behavior.","rest-api":"Use for API versioning, contracts, error shapes, and other framework-independent API design decisions."}'
---

## State location
This skill stores user preferences and project context. Before its first state read or write, resolve `<state_root>` once for the invocation:

1. Use a user- or host-configured state root when one is explicit.
2. Otherwise, use the first existing directory in this order: `<workspace>/django/`, `<workspace>/memory/django/`, then `~/django/`.
3. If more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist; do not merge or synchronize them.
4. If no candidate exists and the user wants to save state, create `<workspace>/django/`. The host supplies `<workspace>`; never substitute the shell working directory.

Use the selected `<state_root>` for every state operation. User preferences and memory format follow `references/setup.md` and `references/memory-template.md`.

## When To Use

- Writing or reviewing Django models, migrations, views, forms, templates, admin classes, or DRF serializers
- A page is slow or the query count grows with the number of rows on screen
- A migration will not generate, will not apply, conflicts after a merge, or would lock a production table
- An exception that is Django's and not Python's: `SynchronousOnlyOperation`, `TransactionManagementError`, `AppRegistryNotReady`, `NoReverseMatch`, `DisallowedHost`, `ImproperlyConfigured`
- Hardening a project for production: settings split, `check --deploy`, static and media, sessions, permissions, upload limits
- Background jobs, async views, Channels, caching, or a test suite that is slow or order-dependent
- For plain Python, use `py`; for PostgreSQL engine tuning, use `pg`; for async-first services without Django’s ORM, admin, or templates, use `fastapi`.

## Quick Reference

| Category | Reference File | When to load |
| --- | --- | --- |
| Admin | `references/admin.md` | When customizing the Django admin interface |
| Async | `references/async.md` | When working with ASGI, Channels, or async views |
| Auth | `references/auth.md` | When dealing with authentication, permissions, or user models |
| Commands | `references/commands.md` | When writing custom management commands |
| Debug | `references/debug.md` | When troubleshooting exceptions or debugging |
| Deployment | `references/deployment.md` | When preparing the app for production (static files, WSGI, config) |
| DRF | `references/drf.md` | When building APIs with Django Rest Framework |
| Forms | `references/forms.md` | When creating or validating forms and formsets |
| i18n | `references/i18n.md` | When translating or localizing the application |
| Layout | `references/layout.md` | When structuring apps or the project directory |
| Migrations | `references/migrations.md` | When generating, applying, or debugging migrations |
| Models | `references/models.md` | When defining data schema, constraints, or signals |
| ORM | `references/orm.md` | When writing or optimizing database queries (N+1, annotations) |
| Performance | `references/performance.md` | When analyzing or improving response times |
| Security | `references/security.md` | When reviewing CSRF, XSS, or SQL injection protections |
| Settings | `references/settings.md` | When configuring settings and environment variables |
| Setup | `references/setup.md` | Upon first use or when configuring the development environment |
| Tasks | `references/tasks.md` | When writing background jobs (Celery, etc.) |
| Templates | `references/templates.md` | When working with the Django template engine |
| Testing | `references/testing.md` | When writing or debugging test suites |
| Upgrade | `references/upgrade.md` | When migrating to a newer Django version |
| Views | `references/views.md` | When writing class-based or function-based views |
| Traps | `references/traps.md` | When reviewing for common pitfalls or architectural disputes |
| Research | `references/research.md` | When a version-sensitive Django claim needs its official source or verification context |

## Fast path

1. Identify the Django subsystem and load its matching reference from the table above.
2. Check the installed Django version and project settings before applying version- or environment-sensitive guidance.
3. For migrations, destructive commands, or production changes, use the reference’s verification and recovery path before proposing execution.

| Situation | Play |
|---|---|
| Query count grows with rows on the page | `select_related` for forward FK/O2O, `prefetch_related` for reverse FK/M2M (Core Rules 1-2, → `references/orm.md`) |
| `Sum`/`Count` inflated after `annotate` | Two joins multiply rows — `Count("x", distinct=True)` or a `Subquery` (→ `references/orm.md`) |
| Rows come back duplicated after filtering on a related model | Chained `.filter().filter()` joins twice; one `.filter(a=..., b=...)` requires the same related row (→ `references/orm.md`) |
| `makemigrations` reports "No changes detected" | App missing from `INSTALLED_APPS`, or models defined outside an imported module (→ `references/migrations.md`) |
| Two migration leaves after a merge | `makemigrations --merge`; never renumber files by hand (→ `references/migrations.md`) |
| The migration must run on a live table | Expand → backfill in batches → contract, each in its own migration (Core Rules 6, → `references/migrations.md`) |
| 403 "CSRF verification failed" | Missing `{% csrf_token %}`, or `CSRF_TRUSTED_ORIGINS` entries without a scheme behind a proxy (→ `references/security.md`) |
| 400 on every request once `DEBUG=False` | `ALLOWED_HOSTS` (→ `references/settings.md`) |
| 500 with an empty response and nothing in the logs | `DEBUG` off with no `LOGGING` config — the exception exists, nothing writes it down (→ `references/settings.md`) |
| Redirect loop behind a load balancer | `SECURE_SSL_REDIRECT` without `SECURE_PROXY_SSL_HEADER` (→ `references/deployment.md`) |
| `SynchronousOnlyOperation` | ORM touched from an async context — `sync_to_async` or the `a`-prefixed ORM methods (→ `references/async.md`) |
| Task fails with `DoesNotExist`, then succeeds on retry | Queued inside `atomic()` and picked up before COMMIT — `transaction.on_commit` (Core Rules 5, → `references/tasks.md`) |
| Admin change page hangs or times out | A ForeignKey rendered as a `<select>` of every row — `autocomplete_fields`, `list_select_related` (→ `references/admin.md`) |
| Static files 404, or the manifest raises after deploy | `collectstatic`, `STATIC_ROOT`, and hashed-name references (→ `references/deployment.md`) |
| Tests pass alone and fail as a suite | Mutated `setUpTestData` objects, or a setting read at import time (→ `references/testing.md`) |
| A DRF endpoint issues N+1 or leaks a field | `SerializerMethodField` touching a relation; `fields = "__all__"` (→ `references/drf.md`) |
| Login, permissions, or a custom user model | `references/auth.md` — and set `AUTH_USER_MODEL` before the first `migrate` (Core Rules 8) |
| Starting a project, or deciding where a new app goes | `startproject config .`, domain-shaped apps, and a label chosen once — it is baked into every table name (→ `references/layout.md`) |
| Bumping the Django version, or `RemovedInDjangoXXWarning` in the test output | Clear deprecations on the current version with `python -Wa manage.py test`, then move one feature release at a time (→ `references/upgrade.md`) |
| Text must render in the user's language, or dates in their format | `gettext_lazy` at import time, `{% blocktranslate %}` in templates, and `compilemessages` — Django reads `.mo`, never `.po` (→ `references/i18n.md`) |
| Anything else | Reproduce in `manage.py shell`, switch the `django.db.backends` logger to DEBUG, and read the SQL Django actually emitted before changing any code (→ `references/debug.md`) |

Depth on demand, by phase:

- **Start** — `references/layout.md` project skeleton, app boundaries, labels, where non-app code goes
- **Diagnose** — `references/debug.md` symptom to cause in minutes · `references/commands.md` the `manage.py` toolkit and what each command really does
- **Model the data** — `references/models.md` fields, relations, constraints, managers, signals · `references/migrations.md` generating, merging, squashing, online schema change · `references/orm.md` querysets, joins, aggregation, transactions, locking
- **Serve requests** — `references/views.md` view classes, URLs, middleware, requests and responses · `references/forms.md` validation, formsets, file uploads · `references/templates.md` escaping, context, custom tags · `references/auth.md` users, sessions, permissions, password flows · `references/admin.md` the admin at real data volume · `references/drf.md` serializers, viewsets, permissions, pagination · `references/i18n.md` translation, locale switching, formats, timezones
- **Make it fast** — `references/performance.md` query budgets, caching layers, profiling · `references/async.md` async views, ASGI, Channels · `references/tasks.md` background jobs, on_commit, retries, email
- **Ship it** — `references/settings.md` settings layout, env config, logging, timezone · `references/deployment.md` WSGI/ASGI, workers, static and media, release sequence · `references/security.md` the Django-specific attack surface · `references/testing.md` fast, isolated, honest tests · `references/upgrade.md` release cadence, deprecations, LTS windows

## Core Rules

1. **Give every list view a query budget and assert it.** Budget = 1 query for the page + 1 per `prefetch_related` + 0 for `select_related` (it joins into the page query) + 1 for the count if you paginate. A paginated 50-row page of orders with `select_related("customer")` and `prefetch_related("items")` is 1 + 1 + 0 + 1 = 3 queries; the unoptimized version of the same page is 1 + 50 + 50 + 1 = 102. Check it with `assertNumQueries(3)` in a test, not by eye — the regression arrives inside someone else's template change.
2. **`select_related` joins, `prefetch_related` runs a second query.** Forward `ForeignKey`/`OneToOneField` → `select_related` (SQL JOIN, one query). Reverse FK and `ManyToManyField` → `prefetch_related` (one extra query, joined in Python). Passing an M2M to `select_related` raises `FieldError`; passing a forward FK to `prefetch_related` works but buys an extra round trip for nothing.
3. **Queryset-level writes bypass the model.** `update()`, `delete()`, `bulk_create()`, `bulk_update()` never call `Model.save()`, never fire `pre_save`/`post_save`, never touch `auto_now`, and never run validators. That is exactly why they are fast. When you use them, set the timestamp yourself: `.update(status="done", updated_at=timezone.now())`.
4. **Counters use `F()`, not read-modify-write.** `obj.n += 1; obj.save()` reads a stale value and loses every concurrent increment; `Model.objects.filter(pk=pk).update(n=F("n") + 1)` is a single atomic `UPDATE ... SET n = n + 1`. After an `F()` write the in-memory attribute holds an expression object, not a number — `refresh_from_db()` before reading it.
5. **Side effects belong in `transaction.on_commit`.** Anything outside the database — a queued task, an email, a webhook, a cache invalidation — fires only after COMMIT. Queued inside `atomic()`, a worker can pick the job up before the row is visible: the symptom is a task failing with `DoesNotExist` for an object you just created, and passing on retry.
6. **A schema change on a live table is three deploys, not one.** Expand (add the nullable column or new table, ship code that tolerates both shapes) → backfill in batches with a resume key → contract (set NOT NULL, drop the old column) once nothing reads the old shape. One migration that adds a NOT NULL column to a large table rewrites it under a lock, and every request queues behind that lock.
7. **Catch database errors outside the `atomic()` block.** After any statement raises inside a transaction, the connection is poisoned: every later query raises `TransactionManagementError` until rollback. To continue after an expected `IntegrityError`, wrap just the risky statement in its own nested `with transaction.atomic():` — the nesting is a savepoint, and only the savepoint rolls back.
8. **Set `AUTH_USER_MODEL` before the first `migrate`.** Start every project with `class User(AbstractUser): pass` even if it stays empty. Swapping the user model after tables exist means rewriting every FK to `auth.User` and, in practice, rebuilding migration history — Django offers no supported path for it.
9. **Reference models by string; never import them at module import time.** `ForeignKey("shop.Order")` and `settings.AUTH_USER_MODEL` break import cycles. `get_user_model()` or a queryset at module level raises `AppRegistryNotReady`; put it inside the function, or in `AppConfig.ready()` for signal registration only.

## Exception To Cause

Django raises its own exception types before Python's. The type names the subsystem.

| Exception | What it actually means | First move |
|---|---|---|
| `SynchronousOnlyOperation` | An ORM call reached an async context | Wrap in `sync_to_async(...)`, or use `aget`/`acreate`/`async for` (Django >=4.1) (→ `references/async.md`) |
| `TransactionManagementError` | A query ran after an error inside `atomic()`, or `select_for_update()` ran outside a transaction | Rule 7; for locking, open an `atomic()` block first |
| `AppRegistryNotReady` | Models or `get_user_model()` touched during import | Rule 9 — move it into a function or `AppConfig.ready()` |
| `ImproperlyConfigured` | Settings used before `django.setup()`, or a required setting missing or empty | The message tail names the setting; standalone scripts need `django.setup()` before importing any app code |
| `DisallowedHost` | The `Host` header is not in `ALLOWED_HOSTS` | Add the host; behind a proxy also check `USE_X_FORWARDED_HOST` (→ `references/settings.md`) |
| `NoReverseMatch` | A `{% url %}`/`reverse()` name, namespace, or argument count is wrong | Check `app_name` plus the pattern's converters — a `<int:pk>` route rejects a string silently (→ `references/views.md`) |
| `TemplateDoesNotExist` | Loader order, not a missing file, most of the time | The debug page lists every path tried; check `APP_DIRS` and `DIRS` (→ `references/templates.md`) |
| `FieldError` | An invalid lookup, or `only()`/`defer()` conflicting with `select_related` | The message lists the valid choices; re-read the `__` lookup chain |
| `RelatedObjectDoesNotExist` | A nullable FK that is NULL, or a reverse OneToOne with no row | `getattr(obj, "profile", None)`; the class also catches as `Model.DoesNotExist` |
| `MultipleObjectsReturned` | `get()` matched more than one row — a uniqueness constraint is missing | Add the `UniqueConstraint`, then decide whether the caller wanted `filter().first()` |
| `SuspiciousFileOperation` | A generated path escaped the storage root | Never build `upload_to` or a storage name from raw user input (→ `references/security.md`) |
| `InconsistentMigrationHistory` | A migration is recorded as applied before a dependency it needs | Usually a late user-model swap or a re-pointed FK; repair the graph, do not `--fake` blindly (→ `references/migrations.md`) |
| `OperationalError: database is locked` | SQLite with concurrent writers | SQLite serializes writes; raise `timeout` in `DATABASES["default"]["OPTIONS"]`, or move to Postgres for anything concurrent |

## HTTP Symptoms

| Response | Usual cause |
|---|---|
| 400 on everything after `DEBUG=False` | `ALLOWED_HOSTS` empty or missing this host |
| 403 "CSRF verification failed" | No `{% csrf_token %}`; a cross-origin POST needing `CSRF_TRUSTED_ORIGINS` entries with the scheme (`https://app.example.com`, required since Django >=4.0); or `CSRF_COOKIE_SECURE` on a plain-HTTP origin |
| 404 on a URL that exists | Trailing-slash mismatch, `include()` ordering, or a path converter rejecting the value |
| 301 loop | `SECURE_SSL_REDIRECT` behind a TLS-terminating proxy with no `SECURE_PROXY_SSL_HEADER` |
| 302 to `/accounts/login/` from an API client | `LoginRequiredMixin` on an endpoint that should answer 401/403 — use DRF permissions instead (→ `references/drf.md`) |
| A POST arrives as a GET with no data | `APPEND_SLASH`: Django answers a slash-less POST with a 301 and the body is dropped. Post to the exact URL |
| 500, blank body, nothing logged | `DEBUG=False` with default logging — Django mails `ADMINS` and writes nothing else (→ `references/settings.md`) |
| 502/504 under load, fine when idle | Worker saturation, or a request longer than the proxy timeout (→ `references/deployment.md`) |
| Users randomly logged out | `SECRET_KEY` differs between instances, or was rotated without `SECRET_KEY_FALLBACKS` (Django >=4.1) |

## Settings Defaults That Bite

Exact Django defaults that produce confusing failures. All are overridable in settings.

| Setting | Default | What the default costs you |
|---|---|---|
| `DATA_UPLOAD_MAX_MEMORY_SIZE` | 2621440 bytes (2.5 MB) | A non-file POST body above it raises `RequestDataTooBig` — hits large JSON payloads and long text fields |
| `DATA_UPLOAD_MAX_NUMBER_FIELDS` | 1000 | `TooManyFieldsSent` on large formsets. A formset posts `forms × fields_per_form + 4` management inputs, so 1000 caps you near 200 forms of 5 fields |
| `FILE_UPLOAD_MAX_MEMORY_SIZE` | 2621440 bytes (2.5 MB) | Below it an upload is an in-memory object with no `temporary_file_path()`; above it, a temp file on disk. Code that assumes one shape breaks on the other |
| `CONN_MAX_AGE` | 0 | A fresh TCP connect plus auth handshake on every single request |
| `CACHES["default"]["TIMEOUT"]` | 300 seconds | Anything cached without an explicit timeout expires in five minutes |
| `LocMemCache` `MAX_ENTRIES` | 300, with `CULL_FREQUENCY` 3 | At 300 keys it evicts one third at random — and each worker process holds its own copy, which is why hit rates look impossible (→ `references/performance.md`) |
| `SESSION_COOKIE_AGE` | 1209600 seconds (14 days) | Sessions live two weeks and the `django_session` table grows forever unless `clearsessions` runs on a schedule |
| `PASSWORD_RESET_TIMEOUT` | 259200 seconds (3 days) | Reset links stay valid for three days |
| Formset `max_num` | 1000, with `absolute_max` = `max_num + 1000` | A crafted POST can force Django to build up to `absolute_max` forms before validation runs |
| `DEFAULT_AUTO_FIELD` | unset → `models.W042` | Every app gets a 32-bit `AutoField` and the system check nags; set `BigAutoField` project-wide |
| `DEBUG` | `False` | Right for production, and the one default people expect backwards: with `DEBUG=True` Django appends every query to `connection.queries` forever, so a long-running dev process grows without bound |

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| django_version | number (4.2-6.x) | 5.2 | Which `Django >=X.Y` gated advice applies when the project's version is unknown, and which deprecations to flag |
| database | postgres \| mysql \| sqlite \| oracle | postgres | Switches ORM and migration advice: `select_for_update` options, server-side cursors, JSON lookups, whether `__date` needs loaded timezone tables |
| api_layer | none \| drf \| ninja \| plain-json | drf | Which request/response idiom generated endpoints use, and whether `references/drf.md` guidance applies at all |
| settings_layout | single \| split-by-env \| env-vars | split-by-env | Where a new setting is written and how secrets are read (→ `references/settings.md`) |
| project_layout | flat \| apps-package | flat | Where a new app is created and which dotted names appear in `INSTALLED_APPS` and `AppConfig.name` (→ `references/layout.md`) |
| task_queue | none \| celery \| rq \| django-tasks | celery | Shape of background-job examples; with `none`, work is inlined behind `transaction.on_commit` instead (→ `references/tasks.md`) |
| test_runner | django \| pytest-django | django | Whether tests are emitted as `TestCase` classes or pytest functions with fixtures (→ `references/testing.md`) |
| deploy_target | gunicorn-wsgi \| uvicorn-asgi \| paas \| serverless | gunicorn-wsgi | Worker-count formula, static-file strategy, and whether long-lived database connections are safe (→ `references/deployment.md`) |
| destructive_confirm | bool | true | `migrate --fake`, `flush`, `sqlflush`, reverse migrations and drop-column operations are emitted for review instead of run |

Preference areas — customizable dimensions; record a stated preference in `<state_root>/config.yaml` and apply it from then on:

- **Tooling** — dependency manager and venv layout, debug toolbar vs profiler, `django-filter`/`factory_boy`/`allauth` and friends, migration linting in CI
- **Thresholds** — query budget per view, default page size, cache TTLs, backfill batch size, the slow-request threshold worth reporting
- **Conventions** — fat models vs a service layer, URL and view naming, `related_name` style, serializer naming, app naming style
- **Platform** — database engine and version, cache and broker backends, media storage backend, hosting target, Python version floor
- **Risk posture** — whether migrations may be applied directly, whether raw SQL is allowed, how hard to push back on `fields = "__all__"` and `@csrf_exempt`
- **Output format** — whole files vs diffs, how much explanation ships with generated code, type hints and docstrings
- **Work order** — test-first vs code-first, whether a migration review gate precedes merge, when `check --deploy` runs
- **Integrations** — auth provider and SSO, email and payment providers, error tracking, broker choice, object storage
- **Restrictions** — banned packages, LTS-only policy, PII fields that must never be logged, compliance regimes requiring audit trails
- **Cadence** — dependency and security upgrade rhythm, LTS upgrade window, session and log cleanup schedules

## Output Gates

Before emitting models, a migration, a view, or a serializer:

- Does every view that lists related data declare its query budget, with `select_related`/`prefetch_related` to match (Rule 1)?
- Does the migration touch a live table, and if so, is it split expand → backfill → contract (Rule 6)?
- Is every external side effect wrapped in `transaction.on_commit` (Rule 5)?
- Do new foreign keys and frequently filtered columns get an index in the same migration?
- Are `ModelForm` and `ModelSerializer` field lists explicit, never `"__all__"`?
- Does every object fetched by an ID from the request also filter on ownership or permission (→ `references/security.md`)?
- Are user-supplied strings rendered without `|safe`/`mark_safe`, and JSON handed to scripts through `{{ data|json_script:"id" }}`?
- Timestamps via `timezone.now()` / `timezone.localdate()`, never `datetime.now()` / `date.today()`?
