# Dashboard Provisioning

- JSON export includes data source UID — will fail if different on import
- Use data source variables — `${DS_PROMETHEUS}` substituted at runtime
- Provisioned dashboards read-only by default — `allowEditing: true` in provisioning
- Configure the target folder before dashboard provisioning so the imported dashboard has a visible destination.

## Provisioning Checks

Provision dashboard files through the filesystem provider and ensure the configured folder exists or is created by the provider configuration. Before promoting exported JSON, replace environment-specific data source UIDs with provisioned data source references or variables, then verify the dashboard loads in the target environment.

Source: [Grafana dashboard provisioning documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#dashboards).
