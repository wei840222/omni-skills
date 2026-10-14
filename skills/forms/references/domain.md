# Core domain rules (forms)

Load this file when designing field sets, conversion hygiene, spam controls, or
compliance gates. Keep answers tied to the user's use case.

## Use-case first

| Use case | Goal | Field posture |
| --- | --- | --- |
| Lead capture | Contact for follow-up | Minimal; delay qualification |
| Survey / research | Honest answers | Clear scales; optional open text |
| Job / program application | Decision-quality data | Multi-step; save progress |
| Feedback / CSAT / NPS | Fast signal | 1 primary score + optional why |
| Registration / event | Attendance ops | Required logistics only |

Do not copy a long application pattern onto a marketing lead form.

## Progressive disclosure

1. Ask the smallest set that unlocks the next decision.
2. Split into steps when cognitive load or sensitive uploads appear.
3. Show progress on multi-step flows; state a time estimate for long applications.
4. Capture contact **before** gated results only when the user accepted that bargain (quiz funnels).

## Conversion and length

- Extra fields usually reduce completion; treat each field as a cost.
- Practical lead-capture target: **at most about 7 fields**, fewer when cold traffic.
- Multi-step often beats one long scroll for 5+ fields if each step is short.
- Do not invent exact industry-wide “% drop per field” numbers without a cited study for that context.

## Validation and errors

- Client checks for speed; **server checks for authority**.
- Validate on blur where it helps; restate errors near the field with recovery text.
- Success states must confirm what happened (email sent, ticket opened, next step).

## Accessibility and mobile

- Visible labels (not placeholder-only).
- Associate errors with controls; keep focus management sane after submit failures.
- Touch targets and keyboard types (`email`, `tel`, numeric) matter more than desktop chrome.
- Test real devices for autofill, zoom, and soft-keyboard overlap.

## Spam and abuse

- Default: honeypot field + server rate limit + webhook signature verification.
- Escalate to CAPTCHA/Turnstile when automated abuse is evidenced.
- File uploads: allowlist extensions/MIME, size cap, store outside web root, scan when risk warrants.

## Privacy

- Know lawful basis before collecting EU personal data; link privacy policy on consent controls.
- Minimize retention of submissions; do not paste live PII into reusable skill state.
- Health/finance/HR forms may force self-host or vetted enterprise SaaS — ask before defaulting to a free consumer tool.

## Conditional logic

Document branches as `IF field=value THEN show|hide|require field`.
Implement with the platform’s native logic (Typeform logic jumps, SurveyJS conditions, RHF `watch`, etc.) — do not invent a universal DSL in production code without mapping it.

## Positive steering (Gate 9)

Prefer instructions that name the desired behavior ("validate on blur and on the server", "limit lead capture to the fields you will use this week") over stacks of bare prohibitions. Keep hard safety limits, but pair each with the allowed path.
