#!/bin/sh
set -e # Exit on any error

echo "Running database migrations..."
uv run alembic upgrade head

echo "Starting application..."
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

# !! Penting !!
# Pastikan baris berikut ada di awal skrip:
#!/bin/sh -> harus paling awal, ini adalah shebang untuk menentukan interpreter yang digunakan
# set -e -> opsi ini membuat skrip berhenti jika ada perintah yang gagal

# shell script untuk run alembic upgrade head dan uvicorn
# Note: The above command will keep the container running, allowing you to access the FastAPI application at http://localhost:8000
# If you want to run this in the background, you can use `uv run uvicorn app.main:app --host 0.0.0 --port 8000 &`
# but this is not recommended for production use. Instead, consider using a process manager like Gunicorn or Uvicorn with multiple workers.