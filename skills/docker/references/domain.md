# Docker Domain Rules

## Core Rules

1. **Pin what you can't afford to re-debug.** Dev: minor tag (`python:3.11-slim`). Prod and CI: digest (`python@sha256:...`) — tags are mutable, digests are not. Governed by `pin_policy`. Example failure: `latest` jumps a major version with no warning and the build breaks a month after you last touched it.
2. **Order layers by change frequency.** Dependency manifest → install → source code. `COPY . .` before the install step invalidates the dependency cache on every code edit — the single largest build-time waste in real projects.
3. **`apt-get update && apt-get install -y pkg` in one RUN.** Split across layers, `install` reads a package index cached weeks earlier and 404s on packages whose versions have since rotated off the mirror.
4. **Exec-form CMD; respect PID 1.** Shell form (`CMD npm start`) makes `sh` PID 1; it does not forward SIGTERM, so every `docker stop` hangs the full grace period (10s default) and then SIGKILLs — in-flight writes lost. Use `CMD ["npm","start"]` or `--init`. Linux ignores default signal dispositions for PID 1, so a runtime that installs no SIGTERM handler (Node is the common one) hangs even in exec form (`references/languages.md`).
5. **Non-root with a numeric UID.** `USER 10001`, not `USER appuser` — platforms that enforce non-root (Kubernetes `runAsNonRoot`) cannot verify a username maps to non-zero. Place `USER` after the RUNs that need root.
6. **Memory limits: know the swap formula.** `-m 512m` alone allows swap = 2× memory, so the real ceiling is 1 GiB. Hard cap: set `--memory-swap` equal to `--memory` (`-m 512m --memory-swap 512m` = no swap). Then cap the runtime inside it at ~75% of that (`references/languages.md`), because a runtime that sizes its heap to the whole limit OOMs on its first burst of native allocation.
7. **Cap logs at run time.** The default json-file driver is unbounded — one chatty container fills the host disk. `--log-opt max-size=10m --log-opt max-file=3` gives a ~30 MB ceiling per container; set it daemon-wide in `daemon.json` so nobody forgets.
8. **Gate startup on health, not on start.** Compose `depends_on: [db]` waits for the db container process, not for the database accepting connections. Use `condition: service_healthy` plus a real healthcheck (defaults and traps in `references/compose.md`).
9. **Record the digest at deploy, or you have no rollback.** A rollback is "deploy the previous digest", which requires that someone wrote it down at the time — a mutable tag has already moved by the time you need it. Capture `docker inspect -f '{{index .RepoDigests 0}}' <image>` at deploy and write the row to `deploys/<year>.md` (`references/memory-template.md`) in the same turn. Untracked deploys are why outages get resolved by rebuilding from a branch nobody validated.

## Exit Codes

Formula: a code above 128 means killed by signal `code − 128`.

| Code | Meaning | First move |
|------|---------|-----------|
| 125 | Docker daemon error (bad flag, missing image) | Read the run command, not the app |
| 126 | File found but not executable | `chmod +x`; or the entrypoint is a directory; or CRLF line endings on the entrypoint script |
| 127 | Command not found | PATH wrong, or a glibc binary on musl (Alpine), or the shell itself is absent (distroless) |
| 137 | SIGKILL (128+9) | Check `.State.OOMKilled`; also fired by stop-timeout expiry |
| 139 | SIGSEGV (128+11) | Native crash — suspect glibc/musl or architecture mismatch |
| 143 | SIGTERM (128+15) | Clean external stop — usually not a bug |

## Defaults That Decide Behavior

Docker's defaults are tuned for a laptop demo, not for a service. Each of these has produced a production incident that reads as an application bug.

| Default | Value | Why it bites |
|---|---|---|
| Log driver | `json-file`, unbounded | One chatty container fills the host disk and hangs the daemon (Rule 7) |
| `/dev/shm` | 64 MB | Chrome/Playwright and Postgres parallel queries crash with obscure errors; `--shm-size=1g` is the fix, not more RAM |
| Stop grace period | 10s, then SIGKILL | Anything that needs longer to drain must set `--stop-timeout`/`stop_grace_period` AND actually handle SIGTERM |
| Restart backoff | 100 ms, doubling, capped at 1 min | A crash loop self-throttles; rising `RestartCount` is the alarm, not the log volume |
| Default bridge network | No embedded DNS | Container-name resolution fails; user-defined networks have it (`references/networking.md`) |
| Healthcheck | interval 30s, timeout 30s, retries 3, `start_period` 0s | A service that boots in 60s is marked unhealthy before it ever answers (`references/compose.md`) |
| Address pool | 172.17.0.0/16 onward | Collides with corporate VPN ranges; set `default-address-pools` (`references/production.md`) |
| Network MTU | 1500 | Under a VPN with a lower MTU, large payloads hang while small ones succeed (`references/networking.md`) |
| User | root | Unless the image or `USER` says otherwise (Rule 5) |
| pids limit | unlimited | One fork bomb takes the host, not the container; `pids_limit: 256` is cheap insurance |

