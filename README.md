# ShipStation Python SDK

A fully-typed Python SDK for the [ShipStation API V2](https://docs.shipstation.com/getting-started#/openapi), auto-generated from the official OpenAPI spec.

> **Disclaimer:** This is **not** an official ShipStation product. ShipStation does not currently provide a Python SDK for the V2 API.
> This project is community-built and maintained independently. If you work at ShipStation and would like to
> adopt, feel free to reach out!

## What is this?

- Python wrapper for **ShipStation API V2** (not V1)
- **134 Pydantic v2 models** with full type annotations
- **42 enums** mapped from the OpenAPI spec
- **80+ typed methods** across 18 resource groups
- Full IDE support — autocompletion, hover docs, type checking
- `py.typed` PEP 561 marker included

## Getting an API Key

ShipStation API V2 uses API keys from ShipEngine:

1. Create a free sandbox account at [shipengine.com/signup](https://www.shipengine.com/signup)
2. Generate an API key from the dashboard
3. Use that key with this SDK — it hits `https://api.shipstation.com` by default (/v2 built into sdk)

## Installation

```bash
pip install -e .
```

Or install the dependencies directly:

```bash
pip install pydantic>=2.0 requests>=2.28
```

## Quick Start

Set your API key as an environment variable:

```bash
export SHIPSTATION_API_KEY="your-api-key-here"
```

### List Shipments

```python
import os
from shipstation import ShipStation

client = ShipStation(api_key=os.environ["SHIPSTATION_API_KEY"])

# List shipments for a given pickup
response = client.shipments.list(pickup_id="se-123456")

for shipment in response.shipments:
    print(f"  {shipment.shipment_id} — status: {shipment.shipment_status}")

# List all carriers on your account
carriers = client.carriers.list()
print(carriers)
```

## Available Resources

| Resource | Access | Examples |
|---|---|---|
| Batches | `client.batches` | `.list()`, `.create()`, `.process()` |
| Carriers | `client.carriers` | `.list()`, `.get_by_id()`, `.list_services()` |
| Downloads | `client.downloads` | `.download()` |
| Fulfillments | `client.fulfillments` | `.list()` |
| Inventory | `client.inventory` | `.get_levels()` |
| Labels | `client.labels` | `.list()`, `.create()`, `.void()` |
| Manifests | `client.manifests` | `.list()`, `.create()` |
| Package Pickups | `client.package_pickups` | `.list_scheduled()`, `.schedule()` |
| Package Types | `client.package_types` | `.list()`, `.create()` |
| Products | `client.products` | product operations |
| Rates | `client.rates` | `.calculate()`, `.estimate()` |
| Shipments | `client.shipments` | `.list()`, `.create()`, `.cancel()` |
| Tags | `client.tags` | `.list()` |
| Totes | `client.totes` | tote operations |
| Tracking | `client.tracking` | tracking operations |
| Users | `client.users` | user operations |
| Warehouses | `client.warehouses` | `.list()`, `.get_by_id()` |
| Webhooks | `client.webhooks` | `.list()`, `.create()`, `.delete()` |

## Requirements

- Python >= 3.11
- pydantic >= 2.0
- requests >= 2.28

## Contributing

If you'd like to see improvements, [create an issue](../../issues) on this repo. Pull requests are welcome.

---

*Last updated: 2026-03-18*
