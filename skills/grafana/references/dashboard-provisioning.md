# Dashboard Provisioning

- JSON export includes data source UID — will fail if different on import
- Use data source variables — `${DS_PROMETHEUS}` substituted at runtime
- Provisioned dashboards read-only by default — `allowEditing: true` in provisioning
- Folder must exist before dashboard provisioning — or import fails silently
