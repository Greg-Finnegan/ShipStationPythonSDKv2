"""ShipStation fulfillments resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


class FulfillmentsResource:
    """Fulfillments API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        ship_to_name: Optional[str] = None,
        ship_to_country_code: Optional[str] = None,
        shipment_number: Optional[str] = None,
        shipment_id: Optional[str] = None,
        fulfillment_id: Optional[str] = None,
        batch_id: Optional[str] = None,
        order_source_id: Optional[str] = None,
        fulfillment_provider_code: Optional[str] = None,
        tracking_number: Optional[str] = None,
        ship_date_start: Optional[datetime] = None,
        ship_date_end: Optional[datetime] = None,
        create_date_start: Optional[datetime] = None,
        create_date_end: Optional[datetime] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
        sort_dir: Optional[str] = 'asc',
        sort_by: Optional[str] = 'created_at',
    ) -> Any:
        """Retrieve a list of fulfillments based on various filter criteria. You can filter by shipment details, tracking information, dates, and more to find the specific fulfillments you need."""
        params: dict[str, Any] = {}
        if ship_to_name is not None:
            params["ship_to_name"] = serialize_param(ship_to_name)
        if ship_to_country_code is not None:
            params["ship_to_country_code"] = serialize_param(ship_to_country_code)
        if shipment_number is not None:
            params["shipment_number"] = serialize_param(shipment_number)
        if shipment_id is not None:
            params["shipment_id"] = serialize_param(shipment_id)
        if fulfillment_id is not None:
            params["fulfillment_id"] = serialize_param(fulfillment_id)
        if batch_id is not None:
            params["batch_id"] = serialize_param(batch_id)
        if order_source_id is not None:
            params["order_source_id"] = serialize_param(order_source_id)
        if fulfillment_provider_code is not None:
            params["fulfillment_provider_code"] = serialize_param(fulfillment_provider_code)
        if tracking_number is not None:
            params["tracking_number"] = serialize_param(tracking_number)
        if ship_date_start is not None:
            params["ship_date_start"] = serialize_param(ship_date_start)
        if ship_date_end is not None:
            params["ship_date_end"] = serialize_param(ship_date_end)
        if create_date_start is not None:
            params["create_date_start"] = serialize_param(create_date_start)
        if create_date_end is not None:
            params["create_date_end"] = serialize_param(create_date_end)
        if page is not None:
            params["page"] = serialize_param(page)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if sort_dir is not None:
            params["sort_dir"] = serialize_param(sort_dir)
        if sort_by is not None:
            params["sort_by"] = serialize_param(sort_by)
        response = self._api.request("GET", "/v2/fulfillments", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def create(self) -> Any:
        """Create one or more fulfillments by marking shipments as shipped with tracking information. This will notify customers and marketplaces according to your configuration."""
        response = self._api.request("POST", "/v2/fulfillments", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]
