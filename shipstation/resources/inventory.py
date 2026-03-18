"""ShipStation inventory resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


class InventoryResource:
    """Inventory API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def get_levels(
        self,
        *,
        sku: Optional[str] = None,
        inventory_warehouse_id: Optional[str] = None,
        inventory_location_id: Optional[str] = None,
        group_by: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> Any:
        params: dict[str, Any] = {}
        if sku is not None:
            params["sku"] = serialize_param(sku)
        if inventory_warehouse_id is not None:
            params["inventory_warehouse_id"] = serialize_param(inventory_warehouse_id)
        if inventory_location_id is not None:
            params["inventory_location_id"] = serialize_param(inventory_location_id)
        if group_by is not None:
            params["group_by"] = serialize_param(group_by)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        response = self._api.request("GET", "/v2/inventory", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def update_sku_stock_levels(self) -> None:
        response = self._api.request("POST", "/v2/inventory", params=None, json_body=None)
        return None

    def get_warehouses(self, *, page_size: Optional[int] = None) -> Any:
        params: dict[str, Any] = {}
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        response = self._api.request("GET", "/v2/inventory_warehouses", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def add_new_warehouse(self) -> Any:
        response = self._api.request("POST", "/v2/inventory_warehouses", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def get_warehouse_by_id(self, inventory_warehouse_id: str) -> Any:
        response = self._api.request("GET", f"/v2/inventory_warehouses/{inventory_warehouse_id}", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def update_warehouse(self, inventory_warehouse_id: str) -> None:
        response = self._api.request("PUT", f"/v2/inventory_warehouses/{inventory_warehouse_id}", params=None, json_body=None)
        return None

    def delete_warehouse(
        self,
        inventory_warehouse_id: str,
        *,
        remove_inventory: Optional[str] = None,
    ) -> None:
        params: dict[str, Any] = {}
        if remove_inventory is not None:
            params["remove_inventory"] = serialize_param(remove_inventory)
        response = self._api.request("DELETE", f"/v2/inventory_warehouses/{inventory_warehouse_id}", params=params, json_body=None)
        return None

    def list_locations(self, *, page_size: Optional[int] = None) -> Any:
        params: dict[str, Any] = {}
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        response = self._api.request("GET", "/v2/inventory_locations", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def create_location(self) -> Any:
        response = self._api.request("POST", "/v2/inventory_locations", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def get_location_by_id(self, inventory_location_id: str) -> Any:
        response = self._api.request("GET", f"/v2/inventory_locations/{inventory_location_id}", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def update_location(self, inventory_location_id: str) -> None:
        response = self._api.request("PUT", f"/v2/inventory_locations/{inventory_location_id}", params=None, json_body=None)
        return None

    def delete_location_by_id(
        self,
        inventory_location_id: str,
        *,
        remove_inventory: Optional[str] = None,
    ) -> None:
        params: dict[str, Any] = {}
        if remove_inventory is not None:
            params["remove_inventory"] = serialize_param(remove_inventory)
        response = self._api.request("DELETE", f"/v2/inventory_locations/{inventory_location_id}", params=params, json_body=None)
        return None
