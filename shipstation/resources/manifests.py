"""ShipStation manifests resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
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
            params["warehouse_id"] = serialize_param(warehouse_id)
        if ship_date_start is not None:
            params["ship_date_start"] = serialize_param(ship_date_start)
        if ship_date_end is not None:
            params["ship_date_end"] = serialize_param(ship_date_end)
        if created_at_start is not None:
            params["created_at_start"] = serialize_param(created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = serialize_param(created_at_end)
        if carrier_id is not None:
            params["carrier_id"] = serialize_param(carrier_id)
        if page is not None:
            params["page"] = serialize_param(page)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if label_ids is not None:
            params["label_ids"] = serialize_param(label_ids)
        response = self._api.request("GET", "/v2/manifests", params=params, json_body=None)
        return ListManifestsResponseBody.model_validate(response.json())

    def create(self, *, body: Union[CreateManifestByObjectRequestBody, CreateManifestLabelIdsRequestBody]) -> CreateManifestResponseBody:
        """Each ShipStation manifest is created for a specific warehouse, so you'll need to provide the warehouse_id rather than the ship_from address. You can create a warehouse for each location that you want """
        response = self._api.request("POST", "/v2/manifests", params=None, json_body=serialize_body(body))
        return CreateManifestResponseBody.model_validate(response.json())

    def get_by_id(self, manifest_id: str) -> GetManifestByIdResponseBody:
        """Get Manifest By Id"""
        response = self._api.request("GET", f"/v2/manifests/{manifest_id}", params=None, json_body=None)
        return GetManifestByIdResponseBody.model_validate(response.json())
