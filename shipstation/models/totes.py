"""ShipStation totes models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field



class Tote(BaseModel):
    """A tote (bin or container) used in warehouse picking and packing operations"""

    model_config = ConfigDict(populate_by_name=True)

    tote_id: str
    """Unique identifier for the tote"""
    inventory_warehouse_id: str
    """The warehouse this tote belongs to"""
    tote_name: str
    """Name of the tote"""
    created_at: datetime
    """Date and time when the tote was created"""
    tote_barcode: Optional[str] = None
    """Barcode identifier for the tote"""


class FailedToteResponse(BaseModel):
    """Information about a failed tote creation"""

    model_config = ConfigDict(populate_by_name=True)

    inventory_warehouse_id: Optional[str] = None
    """The warehouse ID from the failed request"""
    tote_name: Optional[str] = None
    """The tote name from the failed request"""
    tote_barcode: Optional[str] = None
    """The tote barcode from the failed request"""
    error_message: Optional[str] = None
    """Error message explaining why creation failed"""


class BulkCreateToteResponse(BaseModel):
    """Response for batch tote creation"""

    model_config = ConfigDict(populate_by_name=True)

    succeeded_totes: Optional[list[Tote]] = None
    """Totes that were successfully created"""
    failed_totes: Optional[list[FailedToteResponse]] = None
    """Totes that failed to be created"""


class ToteCreateRequest(BaseModel):
    """Request to create a new tote"""

    model_config = ConfigDict(populate_by_name=True)

    inventory_warehouse_id: str
    """The warehouse where this tote will be created"""
    tote_name: str
    """Name for the new tote"""
    tote_barcode: Optional[str] = None
    """Barcode identifier for the tote (optional)"""


class ToteCreateBatchRequest(BaseModel):
    """Request to create multiple totes in batch"""

    model_config = ConfigDict(populate_by_name=True)

    totes: list[ToteCreateRequest]
    """Array of totes to create"""
    return_succeeded_totes: Optional[bool] = None
    """Whether to include successfully created totes in the response. When false, only failed_totes will be returned."""


class ToteUpdateRequest(BaseModel):
    """Request to update an existing tote"""

    model_config = ConfigDict(populate_by_name=True)

    inventory_warehouse_id: str
    """The warehouse where this tote is located"""
    tote_name: str
    """Updated name for the tote"""
    tote_barcode: Optional[str] = None
    """Updated barcode for the tote"""
