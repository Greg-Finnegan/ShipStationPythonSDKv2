"""ShipStation labels enums — auto-generated, do not edit."""

from __future__ import annotations

from enum import StrEnum


class LabelChargeEvent(StrEnum):
    """Determines when the user's account will be charged for the label."""

    CARRIER_DEFAULT = "carrier_default"
    ON_CREATION = "on_creation"
    ON_CARRIER_ACCEPTANCE = "on_carrier_acceptance"


class LabelStatus(StrEnum):
    """The possible statuses that a [shipping label] can be in. |Status |Description |:------------|:----------------------------------------------------- |`processing` |When labels are created in a [batch], it may take a few minutes for all of the labels in the batch to be created. During this period, they will be in `processing` status. |`completed` |The label was successfully created |`error` |The label could not be created due to an error, such as an invalid delivery address |`voided` |The label has been [voided]"""

    PROCESSING = "processing"
    COMPLETED = "completed"
    ERROR = "error"
    VOIDED = "voided"


class LabelVoidFailureReason(StrEnum):
    """The possible normalized reasons a label void request may not have been approved"""

    UNKNOWN = "unknown"
    UNSPECIFIED = "unspecified"
    VALIDATION_FAILED = "validation_failed"
    LABEL_NOT_FOUND_WITHIN_VOID_PERIOD = "label_not_found_within_void_period"
    LABEL_ALREADY_USED = "label_already_used"
    LABEL_ALREADY_VOIDED = "label_already_voided"
    CONTACT_CARRIER = "contact_carrier"


class TrackingStatus(StrEnum):
    """The different statuses that can apply to a shipment."""

    UNKNOWN = "unknown"
    IN_TRANSIT = "in_transit"
    ERROR = "error"
    DELIVERED = "delivered"
