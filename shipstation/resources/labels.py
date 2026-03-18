"""ShipStation labels resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    CreateLabelFromRateRequestBody,
    CreateLabelFromRateResponseBody,
    CreateLabelFromShipmentRequestBody,
    CreateLabelFromShipmentResponseBody,
    CreateLabelRateShopperRequestBody,
    CreateLabelRateShopperResponseBody,
    CreateLabelRequestBody,
    CreateLabelResponseBody,
    CreateReturnLabelRequestBody,
    CreateReturnLabelResponseBody,
    GetLabelByIdResponseBody,
    GetTrackingLogFromLabelResponseBody,
    ListLabelsResponseBody,
    VoidLabelResponseBody,
)
from ..enums import (
    LabelDownloadType,
    LabelStatus,
    SortDir,
)


class LabelsResource:
    """Labels API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(
        self,
        *,
        label_status: Optional[LabelStatus] = None,
        service_code: Optional[str] = None,
        carrier_id: Optional[str] = None,
        tracking_number: Optional[str] = None,
        batch_id: Optional[str] = None,
        rate_id: Optional[str] = None,
        shipment_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
        created_at_start: Optional[datetime] = None,
        created_at_end: Optional[datetime] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 25,
        sort_dir: Optional[SortDir] = 'desc',
        sort_by: Optional[str] = 'created_at',
    ) -> ListLabelsResponseBody:
        """This method returns a list of labels that you've created. You can optionally filter the results as well as control their sort order and the number of results returned at a time. By default all labels """
        params: dict[str, Any] = {}
        if label_status is not None:
            params["label_status"] = label_status.value if hasattr(label_status, 'value') else (label_status.isoformat() if hasattr(label_status, 'isoformat') else label_status)
        if service_code is not None:
            params["service_code"] = service_code.value if hasattr(service_code, 'value') else (service_code.isoformat() if hasattr(service_code, 'isoformat') else service_code)
        if carrier_id is not None:
            params["carrier_id"] = carrier_id.value if hasattr(carrier_id, 'value') else (carrier_id.isoformat() if hasattr(carrier_id, 'isoformat') else carrier_id)
        if tracking_number is not None:
            params["tracking_number"] = tracking_number.value if hasattr(tracking_number, 'value') else (tracking_number.isoformat() if hasattr(tracking_number, 'isoformat') else tracking_number)
        if batch_id is not None:
            params["batch_id"] = batch_id.value if hasattr(batch_id, 'value') else (batch_id.isoformat() if hasattr(batch_id, 'isoformat') else batch_id)
        if rate_id is not None:
            params["rate_id"] = rate_id.value if hasattr(rate_id, 'value') else (rate_id.isoformat() if hasattr(rate_id, 'isoformat') else rate_id)
        if shipment_id is not None:
            params["shipment_id"] = shipment_id.value if hasattr(shipment_id, 'value') else (shipment_id.isoformat() if hasattr(shipment_id, 'isoformat') else shipment_id)
        if warehouse_id is not None:
            params["warehouse_id"] = warehouse_id.value if hasattr(warehouse_id, 'value') else (warehouse_id.isoformat() if hasattr(warehouse_id, 'isoformat') else warehouse_id)
        if created_at_start is not None:
            params["created_at_start"] = created_at_start.value if hasattr(created_at_start, 'value') else (created_at_start.isoformat() if hasattr(created_at_start, 'isoformat') else created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = created_at_end.value if hasattr(created_at_end, 'value') else (created_at_end.isoformat() if hasattr(created_at_end, 'isoformat') else created_at_end)
        if page is not None:
            params["page"] = page.value if hasattr(page, 'value') else (page.isoformat() if hasattr(page, 'isoformat') else page)
        if page_size is not None:
            params["page_size"] = page_size.value if hasattr(page_size, 'value') else (page_size.isoformat() if hasattr(page_size, 'isoformat') else page_size)
        if sort_dir is not None:
            params["sort_dir"] = sort_dir.value if hasattr(sort_dir, 'value') else (sort_dir.isoformat() if hasattr(sort_dir, 'isoformat') else sort_dir)
        if sort_by is not None:
            params["sort_by"] = sort_by.value if hasattr(sort_by, 'value') else (sort_by.isoformat() if hasattr(sort_by, 'isoformat') else sort_by)
        response = self._api.request("GET", "/v2/labels", params=params, json_body=None)
        return ListLabelsResponseBody.model_validate(response.json())

    def create(self, *, body: CreateLabelRequestBody) -> CreateLabelResponseBody:
        """Purchase and print a label for shipment."""
        response = self._api.request("POST", "/v2/labels", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateLabelResponseBody.model_validate(response.json())

    def create_from_rate(
        self,
        rate_id: str,
        *,
        body: CreateLabelFromRateRequestBody,
    ) -> CreateLabelFromRateResponseBody:
        """When retrieving rates for shipments using the `/rates` endpoint, the returned information contains a `rate_id` property that can be used to generate a label without having to refill in the shipment in"""
        response = self._api.request("POST", f"/v2/labels/rates/{rate_id}", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateLabelFromRateResponseBody.model_validate(response.json())

    def create_from_shipment(
        self,
        shipment_id: str,
        *,
        body: CreateLabelFromShipmentRequestBody,
    ) -> CreateLabelFromShipmentResponseBody:
        """Purchase a label using a shipment ID that has already been created with the desired address and package info."""
        response = self._api.request("POST", f"/v2/labels/shipment/{shipment_id}", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateLabelFromShipmentResponseBody.model_validate(response.json())

    def create_from_rate_shopper(
        self,
        rate_shopper_id: str,
        *,
        body: CreateLabelRateShopperRequestBody,
    ) -> CreateLabelRateShopperResponseBody:
        """Create a label using Rate Shopper to automatically select the best carrier and service based on the specified strategy. For more information about Rate Shopper strategies and use cases, see Rate Shopp"""
        response = self._api.request("POST", f"/v2/labels/rate_shopper_id/{rate_shopper_id}", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateLabelRateShopperResponseBody.model_validate(response.json())

    def get_by_id(
        self,
        label_id: str,
        *,
        label_download_type: Optional[LabelDownloadType] = None,
    ) -> GetLabelByIdResponseBody:
        """Retrieve a specific label by its label id."""
        params: dict[str, Any] = {}
        if label_download_type is not None:
            params["label_download_type"] = label_download_type.value if hasattr(label_download_type, 'value') else (label_download_type.isoformat() if hasattr(label_download_type, 'isoformat') else label_download_type)
        response = self._api.request("GET", f"/v2/labels/{label_id}", params=params, json_body=None)
        return GetLabelByIdResponseBody.model_validate(response.json())

    def create_return(
        self,
        label_id: str,
        *,
        body: CreateReturnLabelRequestBody,
    ) -> CreateReturnLabelResponseBody:
        """Create a return label for a previously created outbound label. The return label will automatically swap the ship to and ship from addresses from the original label."""
        response = self._api.request("POST", f"/v2/labels/{label_id}/return", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreateReturnLabelResponseBody.model_validate(response.json())

    def get_tracking_log_from(self, label_id: str) -> GetTrackingLogFromLabelResponseBody:
        """Retrieve the label's tracking details."""
        response = self._api.request("GET", f"/v2/labels/{label_id}/track", params=None, json_body=None)
        return GetTrackingLogFromLabelResponseBody.model_validate(response.json())

    def void(self, label_id: str) -> VoidLabelResponseBody:
        """Void a specific label using its label id. For labels that are paid for at time of label creation, this will also request a refund from the carrier."""
        response = self._api.request("PUT", f"/v2/labels/{label_id}/void", params=None, json_body=None)
        return VoidLabelResponseBody.model_validate(response.json())
