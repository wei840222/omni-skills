# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| provider | text (provider name) | none | Which console paths, plan names, firewall model, and quirks every step assumes; while unset, name the assumption out loud (Core rule 8) |
| default_distro | debian \| ubuntu-lts \| rocky \| alma \| alpine \| arch | debian | Image chosen at creation and package-manager syntax in examples |
| cpu_arch | arm64 \| x86_64 \| either | either | Plan shortlist; `arm64` forces binary-compatibility check before recommendations |
| monthly_budget | number (currency from profile) | 20 | Bar for calling a plan expensive and trigger threshold for spend review |
| admin_user | text (username) | none | Non-root account in provisioning/access steps; unset → examples use `admin` as placeholder |
| ssh_port | number (1-65535) | 22 | Port used in access, firewall, and provisioning guidance |
| firewall_layer | provider \| host \| both | both | Which layer firewall guidance configures and audits |
| backup_target | provider-snapshots \| object-storage \| own-host \| none | provider-snapshots | Where backup drills send data and what the quarterly restore exercises |
| patch_window | text (weekday + hour, or `anytime`) | anytime | When reboots for kernel updates are scheduled and how overdue reboots are reported |

Preference areas — a stated preference is recorded in `config.yaml` and applied from then on:

- **Tooling** — firewall front-end (ufw, firewalld, raw nftables, provider-only), backup tool (restic, borg, rsync, provider), provisioning method (cloud-init, Ansible, shell script, by hand)
- **Conventions** — hostname scheme, private address plan, on-disk project layout, provider tags/labels
- **Platform** — preferred region vs user latency, IPv6 posture, dedicated vs shared vCPU default
- **Safety posture** — whether destructive commands are emitted at all; confirmation before rebuild/resize/address release; deletion protection when offered
- **Isolation model** — one box per project vs many projects per box; containers vs system services vs control panel
- **Data residency and compliance** — acceptable jurisdictions and excluded providers before price is considered
- **Cost reporting** — review cadence, quote currency, whether every answer carries a monthly number
