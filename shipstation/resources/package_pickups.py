"""ShipStation package_pickups resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    DeleteScheduledPickupResponseBody,
    ListPickupResponseBody,
    PickupResponseBody,
    SchedulePickupRequestBody,
    SchedulePickupResponseBody,
)


class PackagePickupsResource:
    """PackagePickups API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list_scheduled(
        self,
        *,
        carrier_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
        created_at_start: Optional[datetime] = None,
        created_at_end: Optional[datetime] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
    ) -> ListPickupResponseBody:
        """List all pickups that have been scheduled for this carrier"""
        params: dict[str, Any] = {}
        if carrier_id is not None:
            params["carrier_id"] = serialize_param(carrier_id)
        if warehouse_id is not None:
            params["warehouse_id"] = serialize_param(warehouse_id)
        if created_at_start is not None:
            params["created_at_start"] = serialize_param(created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = serialize_param(created_at_end)
        if page is not None:
            params["page"] = serialize_param(page)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        response = self._api.request("GET", "/v2/pickups", params=params, json_body=None)
        return ListPickupResponseBody.model_validate(response.json())

    def schedule(self, *, body: SchedulePickupRequestBody) -> SchedulePickupResponseBody:
        """Schedule a package pickup with a carrier"""
        response = self._api.request("POST", "/v2/pickups", params=None, json_body=serialize_body(body))
        return SchedulePickupResponseBody.model_validate(response.json())

    def get_by_id(self, pickup_id: str) -> PickupResponseBody:
        """Get Pickup By ID"""
        response = self._api.request("GET", f"/v2/pickups/{pickup_id}", params=None, json_body=None)
        return PickupResponseBody.model_validate(response.json())

    def delete_scheduled(self, pickup_id: str) -> DeleteScheduledPickupResponseBody:
        """Delete a previously-scheduled pickup by ID"""
        response = self._api.request("DELETE", f"/v2/pickups/{pickup_id}", params=None, json_body=None)
        return DeleteScheduledPickupResponseBody.model_validate(response.json())
