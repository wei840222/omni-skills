# Official Sources & Technical Specifications

This document records the official schema specifications and documentation for Postman collections and the Newman command-line test runner.

## Official Postman & Newman Documentation

- **Postman Collection v2.1.0 JSON Schema**: [https://schema.postman.com/json/collection/v2.1.0/collection.json](https://schema.postman.com/json/collection/v2.1.0/collection.json)
  - Formal JSON Schema definition for collection `info`, `item` request hierarchies, `event` prerequest/test scripts, `variable` definitions, and `auth` profiles.
- **Postman Documentation**: [https://learning.postman.com/docs/introduction/overview/](https://learning.postman.com/docs/introduction/overview/)
  - Core concepts, workspace organization, global/environment variables, response assertion scripting (`pm.test`, `pm.expect`), and API testing workflows.
- **Newman Command-Line Runner**: [https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
  - CLI execution parameters (`newman run <collection> -e <environment>`), reporter configurations (cli, json, junit, html), exit code handling for CI/CD pipelines, and iteration data injection.
