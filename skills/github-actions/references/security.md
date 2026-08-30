# GitHub Actions Security Knowledge

## 1. Principle of Least Privilege and OIDC
GitHub Actions introduces potential security risks if broad permissions are granted across all jobs.
- **OIDC (OpenID Connect)**: When interacting with cloud providers (AWS, Azure, GCP), favor OIDC federation instead of long-lived secrets. This limits the blast radius and eliminates the need to rotate keys.
- **`permissions` Key**: Workflows should always specify narrow `permissions` at either the workflow or job level. For example, do not grant `contents: write` if the job only needs `contents: read`.

## 2. Protected Branches and Workflow Reruns
Workflows triggered by `pull_request_target` run with the base repository's credentials instead of the fork's, which creates vectors for executing untrusted code with elevated privileges.
- Always require approvals for environments deploying to production.
- Use explicit tag or commit SHA pinning for third-party actions instead of branch names like `@master` or `@v1`, since mutable refs can be hijacked.

## 3. Caching Vulnerabilities
Caches are shared across branches based on matching keys. Avoid storing sensitive build artifacts or environment variables in the cache.

## Source Information
- Concepts sourced from [GitHub Actions Security Hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions) and the [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/).
