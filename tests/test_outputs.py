import json
from pathlib import Path

import pytest

REPORT = Path("/app/report.json")

# Expected values derived from the fixed seed log baked into the image
# (environment/access.log, 6 request lines):
#   - 6 total request lines
#   - 3 distinct client IPs: 192.168.0.1, 192.168.0.2, 10.0.0.5
#   - /index.html is the most-requested path (3 hits vs 2 for /about.html, 1 for /api/login)
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


@pytest.fixture(scope="module")
def report():
    """Criterion 1: the agent wrote /app/report.json as a JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json must be a JSON object"
    return data


def test_report_is_json_object(report):
    """Criterion 1: /app/report.json exists and is a JSON object."""
    assert isinstance(report, dict)


def test_total_requests(report):
    """Criterion 2: "total_requests" is the number of request lines (6)."""
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS


def test_unique_ips(report):
    """Criterion 3: "unique_ips" is the count of distinct client IPs (3)."""
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS


def test_top_path(report):
    """Criterion 4: "top_path" is the most-requested path (/index.html)."""
    assert report.get("top_path") == EXPECTED_TOP_PATH
