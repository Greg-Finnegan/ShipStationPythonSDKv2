"""ShipStation carriers models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    PackageType,
)


class Service(BaseModel):
    """A service offered by the carrier"""

    model_config = ConfigDict(populate_by_name=True)

    carrier_id: Optional[str] = None
    """A string that uniquely identifies the carrier"""
    carrier_code: Optional[str] = None
    service_code: Optional[str] = None
    """service code"""
    name: Optional[str] = None
    """User friendly service name"""
    domestic: Optional[bool] = None
    """Supports domestic shipping"""
    international: Optional[bool] = None
    """Supports international shipping."""
    is_multi_package_supported: Optional[bool] = None
    """Carrier supports multiple packages per shipment"""


class CarrierAdvancedOption(BaseModel):
    """Advanced options that are specific to the carrier"""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    """Name of advanced option"""
    default_value: Optional[str] = None
    """Default value of option"""
    description: Optional[str] = None
    """Description of option"""


class Carrier(BaseModel):
    """
    A carrier object that represents a provider such as UPS, USPS, DHL, etc that has been
    tied to the current account.
    """

    model_config = ConfigDict(populate_by_name=True)

    carrier_id: Optional[str] = None
    """A string that uniquely identifies the carrier."""
    carrier_code: Optional[str] = None
    """The [shipping carrier] who will ship the package, such as `fedex`, `dhl_express`, `stamps_com`, etc."""
    account_number: Optional[str] = None
    """The account number that the carrier is connected to."""
    connection_status: Optional[str] = None
    """The connection status of the carrier account. Indicates whether the carrier connection is pending approval or has been a"""
    requires_funded_amount: Optional[bool] = None
    """Indicates whether the carrier requires funding to use its services"""
    balance: Optional[float] = None
    """Current available balance"""
    nickname: Optional[str] = None
    """Nickname given to the account when initially setting up the carrier."""
    friendly_name: Optional[str] = None
    """Screen readable name"""
    funding_source_id: Optional[str] = None
    """Funding source ID for the carrier"""
    primary: Optional[bool] = None
    """Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation"""
    has_multi_package_supporting_services: Optional[bool] = None
    """Carrier supports multiple packages per shipment"""
    supports_label_messages: Optional[bool] = None
    """The carrier supports adding custom label messages to an order."""
    disabled_by_billing_plan: Optional[bool] = None
    """The carrier is disabled by the current ShipStation account's billing plan."""
    services: Optional[list[Service]] = None
    """A list of services that are offered by the carrier"""
    packages: Optional[list[PackageType]] = None
    """A list of package types that are supported by the carrier"""
    options: Optional[list[CarrierAdvancedOption]] = None
    """A list of options that are available to that carrier"""
    send_rates: Optional[bool] = None
    """The carrier provides rates for the shipment."""
    supports_user_managed_rates: Optional[bool] = None
    """The carrier supports user-managed rates for shipments."""


class GetCarrierByIdResponseBody(BaseModel):
    """A get carrier by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    carrier_id: Optional[str] = None
    """A string that uniquely identifies the carrier."""
    carrier_code: Optional[str] = None
    """The [shipping carrier] who will ship the package, such as `fedex`, `dhl_express`, `stamps_com`, etc."""
    account_number: Optional[str] = None
    """The account number that the carrier is connected to."""
    connection_status: Optional[str] = None
    """The connection status of the carrier account. Indicates whether the carrier connection is pending approval or has been a"""
    requires_funded_amount: Optional[bool] = None
    """Indicates whether the carrier requires funding to use its services"""
    balance: Optional[float] = None
    """Current available balance"""
    nickname: Optional[str] = None
    """Nickname given to the account when initially setting up the carrier."""
    friendly_name: Optional[str] = None
    """Screen readable name"""
    funding_source_id: Optional[str] = None
    """Funding source ID for the carrier"""
    primary: Optional[bool] = None
    """Is this the primary carrier that is used by default when no carrier is specified in label/shipment creation"""
    has_multi_package_supporting_services: Optional[bool] = None
    """Carrier supports multiple packages per shipment"""
    supports_label_messages: Optional[bool] = None
    """The carrier supports adding custom label messages to an order."""
    disabled_by_billing_plan: Optional[bool] = None
    """The carrier is disabled by the current ShipStation account's billing plan."""
    services: Optional[list[Service]] = None
    """A list of services that are offered by the carrier"""
    packages: Optional[list[PackageType]] = None
    """A list of package types that are supported by the carrier"""
    options: Optional[list[CarrierAdvancedOption]] = None
    """A list of options that are available to that carrier"""
    send_rates: Optional[bool] = None
    """The carrier provides rates for the shipment."""
    supports_user_managed_rates: Optional[bool] = None
    """The carrier supports user-managed rates for shipments."""


class GetCarrierOptionsResponseBody(BaseModel):
    """A carrier list options response body"""

    model_config = ConfigDict(populate_by_name=True)

    options: Optional[list[CarrierAdvancedOption]] = None
    """AN array of carrier options"""


class ListCarrierPackageTypesResponseBody(BaseModel):
    """A list carrier package types response body"""

    model_config = ConfigDict(populate_by_name=True)

    packages: Optional[list[PackageType]] = None
    """An array of custom package types"""


class ListCarrierServicesResponseBody(BaseModel):
    """A carrier list services response body"""

    model_config = ConfigDict(populate_by_name=True)

    services: Optional[list[Service]] = None
    """An array of services associated with the carrier"""


class ListCarriersResponseBody(BaseModel):
    """A carrier list response body"""

    model_config = ConfigDict(populate_by_name=True)

    carriers: list[Carrier]
    """The carrier response body"""
