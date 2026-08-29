# Common Mistakes

Use this as a fast pre-edit checklist. Prefer the positive replacement on each line.

- OnPush with mutated objects stays stale — create a new reference (`{...obj}` / `[...arr]`) or call `markForCheck()` / update a signal
- `@ViewChild` is read too early — access it in `ngAfterViewInit` or later
- `*ngFor` rebuilds the whole list — add `trackBy` returning a stable id
- Manual `subscribe()` outlives the component — use `async` pipe, `takeUntilDestroyed()`, or unsubscribe in `ngOnDestroy`
- Repeated `HttpClient` `subscribe()` refires the request — share with `shareReplay({ bufferSize: 1, refCount: true })` when reuse is intended
- `setTimeout` / `setInterval` outside NgZone skip detection — run UI updates through `NgZone.run()` or signals
- Circular DI crashes bootstrap — insert `forwardRef()` or restructure providers
- Direct `ElementRef.nativeElement` access breaks SSR — use `Renderer2` or defer browser-only work
- Route `snapshot` misses same-component navigations — subscribe to `paramMap`
- `setValue()` on FormGroup requires every control — use `patchValue()` for partial updates
