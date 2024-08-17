from pco_python_sdk.api.http_client import HttpClient
from pco_python_sdk.api.pco_client import PCOClient


def pco_client_initializes_an_http_client(valid_credentials):  # type: ignore
    client = PCOClient(
        credentials=valid_credentials,  # type: ignore
    )
    assert isinstance(client._http_client, HttpClient)  # type: ignore
