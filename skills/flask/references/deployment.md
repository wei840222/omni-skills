# Debug mode and production deployment

## Debug mode

- `app.run(debug=True)` or `FLASK_DEBUG=1` enables the interactive debugger—**remote code execution** if exposed.
- Run shared, staged, and production processes with debug disabled.
- Drive development with the `FLASK_DEBUG` environment variable rather than hard-coding `debug=True` in committed entrypoints.
- Debug PIN in logs is an extra hurdle only—not a production control.

## Servers

| Environment | Server |
|-------------|--------|
| Local dev | `flask run` / Werkzeug development server |
| Production | Gunicorn, uWSGI, or another production WSGI server |
| Concurrency on dev server | `threaded=True` still is not production-ready |

## Production checklist

- Reverse-proxy static files (nginx/Caddy); prefer the proxy for static assets under load.
- Set `PROPAGATE_EXCEPTIONS` deliberately when an error tracker needs the original exception.
- Configure proxy fix / `PREFERRED_URL_SCHEME` / `SESSION_COOKIE_SECURE` behind TLS terminators.
- Run multiple workers; share session/backend state explicitly (cookie signing key + any server-side store).
- Health checks and graceful timeout settings belong on the WSGI server, not `app.run`.
