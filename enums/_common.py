"""ShipStation _common enums — auto-generated, do not edit."""

from __future__ import annotations

from enum import StrEnum


class AddressResidentialIndicator(StrEnum):
    """Indicates whether an address is residential."""

    UNKNOWN = "unknown"
    YES = "yes"
    NO = "no"


class AddressValidationCode(StrEnum):
    """The error codes that can be returned by the address validation API"""

    A1000 = "a1000"
    A1001 = "a1001"
    A1002 = "a1002"
    A1003 = "a1003"
    A1004 = "a1004"
    A1005 = "a1005"
    A1006 = "a1006"
    A1007 = "a1007"
    A1008 = "a1008"
    R1000 = "r1000"
    R1001 = "r1001"
    R1002 = "r1002"
    R1003 = "r1003"


class AddressValidationDetailCode(StrEnum):
    """The detailed error codes that can be returned by the address validation API"""

    UNSUPPORTED_COUNTRY = "unsupported_country"
    NON_SUPPORTED_COUNTRY = "non_supported_country"
    MINIMUM_POSTAL_CODE_VERIFICATION_FAILED = "minimum_postal_code_verification_failed"
    STREET_DOES_NOT_MATCH_UNIQUE_STREET_NAME = "street_does_not_match_unique_street_name"
    MULTIPLE_DIRECTIONALS = "multiple_directionals"
    MULTIPLE_MATCHES = "multiple_matches"
    SUITE_NOT_VALID = "suite_not_valid"
    SUITE_MISSING = "suite_missing"
    INCOMPATIBLE_PAIRED_LABELS = "incompatible_paired_labels"
    INVALID_HOUSE_NUMBER = "invalid_house_number"
    MISSING_HOUSE_NUMBER = "missing_house_number"
    INVALID_BOX_NUMBER = "invalid_box_number"
    INVALID_CHARGE_EVENT = "invalid_charge_event"
    MISSING_BOX_NUMBER = "missing_box_number"
    MISSING_CMRA_OR_PRIVATE_MAIL_BOX_NUMBER = "missing_cmra_or_private_mail_box_number"
    SUITE_HAS_NO_SECONDARIES = "suite_has_no_secondaries"
    POSTAL_CODE_CHANGED_OR_ADDED = "postal_code_changed_or_added"
    STATE_PROVINCE_CHANGED_OR_ADDED = "state_province_changed_or_added"
    CITY_LOCALITY_CHANGED_OR_ADDED = "city_locality_changed_or_added"
    URBANIZATION_CHANGED = "urbanization_changed"
    STREET_NAME_SPELLING_CHANGED_OR_ADDED = "street_name_spelling_changed_or_added"
    STREET_NAME_TYPE_CHANGED_OR_ADDED = "street_name_type_changed_or_added"
    STREET_DIRECTION_CHANGED_OR_ADDED = "street_direction_changed_or_added"
    SUITE_TYPE_CHANGED_OR_ADDED = "suite_type_changed_or_added"
    SUITE_UNIT_NUMBER_CHANGED_OR_ADDED = "suite_unit_number_changed_or_added"
    DOUBLE_DEPENDENT_LOCALITY_CHANGED_OR_ADDED = "double_dependent_locality_changed_or_added"
    SUBADMINISTRATIVE_AREA_CHANGED_OR_ADDED = "subadministrative_area_changed_or_added"
    SUBNATIONAL_AREA_CHANGED_OR_ADDED = "subnational_area_changed_or_added"
    PO_BOX_CHANGED_OR_ADDED = "po_box_changed_or_added"
    PREMISE_TYPE_CHANGED_OR_ADDED = "premise_type_changed_or_added"
    HOUSE_NUMBER_CHANGED = "house_number_changed"
    ORGANIZATION_CHANGED_OR_ADDED = "organization_changed_or_added"
    PARTIALLY_VERIFIED_TO_STATE_LEVEL = "partially_verified_to_state_level"
    PARTIALLY_VERIFIED_TO_CITY_LEVEL = "partially_verified_to_city_level"
    PARTIALLY_VERIFIED_TO_STREET_LEVEL = "partially_verified_to_street_level"
    PARTIALLY_VERIFIED_TO_PREMISE_LEVEL = "partially_verified_to_premise_level"
    VERIFIED_TO_STATE_LEVEL = "verified_to_state_level"
    VERIFIED_TO_CITY_LEVEL = "verified_to_city_level"
    VERIFIED_TO_STREET_LEVEL = "verified_to_street_level"
    VERIFIED_TO_PREMISE_LEVEL = "verified_to_premise_level"
    VERIFIED_TO_SUITE_LEVEL = "verified_to_suite_level"
    CODED_TO_STREET_LAVEL = "coded_to_street_lavel"
    CODED_TO_NEIGHBORHOOD_LEVEL = "coded_to_neighborhood_level"
    CODED_TO_COMMUNITY_LEVEL = "coded_to_community_level"
    CODED_TO_STATE_LEVEL = "coded_to_state_level"
    CODED_TO_ROOFTOP_LEVEL = "coded_to_rooftop_level"
    CODED_TO_ROOFTOP_INTERPOLATION_LEVEL = "coded_to_rooftop_interpolation_level"
    NAME_MAX_LENGTH_EXCEEDED = "name_max_length_exceeded"
    PHONE_MAX_LENGTH_EXCEEDED = "phone_max_length_exceeded"
    COMPANY_NAME_MAX_LENGTH_EXCEEDED = "company_name_max_length_exceeded"
    LINE1_MIN_MAX_LENGTH = "line1_min_max_length"
    LINE2_MAX_LENGTH_EXCEEDED = "line2_max_length_exceeded"
    LINE3_MAX_LENGTH_EXCEEDED = "line3_max_length_exceeded"
    CITY_LOCALITY_MAX_LENGTH_EXCEEDED = "city_locality_max_length_exceeded"
    STATE_PROVINCE_MAX_LENGTH_EXCEEDED = "state_province_max_length_exceeded"
    INVALID_POSTAL_CODE = "invalid_postal_code"
    COUNTRY_INVALID_LENGTH = "country_invalid_length"
    ADDRESS_NOT_FOUND = "address_not_found"


