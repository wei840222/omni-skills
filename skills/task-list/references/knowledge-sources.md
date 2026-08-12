# Knowledge sources

Use this record when verifying date or recurrence guidance. It documents external facts used by the skill; it is not an instruction to integrate with a calendar service.

## Calendar recurrence semantics

- Internet Engineering Task Force, RFC 5545: Internet Calendaring and Scheduling Core Object Specification (iCalendar). https://www.rfc-editor.org/rfc/rfc5545.html
  - Key points: recurrence instances are defined relative to a start value, recurrence rules can be unbounded without a limiting rule part, and date-time interpretation depends on the associated value type and timezone parameters. The skill therefore preserves the user’s stated anchor and timezone and does not infer or translate calendar recurrence syntax.
