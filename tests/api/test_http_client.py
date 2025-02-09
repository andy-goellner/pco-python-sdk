from typing import Any, Mapping, NamedTuple
from unittest.mock import MagicMock

import pytest
from planning_center_python.api.credentials import Credentials
from planning_center_python.api.http_client import HttpClient
from planning_center_python.api.session import Session
from planning_center_python.errors import RequestFailedError


class FakeResponse(NamedTuple):
    text: str
    ok: bool
    status_code: int
    headers: Mapping[str, Any]


FAKE_RESPONSE = FakeResponse('{"thing": "data"}', True, 200, {})
FAKE_FAILED_RESPONSE = FakeResponse('{"thing": "data"}', False, 404, {})


def test_http_client_configures_session(valid_credentials: Credentials):
    client = HttpClient(valid_credentials)
    assert isinstance(client.session, Session)


def test_http_client_has_valid_base_url(valid_credentials: Credentials):
    client = HttpClient(valid_credentials)
    assert client.base_url == "https://api.planningcenteronline.com"


def test_http_client_request_calls_session(
    mocker: MagicMock, valid_credentials: Credentials
):
    mock = mocker.patch("planning_center_python.api.http_client.Session")
    instance = mock.return_value
    req_method = instance.request
    req_method.return_value = FAKE_RESPONSE
    client = HttpClient(valid_credentials)
    client.request(
        "GET",
        "junk/endpoint",
        query={"param": "param_one"},
        payload={"data": "is_here"},
        headers={"json": "true"},
    )
    assert mock.call_count == 1
    assert req_method.call_count == 1
    req_method.assert_called_once_with(
        method="GET",
        url="https://api.planningcenteronline.com/junk/endpoint",
        params={"param": "param_one"},
        json='{"data": "is_here"}',
        headers={"json": "true"},
    )


def test_http_client_request_fails_raise_error(
    mocker: MagicMock, valid_credentials: Credentials
):
    mock = mocker.patch("planning_center_python.api.http_client.Session")
    instance = mock.return_value
    req_method = instance.request
    req_method.return_value = FAKE_FAILED_RESPONSE
    client = HttpClient(valid_credentials)
    with pytest.raises(RequestFailedError, match="API Returned an Error") as e:
        client.request(
            "GET",
            "junk/endpoint",
            query={"param": "param_one"},
            payload={"data": "is_here"},
            headers={"json": "true"},
        )
        assert e.status_code == 404  # type: ignore
