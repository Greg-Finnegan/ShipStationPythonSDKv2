"""ShipStation shipments models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ._common import (
    AddressValidationResult,
    AdvancedShipmentOptions,
    Error,
    InternationalShipmentOptions,
    MonetaryValue,
    Package,
    PaginationLink,
    Rate,
    Shipment,
    ShipmentItem,
    ShippingAddress,
    ShippingAddressTo,
    Tag,
    TaxIdentifier,
    Weigth,
)
from ..enums import (
    DeliveryConfirmation,
    InsuranceProvider,
    OrderSourceName,
    RateResponseStatus,
    ShipmentStatus,
    ValidateAddress,
)


class CreateShipmentRequest(BaseModel):
    """A single shipment creation request"""

    model_config = ConfigDict(populate_by_name=True)

    validate_address: Optional[ValidateAddress] = None
    """Address validation option"""
    external_shipment_id: Optional[str] = None
    """A unique user-defined key to identify a shipment. This can be used to retrieve the shipment."""
    carrier_id: Optional[str] = None
    """The carrier account that is billed for the shipping charges"""
    create_sales_order: Optional[bool] = None
    """Whether to create a sales order for this shipment"""
    store_id: Optional[str] = None
    """The store ID associated with the shipment"""
    notes_from_buyer: Optional[str] = None
    """Notes from the buyer"""
    notes_for_gift: Optional[str] = None
    """Gift notes"""
    is_gift: Optional[bool] = None
    """Indicates if the shipment is a gift"""
    zone: Optional[int] = None
    """Shipping zone"""
    display_scheme: Optional[str] = None
    """Display scheme for the shipment"""
    assigned_user: Optional[str] = None
    """User assigned to the shipment"""
    shipment_status: Optional[ShipmentStatus] = None
    """The status of the shipment"""
    amount_paid: Optional[MonetaryValue] = None
    """Total amount paid for the order"""
    shipping_paid: Optional[MonetaryValue] = None
    """Amount paid for shipping"""
    tax_paid: Optional[MonetaryValue] = None
    """Amount paid for taxes"""
    ship_to: Optional[ShippingAddressTo] = None
    """The recipient's mailing address"""
    ship_from: Optional[ShippingAddress] = None
    """The shipment's origin address"""
    items: Optional[list[ShipmentItem]] = None
    """Items included in this shipment"""
    packages: Optional[list[Package]] = None
    """The packages in the shipment"""


class CreateShipmentResponse(BaseModel):
    """A single shipment creation response"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    created_at: datetime
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: datetime
    """The date and time that the shipment was created or last modified."""
    shipment_status: ShipmentStatus
    """The current status of the shipment"""
    ship_to: ShippingAddressTo
    """The recipient's mailing address"""
    ship_from: ShippingAddress
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    return_to: ShippingAddress
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    confirmation: DeliveryConfirmation
    """The type of delivery confirmation that is required for this shipment"""
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
    ship_date: Optional[str] = None
    """The date that the shipment was (or will be) shippped. ShipStation will take the day of week into consideration. For exam"""
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    order_source_code: Optional[OrderSourceName] = None
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""
    errors: Optional[list[str]] = None
    """An array of errors that occurred while creating the shipment."""
    address_validation: Optional[AddressValidationResult] = None
    """The address validation result"""


class CreateShipmentsRequestBody(BaseModel):
    """A create shipments request body"""

    model_config = ConfigDict(populate_by_name=True)

    shipments: list[CreateShipmentRequest]
    """Array of shipments to create"""


class CreateShipmentsResponseBody(BaseModel):
    """A create shipments response body"""

    model_config = ConfigDict(populate_by_name=True)

    has_errors: bool
    """Indicates if any shipments had errors during creation"""
    shipments: list[CreateShipmentResponse]
    """Array of created shipments with their results"""


class GetShipmentByExternalIdResponseBody(BaseModel):
    """A get shipment by external id response body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    created_at: datetime
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: datetime
    """The date and time that the shipment was created or last modified."""
    shipment_status: ShipmentStatus
    """The current status of the shipment"""
    ship_to: ShippingAddressTo
    """The recipient's mailing address"""
    ship_from: ShippingAddress
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    return_to: ShippingAddress
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    confirmation: DeliveryConfirmation
    """The type of delivery confirmation that is required for this shipment"""
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
    ship_date: Optional[str] = None
    """The date that the shipment was (or will be) shippped. ShipStation will take the day of week into consideration. For exam"""
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    order_source_code: Optional[OrderSourceName] = None
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""


class GetShipmentByIdResponseBody(BaseModel):
    """A get shipment by id response body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    created_at: datetime
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: datetime
    """The date and time that the shipment was created or last modified."""
    shipment_status: ShipmentStatus
    """The current status of the shipment"""
    ship_to: ShippingAddressTo
    """The recipient's mailing address"""
    ship_from: ShippingAddress
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    return_to: ShippingAddress
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    confirmation: DeliveryConfirmation
    """The type of delivery confirmation that is required for this shipment"""
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
    ship_date: Optional[str] = None
    """The date that the shipment was (or will be) shippped. ShipStation will take the day of week into consideration. For exam"""
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    order_source_code: Optional[OrderSourceName] = None
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""


class ListShipmentRatesResponseBody(BaseModel):
    """A list shipment rates response body"""

    model_config = ConfigDict(populate_by_name=True)

    rates: list[Rate]
    """An array of shipment rates"""
    invalid_rates: list[Rate]
    """An array of invalid shipment rates"""
    rate_request_id: str
    """A string that uniquely identifies the rate request"""
    shipment_id: str
    """A string that uniquely identifies the shipment"""
    created_at: str
    """When the rate was created"""
    status: RateResponseStatus
    errors: list[Error]


class ListShipmentsResponseBody(BaseModel):
    """A list shipment response body"""

    model_config = ConfigDict(populate_by_name=True)

    shipments: list[Shipment]
    """The list of shipments returned by the api call"""
    total: int
    """Total number of shipments returned by the api call"""
    page: int
    pages: int
    links: PaginationLink


class TagShipmentResponseBody(BaseModel):
    """A shipment add tag response body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    tag: Tag
    """The tag that is now associated with this shipment"""
