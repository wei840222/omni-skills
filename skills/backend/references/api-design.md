## API Design

- Versioning strategy from day one—path (/v1/) or header
- Pagination for list endpoints—cursor or offset; include total count
- Consistent response format—same envelope everywhere
- Meaningful status codes—201 for create, 204 for delete, 404 for not found
