# Tencent State Management

## Architecture

Memory lives under the resolved `<state_root>/`. If `<state_root>` does not exist yet, run `references/setup.md`. See `assets/data-templates.md` for structure.

```text
<state_root>/
|- memory.md           # Activation rules, product scope, and preferred outputs
|- accounts.md         # Known tenants, products, and ownership boundaries
|- regions.md          # Mainland, Hong Kong, Singapore, and global rollout notes
|- sources.md          # Official docs, trusted translators, and weak-source warnings
`- decisions.md        # Final recommendations, assumptions, and open risks
```

## Data Storage

Save only durable context that improves later Tencent work:

- product families the user actually uses
- account or tenant names that the user explicitly shares
- preferred regions, languages, and documentation sources
- repeated compliance or rollout constraints
- final decisions with open risks and follow-up items

Store only safe context; omit secrets, billing exports, raw customer data, or copied console tokens.

## Requirements

- No credentials required for planning, research, or source verification
- Account-specific execution may require user-approved access to Tencent Cloud, WeChat, or partner consoles
- Omit passwords, QR-login secrets, SMS codes, cookies, or private access keys into chat
