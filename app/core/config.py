from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    secret_key: str
    algorithm: str
    host: str  = "127.0.0.1"
    port: int = 8000
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utc-8"
    )

settings = Settings()