"""ShipStation rates models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    AdvancedShipmentOptions,
    Dimensions,
    Error,
    InternationalShipmentOptions,
    MonetaryValue,
    Package,
    Rate,
    ShipmentItem,
    ShippingAddress,
    ShippingAddressTo,
    Tag,
    TaxIdentifier,
    Weigth,
)
from ..enums import (
    AddressResidentialIndicator,
    DeliveryConfirmation,
    InsuranceProvider,
    OrderSourceName,
    RateResponseStatus,
    RateType,
    ShipmentStatus,
    ValidationStatus,
)


class RateRequestBody(BaseModel):
    """A rate request body"""

    model_config = ConfigDict(populate_by_name=True)

    carrier_ids: list[str]
    """Array of carrier ids to get rates for"""
    package_types: Optional[list[str]] = None
    service_codes: Optional[list[str]] = None
    calculate_tax_amount: Optional[bool] = None
    """Calculate the duties and tariffs for cross border shipments."""
    preferred_currency: Optional[str] = None
    is_return: Optional[bool] = None
    """Indicate if it's a return shipment"""


class CalculateRatesRequestBody(BaseModel):
    """A rate shipment request body"""

    model_config = ConfigDict(populate_by_name=True)

    rate_options: Optional[RateRequestBody] = None
    """The rate options"""


class RatesInformation(BaseModel):
    """A rates information resource"""

    model_config = ConfigDict(populate_by_name=True)

    rates: Optional[list[Rate]] = None
    """An array of shipment rates"""
    invalid_rates: Optional[list[Rate]] = None
    """An array of invalid shipment rates"""
    rate_request_id: Optional[str] = None
    """A string that uniquely identifies the rate request"""
    shipment_id: Optional[str] = None
    """A string that uniquely identifies the shipment"""
    created_at: Optional[str] = None
    """When the rate was created"""
    status: Optional[RateResponseStatus] = None
    errors: Optional[list[Error]] = None


