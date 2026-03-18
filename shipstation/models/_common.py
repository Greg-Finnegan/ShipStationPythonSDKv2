"""ShipStation _common models — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from ..enums import (
    AddressResidentialIndicator,
    AddressValidationStatus,
    BillToParty,
    DeliveryConfirmation,
    DimensionUnit,
    DisplayScheme,
    ErrorCode,
    ErrorSource,
    ErrorType,
    IdentifierType,
    InsuranceProvider,
    LabelDownloadType,
    LabelFormat,
    LabelLayout,
    ManifestRequestStatus,
    NonDelivery,
    OrderSourceName,
    OriginType,
    PackageContents,
    RateType,
    RegulatedContentType,
    ShipmentStatus,
    TaxableEntityType,
    TermsOfTradeCode,
    TrackingStatusDetailCode,
    ValidateAddress,
    ValidationStatus,
    WebhookEvent,
    WeightUnit,
)


class AddToBatchRequestBody(BaseModel):
    """An add to batch request body"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_ids: Optional[list[str]] = None
    """The Shipment Ids to be modified on the batch"""
    rate_ids: Optional[list[str]] = None
    """Array of Rate IDs to be modifed on the batch"""


class Address(BaseModel):
    """
    Any residential or business mailing address, anywhere in the world. > **Note:** Either
    `name` or `company_name` must be set. Both may be specified, if relevant.
    """

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` """
    phone: str
    """The phone number of a contact person at this address. The format of this phone number varies depending on the country."""
    address_line1: str
    """The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 """
    city_locality: str
    """The name of the city or locality"""
    state_province: str
    """The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the"""
    postal_code: str
    country_code: str
    """The two-letter ISO 3166-1 country code"""
    address_residential_indicator: AddressResidentialIndicator
    """Indicates whether this is a residential address."""
    email: Optional[str] = None
    """Email for the address owner."""
    company_name: Optional[str] = None
    """If this is a business address, then the company name should be specified here."""
    address_line2: Optional[str] = None
    """The second line of the street address. For some addresses, this line may not be needed."""
    address_line3: Optional[str] = None
    """The third line of the street address. For some addresses, this line may not be needed."""


class ShippingAddress(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` """
    phone: str
    """The phone number of a contact person at this address. The format of this phone number varies depending on the country."""
    address_line1: str
    """The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 """
    city_locality: str
    """The name of the city or locality"""
    state_province: str
    """The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the"""
    postal_code: str
    country_code: str
    """The two-letter ISO 3166-1 country code"""
    address_residential_indicator: AddressResidentialIndicator
    """Indicates whether this is a residential address."""
    email: Optional[str] = None
    """Email for the address owner."""
    company_name: Optional[str] = None
    """If this is a business address, then the company name should be specified here."""
    address_line2: Optional[str] = None
    """The second line of the street address. For some addresses, this line may not be needed."""
    address_line3: Optional[str] = None
    """The third line of the street address. For some addresses, this line may not be needed."""
    instructions: Optional[str] = None
    """Additional text about how to handle the shipment at this address."""


class LabelMessages(BaseModel):
    """
    Custom messages to print on the shipping label for the package. These are typically used
    to print invoice numbers, product numbers, or other internal reference numbers. Not all
    carriers support label messages. The number of lines and the maximum length of each line
    also varies by carrier. |Carrier |Max lines |Max line length
    |-------------------|----------|-------------------- |USPS (Stamps.com) |3 |60 |FedEx |3
    |35 for the first line. 30 for additional lines. |UPS |2 |35 |OnTrac |2 |25
    """

    model_config = ConfigDict(populate_by_name=True)

    reference1: str
    """The first line of the custom label message. Some carriers may prefix this line with something like "REF", "Reference", '"""
    reference2: str
    """The second line of the custom label message. Some carriers may prefix this line with something like "INV", "Reference 2'"""
    reference3: str
    """The third line of the custom label message. Some carriers may prefix this line with something like "PO", "Reference 3", """


class Dimensions(BaseModel):
    """The dimensions of a package"""

    model_config = ConfigDict(populate_by_name=True)

    unit: DimensionUnit
    """Dimension unit"""
    length: float
    """The length of the package, in the specified unit"""
    width: float
    """The width of the package, in the specified unit"""
    height: float
    """The height of the package, in the specified unit"""


class MonetaryValue(BaseModel):
    """
    A monetary value, such as the price of a shipping label, the insured value of a package,
    or an account balance.
    """

    model_config = ConfigDict(populate_by_name=True)

    currency: str
    """Currency code"""
    amount: float
    """The monetary amount, in the specified currency."""


class Weight(BaseModel):
    """The weight of a package"""

    model_config = ConfigDict(populate_by_name=True)

    value: float
    """The weight, in the specified unit"""
    unit: WeightUnit
    """Weight unit"""


