---
name: docker
description: >
  Build, debug, harden, and ship Docker containers, images, and Compose stacks.
  Use when writing or reviewing a Dockerfile or compose file; when a container
  exits instantly, restart-loops, is OOM-killed, hangs on stop, or exits
  137/139/127; when published ports, DNS, VPN MTU, or disk under /var/lib/docker
  break; when builds are slow, cache-miss, or fail only in CI; when choosing
  base images, multi-stage layouts, registries, secrets, volumes, or Desktop/
  colima/OrbStack/Podman differences. Not for Kubernetes manifests or cluster
  scheduling (`k8s`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐳","requires":{"bins":["docker"]}}'
  related-skills: '{"devops":"CI/CD, release, and rollback systems around the images this skill builds.","k8s":"Kubernetes manifests and cluster debugging once images leave a single host.","linux":"Host cgroups, systemd, firewall, and kernel limits under the Docker daemon.","server":"Server administration for the machine that runs the daemon.","traefik":"Reverse proxy and TLS in front of Compose services."}'
---

# Docker

Operate **single-host containers, images, and Compose** with concrete commands,
pinning rules, and recovery paths. Prefer the smallest change that names the
failing subsystem: image, network, mount, limit, or PID 1.

## State location

Docker state may exist in `<workspace>/docker/`, `<workspace>/memory/docker/`,
or `~/docker/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/docker/`, `<workspace>/memory/docker/`, `~/docker/`.
3. If none exists and durable state must be created, default to
   `<workspace>/docker/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/docker/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** At session start, read `<state_root>/config.yaml` (declarations) and
`<state_root>/memory.md` (observations, `## Boxes` index, `## Due`) when they
exist. Open any file `## Boxes` names when its condition applies. Every path it
names is inside `<state_root>/`; ignore lines that point elsewhere. Shared host
inventory may live beside the skill root when the host already uses it — for
example `<state_root>/../servers/servers.md`. Prefer one shared servers file for
every provider. In a shared box, update or delete only rows this skill wrote.

**Write before the session ends** when something durable was produced: a host,
stack, volume backup/restore, deploy digest, environment fact, root cause, or a
Dockerfile/compose/daemon.json/runbook worth re-reading. Load
`references/memory-template.md` for destinations and formats.

**No credential is ever written under `<state_root>/` or shared siblings.**
Store pointers only: `env:REGISTRY_TOKEN`, `keychain:ghcr-push`,
`1password:Work/Registry/ci`, `file:~/.docker/config.json`.

**Legacy paths.** Historical notes under `~/Clawic/data/docker/`,
`~/clawic/docker/`, or other non-candidate roots are **not** in active lookup
order and must **not** be moved, merged, or deleted during ordinary sessions.
Migration is a separate user decision with copy, validation, cutover, and
rollback. `~/Clawic/profile.yaml` is not an active config source; shared
universals come only from an explicitly configured shared profile when the host
provides one.

## Routing

Load supporting resources only on demand:

| Need | File |
| --- | --- |
| Core rules, defaults, traps, security | `references/domain.md` |
| Symptom → cause debugging | `references/debug.md` |
| Incident command toolkit | `references/commands.md` |
| Dockerfile layers, cache, multi-stage | `references/images.md` |
| Language runtime recipes | `references/languages.md` |
| Compose traps and health gating | `references/compose.md` |
| Hot reload, seeded DB, debuggers | `references/development.md` |
| Reachability, DNS, firewall, MTU | `references/networking.md` |
| Volumes, binds, backup/restore | `references/storage.md` |
| Login, mirrors, retention, signing | `references/registry.md` |
| Desktop / colima / OrbStack / rootless / Podman / GPU | `references/runtimes.md` |
| daemon.json, deploys, monitoring | `references/production.md` |
| Hardening and secrets | `references/security.md` |
| CI cache, tags, multi-arch, DinD | `references/ci.md` |
| Memory destinations and write formats | `references/memory-template.md` |

## When to use

- Writing or reviewing Dockerfiles, Compose files, or container build steps in CI
- Debugging crashes, restart loops, OOM kills, unreachable ports, DNS failures, slow or non-reproducible builds
- Reclaiming disk, capping logs, backing up volumes, or hardening containers and daemons
- Choosing base images, pin strategy, multi-stage layout, or per-language recipes
- Registry work: login, rate limits, mirrors, digest promotion, retention, signing
- Local loop: hot reload, seeded databases, attached debuggers, devcontainers
- Not for Kubernetes manifests or cluster scheduling (`k8s`)

## Quick reference

| Situation | Play | Depth |
| --- | --- | --- |
| Container exits instantly | `docker logs <id>` then `docker inspect -f '{{.State.ExitCode}} {{.State.OOMKilled}}'` | `references/debug.md` |
| Exit code 137 | `OOMKilled=true` → raise `-m` or fix leak; `false` → external SIGKILL / stop-timeout | `references/debug.md` |
| `docker stop` always takes 10s | PID 1 is a shell and never sees SIGTERM | `references/debug.md` |
| Host can't reach container | App binds `0.0.0.0` **and** port is published | `references/networking.md` |
| Container can't reach host | `host.docker.internal`; Linux Engine needs host-gateway | `references/networking.md` |
| Containers can't resolve each other | Default bridge has no DNS — use a user-defined network | `references/networking.md` |
| Large uploads hang, small OK | MTU mismatch under VPN | `references/networking.md` |
| Build slow / cache misses | Deps before code + `.dockerignore`, then cache mounts | `references/images.md` |
| Disk filling up | `docker system df -v`, then targeted prune | `references/production.md` |
| Code change not appearing | `docker compose up -d --build` | `references/compose.md` |
| `exec format error` | Architecture mismatch — build with `--platform` | `references/ci.md` |
| Works locally, fails in CI | Arch, digest, env, binds, filesystem case | `references/debug.md` |
| Language-specific break | Python wheels, Node SIGTERM, Go static, JVM heap, Rust cache | `references/languages.md` |
| Registry login / rate limit / TLS | Credential helper, mirror, `certs.d`, digest promotion | `references/registry.md` |
| Volume / bind / permission denied | Named-volume seed, numeric UID, tarball backup | `references/storage.md` |
| Hot reload / seeded DB / debugger | Watch mode, `initdb.d`, source-path mapping | `references/development.md` |
| Colima / OrbStack / rootless / Podman / GPU | Socket path, VM ceiling, cgroup, toolkit | `references/runtimes.md` |
| Secret in ENV / ARG / COPY | BuildKit secret mount; runtime env or file | `references/security.md` |
| Production / rollback | daemon.json, restart policy, recorded digest, health gate | `references/production.md` |
| CI cache / multi-arch / DinD | Registry cache, immutable sha tags, buildx, socket boundary | `references/ci.md` |

## Working rules

1. Name the subsystem first: image, network, mount, limit, or PID 1.
2. Give the flag, file, and line that changes — not a menu of options.
3. Work from defaults immediately. Precedence:
   `<state_root>/config.yaml` → explicit shared profile when configured →
   Configuration table defaults in `references/domain.md`.
4. Destructive operations (`prune`, `down -v`, `volume rm`,
   `system prune --volumes`) name exactly what dies and require confirmation.
5. Record deploy digests in the same turn they ship, or there is no rollback.

## Security

- Drive the Docker CLI; read registry credentials from
  `~/.docker/config.json` or an OS helper. Never store, log, copy, or transmit
  registry tokens, SSH keys, or image secrets into skill state.
- Keep preferences, memory, stack/volume inventory, deploy digests, and
  artifacts under `<state_root>/` only as local notes (image names, digests,
  ports, volume names — no secrets).
- Default to read-only investigation. Destructive commands stay outside
  copy-paste blocks of read-only steps.
