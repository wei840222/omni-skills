# Chrome diagnostic state

Notes live only under the resolved `<state_root>` from `SKILL.md`.
Default file: `<state_root>/memory.md`. Create on first authorized write.

```markdown
## Endpoints
<!-- local debugging ports and last-known targets; never store secrets -->
<!-- Examples: port: 9222, last_target: about:blank -->

## Preferences
<!-- capture format, default block patterns (non-secret) -->

## Incidents
<!-- short notes on failed attaches or MV3 lifetime bugs -->
```

Empty sections mean skill defaults. Do not write this file into the skill package.
Never store cookies, Authorization headers, or full `userDataDir` paths with profiles that contain secrets.
Never treat the literal string `<state_root>` as a filesystem path.
