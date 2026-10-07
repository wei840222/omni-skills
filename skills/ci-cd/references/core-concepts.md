# CI/CD Core Concepts and Troubleshooting

## Platform Selection

| Stack | Recommended | Why |
|-------|-------------|-----|
| Web (Next.js, Nuxt, static) | Vercel, Netlify | Zero-config, auto-deploys, preview URLs |
| Mobile (iOS/Android/Flutter) | Codemagic, Bitrise + Fastlane | Pre-configured signing, app store upload |
| Backend/Docker | GitHub Actions, GitLab CI | Full control, self-hosted runners option |
| Monorepo | Nx/Turborepo + GHA | Affected detection, build caching |

**Decision tree:** If platform handles deploy automatically (Vercel, Netlify) → skip custom CI. Only add GitHub Actions when you need tests, custom builds, or deploy to your own infra.

## Common Pipeline Pitfalls

| Mistake | Impact | Fix |
|---------|--------|-----|
| Using `latest` image tags | Builds break randomly | Pin versions: `node:20.11.0` |
| Not caching dependencies | +5-10 min per build | Cache `node_modules`, `.next/cache` |
| Secrets in workflow files | Leaked in logs/PRs | Use platform secrets, OIDC for cloud |
| Missing `timeout-minutes` | Stuck jobs burn budget | Always set: `timeout-minutes: 15` |
| No `concurrency` control | Redundant runs on rapid pushes | Group by branch/PR |
| Building on every push | Wasted resources | Build on push to main, test on PRs |

## Debugging Failed Builds

| Error Pattern | Likely Cause | Check |
|---------------|--------------|-------|
| Works locally, fails in CI | Environment drift | Node version, env vars, OS |
| Intermittent failures | Flaky tests, resource limits | Retry logic, increase timeout |
| `ENOENT` / file not found | Build order, missing artifact | Check `needs:` dependencies |
| Exit code 137 | Out of memory | Use larger runner or optimize |
| Certificate/signing errors | Expired or mismatched creds | Regenerate with Match/Fastlane |
