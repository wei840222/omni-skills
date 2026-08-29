# Ansible Core Rules

## Prefer Idempotent Modules

- Use purpose-built modules (`apt`, `yum`, `dnf`, `copy`, `template`, `file`, `service`, `systemd`) instead of `command`/`shell` whenever a module exists.
- If `command`/`shell` is unavoidable, add `creates:` / `removes:` or an explicit `changed_when:` so reruns stay stable.
- Use `changed_when: false` only for read-only queries that must never report `changed`.

## YAML and Jinja2 Boundaries

- Quote values that contain Jinja2: `msg: "{{ variable }}"`.
- Quote strings that contain `:`, and quote literal `yes`/`no`/`true`/`false` when they must remain strings.
- Indent with spaces only (2-space Ansible convention); tabs are invalid.

## Conditionals

- Write `when:` without Jinja2 braces: `when: ansible_os_family == "Debian"`.
- Combine conditions with `and` / `or`, or use a YAML list for implicit `and`.
- Test optional values with `is defined` / `is not defined`.
- Evaluate booleans directly: `when: my_bool` — do not compare `== true`.

## Variable Precedence (Practical Order)

From lower to higher influence in common playbook work:

1. Inventory group/host vars
2. Play `vars:`
3. Extra vars (`-e`) — highest and overrides almost everything

Prefer more specific host vars over broad group vars. Use `{{ var | default('fallback') }}` when absence is allowed.

## Handlers

- Handlers run only when a notifying task reports `changed`.
- Handlers are deduplicated and normally flush at end of play.
- Use `meta: flush_handlers` to flush early; use `--force-handlers` only when failure must still flush handlers.

## Privilege Escalation

- `become: true` escalates; set `become_user:` when the target is not root.
- Default method is usually `sudo`; override with `become_method` only when required.
- Some tasks still need task-level `become` even if the play already sets it.
- Supply the become password via `--ask-become-pass` or configured vault/password mechanisms — never hard-code it in the playbook.

## Facts and Delegation

- `gather_facts: false` speeds runs but removes `ansible_*` facts.
- Fact caching (`fact_caching`) can reuse facts across plays/runs when configured.
- Custom facts under `/etc/ansible/facts.d/*.fact` appear under `ansible_local`.
- Prefer `delegate_to: localhost` for controller-side work; treat `local_action` as legacy shorthand.
