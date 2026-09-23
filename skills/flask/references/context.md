# Application and request context

## Application context

- `current_app` and `g` require an active application context.
- Request handling pushes both application and request contexts automatically.
- Outside a request (CLI, job runner, shell script): use `with app.app_context():` or pass concrete values instead of proxies.
- `g` is request-scoped storage (connection handles, per-request flags). It is cleared when the request ends—use a real cache/store for process-wide data.

## Request context

- `request` and `session` require a request context.
- Tests: the Flask test client pushes contexts for you; non-request unit code can use `with app.test_request_context(...):`.
- Absolute URLs: `url_for('static', filename='x', _external=True)` needs a request context (or explicit `SERVER_NAME` / preferred URL scheme configuration).

## Background work

- Capture plain values in the request; reopen a fresh app context on another thread instead of reusing proxies.
- Preferred pattern: extract IDs/payloads in the request, enqueue plain data, reopen app context (and a new DB session) in the worker.
- Example:

```python
def send_invoice(app, invoice_id: int) -> None:
    with app.app_context():
        invoice = Invoice.query.get(invoice_id)
        ...
```
