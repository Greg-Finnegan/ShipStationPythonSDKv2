"""ShipStation labels resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
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
            params["label_status"] = serialize_param(label_status)
        if service_code is not None:
            params["service_code"] = serialize_param(service_code)
        if carrier_id is not None:
            params["carrier_id"] = serialize_param(carrier_id)
        if tracking_number is not None:
            params["tracking_number"] = serialize_param(tracking_number)
        if batch_id is not None:
            params["batch_id"] = serialize_param(batch_id)
        if rate_id is not None:
            params["rate_id"] = serialize_param(rate_id)
        if shipment_id is not None:
            params["shipment_id"] = serialize_param(shipment_id)
        if warehouse_id is not None:
            params["warehouse_id"] = serialize_param(warehouse_id)
        if created_at_start is not None:
            params["created_at_start"] = serialize_param(created_at_start)
        if created_at_end is not None:
            params["created_at_end"] = serialize_param(created_at_end)
        if page is not None:
            params["page"] = serialize_param(page)
        if page_size is not None:
            params["page_size"] = serialize_param(page_size)
        if sort_dir is not None:
            params["sort_dir"] = serialize_param(sort_dir)
        if sort_by is not None:
            params["sort_by"] = serialize_param(sort_by)
        response = self._api.request("GET", "/v2/labels", params=params, json_body=None)
        return ListLabelsResponseBody.model_validate(response.json())

    def create(self, *, body: CreateLabelRequestBody) -> CreateLabelResponseBody:
        """Purchase and print a label for shipment."""
        response = self._api.request("POST", "/v2/labels", params=None, json_body=serialize_body(body))
        return CreateLabelResponseBody.model_validate(response.json())

    def create_from_rate(
        self,
        rate_id: str,
        *,
        body: CreateLabelFromRateRequestBody,
    ) -> CreateLabelFromRateResponseBody:
        """When retrieving rates for shipments using the `/rates` endpoint, the returned information contains a `rate_id` property that can be used to generate a label without having to refill in the shipment in"""
        response = self._api.request("POST", f"/v2/labels/rates/{rate_id}", params=None, json_body=serialize_body(body))
        return CreateLabelFromRateResponseBody.model_validate(response.json())

    def create_from_shipment(
        self,
        shipment_id: str,
        *,
        body: CreateLabelFromShipmentRequestBody,
    ) -> CreateLabelFromShipmentResponseBody:
        """Purchase a label using a shipment ID that has already been created with the desired address and package info."""
        response = self._api.request("POST", f"/v2/labels/shipment/{shipment_id}", params=None, json_body=serialize_body(body))
        return CreateLabelFromShipmentResponseBody.model_validate(response.json())

    def create_from_rate_shopper(
        self,
        rate_shopper_id: str,
        *,
        body: CreateLabelRateShopperRequestBody,
    ) -> CreateLabelRateShopperResponseBody:
        """Create a label using Rate Shopper to automatically select the best carrier and service based on the specified strategy. For more information about Rate Shopper strategies and use cases, see Rate Shopp"""
        response = self._api.request("POST", f"/v2/labels/rate_shopper_id/{rate_shopper_id}", params=None, json_body=serialize_body(body))
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
            params["label_download_type"] = serialize_param(label_download_type)
        response = self._api.request("GET", f"/v2/labels/{label_id}", params=params, json_body=None)
        return GetLabelByIdResponseBody.model_validate(response.json())

    def create_return(
        self,
        label_id: str,
        *,
        body: CreateReturnLabelRequestBody,
    ) -> CreateReturnLabelResponseBody:
        """Create a return label for a previously created outbound label. The return label will automatically swap the ship to and ship from addresses from the original label."""
        response = self._api.request("POST", f"/v2/labels/{label_id}/return", params=None, json_body=serialize_body(body))
        return CreateReturnLabelResponseBody.model_validate(response.json())

    def get_tracking_log_from(self, label_id: str) -> GetTrackingLogFromLabelResponseBody:
        """Retrieve the label's tracking details."""
        response = self._api.request("GET", f"/v2/labels/{label_id}/track", params=None, json_body=None)
        return GetTrackingLogFromLabelResponseBody.model_validate(response.json())

    def void(self, label_id: str) -> VoidLabelResponseBody:
        """Void a specific label using its label id. For labels that are paid for at time of label creation, this will also request a refund from the carrier."""
        response = self._api.request("PUT", f"/v2/labels/{label_id}/void", params=None, json_body=None)
        return VoidLabelResponseBody.model_validate(response.json())
