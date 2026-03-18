"""ShipStation shipments resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    CreateShipmentsRequestBody,
    CreateShipmentsResponseBody,
    GetShipmentByExternalIdResponseBody,
    GetShipmentByIdResponseBody,
    ListShipmentRatesResponseBody,
    ListShipmentsResponseBody,
    TagShipmentResponseBody,
)
from ..enums import (
    ShipmentStatus,
    ShipmentsSortBy,
    SortDir,
)


class ShipmentsResource:
    """Shipments API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        shipment_status: Optional[ShipmentStatus] = None,
        batch_id: Optional[str] = None,
        pickup_id: Optional[str] = None,
        created_at_start: Optional[datetime] = None,
        created_at_end: Optional[datetime] = None,
        modified_at_start: Optional[datetime] = None,
        modified_at_end: Optional[datetime] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
        sales_order_id: Optional[str] = None,
        sort_dir: Optional[SortDir] = 'desc',
        shipment_number: Optional[str] = None,
        ship_to_name: Optional[str] = None,
        item_keyword: Optional[str] = None,
        payment_date_start: Optional[datetime] = None,
        payment_date_end: Optional[datetime] = None,
        store_id: Optional[str] = None,
        external_shipment_id: Optional[str] = None,
        sort_by: Optional[ShipmentsSortBy] = None,
    ) -> ListShipmentsResponseBody:
        """Get list of Shipments"""
        params: dict[str, Any] = {}
        if shipment_status is not None:
            params["shipment_status"] = serialize_param(shipment_status)
        if batch_id is not None:
            params["batch_id"] = serialize_param(batch_id)
        if pickup_id is not None:
            params["pickup_id"] = serialize_param(pickup_id)
        if created_at_start is not None:
            params["created_at_start"] = serialize_param(created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = serialize_param(created_at_end)
        if modified_at_start is not None:
            params["modified_at_start"] = serialize_param(modified_at_start)
        if modified_at_end is not None:
            params["modified_at_end"] = serialize_param(modified_at_end)
        if page is not None:
            params["page"] = serialize_param(page)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if sales_order_id is not None:
            params["sales_order_id"] = serialize_param(sales_order_id)
        if sort_dir is not None:
            params["sort_dir"] = serialize_param(sort_dir)
        if shipment_number is not None:
            params["shipment_number"] = serialize_param(shipment_number)
        if ship_to_name is not None:
            params["ship_to_name"] = serialize_param(ship_to_name)
        if item_keyword is not None:
            params["item_keyword"] = serialize_param(item_keyword)
        if payment_date_start is not None:
            params["payment_date_start"] = serialize_param(payment_date_start)
        if payment_date_end is not None:
            params["payment_date_end"] = serialize_param(payment_date_end)
        if store_id is not None:
            params["store_id"] = serialize_param(store_id)
        if external_shipment_id is not None:
            params["external_shipment_id"] = serialize_param(external_shipment_id)
        if sort_by is not None:
            params["sort_by"] = serialize_param(sort_by)
        response = self._api.request("GET", "/v2/shipments", params=params, json_body=None)
        return ListShipmentsResponseBody.model_validate(response.json())

    def create(self, *, body: CreateShipmentsRequestBody) -> CreateShipmentsResponseBody:
        """Create one or more shipments"""
        response = self._api.request("POST", "/v2/shipments", params=None, json_body=serialize_body(body))
        return CreateShipmentsResponseBody.model_validate(response.json())

    def get_by_external_id(self, external_shipment_id: str) -> GetShipmentByExternalIdResponseBody:
        """Query Shipments created using your own custom ID convention using this endpoint"""
        response = self._api.request("GET", f"/v2/shipments/external_shipment_id/{external_shipment_id}", params=None, json_body=None)
        return GetShipmentByExternalIdResponseBody.model_validate(response.json())

    def get_by_id(self, shipment_id: str) -> GetShipmentByIdResponseBody:
        """Get an individual shipment based on its ID"""
        response = self._api.request("GET", f"/v2/shipments/{shipment_id}", params=None, json_body=None)
        return GetShipmentByIdResponseBody.model_validate(response.json())

    def cancel(self, shipment_id: str) -> None:
        """Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first An example use case would be if a batch label crea"""
        response = self._api.request("PUT", f"/v2/shipments/{shipment_id}/cancel", params=None, json_body=None)
        return None

    def list_rates(
        self,
        shipment_id: str,
        *,
        created_at_start: Optional[datetime] = None,
    ) -> ListShipmentRatesResponseBody:
        """Get Rates for the shipment information associated with the shipment ID"""
        params: dict[str, Any] = {}
        if created_at_start is not None:
            params["created_at_start"] = serialize_param(created_at_start)
        response = self._api.request("GET", f"/v2/shipments/{shipment_id}/rates", params=params, json_body=None)
        return ListShipmentRatesResponseBody.model_validate(response.json())

    def tag(self, shipment_id: str, tag_name: str) -> TagShipmentResponseBody:
        """Add a tag to the shipment object"""
        response = self._api.request("POST", f"/v2/shipments/{shipment_id}/tags/{tag_name}", params=None, json_body=None)
        return TagShipmentResponseBody.model_validate(response.json())

    def untag(self, shipment_id: str, tag_name: str) -> None:
        """Remove an existing tag from the Shipment object"""
        response = self._api.request("DELETE", f"/v2/shipments/{shipment_id}/tags/{tag_name}", params=None, json_body=None)
        return None
