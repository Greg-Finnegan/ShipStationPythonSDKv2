"""ShipStation fulfillments resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient


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
            params["ship_to_name"] = ship_to_name.value if hasattr(ship_to_name, 'value') else (ship_to_name.isoformat() if hasattr(ship_to_name, 'isoformat') else ship_to_name)
        if ship_to_country_code is not None:
            params["ship_to_country_code"] = ship_to_country_code.value if hasattr(ship_to_country_code, 'value') else (ship_to_country_code.isoformat() if hasattr(ship_to_country_code, 'isoformat') else ship_to_country_code)
        if shipment_number is not None:
            params["shipment_number"] = shipment_number.value if hasattr(shipment_number, 'value') else (shipment_number.isoformat() if hasattr(shipment_number, 'isoformat') else shipment_number)
        if shipment_id is not None:
            params["shipment_id"] = shipment_id.value if hasattr(shipment_id, 'value') else (shipment_id.isoformat() if hasattr(shipment_id, 'isoformat') else shipment_id)
        if fulfillment_id is not None:
            params["fulfillment_id"] = fulfillment_id.value if hasattr(fulfillment_id, 'value') else (fulfillment_id.isoformat() if hasattr(fulfillment_id, 'isoformat') else fulfillment_id)
        if batch_id is not None:
            params["batch_id"] = batch_id.value if hasattr(batch_id, 'value') else (batch_id.isoformat() if hasattr(batch_id, 'isoformat') else batch_id)
        if order_source_id is not None:
            params["order_source_id"] = order_source_id.value if hasattr(order_source_id, 'value') else (order_source_id.isoformat() if hasattr(order_source_id, 'isoformat') else order_source_id)
        if fulfillment_provider_code is not None:
            params["fulfillment_provider_code"] = fulfillment_provider_code.value if hasattr(fulfillment_provider_code, 'value') else (fulfillment_provider_code.isoformat() if hasattr(fulfillment_provider_code, 'isoformat') else fulfillment_provider_code)
        if tracking_number is not None:
            params["tracking_number"] = tracking_number.value if hasattr(tracking_number, 'value') else (tracking_number.isoformat() if hasattr(tracking_number, 'isoformat') else tracking_number)
        if ship_date_start is not None:
            params["ship_date_start"] = ship_date_start.value if hasattr(ship_date_start, 'value') else (ship_date_start.isoformat() if hasattr(ship_date_start, 'isoformat') else ship_date_start)
        if ship_date_end is not None:
            params["ship_date_end"] = ship_date_end.value if hasattr(ship_date_end, 'value') else (ship_date_end.isoformat() if hasattr(ship_date_end, 'isoformat') else ship_date_end)
        if create_date_start is not None:
            params["create_date_start"] = create_date_start.value if hasattr(create_date_start, 'value') else (create_date_start.isoformat() if hasattr(create_date_start, 'isoformat') else create_date_start)
        if create_date_end is not None:
            params["create_date_end"] = create_date_end.value if hasattr(create_date_end, 'value') else (create_date_end.isoformat() if hasattr(create_date_end, 'isoformat') else create_date_end)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if sort_dir is not None:
            params["sort_dir"] = sort_dir.value if hasattr(sort_dir, 'value') else (sort_dir.isoformat() if hasattr(sort_dir, 'isoformat') else sort_dir)
        if sort_by is not None:
            params["sort_by"] = sort_by.value if hasattr(sort_by, 'value') else (sort_by.isoformat() if hasattr(sort_by, 'isoformat') else sort_by)
        response = self._api.request("GET", "/v2/fulfillments", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def create(self) -> Any:
        """Create one or more fulfillments by marking shipments as shipped with tracking information. This will notify customers and marketplaces according to your configuration."""
        response = self._api.request("POST", "/v2/fulfillments", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]
