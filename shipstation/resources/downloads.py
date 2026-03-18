"""ShipStation downloads resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


class DownloadsResource:
    """Downloads API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def file(
        self,
        subdir: str,
        filename: str,
        dir: str,
        *,
        download: Optional[str] = None,
        rotation: Optional[int] = None,
    ) -> None:
        """Download labels and other shipment-related documents."""
        params: dict[str, Any] = {}
        if download is not None:
            params["download"] = serialize_param(download)
        if rotation is not None:
            params["rotation"] = serialize_param(rotation)
        response = self._api.request("GET", f"/v2/downloads/{dir}/{subdir}/{filename}", params=params, json_body=None)
        return None