class AddressValidationMessageType(StrEnum):
    """The different types of messages that can be returned by the address validation API"""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class AddressValidationStatus(StrEnum):
    """The possible address validation status values"""

    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    WARNING = "warning"
    ERROR = "error"


class BillToParty(StrEnum):
    """The possible bill to party values"""

    RECIPIENT = "recipient"
    THIRD_PARTY = "third_party"


class CollectOnDeliveryPaymentType(StrEnum):
    """Types of payment that are supported"""

    ANY = "any"
    CASH = "cash"
    CASH_EQUIVALENT = "cash_equivalent"
    NONE = "none"


class DeliveryConfirmation(StrEnum):
    """The possible delivery confirmation values"""

    NONE = "none"
    DELIVERY = "delivery"
    SIGNATURE = "signature"
    ADULT_SIGNATURE = "adult_signature"
    DIRECT_SIGNATURE = "direct_signature"
    DELIVERY_MAILED = "delivery_mailed"
    VERBAL_CONFIRMATION = "verbal_confirmation"
    DELIVERY_CODE = "delivery_code"
    AGE_VERIFICATION_16_PLUS = "age_verification_16_plus"


class DimensionUnit(StrEnum):
    """The dimension units that are supported by ShipStation ."""

    INCH = "inch"
    CENTIMETER = "centimeter"


class DisplayScheme(StrEnum):
    """The display format that the label should be shown in."""

    LABEL = "label"
    QR_CODE = "qr_code"
    LABEL_AND_QR_CODE = "label_and_qr_code"
    PAPERLESS = "paperless"
    LABEL_AND_PAPERLESS = "label_and_paperless"


