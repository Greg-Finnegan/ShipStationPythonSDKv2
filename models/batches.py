"""ShipStation batches models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    Error,
    LabelDownload,
    OptionalLink,
    PaginationLink,
    PaperlessDownload,
)
from ..enums import (
    BatchStatus,
    DisplayScheme,
    LabelFormat,
    LabelLayout,
)


class CreateBatchResponseBody(BaseModel):
    """A create batch response body"""

    model_config = ConfigDict(populate_by_name=True)

    label_layout: LabelLayout
    """label layout"""
    label_format: LabelFormat
    batch_id: str
    """A string that uniquely identifies the batch"""
    batch_number: str
    """The batch number."""
    external_batch_id: str
    """A string that uniquely identifies the external batch"""
    batch_notes: str
    """Custom notes you can add for each created batch"""
    created_at: datetime
    """The date and time the batch was created in ShipStation"""
    processed_at: datetime
    """The date and time the batch was processed in ShipStation"""
    errors: int
    """The number of errors that occurred while generating the batch"""
    process_errors: list[Error]
    """The errors associated with the failed API call"""
    warnings: int
    """The number of warnings that occurred while generating the batch"""
    completed: int
    """The number of labels generated in the batch"""
    forms: int
    """The number of forms for customs that are available for download"""
    count: int
    """The total of errors, warnings, and completed properties"""
    batch_shipments_url: OptionalLink
    """The batch shipments endpoint"""
    batch_labels_url: OptionalLink
    """Link to batch labels query"""
    batch_errors_url: OptionalLink
    """Link to batch errors endpoint"""
    label_download: LabelDownload
    """The label download for the batch"""
    form_download: OptionalLink
    """The form download for any customs that are needed"""
    paperless_download: PaperlessDownload
    """The paperless details which may contain elements like `href`, `instructions` and `handoff_code`."""
    status: BatchStatus


class Batch(BaseModel):
    """
    Batches are an advanced feature of ShipStation designed for users who need to generate
    hundreds or thousands of labels at a time.
    """

    model_config = ConfigDict(populate_by_name=True)

    label_layout: LabelLayout
    """label layout"""
    label_format: LabelFormat
    batch_id: str
    """A string that uniquely identifies the batch"""
    batch_number: str
    """The batch number."""
    external_batch_id: str
    """A string that uniquely identifies the external batch"""
    batch_notes: str
    """Custom notes you can add for each created batch"""
    created_at: datetime
    """The date and time the batch was created in ShipStation"""
    processed_at: datetime
    """The date and time the batch was processed in ShipStation"""
    errors: int
    """The number of errors that occurred while generating the batch"""
    process_errors: list[Error]
    """The errors associated with the failed API call"""
    warnings: int
    """The number of warnings that occurred while generating the batch"""
    completed: int
    """The number of labels generated in the batch"""
    forms: int
    """The number of forms for customs that are available for download"""
    count: int
    """The total of errors, warnings, and completed properties"""
    batch_shipments_url: OptionalLink
    """The batch shipments endpoint"""
    batch_labels_url: OptionalLink
    """Link to batch labels query"""
    batch_errors_url: OptionalLink
    """Link to batch errors endpoint"""
    label_download: LabelDownload
    """The label download for the batch"""
    form_download: OptionalLink
    """The form download for any customs that are needed"""
    paperless_download: PaperlessDownload
    """The paperless details which may contain elements like `href`, `instructions` and `handoff_code`."""
    status: BatchStatus


class ListBatchesResponseBody(BaseModel):
    """A list batch response body"""

    model_config = ConfigDict(populate_by_name=True)

    batches: list[Batch]
    """Batch List"""
    total: int
    """The total number of batches the API call returned"""
    page: int
    """The page that is currently being read"""
    pages: int
    """The total number of batch pages the API call returned"""
    links: PaginationLink


class CreateAndProcessBatchRequestBody(BaseModel):
    """A create and process batch request body"""

    model_config = ConfigDict(populate_by_name=True)

    external_batch_id: Optional[str] = None
    """A string that uniquely identifies the external batch"""
    batch_notes: Optional[str] = None
    """Add custom messages for a particular batch"""
    shipment_ids: Optional[list[str]] = None
    """Array of shipment IDs used in the batch"""
    rate_ids: Optional[list[str]] = None
    """Array of rate IDs used in the batch"""
    process_labels: Optional[dict[str, Any]] = None
    """The information used to process the batch"""


class CreateBatchRequestBody(BaseModel):
    """A create batch request body"""

    model_config = ConfigDict(populate_by_name=True)

    external_batch_id: Optional[str] = None
    """A string that uniquely identifies the external batch"""
    batch_notes: Optional[str] = None
    """Add custom messages for a particular batch"""
    shipment_ids: Optional[list[str]] = None
    """Array of shipment IDs used in the batch"""
    rate_ids: Optional[list[str]] = None
    """Array of rate IDs used in the batch"""


class GetBatchByExternalIdResponseBody(BaseModel):
    """A get batch by external id response body"""

    model_config = ConfigDict(populate_by_name=True)

    label_layout: LabelLayout
    """label layout"""
    label_format: LabelFormat
    batch_id: str
    """A string that uniquely identifies the batch"""
    batch_number: str
    """The batch number."""
    external_batch_id: str
    """A string that uniquely identifies the external batch"""
    batch_notes: str
    """Custom notes you can add for each created batch"""
    created_at: datetime
    """The date and time the batch was created in ShipStation"""
    processed_at: datetime
    """The date and time the batch was processed in ShipStation"""
    errors: int
    """The number of errors that occurred while generating the batch"""
    process_errors: list[Error]
    """The errors associated with the failed API call"""
    warnings: int
    """The number of warnings that occurred while generating the batch"""
    completed: int
    """The number of labels generated in the batch"""
    forms: int
    """The number of forms for customs that are available for download"""
    count: int
    """The total of errors, warnings, and completed properties"""
    batch_shipments_url: OptionalLink
    """The batch shipments endpoint"""
    batch_labels_url: OptionalLink
    """Link to batch labels query"""
    batch_errors_url: OptionalLink
    """Link to batch errors endpoint"""
    label_download: LabelDownload
    """The label download for the batch"""
    form_download: OptionalLink
    """The form download for any customs that are needed"""
    paperless_download: PaperlessDownload
    """The paperless details which may contain elements like `href`, `instructions` and `handoff_code`."""
    status: BatchStatus


class GetBatchByIdResponseBody(BaseModel):
    """A get batch by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    label_layout: LabelLayout
    """label layout"""
    label_format: LabelFormat
    batch_id: str
    """A string that uniquely identifies the batch"""
    batch_number: str
    """The batch number."""
    external_batch_id: str
    """A string that uniquely identifies the external batch"""
    batch_notes: str
    """Custom notes you can add for each created batch"""
    created_at: datetime
    """The date and time the batch was created in ShipStation"""
    processed_at: datetime
    """The date and time the batch was processed in ShipStation"""
    errors: int
    """The number of errors that occurred while generating the batch"""
    process_errors: list[Error]
    """The errors associated with the failed API call"""
    warnings: int
    """The number of warnings that occurred while generating the batch"""
    completed: int
    """The number of labels generated in the batch"""
    forms: int
    """The number of forms for customs that are available for download"""
    count: int
    """The total of errors, warnings, and completed properties"""
    batch_shipments_url: OptionalLink
    """The batch shipments endpoint"""
    batch_labels_url: OptionalLink
    """Link to batch labels query"""
    batch_errors_url: OptionalLink
    """Link to batch errors endpoint"""
    label_download: LabelDownload
    """The label download for the batch"""
    form_download: OptionalLink
    """The form download for any customs that are needed"""
    paperless_download: PaperlessDownload
    """The paperless details which may contain elements like `href`, `instructions` and `handoff_code`."""
    status: BatchStatus


class ListBatchErrorsResponseBody(BaseModel):
    """A batch errors response body"""

    model_config = ConfigDict(populate_by_name=True)

    errors: list[dict[str, Any]]
    """The errors currently associated with the batch"""
    links: PaginationLink


class ProcessBatchRequestBody(BaseModel):
    """A process batch request body"""

    model_config = ConfigDict(populate_by_name=True)

    ship_date: Optional[datetime] = None
    """The Ship date the batch is being processed for"""
    label_layout: Optional[LabelLayout] = None
    label_format: Optional[LabelFormat] = None
    display_scheme: Optional[DisplayScheme] = None
    """The display format that the label should be shown in."""


class RemoveFromBatchRequestBody(BaseModel):
    """A modify batch request body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_ids: Optional[list[str]] = None
    """The Shipment Ids to be modified on the batch"""
    rate_ids: Optional[list[str]] = None
    """Array of Rate IDs to be modifed on the batch"""
