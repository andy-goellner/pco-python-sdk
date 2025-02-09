from unittest.mock import MagicMock
import pytest
from planning_center_python.api._pco_service import PcoService
from planning_center_python.api.abstract_http_client import AbstractHttpClient


def test_get_raises_not_implemented_error(successful_client: AbstractHttpClient):
    svc = PcoService(successful_client)
    with pytest.raises(NotImplementedError):
        svc.get("foo", {"bar": "baz"})


def test__request_formats_query_on_get(
    mocker: MagicMock, successful_client: AbstractHttpClient
):
    spy = mocker.spy(successful_client, "request")
    svc = PcoService(successful_client)
    svc._request("GET", "foo/bar", {"param": "one"})  # type: ignore
    assert spy.call_count == 1
    spy.assert_called_once_with("GET", "foo/bar", {"param": "one"}, None, {})


def test__request_formats_payload_on_post(
    mocker: MagicMock, successful_client: AbstractHttpClient
):
    spy = mocker.spy(successful_client, "request")
    svc = PcoService(successful_client)
    svc._request("POST", "foo/bar", {"param": "one"})  # type: ignore
    assert spy.call_count == 1
    spy.assert_called_once_with("POST", "foo/bar", None, {"param": "one"}, {})
