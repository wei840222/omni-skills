# JSON Domain Knowledge

## Overview
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write and easy for machines to parse and generate (ECMA-404, RFC 8259).

## Key Characteristics and Standards
- **Data Types**: JSON supports strings, numbers, objects (name-value pairs), arrays, booleans, and null.
- **Numbers**: The JSON specification does not define limits on the precision or range of numbers, but interoperability issues arise when numbers cannot be accurately represented by double-precision floating-point format (IEEE 754), common in JavaScript. Integers larger than \(2^{53}-1\) are often sent as strings to prevent precision loss.
- **Dates**: JSON lacks a native date type. Dates are typically serialized as strings, frequently in ISO 8601 / RFC 3339 format (e.g., `2024-01-01T12:00:00Z`).
- **Parsing**: Standard parsing behavior (e.g. `JSON.parse` in JS) strictly enforces syntax. Duplicate keys are valid per spec but are usually handled by parsers taking the last value.

## JSON Schema
JSON Schema (e.g., drafts 2020-12, 2019-09, draft-07) defines vocabulary that allows annotation and validation of JSON documents. Key concerns when using schemas include proper use of `$ref` for composition, managing `additionalProperties` and `unevaluatedProperties`, and clear error reporting.

## Tooling
- **jq**: A lightweight and flexible command-line JSON processor. It allows filtering, mapping, and transforming structured data.
- **JSON Path / JMESPath**: Query languages for extracting elements from a JSON document.
- **Streaming**: For very large datasets, NDJSON (Newline Delimited JSON) is often used, where each line is a valid JSON value, reducing the memory overhead of parsing an entire array into memory.

## Security
- **Prototype Pollution**: Vulnerabilities where properties like `__proto__` can be injected through recursive merges during JSON parsing or processing.
- **Denial of Service**: Processing excessively deep or large JSON payloads can consume significant CPU and memory. Strict payload size and depth limits should be applied at boundaries.
