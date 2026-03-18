"""ShipStation package_types resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient
from ..models import (
    CreatePackageTypeRequestBody,
    CreatePackageTypeResponseBody,
    GetPackageTypeByIdResponseBody,
    ListPackageTypesResponseBody,
    UpdatePackageTypeRequestBody,
)


class PackageTypesResource:
    """PackageTypes API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def list(self) -> ListPackageTypesResponseBody:
        """List the custom package types associated with the account"""
        response = self._api.request("GET", "/v2/packages", params=None, json_body=None)
        return ListPackageTypesResponseBody.model_validate(response.json())

    def create(self, *, body: CreatePackageTypeRequestBody) -> CreatePackageTypeResponseBody:
        """Create a custom package type to better assist in getting accurate rate estimates"""
        response = self._api.request("POST", "/v2/packages", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return CreatePackageTypeResponseBody.model_validate(response.json())

    def get_by_id(self, package_id: str) -> GetPackageTypeByIdResponseBody:
        """Get Custom Package Type by ID"""
        response = self._api.request("GET", f"/v2/packages/{package_id}", params=None, json_body=None)
        return GetPackageTypeByIdResponseBody.model_validate(response.json())

    def update(
        self,
        package_id: str,
        *,
        body: UpdatePackageTypeRequestBody,
    ) -> None:
        """Update the custom package type object by ID"""
        response = self._api.request("PUT", f"/v2/packages/{package_id}", params=None, json_body=body.model_dump(exclude_none=True, by_alias=True) if hasattr(body, 'model_dump') else body)
        return None

    def delete(self, package_id: str) -> None:
        """Delete a custom package using the ID"""
        response = self._api.request("DELETE", f"/v2/packages/{package_id}", params=None, json_body=None)
        return None
