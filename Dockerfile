FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY ./app /app

#FROM python:3.8.1-slim
#
#ENV PYTHONUNBUFFERED 1
#
#EXPOSE 8000
#WORKDIR /app
#
#
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends netcat && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#
#COPY poetry.lock pyproject.toml ./
#RUN pip install poetry==1.1 && \
#    poetry config virtualenvs.in-project true && \
#    poetry install --no-dev
#
#COPY . ./
#
#CMD poetry run alembic upgrade head && \
#    poetry run uvicorn --host=0.0.0.0 app.main:app
#sudo apt-get install python3-dev libmysqlclient-dev
#PYTHONPATH=. alembic -c alembic.ini revision --autogenerate -m "init"