---
name: csv
description: Parse, validate, and generate CSV or delimited text safely across spreadsheets and programs. Use when importing, exporting, cleaning, or troubleshooting CSV, TSV, or delimiter-separated data; not for native spreadsheet workbook editing.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
---

## Choose an interchange contract

Before parsing or generating data, identify the producer, consumer, delimiter, encoding, header policy, and whether a spreadsheet will open the file. Treat semicolon-, tab-, and pipe-delimited data as explicit dialects rather than assuming they are RFC 4180 CSV. When the producer contract is unavailable, sample multiple records, test a small delimiter allowlist, and validate the selected dialect against the full file before transforming it.

For an RFC 4180-compatible profile, use commas, `CRLF` record terminators, an optional first-row header, and a consistent field count. The final record may include or omit its terminating line break.

## Parse and validate with a CSV library

Use a parser configured for the agreed dialect; it preserves quoted delimiters and quoted line breaks. Record the source encoding explicitly, or obtain it from the producer. A byte-order mark is a consumer-specific compatibility choice, so generate it only for a documented consumer profile and test the resulting file with that consumer.

If Python is the selected runtime, open files with `newline=''` and let `csv.reader` or `csv.writer` handle quoting and record boundaries:

```python
import csv

with open("input.csv", newline="", encoding="utf-8") as source:
    rows = list(csv.reader(source))

with open("output.csv", "w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target, lineterminator="\r\n")
    writer.writerows(rows)
```

Validate the output contract before delivery:

1. Parse the generated file again with the same declared dialect.
2. Verify every data row has the expected field count, or report intentional ragged rows with their record numbers.
3. Compare row count and a representative set of exact field values with the source.
4. Report the delimiter, encoding, header decision, and any normalization performed.

## Recovery path

If parsing, field-count validation, or the reparse check fails, retain the original input and report the selected dialect, encoding, physical record number, and parser error. Continue only with an explicit producer contract or a user-selected candidate profile that passes the same validation checks. Preserve an untouched source copy whenever a normalization changes values or delimiters.

## Quoting and value semantics

- Enclose fields containing the delimiter, a double quote, or a line break in double quotes; an embedded double quote becomes `""`.
- Quote fields whose leading or trailing whitespace must survive consumers that trim unquoted values.
- Preserve the producer's distinction only when its parser supports it: many CSV readers return both `,,` and `,"",` as empty strings. For a durable null-versus-empty distinction, carry an explicit schema or use a format with typed nulls.
- Keep identifiers, postal codes, and other numeric-looking text as text by defining the column type in the consumer profile. Use an unambiguous documented date format such as `YYYY-MM-DD` when dates are exchanged as text.

## Spreadsheet delivery profile

For data that will be opened in spreadsheet software, evaluate every untrusted field before writing it. A field beginning with `=`, `+`, `-`, `@`, tab, carriage return, or line feed can become a formula or start a new cell after parsing. Apply quoting to every emitted field and use a spreadsheet-specific sanitization profile for those dangerous prefixes.

For Microsoft Excel recipients, OWASP documents a tab prefix inside the quoted field as an Excel-resistant mitigation for `=`, `+`, `-`, and `@`. It deliberately changes the underlying value, so disclose that transformation and keep a separate lossless export profile for programmatic consumers. Re-opening and saving a CSV in Excel can invalidate weaker escaping strategies.

Excel stores at most 15 digits of numeric precision. Deliver identifiers with 16 or more digits, leading-zero codes, and literal scientific-notation-looking values as text according to the recipient's documented import process.

## Delivery boundaries

Use a native-workbook workflow for `.xlsx` formatting, formulas, charts, or workbook-level editing. Keep CSV delivery focused on the declared text interchange contract and the validation evidence for that output.

## Source anchors

- RFC 4180 CSV grammar and `text/csv`: https://www.rfc-editor.org/rfc/rfc4180.html
- Python CSV parsing, dialects, and `newline=''`: https://docs.python.org/3/library/csv.html
- Spreadsheet formula-injection risks and trade-offs: https://owasp.org/www-community/attacks/CSV_Injection
- Excel text formatting and 15-digit precision: https://support.microsoft.com/en-us/excel/format-numbers-as-text
