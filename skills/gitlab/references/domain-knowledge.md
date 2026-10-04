# Domain knowledge and sources

Verify GitLab CI claims against current official docs before stating version-specific behavior. Prefer docs.gitlab.com over blog reproductions.

## Authoritative sources (Gate 6)

| Topic | What we rely on | URL |
|-------|-----------------|-----|
| `rules`, job keywords, `extends` merge model | CI/CD YAML reference | https://docs.gitlab.com/ci/yaml/ |
| `only`/`except` legacy keywords | YAML reference (deprecated keywords area) | https://docs.gitlab.com/ci/yaml/#onlyexcept-basic |
| `include` merge behavior | Include documentation | https://docs.gitlab.com/ci/yaml/includes/ |
| Docker-in-Docker / build strategies | Use Docker to build Docker images | https://docs.gitlab.com/ci/docker/using_docker_build/ |
| Job artifacts | Job artifacts | https://docs.gitlab.com/ci/jobs/job_artifacts/ |
| Caching semantics | Caching in CI/CD | https://docs.gitlab.com/ci/caching/ |
| Variable security (masked/protected) | CI/CD variable security | https://docs.gitlab.com/ci/variables/#cicd-variable-security |
| Predefined variables / pipeline sources | Predefined variables | https://docs.gitlab.com/ci/variables/predefined_variables/ |

## Corrections vs naive folklore

- **`extends` does not append arrays.** Official merge is reverse deep-merge on keys without merging keyword values — child `script:` replaces parent `script:`.
- **Cache is not a dependency graph.** Required outputs belong in artifacts (or images), not cache.
- **Protected variables fail closed on unprotected refs** by being unavailable, not by failing the job automatically.

## Out of scope facts

Do not invent pricing tiers, runner minute quotas, or SaaS shared-runner privileged policy as universal constants — those change by plan and instance. State the mechanism and tell the user to confirm on their GitLab instance.
