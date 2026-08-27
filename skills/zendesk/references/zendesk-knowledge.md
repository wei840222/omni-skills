## Zendesk Domain Knowledge

Zendesk is a customer service and engagement platform. Its core offerings focus on providing software-as-a-service (SaaS) products for customer support, sales, and communication.

### Key Concepts

*   **Tickets**: The central entity in Zendesk Support. A ticket represents a customer's inquiry or issue.
*   **Users (Requesters and Agents)**: 
    *   **Requesters**: The end-users or customers who open tickets.
    *   **Agents**: The support staff who respond to and resolve tickets.
*   **Views**: Customizable groupings of tickets based on specific criteria (e.g., status, assignee, tags). They help agents organize and prioritize their workflow.
*   **Macros**: Predefined actions or responses that agents can apply to tickets with a single click, automating repetitive tasks.
*   **Triggers and Automations**: Business rules that automatically perform actions on tickets based on specific events or time-based conditions.
*   **Help Center (Guide)**: A self-service knowledge base where customers can find articles and FAQs to resolve issues without contacting support.

### API Foundations

The Zendesk REST API is extensive and allows for nearly all operations available in the web interface.

*   **Authentication**: Typically uses Basic Auth with an API token (`email@example.com/token:YOUR_API_TOKEN`) or OAuth tokens.
*   **Rate Limits**: APIs are rate-limited. Standard limits are often 200 or 700 requests per minute depending on the plan. Applications should implement backoff strategies (`Retry-After` headers).
*   **Pagination**: Most list endpoints are paginated, either using cursor-based pagination (recommended for large datasets) or offset pagination.
