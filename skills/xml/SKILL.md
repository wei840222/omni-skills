---
name: xml
description: >
  Parse, generate, and transform XML documents. Use when handling XML
  namespaces, encodings, XPath queries, entity escaping, CDATA, schema
  validation (DTD/XSD/RelaxNG), or whitespace-sensitive processing.
metadata:
  openclaw: '{"emoji": "📄"}'
---
## Namespaces

- When querying a document with a default namespace, use `//*[local-name()='child']` or register a prefix, since `/root/child` requires explicit namespaces.
- Default namespace (`xmlns="..."`) applies to elements, not attributes—attributes need explicit prefix
- Namespace prefix is arbitrary—`<foo:element>` and `<bar:element>` are identical if both prefixes map to same URI
- Each child element must declare or use a prefix explicitly, as parent's prefixed namespaces are not inherited.

## Encoding

- `<?xml version="1.0" encoding="UTF-8"?>` must match actual file encoding—mismatch corrupts non-ASCII
- The encoding declaration must be the first thing in the file (only a UTF-8 BOM is permitted before it); ensure no other whitespace or BOM precedes it.
- Default encoding is UTF-8 if declaration omitted—however, explicitly declaring it ensures consistent behavior across parsers

## Escaping & CDATA

- Five entities always escape in text: `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`
- CDATA sections `<![CDATA[...]]>` for blocks with many special chars—ensure `]]>` does not appear inside CDATA to maintain valid structure
- Attribute values: use `&quot;` if delimited by `"`, or `&apos;` if delimited by `'`
- Numeric entities `&#60;` and `&#x3C;` work everywhere—useful for edge cases

## Whitespace

- Whitespace between elements is preserved by default—pretty-printing adds nodes that may break processing
- `xml:space="preserve"` attribute signals whitespace significance—although parser behavior on this attribute varies
- Normalize-space in XPath: `normalize-space(text())` trims and collapses internal whitespace

## XPath Pitfalls

- `//element` is expensive—traverses entire document; use specific paths when structure is known
- Position is 1-indexed: `[1]` is first, not `[0]`
- `text()` returns direct text children only—use `string()` or `.` for concatenated descendant text
- Boolean in predicates: `[@attr]` tests existence, `[@attr='']` tests empty value—different results

## Structure

- Self-closing `<tag/>` and empty `<tag></tag>` are semantically identical—although some legacy systems require explicit closing tags
- Avoid using `--` inside comments to maintain parser stability, as it is invalid syntax.
- Ensure processing instructions `<?target data?>` are free of `?>` in their data payload.
- A root element is required; documents containing only comments or PIs are invalid.

## Validation

- Well-formed ≠ valid—parser may accept structure but fail against schema
- While DTD validates structure, prefer XSD or RelaxNG for expressing complex constraints in new projects.
- XSD namespace `xmlns:xs="http://www.w3.org/2001/XMLSchema"` commonly confused with instance namespace
