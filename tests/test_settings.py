from pathlib import Path
from pco_python_sdk.settings import Settings


def test_default_settings_initialize():
    assert Settings().base_url == "https://api.planningcenteronline.com"


def test_override_settings_initialize():
    url = "http://blah.com"
    assert Settings(base_url=url).base_url == url


def test_env_file_loading(tmp_path: Path):
    client_id = "xyz"
    client_secret = "abc"
    env_path = tmp_path / ".env"
    env_path.write_text(
        f"PCO_CLIENT_ID={client_id}\n PCO_CLIENT_SECRET={client_secret}"
    )
    settings = Settings(_env_file=env_path)  # type: ignore
    assert settings.pco_client_id == client_id
    assert settings.pco_client_secret == client_secret
