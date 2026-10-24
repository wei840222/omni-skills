# Official Sources & API References

This document records the official NCBI and National Library of Medicine (NLM) documentation for PubMed search syntax and E-utilities API interfaces.

## Official Documentation & Medical Subject Headings

- **PubMed User Guide**: [https://pubmed.ncbi.nlm.nih.gov/help/](https://pubmed.ncbi.nlm.nih.gov/help/)
  - Query construction, uppercase Boolean operators (`AND`, `OR`, `NOT`), field tags (`[Title]`, `[Author]`, `[MeSH Terms]`), and search filters.
- **MeSH (Medical Subject Headings) Database**: [https://www.ncbi.nlm.nih.gov/mesh/](https://www.ncbi.nlm.nih.gov/mesh/)
  - Controlled vocabulary thesaurus used for indexing, cataloging, and querying biomedical and health-related information.

## Programmatic Access (NCBI E-Utilities)

- **Entrez Programming Utilities (E-utilities) Guide**: [https://www.ncbi.nlm.nih.gov/books/NBK25501/](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
  - API tools: `ESearch` (retrieve PMIDs from query strings), `EFetch` (retrieve formatted records/abstracts), `ESummary` (document summaries).
  - Rate Limits: Default limit of 3 requests/second per IP address without an API key; up to 10 requests/second with a valid registered NCBI API key.
