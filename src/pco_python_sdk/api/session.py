from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from pco_python_sdk.settings import Settings


class Session(OAuth2Session):
    def __init__(self, settings: Settings = Settings()) -> None:
        self.settings = settings
        pco_client_id = self.settings.pco_client_id
        pco_client_secret = self.settings.pco_client_secret
        client = BackendApplicationClient(client_id=pco_client_id)
        super().__init__(client=client)  # type: ignore

        token_url = "https://api.planningcenteronline.com/oauth/token"
        self.fetch_token(  # type: ignore
            token_url=token_url,
            client_id=pco_client_id,
            client_secret=pco_client_secret,
        )