class ErrorCode(StrEnum):
    """The error code specified for the failed API Call"""

    AUTO_FUND_NOT_SUPPORTED = "auto_fund_not_supported"
    BATCH_CANNOT_BE_MODIFIED = "batch_cannot_be_modified"
    CARRIER_CONFLICT = "carrier_conflict"
    CARRIER_DISCONNECTED = "carrier_disconnected"
    CARRIER_NOT_CONNECTED = "carrier_not_connected"
    CARRIER_NOT_SUPPORTED = "carrier_not_supported"
    CONFIRMATION_NOT_SUPPORTED = "confirmation_not_supported"
    DEFAULT_WAREHOUSE_CANNOT_BE_DELETED = "default_warehouse_cannot_be_deleted"
    FIELD_CONFLICT = "field_conflict"
    FIELD_VALUE_REQUIRED = "field_value_required"
    FORBIDDEN = "forbidden"
    IDENTIFIER_CONFLICT = "identifier_conflict"
    IDENTIFIERS_MUST_MATCH = "identifiers_must_match"
    INSUFFICIENT_FUNDS = "insufficient_funds"
    INVALID_ADDRESS = "invalid_address"
    INVALID_BILLING_PLAN = "invalid_billing_plan"
    INVALID_FIELD_VALUE = "invalid_field_value"
    INVALID_IDENTIFIER = "invalid_identifier"
    INVALID_STATUS = "invalid_status"
    INVALID_STRING_LENGTH = "invalid_string_length"
    LABEL_IMAGES_NOT_SUPPORTED = "label_images_not_supported"
    METER_FAILURE = "meter_failure"
    ORDER_SOURCE_NOT_ACTIVE = "order_source_not_active"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    REFRESH_NOT_SUPPORTED = "refresh_not_supported"
    REQUEST_BODY_REQUIRED = "request_body_required"
    RETURN_LABEL_NOT_SUPPORTED = "return_label_not_supported"
    SETTINGS_NOT_SUPPORTED = "settings_not_supported"
    SUBSCRIPTION_INACTIVE = "subscription_inactive"
    TERMS_NOT_ACCEPTED = "terms_not_accepted"
    TRACKING_NOT_SUPPORTED = "tracking_not_supported"
    TRIAL_EXPIRED = "trial_expired"
    UNAUTHORIZED = "unauthorized"
    UNKNOWN = "unknown"
    UNSPECIFIED = "unspecified"
    VERIFICATION_FAILURE = "verification_failure"
    WAREHOUSE_CONFLICT = "warehouse_conflict"
    WEBHOOK_EVENT_TYPE_CONFLICT = "webhook_event_type_conflict"
    CUSTOMS_ITEMS_REQUIRED = "customs_items_required"
    INCOMPATIBLE_PAIRED_LABELS = "incompatible_paired_labels"
    INVALID_CHARGE_EVENT = "invalid_charge_event"
    INVALID_OBJECT = "invalid_object"
    NO_RATES_RETURNED = "no_rates_returned"


class ErrorSource(StrEnum):
    """The source of the error, as indicated by the name this informs us if the API call failed because of the carrier, the order source, or the ShipStation API itself."""

    CARRIER = "carrier"
    ORDER_SOURCE = "order_source"
    SHIPSTATION = "ShipStation"


class ErrorType(StrEnum):
    """The type of error"""

    ACCOUNT_STATUS = "account_status"
    BUSINESS_RULES = "business_rules"
    VALIDATION = "validation"
    SECURITY = "security"
    SYSTEM = "system"
    INTEGRATIONS = "integrations"


class IdentifierType(StrEnum):
    """Tax identifier type for customs declaration |Pickup Type | Description |---------------|----------------------------------------- |`vat` | The tax identifier is a Value Added Tax. |`eori` | The tax identifier is an Economic Operators Registration and Identification Number (EORI). |`ssn` | The tax identifier is a Social Security Number. |`ein` | The tax identifier is an Employer Identification Number (EIN). |`tin` | The tax identifier is a Tax Identification Number (TIN). |`ioss` | The tax identifier is an Import One-Stop Shop (IOSS). |`pan` | The tax identifier is a Permanent Account Number (PAN). |`voec` | The tax identifier is a Norwegian VAT On E-Commerce(VOEC). |`pccc` | The tax identifier is a Personal Customs Clearance Code (PCCC). |`oss` | The tax identifier is an One-Stop Shop (OSS). |`passport` | The tax identifier is a Passport Number. |`abn` | The tax identifier is an Australian Business Number. |`ukims` | The tax identifier is an UK Internal Market Scheme number."""

    VAT = "vat"
    EORI = "eori"
    SSN = "ssn"
    EIN = "ein"
    TIN = "tin"
    IOSS = "ioss"
    PAN = "pan"
    VOEC = "voec"
    PCCC = "pccc"
    OSS = "oss"
    PASSPORT = "passport"
    ABN = "abn"
    UKIMS = "ukims"


class InsuranceProvider(StrEnum):
    """The possible insurance provider values"""

    NONE = "none"
    SHIPSURANCE = "shipsurance"
    CARRIER = "carrier"
    THIRD_PARTY = "third_party"


