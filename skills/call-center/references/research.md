# Call Center Domain Research

## First Call Resolution (FCR)

Industry guidance treats FCR as a primary efficiency and experience metric. Call Centre Helper's FCR guide frames first-contact resolution as a core KPI and discusses realistic operating ranges rather than a single universal target. The refactored skill therefore uses an FCR band of **70-80%** instead of a bare `>75%` threshold, so agents optimize for complete resolution quality rather than gaming a single percentage.

Source: https://www.callcentrehelper.com/the-ultimate-guide-to-first-call-resolution-105108.htm

## Average Handle Time (AHT)

AHT remains useful for staffing and queue design, but Call Centre Helper notes that the "right" AHT target depends on contact type, complexity, and channel mix. The skill therefore keeps AHT as **3-6 minutes (context-dependent)** rather than implying one fixed handle-time SLA for every call.

Source: https://www.callcentrehelper.com/average-handle-time-aht-whats-the-right-target-147376.htm

## Customer Satisfaction (CSAT)

Qualtrics documents CSAT as a direct post-interaction satisfaction measure commonly expressed as a percentage of positive responses. The skill updates the CSAT target to **>85%** to match percentage-based CSAT reporting rather than a 5-point average that was easy to misread in voice-call workflows.

Source: https://www.qualtrics.com/experience-management/customer/what-is-csat/

## Obsolete Knowledge Corrected

- Replaced hardcoded `~/Clawic/data/call-center/` with portable `<state_root>` resolution.
- Removed Clawic homepage / feedback promotional content.
- Converted negative "What to Avoid" de-escalation framing into positive "Preferred Responses".
- Added identity-verification / account-takeover and fraud / money-laundering escalation cues for voice channels.
