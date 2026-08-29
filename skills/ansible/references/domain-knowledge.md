# Ansible Domain Knowledge

## What This Skill Covers

Ansible is an agentless automation engine that applies idempotent desired-state changes over SSH (or other connections) using playbooks written in YAML plus Jinja2. This skill focuses on the playbook-author traps that most often create non-idempotent runs, broken conditionals, handler surprises, and privilege-escalation failures.

## Stable Domain Facts

- YAML is the serialization layer; Jinja2 is the templating layer. Mixing their quoting rules is the root of many parse and conditional bugs.
- Idempotence is a module/contract property, not a YAML property. `command` and `shell` are escape hatches.
- Handlers are a deferred change-notification mechanism, not immediate callbacks.
- Variable precedence is layered; extra vars are an emergency override, not a default configuration channel.
- Facts are gathered inventory about the remote host; disabling fact gathering removes a large class of conditionals and templates.

## Corrected / Tightened Guidance

- Prefer `delegate_to: localhost` over legacy `local_action` when documenting controller-side tasks.
- Prefer boolean `true`/`false` in new playbooks while recognizing YAML `yes`/`no` still parse as booleans.
- Keep source citations pointed at current Ansible documentation under `docs.ansible.com/projects/ansible/latest/`.

## Sources

### Playbook semantics
- Ansible variables — precedence concepts and play/inventory/extra vars via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html
- Understanding variable precedence — layered override model via https://docs.ansible.com/projects/ansible/latest/reference_appendices/general_precedence.html
- Conditionals — `when` without Jinja2 braces via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_conditionals.html
- Handlers — notify, flush, and force-handlers behavior via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html
- Loops — `loop`, `loop_control`, and `until` via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_loops.html
- Privilege escalation — become methods and passwords via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_privilege_escalation.html
- Vars and facts — gathering and `ansible_local` custom facts via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_vars_facts.html
- Error handling — registers, ignore_errors, and failure inspection via https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_error_handling.html

### Syntax and authoring hygiene
- YAML syntax appendix — quoting and indentation pitfalls via https://docs.ansible.com/projects/ansible/latest/reference_appendices/YAMLSyntax.html
- Tips and tricks — practical playbook authoring guidance via https://docs.ansible.com/projects/ansible/latest/tips_tricks/ansible_tips_tricks.html
