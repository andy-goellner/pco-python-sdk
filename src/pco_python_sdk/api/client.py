import json
from typing import Any, Dict
from pco_python_sdk.api import AbstractClient
from pco_python_sdk.errors import RequestFailedError
from pco_python_sdk.settings import Settings
from requests import Session


class Client(AbstractClient):
    def __init__(self, settings: Settings = Settings(), session: Session = Session()):
        self.settings = settings
        self.session = session
        self.token = "something_here"

    def request(
        self,
        verb: str,
        endpoint: str,
        query: Dict[str, str] = {},
        payload: Dict[str, Any] = {},
        headers: Dict[str, str] = {},
    ) -> Dict[str, Any]:
        url = f"{self.settings.base_url}/{endpoint}"
        response = self.session.request(
            method=verb,
            url=url,
            params=query,
            json=json.dumps(payload),
            headers=headers,
            auth=None,
        )
        if not response.ok:
            raise RequestFailedError(
                message="API Returned an Error", status_code=response.status_code
            )

        return response.json()
