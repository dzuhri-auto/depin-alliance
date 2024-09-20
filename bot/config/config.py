from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str
    API_KEY: str
    
    AUTO_OPEN_BOX: bool = False
    RESERVE_POINT: int = 100000
    AUTO_UPGRADE_SKILL: bool = True

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [5, 30]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
