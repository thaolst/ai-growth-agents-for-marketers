# Growth Metrics Context

> Optional. If connected, provides real-time data to all skills via growth-mcp.
> Leave empty to use expert defaults.

## Growth MCP Connection

If you have growth-mcp running, skills will connect automatically to pull live data.

```bash
# Install growth-mcp
git clone https://github.com/thaolst/growth-mcp.git
cd growth-mcp && pip install -e .
```

## Manual Metric Overrides

Fill these if growth-mcp is not connected:

- **Current retention rate (D1 / D7 / D30):**  /  /
- **Current churn rate (monthly):**
- **Average campaign redemption rate:**
- **Average voucher cost per redemption:**
- **Push notification CTR:**
- **SMS/email conversion rate:**
- **Typical campaign ROI:**
