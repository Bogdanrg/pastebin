from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    UVICORN_PORT: int
    UVICORN_HOST: str
    BACKEND_PORT: int
    TITLE: str
    BUCKET_NAME: str

    model_config = SettingsConfigDict(env_prefix="APP_", env_file="../.env")


class HashServiceSettings(BaseSettings):
    SERVICE_NAME: str
    SERVICE_PORT: str
    SERVICE_URL: str

    model_config = SettingsConfigDict(env_prefix="HASH_", env_file="../.env")


class NginxSettings(BaseSettings):
    EXTERNAL_PORT: int
    INTERNAL_PORT: int

    model_config = SettingsConfigDict(env_prefix="NGINX_", env_file="../.env")


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    hash_service: HashServiceSettings = HashServiceSettings()
    postgres: NginxSettings = NginxSettings()


settings = Settings()
