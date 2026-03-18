"""ShipStation webhooks resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    CreateWebhookRequestBody,
    CreateWebhookResponseBody,
    GetWebhookByIdResponseBody,
    UpdateWebhookRequestBody,
)


class WebhooksResource:
    """Webhooks API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self) -> ListWebhooksResponseBody:
        """List all webhooks currently enabled for the account."""
        response = self._api.request("GET", "/v2/environment/webhooks", params=None, json_body=None)
        return ListWebhooksResponseBody.model_validate(response.json())

    def create(self, *, body: CreateWebhookRequestBody) -> CreateWebhookResponseBody:
        """Create a webhook for specific events in the environment."""
        response = self._api.request("POST", "/v2/environment/webhooks", params=None, json_body=serialize_body(body))
        return CreateWebhookResponseBody.model_validate(response.json())

    def get_by_id(self, webhook_id: str) -> GetWebhookByIdResponseBody:
        """Retrieve individual webhook by an ID"""
        response = self._api.request("GET", f"/v2/environment/webhooks/{webhook_id}", params=None, json_body=None)
        return GetWebhookByIdResponseBody.model_validate(response.json())

    def update(
        self,
        webhook_id: str,
        *,
        body: UpdateWebhookRequestBody,
    ) -> None:
        """Update the webhook url property"""
        response = self._api.request("PUT", f"/v2/environment/webhooks/{webhook_id}", params=None, json_body=serialize_body(body))
        return None

    def delete(self, webhook_id: str) -> None:
        """Delete a webhook"""
        response = self._api.request("DELETE", f"/v2/environment/webhooks/{webhook_id}", params=None, json_body=None)
        return None