class LabelDownloadType(StrEnum):
    """There are two different ways to [download a label]: |Label Download Type | Description |--------------------|------------------------------ |`url` |You will receive a URL, which you can use to download the label in a separate request. The URL will remain valid for 90 days.<br><br>This is the default if `label_download_type` is unspecified. |`inline` |You will receive the Base64-encoded label as part of the response. No need for a second request to download the label."""

    URL = "url"
    INLINE = "inline"


class LabelFormat(StrEnum):
    """The possible file formats in which shipping labels can be downloaded. We recommend `pdf` format because it is supported by all carriers, whereas some carriers do not support the `png` or `zpl` formats. |Label Format | Supported Carriers |--------------|----------------------------------- |`pdf` | All carriers |`png` | `fedex` <br> `stamps_com` <br> `ups` <br> `usps` |`zpl` | `access_worldwide` <br> `apc` <br> `asendia` <br> `dhl_global_mail` <br> `dhl_express` <br> `dhl_express_australia` <br> `dhl_express_canada` <br> `dhl_express_worldwide` <br> `dhl_express_uk` <br> `dpd` <br> `endicia` <br> `fedex` <br> `fedex_uk` <br> `firstmile` <br> `imex` <br> `newgistics` <br> `ontrac` <br> `rr_donnelley` <br> `stamps_com` <br> `ups` <br> `usps`"""

    PDF = "pdf"
    PNG = "png"
    ZPL = "zpl"


class LabelLayout(StrEnum):
    """The available layouts (sizes) in which shipping labels can be downloaded. The label format determines which sizes are supported. `4x6` is supported for all label formats, whereas `letter` (8.5" x 11") is only supported for `pdf` format."""

    _4X6 = "4x6"
    LETTER = "letter"


class ManifestRequestStatus(StrEnum):
    """The possible statuses of a manifest request"""

    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class NonDelivery(StrEnum):
    """The possible non delivery values"""

    RETURN_TO_SENDER = "return_to_sender"
    TREAT_AS_ABANDONED = "treat_as_abandoned"


class OrderSourceName(StrEnum):
    """The order sources that are supported by ShipStation"""

    AMAZON_CA = "amazon_ca"
    AMAZON_US = "amazon_us"
    BRIGHTPEARL = "brightpearl"
    CHANNEL_ADVISOR = "channel_advisor"
    CRATEJOY = "cratejoy"
    EBAY = "ebay"
    ETSY = "etsy"
    JANE = "jane"
    GROUPON_GOODS = "groupon_goods"
    MAGENTO = "magento"
    PAYPAL = "paypal"
    SELLER_ACTIVE = "seller_active"
    SHOPIFY = "shopify"
    STITCH_LABS = "stitch_labs"
    SQUARESPACE = "squarespace"
    THREE_DCART = "three_dcart"
    TOPHATTER = "tophatter"
    WALMART = "walmart"
    WOO_COMMERCE = "woo_commerce"
    VOLUSION = "volusion"


class OriginType(StrEnum):
    """Indicates if the package will be picked up or dropped off by the carrier"""

    PICKUP = "pickup"
    DROP_OFF = "drop_off"


class PackageContents(StrEnum):
    """The possible package contents values"""

    MERCHANDISE = "merchandise"
    DOCUMENTS = "documents"
    GIFT = "gift"
    RETURNED_GOODS = "returned_goods"
    SAMPLE = "sample"
    OTHER = "other"


class RateResponseStatus(StrEnum):
    """The possible rate response status values"""

    WORKING = "working"
    COMPLETED = "completed"
    PARTIAL = "partial"
    ERROR = "error"


class RateType(StrEnum):
    """The possible rate type values"""

    CHECK = "check"
    SHIPMENT = "shipment"


class RegulatedContentType(StrEnum):
    """Indicates the category of goods in the shipment that is subject to special regulatory or compliance requirements"""

    DAY_OLD_POULTRY = "day_old_poultry"
    OTHER_LIVE_ANIMAL = "other_live_animal"


class ShipmentStatus(StrEnum):
    """The possible shipment status values"""

    PENDING = "pending"
    PROCESSING = "processing"
    LABEL_PURCHASED = "label_purchased"
    CANCELLED = "cancelled"


