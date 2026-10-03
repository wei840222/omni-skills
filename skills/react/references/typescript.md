# TypeScript for React components

## Props

- Export props interfaces/types next to the component.
- Prefer discriminated unions for variants over optional boolean piles.
- Event handlers: use React's event types (`React.ChangeEvent<HTMLInputElement>`).

## Strictness

- `strict` + `noUncheckedIndexedAccess`: treat `array[0]` as `T | undefined`.
- Prefer `unknown` + narrowing over `any`.

## Generics

- Generic components when the consumer supplies item/value types; do not
  over-abstract on first use (second consumer rule still applies).
