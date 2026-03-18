"""ShipStation carriers resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    GetCarrierByIdResponseBody,
    GetCarrierOptionsResponseBody,
    ListCarrierPackageTypesResponseBody,
    ListCarrierServicesResponseBody,
    ListCarriersResponseBody,
)


class CarriersResource:
    """Carriers API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self) -> ListCarriersResponseBody:
        """List all carriers that have been added to this account."""
        response = self._api.request("GET", "/v2/carriers", params=None, json_body=None)
        return ListCarriersResponseBody.model_validate(response.json())

    def get_by_id(self, carrier_id: str) -> GetCarrierByIdResponseBody:
        """Retrive details about a specific carrier by its carrier id."""
        response = self._api.request("GET", f"/v2/carriers/{carrier_id}", params=None, json_body=None)
        return GetCarrierByIdResponseBody.model_validate(response.json())

    def get_options(self, carrier_id: str) -> GetCarrierOptionsResponseBody:
        """Get a list of the options available for a specific carriers."""
        response = self._api.request("GET", f"/v2/carriers/{carrier_id}/options", params=None, json_body=None)
        return GetCarrierOptionsResponseBody.model_validate(response.json())

    def list_package_types(self, carrier_id: str) -> ListCarrierPackageTypesResponseBody:
        """List the package types associated with a specific carrier."""
        response = self._api.request("GET", f"/v2/carriers/{carrier_id}/packages", params=None, json_body=None)
        return ListCarrierPackageTypesResponseBody.model_validate(response.json())

    def list_services(self, carrier_id: str) -> ListCarrierServicesResponseBody:
        """List the services associated with a specific carrier id."""
        response = self._api.request("GET", f"/v2/carriers/{carrier_id}/services", params=None, json_body=None)
        return ListCarrierServicesResponseBody.model_validate(response.json())
