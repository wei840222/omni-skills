---
name: nestjs
description: >
  Debug and structure NestJS apps around DI scopes, circular dependencies,
  modules, ValidationPipe, request lifecycle, exceptions, and testing. Use when
  a provider is missing, forwardRef is needed, REQUEST scope bubbles, DTOs fail
  to validate or transform, guards run before pipes, filters miss thrown errors,
  or Test.createTestingModule mocks break. Prefer nodejs/typescript for plain
  Node or language issues, nextjs/react for React stacks, and docker/k8s for
  deploy/orchestration outside Nest modules.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐱","requires":{"bins":["node"]}}'
  related-skills: '{"docker":"Container images and Compose once Nest builds leave the framework.","k8s":"Cluster manifests and scheduling after Nest ships as a workload.","nextjs":"Next.js/React full-stack when the app is not Nest.","nodejs":"Node runtime, process, and HTTP concerns outside Nest DI.","react":"React UI patterns when the problem is not Nest servers.","typescript":"Language-level typing outside Nest decorators and DTOs."}'
---

# NestJS

Operational NestJS guidance for **dependency injection, modules, validation, request lifecycle, exceptions, and tests**. Keep answers tied to the failing layer and re-open URLs in `references/sources.md` before stating version-sensitive defaults.

This skill is stateless. Keep app configs, env inventories, and runbooks in ordinary user files outside the skill package.

## When to use

- Provider not found / not exported across modules
- Circular module or provider graphs (`forwardRef`, barrel-file cycles)
- Singleton vs `Scope.REQUEST` / `Scope.TRANSIENT` and scope bubbling
- `ValidationPipe` + DTO decorators, whitelist/transform, nested DTOs
- Lifecycle order: middleware → guards → interceptors → pipes → handler → filters
- Throwing `HttpException` subclasses vs returning error objects
- Unit/e2e tests with `Test.createTestingModule`, overrides, `app.init()` / `app.close()`

Prefer `nodejs` / `typescript` for non-Nest runtime or language work, `nextjs` / `react` for React stacks, and `docker` / `k8s` once the question is packaging or cluster ops.

## Quick workflow

