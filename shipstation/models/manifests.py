"""ShipStation manifests models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    ErrorWithLabelId,
    Manifest,
    ManifestDownload,
    PaginationLink,
)
from ..enums import (
    ManifestRequestStatus,
)


class CreateManifestByObjectRequestBody(BaseModel):
    """A create manifest request body"""

    model_config = ConfigDict(populate_by_name=True)

    carrier_id: str
    """A string that uniquely identifies the carrier"""
    warehouse_id: str
    """A string that uniquely identifies the warehouse"""
    ship_date: datetime
    """The ship date that the shipment will be sent out on"""
    excluded_label_ids: Optional[list[str]] = None
    """The list of label ids to exclude from the manifest"""
    label_ids: Optional[list[str]] = None
    """The list of label ids to include for the manifest"""


class CreateManifestLabelIdsRequestBody(BaseModel):
    """A create manifest request body"""

    model_config = ConfigDict(populate_by_name=True)

    label_ids: list[str]
    """The list of label ids to include in the manifest"""


class CreateManifestResponseBody(BaseModel):
    """A create manifest response body"""

    model_config = ConfigDict(populate_by_name=True)

    manifest_id: str
    """A string that uniquely identifies the manifest"""
    form_id: str
    """A string that uniquely identifies the form"""
    created_at: datetime
    """The date-time that the manifest was created"""
    ship_date: datetime
    """The date-time that the manifests shipments will be picked up"""
    shipments: int
    """The number of shipments that are included in this manifest"""
    warehouse_id: str
    """A string that uniquely identifies the warehouse"""
    submission_id: str
    """A string that uniquely identifies the submission"""
    carrier_id: str
    """A string that uniquely identifies the carrier"""
    manifest_download: ManifestDownload
    request_id: str
    """A UUID that uniquely identifies the request id. This can be given to the support team to help debug non-trivial issues t"""
    errors: list[ErrorWithLabelId]
    """The errors associated with the failed API call"""
    manifests: Optional[list[Manifest]] = None
    """Resulting Manifests"""
    manifest_request_id: Optional[str] = None
    """A string that uniquely identifies a manifest request"""
    status: Optional[ManifestRequestStatus] = None
    label_ids: Optional[list[str]] = None
    """An array of the label ids used in this manifest."""


class GetManifestByIdResponseBody(BaseModel):
    """A get manifest by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    manifest_id: str
    """A string that uniquely identifies the manifest"""
    form_id: str
    """A string that uniquely identifies the form"""
    created_at: datetime
    """The date-time that the manifest was created"""
    ship_date: datetime
    """The date-time that the manifests shipments will be picked up"""
    shipments: int
    """The number of shipments that are included in this manifest"""
    label_ids: list[str]
    """An array of the label ids used in this manifest."""
    warehouse_id: str
    """A string that uniquely identifies the warehouse"""
    submission_id: str
    """A string that uniquely identifies the submission"""
    carrier_id: str
    """A string that uniquely identifies the carrier"""
    manifest_download: ManifestDownload


class ListManifestsResponseBody(BaseModel):
    """A list manifests response body"""

    model_config = ConfigDict(populate_by_name=True)

    manifests: list[Manifest]
    """The list of available manifests"""
    total: int
    """The total number of manifests returned"""
    page: int
    """Current page of the list manifests results"""
    pages: int
    """Total number of pages for list manifests results"""
    links: PaginationLink
    """Helpful links to other pages of results"""
