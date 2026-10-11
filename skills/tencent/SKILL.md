---
name: tencent
description: >
  Route and plan Tencent Cloud, WeChat/WeCom, payments, ads, and corporate
  ecosystem decisions with region-aware guidance and official-source
  verification. Use when the user needs Tencent product routing, mainland
  versus global rollout planning, Mini Program or WeChat Pay context, or
  Tencent Cloud architecture choices. Prefer cloud-storage for generic object
  stores, payments for multi-provider checkout design, and market-research for
  non-Tencent China market strategy.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐧"}'
  related-skills: '{"cloud":"Consumer multi-cloud file sync when the task is not Tencent-specific infrastructure.","cloud-storage":"Multi-provider object/file transfer ops outside Tencent Cloud COS-focused planning.","in-depth-research":"Long-form multi-source investigation beyond Tencent product routing.","market-research":"Broader market and competitive research when Tencent is only one vendor.","payments":"Multi-provider payment architecture when WeChat Pay is one option among many."}'
---

## State location

Tencent state may exist in `<workspace>/tencent/`, `<workspace>/memory/tencent/`, or `~/tencent/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell's current working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/tencent/`, `<workspace>/memory/tencent/`, `~/tencent/`.
3. If none exists and state must be created, default to `<workspace>/tencent/`.

If multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and leave the others untouched. Use the selected `<state_root>` for every state operation during the run. Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy path `~/Clawic/data/tencent/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md` and follow it. Confirm with the user before the first write to `<state_root>`.

## When to use

Use this skill when the user needs help choosing, comparing, implementing, or de-risking something in the Tencent ecosystem:

- Tencent Cloud architecture, regions, and operations
- WeChat / WeCom / Mini Program decisions
- payments and ads context tied to Tencent surfaces
- mainland-versus-global rollout constraints
- official-doc verification when Tencent naming is ambiguous

Do not use it as a general China market strategy skill, or as a substitute for a dedicated product skill when the task is already narrowed to a single non-Tencent tool.

## Architecture

State layout, activation rules, and durable fields are described in [`references/state.md`](references/state.md). Baseline file templates live in [`assets/data-templates.md`](assets/data-templates.md).

```text
<state_root>/
|- memory.md           # Activation rules, product scope, and preferred outputs
|- accounts.md         # Known tenants, products, and ownership boundaries
|- regions.md          # Mainland, Hong Kong, Singapore, and global rollout notes
|- sources.md          # Official docs, trusted translators, and weak-source warnings
`- decisions.md        # Final recommendations, assumptions, and open risks
```

## Quick reference

Load the smallest relevant file for the current task.

| Topic | File | Use it for |
|-------|------|------------|
| Setup flow and saved defaults | `references/setup.md` | Initialize local state and activation rules |
| Memory schema and status values | `assets/data-templates.md` | Create baseline local files |
| Tencent surface-area map | `references/ecosystem-map.md` | Route requests to the right product family |
| Product and vendor choice | `references/decision-framework.md` | Turn vague Tencent requests into a decision path |
| Tencent Cloud planning | `references/cloud-platform.md` | Map workloads, regions, and operations |
| Mainland-versus-global constraints | `references/mainland-vs-global.md` | Check region, residency, language, and go-live risks |
| Official-source handling | `references/source-validation.md` | Verify docs, translations, and time-sensitive claims |
| Delivery and escalation checklist | `references/rollout-checklist.md` | Final review before implementation or launch |
| Core rules and traps | `references/domain.md` | Domain guidelines, endpoints, and security |

## Primary workflow

Execute in order.

### Step 1: Resolve state

1. Resolve `<state_root>` with the State location procedure.
2. If state is missing and durable defaults would help later sessions, offer setup via `references/setup.md`.
3. Load only the durable files needed for the current request.

Done when: `<state_root>` is fixed or the task is treated as planning-only without writes.

### Step 2: Route the Tencent surface

1. Classify the request into one primary family using `references/ecosystem-map.md`.
2. If the request mixes families, split workstreams instead of blending owners.
3. State what this task excludes.

Done when: one primary surface owns the next actions.

### Step 3: Lock region, audience, and decision path

1. Make geography and audience explicit with `references/mainland-vs-global.md`.
2. Translate the business job into a decision path with `references/decision-framework.md`.
3. For Tencent Cloud workloads, map services and operational minimums with `references/cloud-platform.md`.

Done when: region, audience, and primary path are named, with rejected paths listed.

### Step 4: Verify sources and deliver

1. Check time-sensitive or high-stakes claims with `references/source-validation.md` and the endpoint table in `references/domain.md`.
2. Separate planning guidance from account-changing execution; require explicit approval before login or resource changes.
3. Close with `references/rollout-checklist.md` and a decision record.
4. Persist only user-approved durable outcomes under `<state_root>/`.

Done when: recommendation, assumptions, blockers, and required human confirmations are explicit.

## Requirements

- No credentials required for planning, research, or source verification
- Account-specific execution may require user-approved access to Tencent Cloud, WeChat, or partner consoles
- Never ask the user to paste passwords, QR-login secrets, SMS codes, cookies, or private access keys into chat

## Data storage

Save only durable context that improves later Tencent work:

- product families the user actually uses
- account or tenant names the user explicitly shares
- preferred regions, languages, and documentation sources
- repeated compliance or rollout constraints
- final decisions with open risks and follow-up items

Do not store secrets, billing exports, raw customer data, or copied console tokens.
