# Traps and Disputes

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Assuming `Model.save()` validates | `save()` bypasses `full_clean()`: `choices`, validators and most `max_length` checks are form-layer only | Enforce in the database with `Meta.constraints`, or call `full_clean()` explicitly |
| `null=True` on a text field | Two empty states (`""` and `NULL`) that every query then has to handle | `blank=True` alone; keep `null=True` for non-text columns |
| `Meta.ordering` on a busy model | Every query inherits the sort — and in `values().annotate()` the ordering column silently joins the `GROUP BY`, changing your aggregate | Order at the queryset; `.order_by()` with no arguments clears an inherited sort |
| `exclude(field=None)` to find NULLs | Compiles to `NOT (field = NULL)`, which drops NULL rows instead of selecting them | `filter(field__isnull=True)` |
| `queryset.delete()` over millions of rows | Django loads the objects to cascade and fire signals in Python | Delete in primary-key batches, or move the cascade into the database and own it there |
| `get_object_or_404(Order, pk=pk)` in a user-facing view | Any authenticated user can read any ID | Scope the lookup: `get_object_or_404(Order, pk=pk, user=request.user)` |
| `fields = "__all__"` on a ModelForm or ModelSerializer | Every future field becomes exposed and writable the day it is added | List fields explicitly and let that list be the review surface |
| `@login_required` on a class-based view | The decorator wraps the class object, not the request handler | `LoginRequiredMixin` first in the bases, or `method_decorator` on `dispatch` |
| Signals carrying business logic | They fire from anywhere, are invisible at the call site, and never run for `update()`/`bulk_create()` | An explicit service function; keep signals for cross-app decoupling you actually need |
| `datetime.now()` in models or views | Naive local time; with `USE_TZ=True` (the default in Django >=5.0) you get a `RuntimeWarning` and drifted comparisons | `timezone.now()`, and `timezone.localdate()` for "today" |
| `.raw()` or `.extra()` built with f-strings | String interpolation is SQL injection regardless of the ORM around it | Bind parameters: `.raw("... WHERE id = %s", [pk])` |
| Reading `request.body` twice | The stream is consumed; the second read returns `b""` | Read once into a local, or use `request.POST` for form encodings |
| Leaving sessions to grow | The `django_session` table has no automatic cleanup | `manage.py clearsessions` on a schedule, or a cache-backed session engine |


## Where Experts Disagree

- **Fat models vs a service layer.** Model methods keep behavior next to the data and make the shell powerful; a service layer keeps transactions, side effects and orchestration in one readable place. The testable boundary: anything that spans two aggregates or touches the outside world (payments, email, tasks) belongs in a service, because that is precisely what has to be wrapped in `atomic()` and `on_commit`.
- **Signals.** One camp bans them as action at a distance; the other keeps them for genuine cross-app decoupling. Both agree they are the wrong tool inside a single app, and both concede they never fire for queryset-level writes — so a signal can never be the only enforcement of an invariant.
- **DRF vs plain views for JSON.** DRF earns its weight when you need content negotiation, browsable docs, permissions and pagination as policy; for a handful of endpoints it is a large surface to reason about. Boundary: a public API or more than a few endpoints → DRF or Ninja; three internal endpoints → `JsonResponse` with explicit validation.
- **Async Django.** Async views pay off for I/O fan-out (several outbound HTTP calls per request); they buy little where the request time is ORM queries, since that path still crosses a thread. Adopt per view, not per project (→ `references/async.md`).
- **UUID vs bigint primary keys.** UUIDs stop enumeration and let clients mint IDs offline; random v4 fragments the index and widens every foreign key. Common ground: exposing a sequential ID is only a problem when authorization is missing — the check protects the row, not the shape of the key.
