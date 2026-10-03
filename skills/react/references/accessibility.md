# Accessibility baseline

- Prefer native `button`, `a`, `label`, `input` — keyboard and focus come free.
- Every interactive control needs an accessible name (visible text,
  `aria-label`, or labelled-by).
- Do not rebuild click targets with `<div onClick>` unless role, tabIndex,
  and keyboard handlers are complete.
- Manage focus when opening/closing dialogs and after major view transitions.
- Support keyboard paths for the same actions mouse users get.
