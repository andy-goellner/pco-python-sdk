from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from pco_python_sdk.settings import Settings


class Session(OAuth2Session):
    def __init__(self, settings: Settings = Settings()) -> None:
        self.client = BackendApplicationClient(client_id=settings.pco_client_id)
        super().__init__(client=self.client)  # type: ignore
