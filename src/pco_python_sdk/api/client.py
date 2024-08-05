import json
from pco_python_sdk.settings import Settings
from requests import Session


class Client:
    def __init__(self, settings: Settings = Settings(), session: Session = Session()):
        self.settings = settings
        self.session = session
        self.token = "something_here"

    def request(
        self,
        verb: str,
        endpoint: str,
        query: dict = {},
        payload: dict = {},
        headers: dict = {},
    ):
        url = f"{self.settings.base_url}/{endpoint}"
        self.session.request(
            method=verb,
            url=url,
            params=query,
            json=json.dumps(payload),
            headers=headers,
            auth=self.auth,
        )

    def dump_settings(self):
        return self.settings.model_dump()
