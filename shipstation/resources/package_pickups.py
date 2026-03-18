"""ShipStation package_pickups resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    SchedulePickupRequestBody,
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
    ) -> Any:
        """List all pickups that have been scheduled for this carrier"""
        params: dict[str, Any] = {}
        if carrier_id is not None:
            params["carrier_id"] = carrier_id.value if hasattr(carrier_id, 'value') else (carrier_id.isoformat() if hasattr(carrier_id, 'isoformat') else carrier_id)
        if warehouse_id is not None:
            params["warehouse_id"] = warehouse_id.value if hasattr(warehouse_id, 'value') else (warehouse_id.isoformat() if hasattr(warehouse_id, 'isoformat') else warehouse_id)
        if created_at_start is not None:
            params["created_at_start"] = created_at_start.value if hasattr(created_at_start, 'value') else (created_at_start.isoformat() if hasattr(created_at_start, 'isoformat') else created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = created_at_end.value if hasattr(created_at_end, 'value') else (created_at_end.isoformat() if hasattr(created_at_end, 'isoformat') else created_at_end)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        response = self._api.request("GET", "/v2/pickups", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def schedule(self, *, body: SchedulePickupRequestBody) -> Any:
        """Schedule a package pickup with a carrier"""
        response = self._api.request("POST", "/v2/pickups", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return response.json()  # type: ignore[return-value]

    def get_by_id(self, pickup_id: str) -> Any:
        """Get Pickup By ID"""
        response = self._api.request("GET", f"/v2/pickups/{pickup_id}", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def delete_scheduled(self, pickup_id: str) -> Any:
        """Delete a previously-scheduled pickup by ID"""
        response = self._api.request("DELETE", f"/v2/pickups/{pickup_id}", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]
