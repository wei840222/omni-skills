# Execution Environment

## Docker-in-Docker (DinD)

- DinD commonly needs a runner/executor setup that allows privileged containers. Many shared runners disallow privileged mode; use a self-hosted runner, an approved privileged tag, or a non-privileged alternative (for example Docker socket binding or Kaniko-style builds) when privileged mode is unavailable.
- Set `DOCKER_HOST` explicitly when the job must talk to a DinD service (typical pattern: `tcp://docker:2375` or the TLS port your template documents).
- TLS must be coherent: either configure certificates correctly or set `DOCKER_TLS_CERTDIR: ""` for the non-TLS lab pattern. Half-configured TLS is a frequent “cannot connect to docker daemon” cause.

Example shape (adjust image tags and TLS to the project's hardened baseline):

```yaml
default:
  image: docker:24-cli
  services:
    - docker:24-dind
  variables:
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""

build:
  script:
    - docker info
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
```

## Runner tags and executors

- Jobs that set `tags:` only run on matching runners. A tag mismatch leaves the job **pending** with little feedback.
- Confirm executor type (Docker, Kubernetes, shell) before prescribing DinD or socket-mount patterns.

## Artifacts vs cache

| Mechanism | Guarantee | Use for |
|-----------|-----------|---------|
| **Cache** | Best-effort; may miss | Dependency downloads, rebuild acceleration |
| **Artifacts** | Produced by a job and passed on success (per job policy) | Build outputs required by later jobs |
| **needs** | DAG edges; downloads artifacts by default | Faster pipelines and explicit artifact graphs |

- Add `dependencies: []` when a job must not download prior-stage artifacts.
- Use `needs: [{ job: build, artifacts: false }]` when ordering matters but artifacts do not.
- Never treat cache restoration as required correctness; encode required inputs as artifacts or registry images.
