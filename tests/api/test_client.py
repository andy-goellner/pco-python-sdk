from pco_python_sdk.api.client import Client


class TestClient:
    client = Client()

    def test_session_identity(self):
        print(Client().session)
        assert Client().session == Client().session
