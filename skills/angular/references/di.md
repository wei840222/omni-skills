# Dependency Injection Traps

- Circular dependency crashes at runtime — break the cycle with `forwardRef()` or by restructuring providers
- Component `providers` creates a new instance for that component subtree — use root/`providedIn` when a shared singleton is required
- `@Optional()` missing returns `null` — null-check before dereferencing
- InjectionToken values need `@Inject(TOKEN)` — omitting it looks up by class name and fails
- `providedIn: 'any'` creates an instance per lazy-loaded environment — choose `root` for an app-wide singleton
- `useFactory` dependency order must match factory parameters — wrong order injects the wrong service
- Abstract class tokens usually need `useExisting` / `useClass` mapping — bare abstract tokens do not construct themselves
