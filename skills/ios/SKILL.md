---
name: ios
description: 'Builds, ships, and debugs native iOS apps: lifecycle, permissions, entitlements, push, widgets, StoreKit, and App Store review. Use when a submission is rejected, permission prompt fails to appear, missing-entitlement error occurs, background task fails, universal link fails, app crashes/hangs, widget runs out of memory, purchases fail, privacy manifest is required, layout breaks, or new iOS release breaks an app. Route tasks involving Swift language mechanics, Xcode IDE settings, Store listings, or cross-platform apps to the respective skills.'
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"📱","os":["darwin"],"requires":{"bins":["xcodebuild"]}}'
  related-skills: '{"app-store":"Handles store listings and submission workflow.","app-store-connect":"Uses the ASC API for automating builds, metadata and analytics.","flutter":"Cross-platform framework for building apps.","react-native":"Cross-platform framework for building apps.","swift":"Handles Swift language mechanics: concurrency, ARC, optionals, Codable, packages.","testflight":"Handles beta distribution, tester management, and build expiry.","xcode":"Handles IDE, build settings, signing, provisioning, derived data."}'
---
## State location

iOS state may exist in `<workspace>/ios/`, `<workspace>/memory/ios/`, or `~/ios/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/ios/`, `<workspace>/memory/ios/`, `~/ios/`.
3. If none exists and state must be created, default to `<workspace>/ios/`.

Use the selected `<state_root>` for every state operation in this skill.

Device inventory is shared across skills; resolve its state root similarly, preferring `<workspace>/devices/`, `<workspace>/memory/devices/`, `~/devices/`.
Project and contact state should also be resolved to a workspace-first `<state_root>` (e.g., `<workspace>/contacts/`, `<workspace>/projects/`, `<workspace>/finances/`).

## Setup and Data

At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Declarations explicitly win over observations: where the two disagree, `config.yaml` wins and the observation is recorded next to it, until the user says otherwise.
Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, treat the index as an expandable list. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared — keep data exclusively on the machine and strip all credentials before writing.

In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; read rows written by other skills without modifying or deleting them, and every write and deletion is named in one line as it happens. Read `<state_root>/devices.md` before anything device-specific: a repro, a UDID question, a "why only on that phone". If none of it exists, work from defaults and say nothing about it.

Write before the session ends whenever it produced something durable. If `<state_root>/memory-template.md` exists, use it as the only write-routing file for destinations, formats, and thresholds; otherwise write durable notes to `<state_root>/memory.md` with a one-line destination label.

Test devices go to the shared inventory `<state_root>/devices.md`, not here: one file holds every phone, tablet and box the user owns. When an app is client work, the client goes to `<state_root>/contacts.md` and the engagement to `<state_root>/<project>.md`.

Strip all credentials from data before saving to `<state_root>/`. Store the pointer and strip the value. App Review demo-account passwords are credentials too.

Every iOS defect belongs to exactly one of five layers: the process lifecycle, an entitlement, a permission, a resource budget, or the platform version. Name the layer before proposing a fix. Precedence for any value: `config.yaml` → `<workspace>/profile.yaml` (shared universals) → the Configuration table default.

## Reference Loading Instructions

When handling tasks, explicitly load the following references as needed by reading the corresponding file in `references/`:

- Load `references/quick-reference.md` to see common problems and the recommended playbook.
- Load `references/core-rules.md` for foundational rules on deployment targets, budgets, permissions, and app review.
- Load `references/termination-codes.md` when diagnosing an app termination, hang, or crash.
- Load `references/budgets-and-ceilings.md` for memory, background execution, timeline refresh, and capability limits.
- Load `references/permission-map.md` when diagnosing missing purpose strings, permission prompts, or faceless failures.
- Load `references/output-gates.md` for the checklist of items to verify before shipping code or changes.
- Load `references/configuration.md` for the default variables and preferences you should consult in `<state_root>/config.yaml`.
- Load `references/traps.md` to avoid common mistakes with permissions, testing, keychain, and App Review.
- Load `references/where-experts-disagree.md` to understand subjective technology choices (e.g., SwiftUI vs UIKit).
- Load `references/security-privacy.md` for rules on credential handling, local storage, and guardrails for destructive commands.
- Load `references/sources.md` for the primary Apple documentation URLs that back platform claims in this skill.
