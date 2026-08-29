# Forms Traps

- `setValue()` requires every FormGroup control — use `patchValue()` for partial updates
- `valueChanges` can emit before the value settles — debounce or inspect the latest value in the subscription
- Async validators run only after synchronous validators succeed — fix sync errors first when async work never starts
- `updateOn: 'blur'` on a FormGroup does not cascade automatically — set it on each control that needs blur updates
- Disabled controls are omitted from `.value` — call `getRawValue()` when disabled fields must be included
- Untyped `FormArray` erodes control types — prefer typed `FormArray<FormControl<T>>` or `FormRecord`
- Mixing template-driven `[(ngModel)]` with reactive `formControlName` on the same input breaks binding — pick one forms API
