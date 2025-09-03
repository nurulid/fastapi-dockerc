FROM ghcr.io/astral-sh/uv:python3.13-alpine
# sesuaikan dengan versi python (di pyproject.toml)

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["./bin/start.sh"]
# script yang akan dijalankan