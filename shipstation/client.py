"""ShipStation API client — auto-generated, do not edit."""

from __future__ import annotations

from ._api import ApiClient
from .resources.batches import BatchesResource
from .resources.carriers import CarriersResource
from .resources.downloads import DownloadsResource
from .resources.fulfillments import FulfillmentsResource
from .resources.inventory import InventoryResource
from .resources.labels import LabelsResource
from .resources.manifests import ManifestsResource
from .resources.package_pickups import PackagePickupsResource
from .resources.package_types import PackageTypesResource
from .resources.products import ProductsResource
from .resources.rates import RatesResource
from .resources.shipments import ShipmentsResource
from .resources.tags import TagsResource
from .resources.totes import TotesResource
from .resources.tracking import TrackingResource
from .resources.users import UsersResource
from .resources.warehouses import WarehousesResource
from .resources.webhooks import WebhooksResource


class ShipStation:
    """ShipStation API v2 client with fully typed methods."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.shipstation.com",
    ) -> None:
        self._api = ApiClient(api_key=api_key, base_url=base_url)
        self.batches = BatchesResource(self._api)
        self.carriers = CarriersResource(self._api)
        self.downloads = DownloadsResource(self._api)
        self.fulfillments = FulfillmentsResource(self._api)
        self.inventory = InventoryResource(self._api)
        self.labels = LabelsResource(self._api)
        self.manifests = ManifestsResource(self._api)
        self.package_pickups = PackagePickupsResource(self._api)
        self.package_types = PackageTypesResource(self._api)
        self.products = ProductsResource(self._api)
        self.rates = RatesResource(self._api)
        self.shipments = ShipmentsResource(self._api)
        self.tags = TagsResource(self._api)
        self.totes = TotesResource(self._api)
        self.tracking = TrackingResource(self._api)
        self.users = UsersResource(self._api)
        self.warehouses = WarehousesResource(self._api)
        self.webhooks = WebhooksResource(self._api)
