# Security & Privacy

**Credentials:** this skill works with Xcode toolchain commands, which read signing identities from the login keychain and API keys from files the user controls. Ensure signing certificates, private keys, App Store Connect API keys, app-specific passwords, and demo-account passwords remain strictly outside `<state_root>/` without logging, copying, or transmitting them.

**Local storage:** app identifiers, capabilities, release history, rejections, measured baselines and platform notes stay in `<state_root>/` on this machine, plus device rows in the shared `<devices_state_root>/`. Identifiers only — no secrets.

**Guardrails:** commands are read-only by default. Anything that destroys user data or state (resetting a simulator or a device, wiping a keychain item, a lossy migration) names exactly what is lost and requires explicit confirmation before running.
