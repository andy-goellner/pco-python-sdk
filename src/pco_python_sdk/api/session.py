from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from pco_python_sdk.api.credentials import Credentials
from pco_python_sdk.errors import InvalidCredentialsError

TOKEN_URL = "https://api.planningcenteronline.com/oauth/token"


class Session(OAuth2Session):
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

        if not credentials.pco_token and not credentials.access_code:
            raise InvalidCredentialsError(
                "Either PCO Token or Access Code must be provided"
            )

        pco_client_id = self.credentials.client_id
        pco_client_secret = self.credentials.client_secret

        if credentials.pco_token:
            scope = "people"
            client = BackendApplicationClient(client_id=pco_client_id, scope=scope)
            super().__init__(client=client)  # type: ignore

            token = self.fetch_token(  # type: ignore
                token_url=TOKEN_URL,
                client_id=pco_client_id,
                client_secret=pco_client_secret,
            )
            print(token)  # TODO: Remove this
            return

        if credentials.access_code:
            pass
            # TODO: implement the initial token fetch code
