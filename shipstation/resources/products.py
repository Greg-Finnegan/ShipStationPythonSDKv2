"""ShipStation products resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


class ProductsResource:
    """Products API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        sku: Optional[str] = None,
        name: Optional[str] = None,
        active: Optional[bool] = None,
        page_size: Optional[int] = 100,
        page: Optional[int] = 1,
    ) -> Any:
        params: dict[str, Any] = {}
        if sku is not None:
            params["sku"] = serialize_param(sku)
        if name is not None:
            params["name"] = serialize_param(name)
        if active is not None:
            params["active"] = serialize_param(active)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if page is not None:
            params["page"] = serialize_param(page)
        response = self._api.request("GET", "/v2/products", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]
