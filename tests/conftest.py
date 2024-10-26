from typing import Any, Dict

import pytest
from pco_python.api import AbstractHttpClient, Credentials, PCOToken
from pco_python.errors import RequestFailedError


@pytest.fixture
def successful_client() -> AbstractHttpClient:
    class FakeClient(AbstractHttpClient):
        def request(
            self,
            verb: str,
            endpoint: str,
            query: Dict[str, str] = {},
            payload: Dict[str, Any] = {},
            headers: Dict[str, str] = {},
        ) -> Dict[str, Any]:
            return {"id": "1234", "attributes": {"fake_prop": "foobar"}}

    return FakeClient()


@pytest.fixture
def failed_client():
    class FakeClient(AbstractHttpClient):
        def request(
            self,
            verb: str,
            endpoint: str,
            query: Dict[str, str] = {},
            payload: Dict[str, Any] = {},
            headers: Dict[str, str] = {},
        ) -> Dict[str, Any]:
            raise RequestFailedError(message="failed request", status_code=400)

    return FakeClient()


@pytest.fixture
def valid_credentials():
    pco_token = PCOToken(
        access_token="foo", expires_in=700, refresh_token="refreshtoken"
    )
    creds = Credentials(
        client_id="testclientid", client_secret="testclientsecret", pco_token=pco_token
    )
    return creds
