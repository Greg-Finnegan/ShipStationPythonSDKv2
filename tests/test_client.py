"""Unit tests for the ShipStation SDK client — mocks all HTTP calls."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from shipstation import ShipStation, ShipStationError
from shipstation.enums import (
    BatchStatus,
    LabelStatus,
    ShipmentStatus,
    SortDir,
)
from shipstation.models import (
    ListBatchesResponseBody,
    ListLabelsResponseBody,
    ListShipmentsResponseBody,
    ListTagsResponseBody,
    ListWarehousesResponseBody,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

EMPTY_LINK = {"href": ""}

EMPTY_LINKS = {
    "first": EMPTY_LINK,
    "last": EMPTY_LINK,
    "prev": EMPTY_LINK,
    "next": EMPTY_LINK,
}

SAMPLE_ADDRESS = {
    "name": "Jane Doe",
    "phone": "555-0100",
    "address_line1": "123 Main St",
    "city_locality": "Austin",
    "state_province": "TX",
    "postal_code": "78701",
    "country_code": "US",
    "address_residential_indicator": "yes",
}


def _mock_response(status_code: int = 200, json_data: dict | None = None) -> MagicMock:
    """Create a mock requests.Response."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = json.dumps(json_data or {})
    resp.json.return_value = json_data or {}
    return resp


@pytest.fixture()
def client() -> ShipStation:
    return ShipStation(api_key="test-key-123")


# ---------------------------------------------------------------------------
# shipments.list
# ---------------------------------------------------------------------------


