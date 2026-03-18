"""ShipStation batches resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    CreateAndProcessBatchRequestBody,
    CreateBatchRequestBody,
    CreateBatchResponseBody,
    GetBatchByExternalIdResponseBody,
    GetBatchByIdResponseBody,
    ListBatchErrorsResponseBody,
    ListBatchesResponseBody,
    ProcessBatchRequestBody,
    RemoveFromBatchRequestBody,
)
from ..enums import (
    BatchStatus,
    BatchesSortBy,
    SortDir,
)


class BatchesResource:
    """Batches API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        status: Optional[BatchStatus] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
        sort_dir: Optional[SortDir] = 'desc',
        batch_number: Optional[str] = None,
        sort_by: Optional[BatchesSortBy] = None,
    ) -> ListBatchesResponseBody:
        """List the batches associated with your ShipStation account."""
        params: dict[str, Any] = {}
        if status is not None:
            params["status"] = status.value if hasattr(status, 'value') else (status.isoformat() if hasattr(status, 'isoformat') else status)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if sort_dir is not None:
            params["sort_dir"] = sort_dir.value if hasattr(sort_dir, 'value') else (sort_dir.isoformat() if hasattr(sort_dir, 'isoformat') else sort_dir)
        if batch_number is not None:
            params["batch_number"] = batch_number.value if hasattr(batch_number, 'value') else (batch_number.isoformat() if hasattr(batch_number, 'isoformat') else batch_number)
        if sort_by is not None:
            params["sort_by"] = sort_by.value if hasattr(sort_by, 'value') else (sort_by.isoformat() if hasattr(sort_by, 'isoformat') else sort_by)
        response = self._api.request("GET", "/v2/batches", params=params, json_body=None)
        return ListBatchesResponseBody.model_validate(response.json())

    def create(self, *, body: Union[CreateBatchRequestBody, CreateAndProcessBatchRequestBody]) -> CreateBatchResponseBody:
        """Create a batch containing multiple labels."""
        response = self._api.request("POST", "/v2/batches", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateBatchResponseBody.model_validate(response.json())

    def get_by_external_id(self, external_batch_id: str) -> GetBatchByExternalIdResponseBody:
        """Retreive a batch using an external batch ID"""
        response = self._api.request("GET", f"/v2/batches/external_batch_id/{external_batch_id}", params=None, json_body=None)
        return GetBatchByExternalIdResponseBody.model_validate(response.json())

    def get_by_id(self, batch_id: str) -> GetBatchByIdResponseBody:
        """Get batch details for a specific batch id."""
        response = self._api.request("GET", f"/v2/batches/{batch_id}", params=None, json_body=None)
        return GetBatchByIdResponseBody.model_validate(response.json())

    def update(self, batch_id: str) -> None:
        """Update a batch by id setting its status to 'archived'."""
        response = self._api.request("PUT", f"/v2/batches/{batch_id}", params=None, json_body=None)
        return None

    def delete(self, batch_id: str) -> None:
        """Delete a batch based on its batch id. Sets its status to 'archived'."""
        response = self._api.request("DELETE", f"/v2/batches/{batch_id}", params=None, json_body=None)
        return None

    def add_to(
        self,
        batch_id: str,
        *,
        body: CreateAndProcessBatchRequestBody,
    ) -> None:
        """Add a shipment or rate to a batch."""
        response = self._api.request("POST", f"/v2/batches/{batch_id}/add", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return None

    def list_errors(
        self,
        batch_id: str,
        *,
        page: Optional[int] = 1,
        pagesize: Optional[int] = None,
    ) -> ListBatchErrorsResponseBody:
        """Errors in batches must be handled differently from synchronous requests. You must retrieve the status of your batch by getting a batch and getting an overview of the statuses or by listing the batch e"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if pagesize is not None:
            params["pagesize"] = pagesize.value if hasattr(pagesize, 'value') else (pagesize.isoformat() if hasattr(pagesize, 'isoformat') else pagesize)
        response = self._api.request("GET", f"/v2/batches/{batch_id}/errors", params=params, json_body=None)
        return ListBatchErrorsResponseBody.model_validate(response.json())

    def process(
        self,
        batch_id: str,
        *,
        body: ProcessBatchRequestBody,
    ) -> None:
        """Create and purchase the labels for the shipments included in the batch."""
        response = self._api.request("POST", f"/v2/batches/{batch_id}/process/labels", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return None

    def remove_from(
        self,
        batch_id: str,
        *,
        body: RemoveFromBatchRequestBody,
    ) -> None:
        """Remove specific shipment ids or rate ids from a batch."""
        response = self._api.request("POST", f"/v2/batches/{batch_id}/remove", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return None
