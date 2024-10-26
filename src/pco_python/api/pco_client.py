from typing import Optional
from pco_python.api.abstract_http_client import AbstractHttpClient
from pco_python.api.credentials import Credentials
from pco_python.api.http_client import HttpClient
from pco_python.models.person import Person


class PCOClient(object):
    def __init__(
        self, credentials: Credentials, http_client: Optional[AbstractHttpClient] = None
    ) -> None:
        if http_client:
            self._http_client = http_client
        else:
            self._http_client = HttpClient(credentials=credentials)

        self.person = Person(self._http_client)
