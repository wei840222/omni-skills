# Core Rules

Use this reference whenever a mailbox request could alter state.

1. Discover server capabilities, mailbox names, and namespace behavior before using optional commands.
2. For a read request, preserve flags with read-only selection and non-mutating fetches.
3. For a mutation, list the exact UIDs and proposed operation, obtain explicit approval unless a matching standing policy exists, execute the smallest approved batch, then verify the resulting state.
4. Keep sync checkpoints per account and folder with `UIDVALIDITY`; a changed value starts a fresh scan.
5. Fetch headers and MIME metadata before bodies or attachments, then disclose only the requested minimum.
