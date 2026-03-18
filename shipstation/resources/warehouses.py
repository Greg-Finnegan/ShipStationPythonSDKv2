"""ShipStation warehouses resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    GetWarehouseByIdResponseBody,
    ListWarehousesResponseBody,
)


class WarehousesResource:
    """Warehouses API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self) -> ListWarehousesResponseBody:
        """Retrieve a list of warehouses associated with this account."""
        response = self._api.request("GET", "/v2/warehouses", params=None, json_body=None)
        return ListWarehousesResponseBody.model_validate(response.json())

    def get_by_id(self, warehouse_id: str) -> GetWarehouseByIdResponseBody:
        """Retrieve warehouse data based on the warehouse ID"""
        response = self._api.request("GET", f"/v2/warehouses/{warehouse_id}", params=None, json_body=None)
        return GetWarehouseByIdResponseBody.model_validate(response.json())
