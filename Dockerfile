FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY linkedin_strategist/ linkedin_strategist/

RUN pip install --no-cache-dir .

ENTRYPOINT ["linkedin-strategist"]
