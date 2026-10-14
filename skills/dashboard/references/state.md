# Data Storage

After resolving `<state_root>` (see `SKILL.md` State location), use this layout:

```text
<state_root>/dashboard/
├── registry.json           # Dashboard index
├── {name}/
│   ├── config.json         # Layout, widgets
│   ├── data.json           # Current data snapshot
│   ├── fetch.sh            # Optional user-run collector
│   └── index.html          # Dashboard page
```

Create on first confirmed use:

```bash
mkdir -p "$STATE_ROOT/dashboard"
```

`$STATE_ROOT` is the resolved filesystem path for `<state_root>`. Never mkdir the literal characters `<state_root>`.
