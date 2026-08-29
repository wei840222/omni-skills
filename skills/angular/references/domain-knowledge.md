# Domain Knowledge

Stable Angular/RxJS rules used by this skill, grounded in current official docs.

## Change detection and queries

- Default change detection walks the component tree; `OnPush` skips a subtree until an input reference changes, an event originates from the component/template, an async pipe emits, or the code marks the view for check via `ChangeDetectorRef`.
- `markForCheck()` marks the current view and its ancestors so the next detection cycle includes them.
- Signals integrate with Angular's reactivity model and are the preferred way to express local reactive state in modern apps.
- View queries such as `@ViewChild` resolve after the view initializes; read them from `ngAfterViewInit` or later unless using signal queries designed for later updates.

## RxJS lifetimes

- `takeUntilDestroyed()` completes the source when the surrounding injectable/component is destroyed, but it must be called in an injection context.
- Prefer the `async` pipe in templates when the only goal is to bind an Observable to the view; it subscribes and unsubscribes with the view.
- `shareReplay({ bufferSize: 1, refCount: true })` shares a cold source while subscribers remain, then unsubscribes when the refcount hits zero.

## Dependency injection

- The injector hierarchy resolves tokens from the local injector upward.
- `forwardRef()` defers token evaluation so mutually referencing classes can be declared safely.
- Component-level `providers` create a new instance for that component subtree rather than reusing the root singleton.

## Forms and HTTP

- Reactive `FormGroup.setValue()` requires a value for every control; `patchValue()` updates a subset.
- Disabled controls are omitted from `.value` and included in `getRawValue()`.
- Async validators run only after synchronous validators succeed.
- `HttpClient` methods return cold Observables; each subscription triggers a request unless shared.
- HTTP interceptors form a chain and must call `next.handle(...)` to continue the request.

## Routing

- `ActivatedRoute.snapshot` captures route state once; reuse of the same component instance requires Observable `paramMap` / `queryParamMap` reads.
- Guards can return a `UrlTree` to redirect instead of a bare `false` that leaves navigation unresolved.

## Sources

### Change detection / signals / queries
- **Angular change detection guide** — OnPush and detection triggers via https://angular.dev/guide/change-detection
- **Angular signals guide** — signal-based reactivity via https://angular.dev/guide/signals
- **ChangeDetectorRef API** — `markForCheck` semantics via https://angular.dev/api/core/ChangeDetectorRef
- **Component queries guide** — query timing via https://angular.dev/guide/components/queries

### DI / forms / HTTP / routing / RxJS
- **Angular DI guide** — injector hierarchy and `forwardRef` via https://angular.dev/guide/di
- **Dependency injection in action** — provider patterns via https://angular.dev/guide/di/dependency-injection
- **Angular forms overview** — reactive vs template-driven via https://angular.dev/guide/forms
- **Reactive forms guide** — `setValue` / `patchValue` behavior via https://angular.dev/guide/forms/reactive-forms
- **HttpClient making requests** — cold Observables via https://angular.dev/guide/http/making-requests
- **HTTP interceptors** — interceptor chain requirements via https://angular.dev/guide/http/interceptors
- **Common router tasks** — snapshot vs Observable params via https://angular.dev/guide/routing/common-router-tasks
- **takeUntilDestroyed API** — injection-context lifetime helper via https://angular.dev/api/core/rxjs-interop/takeUntilDestroyed
- **shareReplay API** — refCount sharing behavior via https://rxjs.dev/api/index/function/shareReplay
