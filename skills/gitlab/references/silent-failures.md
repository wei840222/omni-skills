# Silent Failures

## Protected variables on unprotected refs

Protected CI/CD variables are available only on protected branches and tags. On unprotected refs the job can still run while the variable expands to empty — look like a script bug, not an auth config miss.

**Fix direction:** protect the branch/tag, duplicate a non-protected test secret with clear naming, or skip the job on unprotected refs with `rules`.

## Runner tag mismatch

If `tags:` do not match any online runner, the job stays **pending** indefinitely without a script error.

**Fix direction:** verify runner tags in **Settings → CI/CD → Runners**, remove unnecessary tags, or start a runner that advertises the tag.

## DinD on non-privileged runners

Without privileged mode (or an approved alternative), DinD fails with opaque daemon connection errors.

**Fix direction:** see `environment.md` — privileged capability, `DOCKER_HOST`, and TLS must agree; otherwise switch build strategy.

## Masked variables

Masked variables must meet GitLab's masking constraints. Invalid values may be rejected or fail to mask as expected, which can expose secrets in job logs.

**Fix direction:** follow current masking requirements in GitLab variable security docs; never “unmask to debug” in shared logs on production secrets — reproduce with a disposable dummy value.

## Diagnostic order

1. Is the job created at all? (`rules` / `only`)
2. Is it pending? (tags / runners)
3. Are variables empty? (protected scope)
4. Is the executor capable? (DinD / services)
5. Only then rewrite business script steps

## White-bear note

Do not jump to rewriting deploy scripts while the job is still uncreated, pending, or missing variables — fix selection and environment first.
