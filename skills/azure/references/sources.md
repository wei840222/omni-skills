# Azure sources

Checked 2026-10-08. Re-open the live page before restating limits, prices, or API behavior.

## Agent Skills / validator

- **Agent Skills specification** — frontmatter and package shape.
  - https://agentskills.io/specification
- **skills-ref** — reference validator used by this repo.
  - https://github.com/agentskills/agentskills/tree/main/skills-ref

## Identity, RBAC, managed identity

- **Azure RBAC overview**
  - https://learn.microsoft.com/en-us/azure/role-based-access-control/overview
- **RBAC troubleshooting**
  - https://learn.microsoft.com/en-us/azure/role-based-access-control/troubleshooting
- **Managed identities overview (Entra)**
  - https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview
- **Privileged Identity Management**
  - https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure
- **Azure CLI authentication**
  - https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli

## Networking and Private Link

- **Private endpoint overview**
  - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
- **Private endpoint DNS**
  - https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
- **Outbound connections from Azure Load Balancer (SNAT)**
  - https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-outbound-connections
- **Virtual network peering**
  - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview
- **AKS CNI networking concepts**
  - https://learn.microsoft.com/en-us/azure/aks/concepts-network-cni-overview

## App platform, Functions, VMs

- **App Service availability/performance FAQ (includes ~230s front-end behavior)**
  - https://learn.microsoft.com/en-us/azure/app-service/faq-availability-performance-application-issues
- **App Service hosting plans**
  - https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans
- **Azure Functions scale and hosting**
  - https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale
- **VM allocation failure troubleshooting**
  - https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/windows/allocation-failure
- **VM sizes overview**
  - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview

## Data and storage

- **Cosmos DB service limits**
  - https://learn.microsoft.com/en-us/azure/cosmos-db/concepts-limits
- **Cosmos DB partitioning**
  - https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview
- **Cosmos DB autoscale FAQ**
  - https://learn.microsoft.com/en-us/azure/cosmos-db/autoscale-faq
- **Storage account overview**
  - https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview

## Cost, governance, Key Vault, Monitor, IaC

- **Cost Analysis common uses**
  - https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-analysis-common-uses
- **Create budgets in Cost Management**
  - https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- **Azure Policy overview**
  - https://learn.microsoft.com/en-us/azure/governance/policy/overview
- **Resource providers and types**
  - https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types
- **ARM deployment modes**
  - https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-modes
- **Key Vault soft-delete**
  - https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview
- **Key Vault RBAC guide**
  - https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide
- **Diagnostic settings**
  - https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings

## What this skill does not treat as a live measurement

Stage monthly cost tables are **order-of-magnitude planning anchors**, not quotes. SNAT port budgets, RU pricing multipliers, and regional capacity change; confirm on the live Learn / pricing / quotas blades for the target subscription and region before acting on money or capacity.
