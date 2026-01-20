from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str

    # Магия, которая читает файл .env
    model_config = SettingsConfigDict(env_file=".env")

# Создаем экземпляр, который будем импортировать везде
settings = Settings()