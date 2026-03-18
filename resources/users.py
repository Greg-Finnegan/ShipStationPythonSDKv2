"""ShipStation users resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient


class UsersResource:
    """Users API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        status: Optional[str] = None,
        page_size: Optional[int] = 25,
        page: Optional[int] = 1,
    ) -> Any:
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status.value if hasattr(status, 'value') else (status.isoformat() if hasattr(status, 'isoformat') else status)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        response = self._api.request("GET", "/v2/users", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]
