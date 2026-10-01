# Data Quality

- Validate data before analyzing — garbage in, garbage out.
- Check row counts, date ranges, and null rates first.
- Duplicates hide in joins — always verify uniqueness and grain after each join.
- Source definitions matter — "revenue" and "active user" often mean different things to different teams.
- Document assumptions — incomplete trailing days, backfills, and timezone shifts change totals.
- Spot-check extreme values and unexpected categorical levels before storytelling.
