# Sources — JavaScript

Primary references for language semantics, runtime floors, and platform edges. Re-check the linked docs before quoting API availability or behavior that varies by engine.

## Language and specification

- ECMAScript® 2024 Language Specification — https://tc39.es/ecma262/
- TC39 Finished Proposals (stage progression context) — https://github.com/tc39/proposals/blob/main/finished-proposals.md
- MDN JavaScript Guide — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- MDN JavaScript reference — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

## Equality, numbers, dates, Unicode

- MDN Equality comparisons and sameness — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness
- MDN Number.EPSILON — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON
- MDN Date parsing and time values — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
- MDN Intl.Segmenter — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter
- Unicode Standard Annex #29 (text segmentation) — https://unicode.org/reports/tr29/

## Async, promises, abort

- MDN Using promises — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises
- MDN Promise — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- MDN AbortController — https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- MDN AbortSignal.timeout() — https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static

## Node.js runtime edges

- Node.js process documentation — https://nodejs.org/api/process.html
- Node.js stream promises (pipeline) — https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-options
- Node.js Buffer — https://nodejs.org/api/buffer.html
- Node.js unhandled promise rejections — https://nodejs.org/api/process.html#event-unhandledrejection

## Browser runtime edges

- MDN Fetch API — https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN Window: unhandledrejection event — https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event
- HTML Living Standard (scripting / events context) — https://html.spec.whatwg.org/multipage/

## Agent Skills package contract

- Agent Skills Specification — https://agentskills.io/specification.md
- Agent Skills Best Practices — https://agentskills.io/skill-creation/best-practices.md

## Scope notes

- TypeScript type-system design belongs to `typescript`.
- Node platform operations beyond language edges belong primarily to `nodejs`.
- Framework-specific React internals belong to `react`.