class SortDir(StrEnum):
    """Controls the sort order of queries |Value |Description |:---------|:----------------------------------------------------- |`asc` |Return results in ascending order |`desc` |Return results in descending order"""

    ASC = "asc"
    DESC = "desc"


class TaxableEntityType(StrEnum):
    """The taxable entity type for this tax item. Valid values include the following |Value |Description |:--------- |:----------------------------------------------------- |`shipper` | The shipper is responsible for this tax. |`recipient` | The recipient of the shipment is responsible for this tax. |`ior` | The importer of records is responsible for tax."""

    SHIPPER = "shipper"
    RECIPIENT = "recipient"
    IOR = "ior"


class TermsOfTradeCode(StrEnum):

    EXW = "exw"
    FCA = "fca"
    CPT = "cpt"
    CIP = "cip"
    DPU = "dpu"
    DAP = "dap"
    DDP = "ddp"
    FAS = "fas"
    FOB = "fob"
    CFR = "cfr"
    CIF = "cif"
    DDU = "ddu"
    DAF = "daf"
    DEQ = "deq"
    DES = "des"


class TrackingStatusDetailCode(StrEnum):
    """The tracking status detail codes |Value |Description |:--------- |:----------------------------------------------------- | `COLLECTION_FAILED` | Shipment pickup failed. The delivery company will try again soon. | `AWAITING_DESPATCH` | Your shipment is ready to go and is waiting for pickup. | `COLLECTION_REQUESTED` | Your shipment pickup has been scheduled. | `DESPATCHED` | Your shipment has been handed over to the carrier or dropped off at collection point. It will soon start its journey. | `ELEC_ADVICE_RECD_BY_CARRIER` | Your shipment is now in the carrier's system. | `NOT_YET_RECEIVED_BY_CARRIER` | The sender couldn't hand over your shipment. The delivery company will try to collect it again. | `COLLECTION_MADE` | Your shipment has been picked up by the carrier. | `ATTEMPTED_DELIVERY` | Delivery attempt failed. Please check the carrier's instructions for next steps. | `ATTEMPTED_DELIVERY_2ND` | Second delivery attempt failed. Please check the carrier's instructions for next steps. | `ATTEMPTED_DELIVERY_3RD` | Third delivery attempt failed. Please check the carrier's instructions for next steps. | `COD_AMOUNT_NOT_PAID` | Delivery failed due to unpaid cash on delivery. Please check carrier instructions. | `COD_AMOUNT_PAID` | Cash on delivery payment received. | `CUSTOMER_CARDED` | Delivery attempt failed. Please check for delivery instructions left by the carrier. | `CUSTOMER_IDENTIFICATION_FAILED` | There was a recipient identification issue. Please check carrier instructions. | `INVALID_METHOD_OF_PAYMENT` | Delivery failed due to incorrect payment. Please check carrier instructions. | `NO_ACCESS_TO_RECIPIENTS_ADDRESS` | Delivery couldn't be completed due to issues with accessing address. Please follow carrier instructions. | `OUT_FOR_DELIVERY` | Your shipment is out for delivery. | `DELIVERED` | Your shipment has been delivered. | `DELIVERED_DAMAGED` | Your shipment was delivered but arrived damaged. | `DELIVERED_IN_PART` | Part of your shipment has been delivered. Check for updates on the rest. | `DELIVERED_SPECIFIED_SAFE_PLACE` | Your shipment has been left in your designated safe place. | `DELIVERED_TO_ALTERNATIVE_DELIVERY_LOCATION` | Your shipment was delivered to an alternative location due to the delivery company being unable to deliver it to the specified address. Check carrier instructions for pickup details. | `DELIVERED_TO_NEIGHBOUR` | Your shipment was delivered to your neighbor. | `DELIVERED_TO_PO_BOX` | Your shipment was delivered to your PO Box. | `PARCEL_COLLECTED_FROM_PICKUP_POINT` | Your package has been picked up from the collection point. | `POST_TRANSIT_STATUS` | The carrier has added more information about your delivery. | `PROOF_OF_DELIVERY` | Delivery confirmed. | `CANCELLED` | Your shipment has been cancelled. | `CANCELLED_BEFORE_DESPATCH` | Your shipment was cancelled before pickup. Contact the sender if unexpected. | `CUSTOMER_MOVED` | Recipient not at address. Your shipment is being returned. | `HAZARDOUS_PROHIBITED` | Your parcel contained a prohibited item and is being returned. Contact the sender. | `NOT_COLLECTED_FROM_PICKUP_POINT` | Shipment not collected from the pickup point. Your parcel is being returned to the sender. | `NOT_DELIVERED` | Delivery attempts failed. Your parcel is being returned to the sender. | `NOT_DELIVERED_ADDRESSEE_DECEASED` | Delivery not possible due to recipient's passing. | `PARCEL_DAMAGED` | Your parcel was damaged and can't be delivered. It's being returned. Contact the sender. | `PARCEL_DISPOSED` | Shipment was disposed of. Contact the sender for details. | `PARCEL_LOST` | Your parcel is lost. Contact the sender for next steps. | `PARCEL_OUTSIDE_OF_SERVICE_CAPABILITY` | Shipment is too large/heavy for delivery. Being returned. Contact sender. | `REFUSED_BY_CUSTOMER` | Delivery refused. Shipment being returned. Contact the sender. | `RETURN_TO_SENDER` | Your shipment is being returned to the sender. Contact them for details. | `ADDRESS_QUERY` | There's an issue with your delivery address. This may cause a delay or return. Contact sender or carrier. | `CARRIER_DELAYS` | There's a delivery delay. We'll update you when there's more info. | `CUSTOMS_CLEARED` | Your shipment has passed customs clearance. | `CUSTOMS_PROCESSING` | Your shipment is going through customs. | `DELAYED_NOT_CARRIER` | Unexpected delivery delay. We'll update you soon. | `DELIVERY_ARRANGED_WITH_RECIPIENT` | Delivery arranged by recipient. | `HELD_BY_CARRIER` | Your shipment is on hold due to a carrier issue. We'll update you soon. | `HELD_BY_CARRIER_FOR_CLEARANCE_PRE_PROCESSING` | Your shipment is held by carrier due to customs issues. We'll update you. | `HELD_BY_CUSTOMS` | Your shipment is held in customs. We'll update you. | `HELD_BY_EXPORT_CUSTOMS` | Your shipment is held in export customs. We'll update you. | `HELD_BY_IMPORT_CUSTOMS` | Your shipment is held in import customs. We'll update you. | `HUB_SCAN_OUT` | Your shipment is at the main delivery depot. | `IN_TRANSIT` | Your shipment is on its way between depots. | `INCORRECT_DECLARATION` | Incorrect shipment dimensions. Delivery may be delayed or returned. We'll update you. | `INFORMATION` | The carrier has shared additional shipment information. | `MISSORTED` | Your shipment was missorted. There might be a delivery delay. We'll update you. | `PARCEL_OVER_LABELLED` | Your shipment was over labelled by the delivery company to improve processing. | `PARCEL_REPACKED` | Your shipment packaging was damaged. It's being repacked. This might delay delivery. | `PARCEL_UPDATE_NOTIFICATION_VIA_EMAIL` | You've received an email with a shipment update. | `PARCEL_UPDATE_NOTIFICATION_VIA_SMS` | You've received a text message with a shipment update. | `RECEIVED_BY_CARRIER` | Your shipment has been received by the carrier. | `RECEIVED_LOCAL_DELIVERY_DEPOT` | Your shipment is at the local delivery depot, ready for delivery. | `ROUTING_ERROR` | Your shipment was sent to the wrong place. There might be a delay. | `SUB_CONTRACTOR_EVENT` | Your shipment is with the local delivery partner. | `SUB_CONTRACTOR_RECEIVED` | Your shipment has been received by the local delivery partner. | `RECD_BY_CARRIER_NO_ELEC_ADVICE` | There's a system issue with your shipment. Tracking updates might be delayed. | `AWAITING_ELECTRONIC_ADVICE` | Your tracking number is ready. Your shipment is waiting to be registered in the carrier system and scheduled for pickup. | `AWAITING_COLLECTION_FROM_PICKUP_POINT` | Your shipment is ready for pickup at the specified location. | `COLLECT_AT_LOCAL_PO` | Your shipment has been redirected to the local post office for pickup. Check carrier instructions. | `CUSTOMER_TO_COLLECT_FROM_CARRIER` | Your shipment is being held for pickup. Check carrier instructions. | `DELIVERED_TO_LOCKER_COLLECTION_POINT` | Your shipment has been delivered to your locker. | `CARRIER_STATUS_NOT_MAPPED` | Status not mapped. Please check the carrier's website for updates."""

    COLLECTION_FAILED = "COLLECTION_FAILED"
    AWAITING_DESPATCH = "AWAITING_DESPATCH"
    COLLECTION_REQUESTED = "COLLECTION_REQUESTED"
    DESPATCHED = "DESPATCHED"
    ELEC_ADVICE_RECD_BY_CARRIER = "ELEC_ADVICE_RECD_BY_CARRIER"
    NOT_YET_RECEIVED_BY_CARRIER = "NOT_YET_RECEIVED_BY_CARRIER"
    COLLECTION_MADE = "COLLECTION_MADE"
    ATTEMPTED_DELIVERY = "ATTEMPTED_DELIVERY"
    ATTEMPTED_DELIVERY_2ND = "ATTEMPTED_DELIVERY_2ND"
    ATTEMPTED_DELIVERY_3RD = "ATTEMPTED_DELIVERY_3RD"
    COD_AMOUNT_NOT_PAID = "COD_AMOUNT_NOT_PAID"
    COD_AMOUNT_PAID = "COD_AMOUNT_PAID"
    CUSTOMER_CARDED = "CUSTOMER_CARDED"
    CUSTOMER_IDENTIFICATION_FAILED = "CUSTOMER_IDENTIFICATION_FAILED"
    INVALID_METHOD_OF_PAYMENT = "INVALID_METHOD_OF_PAYMENT"
    NO_ACCESS_TO_RECIPIENTS_ADDRESS = "NO_ACCESS_TO_RECIPIENTS_ADDRESS"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    DELIVERED_DAMAGED = "DELIVERED_DAMAGED"
    DELIVERED_IN_PART = "DELIVERED_IN_PART"
    DELIVERED_SPECIFIED_SAFE_PLACE = "DELIVERED_SPECIFIED_SAFE_PLACE"
    DELIVERED_TO_ALTERNATIVE_DELIVERY_LOCATION = "DELIVERED_TO_ALTERNATIVE_DELIVERY_LOCATION"
    DELIVERED_TO_NEIGHBOUR = "DELIVERED_TO_NEIGHBOUR"
    DELIVERED_TO_PO_BOX = "DELIVERED_TO_PO_BOX"
    PARCEL_COLLECTED_FROM_PICKUP_POINT = "PARCEL_COLLECTED_FROM_PICKUP_POINT"
    POST_TRANSIT_STATUS = "POST_TRANSIT_STATUS"
    PROOF_OF_DELIVERY = "PROOF_OF_DELIVERY"
    CANCELLED = "CANCELLED"
    CANCELLED_BEFORE_DESPATCH = "CANCELLED_BEFORE_DESPATCH"
    CUSTOMER_MOVED = "CUSTOMER_MOVED"
    HAZARDOUS_PROHIBITED = "HAZARDOUS_PROHIBITED"
    NOT_COLLECTED_FROM_PICKUP_POINT = "NOT_COLLECTED_FROM_PICKUP_POINT"
    NOT_DELIVERED = "NOT_DELIVERED"
    NOT_DELIVERED_ADDRESSEE_DECEASED = "NOT_DELIVERED_ADDRESSEE_DECEASED"
    PARCEL_DAMAGED = "PARCEL_DAMAGED"
    PARCEL_DISPOSED = "PARCEL_DISPOSED"
    PARCEL_LOST = "PARCEL_LOST"
    PARCEL_OUTSIDE_OF_SERVICE_CAPABILITY = "PARCEL_OUTSIDE_OF_SERVICE_CAPABILITY"
    REFUSED_BY_CUSTOMER = "REFUSED_BY_CUSTOMER"
    RETURN_TO_SENDER = "RETURN_TO_SENDER"
    ADDRESS_QUERY = "ADDRESS_QUERY"
    CARRIER_DELAYS = "CARRIER_DELAYS"
    CUSTOMS_CLEARED = "CUSTOMS_CLEARED"
    CUSTOMS_PROCESSING = "CUSTOMS_PROCESSING"
    DELAYED_NOT_CARRIER = "DELAYED_NOT_CARRIER"
    DELIVERY_ARRANGED_WITH_RECIPIENT = "DELIVERY_ARRANGED_WITH_RECIPIENT"
    HELD_BY_CARRIER = "HELD_BY_CARRIER"
    HELD_BY_CARRIER_FOR_CLEARANCE_PRE_PROCESSING = "HELD_BY_CARRIER_FOR_CLEARANCE_PRE_PROCESSING"
    HELD_BY_CUSTOMS = "HELD_BY_CUSTOMS"
    HELD_BY_EXPORT_CUSTOMS = "HELD_BY_EXPORT_CUSTOMS"
    HELD_BY_IMPORT_CUSTOMS = "HELD_BY_IMPORT_CUSTOMS"
    HUB_SCAN_OUT = "HUB_SCAN_OUT"
    IN_TRANSIT = "IN_TRANSIT"
    INCORRECT_DECLARATION = "INCORRECT_DECLARATION"
    INFORMATION = "INFORMATION"
    MISSORTED = "MISSORTED"
    PARCEL_OVER_LABELLED = "PARCEL_OVER_LABELLED"
    PARCEL_REPACKED = "PARCEL_REPACKED"
    PARCEL_UPDATE_NOTIFICATION_VIA_EMAIL = "PARCEL_UPDATE_NOTIFICATION_VIA_EMAIL"
    PARCEL_UPDATE_NOTIFICATION_VIA_SMS = "PARCEL_UPDATE_NOTIFICATION_VIA_SMS"
    RECEIVED_BY_CARRIER = "RECEIVED_BY_CARRIER"
    RECEIVED_LOCAL_DELIVERY_DEPOT = "RECEIVED_LOCAL_DELIVERY_DEPOT"
    ROUTING_ERROR = "ROUTING_ERROR"
    SUB_CONTRACTOR_EVENT = "SUB_CONTRACTOR_EVENT"
    SUB_CONTRACTOR_RECEIVED = "SUB_CONTRACTOR_RECEIVED"
    RECD_BY_CARRIER_NO_ELEC_ADVICE = "RECD_BY_CARRIER_NO_ELEC_ADVICE"
    AWAITING_ELECTRONIC_ADVICE = "AWAITING_ELECTRONIC_ADVICE"
    AWAITING_COLLECTION_FROM_PICKUP_POINT = "AWAITING_COLLECTION_FROM_PICKUP_POINT"
    COLLECT_AT_LOCAL_PO = "COLLECT_AT_LOCAL_PO"
    CUSTOMER_TO_COLLECT_FROM_CARRIER = "CUSTOMER_TO_COLLECT_FROM_CARRIER"
    DELIVERED_TO_LOCKER_COLLECTION_POINT = "DELIVERED_TO_LOCKER_COLLECTION_POINT"
    CARRIER_STATUS_NOT_MAPPED = "CARRIER_STATUS_NOT_MAPPED"


