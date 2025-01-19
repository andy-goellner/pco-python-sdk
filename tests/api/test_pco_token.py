from datetime import datetime
from typing import Any, Mapping
from freezegun import freeze_time
from planning_center_python.api.pco_token import PCOToken


@freeze_time("2025-01-19 11:00:00")
def test_pco_token_returns_expires_in():
    expiry = datetime.fromisoformat("2025-01-19T12:00:00").timestamp()
    expires_in = 3600  # seconds in an hour
    token = PCOToken({"expires_at": expiry})
    assert token.expires_in == expires_in


def test_pco_token_no_expires_at():
    token = PCOToken({})
    assert token.expires_in == 1


@freeze_time("2025-01-19 11:00:00")
def test_pco_token_as_dict():
    expiry = datetime.fromisoformat("2025-01-19T12:00:00").timestamp()
    expires_in = 3600  # seconds in an hour
    args: Mapping[str, Any] = {
        "access_token": "testtoken",
        "expires_at": expiry,
        "refresh_token": "refreshtoken",
        "scope": ["test_scope"],
    }
    expected_args: Mapping[str, Any] = {
        "access_token": "testtoken",
        "expires_at": expiry,
        "expires_in": expires_in,
        "refresh_token": "refreshtoken",
        "scope": ["test_scope"],
        "token_type": "bearer",
    }
    token = PCOToken(args)
    assert token.as_dict() == expected_args
