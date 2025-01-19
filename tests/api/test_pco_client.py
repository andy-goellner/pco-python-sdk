from planning_center_python.api import Credentials, PCOClient
from planning_center_python.api._person_service import PersonService
from planning_center_python.api.abstract_http_client import AbstractHttpClient


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
