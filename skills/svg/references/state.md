# SVG preference state

Preferences live only under the resolved `<state_root>` from `SKILL.md`.
Default file: `<state_root>/memory.md`. Create on first authorized write.

```markdown
## User Preferences
<!-- SVG workflow defaults. Format: "setting: value" -->
<!-- Examples: default_viewbox: 0 0 24 24, prefer_inline: true -->

## Accessibility Mode
<!-- informative | decorative -->

## Optimization
<!-- Tool and settings. Format: "tool: setting" -->
<!-- Examples: svgo: preserve-viewbox-title, remove_metadata: true -->

## Icon Defaults
<!-- Fill and sizing preferences -->
<!-- Examples: fill: currentColor, default_size: 24x24 -->
```

Empty sections mean skill defaults. Do not write this file into the skill package.
Never treat the literal string `<state_root>` as a filesystem path.
