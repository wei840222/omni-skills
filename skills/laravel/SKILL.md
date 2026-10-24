---
name: laravel
description: "Apply Laravel framework best practices. Use when developing or reviewing controllers, Eloquent models, Blade templates, queues, Artisan commands, or authentication to avoid common framework pitfalls."
metadata:
  openclaw: '{"emoji":"🔴","requires":{"bins":["php","composer"]}}'
  related-skills: '{"api": "HTTP API design patterns often paired with Laravel controllers.", "auth": "Cross-framework authentication concepts used with guards and policies.", "backend": "General backend service design beyond the Laravel stack.", "docker": "Containerized local stacks commonly used with Laravel Sail.", "php": "Core PHP language patterns that Laravel builds on."}'
---

## When to load

Load this skill when writing or reviewing Laravel application code — controllers, Eloquent models, Blade views, queues, Artisan commands, middleware, or authentication — and you need concrete trap avoidance rather than generic PHP advice.

## Critical Rules

- Eager load relationships — `with('posts')` not lazy `->posts` in loop (N+1)
- `preventLazyLoading()` in dev AppServiceProvider — crashes on N+1, catches early
- `env()` only in config files — returns null after `config:cache`
- `$fillable` whitelist fields — `$guarded = []` allows mass assignment attacks
- `find()` returns null — use `findOrFail()` to enforce presence without manual null checks
- Job properties serialize models as ID — re-fetched on process, may be stale/deleted
- `route:cache` requires controller routes — closures break cached routes
- `DB::transaction()` doesn't catch `exit`/timeout — only exceptions roll back
- `RefreshDatabase` uses transactions — faster than `DatabaseMigrations`
- `{!! $html !!}` skips escaping — XSS vector, use `{{ }}` by default
- Middleware order matters — earlier middleware wraps later execution
- `required` validation passes empty string — use `required|filled` for content
- `firstOrCreate` persists immediately — `firstOrNew` returns unsaved model
- Route model binding uses `id` — override `getRouteKeyName()` for slug

## Progressive disclosure

Load only the reference that matches the current task:

| Topic | File |
|-------|------|
| N+1 queries, eager loading, accessors, observers | `references/eloquent.md` |
| Validation, middleware order, dependency injection | `references/controllers.md` |
| Job serialization, retries, failed jobs | `references/queues.md` |
| Guards, policies, gates, Sanctum tokens | `references/auth.md` |
| XSS escaping, components, slots | `references/blade.md` |
| Commands, scheduling, tinker | `references/artisan.md` |

## Requirements

- `php` and `composer` available on the target machine when executing Laravel tooling.
- Prefer official Laravel docs for version-specific behavior; treat framework defaults as live surface.
