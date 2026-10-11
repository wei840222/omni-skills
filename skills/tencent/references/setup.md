# Setup - Tencent

Use this file when the resolved `<state_root>` is missing or `<state_root>/memory.md` is empty.

Answer the immediate Tencent request first, then lock only the defaults that should repeat in future Tencent tasks.

## Immediate First-Run Actions

### 1. Lock activation behavior early

Within the first exchanges, clarify:

- should this activate for any Tencent-related request or only when named explicitly
- which Tencent surfaces it should cover by default: Tencent Cloud, WeChat ecosystem, WeCom, payments, ads, or corporate research
- when it should stay silent because a narrower skill owns the task better

Keep this short. One routing question is enough if the request is already specific.

### 2. Lock the region defaults that change the answer

Capture the defaults that materially change Tencent recommendations:

- target market or geography
- preferred documentation language
- whether mainland-only products are acceptable
- whether the user prefers official docs only or allows secondary analysis

If the user does not care, store a neutral default and make assumptions explicit in outputs.

### 3. Lock the preferred output shape

Choose the normal answer style for this workspace:

- quick routing recommendation
- decision matrix with tradeoffs
- implementation plan
- due-diligence checklist

Default to the lightest format that still prevents the usual Tencent confusion.

### 4. Prepare local state after routing is approved

Create only the already-resolved filesystem path for `<state_root>` (never the literal string `<state_root>`):

```bash
mkdir -p "$STATE_ROOT"
touch "$STATE_ROOT"/{memory.md,accounts.md,regions.md,sources.md,decisions.md}
chmod 700 "$STATE_ROOT"
chmod 600 "$STATE_ROOT"/{memory.md,accounts.md,regions.md,sources.md,decisions.md}
```

If `<state_root>/memory.md` is empty, initialize the baseline files from `assets/data-templates.md`.

### 5. What to save

Save only what helps later Tencent work:

- activation and silence preferences
- product families in scope
- user-stated account or tenant labels
- region and language defaults
- durable rollout blockers, trust rules, and final decisions

Before saving any account label, internal team name, or ongoing project note, confirm that the user wants it remembered.

## Guardrails

- Omit passwords, QR codes, cookies, SMS codes, or cloud access keys.
- Distinguish clearly between mainland and international Tencent surfaces.
- Verify inferred assumptions before storing them.
- Require explicit user approval before triggering account-changing actions.
