from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    base_url: str = "https://api.planningcenteronline.com"
    pco_client_id: str = ""
    pco_client_secret: str = ""