## Disk Leaks

`/var/lib/docker` at 100% hangs the daemon itself — you cannot prune through a daemon that won't respond. Alert well before full; locate leaks with `docker system df -v`.

| Leak | Reclaim |
|------|---------|
| Dangling images | `docker image prune` |
| Build cache | `docker builder prune --keep-storage <build_cache_budget_gb>GB` |
| Stopped containers | `docker container prune`, or `--rm` at run time |
| Named volumes | `docker volume prune` — NOT touched by `system prune` without `--volumes`; destructive, confirm first |
| Orphan networks | `docker network prune` |
| A container's own writable layer | Not prunable — the app is writing inside the container instead of a volume; find it with `docker diff <c>` (`references/storage.md`) |

## Output Gates

Before emitting a Dockerfile, a Compose file, or a deploy command:

- Base image pinned to the strictness `pin_policy` requires — tag at minimum, digest if this ships to prod?
- Dependency install layered before source copy, and a `.dockerignore` present excluding `.git` and dependency directories?
- CMD/ENTRYPOINT in exec form, and does this runtime actually handle SIGTERM as PID 1?
- `USER` set with a numeric UID, or root explicitly justified?
- No secret reachable via ENV, ARG, or a COPYed file — and none written into `<state_root>/`?
- Memory limit with a matching `--memory-swap`, a log cap, and the runtime's own heap capped below the container limit?
- Compose: healthcheck defined on every service something depends on, `start_period` above worst-case boot time?
- Is the command destructive (`prune`, `down -v`, `volume rm`, `system prune --volumes`)? Then it names exactly what dies and ships with a confirmation step, must be isolated outside copy-paste blocks of read-only commands.
- Did anything durable come out of this — a host, a deploy digest, a working file, a volume, an environment fact, a root cause? Then it is written to its box in `references/memory-template.md`, with its `## Boxes` line, in this same turn.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| runtime_flavor | Desktop \| colima \| orbstack \| rootless \| podman | Desktop | Selects socket path, `host.docker.internal` behavior, VM-ceiling reasoning and default-platform assumptions; rootless and podman change port-binding, cgroup and volume-permission advice (`references/runtimes.md`) |
| default_registry | text (registry host) | docker.io | Prefixes unqualified image references; switches push/pull and mirror examples to the user's registry (`references/registry.md`) |
| base_image_family | alpine \| debian-slim \| distroless | debian-slim | Drives base-image recommendations and the Alpine-vs-slim tradeoff (musl wheels, DNS, no-shell debugging) in `references/images.md` and `references/languages.md` |
| default_platform | arm64 \| amd64 | arm64 | Sets the assumed build/run architecture; governs `--platform` reminders, multi-arch advice in `references/ci.md`, and `exec format error` diagnosis |
| pin_policy | tag \| digest-in-prod \| digest-everywhere | digest-in-prod | The strictness Rule 1 and the Output Gates enforce on every generated Dockerfile and compose file |
| hardening_profile | default \| hardened | default | `hardened` makes every generated run/compose ship `--read-only`, `--cap-drop ALL`, `no-new-privileges` and a non-root UID unprompted (`references/security.md`) |
| ci_platform | github-actions \| gitlab-ci \| jenkins \| buildkite \| none | none | Which CI dialect `references/ci.md` examples are written in, and which cache backend is recommended |
| build_cache_budget_gb | number (GB, 1-200) | 10 | The `--keep-storage` figure in every prune command and the threshold for calling build cache a disk problem |
| destructive_confirm | bool | true | Whether `prune`, `down -v` and `volume rm` are emitted behind an explicit confirmation step or inline |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — Compose vs plain `docker run`, buildx/bake vs classic build, devcontainers vs a hand-rolled dev compose file, testcontainers usage — affects which shape every example takes
- **Conventions** — tag scheme (`sha`, semver, date), image namespace and labels, `.dockerignore` habits, one-file-vs-many compose layout — affects generated files and `references/ci.md` tagging
- **Platform** — single host vs CI vs a cloud target, multi-arch need, registry mirror or pull-through cache, host OS family (SELinux hosts need `:z`/`:Z`) — affects `references/storage.md` and `references/registry.md`
- **Safety posture** — how proactively to surface production hardening, whether to emit destructive commands at all, deletion confirmations, appetite for `--privileged` escapes — affects Output Gates and `references/security.md`
- **Cadence** — prune schedule, base-image rebuild and rescan frequency, volume-restore drill, reboot drill — every accepted cadence becomes a row in the `## Due` table of `memory.md`
- **Output register** — command-first vs explanation-first, whether to show the diff of a Dockerfile or the whole file, how much of the reasoning to keep — affects every answer's shape

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Secrets via ENV, ARG, or COPY | All three persist in image history — deleting the file in a later layer does not remove the earlier layer | BuildKit `RUN --mount=type=secret`; runtime env or mounted files (`references/security.md`) |
| Mounting `/var/run/docker.sock` | Socket access = root on the host; any container escape is total | Dedicated proxy with a filtered API, or rethink the design |
| `ADD` for local files | Auto-extracts archives; URL downloads bypass the build cache | `COPY`; fetch URLs in a RUN with checksum verification |
| `docker logs` shows nothing | Only PID 1's stdout/stderr is captured — and buffered runtimes hold it until they exit | Log to stdout unbuffered (`PYTHONUNBUFFERED=1` and friends, `references/languages.md`), or symlink the logfile to `/dev/stdout` |
| No shell in distroless/slim image | Nothing to `exec` into | `docker cp` files out, or attach a sidecar sharing the netns (`references/commands.md`) |
| `--privileged` to fix a permission error | Disables every isolation mechanism at once | Find the one capability or device needed (`references/security.md`) |
| Bind mount over an image path | Host dir replaces container contents; empty host dir = empty app dir | Named volume — it seeds from the image on first use (`references/storage.md`) |
| `restart: always` on dev boxes | Containers you stopped by hand come back after every host reboot | `unless-stopped` |
| Chasing an app "memory leak" without checking the VM | On Desktop/colima the VM has its own ceiling; the container did not see the RAM you think you gave it | `docker info` Total Memory before touching `-m` (`references/runtimes.md`) |
| `chmod 777` on a bind mount | Makes the symptom go away and the data world-writable; the mismatch is numeric UID, not permission bits | `COPY --chown=<uid>:<gid>` at build and run as that UID (`references/storage.md`) |
| Rebuilding to roll back | The branch you rebuild from is not the artifact that was validated | Deploy the recorded digest (Rule 9) |
| Scanning only in CI | CVEs are published after the build; an image approved in March rots in place | Scan at build AND in the registry, and rebuild on a cadence (`references/security.md`, `## Due`) |
| A base-image or hardening decision that lives only in the chat | Re-litigated every quarter by whoever is on call | `artifacts/` with the date and what was rejected (`references/memory-template.md`) |

