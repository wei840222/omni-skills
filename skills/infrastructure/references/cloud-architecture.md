# Cloud Architecture Principles

## Design for Failure
- **Assume everything will fail**: Hardware, network, and software components will eventually fail.
- **Redundancy**: Deploy across multiple availability zones or regions.
- **Stateless components**: Where possible, make application servers stateless so they can be easily replaced.

## Scalability
- **Horizontal vs Vertical**: Prefer horizontal scaling (more instances) over vertical scaling (larger instances) for high availability.
- **Auto-scaling**: Use metrics (CPU, memory, custom application metrics) to automatically adjust capacity.

## Security
- **Defense in depth**: Apply security controls at all layers (network, application, data).
- **Least privilege**: Grant only necessary permissions to users, services, and components.
- **Encryption**: Encrypt data at rest and in transit.

## Operations
- **Infrastructure as Code (IaC)**: Automate provisioning and management of infrastructure.
- **Monitoring and Logging**: Implement comprehensive observability for quick issue detection and resolution.

*Sources:*
- AWS Well-Architected Framework (https://aws.amazon.com/architecture/well-architected/)
- Google Cloud Architecture Framework (https://cloud.google.com/architecture/framework)
