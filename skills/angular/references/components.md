# Components Traps

- `@ViewChild` is available after view init — read it in `ngAfterViewInit` or later
- OnPush ignores in-place object mutations — create a new reference, update a signal, or call `markForCheck()`
- `ngOnChanges` reacts to reference changes — replace the parent object/array when the child must notice
- `@Output` EventEmitter needs `.emit(...)` — calling the property without `emit` does nothing
- `@Input({ required: true })` is mainly a compile-time check — still guard runtime undefined when data can arrive late
- `ngAfterContentInit` runs before `ngAfterViewInit` — projected content is ready before the component's own template queries
- `@HostListener` callbacks can outlive the view — pair them with `takeUntilDestroyed()` or remove the listener on destroy
