"""Pytest conftest — logs raw API responses to a unique file per test run."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest


LOGS_DIR = Path(__file__).parent.parent / "logs"


@pytest.fixture(scope="session", autouse=True)
def response_logger():
    """Wrap ApiClient.request to log every raw HTTP response."""
    from shipstation._api import ApiClient

    LOGS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOGS_DIR / f"responses_{timestamp}.log"

    original_request = ApiClient.request
    current_test = {"name": "unknown"}

    def logging_request(self, method, path, *, params=None, json_body=None):
        resp = original_request(self, method, path, params=params, json_body=json_body)

        entry = {
            "test": current_test["name"],
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "path": path,
            "params": params,
            "request_body": json_body,
            "status_code": resp.status_code,
            "response_body": resp.json() if resp.headers.get("Content-Type", "").startswith("application/json") else resp.text,
        }

        with open(log_path, "a") as f:
            f.write(json.dumps(entry, indent=2, default=str) + "\n---\n")

        return resp

    # Also log errors (re-raise after logging)
    def logging_request_with_errors(self, method, path, *, params=None, json_body=None):
        try:
            return logging_request(self, method, path, params=params, json_body=json_body)
        except Exception as exc:
            entry = {
                "test": current_test["name"],
                "timestamp": datetime.now().isoformat(),
                "method": method,
                "path": path,
                "params": params,
                "request_body": json_body,
                "error": str(exc),
            }
            with open(log_path, "a") as f:
                f.write(json.dumps(entry, indent=2, default=str) + "\n---\n")
            raise

    with patch.object(ApiClient, "request", logging_request_with_errors):
        yield current_test, log_path

    print(f"\nAPI responses logged to: {log_path}")


@pytest.fixture(autouse=True)
def _track_test_name(request, response_logger):
    """Update the current test name so the logger can tag each entry."""
    current_test, _ = response_logger
    current_test["name"] = request.node.nodeid
