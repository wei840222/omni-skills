# Common request/response mistakes

| Mistake | Do instead |
|---------|------------|
| `return redirect('/login')` | `return redirect(url_for('auth.login'))` — survives blueprint prefixes and mount points |
| `return json.dumps(data)` | `return jsonify(data)` — correct content type and app JSON provider |
| Read JSON from `request.form` | Use `request.get_json(silent=True)` / `request.json` for JSON bodies |
| Query params via ad-hoc parsing | `request.args.get("page", default=1, type=int)` |
| Mutate nested `session["cart"]["x"]` in place | Reassign the top-level key or set `session.modified = True` |
| Serve production with `flask run` | Gunicorn/uWSGI (see `deployment.md`) |
