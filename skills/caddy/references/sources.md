# Gate 6 sources (verified at handoff)

Primary documentation used to check automatic HTTPS, Caddyfile, reverse_proxy, CLI, and storage claims. Re-open the live page before restating endpoints or defaults.

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Docs home / map | Caddy Documentation | https://caddyserver.com/docs/ | Entry points for Caddyfile, Auto HTTPS, CLI, conventions. |
| Automatic HTTPS | Automatic HTTPS | https://caddyserver.com/docs/automatic-https | Default HTTPS, HTTP→HTTPS redirect, public vs local certs, HTTP-01 / TLS-ALPN / DNS-01, on-demand TLS needs restrictions, storage persistence, staging for tests, issuer fallback. |
| Caddyfile | The Caddyfile | https://caddyserver.com/docs/caddyfile | Human config adapter; site address + directives; JSON still native under the hood. |
| reverse_proxy | reverse_proxy directive | https://caddyserver.com/docs/caddyfile/directives/reverse_proxy | Upstreams, default random LB, active/passive health, header_up/down, transports, streaming knobs. |
| CLI | Command Line | https://caddyserver.com/docs/command-line | `validate`, `fmt`, `reload`, `adapt`, `run`, `trust` / `untrust`, storage export/import. |
| Paths & addresses | Conventions | https://caddyserver.com/docs/conventions | Data vs config directories, XDG paths, network address forms (not URLs). |
| Container image | Docker Hub official Caddy | https://hub.docker.com/_/caddy | Common `/data` + `/config` persistence guidance for images. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/caddy`. |

## Operational notes retained (not live measurements)

- Let's Encrypt staging directory commonly used in docs: `https://acme-staging-v02.api.letsencrypt.org/directory` — confirm on the live ACME/CA page before hard-coding in production automation.
- Default LB policy name `random` and passive health field names follow the reverse_proxy directive page at handoff time.
- Exact container paths can differ for custom images; prefer the image's documented volumes when they disagree with Hub defaults.

Handoff verification date: 2026-10-02 (local takeover of Jules session 884261543295428085).
