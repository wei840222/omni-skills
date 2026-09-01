---
name: baidu
description: Route Baidu Search, Baike, Wenku, Maps, AI Cloud, and Qianfan work using region-aware assumptions and official sources. Use for Baidu product research, planning, source checks, or account-bound implementation; use a narrower skill for one known endpoint or console workflow.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"B"}'
  related-skills: '{"maps":"Handles deeper geospatial and map-platform workflows after Baidu surface routing.","market-research":"Frames competitive and ecosystem analysis beyond a single Baidu product.","monitoring":"Adds thresholds, status rules, and recurring checks to an approved Baidu workflow.","tencent":"Supports a comparison with another China-focused platform when vendor tradeoffs matter.","web":"Inspects specific pages after Baidu routing identifies the target surface."}'
---

## State location

Baidu state may exist in `<workspace>/baidu/`, `<workspace>/memory/baidu/`, or `~/baidu/`.
Before a state operation, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when available.
2. Otherwise use the first existing directory in this order: `<workspace>/baidu/`, `<workspace>/memory/baidu/`, then `~/baidu/`.
3. If none exists and the user has approved saving state, create `<workspace>/baidu/`.

Use the selected `<state_root>` for every state operation. When more than one candidate exists, use the highest-precedence path, report the duplicate state, and leave lower-precedence paths unchanged.

## When to use

Use this skill when a request involves Baidu Search, Baike, Wenku, Maps, AI Cloud, Qianfan, or Baidu-wide vendor research. First select one primary surface, state the target geography and documentation language, then separate public research from account execution.

## Workflow

1. **Route the request.** Read `references/ecosystem-map.md` for an ambiguous request or one spanning multiple Baidu products.
2. **Set region assumptions.** Read `references/mainland-vs-global.md` whenever geography, language, availability, or rollout could change the answer.
3. **Choose evidence.** Read `references/search-knowledge.md` for Search, Baike, or Wenku work; read `references/source-validation.md` and `references/official-sources.md` before treating a discovery result as support for an important claim.
4. **Plan the product path.** Read `references/qianfan-cloud.md` for AI Cloud or Qianfan questions. Keep product selection, model workflow, and cloud operations as separate decisions.
5. **Prepare durable state only when needed.** Read `references/setup.md` and `references/memory-template.md` after the user approves saving reusable Baidu preferences or decisions.
6. **Close safely.** Read `references/execution-checklist.md` before recommending account-level execution or delivering a high-impact recommendation.

## Surface map

| Surface | Route here when | Official starting point |
|---|---|---|
| Search and discovery | Finding current pages, trends, or official statements | `https://www.baidu.com` |
| Knowledge and documents | Getting orientation or document leads from Baike or Wenku | `https://baike.baidu.com`, `https://wenku.baidu.com` |
| Maps and local data | Geocoding, routing, nearby search, or local-platform implementation | `https://map.baidu.com`, `https://lbsyun.baidu.com` |
| AI Cloud and Qianfan | Model, agent, AI platform, or cloud implementation work | `https://cloud.baidu.com`, `https://qianfan.cloud.baidu.com` |
| Corporate research | Assessing Baidu as a company, vendor, or ecosystem | `https://ir.baidu.com` |

## Execution boundary

Planning, source comparison, and workflow design are safe defaults. Before console login, key creation, cloud-resource changes, map-key submission, or billing activity, identify the owner and obtain explicit approval for that account and action.

Store only user-approved durable planning context under `<state_root>`: selected surfaces, region and language defaults, source preferences, account labels, decisions, and open risks. Keep passwords, codes, cookies, refresh tokens, private keys, billing exports, and raw customer data outside the state record.

## Decision record

For non-trivial work, state the chosen surface, region and language assumptions, source tier, rejected paths, required approval, and next verification step.

## Common traps

- A Baidu label can cover distinct Search, knowledge, Maps, and Qianfan products; route the actual product before proposing a workflow.
- Search ranking, Baike content, and Wenku documents are discovery signals; use the strongest available primary source for material claims.
- Mainland-first and global workflows can differ in language, availability, ownership, and rollout constraints; make the selected context explicit.
- Account execution has its own permission and billing boundary even when public research is complete.
