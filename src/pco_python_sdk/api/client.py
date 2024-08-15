import json
from typing import Any, Dict, Optional
from pco_python_sdk.api import AbstractClient, Session
from pco_python_sdk.errors import RequestFailedError
from pco_python_sdk.settings import Settings


class Client(AbstractClient):
    """An HTTP Client implementation of the AbstractClient. Handles auth and making requests to
    the planning center api.
    """

    def __init__(self, settings: Settings = Settings(), session: Session = Session()):
        self.settings = settings
        self.session = session
        self.token = "something_here"

    def request(
        self,
        verb: str,
        endpoint: str,
        query: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make a request to the API and returns the body of the response

        Args:
            verb (str):  get/post/patch
            endpoint (str): the specific endpoint to hit.
            query (Dict[str, str], optional): a query string to pass to the request. Defaults to {}.
            payload (Dict[str, Any], optional): a dict to include in the body of the request. Defaults to {}.
            headers (Dict[str, str], optional): any extra headers to include (do not include auth headers). Defaults to {}.

        Raises:
            RequestFailedError: will raise if the request failes. Includes a status_code attribute.

        Returns:
            Dict[str, Any]: parsed json body of the response.
        """
        url = f"{self.settings.base_url}/{endpoint}"
        body = json.dumps(payload) if payload else payload
        response = self.session.request(
            method=verb,
            url=url,
            params=query,
            json=body,
            headers=headers,
        )
        print(vars(response.request))
        print(response.text)
        if not response.ok:
            raise RequestFailedError(
                message="API Returned an Error", status_code=response.status_code
            )

        return response.json()  # TODO: Let's return an object here instead.
