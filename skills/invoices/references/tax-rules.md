# Tax Rules and Retention

## Electronic Invoicing Mandates

E-invoicing refers to issuing, transmitting, and receiving invoices in a structured electronic format that allows automatic processing.

### Key Formats:
- **ZUGFeRD** (Germany) / **Factur-X** (France): These are hybrid invoice formats containing both a visual PDF representation (PDF/A-3) and an embedded structured XML data file based on the EN 16931 European standard. OCR should generally be avoided if the embedded XML can be read, as the XML is the legally binding data.
- **XRechnung**: The standard for electronic invoicing to public administrations in Germany (B2G).
- **PEPPOL**: A network for exchanging electronic business documents across borders, particularly in Europe.
- **FatturaPA**: The mandatory B2B and B2C electronic invoicing standard in Italy, transmitted through the Sistema di Interscambio (SdI).

### Extracting E-Invoice Data:
When processing PDFs, always check for an attached XML payload (e.g. `factur-x.xml` or `zugferd-invoice.xml`). If present, this payload contains exact amounts, dates, and line items, bypassing the errors and hallucinations of OCR.

## Invoice Retention Periods

Invoice retention refers to the period during which business records must be kept for tax and commercial audits. It varies significantly by jurisdiction and document type.

- **Germany**: 10 years for invoices and commercial books (HGB & AO).
- **United Kingdom**: 6 years from the end of the last company financial year they relate to (HMRC).
- **France**: 10 years for accounting records (Code de commerce). Tax audits typically cover 3-6 years.
- **United States**: Generally 3-7 years for IRS purposes, depending on the tax situation.

*Always check the default `retention_years` configuration setting against local rules.* If in doubt, default to 10 years to satisfy strict European norms, especially if the invoice contains capital asset information where VAT adjustments can be reviewed for up to a decade.

## Value-Added Tax (VAT)

When extracting VAT information:
1. Identify the gross total, net total, and VAT amount.
2. Separate VAT by rate band if multiple rates apply (e.g. standard rate vs reduced rate).
3. Identify cross-border invoices, specifically noting Reverse Charge rules where VAT is accounted for by the buyer rather than charged by the seller.

## Sources

- Factur-X overview: https://en.wikipedia.org/wiki/Factur-X
- ZUGFeRD overview: https://en.wikipedia.org/wiki/ZUGFeRD
- Data retention overview (jurisdiction starting points): https://en.wikipedia.org/wiki/Data_retention
- Always prefer the jurisdiction statute or tax authority guidance named in `<state_root>/config.yaml` over encyclopedia summaries when they conflict.
