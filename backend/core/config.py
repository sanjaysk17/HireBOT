from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    MAILJET_API_KEY: str
    LLM_ENDPOINT: str
    JWT_SECRET: str
    REDIS_URL: str
    MAIL_SENDER_EMAIL: str
    APP_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