1. **Name the layer** — DI, module boundary, validation/pipe, guard/authz, interceptor, filter, or test harness.
2. **Check the lifecycle position** — guards cannot see pipe-transformed bodies; filters only see **thrown** exceptions.
3. **Apply the matching section below** — keep the smallest fix that restores the Nest contract.
4. **Verify against sources** — open `references/sources.md` for disputed API or default behavior.
5. **Answer operationally** — failing layer, concrete decorator/API, and the rule that justifies it.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/sources.md` | Official Nest / class-validator / Agent Skills URLs before citing defaults |
| `test-prompts.json` | Evaluation harness only — do not load during normal user assistance |

Keep `SKILL.md` as the sole runtime rule surface; `references/sources.md` is citation-only progressive disclosure.

## Dependency Injection

- A provider is injectable in another module only when it is listed in that module's `providers` **and**, for cross-module use, `exports` of the host module while the consumer `imports` the host module.
- Circular **provider** dependencies: both sides use `@Inject(forwardRef(() => Other))` (from `@nestjs/common`). Circular **module** imports likewise use `forwardRef(() => OtherModule)` on both `imports` arrays.
- Prefer removing the cycle when possible. Barrel `index.ts` re-exports inside the same folder often create false cycles — import concrete files instead of the barrel.
- Default provider scope is **singleton** (`Scope.DEFAULT`): one instance for the app lifetime. Hold per-request data carefully or use request scope intentionally.
- Request-scoped provider: `@Injectable({ scope: Scope.REQUEST })`. `REQUEST` scope **bubbles** up the injection chain — consumers become request-scoped too. Pairing `REQUEST` scope with circular `forwardRef` graphs can yield undefined deps; redesign the graph when that appears.
- `Scope.TRANSIENT` gives each consumer its own instance (not shared across injectors).

## Module Organization

- Import the **module**, not a foreign provider class, in `imports: [UserModule]`. Do not list another module's service only under `providers` and expect DI to find the real implementation.
- `exports` is the module public API: without export, the provider stays private to its host module.
- `@Global()` makes exported providers available without repeated imports — reserve for truly shared infrastructure (config, logging), not feature modules.
- Dynamic modules: static `forRoot()` / `forRootAsync()` / `register()` / `forFeature()` return a `DynamicModule`. Use async variants when options depend on other providers or config factories.

## Validation

- Install `class-validator` and `class-transformer` when using the built-in `ValidationPipe` with DTO classes.
- Decorate DTO **classes** (not interfaces or type-only imports). Type-only imports erase at runtime and leave nothing for the pipe to reflect.
- Enable useful defaults globally, for example:

```typescript
app.useGlobalPipes(
  new ValidationPipe({
    whitelist: true,
    forbidNonWhitelisted: true,
    transform: true,
  }),
);
```

- `whitelist: true` strips properties without validation decorators; add `forbidNonWhitelisted: true` to reject them instead.
- `transform: true` turns plain payloads into DTO class instances and can coerce primitives from path/query strings when the handler declares a number/boolean type.
- Nested object validation needs **both** `@ValidateNested()` (class-validator) and `@Type(() => NestedDto)` (class-transformer) on the nested property; one without the other leaves nested plain objects unvalidated.
- Array body elements lack emitted generic metadata — wrap with `ParseArrayPipe({ items: Dto })` or a dedicated wrapper class.
- Path/query params arrive as strings; use `ParseIntPipe` / `ParseBoolPipe` / `ParseUUIDPipe` (or transform + declared types) instead of assuming numbers.
- Schema-first alternative: `StandardSchemaValidationPipe` with Zod/Valibot/ArkType via the parameter `schema` option — do not invent options; re-open validation docs when mixing both pipes.

## Execution Order

Inbound request lifecycle (official summary):

1. Middleware (global `app.use`, then module-bound; global modules first)
2. Guards (global → controller → route)
3. Interceptors pre-controller (global → controller → route)
4. Pipes (global → controller → route → parameter pipes; at parameter level last param first)
5. Controller handler → services
6. Interceptors post-response (route → controller → global; FILO via RxJS)
7. Exception filters **only on uncaught throws** (route → controller → global)
8. Server response

Implications:

- Guards run **before** pipes, so they cannot rely on ValidationPipe-transformed DTO instances.
- Global pipes still run after guards and before the handler.
- Filters skip the rest of the lifecycle once an uncaught exception appears. Middleware errors reach **global** filters only (no route selected yet).
- Returning an error object does not enter the exceptions layer — **throw** instead.

## Exception Handling

- Throw `new HttpException(...)` or a built-in subclass (`BadRequestException`, `NotFoundException`, `ForbiddenException`, `UnauthorizedException`, …). Returning the instance does not trigger filters.
- Custom HTTP errors: extend `HttpException`. Custom filter classes implement `ExceptionFilter` and use `@Catch(...)`.
- Unrecognized thrown values become a generic 500 (`Internal server error`) via the built-in global filter.
- Wrap external I/O that should become domain HTTP errors; map failures to the right status instead of leaking raw stack traces.
- Prefer specific built-ins over a bare generic `HttpException` when the status already has a dedicated class.

## Testing

- `Test.createTestingModule({ ... }).compile()` does **not** auto-mock missing deps — list mocks explicitly in `providers` or override them.
- Call `.overrideProvider(Token).useValue(mock)` (or `useClass` / `useFactory`) **before** `.compile()`.
- E2E: `moduleRef.createNestApplication()`, then `await app.init()` before HTTP calls; `await app.close()` in `afterAll`.
- Request-scoped providers complicate unit tests (per-request instances). Prefer singleton seams for pure unit tests when behavior does not require request scope.
- Override helpers also cover guards/interceptors/filters/pipes (`overrideGuard`, `overrideInterceptor`, …).

## Common Mistakes

- `@Body()` typed as a bare interface/object → no class-validator metadata, no transform.
- `@Param('id')` treated as `number` without `ParseIntPipe` or `transform: true` + proper typing → still a string at runtime when transform is off.
- Guard returns `false` → default 403. Throw a specific `HttpException` when the client needs a clearer status/body.
- Async custom providers need `useFactory` (often async) plus `inject` tokens — a plain class token will not await setup.
- Forgetting `await` on async service methods returns a `Promise`, not the resolved value, and breaks callers/tests.
- Importing a provider class into another module's `providers` array duplicates a second instance instead of using the exported one.

## Safety boundaries

- Treat env secrets, DB URLs, and JWT signing keys as host secrets — keep them out of skill files and example commits.
- Re-open `references/sources.md` before asserting Nest major-version defaults, pipe option names, or lifecycle order.
- Route non-Nest Node/TS questions to `nodejs` / `typescript` rather than overloading this skill.
