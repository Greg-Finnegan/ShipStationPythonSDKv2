"""ShipStation batches enums — auto-generated, do not edit."""

from __future__ import annotations

from enum import StrEnum


class BatchStatus(StrEnum):
    """The possible batch status values"""

    OPEN = "open"
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    COMPLETED_WITH_ERRORS = "completed_with_errors"
    ARCHIVED = "archived"
    NOTIFYING = "notifying"
    INVALID = "invalid"


class BatchesSortBy(StrEnum):
    """The possible batches sort by values"""

    SHIP_DATE = "ship_date"
    PROCESSED_AT = "processed_at"
    CREATED_AT = "created_at"
