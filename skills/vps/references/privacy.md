# Security and privacy

**Credentials.** This skill works with SSH and provider consoles. Do not store, log, copy, or transmit private keys, passphrases, root passwords, or provider API tokens into `<state_root>/` or the skill package. Store pointers only (`file:…`, `keychain:…`, `1password:…`, `env:…`).

**Local storage.** Host inventory, provider account *names*, exposure maps, spend history, and runbooks stay on the machine under the resolved state root and shared inventories — hostnames, addresses, plan names, and prices only.

**Guardrails.** Commands are read-only by default. Rebuild, destroy, disk growth, address release, snapshot deletion, and firewall enable are presented with blast radius and fallback path, and require explicit confirmation before running.
