# Output Gates

Before sending Angular guidance, confirm:

1. The failing layer is named (change detection, RxJS, DI, forms, routing, or HTTP).
2. The next action uses a concrete Angular/RxJS API rather than a vague rewrite.
3. Only the matching reference file was loaded for the active layer.
4. Lifetime guidance prefers `async` pipe or `takeUntilDestroyed()` over open-ended subscriptions.
5. OnPush advice creates a new reference, updates a signal, or calls `markForCheck()`.
6. Forms advice uses `patchValue()` / `getRawValue()` when partial or disabled values matter.
7. Router advice uses Observable params for reused components and `UrlTree` for intentional redirects.
