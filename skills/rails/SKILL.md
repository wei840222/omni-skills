---
name: rails
description: Write reliable Ruby on Rails applications. Trigger this skill when writing controllers, working with ActiveRecord, setting up routes, or implementing background jobs.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🛤️","requires":{"bins":["rails"]},"os":["linux","darwin","win32"],"displayName":"Rails"}'
  related-skills: '{"ruby":"Language-level Ruby traps outside Rails APIs","backend":"General backend service design beyond the Rails stack","web":"Front-end HTML/CSS/JS work adjacent to Rails views","security-best-practices":"Cross-stack security review beyond Rails-specific traps"}'
---

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| N+1, callbacks, validations, scopes | `references/activerecord.md` | Writing models, queries, or database logic |
| Strong params, filters, render | `references/controllers.md` | Handling requests, params, and responses |
| Route conflicts, constraints | `references/routing.md` | Modifying `config/routes.rb` |
| Partials, helpers, caching, XSS | `references/views.md` | Writing ERB templates and view helpers |
| ActiveJob, Sidekiq, retries | `references/jobs.md` | Creating or modifying background jobs |
| Mass assignment, CSRF, SQL injection | `references/security.md` | Reviewing authentication or data security |
| Tech stack & Best practices | `references/tech.md` | Seeking advice on the Rails ecosystem |

## Critical Rules

- `save` returns false on failure. Use `save!` to raise exceptions, or explicitly check the return value.
- `update_all`/`delete_all` skip callbacks and validations. Verify data integrity before using them.
- Use `find_each` for batch processing. `Model.all.each` loads the entire table into memory and exhausts resources.
- `redirect_to` continues execution. Add `and return` to halt the action immediately.
- Define `dependent: :destroy` on associations to prevent orphan records from accumulating.
- Use explicit scopes (e.g., `scope :active`) instead of `default_scope`. Default scopes pollute all queries, including joins.
- Callbacks fail silently if not handled. Use `throw :abort` to stop a save and return false safely.
- Chain `includes` with `references` when referencing associated tables in `where` conditions to prevent N+1 queries.
- `||=` caches nil or false. Use `defined?(@var) ? @var : @var = compute` to correctly memoize falsey values.
- Prefer `has_many through:` over `has_and_belongs_to_many` to gain a distinct join model for tracking attributes.
- Keep `before_action` flat in controllers to maintain a readable execution flow instead of nesting them.
- `render` continues execution. Ensure only a single render or redirect occurs per action to prevent crashes.

## State location

This skill is stateless and does not store local configuration or state.
