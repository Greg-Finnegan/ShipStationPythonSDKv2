"""ShipStation products resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient


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
            params["sku"] = sku.value if hasattr(sku, 'value') else (sku.isoformat() if hasattr(sku, 'isoformat') else sku)
        if name is not None:
            params["name"] = name.value if hasattr(name, 'value') else (name.isoformat() if hasattr(name, 'isoformat') else name)
        if active is not None:
            params["active"] = active.value if hasattr(active, 'value') else (active.isoformat() if hasattr(active, 'isoformat') else active)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        response = self._api.request("GET", "/v2/products", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]
