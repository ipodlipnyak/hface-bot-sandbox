FROM python:3
#FROM huggingface/transformers-cpu
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY ./src/pyproject.toml /src/
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
COPY ./src/ /src/

CMD python3 main.py