class Package(BaseModel):
    """A package associated with a shipment"""

    model_config = ConfigDict(populate_by_name=True)

    weight: Weight
    """The package weight"""
    shipment_package_id: Optional[str] = None
    """A string that uniquely identifies this shipment package"""
    package_id: Optional[str] = None
    """A string that uniquely identifies this [package type]"""
    package_code: Optional[str] = None
    """The [package type] such as `thick_envelope`, `small_flat_rate_box`, `large_package`, etc. The code `package` indicates a"""
    package_name: Optional[str] = None
    """The name of the of the [package type]"""
    dimensions: Optional[Dimensions] = None
    """The package dimensions"""
    insured_value: Optional[MonetaryValue] = None
    """The insured value of the package. Requires the `insurance_provider` field of the shipment to be set."""
    label_messages: Optional[LabelMessages] = None
    external_package_id: Optional[str] = None
    """An external package id."""
    tracking_number: Optional[str] = None
    """The tracking number for the package. The format depends on the carrier."""
    content_description: Optional[str] = None
    """A short description of the package content. Required for shipments moving to, from, and through Mexico."""
    products: Optional[list[dict[str, Any]]] = None
    """Details about products inside packages (Information provided would be used on custom documentation)"""


class ShippingAddressTo(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` """
    phone: str
    """The phone number of a contact person at this address. The format of this phone number varies depending on the country."""
    address_line1: str
    """The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 """
    city_locality: str
    """The name of the city or locality"""
    state_province: str
    """The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the"""
    postal_code: str
    country_code: str
    """The two-letter ISO 3166-1 country code"""
    address_residential_indicator: AddressResidentialIndicator
    """Indicates whether this is a residential address."""
    email: Optional[str] = None
    """Email for the address owner."""
    company_name: Optional[str] = None
    """If this is a business address, then the company name should be specified here."""
    address_line2: Optional[str] = None
    """The second line of the street address. For some addresses, this line may not be needed."""
    address_line3: Optional[str] = None
    """The third line of the street address. For some addresses, this line may not be needed."""
    instructions: Optional[str] = None
    """Additional text about how to handle the shipment at this address."""
    geolocation: Optional[list[dict[str, Any]]] = None


class Weigth(BaseModel):
    """The weight of a package"""

    model_config = ConfigDict(populate_by_name=True)

    value: float
    """The weight, in the specified unit"""
    unit: WeightUnit
    """Weight unit"""


class ShipmentItem(BaseModel):
    """A shipment item"""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    """item name"""
    sales_order_id: Optional[str] = None
    """sales order id"""
    sales_order_item_id: Optional[str] = None
    """sales order item id"""
    quantity: Optional[int] = None
    """The quantity of this item included in the shipment"""
    sku: Optional[str] = None
    """Item Stock Keeping Unit"""
    bundle_sku: Optional[str] = None
    """Bundle SKU for the item"""
    external_order_id: Optional[str] = None
    """external order id"""
    external_order_item_id: Optional[str] = None
    """external order item id"""
    asin: Optional[str] = None
    """Amazon Standard Identification Number"""
    order_source_code: Optional[OrderSourceName] = None
    item_id: Optional[str] = None
    """Unique identifier for the item"""
    allocation_status: Optional[str] = None
    """Allocation status of the item"""
    image_url: Optional[str] = None
    """URL to the item image"""
    weight: Optional[Weight] = None
    """Weight of the individual item"""
    unit_price: Optional[float] = None
    """Unit price of the item"""
    tax_amount: Optional[float] = None
    """Tax amount for the item"""
    shipping_amount: Optional[float] = None
    """Shipping amount for the item"""
    inventory_location: Optional[str] = None
    """Inventory location of the item"""
    options: Optional[list[dict[str, Any]]] = None
    """Item options/variants"""
    product_id: Optional[str] = None
    """Product ID"""
    fullfilment_sku: Optional[str] = None
    """Fulfillment SKU"""
    upc: Optional[str] = None
    """Universal Product Code"""


class ImporterOfRecords(BaseModel):
    """importer of records address, anywhere in the world."""

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The name of a contact person at this address. Either `name` or the `company_name` field should always be set."""
    address_line1: str
    """The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 """
    city_locality: str
    """The name of the city or locality"""
    postal_code: str
    country_code: str
    """The two-letter ISO 3166-1 country code"""
    phone: Optional[str] = None
    """The phone number of a contact person at this address. The format of this phone number varies depending on the country."""
    email: Optional[str] = None
    """Email for the address owner."""
    company_name: Optional[str] = None
    """If this is a business address, then the company name should be specified here. Either `name` or the `company_name` field"""
    address_line2: Optional[str] = None
    """The second line of the street address. For some addresses, this line may not be needed."""
    address_line3: Optional[str] = None
    """The third line of the street address. For some addresses, this line may not be needed."""
    state_province: Optional[str] = None
    """The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the"""


class EstimatedImportCharges(BaseModel):
    """Estimated import charges for commercial invoices for international shipments."""

    model_config = ConfigDict(populate_by_name=True)

    taxes: Optional[MonetaryValue] = None
    """Estimated import taxes."""
    duties: Optional[MonetaryValue] = None
    """Estimated import duties."""


class InvoiceAdditionalDetails(BaseModel):
    """The additional information to put on commercial invoice"""

    model_config = ConfigDict(populate_by_name=True)

    freight_charge: Optional[MonetaryValue] = None
    """Freight Charge for shipment."""
    insurance_charge: Optional[MonetaryValue] = None
    """Insurance Charge for shipment."""
    discount: Optional[MonetaryValue] = None
    """Discount for shipment."""
    estimated_import_charges: Optional[EstimatedImportCharges] = None
    """Estimated import charges for commercial invoices for international shipments."""
    other_charge: Optional[MonetaryValue] = None
    """Other charge for shipment."""
    other_charge_description: Optional[str] = None
    """Description for the other charge (if provided)."""


class InternationalShipmentOptions(BaseModel):
    """Options for international shipments, such as customs declarations."""

    model_config = ConfigDict(populate_by_name=True)

    contents: PackageContents
    """The type of contents in this shipment. This may impact import duties or customs treatment."""
    non_delivery: NonDelivery
    """Indicates what to do if a package is unable to be delivered."""
    contents_explanation: Optional[str] = None
    """Explanation for contents (required if the `contents` is provided as `other`)"""
    terms_of_trade_code: Optional[TermsOfTradeCode] = None
    """Specifies the supported terms of trade code (incoterms)"""
    declaration: Optional[str] = None
    """Declaration statement to be placed on the commercial invoice"""
    invoice_additional_details: Optional[InvoiceAdditionalDetails] = None
    importer_of_record: Optional[ImporterOfRecords] = None
    customs_items: Optional[list[dict[str, Any]]] = None
    """Customs declarations for each item in the shipment. (Please provide this information under `products` inside `packages`)"""


class AdvancedShipmentOptions(BaseModel):
    """Advanced shipment options"""

    model_config = ConfigDict(populate_by_name=True)

    bill_to_account: Optional[str] = None
    """This field is used to [bill shipping costs to a third party]. This field must be used in conjunction with the `bill_to_c"""
    bill_to_country_code: Optional[str] = None
    """The two-letter ISO 3166-1 country code of the third-party that is responsible for shipping costs."""
    bill_to_party: Optional[BillToParty] = None
    """Indicates whether to bill shipping costs to the recipient or to a third-party. When billing to a third-party, the `bill_"""
    bill_to_postal_code: Optional[str] = None
    """The postal code of the third-party that is responsible for shipping costs."""
    contains_alcohol: Optional[bool] = None
    """Indicates that the shipment contains alcohol."""
    delivered_duty_paid: Optional[bool] = None
    """Indicates that the shipper is paying the international delivery duties for this shipment. This option is supported by UP"""
    dry_ice: Optional[bool] = None
    """Indicates if the shipment contain dry ice"""
    dry_ice_weight: Optional[Weight] = None
    """The weight of the dry ice in the shipment"""
    non_machinable: Optional[bool] = None
    """Indicates that the package cannot be processed automatically because it is too large or irregularly shaped. This is prim"""
    saturday_delivery: Optional[bool] = None
    """Enables Saturday delivery, if supported by the carrier."""
    fedex_freight: Optional[dict[str, Any]] = None
    """Provide details for the Fedex freight service"""
    use_ups_ground_freight_pricing: Optional[bool] = None
    """Whether to use [UPS Ground Freight pricing] If enabled, then a `freight_class` must also be specified."""
    freight_class: Optional[str] = None
    """The National Motor Freight Traffic Association freight class, such as "77.5", "110", or "250"."""
    custom_field1: Optional[str] = None
    """An arbitrary field that can be used to store information about the shipment."""
    custom_field2: Optional[str] = None
    """An arbitrary field that can be used to store information about the shipment."""
    custom_field3: Optional[str] = None
    """An arbitrary field that can be used to store information about the shipment."""
    origin_type: Optional[OriginType] = None
    additional_handling: Optional[bool] = None
    """Indicate to the carrier that this shipment requires additional handling."""
    shipper_release: Optional[bool] = None
    collect_on_delivery: Optional[dict[str, Any]] = None
    """Defer payment until package is delivered, instead of when it is ordered."""
    third_party_consignee: Optional[bool] = None
    """Third Party Consignee option is a value-added service that allows the shipper to supply goods without commercial invoice"""
    dangerous_goods: Optional[bool] = None
    """Indicates if the Dangerous goods are present in the shipment"""
    dangerous_goods_contact: Optional[dict[str, Any]] = None
    """Contact information for Dangerous goods"""
    windsor_framework_details: Optional[dict[str, Any]] = None
    """The Windsor framework is a new regulation in the UK that simplifies customs procedures for goods moved from the UK mainl"""
    ancillary_endorsements_option: Optional[str] = None
    """Ancillary endorsements option for the shipment"""
    return_pickup_attempts: Optional[int] = None
    """Number of return pickup attempts"""
    own_document_upload: Optional[bool] = None
    """Indicates if own document upload is enabled"""
    limited_quantity: Optional[bool] = None
    """Indicates if the shipment contains limited quantities"""
    event_notification: Optional[bool] = None
    """Indicates if event notifications are enabled"""
    delivery_as_addressed: Optional[bool] = None
    """Instructs the carrier to deliver the package only to the exact address provided"""
    return_after_first_attempt: Optional[bool] = None
    """Ensures the shipment is immediately flagged for return to the sender if the initial delivery attempt fails"""
    regulated_content_type: Optional[RegulatedContentType] = None
    """Indicates the category of goods in the shipment that is subject to special regulatory or compliance requirements"""


class Tag(BaseModel):
    """
    Tags are arbitrary strings that you can use to categorize shipments. For example, you
    may want to use tags to distinguish between domestic and international shipments, or
    between insured and uninsured shipments. Or maybe you want to create a tag for each of
    your customers so you can easily retrieve every shipment for a customer.
    """

    model_config = ConfigDict(populate_by_name=True)

    name: str
    """The tag name."""


class TaxIdentifier(BaseModel):
    """A tax identifier object"""

    model_config = ConfigDict(populate_by_name=True)

    taxable_entity_type: TaxableEntityType
    identifier_type: IdentifierType
    issuing_authority: str
    """The authority that issued this tax. This must be a valid 2 character ISO 3166 Alpha 2 country code."""
    value: str
    """The value of the identifier"""


class AddressValidatingShipment(BaseModel):
    """An address validating shipment"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: str
    """A string that uniquely identifies the shipment"""
    carrier_id: str
    """The carrier account that is billed for the shipping charges"""
    service_code: str
    """The [carrier service] used to ship the package, such as `fedex_ground`, `usps_first_class_mail`, `flat_rate_envelope`, e"""
    ship_to: ShippingAddressTo
    """The recipient's mailing address"""
    ship_from: ShippingAddress
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    validate_address: Optional[ValidateAddress] = None
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
    created_at: Optional[datetime] = None
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: Optional[datetime] = None
    """The date and time that the shipment was created or last modified."""
    shipment_status: Optional[ShipmentStatus] = None
    """The current status of the shipment"""
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    return_to: Optional[ShippingAddress] = None
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    confirmation: Optional[DeliveryConfirmation] = None
    """The type of delivery confirmation that is required for this shipment"""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    advanced_options: Optional[AdvancedShipmentOptions] = None
    """Advanced shipment options. These are entirely optional."""
    insurance_provider: Optional[InsuranceProvider] = None
    """The insurance provider to use for any insured packages in the shipment."""
    tags: Optional[list[Tag]] = None
    """Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by """
    order_source_code: Optional[OrderSourceName] = None
    packages: Optional[list[Package]] = None
    """The packages in the shipment. > **Note:** Some carriers only allow one package per shipment. If you attempt to create a """
    total_weight: Optional[Weigth] = None
    """The combined weight of all packages in the shipment"""
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""


class AddressValidationResult(BaseModel):
    """An address validation result"""

    model_config = ConfigDict(populate_by_name=True)

    status: AddressValidationStatus
    original_address: Address
    """The original address that was sent for validation"""
    matched_address: Address
    """The matched address found by the ShipStation API"""
    messages: list[dict[str, Any]]
    """The list of messages that were generated during the address validation request."""


class AlternativeIdentifier(BaseModel):
    """
    Additional information some carriers may provide by which to identify a given label in
    their system.
    """

    model_config = ConfigDict(populate_by_name=True)

    type_: Optional[str] = Field(default=None, alias="type")
    """The type of alternative_identifier that corresponds to the value."""
    value: Optional[str] = None
    """The value of the alternative_identifier."""


class CreateAndValidateShipment(BaseModel):
    """A create and validate shipment resource"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: Optional[str] = None
    """A string that uniquely identifies the shipment"""
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
    created_at: Optional[datetime] = None
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: Optional[datetime] = None
    """The date and time that the shipment was created or last modified."""
    shipment_status: Optional[ShipmentStatus] = None
    """The current status of the shipment"""
    ship_to: Optional[ShippingAddressTo] = None
    """The recipient's mailing address"""
    ship_from: Optional[ShippingAddress] = None
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    return_to: Optional[ShippingAddress] = None
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    confirmation: Optional[DeliveryConfirmation] = None
    """The type of delivery confirmation that is required for this shipment"""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    advanced_options: Optional[AdvancedShipmentOptions] = None
    """Advanced shipment options. These are entirely optional."""
    insurance_provider: Optional[InsuranceProvider] = None
    """The insurance provider to use for any insured packages in the shipment."""
    tags: Optional[list[Tag]] = None
    """Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by """
    order_source_code: Optional[OrderSourceName] = None
    packages: Optional[list[Package]] = None
    """The packages in the shipment. > **Note:** Some carriers only allow one package per shipment. If you attempt to create a """
    total_weight: Optional[Weigth] = None
    """The combined weight of all packages in the shipment"""
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""
    errors: Optional[list[str]] = None
    """An array of errors that occurred while creating shipment."""
    address_validation: Optional[AddressValidationResult] = None
    """The address validation"""


class DangerousGoods(BaseModel):
    """Dangerous goods attribute associated with the product"""

    model_config = ConfigDict(populate_by_name=True)

    id_number: Optional[str] = None
    """UN number to identify the dangerous goods."""
    shipping_name: Optional[str] = None
    """Trade description of the dangerous goods."""
    technical_name: Optional[str] = None
    """Recognized Technical or chemical name of dangerous goods."""
    product_class: Optional[str] = None
    """Dangerous goods product class based on regulation."""
    product_class_subsidiary: Optional[str] = None
    """A secondary of product class for substances presenting more than one particular hazard"""
    packaging_group: Optional[str] = None
    dangerous_amount: Optional[str] = None
    """This model represents the amount of the dangerous goods."""
    quantity: Optional[int] = None
    """Quantity of dangerous goods."""
    packaging_instruction: Optional[str] = None
    """The specific standardized packaging instructions from the relevant regulatory agency that have been applied to the parce"""
    packaging_instruction_section: Optional[str] = None
    packaging_type: Optional[str] = None
    """The type of exterior packaging used to contain the dangerous good."""
    transport_mean: Optional[str] = None
    transport_category: Optional[str] = None
    """Transport category assign to dangerous goods for the transport purpose."""
    regulation_authority: Optional[str] = None
    """Name of the regulatory authority."""
    regulation_level: Optional[str] = None
    radioactive: Optional[bool] = None
    """Indication if the substance is radioactive."""
    reportable_quantity: Optional[bool] = None
    """Indication if the substance needs to be reported to regulatory authority based on the quantity."""
    tunnel_code: Optional[str] = None
    """Defines which types of tunnels the shipment is allowed to go through"""
    additional_description: Optional[str] = None
    """Provider additonal description regarding the dangerous goods. This is used as a placed holder to provider additional con"""


class ManifestDownload(BaseModel):
    """Object containing the href link to download the manifest file"""

    model_config = ConfigDict(populate_by_name=True)

    href: Optional[str] = None
    """The URL of the linked resource, if any"""


class DeprecatedManifest(BaseModel):
    """Deprecated manifest resource"""

    model_config = ConfigDict(populate_by_name=True)

    manifest_id: Optional[str] = None
    """A string that uniquely identifies the manifest"""
    form_id: Optional[str] = None
    """A string that uniquely identifies the form"""
    created_at: Optional[datetime] = None
    """The date-time that the manifest was created"""
    ship_date: Optional[datetime] = None
    """The date-time that the manifests shipments will be picked up"""
    shipments: Optional[int] = None
    """The number of shipments that are included in this manifest"""
    warehouse_id: Optional[str] = None
    """A string that uniquely identifies the warehouse"""
    submission_id: Optional[str] = None
    """A string that uniquely identifies the submission"""
    carrier_id: Optional[str] = None
    """A string that uniquely identifies the carrier"""
    manifest_download: Optional[ManifestDownload] = None
    label_ids: Optional[list[str]] = None
    """An array of the label ids used in this manifest."""


class Error(BaseModel):
    """The error structure that gets returned with almost all failed API calls"""

    model_config = ConfigDict(populate_by_name=True)

    error_source: ErrorSource
    error_type: ErrorType
    error_code: ErrorCode
    message: str
    """An error message associated with the failed API call"""
    field_name: Optional[str] = None
    """The name of the field that caused the error (only present for validation errors)"""
    field_value: Optional[str] = None
    """The invalid value that was provided for the field (only present for validation errors)"""


class ErrorResponseBody(BaseModel):
    """An error response body"""

    model_config = ConfigDict(populate_by_name=True)

    request_id: str
    """A UUID that uniquely identifies the request id. This can be given to the support team to help debug non-trivial issues t"""
    errors: list[Error]
    """The errors associated with the failed API call"""


class ErrorWithLabelId(BaseModel):
    """The error structure that gets returned with almost all failed API calls"""

    model_config = ConfigDict(populate_by_name=True)

    error_source: ErrorSource
    error_type: ErrorType
    error_code: ErrorCode
    message: str
    """An error message associated with the failed API call"""
    label_id: Optional[str] = None
    """The label this error is associated with if it is specific to a individual label."""


class ErrorWithLabelIdResponseBody(BaseModel):
    """An error response body"""

    model_config = ConfigDict(populate_by_name=True)

    request_id: str
    """A UUID that uniquely identifies the request id. This can be given to the support team to help debug non-trivial issues t"""
    errors: list[ErrorWithLabelId]
    """The errors associated with the failed API call"""


class Fulfillment(BaseModel):
    """A fulfillment represents a completed shipment with tracking information"""

    model_config = ConfigDict(populate_by_name=True)

    fulfillment_id: Optional[str] = None
    """Unique identifier for the fulfillment"""
    shipment_id: Optional[str] = None
    """The associated shipment id"""
    shipment_number: Optional[str] = None
    """The shipment number (order number)"""
    user_id: Optional[str] = None
    """The user id that created this fulfillment"""
    tracking_number: Optional[str] = None
    """Tracking number for the shipment"""
    created_at: Optional[datetime] = None
    """Date and time when the fulfillment was created"""
    ship_date: Optional[datetime] = None
    """Date when the shipment was shipped"""
    voided_at: Optional[Optional[datetime]] = None
    """Date and time when the fulfillment was voided"""
    delivered_at: Optional[Optional[datetime]] = None
    """Date and time when the shipment was delivered"""
    fulfillment_carrier_friendly_name: Optional[str] = None
    """Friendly name of the carrier"""
    fulfillment_provider_id: Optional[Optional[str]] = None
    """Fulfillment provider ID"""
    fulfillment_provider_friendly_name: Optional[Optional[str]] = None
    """Friendly name of the fulfillment provider"""
    fulfillment_provider_code: Optional[Optional[str]] = None
    """Code of the fulfillment provider"""
    fulfillment_service_code: Optional[Optional[str]] = None
    """Service code used for fulfillment"""
    fulfillment_fee: Optional[dict[str, Any]] = None
    """Fee charged for the fulfillment"""
    void_requested: Optional[bool] = None
    """Whether a void has been requested for this fulfillment"""
    voided: Optional[bool] = None
    """Whether this fulfillment has been voided"""
    order_source_notified: Optional[bool] = None
    """Whether the order source has been notified"""
    notification_error_message: Optional[Optional[str]] = None
    """Error message if notification failed"""
    ship_to: Optional[dict[str, Any]] = None
    """Shipping address information"""


class LabelDownload(BaseModel):
    """Reference to the various downloadable file formats for the generated label"""

    model_config = ConfigDict(populate_by_name=True)

    href: Optional[str] = None
    """The URL of the linked resource, if any"""
    pdf: Optional[str] = None
    """The URL for the pdf generated label"""
    png: Optional[str] = None
    """The URL for the png generated label"""
    zpl: Optional[str] = None
    """The URL for the zpl generated label"""


class Link(BaseModel):
    """A link to a related resource"""

    model_config = ConfigDict(populate_by_name=True)

    href: str
    """The URL of the linked resource, if any"""
    type_: Optional[str] = Field(default=None, alias="type")
    """The type of resource, or the type of relationship to the parent resource"""


class Manifest(BaseModel):
    """
    Used for combining packages into one scannable form that a carrier can use when picking
    up a large number of shipments
    """

    model_config = ConfigDict(populate_by_name=True)

    manifest_id: Optional[str] = None
    """A string that uniquely identifies the manifest"""
    form_id: Optional[str] = None
    """A string that uniquely identifies the form"""
    created_at: Optional[datetime] = None
    """The date-time that the manifest was created"""
    ship_date: Optional[datetime] = None
    """The date-time that the manifests shipments will be picked up"""
    shipments: Optional[int] = None
    """The number of shipments that are included in this manifest"""
    label_ids: Optional[list[str]] = None
    """An array of the label ids used in this manifest."""
    warehouse_id: Optional[str] = None
    """A string that uniquely identifies the warehouse"""
    submission_id: Optional[str] = None
    """A string that uniquely identifies the submission"""
    carrier_id: Optional[str] = None
    """A string that uniquely identifies the carrier"""
    manifest_download: Optional[ManifestDownload] = None


class ManifestRequests(BaseModel):
    """A reference to the manifest request"""

    model_config = ConfigDict(populate_by_name=True)

    manifest_request_id: Optional[str] = None
    """A string that uniquely identifies a manifest request"""
    status: Optional[ManifestRequestStatus] = None


class Manifests(BaseModel):
    """An array of manifest resources"""

    model_config = ConfigDict(populate_by_name=True)

    manifests: Optional[list[Manifest]] = None
    """Resulting Manifests"""


class ModifyBatch(BaseModel):
    """A modify batch object"""

    model_config = ConfigDict(populate_by_name=True)

    shipment_ids: Optional[list[str]] = None
    """The Shipment Ids to be modified on the batch"""
    rate_ids: Optional[list[str]] = None
    """Array of Rate IDs to be modifed on the batch"""


class OptionalLink(BaseModel):
    """A link to a related resource, or an empty object if there is no resource to link to"""

    model_config = ConfigDict(populate_by_name=True)

    href: Optional[str] = None
    """The URL of the linked resource, if any"""
    type_: Optional[str] = Field(default=None, alias="type")
    """The type of resource, or the type of relationship to the parent resource"""


class PackageType(BaseModel):
    """A package type that a carrier supports for shipment."""

    model_config = ConfigDict(populate_by_name=True)

    package_code: str
    name: str
    package_id: Optional[str] = None
    """A string that uniquely identifies the package."""
    dimensions: Optional[Dimensions] = None
    """The custom dimensions for the package."""
    description: Optional[str] = None
    """Provides a helpful description for the custom package."""


class PaginationLink(BaseModel):
    """Helpful links to other pages of results"""

    model_config = ConfigDict(populate_by_name=True)

    first: Link
    """The link to the first page of results. This object will _always_ have an `href` field. If there are no results, then the"""
    last: Link
    """The link to the final page of results. This object will _always_ have an `href` field. If there are no results, then the"""
    prev: OptionalLink
    """The link to the previous page of results. The `href` field will only be set when the `page` is 2 or greater."""
    next: OptionalLink
    """The link to the next page of results. The `href` field will only be set when the `page` is less than `pages`."""


class PagedListResponseBody(BaseModel):
    """
    Many ShipStation endpoints return a paged list of items. In addition to the returned
    items, these responses also include information about the total number of items, the
    number of pages of results, and URLs of other pages of results.
    """

    model_config = ConfigDict(populate_by_name=True)

    total: int
    """The total number of items across all pages of results"""
    page: int
    """The current page number of results. For example, if there are 80 results, and the page size is 25, then `page` could be """
    pages: int
    """The total number of pages of results. For example, if there are 80 results, and the page size is 25, then `pages` would """
    links: PaginationLink


class PaperlessDownload(BaseModel):
    """
    The paperless details which may contain elements like `href`, `instructions` and
    `handoff_code`.
    """

    model_config = ConfigDict(populate_by_name=True)

    href: Optional[str] = None
    """The URL of the linked resource, if any"""
    instructions: Optional[str] = None
    """The instructions for the paperless download."""
    handoff_code: Optional[str] = None
    """The handoff code for the paperless download."""


class PartialAddress(BaseModel):
    """A complete or partial mailing address."""

    model_config = ConfigDict(populate_by_name=True)

    name: Optional[str] = None
    """The name of a contact person at this address. This field may be set instead of - or in addition to - the `company_name` """
    phone: Optional[str] = None
    """The phone number of a contact person at this address. The format of this phone number varies depending on the country."""
    email: Optional[str] = None
    """Email for the address owner."""
    company_name: Optional[str] = None
    """If this is a business address, then the company name should be specified here."""
    address_line1: Optional[str] = None
    """The first line of the street address. For some addresses, this may be the only line. Other addresses may require 2 or 3 """
    address_line2: Optional[str] = None
    """The second line of the street address. For some addresses, this line may not be needed."""
    address_line3: Optional[str] = None
    """The third line of the street address. For some addresses, this line may not be needed."""
    city_locality: Optional[str] = None
    """The name of the city or locality"""
    state_province: Optional[str] = None
    """The state or province. For some countries (including the U.S.) only abbreviations are allowed. Other countries allow the"""
    postal_code: Optional[str] = None
    country_code: Optional[str] = None
    """The two-letter ISO 3166-1 country code"""
    address_residential_indicator: Optional[AddressResidentialIndicator] = None
    """Indicates whether this is a residential address."""


class PartialShipment(BaseModel):
    """
    The information necessary to ship a package, such as the origin, the destination, the
    carrier service, and the package dimensions and weight.
    """

    model_config = ConfigDict(populate_by_name=True)

    shipment_id: Optional[str] = None
    """A string that uniquely identifies the shipment"""
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
    created_at: Optional[datetime] = None
    """The date and time that the shipment was created in ShipStation ."""
    modified_at: Optional[datetime] = None
    """The date and time that the shipment was created or last modified."""
    shipment_status: Optional[ShipmentStatus] = None
    """The current status of the shipment"""
    ship_to: Optional[ShippingAddressTo] = None
    """The recipient's mailing address"""
    ship_from: Optional[ShippingAddress] = None
    """The shipment's origin address. If you frequently ship from the same location, consider [creating a warehouse]. Then you """
    warehouse_id: Optional[str] = None
    """The [warehouse] that the shipment is being shipped from. Either `warehouse_id` or `ship_from` must be specified."""
    return_to: Optional[ShippingAddress] = None
    """The return address for this shipment. Defaults to the `ship_from` address. Can be sent with a warehouse_id, in which cas"""
    is_return: Optional[bool] = None
    """An optional indicator if the shipment is intended to be a return. Defaults to false if not provided."""
    confirmation: Optional[DeliveryConfirmation] = None
    """The type of delivery confirmation that is required for this shipment"""
    customs: Optional[InternationalShipmentOptions] = None
    """Customs information. This is usually only needed for international shipments."""
    advanced_options: Optional[AdvancedShipmentOptions] = None
    """Advanced shipment options. These are entirely optional."""
    insurance_provider: Optional[InsuranceProvider] = None
    """The insurance provider to use for any insured packages in the shipment."""
    tags: Optional[list[Tag]] = None
    """Arbitrary tags associated with this shipment. Tags can be used to categorize shipments, and shipments can be queried by """
    order_source_code: Optional[OrderSourceName] = None
    packages: Optional[list[Package]] = None
    """The packages in the shipment. > **Note:** Some carriers only allow one package per shipment. If you attempt to create a """
    total_weight: Optional[Weigth] = None
    """The combined weight of all packages in the shipment"""
    comparison_rate_type: Optional[str] = None
    """Calculate a rate for this shipment with the requested carrier using a ratecard that differs from the default. Only suppo"""


class PartialShippingAddress(BaseModel):
    """A complete or partial mailing address."""

    model_config = ConfigDict(populate_by_name=True)

    instructions: Optional[str] = None
    """Additional text about how to handle the shipment at this address."""


class PartialShippingAddressTo(BaseModel):
    """A complete or partial mailing address."""

    model_config = ConfigDict(populate_by_name=True)

    instructions: Optional[str] = None
    """Additional text about how to handle the shipment at this address."""
    geolocation: Optional[list[dict[str, Any]]] = None


class PurchaseLabelWithoutShipment(BaseModel):
    """A purchase label without shipment resource"""

    model_config = ConfigDict(populate_by_name=True)

    validate_address: Optional[ValidateAddress] = None
    label_layout: Optional[LabelLayout] = None
    label_format: Optional[LabelFormat] = None
    label_download_type: Optional[LabelDownloadType] = None
    display_scheme: Optional[DisplayScheme] = None
    """The display format that the label should be shown in."""


class Rate(BaseModel):
    """A rate"""

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


class RateEstimate(BaseModel):
    """A rate estimate"""

    model_config = ConfigDict(populate_by_name=True)

    rate_type: RateType
    carrier_id: str
    """A string that uniquely identifies the carrier"""
    shipping_amount: MonetaryValue
    """The shipping amount"""
    insurance_amount: MonetaryValue
    """The insurance amount"""
    confirmation_amount: MonetaryValue
    """The confirmation amount"""
    other_amount: MonetaryValue
    """Any other charges associated with this rate"""
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
    """A [shipping carrier] , such as `fedex`, `dhl_express`, `stamps_com`, etc."""
    carrier_nickname: str
    """carrier nickname"""
    carrier_friendly_name: str
    """carrier friendly name"""
    validation_status: ValidationStatus
    warning_messages: list[str]
    """The warning messages"""
    error_messages: list[str]
    """The error messages"""
    tax_amount: Optional[MonetaryValue] = None
    """Tariff and additional taxes associated with an international shipment."""
    delivery_days: Optional[int] = None
    """The number of days estimated for delivery, this will show the _actual_ delivery time if for example, the package gets sh"""
    estimated_delivery_date: Optional[str] = None
    carrier_delivery_days: Optional[str] = None
    """The carrier delivery days"""
    ship_date: Optional[datetime] = None
    """ship date"""


class Shipment(BaseModel):
    """
    The information necessary to ship a package, such as the origin, the destination, the
    carrier service, and the package dimensions and weight. > **Note:** Either `ship_from`
    or `warehouse_id` must be set.
    """

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


class ToteQuantityResponse(BaseModel):
    """Tote quantity grouped by warehouse"""

    model_config = ConfigDict(populate_by_name=True)

    inventory_warehouse_id: str
    """The warehouse ID"""
    quantity: int
    """Number of totes in this warehouse"""


class TrackingInformation(BaseModel):
    """A tracking information resource"""

    model_config = ConfigDict(populate_by_name=True)

    tracking_number: Optional[str] = None
    tracking_url: Optional[str] = None
    """Carrier Tracking Url, if available"""
    status_code: Optional[TrackingStatusDetailCode] = None
    status_detail_code: Optional[TrackingStatusDetailCode] = None
    carrier_code: Optional[str] = None
    carrier_id: Optional[int] = None
    """The unique ID of the [carrier account] that was used to create this label"""
    status_description: Optional[str] = None
    """Status description"""
    status_detail_description: Optional[str] = None
    """Status detail description"""
    carrier_status_code: Optional[str] = None
    """Carrier status code"""
    carrier_detail_code: Optional[str] = None
    """Carrier detail code"""
    carrier_status_description: Optional[str] = None
    """carrier status description"""
    ship_date: Optional[datetime] = None
    estimated_delivery_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    exception_description: Optional[str] = None
    """Exception description"""
    events: Optional[list[dict[str, Any]]] = None
    """The events that have occured during the lifetime of this tracking number."""


class WebhookHeader(BaseModel):
    """Optional header to be specified in webhook"""

    model_config = ConfigDict(populate_by_name=True)

    key: str
    """Key/name of a header"""
    value: str
    """Value of a header"""


class Webhook(BaseModel):
    """A webhook"""

    model_config = ConfigDict(populate_by_name=True)

    webhook_id: Optional[str] = None
    """A string that uniquely identifies the webhook"""
    url: Optional[str] = None
    """The url that the webhook sends the request to"""
    event: Optional[WebhookEvent] = None
    headers: Optional[list[WebhookHeader]] = None
    """Array of custom webhook headers"""
    name: Optional[str] = None
    """The name of the webhook"""
    store_id: Optional[int] = None
    """Store ID"""
