from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  APP_NAME: str = "FastAPI Application"
  DOCS_URL: str | None = None
  REDOC_URL: str | None = None
  OPENAPI_URL: str = "/openapi.json"
  SCALAR_URL: str = "/scalar"

  DB_NAME: str = "postgres"
  DB_USER: str = "postgres"
  DB_PASSWORD: str = "postgres"
  DB_HOST: str = "localhost"
  DB_PORT: int = 5432

  # Connection string for SQLAlchemy
  # Merangkai semua informasi koneksi ke database
  # Contoh: postgresql://user:password@host:port/dbname
  # Gunakan format string untuk menggabungkan variabel-variabel di atas
  DB_CONNECTION_STR: str = (
      f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
  )

  class Config:
    env_file = ".env"
    extra = "ignore" # Ignore extra fields not defined in the model, agar tidak error jika ada field baru di .env

settings = Settings()
