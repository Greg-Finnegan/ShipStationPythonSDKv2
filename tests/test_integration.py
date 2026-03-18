"""Integration tests that hit the real ShipStation API."""

from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from shipstation import ShipStation, ShipStationError
from shipstation.enums import ShipmentStatus, LabelStatus, BatchStatus, SortDir
from shipstation.models import (
    ListShipmentsResponseBody,
    ListLabelsResponseBody,
    ListBatchesResponseBody,
    ListTagsResponseBody,
    ListWarehousesResponseBody,
    ListCarrierPackageTypesResponseBody,
    ListCarrierServicesResponseBody,
)

load_dotenv()


@pytest.fixture(scope="session")
def client() -> ShipStation:
    api_key = os.environ.get("SHIPSTATION_API_KEY")
    if not api_key:
        pytest.skip("SHIPSTATION_API_KEY not set")
    return ShipStation(api_key=api_key)


# ---------------------------------------------------------------------------
# Carriers
# ---------------------------------------------------------------------------


class TestCarriers:
    def test_list_carriers(self, client: ShipStation) -> None:
        result = client.carriers.list()
        assert result is not None
        assert isinstance(result, (dict, list))

    def test_get_carrier_by_id(self, client: ShipStation) -> None:
        carriers_data = client.carriers.list()
        carrier_list = carriers_data.get("carriers", []) if isinstance(carriers_data, dict) else carriers_data
        if not carrier_list:
            pytest.skip("No carriers connected")
        carrier_id = carrier_list[0]["carrier_id"]
        result = client.carriers.get_by_id(carrier_id=carrier_id)
        assert result.carrier_id == carrier_id

    def test_list_carrier_services(self, client: ShipStation) -> None:
        carriers_data = client.carriers.list()
        carrier_list = carriers_data.get("carriers", []) if isinstance(carriers_data, dict) else carriers_data
        if not carrier_list:
            pytest.skip("No carriers connected")
        carrier_id = carrier_list[0]["carrier_id"]
        result = client.carriers.list_services(carrier_id=carrier_id)
        assert isinstance(result, ListCarrierServicesResponseBody)

    def test_list_carrier_package_types(self, client: ShipStation) -> None:
        carriers_data = client.carriers.list()
        carrier_list = carriers_data.get("carriers", []) if isinstance(carriers_data, dict) else carriers_data
        if not carrier_list:
            pytest.skip("No carriers connected")
        carrier_id = carrier_list[0]["carrier_id"]
        result = client.carriers.list_package_types(carrier_id=carrier_id)
        assert isinstance(result, ListCarrierPackageTypesResponseBody)


# ---------------------------------------------------------------------------
# Shipments
# ---------------------------------------------------------------------------


class TestShipments:
    def test_list_shipments(self, client: ShipStation) -> None:
        result = client.shipments.list(pickup_id="")
        assert isinstance(result, ListShipmentsResponseBody)
        print(f"{result.total} shipments found.")
        assert result.page >= 1

    def test_list_shipments_with_pagination(self, client: ShipStation) -> None:
        result = client.shipments.list(pickup_id="", page=1, page_size=5)
        assert isinstance(result, ListShipmentsResponseBody)
        assert len(result.shipments) <= 5

    def test_list_shipments_with_status_filter(self, client: ShipStation) -> None:
        result = client.shipments.list(
            pickup_id="",
            shipment_status=ShipmentStatus.PENDING,
            page_size=5,
        )
        assert isinstance(result, ListShipmentsResponseBody)
        for s in result.shipments:
            assert s.shipment_status == ShipmentStatus.PENDING

    def test_get_shipment_by_id(self, client: ShipStation) -> None:
        shipments = client.shipments.list(pickup_id="", page_size=1)
        if not shipments.shipments:
            pytest.skip("No shipments found")
        shipment = shipments.shipments[0]
        result = client.shipments.get_by_id(shipment_id=shipment.shipment_id)
        assert result.shipment_id == shipment.shipment_id


# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------


class TestLabels:
    def test_list_labels(self, client: ShipStation) -> None:
        result = client.labels.list(page_size=5)
        assert isinstance(result, ListLabelsResponseBody)
        assert result.page >= 1

    def test_list_labels_with_status(self, client: ShipStation) -> None:
        result = client.labels.list(
            label_status=LabelStatus.COMPLETED,
            page_size=5,
        )
        assert isinstance(result, ListLabelsResponseBody)

    def test_get_label_by_id(self, client: ShipStation) -> None:
        labels = client.labels.list(page_size=1)
        if not labels.labels:
            pytest.skip("No labels found")
        label = labels.labels[0]
        result = client.labels.get_by_id(label_id=label.label_id)
        assert result.label_id == label.label_id


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------


class TestTags:
    def test_list_tags(self, client: ShipStation) -> None:
        result = client.tags.list()
        assert isinstance(result, ListTagsResponseBody)


# ---------------------------------------------------------------------------
# Warehouses
# ---------------------------------------------------------------------------


class TestWarehouses:
    def test_list_warehouses(self, client: ShipStation) -> None:
        result = client.warehouses.list()
        assert isinstance(result, ListWarehousesResponseBody)


# ---------------------------------------------------------------------------
# Batches
# ---------------------------------------------------------------------------


class TestBatches:
    def test_list_batches(self, client: ShipStation) -> None:
        result = client.batches.list(page_size=5)
        assert isinstance(result, ListBatchesResponseBody)

    def test_list_batches_with_filter(self, client: ShipStation) -> None:
        result = client.batches.list(
            status=BatchStatus.COMPLETED,
            page_size=5,
            sort_dir=SortDir.DESC,
        )
        assert isinstance(result, ListBatchesResponseBody)


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


class TestErrors:
    def test_invalid_shipment_id_raises_error(self, client: ShipStation) -> None:
        with pytest.raises(ShipStationError) as exc_info:
            client.shipments.get_by_id(shipment_id="se-0000000000000")
        assert exc_info.value.status_code >= 400
