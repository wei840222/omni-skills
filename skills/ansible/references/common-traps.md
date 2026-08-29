# Ansible Common Traps

## Syntax and Quoting

- Unquoted Jinja2 in a mapping value can break YAML parsing or silently change meaning.
- Unquoted `yes` / `no` / `true` / `false` become booleans.
- Putting `"{{ ... }}"` inside `when:` is a classic conditional bug.

## Idempotence Failures

- Bare `command` / `shell` always looks changed unless guarded.
- `--check` / dry-run is incomplete for modules that cannot simulate side effects; `command` and `shell` often skip meaningful check-mode behavior.

## Handlers and Control Flow

- Expecting a handler to run immediately after `notify:` fails unless handlers are flushed.
- Multiple notifies to one handler still run it once per flush.

## Become and Auth

- Play-level `become: true` does not guarantee every nested include/role/task escalates as intended.
- Missing become password or wrong `become_method` looks like a module failure.

## Registers and Errors

- `register:` captures output even when the task failed — inspect `failed`, `rc`, or module-specific fields.
- `ignore_errors: true` continues the play but leaves the registered result failed.
- Vault-encrypted files still need `--ask-vault-pass` or a vault password file at runtime.

## Loops

- Prefer `loop:` over legacy `with_items:`.
- Nested loops need `loop_control.loop_var` to avoid `item` collisions.
- Use `loop_control.label` to keep output readable.
- Retry with `until:` / `retries` / `delay` instead of ad-hoc sleep loops.
