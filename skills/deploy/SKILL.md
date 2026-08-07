---
name: deploy
description: Plan and execute application deployments with CI/CD pipelines, GitOps workflows, and zero-downtime strategies. Covers rolling/blue-green/canary deployments, rollback procedures, supply chain security (SLSA, SBOM, cosign), and platform engineering patterns. Use when deploying to Kubernetes, configuring GitHub Actions security, setting up Argo CD/Flux, designing rollback procedures, or troubleshooting deployment failures.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🚀"}'
---

## State location

Deploy is a knowledge skill that does not persist state across sessions. All deployment commands execute in the current workspace or target environment context.

## Deployment Strategies

Choose a deployment strategy based on risk tolerance, resource availability, and rollback speed requirements:

- **Rolling**: update instances one by one — safe, slower, no extra resources needed
- **Blue-green**: full parallel environment, instant switch — fast rollback, requires 2x resources
- **Canary**: route percentage of traffic to new version — catch issues early, requires complex routing
- **GitOps promotion**: Argo CD/Flux reconcile desired state from Git — declarative, auditable, automatic drift detection

No universal best exists. Match strategy to your risk tolerance and available resources.

## 🔴 Pre-Deploy Checkpoint

**STOP and verify these conditions before every deployment:**

- Tests passing in CI — verify all tests pass before deploying
- Environment variables set in target — missing secrets cause silent failures
- Database migrations run before code deploy — new code expecting new schema fails
- Rollback plan ready — know exactly how to revert before you need to
- Supply chain verified — artifacts signed and provenance checked

**If any check fails, halt deployment and resolve the issue first.**

## Zero-Downtime Deploys

- Health checks must pass before traffic routes — unhealthy instances stay out
- Graceful shutdown: finish in-flight requests before terminating
- Database changes must be backwards compatible — old code still running during deploy
- Session handling: sticky sessions or external session store — preserve user state
- PreStop hooks in Kubernetes — allow load balancer to drain connections before pod termination

**If health check fails after deploy:**
1. Check pod logs: `kubectl logs <pod-name> --previous`
2. Verify readiness probe endpoint returns 200
3. Check resource limits: `kubectl describe pod <pod-name>`
4. If stuck, rollback immediately: `kubectl rollout undo deployment/<name>`

## CI/CD Pipeline

- Build once, deploy everywhere — same artifact to staging and prod
- Cache dependencies between builds — save minutes per deploy
- Parallel steps where possible — tests, linting, security scans
- Fail fast: quick checks first — don't wait for slow tests to catch typos
- Pin action versions with SHA — tags can change unexpectedly (e.g., `@v4` → `@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1`)
- Use Dependabot or Renovate to automate SHA pin updates

## CI/CD Security Hardening

- Set `permissions: read-all` at workflow top — override default read-write token
- Use `permissions: {}` for jobs that don't need GitHub API access
- Pass user-controlled values via environment variables — prevent expression injection
- Use `pull_request` trigger for forks — not `pull_request_target` with PR head checkout
- Configure CODEOWNERS for `.github/workflows/` — require security team review
- Use GitHub Environments with required reviewers for production deployments

**OIDC Federation Example (AWS):**
```yaml
- name: Configure AWS Credentials
  uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502 # v4.0.2
  with:
    role-to-assume: arn:aws:iam::123456789012:role/GitHubActions
    aws-region: us-east-1
```

**If OIDC token expires mid-workflow:**
1. Split long-running jobs into shorter steps (< 5 minutes each)
2. Re-authenticate at the start of each deployment stage
3. Re-run the OIDC federation step (e.g., `configure-aws-credentials`) before the deploy stage

## Supply Chain Security

- Sign container images with cosign — keyless signing via OIDC identity
- Generate SLSA provenance attestations — record build source, environment, and parameters
- Verify artifact provenance before deployment — reject unsigned or unverified artifacts
- Generate SBOM (Software Bill of Materials) — SPDX or CycloneDX format for dependency transparency
- Pin all third-party actions to full commit SHA — prevent supply chain attacks like GhostAction
- Fork critical actions into your organization — review diffs before merging upstream changes

**Cosign Signing Example:**
```bash
# Sign container image (keyless, using OIDC identity)
cosign sign --yes ghcr.io/myorg/myapp:v1.2.3

# Verify signature before deployment
cosign verify \
  --certificate-identity-regexp="https://github.com/myorg/myapp" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/myorg/myapp:v1.2.3
```

**If artifact verification fails:**
1. Check if image was signed: `cosign verify <image>`
2. Verify certificate identity matches expected GitHub repo
3. Check Rekor transparency log: `cosign verify --rekor-url https://rekor.sigstore.dev <image>`
4. Reject unsigned artifacts — do not deploy without provenance

## Environment Management

- Staging mirrors prod — different configs cause "works in staging" bugs
- Secrets in secret manager, not environment files — rotation without redeploy
- Feature flags decouple deploy from release — ship dark, enable later
- Config as code in version control — except secrets
- Use OIDC federation for cloud auth — short-lived tokens, no static credentials to steal
- Environment protection rules — require reviewers, wait timers, branch restrictions for production

## Database Migrations

- Migrations must be backwards compatible during deploy window
- Add columns nullable first, then backfill, then add constraint
- Rename columns in multiple steps — add new, migrate data, remove old
- Test migrations on prod-size data — 10 rows is fast, 10 million isn't
- Rollback script for every migration
- Expand-contract pattern for schema changes — add new, dual-write, migrate readers, migrate writers, drop old

