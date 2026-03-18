"""ShipStation users resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


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
            params["status"] = serialize_param(status)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if page is not None:
            params["page"] = serialize_param(page)
        response = self._api.request("GET", "/v2/users", params=params, json_body=None)
        return response.json()  # type: ignore[return-value]
