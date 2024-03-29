FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app
RUN python3 -m venv /app/venv


# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml  /app/
RUN PATH=/app/accounting:$PATH
RUN poetry install
COPY ./ /app