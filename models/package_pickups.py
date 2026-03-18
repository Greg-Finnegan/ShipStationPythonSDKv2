"""ShipStation package_pickups models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    Address,
    PaginationLink,
)


class DeleteScheduledPickupResponseBody(BaseModel):
    """A delete scheduled pickup response body"""

    model_config = ConfigDict(populate_by_name=True)

    pickup_id: str


class Pickup(BaseModel):
    """The information necessary to schedule a package pickup"""

    model_config = ConfigDict(populate_by_name=True)

    pickup_id: Optional[str] = None
    label_ids: Optional[list[str]] = None
    """Label IDs that will be included in the pickup request"""
    created_at: Optional[datetime] = None
    """The date and time that the pickup was created in ShipStation ."""
    cancelled_at: Optional[datetime] = None
    """The date and time that the pickup was cancelled in ShipStation ."""
    carrier_id: Optional[str] = None
    """The carrier_id associated with the pickup"""
    confirmation_number: Optional[str] = None
    """The carrier confirmation number for the scheduled pickup."""
    warehouse_id: Optional[str] = None
    """The warehouse_id associated with the pickup"""
    pickup_address: Optional[Address] = None
    contact_details: Optional[dict[str, Any]] = None
    pickup_notes: Optional[str] = None
    """Used by some carriers to give special instructions for a package pickup"""
    pickup_window: Optional[dict[str, Any]] = None
    """The desired time range for the package pickup."""
    pickup_windows: Optional[list[Any]] = None
    """An array of available pickup windows. Carriers can return multiple times that they will pickup packages."""


class ListPickupResponseBody(BaseModel):
    """A list pickup response body"""

    model_config = ConfigDict(populate_by_name=True)

    pickups: list[Pickup]
    """An array of pickups associated with the user's account."""
    total: int
    """The total number of pickups returned"""
    page: int
    """Current page of the list pickups results"""
    pages: int
    """Total number of pages for list pickups results"""
    links: PaginationLink
    """Helpful links to other pages of results"""


class PickupResponseBody(BaseModel):
    """A pickup response body"""

    model_config = ConfigDict(populate_by_name=True)

    pickup_id: str
    label_ids: list[str]
    """Label IDs that will be included in the pickup request"""
    created_at: datetime
    """The date and time that the pickup was created in ShipStation ."""
    carrier_id: str
    """The carrier_id associated with the pickup"""
    confirmation_number: str
    """The carrier confirmation number for the scheduled pickup."""
    warehouse_id: str
    """The warehouse_id associated with the pickup"""
    pickup_address: Address
    contact_details: dict[str, Any]
    pickup_window: dict[str, Any]
    """The desired time range for the package pickup."""
    cancelled_at: Optional[datetime] = None
    """The date and time that the pickup was cancelled in ShipStation ."""
    pickup_notes: Optional[str] = None
    """Used by some carriers to give special instructions for a package pickup"""
    pickup_windows: Optional[list[Any]] = None
    """An array of available pickup windows. Carriers can return multiple times that they will pickup packages."""


class SchedulePickupRequestBody(BaseModel):
    """A schedule pickup request body"""

    model_config = ConfigDict(populate_by_name=True)

    label_ids: list[str]
    """Label IDs that will be included in the pickup request"""
    contact_details: dict[str, Any]
    pickup_window: dict[str, Any]
    """The desired time range for the package pickup."""
    pickup_id: Optional[str] = None
    created_at: Optional[datetime] = None
    """The date and time that the pickup was created in ShipStation ."""
    cancelled_at: Optional[datetime] = None
    """The date and time that the pickup was cancelled in ShipStation ."""
    carrier_id: Optional[str] = None
    """The carrier_id associated with the pickup"""
    confirmation_number: Optional[str] = None
    """The carrier confirmation number for the scheduled pickup."""
    warehouse_id: Optional[str] = None
    """The warehouse_id associated with the pickup"""
    pickup_address: Optional[Address] = None
    pickup_notes: Optional[str] = None
    """Used by some carriers to give special instructions for a package pickup"""
    pickup_windows: Optional[list[Any]] = None
    """An array of available pickup windows. Carriers can return multiple times that they will pickup packages."""


class SchedulePickupResponseBody(BaseModel):
    """A schedule pickup response body"""

    model_config = ConfigDict(populate_by_name=True)

    pickup_id: str
    label_ids: list[str]
    """Label IDs that will be included in the pickup request"""
    created_at: datetime
    """The date and time that the pickup was created in ShipStation ."""
    carrier_id: str
    """The carrier_id associated with the pickup"""
    confirmation_number: str
    """The carrier confirmation number for the scheduled pickup."""
    warehouse_id: str
    """The warehouse_id associated with the pickup"""
    pickup_address: Address
    contact_details: dict[str, Any]
    pickup_window: dict[str, Any]
    """The desired time range for the package pickup."""
    cancelled_at: Optional[datetime] = None
    """The date and time that the pickup was cancelled in ShipStation ."""
    pickup_notes: Optional[str] = None
    """Used by some carriers to give special instructions for a package pickup"""
    pickup_windows: Optional[list[Any]] = None
    """An array of available pickup windows. Carriers can return multiple times that they will pickup packages."""
