"""ShipStation rates resource — auto-generated, do not edit."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from .._api import ApiClient, serialize_body, serialize_param
from ..models import (
    CalculateRatesRequestBody,
    CalculateRatesResponseBody,
    EstimateRatesRequestBody,
    GetRateByIdResponseBody,
)


class RatesResource:
    """Rates API operations."""

    def __init__(self, api: ApiClient) -> None:
        self._api = api

    def calculate(self, *, body: CalculateRatesRequestBody) -> CalculateRatesResponseBody:
        """It's not uncommon that you want to give your customer the choice between whether they want to ship the fastest, cheapest, or the most trusted route. Most companies don't solely ship things using a sin"""
        response = self._api.request("POST", "/v2/rates", params=None, json_body=serialize_body(body))
        return CalculateRatesResponseBody.model_validate(response.json())

    def estimate(self, *, body: EstimateRatesRequestBody) -> EstimateRatesResponseBody:
        """Get Rate Estimates"""
        response = self._api.request("POST", "/v2/rates/estimate", params=None, json_body=serialize_body(body))
        return EstimateRatesResponseBody.model_validate(response.json())

    def get_by_id(self, rate_id: str) -> GetRateByIdResponseBody:
        """Retrieve a previously queried rate by its ID"""
        response = self._api.request("GET", f"/v2/rates/{rate_id}", params=None, json_body=None)
        return GetRateByIdResponseBody.model_validate(response.json())
