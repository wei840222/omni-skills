# SVG optimization

## SVGO destructive defaults

Default SVGO presets can remove authoring-critical attributes. Override explicitly and **verify output**:

```javascript
// svgo.config.mjs — illustrative overrides; confirm against installed SVGO docs
export default {
  plugins: [{
    name: 'preset-default',
    params: {
      overrides: {
        removeViewBox: false,
        removeTitle: false,
        removeDesc: false,
        cleanupIds: false,
      }
    }
  }]
};
```

Always re-check that `viewBox` and needed `<title>`/`<desc>` still exist after optimization. Confirm plugin names against https://svgo.dev/docs/preset-default/ for the installed major version.

## Usually safe to remove

- Editor metadata (Illustrator, Sketch, Figma cruft)
- XML comments
- Empty groups
- Unused `<defs>`
- Redundant attributes that do not affect rendering or a11y

## Icon system strategy

- **Fewer than ~10 icons:** inline SVG is fine
- **~10–50 icons:** symbol sprite is a common fit
- **Large sets:** consider lazy loading, subsetting, or a dedicated icon pipeline (`icons` skill)

## Checking file size

```bash
ls -la icon.svg
npx svgo icon.svg   # or project-local SVGO invocation
ls -la icon.svg
```

If reduction is tiny, the source was already clean — still verify semantic attributes survived.