class TestListShipments:
    def test_basic_call(self, client: ShipStation) -> None:
        payload = {
            "shipments": [],
            "total": 0,
            "page": 1,
            "pages": 0,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            result = client.shipments.list(pickup_id="se-123")

        mock.assert_called_once()
        args, kwargs = mock.call_args
        assert args[0] == "GET"
        assert args[1] == "/v2/shipments"
        assert isinstance(result, ListShipmentsResponseBody)
        assert result.total == 0

    def test_with_filters(self, client: ShipStation) -> None:
        payload = {
            "shipments": [],
            "total": 0,
            "page": 2,
            "pages": 5,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            client.shipments.list(
                pickup_id="se-123",
                shipment_status=ShipmentStatus.PENDING,
                page=2,
                page_size=50,
                sort_dir=SortDir.ASC,
            )

        _, kwargs = mock.call_args
        params = kwargs["params"]
        assert params["shipment_status"] == "pending"
        assert params["page"] == 2
        assert params["page_size"] == 50
        assert params["sort_dir"] == "asc"

    def test_response_deserialization(self, client: ShipStation) -> None:
        payload = {
            "shipments": [
                {
                    "shipment_id": "se-100",
                    "created_at": "2025-01-15T10:30:00Z",
                    "modified_at": "2025-01-15T10:30:00Z",
                    "shipment_status": "pending",
                    "ship_to": SAMPLE_ADDRESS,
                    "ship_from": SAMPLE_ADDRESS,
                    "return_to": SAMPLE_ADDRESS,
                    "confirmation": "none",
                    "advanced_options": {},
                    "insurance_provider": "none",
                    "tags": [],
                    "packages": [],
                    "total_weight": {"value": 5, "unit": "pound"},
                }
            ],
            "total": 1,
            "page": 1,
            "pages": 1,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ):
            result = client.shipments.list(pickup_id="se-123")

        assert result.total == 1
        assert len(result.shipments) == 1
        assert result.shipments[0].shipment_id == "se-100"
        assert result.shipments[0].shipment_status == ShipmentStatus.PENDING


# ---------------------------------------------------------------------------
# labels.list
# ---------------------------------------------------------------------------


class TestListLabels:
    def test_basic_call(self, client: ShipStation) -> None:
        payload = {
            "labels": [],
            "total": 0,
            "page": 1,
            "pages": 0,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            result = client.labels.list()

        mock.assert_called_once()
        assert isinstance(result, ListLabelsResponseBody)

    def test_with_label_status_filter(self, client: ShipStation) -> None:
        payload = {
            "labels": [],
            "total": 0,
            "page": 1,
            "pages": 0,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            client.labels.list(label_status=LabelStatus.COMPLETED)

        _, kwargs = mock.call_args
        assert kwargs["params"]["label_status"] == "completed"


# ---------------------------------------------------------------------------
# tags.list
# ---------------------------------------------------------------------------


class TestListTags:
    def test_basic_call(self, client: ShipStation) -> None:
        payload = {"tags": [{"name": "Priority", "tag_id": 1}]}
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            result = client.tags.list()

        mock.assert_called_once()
        args, _ = mock.call_args
        assert args[0] == "GET"
        assert args[1] == "/v2/tags"
        assert isinstance(result, ListTagsResponseBody)


# ---------------------------------------------------------------------------
# warehouses.list
# ---------------------------------------------------------------------------


class TestListWarehouses:
    def test_basic_call(self, client: ShipStation) -> None:
        payload = {"warehouses": []}
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            result = client.warehouses.list()

        mock.assert_called_once()
        assert isinstance(result, ListWarehousesResponseBody)


# ---------------------------------------------------------------------------
# batches.list
# ---------------------------------------------------------------------------


class TestListBatches:
    def test_basic_call(self, client: ShipStation) -> None:
        payload = {
            "batches": [],
            "total": 0,
            "page": 1,
            "pages": 0,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            result = client.batches.list()

        mock.assert_called_once()
        assert isinstance(result, ListBatchesResponseBody)

    def test_with_status_filter(self, client: ShipStation) -> None:
        payload = {
            "batches": [],
            "total": 0,
            "page": 1,
            "pages": 0,
            "links": EMPTY_LINKS,
        }
        with patch.object(
            client._api, "request", return_value=_mock_response(json_data=payload)
        ) as mock:
            client.batches.list(status=BatchStatus.COMPLETED, page=3)

        _, kwargs = mock.call_args
        assert kwargs["params"]["status"] == "completed"
        assert kwargs["params"]["page"] == 3


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


class TestErrorHandling:
    def test_api_error_raises_exception(self, client: ShipStation) -> None:
        error_resp = _mock_response(
            status_code=404,
            json_data={"message": "Shipment not found"},
        )
        with patch.object(client._api.session, "request", return_value=error_resp):
            with pytest.raises(ShipStationError) as exc_info:
                client.shipments.get_by_id(shipment_id="se-invalid")

        assert exc_info.value.status_code == 404
        assert "Shipment not found" in exc_info.value.message

    def test_server_error(self, client: ShipStation) -> None:
        error_resp = _mock_response(
            status_code=500,
            json_data={"message": "Internal server error"},
        )
        with patch.object(client._api.session, "request", return_value=error_resp):
            with pytest.raises(ShipStationError) as exc_info:
                client.tags.list()

        assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Client construction
# ---------------------------------------------------------------------------


class TestClientInit:
    def test_default_base_url(self) -> None:
        c = ShipStation(api_key="key")
        assert c._api.base_url == "https://api.shipstation.com"

    def test_custom_base_url(self) -> None:
        c = ShipStation(api_key="key", base_url="https://custom.example.com/")
        assert c._api.base_url == "https://custom.example.com"

    def test_api_key_in_headers(self) -> None:
        c = ShipStation(api_key="my-secret-key")
        assert c._api.session.headers["api-key"] == "my-secret-key"

    def test_resource_sub_clients_exist(self) -> None:
        c = ShipStation(api_key="key")
        assert hasattr(c, "shipments")
        assert hasattr(c, "labels")
        assert hasattr(c, "carriers")
        assert hasattr(c, "batches")
        assert hasattr(c, "tags")
        assert hasattr(c, "warehouses")
        assert hasattr(c, "rates")
        assert hasattr(c, "manifests")
        assert hasattr(c, "webhooks")

    def test_resources_share_api_client(self) -> None:
        c = ShipStation(api_key="key")
        assert c.shipments._api is c._api
        assert c.labels._api is c._api
        assert c.carriers._api is c._api
