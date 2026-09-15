from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "Blockchain Market Status API"
    APP_ENV: Literal["development", "staging", "production"] = "development"

    # External API URLs
    LISK_API_URL: str
    COINGECKO_API_URL: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        extra="ignore"
    )

settings = Settings()
