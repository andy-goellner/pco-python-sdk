from collections.abc import Mapping
import json
from typing import Any, Optional

import pytest
from planning_center_python.api import AbstractHttpClient, Credentials, PCOToken
from planning_center_python.data.api_response.pco_response import PCOResponse
from planning_center_python.errors import RequestFailedError


@pytest.fixture
def successful_client() -> AbstractHttpClient:
    class FakeClient(AbstractHttpClient):
        def request(
            self,
            verb: str,
            endpoint: str,
            query: Optional[Mapping[str, str]] = None,
            payload: Optional[Mapping[str, Any]] = None,
            headers: Optional[Mapping[str, str]] = None,
        ) -> PCOResponse:
            return PCOResponse(
                body=json.dumps(
                    {"data": {"id": "1234", "attributes": {"fake_prop": "foobar"}}}
                ),
                code=200,
                headers={},
            )

    return FakeClient()


@pytest.fixture
def failed_client():
    class FakeClient(AbstractHttpClient):
        def request(
            self,
            verb: str,
            endpoint: str,
            query: Optional[Mapping[str, str]] = None,
            payload: Optional[Mapping[str, Any]] = None,
            headers: Optional[Mapping[str, str]] = None,
        ) -> PCOResponse:
            raise RequestFailedError(message="failed request", status_code=400)

    return FakeClient()


@pytest.fixture
def valid_credentials():
    pco_token = PCOToken(
        {"access_token": "foo", "expires_in": 700, "refresh_token": "refreshtoken"}
    )
    creds = Credentials(
        client_id="testclientid", client_secret="testclientsecret", pco_token=pco_token
    )
    return creds
