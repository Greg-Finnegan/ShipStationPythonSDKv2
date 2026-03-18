"""ShipStation warehouses models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    Address,
)


class GetWarehouseByIdResponseBody(BaseModel):
    """A get warehouse by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    warehouse_id: str
    """A string that uniquely identifies the warehouse"""
    name: str
    """Name of the warehouse"""
    created_at: datetime
    """Timestamp that indicates when the warehouse was created"""
    origin_address: Address
    """The origin address of the warehouse"""
    return_address: Address
    """The return address associated with the warehouse"""
    is_default: Optional[bool] = None
    """Designates which single warehouse is the default on the account"""


class Warehouse(BaseModel):
    """A warehouse"""

    model_config = ConfigDict(populate_by_name=True)

    warehouse_id: Optional[str] = None
    """A string that uniquely identifies the warehouse"""
    is_default: Optional[bool] = None
    """Designates which single warehouse is the default on the account"""
    name: Optional[str] = None
    """Name of the warehouse"""
    created_at: Optional[datetime] = None
    """Timestamp that indicates when the warehouse was created"""
    origin_address: Optional[Address] = None
    """The origin address of the warehouse"""
    return_address: Optional[Address] = None
    """The return address associated with the warehouse"""


class ListWarehousesResponseBody(BaseModel):
    """A warehouse list response body"""

    model_config = ConfigDict(populate_by_name=True)

    warehouses: list[Warehouse]
    """The array of warehouses returned by the API call"""
