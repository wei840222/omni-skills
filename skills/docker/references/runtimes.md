# Runtimes — Desktop, colima, OrbStack, rootless, Podman, GPU

Runtime flavor changes socket paths, VM memory ceilings, port binding, cgroup behavior, and volume performance. Read this before chasing an application "memory leak" on a laptop VM.

## Flavor matrix

| Flavor | API endpoint (typical) | Notes |
| --- | --- | --- |
| Docker Desktop | OS-specific VM socket via Docker context | VM has its own CPU/RAM ceiling independent of host free memory |
| colima | `unix://$HOME/.colima/default/docker.sock` | Lima VM; set CPU/memory explicitly or defaults starve builds |
| OrbStack | Docker-compatible context | Fast I/O; still a VM boundary for total memory |
| Linux Engine (rootful) | `/var/run/docker.sock` | Full feature set; daemon runs as root |
| Rootless Engine | `$XDG_RUNTIME_DIR/docker.sock` | No privileged ports (<1024) without rootlesskit tricks; some mounts unsupported |
| Podman | `podman.sock` / remote API | Often rootless by default; Compose via `podman compose` or podman-docker shim |

Set `runtime_flavor` in `<state_root>/config.yaml` so examples match the user's socket and security model.

## First checks on every runtime

1. `docker context show` and `docker info` — confirm the daemon you think you are talking to.
2. `docker info` → Total Memory before raising container `-m`. On Desktop/colima/OrbStack the VM ceiling is the real limit.
3. Disk path for images/volumes (`Docker Root Dir`) — VM disks fill independently of host free space.

## Rootless specifics

- Binding host ports below 1024 fails without extra capability setup; use high ports or a reverse proxy on the host.
- cgroup v2 delegation must be enabled for memory/CPU limits to stick; otherwise limits appear accepted and are ignored.
- Some storage drivers and overlay options differ; permission errors on volumes often mean UID mapping, not a bad app user.
- Rootless removes daemon-as-root risk at the cost of privileged workloads and some network modes (`references/domain.md` expert tradeoffs).

## Podman differences that matter

- Emulates Docker CLI well for common flows; do not assume every Swarm/Desktop extension exists.
- Systemd integration (`podman generate systemd` / quadlets) replaces Docker restart policies on many hosts.
- SELinux labeling on binds is more commonly required than on stock Desktop.

## GPU

- NVIDIA: host driver + NVIDIA Container Toolkit; request GPUs via `--gpus` / Compose `deploy.resources.reservations.devices` depending on stack version.
- Confirm the toolkit matches the driver before debugging framework CUDA errors.
- GPU access is a host capability — rootless and some VM runtimes need extra wiring or are unsupported.

## Networking and host access

- `host.docker.internal` is built-in on Desktop/OrbStack; on Linux Engine add
  `--add-host=host.docker.internal:host-gateway`.
- VPN clients on the host often break container egress via MTU or routing —
  see `references/networking.md`.
- Rootless cannot use some `network_mode: host` setups the same way rootful can.

## Performance traps

| Symptom | Runtime cause | Mitigation |
| --- | --- | --- |
| OOM with free host RAM | VM memory ceiling | Raise VM RAM; then set container `-m` |
| Slow binds on macOS | VirtioFS/osxfs | Named volumes for dependencies; minimize bind scope |
| Limits ignored | No cgroup delegation (rootless) | Enable delegation; verify in `docker info` |
| Wrong daemon mutated | Multiple contexts | Export `DOCKER_HOST` / context explicitly |

**After discovering a runtime ceiling, socket path, or GPU requirement**, write it under `## Environment` in `<state_root>/memory.md` so the next session does not rediscover it the hard way.
