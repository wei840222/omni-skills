# Forms, wizards, uploads

## Simple server form

Login or single-shot server mutation: `useActionState` + `FormData` is enough.
`useFormStatus` on the submit control avoids pending prop drilling.

## Complex client validation

React Hook Form + Zod: uncontrolled inputs avoid per-keystroke rerenders.
Share one Zod schema between client and server when both validate.

## Wizards

One discriminated-union `status` field (e.g. `step | 'submitting' | 'error'`),
not a pile of booleans.

## Uploads

Track progress outside render-derived state as needed; abort on unmount;
never put secrets in client bundles.

## Optimistic

`useOptimistic` for snappy UI; on failure show the error and restore confirmed state.
