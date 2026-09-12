# Accessibility patterns

Load for contrast, names, keyboard paths, images, and forms.

## Images

| Intent | Pattern |
|---|---|
| Informative | Descriptive `alt` that conveys the same meaning |
| Decorative | `alt=""` and no redundant title |
| Functional (linked/icon-only) | Accessible name on the control (`aria-label` or visible text); see also `icons` |

## Forms

- Every input has a visible `<label for>` / wrapping `<label>`.
- Group related controls with `<fieldset>` + `<legend>` when the group name matters.
- Error text is linked programmatically (`aria-describedby`) and not color-only.
- Do not rely on placeholder-as-label; placeholders disappear on input.

## Keyboard and focus

- All interactive controls reachable in a logical Tab order.
- Visible `:focus-visible` styles; never `outline: none` without a replacement.
- Modals/dialogs trap focus and restore it on close; Escape dismisses when expected.
- Custom widgets implement the keyboard contract of their ARIA role.

## Structure and contrast

- One logical heading outline; do not skip levels for visual size.
- Text contrast: 4.5:1 normal, 3:1 large; UI component contrast 3:1 against adjacent colors.
- Do not convey state by color alone — pair with text, icon, or pattern.
- `lang` on `<html>` (and on passages in another language).

## Quick checks

1. Navigate the page with keyboard only.
2. Zoom to 200% — content reflows without horizontal scroll traps.
3. Run an automated pass (axe/Lighthouse a11y) then fix false confidence with manual review.
4. Spot-check with a screen reader on critical flows (nav, form, errors).
