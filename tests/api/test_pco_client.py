import pytest
from planning_center_python.api import Credentials, PCOClient
from planning_center_python.api._person_service import PersonService
from planning_center_python.api.abstract_http_client import AbstractHttpClient
from planning_center_python.errors import PCOClientInitializationError


def test_pco_client_initializes_an_http_client(
    valid_credentials: Credentials, successful_client: AbstractHttpClient
):
    client = PCOClient(credentials=valid_credentials, http_client=successful_client)
    assert isinstance(client._http_client, AbstractHttpClient)  # type: ignore


def test_pco_client_initializes_person_service(
    valid_credentials: Credentials, successful_client: AbstractHttpClient
):
    assert isinstance(
        PCOClient(credentials=valid_credentials, http_client=successful_client).person,
        PersonService,
    )


def test_invalid_params_raises_error():
    with pytest.raises(PCOClientInitializationError):
        PCOClient().__init__()


def test_client_is_a_singleton(valid_credentials: Credentials):
    instance = PCOClient(credentials=valid_credentials)
    new_instance = PCOClient()
    assert instance is new_instance
