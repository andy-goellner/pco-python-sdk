from pco_python_sdk.api import Credentials, PCOClient
from pco_python_sdk.api.abstract_http_client import AbstractHttpClient
from pco_python_sdk.models.person import Person


def test_pco_client_initializes_an_http_client(
    valid_credentials: Credentials, successful_client: AbstractHttpClient
):
    client = PCOClient(credentials=valid_credentials, http_client=successful_client)
    assert isinstance(client._http_client, AbstractHttpClient)  # type: ignore


def test_pco_client_initializes_person_object(
    valid_credentials: Credentials, successful_client: AbstractHttpClient
):
    assert isinstance(
        PCOClient(credentials=valid_credentials, http_client=successful_client).person,
        Person,
    )
