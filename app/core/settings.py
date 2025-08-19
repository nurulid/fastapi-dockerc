from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  APP_NAME: str = "FastAPI Application"
  DOCS_URL: str | None = None
  REDOC_URL: str | None = None
  OPENAPI_URL: str = "/openapi.json"
  SCALAR_URL: str = "/scalar"

  class Config:
    env_file = ".env"
    extra = "ignore" # Ignore extra fields not defined in the model, agar tidak error jika ada field baru di .env