## Strings

- Basic strings (`"..."`) support escapes such as `\n`, `\t`, `\\`, and `\"`.
- Literal strings (`'...'`) preserve backslashes and do not process escape sequences.
- Multiline basic strings (`"""..."""`) and multiline literal strings (`'''...'''`) support line breaks; multiline basic strings process escapes.

## Keys and tables

- Bare keys use ASCII letters, digits, underscores, and dashes. Quote keys containing other characters.
- Dotted keys such as `a.b.c = 1` define nested values. Define each key path once; a later definition that conflicts with an existing value is invalid.
- `[table]` selects a table for following key/value pairs. `[a.b.c]` selects a nested table.
- `[[array]]` appends a new table to an array of tables. Define a given name consistently as either a table or an array of tables.

## Values

- Integers support decimal, hexadecimal (`0x`), octal (`0o`), binary (`0b`), and underscores for readability.
- Floats include decimal notation, exponent notation, `inf`, and `nan`; booleans are lowercase `true` or `false`.
- TOML has no null value. For an optional setting, omit its key when the consuming application supports that behavior.
- Arrays may contain values of different types, although consistently typed arrays are easier for consumers to interpret.
- Inline tables such as `point = { x = 1, y = 2 }` are self-contained: define every key while creating the table and keep the table on one physical line for TOML 1.0 compatibility.
- TOML 1.1 adds features beyond 1.0. Choose the version required by the target parser before relying on newer syntax.

## Dates, times, and comments

- Offset date-times use RFC 3339 syntax, for example `2024-01-15T14:30:00Z` or `2024-01-15T14:30:00+05:30`.
- Local date-times, dates, and times omit an offset, for example `2024-01-15T14:30:00`, `2024-01-15`, and `14:30:00`.
- Place `#` comments outside string values. A comment may follow a value on the same line.

## Validation routine

1. Confirm each key has one definition and each table name has a consistent shape.
2. Check strings, date-times, and numeric bases against TOML syntax.
3. Parse with the target tool or language runtime when available, then use its line and column to correct the source.

## Sources

- TOML v1.0.0 specification: https://toml.io/en/v1.0.0
- TOML v1.1.0 specification: https://toml.io/en/v1.1.0
