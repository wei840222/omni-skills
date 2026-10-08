# Registries — auth, mirrors, retention, signing

Use this file for login failures, Hub rate limits, private registries, digest promotion, and retention leaks. Image build craft stays in `references/images.md`; CI tagging patterns stay in `references/ci.md`.

## Authentication

- Prefer the OS credential helper (`docker-credential-*`) over a plaintext `~/.docker/config.json` auth blob.
- `docker login` stores a token or encoded password for the registry host in `default_registry` (config default: `docker.io`).
- Never write registry tokens into `<state_root>/`. Store pointers only: `env:REGISTRY_TOKEN`, `keychain:ghcr-push`, `file:~/.docker/config.json`.
- Robot / deploy accounts get least privilege: pull-only on runtime nodes, push on CI identities, delete only where retention jobs run.

## Rate limits and mirrors

- Anonymous Docker Hub pulls are aggressively rate-limited. Authenticated pulls raise the ceiling; a pull-through mirror removes Hub from the hot path.
- Configure daemon mirrors / `registry-mirrors` for Hub caching on shared runners; document the mirror host in `## Registries` of `<state_root>/memory.md`.
- Corporate TLS-intercepting proxies need the CA under `/etc/docker/certs.d/<registry>/ca.crt` (or the distribution's equivalent). Symptom: TLS verify failures only inside the daemon, not in curl on the host.

## Digests and promotion

- Tags move; digests do not. Record `docker inspect -f '{{index .RepoDigests 0}}' <image>` at deploy time (`references/domain.md` rule 9).
- Promote the **same** digest across environments:

```bash
docker buildx imagetools create -t myrepo/app:prod myrepo/app@sha256:<digest>
```

- Never rebuild from a branch to "promote". Staging validated one artifact; a rebuild produces another.

## Retention and cleanup

| Class | Policy |
| --- | --- |
| Immutable sha tags | Keep for the rollback window (often 30–90 days) |
| `pr-<n>` tags | Short TTL + registry GC; otherwise they become the silent disk leak |
| Floating pointers (`latest`, `staging`, `prod`) | Keep; they retarget digests |
| Untagged manifests | Schedule registry GC; local `docker image prune` does not clean the remote |

## Signing and provenance (when required)

- Prefer digest deploys plus attestations/SBOM produced at build time over ad-hoc "we scanned once" claims.
- Signature verification belongs at deploy admission, not only in the PR job that built the image.
- If signing is out of scope for the environment, say so explicitly — do not invent Cosign steps the host cannot run.

## Failure matrix

| Symptom | First checks |
| --- | --- |
| `unauthorized` / `denied` on pull | Identity, helper, token scope, repo visibility |
| `toomanyrequests` | Auth vs anonymous, mirror, concurrent CI jobs |
| TLS / x509 errors | `certs.d`, corporate CA, clock skew |
| Push ok, pull fails on node | Node uses a different registry host or mirror |
| Promote changed behavior | Someone rebuilt instead of retagging the digest |

**After a registry, mirror, or retention change**, update `## Registries` (and any artifact runbook) under `<state_root>/` in the same turn.
