"""Low-level HTTP client for ShipStation API — auto-generated, do not edit."""

from __future__ import annotations

from typing import Any

import requests


class ShipStationError(Exception):
    """Raised when the ShipStation API returns an error response."""

    def __init__(
        self,
        status_code: int,
        message: str,
        response: requests.Response | None = None,
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"[{status_code}] {message}")


def serialize_param(value: Any) -> Any:
    """Serialize a parameter value for query string use."""
    if hasattr(value, "value"):
        return value.value
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def serialize_body(body: Any) -> Any:
    """Serialize a request body for JSON use."""
    if hasattr(body, "model_dump"):
        return body.model_dump(exclude_none=True, by_alias=True)
    return body


class ApiClient:
    """Thin wrapper around ``requests.Session`` for ShipStation API calls."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.shipstation.com",
        timeout: float = 30.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any | None = None,
    ) -> requests.Response:
        url = f"{self.base_url}{path}"
        resp = self.session.request(
            method,
            url,
            params=params,
            json=json_body,
            timeout=self.timeout,
        )
        if resp.status_code >= 400:
            try:
                detail = resp.json()
                msg = detail.get("message", resp.text)
            except Exception:
                msg = resp.text
            raise ShipStationError(resp.status_code, msg, resp)
        return resp
