# Django Domain Knowledge and Sources

## Claim inventory and freshness

| Topic | Freshness | Source of truth | Refactor outcome |
| --- | --- | --- | --- |
| Async ORM behavior and transactions | Version-sensitive | Django async documentation | Retained the async-reference routing and clarified that transaction-sensitive work remains synchronous. |
| Query loading, aggregation, and `select_for_update()` | Version-sensitive | Django queryset reference | Retained ORM guidance and its explicit query-budget checks. |
| Migrations and live-schema changes | Version-sensitive | Django migration documentation | Retained the expand → backfill → contract recovery path. |
| Deployment security checks | Version-sensitive | Django deployment checklist | Retained `check --deploy` as a production-settings verification gate. |
| Core design principles | Stable domain | Django overview | Kept the framework, ORM, template, and admin focus; removed no operational guidance. |

## Verified sources

### Official Django documentation

- **Asynchronous support** — async views can use async ORM methods for many queries, but transactions do not yet work in async mode; keep transaction-sensitive work in a synchronous function called with `sync_to_async()`. <https://docs.djangoproject.com/en/5.2/topics/async/>
- **QuerySet API reference** — documents `select_related()`, `prefetch_related()`, aggregation behavior, and `select_for_update()` semantics used by the ORM guidance. <https://docs.djangoproject.com/en/5.2/ref/models/querysets/>
- **Database transactions** — documents `atomic()`, savepoints, and `on_commit()` behavior behind the side-effect and recovery guidance. <https://docs.djangoproject.com/en/5.2/topics/db/transactions/>
- **Migrations** — documents migration workflow, consistency, and deployment constraints. <https://docs.djangoproject.com/en/5.2/topics/migrations/>
- **Deployment checklist** — documents `manage.py check --deploy` and the production hardening checks. <https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/>
- **Django overview** — confirms Django’s maintained framework scope and its ORM, template, and admin components. <https://docs.djangoproject.com/en/5.2/intro/overview/>

## Update notes

- This skill routes detailed, conditional material through `references/` while preserving the original Django-specific operational guidance.
- For a claim whose behavior differs by installed Django version, inspect the project’s declared version before applying version-gated advice.
