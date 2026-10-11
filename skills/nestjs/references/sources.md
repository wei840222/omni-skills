# NestJS skill sources

Authoritative references used for this refactor. Prefer these over blog posts when guidance conflicts. Re-open before asserting version-specific defaults.

## NestJS core

- Modules — https://docs.nestjs.com/modules
- Dynamic modules — https://docs.nestjs.com/fundamentals/dynamic-modules
- Circular dependency — https://docs.nestjs.com/fundamentals/circular-dependency
- Injection / provider scopes — https://docs.nestjs.com/fundamentals/injection-scopes
- Provider scopes (docs source) — https://github.com/nestjs/docs.nestjs.com/blob/master/content/fundamentals/provider-scopes.md
- Custom providers — https://docs.nestjs.com/fundamentals/custom-providers
- Pipes — https://docs.nestjs.com/pipes
- Validation (ValidationPipe options, whitelist, transform) — https://docs.nestjs.com/techniques/validation
  (docs source path: `content/application/validation.md` in nestjs/docs.nestjs.com)
- Guards — https://docs.nestjs.com/guards
- Interceptors — https://docs.nestjs.com/interceptors
- Exception filters — https://docs.nestjs.com/exception-filters
- Request lifecycle — https://docs.nestjs.com/faq/request-lifecycle
- Testing — https://docs.nestjs.com/fundamentals/testing
  (docs source path: `content/fundamentals/unit-testing.md`)

## Validation libraries

- class-validator usage and nested validation — https://github.com/typestack/class-validator
- class-transformer `@Type` — https://github.com/typestack/class-transformer

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Operational note

Nest docs site paths sometimes redirect (`/techniques/validation` vs application validation chapter; `/fundamentals/injection-scopes` vs `provider-scopes.md` in the docs repo). When a URL and the GitHub docs source disagree, trust the opened page content for the project's Nest major version and record both links in the PR if needed.

### Claim checks performed this refactor

| Claim | Verdict | Source |
|---|---|---|
| Default provider scope is singleton | Confirmed | provider-scopes.md `DEFAULT` row |
| `Scope.REQUEST` bubbles to dependents | Confirmed | provider-scopes.md scope hierarchy |
| Circular providers need `forwardRef` both sides; barrels can create cycles | Confirmed | circular-dependency.md |
| Modules encapsulate providers; `exports` + consumer `imports` required | Confirmed | modules.md |
| `@Global()` for shared modules; dynamic `forRoot`/`register` pattern | Confirmed | modules.md / dynamic-modules.md |
| Lifecycle: middleware → guards → interceptors → pipes → handler → interceptors → filters | Confirmed | request-lifecycle.md summary |
| Guards before pipes (no transformed body in guards) | Confirmed | guards.md hint + lifecycle |
| Filters only on uncaught exceptions; throw `HttpException` | Confirmed | exception-filters.md + lifecycle filters section |
| Middleware errors → global filters only | Confirmed | request-lifecycle.md filters hint |
| `ValidationPipe` needs class-validator/class-transformer; whitelist/forbid/transform options | Confirmed | application/validation.md |
| Nested DTO needs `@ValidateNested` + `@Type` | Confirmed via class-validator nested objects docs + class-transformer `@Type` | library READMEs |
| `Test.createTestingModule`, `overrideProvider` before compile, e2e `app.init`/`close` | Confirmed | unit-testing.md |
