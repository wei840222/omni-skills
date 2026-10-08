# Language-specific Docker rules

Language runtimes change layer order, base-image choice, signal handling, and memory caps. Pair this file with `references/images.md` for generic Dockerfile craft.

## Python

- Prefer `python:<minor>-slim` (Debian) over Alpine. Musl breaks many prebuilt wheels and forces slow source builds; segfaults often exit 139.
- Canonical layer order: copy dependency manifests → install into a cache mount → copy application code.
- Use a virtualenv or `/usr/local` consistently; do not mix system site-packages and venv paths.
- Python has no built-in heap cap comparable to JVM/Node — bound workers, connection pools, and batch sizes under the container `-m` limit.
- Multi-stage: build wheels in a builder stage, copy only the venv or site-packages into the runtime stage.

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefix=/install -r requirements.txt
FROM python:3.12-slim
COPY --from=builder /install /usr/local
COPY . /app
USER 10001
CMD ["python", "-m", "app"]
```

## Node.js

- Prefer `node:<minor>-slim` or a distroless runtime after `npm ci --omit=dev` in a builder stage.
- Exec-form `CMD ["node","server.js"]`. Shell form leaves `sh` as PID 1 and swallows `SIGTERM`, so every `docker stop` waits the full grace period.
- Install an explicit signal handler or use `node --use-openssl-ca` patterns only when needed; still prefer a tiny init (`--init`) when the app ignores signals.
- Cap V8 with `--max-old-space-size` at ~75–80% of the container memory limit (value is MB).
- Native addons: build on the same libc/arch as production; Alpine musl and glibc binaries are not interchangeable.

## Go

- Build static binaries (`CGO_ENABLED=0`) when possible and ship on `scratch` or `gcr.io/distroless/static`.
- Keep the module download cache on a BuildKit cache mount: `--mount=type=cache,target=/go/pkg/mod`.
- Set `USER` with a numeric UID in the final stage; scratch images have no `/etc/passwd` names to resolve.
- Prefer multi-stage: compile in `golang:*`, copy only the binary forward.

## Rust

- Use a builder with the stable toolchain, then copy the release binary to `debian-slim` or distroless.
- Cache `/usr/local/cargo/registry` and target dirs with BuildKit cache mounts to avoid multi-minute cold builds.
- Link against musl only when you intentionally target Alpine/scratch; otherwise stay on glibc for fewer footguns.

## JVM

- Always set `-Xmx` (and usually `-Xms`) to ~75% of the container memory limit. JVMs older than 8u191/10 size the heap from **host** memory and ignore the cgroup.
- Prefer modern cgroup-aware builds (17+) and keep the same major version across local, CI, and prod images.
- Use `exec`-form entrypoints that end on the JVM process so `SIGTERM` reaches the runtime for graceful shutdown.
- Layer dependency fetch (`./mvnw -q -DskipTests dependency:go-offline` or Gradle equivalent) before copying sources.

## Shared rules across languages

| Concern | Rule |
| --- | --- |
| Base image | Default `debian-slim`; Alpine only when size is measured and musl is acceptable |
| PID 1 | Exec-form CMD/ENTRYPOINT; add `--init` when the runtime lacks SIGTERM handling |
| Memory | Container `-m` **and** matching `--memory-swap`; runtime heap below that ceiling |
| Non-root | `USER 10001` (numeric) after privileged build steps |
| Secrets | BuildKit secret mounts — never `ARG`/`ENV` for tokens (`references/security.md`) |

When a service's language or base pin changes, update `## Stacks` under `<state_root>/memory.md` in the same turn.