class ValidateAddress(StrEnum):
    """The possible validate address values"""

    NO_VALIDATION = "no_validation"
    VALIDATE_ONLY = "validate_only"
    VALIDATE_AND_CLEAN = "validate_and_clean"


class ValidationStatus(StrEnum):
    """The possible validation status values"""

    VALID = "valid"
    INVALID = "invalid"
    HAS_WARNINGS = "has_warnings"
    UNKNOWN = "unknown"


class WebhookEvent(StrEnum):
    """The possible webhook event values"""

    BATCH = "batch"
    CARRIER_CONNECTED = "carrier_connected"
    ORDER_SOURCE_REFRESH_COMPLETE = "order_source_refresh_complete"
    RATE = "rate"
    REPORT_COMPLETE = "report_complete"
    SALES_ORDERS_IMPORTED = "sales_orders_imported"
    TRACK = "track"
    BATCH_PROCESSED_V2 = "batch_processed_v2"
    FULFILLMENT_REJECTED_V2 = "fulfillment_rejected_v2"
    FULFILLMENT_SHIPPED_V2 = "fulfillment_shipped_v2"
    LABEL_CREATED_V2 = "label_created_v2"
    SHIPMENT_CREATED_V2 = "shipment_created_v2"
    TRACK_EVENT_V2 = "track_event_v2"


class WeightUnit(StrEnum):
    """The possible weight unit values"""

    POUND = "pound"
    OUNCE = "ounce"
    GRAM = "gram"
    KILOGRAM = "kilogram"
