from unittest.mock import MagicMock
import pytest
from planning_center_python.api.credentials import Credentials
from planning_center_python.api.session import Session
from planning_center_python.errors import InvalidCredentialsError


def test_session_raises_if_no_token():
    invalid_creds = Credentials(client_id="foo", client_secret="bar")
    with pytest.raises(InvalidCredentialsError):
        Session(invalid_creds)


def test_session_initializes_oauth2(
    mock_oauth2: MagicMock, valid_credentials: Credentials
):
    Session(valid_credentials)
    url = "https://api.planningcenteronline.com/oauth/token"
    assert valid_credentials.pco_token is not None
    mock_oauth2.assert_called_once_with(
        valid_credentials.client_id,
        auto_refresh_url=url,
        token=valid_credentials.pco_token.as_dict(),
        auto_refresh_kwargs={
            "client_id": valid_credentials.client_id,
            "client_secret": valid_credentials.client_secret,
        },
        token_updater=valid_credentials.token_updater,
    )
