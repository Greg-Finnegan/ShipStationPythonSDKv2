"""ShipStation webhooks models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    WebhookHeader,
)
from ..enums import (
    WebhookEvent,
)


class CreateWebhookRequestBody(BaseModel):
    """A create webhook request body"""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The name of the webhook"""
    event: WebhookEvent
    url: str
    """The url that the webhook sends the request to"""
    headers: Optional[list[WebhookHeader]] = None
    """Array of custom webhook headers"""
    store_id: Optional[int] = None
    """Store ID"""


class CreateWebhookResponseBody(BaseModel):
    """A webhook response body"""

    model_config = ConfigDict(populate_by_name=True)

    webhook_id: str
    """A string that uniquely identifies the webhook"""
    url: str
    """The url that the webhook sends the request to"""
    event: WebhookEvent
    name: str
    """The name of the webhook"""
    headers: Optional[list[WebhookHeader]] = None
    """Array of custom webhook headers"""
    store_id: Optional[int] = None
    """Store ID"""


class GetWebhookByIdResponseBody(BaseModel):
    """A get webhook id response body"""

    model_config = ConfigDict(populate_by_name=True)

    webhook_id: str
    """A string that uniquely identifies the webhook"""
    url: str
    """The url that the webhook sends the request to"""
    event: WebhookEvent
    headers: Optional[list[WebhookHeader]] = None
    """Array of custom webhook headers"""
    name: Optional[str] = None
    """The name of the webhook"""
    store_id: Optional[int] = None
    """Store ID"""


class UpdateWebhookRequestBody(BaseModel):
    """An update webhook request body"""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    """The name of the webhook"""
    url: Optional[str] = None
    """The url that the webhook sends the request"""
    headers: Optional[list[WebhookHeader]] = None
    """Array of custom webhook headers"""
