# Playbooks

Use these when the user needs execution, not theory.

## 1. New Domain Launch Sprint

- verify SPF, DKIM, DMARC alignment
- enable one-click unsubscribe and postal address footer
- start warmup volume with engaged seed segment only
- watch Postmaster spam rate and hard bounces daily during ramp

## 2. Spam-Folder Recovery Sprint

- freeze volume growth
- suppress unengaged and recently complained cohorts
- re-check auth and List-Unsubscribe headers
- resume only with highly engaged segments and plain, expected content

## 3. List Hygiene Sprint

- remove hard bounces immediately
- run re-engagement then sunset for chronic non-openers
- block purchased-list intake paths
- document segment definitions in `<state_root>/lists.md` if user opts into state

## 4. Sequence Rebuild Sprint

- map triggers and exit criteria
- rewrite email 1 to deliver the promised value
- enforce frequency caps across automation + campaigns
- measure sequence completion and unsubscribe by step

## 5. Complaint Spike Containment

- identify last content, offer, and segment changes
- pause the offending campaign/automation
- strengthen preference center and one-click path
- do not “apologize blasts” to the full list without a clear opt-down path
