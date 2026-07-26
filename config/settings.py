from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Research & Knowledge Assistant"
    DATABASE_URL: str = "sqlite:///./research_assistant.db"
    VECTOR_DB_DIR: str = "./data/vector_db"

    class Config:
        env_file = ".env"


settings = Settings()