---
name: angular
description: "Debugs and builds Angular apps around change detection, RxJS subscriptions, DI, reactive forms, routing, and HttpClient. Use when OnPush misses updates, subscriptions leak, DI cycles crash, FormGroup setValue throws, route params stay stale, or interceptors drop requests; not for React/Vue frameworks or generic TypeScript language mechanics."
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🅰️","displayName":"Angular"}'
  related-skills: '{"typescript":"Language-level typing, generics, and tsconfig issues outside Angular APIs","frontend":"Cross-framework UI polish, accessibility, and layout systems","react":"React component and hooks work instead of Angular","vue":"Vue reactivity and composables instead of Angular"}'
---

# Angular Reliability

Stay inside Angular runtime semantics. Name the failing layer first — change detection, RxJS lifetime, DI graph, forms model, router state, or HTTP pipeline — then load only the matching reference.

## When To Use

- OnPush or signal-backed views miss updates after mutation
- Subscriptions, `HttpClient` calls, or timers keep running after destroy
- Provider graphs crash with circular DI or unexpected instance scope
- Reactive forms reject partial updates, drop disabled values, or mix template-driven bindings
- Same-component route navigations keep stale `snapshot` params
- Interceptors drop requests, mis-order auth, or swallow errors

Route React/Vue framework work and pure TypeScript language questions to their skills.

## Quick Reference

| Situation | Load | Why |
|-----------|------|-----|
| OnPush / queries / outputs miss updates | `references/components.md` | Reference equality and lifecycle timing |
| Subscription leaks or operator choice | `references/rxjs.md` | Lifetime and cancellation rules |
| FormGroup / validators / ngModel conflicts | `references/forms.md` | Reactive forms semantics |
| Circular DI / provider scope surprises | `references/di.md` | Injector hierarchy and tokens |
| Stale params / guard redirects / lazy loads | `references/routing.md` | Router observables and UrlTree |
| Cold requests / interceptor drops | `references/http.md` | HttpClient pipeline |
| Fast checklist before editing | `references/common-mistakes.md` | Highest-frequency traps |
| Source-backed claim refresh | `references/domain-knowledge.md` | Verified Angular / RxJS docs |

## Operating Rules

1. **Identify the layer before proposing a patch.** If the symptom could be change detection *or* a cold Observable, verify which one with one targeted check.
2. **Prefer framework lifetime helpers.** Reach for `async` pipe or `takeUntilDestroyed()` before manual `unsubscribe()` bookkeeping.
3. **Treat identity as the contract under OnPush.** Create a new object/array reference or call `markForCheck()` / signal updates when the view must refresh.
4. **Keep DI graphs explicit.** Use `forwardRef()` or restructure providers when a cycle appears; confirm whether a component `providers` entry intentionally creates a local instance.
5. **Use reactive forms APIs precisely.** Prefer `patchValue()` for partial updates and `getRawValue()` when disabled controls must be included.
6. **Subscribe to router Observables for same-component navigations.** Read `paramMap` / `queryParamMap` instead of a one-shot `snapshot` when the component instance is reused.
7. **Preserve the HTTP pipeline.** Every interceptor calls `next.handle(...)`, rethrows or remaps errors intentionally, and documents retry/backoff when retries are added.

## Output Expectations

When helping with an Angular defect, state:

1. The failing layer
2. The concrete API or operator to use next
3. The reference file that justifies the guidance

Keep answers operational. Load references only for the active layer instead of dumping the whole package.
