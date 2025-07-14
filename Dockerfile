# syntax=docker/dockerfile:1

FROM python:3.9-slim AS base

WORKDIR /app

FROM base AS builder

# Install system dependencies for pip packages (sentence-transformers, prophet, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /app/.venv

# Copy requirements and install dependencies
COPY --link IntelliSpendAI/requirements.txt ./requirements.txt
ENV PIP_CACHE_DIR=/root/.cache/pip
RUN --mount=type=cache,target=$PIP_CACHE_DIR \
    /app/.venv/bin/pip install -r requirements.txt

# Copy application code (excluding .env and venvs)
COPY --link IntelliSpendAI/ ./IntelliSpendAI/

FROM base AS final

# Create non-root user
RUN useradd -m appuser
USER appuser

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code from builder
COPY --from=builder /app/IntelliSpendAI /app/IntelliSpendAI

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "IntelliSpendAI.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
