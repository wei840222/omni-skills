# Research sources (Gate 6)

Retrieved 2026-10-03 during handoff of Jules session `4441104395363954677`. Prefer re-fetching the official pages before asserting version-floor or provider-major behavior.

## Agent Skills format

- **Agent Skills specification** — frontmatter shape, progressive disclosure, resource directories.
  https://agentskills.io/specification
- **Agent Skills llms.txt index** — document discovery entrypoint.
  https://agentskills.io/llms.txt

## Core language and CLI

- **Resource syntax** — resource blocks and configuration surface.
  https://developer.hashicorp.com/terraform/language/block/resource
- **Modules** — module composition and calling conventions.
  https://developer.hashicorp.com/terraform/language/modules
- **Plan command** — saved plans, review-before-apply contract.
  https://developer.hashicorp.com/terraform/cli/commands/plan
- **Terraform settings block** — `required_version` / `required_providers`.
  https://developer.hashicorp.com/terraform/language/block/terraform
- **`for` expressions** — expression language used by `for_each` patterns.
  https://developer.hashicorp.com/terraform/language/expressions/for
- **Functions index** — built-in functions referenced from expression guidance.
  https://developer.hashicorp.com/terraform/language/functions

## State, backends, workspaces

- **State overview** — purpose of state and remote backends.
  https://developer.hashicorp.com/terraform/language/state
- **Backend configuration** — partial configuration and backend constraints.
  https://developer.hashicorp.com/terraform/language/settings/backends/configuration
- **Workspaces** — CLI workspace model and isolation limits.
  https://developer.hashicorp.com/terraform/language/state/workspaces
- **`state mv`** — out-of-band address moves when declarative blocks are unavailable.
  https://developer.hashicorp.com/terraform/cli/commands/state/mv
- **`force-unlock`** — lock recovery after a dead holder.
  https://developer.hashicorp.com/terraform/cli/commands/force-unlock

## Refactor / lifecycle / import

- **`moved` blocks** — declarative renames across applies.
  https://developer.hashicorp.com/terraform/language/block/moved
- **`import` blocks** — bring existing objects under management.
  https://developer.hashicorp.com/terraform/language/import
- **`removed` blocks** — stop managing without always destroying.
  https://developer.hashicorp.com/terraform/language/block/removed
- **Lifecycle meta-arguments** — `create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`.
  https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle

## Secrets, tests, providers

- **Manage sensitive data** — sensitivity vs real state exposure.
  https://developer.hashicorp.com/terraform/language/manage-sensitive-data
- **Ephemeral values / resources** — reduce long-lived secret material in state (Terraform line).
  https://developer.hashicorp.com/terraform/language/manage-sensitive-data/ephemeral
- **Sensitive variables tutorial** — practical masking behavior.
  https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables
- **Tests (`.tftest.hcl`)** — `terraform test` workflow.
  https://developer.hashicorp.com/terraform/language/tests
- **Check blocks** — continuous assertions in config.
  https://developer.hashicorp.com/terraform/language/block/check
- **`providers lock`** — multi-platform lock file generation.
  https://developer.hashicorp.com/terraform/cli/commands/providers/lock
- **AWS provider 4.x upgrade guide** — canonical resource-split major-upgrade pattern cited in upgrades guidance.
  https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-4-upgrade

## OpenTofu

- **OpenTofu intro** — fork posture and drop-in expectations.
  https://opentofu.org/docs/intro/
- **OpenTofu state encryption** — native encryption feature that diverges from Terraform.
  https://opentofu.org/docs/language/state/encryption/
- **OpenTofu CLI commands** — command surface parity checks.
  https://opentofu.org/docs/cli/commands/
- **OpenTofu CHANGELOG** — version-floor verification for post-1.6 features.
  https://github.com/opentofu/opentofu/blob/main/CHANGELOG.md

## Obsolete / corrected packaging claims

| Old packaging claim | Correction | Source |
|---|---|---|
| Homepage / feedback pointed at clawic.com; nested clawdbot metadata; `_meta.json` duplicate | Removed promo + nested metadata; OpenClaw emoji JSON string; deleted `_meta.json` | agentskills specification + project Gates 1/5 |
| Hard-coded `~/Clawic/data/terraform/` only | Portable `<state_root>` resolution with workspace-first defaults | project Gate 3 |
| Flat reference markdown at skill root | Progressive disclosure under `references/` + `assets/memory-template.md` | project Gate 2 |
| OpenTofu floors above 1.6 treated as transferable | Floors diverge; verify OpenTofu changelog / native encryption docs | OpenTofu intro + state encryption + CHANGELOG |
