# Factory pattern and circular imports

## Factory pattern

```python
def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(config_object or "config.ProdConfig")
    db.init_app(app)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
```

- Import `current_app` inside view/model helpers instead of importing a global `app`.
- Register blueprints and bind extensions **inside** the factory, not at import time of extension modules.

## Circular imports

| Failure | Fix |
|---------|-----|
| `models.py` does `from app import app` while `app` imports models | Factory + `current_app`; models import `db` extension only |
| Blueprint module imports app at top level | Register blueprint in factory; blueprint imports `current_app` lazily |
| Extension needs app at construction | `ext = SQLAlchemy()` then `ext.init_app(app)` |

## Late binding

- Import inside the function when two modules must reference each other.
- Prefer explicit app factories in tests so each test gets a clean app/config.
