"""ShipStation tags models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    Tag,
)


class CreateTagResponseBody(BaseModel):
    """Response body for creating tags"""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The tag name."""


class ListTagsResponseBody(BaseModel):
    """Response body from a successful GET /tags API call"""

    model_config = ConfigDict(populate_by_name=True)

    tags: Optional[list[Tag]] = None
    """The array of tags returned by the API call"""
