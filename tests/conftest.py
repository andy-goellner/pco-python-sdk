from typing import Any, Dict

import pytest
from pco_python_sdk.api import AbstractHttpClient
from pco_python_sdk.errors import RequestFailedError


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
