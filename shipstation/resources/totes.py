"""ShipStation totes resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    BulkCreateToteResponse,
    Tote,
    ToteCreateBatchRequest,
    ToteUpdateRequest,
)


class TotesResource:
    """Totes API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self, *, inventory_warehouse_id: Optional[str] = None) -> Any:
        """Get all totes for the seller, optionally filtered by warehouse."""
        params: dict[str, Any] = {}
        if inventory_warehouse_id is not None:
            params["inventory_warehouse_id"] = serialize_param(inventory_warehouse_id)
        response = self._api.request("GET", "/v2/totes", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]

    def create_batch(self, *, body: ToteCreateBatchRequest) -> BulkCreateToteResponse:
        """Create multiple totes at once. Returns both successfully created totes and any failures."""
        response = self._api.request("POST", "/v2/totes", params=None, json_body=serialize_body(body))
        return BulkCreateToteResponse.model_validate(response.json())

    def get_quantities(self) -> Any:
        """Get the number of totes in each warehouse."""
        response = self._api.request("GET", "/v2/totes/quantities", params=None, json_body=None)
        return response.json()  # type: ignore[return-value]

    def get_by_id(self, tote_id: str) -> Tote:
        """Retrieve details of a specific tote."""
        response = self._api.request("GET", f"/v2/totes/{tote_id}", params=None, json_body=None)
        return Tote.model_validate(response.json())

    def update(
        self,
        tote_id: str,
        *,
        body: ToteUpdateRequest,
    ) -> None:
        """Update the name or barcode of an existing tote."""
        response = self._api.request("PUT", f"/v2/totes/{tote_id}", params=None, json_body=serialize_body(body))
        return None

    def delete(self, tote_id: str) -> None:
        """Delete a tote by its ID."""
        response = self._api.request("DELETE", f"/v2/totes/{tote_id}", params=None, json_body=None)
        return None
