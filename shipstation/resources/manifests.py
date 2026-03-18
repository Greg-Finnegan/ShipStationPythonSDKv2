"""ShipStation manifests resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    CreateManifestByObjectRequestBody,
    CreateManifestLabelIdsRequestBody,
    CreateManifestResponseBody,
    GetManifestByIdResponseBody,
    ListManifestsResponseBody,
)


class ManifestsResource:
    """Manifests API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        warehouse_id: Optional[str] = None,
        ship_date_start: Optional[datetime] = None,
        ship_date_end: Optional[datetime] = None,
        created_at_start: Optional[datetime] = None,
        created_at_end: Optional[datetime] = None,
        carrier_id: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
        label_ids: Optional[list[str]] = None,
    ) -> ListManifestsResponseBody:
        """Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time."""
        params: dict[str, Any] = {}
        if warehouse_id is not None:
            params["warehouse_id"] = warehouse_id.value if hasattr(warehouse_id, 'value') else (warehouse_id.isoformat() if hasattr(warehouse_id, 'isoformat') else warehouse_id)
        if ship_date_start is not None:
            params["ship_date_start"] = ship_date_start.value if hasattr(ship_date_start, 'value') else (ship_date_start.isoformat() if hasattr(ship_date_start, 'isoformat') else ship_date_start)
        if ship_date_end is not None:
            params["ship_date_end"] = ship_date_end.value if hasattr(ship_date_end, 'value') else (ship_date_end.isoformat() if hasattr(ship_date_end, 'isoformat') else ship_date_end)
        if created_at_start is not None:
            params["created_at_start"] = created_at_start.value if hasattr(created_at_start, 'value') else (created_at_start.isoformat() if hasattr(created_at_start, 'isoformat') else created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = created_at_end.value if hasattr(created_at_end, 'value') else (created_at_end.isoformat() if hasattr(created_at_end, 'isoformat') else created_at_end)
        if carrier_id is not None:
            params["carrier_id"] = carrier_id.value if hasattr(carrier_id, 'value') else (carrier_id.isoformat() if hasattr(carrier_id, 'isoformat') else carrier_id)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if label_ids is not None:
            params["label_ids"] = label_ids.value if hasattr(label_ids, 'value') else (label_ids.isoformat() if hasattr(label_ids, 'isoformat') else label_ids)
        response = self._api.request("GET", "/v2/manifests", params=params, json_body=None)
        return ListManifestsResponseBody.model_validate(response.json())

    def create(self, *, body: Union[CreateManifestByObjectRequestBody, CreateManifestLabelIdsRequestBody]) -> CreateManifestResponseBody:
        """Each ShipStation manifest is created for a specific warehouse, so you'll need to provide the warehouse_id rather than the ship_from address. You can create a warehouse for each location that you want """
        response = self._api.request("POST", "/v2/manifests", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateManifestResponseBody.model_validate(response.json())

    def get_by_id(self, manifest_id: str) -> GetManifestByIdResponseBody:
        """Get Manifest By Id"""
        response = self._api.request("GET", f"/v2/manifests/{manifest_id}", params=None, json_body=None)
        return GetManifestByIdResponseBody.model_validate(response.json())
