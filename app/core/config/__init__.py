import logging
import sys
from typing import List

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret, CommaSeparatedStrings

from app.core.config.database import DB
from app.core.loggings import InterceptHandler

env = Config(".env")

TITLE = env("APP_TITLE", default="Fast Api")
API_PREFIX = "/api"
JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.1"
# DATABASE_URL: DatabaseURL = env("DB_CONNECTION", cast=DatabaseURL)
MAX_CONNECTIONS_COUNT: int = env("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = env("MIN_CONNECTIONS_COUNT", cast=int, default=10)

DEBUG: bool = env("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = env("SECRET_KEY", cast=Secret)

ALLOWED_HOSTS: List[str] = env(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="*",
)
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

SENTRY_DSN = env("SENTRY_DSN")
SQLALCHEMY_DATABASE_URI = DB.to_string()
