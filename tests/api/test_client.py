from pco_python_sdk.api.http_client import HttpClient


class TestClient:
    client = HttpClient()

    def test_session_identity(self):
        print(HttpClient().session)
        assert HttpClient().session == HttpClient().session