## Where Experts Disagree

- **Alpine vs debian-slim.** Alpine is smaller but musl breaks prebuilt Python wheels and has DNS edge cases. Default: slim for Python/Node, Alpine for Go and static binaries; switch only when image size is a measured constraint, and avoid changing mid-incident.
- **Compose in production.** Legitimate for single-host deployments; the boundary is multi-host scheduling, rolling deploys, or autoscaling — those needs, not fashion, justify an orchestrator (`k8s`).
- **One process per container.** The default. Escape hatch: a process supervisor when the platform offers no sidecar mechanism — avoid using as a convenience to avoid writing a second service.
- **Distroless vs a debuggable base.** Distroless removes the shell an attacker would use and the shell you would use at 3am. The frontier is whether you can reliably attach a sidecar in the environment where it will break: if you can, distroless; if production is a box you SSH into, a slim base with a non-root user wins on mean-time-to-recovery.
- **Rootless as the default.** Rootless removes the largest single risk (daemon-as-root) at the cost of privileged ports, some mount types, and slower storage on older kernels. Teams running untrusted workloads should take the cost; a single-tenant build host usually should not (`references/runtimes.md`).

## Security & Privacy

**Credentials:** this skill drives the Docker CLI, which reads registry credentials from `~/.docker/config.json` or an OS credential helper. It does NOT store, log, copy, or transmit registry credentials, SSH keys, or image secrets, and avoids writing credentials into `<state_root>/`.

**Local storage:** preferences, memory, stack and volume inventory, deploy digests and generated artifacts stay in `<state_root>/` on this machine, plus host rows in the shared `<state_root>/../servers/`. Image names, digests, ports and volume names only — no secrets.

**Guardrails:** commands are read-only by default. Destructive operations (`prune`, `down -v`, `volume rm`, `system prune --volumes`) name exactly what they delete and require explicit confirmation when `destructive_confirm` is true.
