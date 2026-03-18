"""ShipStation tags resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    CreateTagResponseBody,
    ListTagsResponseBody,
)


class TagsResource:
    """Tags API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self) -> ListTagsResponseBody:
        """Get a list of all tags associated with an account."""
        response = self._api.request("GET", "/v2/tags", params=None, json_body=None)
        return ListTagsResponseBody.model_validate(response.json())

    def create(self, tag_name: str) -> CreateTagResponseBody:
        """Create a new Tag for customizing how you track your shipments"""
        response = self._api.request("POST", f"/v2/tags/{tag_name}", params=None, json_body=None)
        return CreateTagResponseBody.model_validate(response.json())
