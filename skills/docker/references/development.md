# Local development loop

Use this file when the goal is a fast edit → rebuild → verify cycle on a single host. Production deploys and CI cache live in `references/production.md` and `references/ci.md`.

## Compose watch and hot reload

- Prefer Compose Watch (`docker compose watch`) or a bind mount of source into the container over rebuilding the whole image for every line change.
- Bind the source read-write only when the process needs to write back; otherwise mount read-only and keep generated artifacts on a named volume.
- After changing the Dockerfile itself, still run `docker compose up -d --build`. Plain `up` reuses a stale image even when source is bind-mounted.
- Exclude `node_modules`, `.git`, build caches, and virtualenvs from the bind when the container installs its own copy — host and container dependency trees diverge silently.

## Seeded databases

- Postgres / MySQL init scripts under `/docker-entrypoint-initdb.d` run **only when the data directory is empty**. Re-running `compose up` will not re-seed an existing named volume.
- To re-seed intentionally: stop the service, remove **that** volume after naming it, then start again. Never pair this with a casual `down -v` against unknown volumes.
- Prefer idempotent seed SQL or a one-shot migrate job over baking production data into the image.
- Keep seed credentials as pointers in state (`env:…` / `file:…`), not as literals in committed compose overrides.

## Debuggers and ports

- Publish the debugger port only on `127.0.0.1` unless remote attach is deliberate.
- Node: ensure the process handles `SIGTERM` and that `CMD` is exec-form so the debugger is not buried under `sh` as PID 1 (`references/languages.md`).
- JVM: expose JDWP explicitly and cap `-Xmx` below the container memory limit so the debugger session does not OOM the cgroup.
- When attach fails, check published ports, user-defined network DNS name, and whether the app bound `127.0.0.1` inside the container instead of `0.0.0.0`.

## Devcontainers and Testcontainers

- Devcontainers are a standardized dev compose + tooling image. Keep secrets out of `devcontainer.json` and out of the committed Dockerfile layers.
- Testcontainers need a reachable Docker API socket or TCP endpoint; rootless and remote contexts change the socket path (`references/runtimes.md`).
- Prefer pulling pinned images for fixtures; floating `latest` tags make CI flake when upstream rebuilds overnight.

## Source-path mapping traps

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Edit not visible | Image not rebuilt / wrong service | `compose up -d --build` for the service |
| Permission denied on bind | Container UID ≠ host file owner | numeric `user:` or chown once on the volume |
| macOS slow I/O | VirtioFS / osxfs on huge trees | delegate caches to named volumes |
| SELinux denials | Host enforces labels | `:Z` / `:z` only when required |

**After the local loop stabilizes**, write the working compose override or runbook under `<state_root>/artifacts/` and index it from `## Boxes` in the same turn (`references/memory-template.md`).
