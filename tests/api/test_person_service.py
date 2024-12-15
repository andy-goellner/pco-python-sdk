from unittest.mock import MagicMock
from pco_python.api._person_service import PersonService
from pco_python.api.abstract_http_client import AbstractHttpClient


def test_person_service_initializes_an_http_client(
    successful_client: AbstractHttpClient,
):
    client = PersonService(http_client=successful_client)
    assert isinstance(client._http_client, AbstractHttpClient)  # type: ignore


def test_person_service_get_calls_http_client(
    mocker: MagicMock, successful_client: AbstractHttpClient
):
    spy = mocker.spy(successful_client, "request")
    client = PersonService(http_client=successful_client)
    client.get("abc")
    spy.assert_called_once_with("GET", "people/v2/people/abc", None, None, {})
