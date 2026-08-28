# Ecommerce Knowledge & Sources

## Common Metrics & Economics
- **Contribution Margin (CM)**: Revenue minus variable costs (COGS, payment fees, outbound shipping, channel commissions). Indicates actual profitability per order.
- **Customer Acquisition Cost (CAC)**: The cost to acquire a new customer. Must be lower than CM per customer.
- **Conversion Rate**: Percentage of visitors who place an order. Typical ranges vary by industry but usually lie between 1.5% and 3% for DTC.
- **Average Order Value (AOV)**: Essential for determining free shipping thresholds and discount limits.

## Payment & Fraud
- Idempotency is crucial for payment webhooks to avoid double charges. Providers may deliver events out of order or multiple times.
- **Chargebacks**: Result from fraud or disputes. Usually entail a fee and a loss of the product. Dispute windows are strict and set by payment processors and networks.

## Sales Tax & VAT
- **US Economic Nexus**: A seller is required to collect sales tax in a state if they exceed a certain threshold (often $100k or 200 transactions).
- **EU Distance Sales & OSS**: The threshold is €10,000 for cross-border B2C sales; after this, businesses must register for the One Stop Shop (OSS) or in individual countries.

## Useful Sources
- **E-commerce Concepts (Wikipedia)**: `https://en.wikipedia.org/wiki/E-commerce`
- **PCI Compliance**: Important for businesses handling credit card details.