**If migration blocks writes on large table:**
1. Find the blocking query's PID and cancel it:
   ```sql
   SELECT pid, query FROM pg_stat_activity WHERE state = 'active';
   SELECT pg_cancel_backend(<pid>);  -- graceful cancel
   SELECT pg_terminate_backend(<pid>);  -- force terminate if cancel fails
   ```
2. Use online migration tool: `pg_repack` for PostgreSQL, `gh-ost` for MySQL
3. Break migration into smaller batches with `LIMIT` clauses
4. Schedule migration during low-traffic window

## Rollback

- Automated rollback on health check failure
- Keep previous version artifacts available — can't rollback what you deleted
- Database rollbacks are hard — design migrations to avoid needing them
- Feature flags for instant rollback of functionality without deploy
- Document rollback procedure — panic time is not learning time
- GitOps revert — change Git manifest back to previous version, controller reconciles automatically

**🔴 Rollback Decision Checkpoint:**
If error rate increases > 1% or latency increases > 20% after deploy, execute rollback immediately. Do not wait for confirmation.

**Kubernetes Rollback:**
```bash
# Check rollout history
kubectl rollout history deployment/<name>

# Rollback to previous version
kubectl rollout undo deployment/<name>

# Rollback to specific revision
kubectl rollout undo deployment/<name> --to-revision=<N>
```

**GitOps Rollback (Argo CD):**
```bash
# Revert Git commit to previous version
git revert HEAD
git push origin main

# Argo CD will automatically reconcile
# Or force sync: argocd app sync <app-name>
```

## Monitoring Post-Deploy

- Watch error rates for 15 minutes after deploy — most issues surface quickly
- Compare key metrics to pre-deploy baseline
- Alerting on anomalies: latency spike, error rate increase
- Log correlation: trace requests through systems
- User-facing smoke tests after deploy
- SLO-based canary analysis — automatically promote or rollback based on error budget impact

**If metrics degrade after deploy:**
1. Check deployment logs: `kubectl logs -l app=<name> --tail=100`
2. Compare with previous version: `kubectl rollout history deployment/<name>`
3. Verify resource limits not exceeded: `kubectl top pods`
4. If SLO breach imminent, rollback immediately

## Platform Engineering

- Build Internal Developer Platform (IDP) — abstract infrastructure complexity
- Self-service environments — developers provision staging without ops tickets
- Golden paths — documented, tested deployment templates for common architectures
- Backstage or custom portal — service catalog, API docs, deployment status in one place
- Platform as product — treat developers as customers, measure adoption and satisfaction

## GitOps Best Practices

- Git as single source of truth — declarative manifests in version control
- Kustomize for patching known values, Helm for parameterizing unknowns — use both together
- Trunk-based development for GitOps repos — separate workflow from application code
- No branches for environments — use folders (base/, overlays/staging/, overlays/prod/)
- Rendered manifests pattern — commit final YAML, not templates, for production
- Argo CD for deployment, Kargo for promotion — separate reconciliation from environment advancement

## Platform-Specific

### Containers
- Image tagged with git SHA — know exactly what's running
- Health check endpoint that verifies dependencies
- Resource limits set — prevent runaway containers
- Multi-stage builds — minimize image size and attack surface
- Non-root user — run containers as unprivileged user

### Serverless
- Cold start optimization — keep bundles small
- Provisioned concurrency for latency-sensitive paths
- Timeout set appropriately — default is often too short
- SnapStart (AWS) or min-instances (GCP) — reduce cold start latency

### Static Sites
- CDN cache invalidation after deploy
- Immutable assets with content hashes — cache forever
- Preview deploys for PRs
- Atomic deploys — all files update simultaneously, no partial state

## Gotchas

Environment-specific facts that defy reasonable assumptions:

- **GitHub Actions `pull_request_target`**: Grants secrets to workflows triggered by forks. If you checkout PR head code, you run attacker-controlled code with your secrets. Use `pull_request` trigger instead.
- **Kubernetes rolling update default**: Without `maxUnavailable` and `maxSurge` configured, Kubernetes may terminate pods faster than your application can drain connections. Always set PreStop hooks.
- **Database migration on large tables**: `ALTER TABLE` on PostgreSQL acquires an exclusive lock. On tables with millions of rows, this blocks writes for minutes. Use tools like `pg_repack` or online migration strategies.
- **OIDC token expiration**: GitHub Actions OIDC tokens expire in 5 minutes. Long-running workflows may need to refresh tokens or split into shorter jobs.
- **Blue-green DNS TTL**: If using DNS for blue-green switching, ensure TTL is low enough (60 seconds or less) to allow fast cutover. High TTL causes users to hit old environment after switch.
- **Feature flag cleanup**: After fully rolling out a feature, remove the flag code. Accumulated dead flags increase cognitive load and create technical debt.

## Common Mistakes

- Deploying Friday afternoon — issues surface when nobody's watching
- No rollback plan — hoping nothing goes wrong isn't a strategy
- Mixing code and migration deploys — one thing at a time
- Manual deploy steps — if it's not automated, it's wrong sometimes
- Deploying without monitoring — you won't know it's broken until users complain
- Using mutable tags for actions — `@v4` can be moved to malicious commit
- Storing long-lived cloud credentials as secrets — use OIDC federation instead
- Direct interpolation of user input in workflows — use environment variables
