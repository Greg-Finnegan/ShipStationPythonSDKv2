"""ShipStation package_types models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    Dimensions,
    PackageType,
)


class CreatePackageTypeRequestBody(BaseModel):
    """A create package type request body"""

    model_config = ConfigDict(populate_by_name=True)

    package_code: str
    name: str
    package_id: Optional[str] = None
    """A string that uniquely identifies the package."""
    dimensions: Optional[Dimensions] = None
    """The custom dimensions for the package."""
    description: Optional[str] = None
    """Provides a helpful description for the custom package."""


class CreatePackageTypeResponseBody(BaseModel):
    """A create package type response body"""

    model_config = ConfigDict(populate_by_name=True)

    package_code: str
    name: str
    package_id: Optional[str] = None
    """A string that uniquely identifies the package."""
    dimensions: Optional[Dimensions] = None
    """The custom dimensions for the package."""
    description: Optional[str] = None
    """Provides a helpful description for the custom package."""


class GetPackageTypeByIdResponseBody(BaseModel):
    """A get package type by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    package_code: str
    name: str
    package_id: Optional[str] = None
    """A string that uniquely identifies the package."""
    dimensions: Optional[Dimensions] = None
    """The custom dimensions for the package."""
    description: Optional[str] = None
    """Provides a helpful description for the custom package."""


class ListPackageTypesResponseBody(BaseModel):
    """A list package types response body"""

    model_config = ConfigDict(populate_by_name=True)

    packages: Optional[list[PackageType]] = None
    """An array of custom package types"""


class UpdatePackageTypeRequestBody(BaseModel):
    """An update package type request body"""

    model_config = ConfigDict(populate_by_name=True)

    package_code: str
    name: str
    package_id: Optional[str] = None
    """A string that uniquely identifies the package."""
    dimensions: Optional[Dimensions] = None
    """The custom dimensions for the package."""
    description: Optional[str] = None
    """Provides a helpful description for the custom package."""