class CalculateRatesResponseBody(BaseModel):
    """A rate shipment response body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    ship_date: str
    """The date that the shipment was (or will be) shippped. ShipStation will take the day of week into consideration. For exam"""
    created_at: datetime
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: datetime
    """The date and time that the shipment was created or last modified."""
    shipment_status: ShipmentStatus
    """The current status of the shipment"""
    return_to: ShippingAddress
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    confirmation: DeliveryConfirmation
    """The type of delivery confirmation that is required for this shipment"""
    customs: InternationalShipmentOptions
    """Customs information. This is usually only needed for international shipments."""
    advanced_options: AdvancedShipmentOptions
    """Advanced shipment options. These are entirely optional."""
    insurance_provider: InsuranceProvider
    """The insurance provider to use for any insured packages in the shipment."""
    tags: list[Tag]
    """Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by """
    packages: list[Package]
    """The packages in the shipment. > **Note:** Some carriers only allow one package per shipment. If you attempt to create a """
    total_weight: Weigth
    """The combined weight of all packages in the shipment"""
    rate_response: RatesInformation
    """The rates response"""
    carrier_id: Optional[str] = None
    """The carrier account that is billed for the shipping charges"""
    service_code: Optional[str] = None
    """The [carrier service] used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, e"""
    requested_shipment_service: Optional[str] = None
    """The requested shipment service"""
    shipping_rule_id: Optional[str] = None
    """ID of the shipping rule, which you want to use to automate carrier/carrier service selection for the shipment"""
    external_order_id: Optional[str] = None
    """ID that the Order Source assigned"""
    hold_until_date: Optional[datetime] = None
    """Date to hold the shipment until"""
    ship_by_date: Optional[datetime] = None
    """Date by which the shipment should be shipped"""
    retail_rate: Optional[MonetaryValue] = None
    """The retail rate for the shipment"""
    store_id: Optional[str] = None
    """The store ID associated with the shipment"""
    items: Optional[list[ShipmentItem]] = None
    """Describe the packages included in this shipment as related to potential metadata that was imported from external order s"""
    notes_from_buyer: Optional[str] = None
    """Notes from the buyer"""
    notes_for_gift: Optional[str] = None
    """Gift notes"""
    is_gift: Optional[bool] = None
    """Indicates if the shipment is a gift"""
    assigned_user: Optional[str] = None
    """User assigned to the shipment"""
    amount_paid: Optional[MonetaryValue] = None
    """Total amount paid for the order"""
    shipping_paid: Optional[MonetaryValue] = None
    """Amount paid for shipping"""
    tax_paid: Optional[MonetaryValue] = None
    """Amount paid for taxes"""
    zone: Optional[int] = None
    """Shipping zone"""
    display_scheme: Optional[str] = None
    """Display scheme for the shipment"""
    tax_identifiers: Optional[list[TaxIdentifier]] = None
    external_shipment_id: Optional[str] = None
    """A unique user-defined key to identify a shipment. This can be used to retrieve the shipment. > **Warning:** The `externa"""
    shipment_number: Optional[str] = None
    """A non-unique user-defined number used to identify a shipment. If undefined, this will match the external_shipment_id of """
    ship_to: Optional[ShippingAddressTo] = None
    """The recipient's mailing address"""
    ship_from: Optional[ShippingAddress] = None
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    order_source_code: Optional[OrderSourceName] = None
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""


class EstimateRatesRequestBody(BaseModel):
    """A rate estimate request body"""

    model_config = ConfigDict(populate_by_name=True)

    from_country_code: str
    from_postal_code: str
    from_city_locality: str
    """from postal code"""
    from_state_province: str
    """From state province"""
    to_country_code: str
    to_postal_code: str
    to_city_locality: str
    """The city locality the package is being shipped to"""
    to_state_province: str
    """To state province"""
    weight: Weigth
    """The weight of the package"""
    ship_date: datetime
    """ship date"""
    dimensions: Optional[Dimensions] = None
    """The dimensions of the package"""
    confirmation: Optional[DeliveryConfirmation] = None
    address_residential_indicator: Optional[AddressResidentialIndicator] = None


class GetRateByIdResponseBody(BaseModel):
    """A rate response body"""

    model_config = ConfigDict(populate_by_name=True)

    rate_id: str
    """A string that uniquely identifies the rate"""
    rate_type: RateType
    carrier_id: str
    """A string that uniquely identifies the carrier"""
    shipping_amount: MonetaryValue
    """The shipping amount. Should be added with confirmation_amount, insurance_amount and other_amount to calculate the total """
    insurance_amount: MonetaryValue
    """The insurance amount. Should be added with shipping_amount, confirmation_amount and other_amount to calculate the total """
    confirmation_amount: MonetaryValue
    """The confirmation amount. Should be added with shipping_amount, insurance_amount and other_amount to calculate the total """
    other_amount: MonetaryValue
    """Any other charges associated with this rate. Should be added with shipping_amount, insurance_amount and confirmation_amo"""
    zone: int
    """Certain carriers base their rates off of custom zones that vary depending upon the ship_to and ship_from location"""
    package_type: str
    """package type that this rate was estimated for"""
    guaranteed_service: bool
    """Indicates if the rate is guaranteed."""
    negotiated_rate: bool
    """Indicates if the rates been negotiated"""
    service_type: str
    """service type"""
    service_code: str
    """service code for the rate"""
    trackable: bool
    """Indicates if rate is trackable"""
    carrier_code: str
    """carrier code"""
    carrier_nickname: str
    """carrier nickname"""
    carrier_friendly_name: str
    """carrier friendly name"""
    validation_status: ValidationStatus
    warning_messages: list[str]
    """The warning messages"""
    error_messages: list[str]
    """The error messages"""
    requested_comparison_amount: Optional[MonetaryValue] = None
    """The total shipping cost for the specified comparison_rate_type."""
    tax_amount: Optional[MonetaryValue] = None
    """Tariff and additional taxes associated with an international shipment."""
    delivery_days: Optional[int] = None
    """The number of days estimated for delivery, this will show the _actual_ delivery time if for example, the package gets sh"""
    estimated_delivery_date: Optional[str] = None
    carrier_delivery_days: Optional[str] = None
    """The carrier delivery days"""
    ship_date: Optional[datetime] = None
    """ship date"""
