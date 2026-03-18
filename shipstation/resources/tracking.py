"""ShipStation tracking resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param


class TrackingResource:
    """Tracking API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def stop(
        self,
        *,
        carrier_code: Optional[str] = None,
        tracking_number: Optional[str] = None,
    ) -> None:
        """Unsubscribe from tracking updates for a package."""
        params: dict[str, Any] = {}
        if carrier_code is not None:
            params["carrier_code"] = serialize_param(carrier_code)
        if tracking_number is not None:
            params["tracking_number"] = serialize_param(tracking_number)
        response = self._api.request("POST", "/v2/tracking/stop", params=params, json_body=None)
        return None
